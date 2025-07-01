# Contact-Book-Web-App
A Streamlit-based Contact Book with full CRUD, sorting, and smart UI features using SQLite and AgGrid.
![App Screenshot](https://github.com/Purgty/Contact-Book-Web-App/blob/main/assets/screenshots/homepage.png)

---

## 🚀 Features

- ➕ Add new contacts with input validation
Easily add a new contact with details like name, gender, age, address, and contact number. Input validations are handled for common errors.
<img src="assets/add_contact.png" alt="Add Contact" width="500"/>

- 📋 View all contacts in a table
Displays all saved contacts in a clean, scrollable table view.
<img src="assets/view_contacts.png" alt="View Contacts" width="500"/>

🔍 Search Contact
Search for a contact by their first name. Displays matching results in real time.
<img src="assets/search_contact.png" alt="Search Contact" width="500"/>

- ✏️ Edit existing contacts
Select a contact and update any of their details using the edit form.
<img src="assets/edit_contact.png" alt="Edit Contact" width="500"/>

- 🗑️ Delete contacts with confirmation
Select a contact and confirm deletion. Deleted records are removed permanently, and IDs are reassigned sequentially.
<img src="assets/delete_contact.png" alt="Delete Contact" width="500"/>

- 🔢 Sort Contacts
Sort the entire contact list by first name, last name, age, address, or contact. Changes are saved to the database.
<img src="assets/sort_contacts.png" alt="Sort Contacts" width="500"/>

- 🧠 Real-time UI with Streamlit + AgGrid

---

## 🖼️ UI Preview

### Add Contact Form
![Add Contact](images/add_contact.png)

### Sorted Contacts Preview
![Sorted View](images/sorted_contacts.png)

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [SQLite3](https://www.sqlite.org/index.html)
- [pandas](https://pandas.pydata.org/)
- [st_aggrid](https://github.com/PablocFonseca/streamlit-aggrid)

---

## 📁 Project Structure

📦 Contact Book/
├── app.py # Main Streamlit app
├── db.py # All database functions
├── contacts.db # SQLite database
├── images/ # Screenshots and images for README
├── README.md # Project documentation
└── requirements.txt # Python dependencies


---

## 🧑‍💻 Getting Started

### ✅ Prerequisites

Make sure you have Python 3.8+ installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

## Running the App
To run the application, open the terminal in your project directory and run the following command:

```bash
streamlit run app.py
```