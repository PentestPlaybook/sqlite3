import pandas as pd
import sqlite3

# Load data from CSV with a different encoding
data = pd.read_csv('commands.csv', encoding='ISO-8859-1')

# Connect to SQLite database
conn = sqlite3.connect('pen-testing.db')

# Create the table
conn.execute('''CREATE TABLE IF NOT EXISTS Commands (id INTEGER PRIMARY KEY, command_name TEXT, command_usage TEXT)''')

# Insert data into the table
data.to_sql('Commands', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
