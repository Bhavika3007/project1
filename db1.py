mport mysql.connector

try:
    db_connection = mysql.connector.connect(
        host="localhost",        
        user="root",            
        password="1234",        
        database="db1" 
    )
    cursor = db_connection.cursor()

    while True:
        print("\nSelect an option:")
        print("1. Insert student details")
        print("2. Delete student details")
        print("3. Update student details")
        print("4. Display all students")
        print("5. Display all students in ascending order of name")
        print("6. Display students based on city 'Mumbai'")
        print("7. Display students with date of birth after '2000-01-01'")
        print("8. Exit")
       
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            student_id = int(input("Enter student ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            city = input("Enter city: ")
           
            insert_query = """
            INSERT INTO student (student_id, first_name, last_name, email, date_of_birth, city)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (student_id, first_name, last_name, email, date_of_birth, city))
            db_connection.commit()
            print("Student details inserted successfully!")

        elif choice == '2':
            student_id = int(input("Enter student ID to delete: "))  
            delete_query = "DELETE FROM student WHERE student_id = %s"
            cursor.execute(delete_query, (student_id,))
            db_connection.commit()
            print(f"Student with ID {student_id} has been deleted successfully!")

        elif choice == '3':
            student_id_to_update = int(input("Enter student ID to update details: "))
            new_first_name = input("Enter new first name: ")
            new_last_name = input("Enter new last name: ")
            new_email = input("Enter new email: ")
            new_city = input("Enter new city: ")
           
            update_query = """
            UPDATE student
            SET first_name = %s, last_name = %s, email = %s, city = %s
            WHERE student_id = %s
            """
            cursor.execute(update_query, (new_first_name, new_last_name, new_email, new_city, student_id_to_update))
            db_connection.commit()
            print(f"Details for student with ID {student_id_to_update} have been updated.")

        elif choice == '4':
            cursor.execute("SELECT * FROM student")
            students = cursor.fetchall()
            print("\nAll Students:")
            for student in students:
                print(student)

        elif choice == '5':
            cursor.execute("SELECT * FROM student ORDER BY first_name ASC")
            students = cursor.fetchall()
            print("\nStudents in Ascending Order of Name:")
            for student in students:
                print(student)

        elif choice == '6':
            cursor.execute("SELECT * FROM student WHERE city = 'Mumbai'")
            students = cursor.fetchall()
            print("\nStudents from 'Mumbai' city:")
            for student in students:
                print(student)

        elif choice == '7':
            cursor.execute("SELECT * FROM student WHERE date_of_birth > '2000-01-01'")
            students = cursor.fetchall()
            print("\nStudents born after '2000-01-01':")
            for student in students:
                print(student)

        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if db_connection:
        db_connection.close()
