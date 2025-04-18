import mysql.connector

try:
    # Connect without specifying the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Akh2006@nidhi"
    )
    cursor = conn.cursor()
    print("Connected to MySQL successfully!")

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management")
    print("Database 'hotel_management' is ready!")

    # Reconnect to the newly created database
    conn.database = "hotel_management"

    # Create table for storing traveler details
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS travelers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        aadhar_number VARCHAR(12),
        phone_number VARCHAR(10),
        check_in DATETIME,
        check_out DATETIME
    )
    ''')
    print("Table 'travelers' is ready!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    


def add_traveler():
    """Function to add a traveler's details to the database."""
    name = input("Enter traveler's name: ")
    age = int(input("Enter traveler's age: "))
    aadhar_number = input("Enter traveler's Aadhar card number: ")
    phone_number = input("Enter traveler's phone number: ")
    check_in = input("Enter check-in date and time (YYYY-MM-DD HH:MM:SS): ")
    check_out = input("Enter check-out date and time (YYYY-MM-DD HH:MM:SS): ")

    try:
        cursor.execute('''
        INSERT INTO travelers (name, age, aadhar_number, phone_number, check_in, check_out)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (name, age, aadhar_number, phone_number, check_in, check_out))
        conn.commit()
        print("Traveler's details added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def view_travelers():
    """Function to view all traveler details from the database."""
    try:
        cursor.execute("SELECT * FROM travelers")
        rows = cursor.fetchall()
        if rows:
            print("\nTraveler Details:")
            for row in rows:
                print(
                    f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Aadhar: {row[3]}, Phone: {row[4]}, Check-In: {row[5]}, Check-Out: {row[6]}")
        else:
            print("No traveler records found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Update Main Menu
while True:
    print("\nHotel Management System")
    print("1. Add Traveler Details")
    print("2. View Traveler Details")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_traveler()
    elif choice == "2":
        view_travelers()
    elif choice == "3":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
cursor.close()
conn.close()
