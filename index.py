class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts found.")
    def search_contact(self, search_name):
        found_contacts = []
        for contact in self.contacts:
            if search_name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print("Found Contacts:")
            for index, contact in enumerate(found_contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No matching contacts found.")
def main():
    my_contact_book = ContactBook()
    # Adding some initial contacts
    my_contact_book.add_contact(Contact("John Doe", "1234567890", "john@example.com"))
    my_contact_book.add_contact(Contact("Alice Smith", "9876543210", "alice@example.com"))
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            my_contact_book.add_contact(Contact(name, phone_number, email))
            print("Contact added successfully!")
        elif choice == "2":
            my_contact_book.display_contacts()
        elif choice == "3":
            search_name = input("Enter name to search: ")
            my_contact_book.search_contact(search_name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
