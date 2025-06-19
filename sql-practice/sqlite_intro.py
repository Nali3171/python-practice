import sqlite3

# Connect to (or create) a database file
conn = sqlite3.connect("company.db")  # creates file locally
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
)
''')

# Insert data (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM employees")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO employees (id, name, dept_id) VALUES (?, ?, ?)", [
        (1, 'Alice', 1),
        (2, 'Bob', 2),
        (3, 'Charlie', None),
        (4, 'Diana', 4)
    ])

    cursor.executemany("INSERT INTO departments (dept_id, dept_name) VALUES (?, ?)", [
        (1, 'HR'),
        (2, 'Engineering'),
        (3, 'Marketing')
    ])

conn.commit() #this saves chnages

results = cursor.fetchall()
for row in results:
    print(row)

# Close connection
conn.close()


#Challenges:
# basic inner join: get a list of employees and their departrment names
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;


#LEFT join query: all employees even without departments
SELECT e.name, d.dept_name
From emplyees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;


