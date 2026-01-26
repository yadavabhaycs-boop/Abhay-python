import sqlite3
connection = sqlite3.connect("student.db")
print(connection.total_changes)
