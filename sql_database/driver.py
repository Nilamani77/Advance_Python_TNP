import mysql.connector as myconn

mydb=myconn.connect(
    host="localhost",
    user="root",
    password="Nk12345@"
)

print("connected successfully")

mycursor=mydb.cursor()


mycursor.execute("CREATE DATABASE IF NOT EXISTS clg")

mycursor.execute("USE clg")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)
""")

data = [
    (1, "Rahul", 85),
    (2, "Priya", 90),
    (3, "Amit", 78),
    (4, "Sneha", 88),
    (5, "Rohit", 76),
    (6, "Anjali", 92),
    (7, "Karan", 80),
    (8, "Pooja", 87)
]

mycursor.executemany("INSERT INTO students VALUES (%s, %s, %s)", data)

mydb.commit()

print("Database, table, and data created successfully!")

mycursor.execute("SELECT * FROM students")

for row in mycursor:
    print(row)

