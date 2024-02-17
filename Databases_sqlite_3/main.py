import sqlite3


# Query The DB and Return All Records
def show_all():
    # Connection....
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    # Printing Data
    c.execute("SELECT rowid,* FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)

    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()


def add_one(first, last, email):
    # Connection....
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def delete_one(id):
    # Connection....
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    # Deleting
    c.execute(f"DELETE FROM customers WHERE rowid = (?)", id)
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def add_more(lst):
    # Connection....
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", lst)
    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def email_lookup(email):
    # Connection....
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    # Displaying
    c.execute(f"SELECT * FROM customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)

    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()
# NULL
# INTEGER
# REAL
# TEXT
# BLOB
