def phone_book_app():
   contacts={}
   while True:
      print("\nPhone Book Application")
      print("\n1. Add Contact")
      print("\n2. View Contacts")
      print("\n3. Search Contact")
      print("\n4. Delete Contact")
      print("\n5. Exit")
      choice = input("\nEnter your choice: ")

      if choice=='1':
        name=input("\nEnter contact name: ")
        phone=input("\nEnter contact phone number: ")
        contacts[name]=phone
        print(f"\nContact {name} added successfully.")
      elif choice=='2':
         if not contacts:
            print("\nNo contacts found.")
         else:
            print("\nContacts List:")
            for name, number in contacts.items():
               print(f"{name}: {number}")
      elif choice=='3':
            name_search=input("\nEnter contact name to search: ")
            if name_search in contacts:
               print(f"\nName:{name_search}, Phone {contacts[name_search]}")        
            else:   
               print("Contact '{name_search}' not found.")
      elif choice=="4":
            name_del=input("\nEnter contact name to delete: ")
            if name_del in contacts:
               del contacts[name_del]
               print(f"\nContact '{name_del}' deleted successfully.")
            else:
               print(f"\nContact '{name_del}' not found.")
      elif choice=='5':
            print("\nExiting Phone Book Application.")
            break
      else:
          print("\nInvalid choice. Please try again.")
if __name__ == "__main__":
    phone_book_app()