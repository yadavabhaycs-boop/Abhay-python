import sqlite3

# Connect to database
connection = sqlite3.connect("Student.db")
print("Total changes before:", connection.total_changes)

cursor = connection.cursor()

# Create table (IF NOT EXISTS to avoid error)
cursor.execute("""
CREATE TABLE IF NOT EXISTS cs (
    roll_no INT,
    name VARCHAR,
    email VARCHAR,
    course VARCHAR
)
""")

# Insert data
cursor.execute("""
INSERT INTO cs VALUES (123, 'ABHAY', 'YADAVABHAYCS252614@GMAIL.COM', 'CS')
""")

print("Data insert successfully")

# Commit changes
connection.commit()

# Fetch data
row = cursor.execute(
    "SELECT roll_no, name, email, course FROM cs"
).fetchall()

print(row)

# Close connection
connection.close()
