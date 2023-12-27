from db import connect_to_mysql
from auth import *

def signIn():
    cnx = connect_to_mysql()

    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            print("Welcome to Netflix. Let's sign you in.")

            while(True):
                email = input("Insert your email: ")
                password = input("Insert your password: ")

                result = cursor.execute("SELECT * FROM cuenta")
                rows = cursor.fetchall()

                for row in rows:
                    emailDB = row[0]
                    passwordDB = row[1]
                    if(emailDB == email and passwordDB == password):
                        return True
                print("Invalid credentials. Try Again")

        cnx.close()
    else:
        print("Could not connect")


if signIn():
    while(True):
        print("1. Movies")
        print("2. Series")
        selection = int(input("Select option: "))

        cnx = connect_to_mysql()

        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                if(selection == 1):
                    print("\nPELICULAS")
                    movies = cursor.execute("SELECT * FROM pelicula")
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row[2])
                elif(selection == 2):
                    print("\nSERIES")
                    series = cursor.execute("SELECT * FROM serie")
                    rows = cursor.fetchall()
                    for row in rows:
                        print(row[2])

            cnx.close()
        else:
            print("Could not connect")
