import sqlite3

DB_NAME = "contacts.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS member (
            mem_id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age TEXT,
            address TEXT,
            contact TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_member(firstname, lastname, gender, age, address, contact):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO member (firstname, lastname, gender, age, address, contact)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (firstname, lastname, gender, age, address, contact))
    conn.commit()
    conn.close()

def get_members(order_by="lastname"):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM member ORDER BY {order_by} ASC")
    data = cursor.fetchall()
    conn.close()
    return data

def delete_member(mem_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM member WHERE mem_id = ?", (mem_id,))
    conn.commit()
    conn.close()

def update_member(mem_id, firstname, lastname, gender, age, address, contact):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE member
        SET firstname = ?, lastname = ?, gender = ?, age = ?, address = ?, contact = ?
        WHERE mem_id = ?
    """, (firstname, lastname, gender, age, address, contact, mem_id))
    conn.commit()
    conn.close()

def search_member_by_firstname(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM member WHERE firstname = ?", (name,))
    data = cursor.fetchall()
    conn.close()
    return data

def sort_table(preview_data):
    conn = connect()
    cursor = conn.cursor()

    # Drop and recreate table (preserving sort)
    cursor.execute("DROP TABLE IF EXISTS member_sorted_temp")
    cursor.execute("""
        CREATE TABLE member_sorted_temp (
            mem_id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age TEXT,
            address TEXT,
            contact TEXT
        )
    """)
    for row in preview_data:
        cursor.execute("""
            INSERT INTO member_sorted_temp (firstname, lastname, gender, age, address, contact)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (row[1], row[2], row[3], row[4], row[5], row[6]))
    # Replace old table with new one
    cursor.execute("DROP TABLE member")
    cursor.execute("ALTER TABLE member_sorted_temp RENAME TO member")
    conn.commit()
    conn.close()

def reassign_ids():
    conn = connect()
    cursor = conn.cursor()

    # Step 1: Get current members (excluding ID)
    cursor.execute("SELECT firstname, lastname, gender, age, address, contact FROM member")
    rows = cursor.fetchall()

    # Step 2: Drop old table
    cursor.execute("DROP TABLE IF EXISTS member")

    # Step 3: Recreate the table
    cursor.execute("""
        CREATE TABLE member (
            mem_id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age TEXT,
            address TEXT,
            contact TEXT
        )
    """)

    # Step 4: Insert data back
    cursor.executemany("""
        INSERT INTO member (firstname, lastname, gender, age, address, contact)
        VALUES (?, ?, ?, ?, ?, ?)
    """, rows)

    conn.commit()
    conn.close()