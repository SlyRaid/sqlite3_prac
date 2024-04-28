import sqlite3


def add_tables():
    connect.execute("""
        CREATE TABLE IF NOT EXISTS students 
        (id          INTEGER       PRIMARY KEY AUTOINCREMENT ,
        name         TEXT,
        age          INTEGER)""")

    connect.execute("""
        CREATE TABLE IF NOT EXISTS grades 
        (id         INTEGER        PRIMARY KEY AUTOINCREMENT,
        student_id  INTEGER,
        subject     TEXT,
        grade       REAL,
        FOREIGN KEY (student_id) REFERENCES students(id))""")


class University:

    def __init__(self, name):
        self.name = name
        self.con = sqlite3.connect('students.db')
        self.cur = self.con.cursor()

    def add_student(self, name, age):
        with self.con:
            self.cur.execute("PRAGMA foreign_key = ON")
            self.cur.execute(""f"INSERT INTO students (name, age) VALUES ('{name}', '{age}')""")
            self.con.commit()

    def add_grade(self, student_id, subject, grade):
        with self.con:
            self.cur.execute("PRAGMA foreign_key = ON")
            self.cur.execute(
                ""f"INSERT INTO grades (student_id, subject, grade) VALUES ('{student_id}', '{subject}', '{grade}')""")
            self.con.commit()

    def get_students(self, subject=None):
        with self.con:
            if subject is None:
                cursor = self.cur.execute(
                    ""f"SELECT students.name, students.age, subject, grade FROM students JOIN grades ON "
                    f"students.id = grades.student_id""")
            else:
                cursor = self.cur.execute(
                    f"SELECT students.name, students.age, subject, grade FROM students JOIN grades ON "
                    f"students.id = grades.student_id WHERE subject = '{subject}'")
            self.con.commit()
            return cursor.fetchall()


with sqlite3.connect('students.db') as connect:
    connect.cursor()
    add_tables()
    connect.commit()

u1 = University('Urban')

# u1.add_student('Ivan', 26)  # id - 1
# u1.add_student('Ilya', 24)  # id - 2
# u1.add_student('Raze', 28)  # id - 3
# u1.add_student('Sova', 33)  # id - 4
#
# u1.add_grade(1, 'Python', 4.8)
# u1.add_grade(2, 'PHP', 4.3)
# u1.add_grade(3, 'Python', 4.5)
# u1.add_grade(4, 'Java', 3.1)

print(u1.get_students())
print(u1.get_students('Python'))
