# Title: 
Phone Book
# Estimated Time:
3 h
# Difficulty Level:
Beginner to Intermediate
2.15 Python Basics - Input-Output
# Topics:
Command line input and output. Using variables and control flow structures. Using while loops and lists. Reading and writing to files. 
# Scenario:
In this project, you will create a phone book using Python that will allow users to store and retrieve contact information. The system will have an initial menu where the user can select to store a new contact or retrieve data based on a contact name. The contact data will be stored in a file, and users will be able to search for contacts based on name substrings. Finally, the program will have an option for the user to quit the program.
## Feautures
1. Create a script that provides an initial menu for the user. The menu will have options for storing a new contact, retrieving data, and quitting the program.
2. When the user selects the option to store a new contact, the program will ask the user to enter the name and telephone number. Then, the program will confirm with the user if they want to save the data. The new data will be saved to a file.
3. If the user selects the option to retrieve data, the program will ask the user to enter a substring of the contact name. The program will then search for all contacts whose names contain the given substring, and print out the names and phone numbers of the relevant contacts.
4. The initial menu will also provide an option for the user to quit the program by entering 'q'.
5. The program will handle errors gracefully. For example, if the user enters an invalid input, the program will print a message and ask for input again.
6. The contact data will be stored in a file. The program will read from and write to this file.
## Use Case
1. User selects to store new contact:
   - User enters name: John Smith
   - User enters telephone number: 555-1234
   - Program confirms: "Save contact John Smith with phone number 555-1234? (y/n)"
   - User enters "y"
   - Program saves data to file and returns to initial menu.
2. User selects to retrieve data:
   - User enters substring of name: "Smith"
   - Program finds contacts whose names contain the substring "Smith":
   - John Smith: 555-1234
   - Sarah Smith: 555-5678
   - Program returns to initial menu.
3. User selects to quit:
   - Program terminates.












