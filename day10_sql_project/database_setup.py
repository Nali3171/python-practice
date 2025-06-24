import sqlite3

def setup_database():
    conn = sqlite3.connect("shop.db")  # creates shop.db in the folder
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product TEXT,
        price REAL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    # Insert sample data
    cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com")
    ])

    cursor.executemany('INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?)', [
        (1, "Laptop", 1200),
        (1, "Mouse", 25),
        (2, "Keyboard", 75),
        (3, "Monitor", 200)
    ])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
