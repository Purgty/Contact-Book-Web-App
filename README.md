# Contact-Book-Web-App
A Streamlit-based Contact Book with full CRUD, sorting, and smart UI features using SQLite and AgGrid.

<img src="https://github.com/Purgty/Contact-Book-Web-App/blob/main/screenshots/homepage.png" alt="Add Contact" width="900"/>
---

## Features

- ➕ **Add new contacts with input validation**  
Easily add a new contact with details like name, gender, age, address, and contact number. Input validations are handled for common errors.

<p align="center">
  <img src="https://github.com/Purgty/Contact-Book-Web-App/blob/main/screenshots/add.png" alt="Add Contact" width="500"/>
</p>

- 📋 **View all contacts in a table**  
Displays all saved contacts in a clean, scrollable table view.

- 🔍 **Search Contact**  
Search for a contact by their first name. Displays matching results in real time.

<p align="center">
  <img src="https://github.com/Purgty/Contact-Book-Web-App/blob/main/screenshots/search.png" alt="Search Contact" width="500"/>
</p>

- ✏️ **Edit existing contacts**  
Select a contact and update any of their details using the edit form.

<p align="center">
  <img src="https://github.com/Purgty/Contact-Book-Web-App/blob/main/screenshots/edit.png" alt="Edit Contact" width="500"/>
</p>

- 🗑️ **Delete contacts with confirmation**  
Select a contact and confirm deletion. Deleted records are removed permanently, and IDs are reassigned sequentially.

<p align="center">
  <img src="https://github.com/Purgty/Contact-Book-Web-App/blob/main/screenshots/delete.png" alt="Delete Contact" width="500"/>
</p>

- 🔢 **Sort Contacts**  
Sort the entire contact list by first name, last name, age, address, or contact. Changes are saved to the database.

<p align="center">
  <img src="https://github.com/Purgty/Contact-Book-Web-App/blob/main/screenshots/sort1.png" alt="Sort Contacts 1" width="500"/>
</p>

<p align="center">
  <img src="https://github.com/Purgty/Contact-Book-Web-App/blob/main/screenshots/sort2.png" alt="Sort Contacts 2" width="500"/>
</p>

- 🧠 **Real-time UI with Streamlit + AgGrid**
---

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [SQLite3](https://www.sqlite.org/index.html)
- [pandas](https://pandas.pydata.org/)
- [st_aggrid](https://github.com/PablocFonseca/streamlit-aggrid)

---

## 📁 Project Structure

Contact Book/
├── app.py # Main Streamlit app
├── db.py # All database functions
├── contacts.db # SQLite database
├── screenshots/ # Screenshots and images for README
├── README.md # Project documentation
└── requirements.txt # Python dependencies


---

## 🧑‍💻 Getting Started

### ✅ Prerequisites

Make sure you have Python 3.8+ installed. Then install dependencies:
```bash
pip install -r requirements.txt
```

### Setup
To setup this project, start by cloning this repository
```bash
git clone https://github.com/your-username/contact-book.git
cd contact-book
```

Create a Virtual Environment
Open the directory and run these commands in it.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Running the App
To run the application, open the terminal in your project directory and run the following command:

```bash
streamlit run app.py
```
