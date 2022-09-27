import mysql.connector as my

con = my.connect(host="localhost",  user="root", password="admin", database = "pythondb")
cur = con.cursor()


def insert(name, age):
    try:
        query = '''INSERT INTO Students (name, age) VALUES ('{0}',{1})'''.format(name, age)
        cur.execute(query)
        con.commit()
        print("Student Inserted Successfully")
    except:
        con.rollback()
        print("Couldn't Insert Student")


def update(roll, name, age):
    try:
        query = '''UPDATE Students SET name='{0}', age={1} WHERE roll={2}'''.format(name, age, roll)
        cur.execute(query)
        con.commit()
        print("Record Updated Successfully")
    except:
        con.rollback()
        print("Couldn't Update the data")


def delete(roll):
    try:
        query ='''DELETE FROM Students WHERE roll={0}'''.format(roll)
        cur.execute(query)
        print("Student with roll no. {0} deleted Successfully".format(roll))
    except:
        con.rollback()
        print("Student couldn't be deleted")


def display():
    try:
        cur.execute("SELECT * FROM pythondb.Students")
        results = cur.fetchall()
        print("No. | Name | Age")
        for i in results:
            roll = i[0]
            name = i[1]
            age = i[2]
            print(roll, "\'", name, "\'", age)
    except:
        print("Couldn't display the data")


print("Welcome to CRUD Application")
print("")
print("1.) Insert Student               2.)  Update Student")
print("3.) Delete Student                4.)  Display Student")
print("5.) Exit ")
print("")

while True:
    option = int(input("Choose any of the option above >> "))

    if option == 1:
        nm = input("Enter the name of the student >> ")
        ag = int(input("Enter the age of the Student >> "))
        insert(nm, ag)
    elif option == 2:
        rl = int(input("Enter the Roll Number of the Student >> "))
        nm = input("Enter the new name of the student >> ")
        ag = int(input("Enter the new age of the student >> "))
        update(rl, nm, ag)
    elif option == 3:
        rl = int(input("Enter the Roll NUmber of the student >> "))
        delete(rl)
    elif option == 4:
        display()
    elif option == 5:
        print("It was a pleasure doing crud with you")
        break
    else:
        print("Choose correct option")
        continue

cur.close()