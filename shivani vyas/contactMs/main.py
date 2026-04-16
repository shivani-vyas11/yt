# Contact Management System using Dictionary

contacts = {
    "Rahul": {"phone": "9876543210", "email": "rahul@gmail.com"},
    "Anita": {"phone": "9123456789", "email": "anita@gmail.com"}
}

def view_contacts():
    print("\n----- CONTACT LIST -----")
    if not contacts:
        print("No contacts available.")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        print("Contact updated successfully.")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found!")

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        print("Exiting Contact Management System.")
        break
    else:
        print("Invalid choice. Try again.")