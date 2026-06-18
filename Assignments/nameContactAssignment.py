class ContactManager:
    def __init__(self):
        self.contacts = []
    def validate_phone(self, phone):
        allowed = "0123456789-+ "

        for char in phone:
            if char not in allowed:
                return False
        return True

    def validate_email(self, email):
        if email == "":
            return True
        return "@" in email and "." in email

    def add_contact(self, name, phone, email=""):
        if not self.validate_phone(phone):
            print("Error: Invalid phone number. Use only digits, '+' and '-'.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email address.")
            return

        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        print("Contact added successfully!")

    def view_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                print("\nContact Details")
                print("----------------")
                print("Name :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                return

        print("Contact not found.")

    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():

                if new_phone:
                    if not self.validate_phone(new_phone):
                        print("Error: Invalid phone number.")
                        return
                    contact["phone"] = new_phone

                if new_email is not None:
                    if not self.validate_email(new_email):
                        print("Error: Invalid email address.")
                        return
                    contact["email"] = new_email

                print("Contact updated successfully!")
                return

        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return

        print("Contact not found.")

    def search_contacts(self, keyword):
        results = []

        for contact in self.contacts:
            if (keyword.lower() in contact["name"].lower() or
                keyword.lower() in contact["phone"].lower() or
                keyword.lower() in contact["email"].lower()):
                results.append(contact)

        if not results:
            print("No matching contacts found.")
            return

        print("\nSearch Results")
        print("-" * 50)

        for i, contact in enumerate(results, start=1):
            print(f"{i}. Name : {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print("-" * 50)

    def list_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("\nAll Contacts")
        print("-" * 50)

        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name : {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print("-" * 50)

def main():
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")

            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter contact name: ")
            manager.view_contact(name)

        elif choice == "3":
            name = input("Enter contact name to update: ")

            new_phone = input("Enter new phone (leave blank to skip): ")
            if new_phone == "":
                new_phone = None

            new_email = input("Enter new email (leave blank to skip): ")
            if new_email == "":
                new_email = None

            manager.update_contact(name, new_phone, new_email)

        elif choice == "4":
            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)

        elif choice == "5":
            keyword = input("Enter name, phone, or email to search: ")
            manager.search_contacts(keyword)

        elif choice == "6":
            manager.list_all_contacts()

        elif choice == "7":
            print("Exiting Contact Manager...")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")


# Run Program
if __name__ == "__main__":
    main()