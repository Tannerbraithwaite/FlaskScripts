import sqlite3

conn = sqlite3.connect('/Users/tannerbraithwaite/github/python_scripts/WebPrograms/example.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")




def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.4, 'Expert')")
    conn.commit()

def enter_dynamic_data():
    lang = input("What Lanuage?: ")
    version = float(input("What version?: "))
    skill = input("What skill level?: ")
    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, version, skill))
    conn.commit()


def read_from_database():
    What_skill = input("What skill level are you looking for? ")
    What_language = input("What language?: ")

    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"
    for row in c.execute(sql, [(What_skill), (What_language)]):
        print(row)
        print(row[0])
    conn.commit()

##Also works with DELETE
def update_database():
    sql = "UPDATE example SET Skill = 'the bestest' WHERE skill = 'Beginner' "
    c.execute(sql)
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)
    conn.commit()


def read_from_database_with_limit():
    sql = "SELECT * FROM example LIMIT 2"
    c.execute(sql)
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)
    conn.commit()



conn.close()
