# Contact-Book-Web-App
A Streamlit-based Contact Book with full CRUD, sorting, and smart UI features using SQLite and AgGrid.
![App Screenshot](https://github.com/Purgty/Contact-Book-Web-App/blob/main/assets/screenshots/homepage.png)

---

## 🚀 Features

- ➕ Add new contacts with input validation
- 📋 View all contacts in a table
- ✏️ Edit existing contacts
- 🗑️ Delete contacts with confirmation
- 🔍 Search by first name
- 🔢 Sort by fields like name, age, address
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