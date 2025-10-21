contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added!")

def view_contacts():
    for name, info in contacts.items():
        print(f"\n{name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Found: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add  2. View  3. Search  4. Delete  5. Exit")
    ch = input("Choose: ")

    if ch == '1': add_contact()
    elif ch == '2': view_contacts()
    elif ch == '3': search_contact()
    elif ch == '4': delete_contact()
    elif ch == '5': break
    else: print("Invalid choice.")