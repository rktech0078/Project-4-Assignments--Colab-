phonebook = {}

while True:
    
    print("\nSimple Phone-book Programme")
    print("1. Add New Number")
    print("2. Search Number")
    print("3. Phonebook List")
    print("4. Exit")
    
    user_input = int(input("Select your options (1-4): "))
    
    if user_input == 1:
        
        name = input("Enter your Name: ")
        number = input("Enter your phone number: ")
        phonebook[name] = number
        print(f"{name}: {number} is saved in your phonebook")
        
    elif user_input == 2:
        
        search = input("Enter Name for searching...")
        
        if search in phonebook:
            print(f"📞 {name} number: {phonebook[name]}")
        else:
            print("This number dosen't exist in your phonebook")
            
    elif user_input == 3:
        
        print("\nPhone Book List\n")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
            
    elif user_input == 4:
        print("Programme successfully closed....")
        break
    
    else:
        print("Wrong Command!")
    