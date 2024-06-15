import sqlite3

# Connect to SQLite database (this will create the file if it does not exist)
conn = sqlite3.connect('pen-testing.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS Commands")

# Create table as per requirement
cursor.execute('''
CREATE TABLE Commands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command_name TEXT,
    command_usage TEXT
)
''')

# Commit your changes in the database
conn.commit()

# Close the connection
conn.close()
