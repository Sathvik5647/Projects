def addNumber(contacts):
    y=True
    while (y):
        person=input("Enter the name of the person: ")
        number=input("Enter the number: ")
        if (len(number)!=10):
            print("Number is not of the right length")
            continue
        contacts[person]=number
        x=input("Do you wish to add another contact(Y/N): ")
        x=x.upper()
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break
def updateNumber(contacts):
    y=True
    if (len(contacts)==0):
        print("You need to add contacts first")
        x=input("Do you wish to add a number: (Y/N): " )
        x=x.upper()
        if (x=="Y"):
            addNumber(contacts)
        elif (x=="N"):
            print("Exiting contactbook")
            return
        else:
            print("You did not enter a valid input")
            return
    while (y):
        person=input("Enter the name of the person's contact you want to edit: ")
        contacts[person]=input("Enter the number: ")
        print(f"{person} has been updated to {contacts[person]}")
        x=input("Do you wish to edit more(Y/N): ")
        x=x.upper()
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break

def deleteNumber(contacts):
    if (len(contacts)==0):
        print("There are no contacts to delete")
        x=input("Do you wish to add a number: (Y/N): " )
        x=x.upper()
        if (x=="Y"):
            addNumber(contacts)
        elif (x=="N"):
            return
        else:
            print("You did not enter a valid input")
            return
    y=True
    while (y):
        deleter=input("Whose contact do you wish to delete: ")
        print(f"{deleter} has been removed from the contactbook")
        del contacts[deleter]
        x=input("Do you wish to delete more(Y/N): ")
        x=x.upper()
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break

def searchNumber(contacts):
    if (len(contacts)==0):
        print("There are no contacts to search")
        x=input("Do you wish to add a number first?: (Y/N): " )
        x=x.upper()
        if (x=="Y"):
            addNumber(contacts)
        elif (x=="N"):
            return
        else:
            print("You did not enter a valid input")
            return
    y=True
    while (y):
        search=input("Whose number do you want to search: ")
        print(contacts[search])
        x=input("Do you wish to search more(Y/N): ")
        x=x.upper()
        if (x=="Y"):
            y=True
        elif (x=="N"):
            y=False
        else:
            print("Invalid input")
            break
contacts={}
print("Welcome to Contactbook")
z=True
while (z):
    print("Actions you can perform in the contactbook: ")
    print("1.Add a nummber")
    print("2.Update")
    print("3.Display all Contacts")
    print("4.Delete numbers")
    print("5.Search contacts")
    print("6.Exit the contactbook")
    x=int(input("Select an action ( 1 / 2 / 3 / 4 / 5 / 6 ): "))
    if (x==1):
        addNumber(contacts)
    elif (x==2):
        updateNumber(contacts)
    elif (x==3):
        print("Your contacts are : ",contacts)
    elif (x==4):
        deleteNumber(contacts)
    elif (x==5):
        searchNumber(contacts)
    elif (x==6):
        print("Exiting Contactbook....")
        break
    else:
        print("Did not enter a valid operation")
        break