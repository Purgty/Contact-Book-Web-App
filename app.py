import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import streamlit.components.v1 as components
import pandas as pd
from db import (
    create_table,
    add_member,
    get_members,
    delete_member,
    update_member,
    search_member_by_firstname,
    sort_table,
    reassign_ids,
)

st.set_page_config(page_title="Contact Manager", layout="wide")
st.markdown("<h1 style='text-align: center;'>📇 Contact Book System</h1>", unsafe_allow_html=True)
st.title(" ")
# Ensure database table exists
create_table()
# Default landing view - centered table of all records
data = get_members(order_by="mem_id")

if data:
    df = pd.DataFrame(data, columns=["ID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"])
    st.dataframe(df.reset_index(drop=True), use_container_width=True)
else:
    st.info("No contacts found. Please add a new contact using the sidebar.")

# Spacer
st.markdown("---")

# SIDEBAR ACTIONS
st.sidebar.header("Actions")
action = st.sidebar.radio("Choose Action", ["Add", "View", "Search", "Edit", "Delete", "Sort"])

# ADD CONTACT
if action == "Add":
    st.subheader("➕ Add New Contact")
    with st.form("add_form", clear_on_submit=True):  # clear_on_submit clears form after submit
        firstname = st.text_input("First Name")
        lastname = st.text_input("Last Name")
        gender = st.radio("Gender", ["Male", "Female", "Non-Binary"], index=None)
        age = st.text_input("Age")
        address = st.text_input("Address")
        contact = st.text_input("Contact Number")

        submitted = st.form_submit_button("Add Contact")

        if submitted:
            if not firstname.strip() or not lastname.strip():
                st.error("First name and last name are required.")
            elif gender is None:
                st.error("Please select a gender.")
            elif not age.isdigit() or int(age) <= 0:
                st.error("Age must be a positive number.")
            elif not contact.isdigit() or len(contact) < 10:
                st.error("Contact must be a valid number with at least 10 digits.")
            else:
                add_member(firstname, lastname, gender, age, address, contact)
                st.success("Contact added successfully!")
                st.rerun()  # resets form manually as well

# VIEW CONTACTS
elif action == "View":
    st.subheader("📋 All Contacts")
    data = get_members(order_by="mem_id")
    df = pd.DataFrame(data, columns=["ID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"])
    st.dataframe(df.reset_index(drop=True), use_container_width=True)

# SEARCH CONTACT
elif action == "Search":
    st.subheader("🔍 Search Contact by First Name")
    search = st.text_input("Enter First Name to Search")
    if st.button("Search"):
        results = search_member_by_firstname(search)
        df = pd.DataFrame(results, columns=["ID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"])
        if results:
            st.write("Result(s):")
            st.dataframe(df.reset_index(drop=True), use_container_width=True)
        else:
            st.warning("No matching contact found.")

# DELETE CONTACT
elif action == "Delete":
    st.subheader("🗑️ Delete Contacts")

    data = get_members(order_by="mem_id")
    if not data:
        st.warning("No contacts available.")
    else:
        import pandas as pd
        df = pd.DataFrame(data, columns=["ID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"])
        gb = GridOptionsBuilder.from_dataframe(df.reset_index(drop=True))
        gb.configure_selection("single", use_checkbox=True)  # FULL ROW selection
        grid_options = gb.build()

        grid_response = AgGrid(
            df,
            gridOptions=grid_options,
            update_mode=GridUpdateMode.SELECTION_CHANGED,
            allow_unsafe_jscode=False,
            height=400,
            theme='streamlit'
        )

        selected = grid_response["selected_rows"]
        selected_df = pd.DataFrame(selected)
        if not selected_df.empty:
            row = selected_df.iloc[0]  # selected is a list of dicts
            
            with st.expander(f"⚠️ Confirm deletion of {row['First Name']} {row['Last Name']}"):
                st.write("This action is irreversible.")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Yes, Delete"):
                        delete_member(int(row["ID"]))
                        st.success("Contact deleted successfully!")
                        reassign_ids()
                        st.rerun()
                with col2:
                    if st.button("❌ Cancel"):
                        st.session_state.grid_key = "grid" + str(int(st.session_state.grid_key[-1]) + 1)
                        st.rerun()


elif action == "Edit":
    st.subheader("✏️ Edit Contact")
    data = get_members()
    if data:
        df = pd.DataFrame(data, columns=["ID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"])
        unique_firstnames = df["First Name"].unique().tolist()
        selected_fname = st.selectbox("Select First Name to Edit", unique_firstnames)

        matches = df[df["First Name"] == selected_fname]

        if len(matches) == 1:
            selected_row = matches.iloc[0]
        elif len(matches) > 1:
            selected_row = matches.iloc[0]
            st.info(f"Multiple entries found for {selected_fname}. Editing the first match.")
        else:
            selected_row = None

        if selected_row is not None:
            with st.form("edit_form"):
                firstname = st.text_input("First Name", selected_row["First Name"])
                lastname = st.text_input("Last Name", selected_row["Last Name"])
                gender_index = ["Male", "Female", "Non-Binary"].index(selected_row["Gender"]) if selected_row["Gender"] in ["Male", "Female", "Non-Binary"] else 0
                gender = st.radio("Gender", ["Male", "Female", "Non-Binary"], index=gender_index)
                age = st.text_input("Age", str(selected_row["Age"]))
                address = st.text_input("Address", selected_row["Address"])
                contact = st.text_input("Contact", selected_row["Contact"])
                submitted = st.form_submit_button("Update Contact")
                if submitted:
                    update_member(selected_row["ID"], firstname, lastname, gender, age, address, contact)
                    st.success("Contact updated successfully!")
                    st.rerun()
    else:
        st.warning("No contacts available to edit.")

# SORT CONTACTS
elif action == "Sort":
    st.subheader("🔢 Sort Contacts")

    # Initial unsorted display
    st.markdown("### 📋 Current Records (Unsorted)")
    current_data = get_members(order_by="mem_id")
    df = pd.DataFrame(current_data, columns=["ID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"])
    st.dataframe(df.reset_index(drop=True), use_container_width=True)

    # Sorting preview
    sort_options = ["--Please select your sorting method--", "First Name", "Last Name", "Age", "Address", "Contact"]
    sort_field = st.selectbox("Choose sorting field", sort_options, index=0)
    if sort_field == "--Please select your sorting method--":
        st.warning("⚠️ Please select a valid sorting method.")
    else:
        sort_category = ""
        if sort_field == "First Name":
            sort_category = "firstname"
        elif sort_field == "Last Name":
            sort_category = "lastname"
        elif sort_field == "Age":
            sort_category = "age"
        elif sort_field == "Address":
            sort_category = "address"
        elif sort_field == "Contact":
            sort_category = "contact"
        preview_data = get_members(order_by=sort_category)
        st.dataframe(preview_data, use_container_width=True)

        # Save confirmation
        if st.button("✅ Confirm Sort and Save Order"):
            sort_table(preview_data)
            st.success("Records sorted and saved permanently.")
            st.rerun()