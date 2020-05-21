import random
import getpass

def admin_room_display():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    fhand = open("room.txt", "r")
    records = fhand.read().split('$')
    del records[-1]
    for record in records:
        attributes = record.split('|')
        print("ROOM NUMBER : ",attributes[1])
        print("NAME        : ",attributes[2])
        print("ADDRESS     : ",attributes[3])
        print("CHECK-IN    : ",attributes[4])
        print("CHECK-OUT   : ",attributes[5])
        print("ROOM-TYPE   : ",attributes[6])

        print("\n")

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def admin_hall_display():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    fhand = open("hall.txt", "r")
    records = fhand.read().split('$')
    del records[-1]
    for record in records:
        attributes = record.split('|')
        print("BOOKING NUMBER : ",attributes[1])
        print("NAME           : ",attributes[2])
        print("ADDRESS        : ",attributes[3])
        print("DATE           : ",attributes[4])
        print("PHONE          : ",attributes[5])
        print("HALL-TYPE      : ",attributes[6])
        print("\n")

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def admin_table_display():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    fhand = open("table.txt", "r")
    records = fhand.read().split('$')
    for record in records:
        attributes = record.split('|')
        try: 
            print("TABLE NUMBER : ",attributes[1])
            print("NAME         : ",attributes[2])
            print("ADDRESS      : ",attributes[3])
            print("PHONE        : ",attributes[4])
            print("PEOPLE COUNT : ",attributes[5])
            print("DATE         : ",attributes[6])
            print("\n")
        except:
            continue

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



def display_room():
    found = False
    key = input("Enter your UID: ")
    fhand = open("room.txt", "r")
    records = fhand.read().split('$')
    for record in records:
        attributes = record.split('|')
        temp = attributes[0]
        if(temp == key ):
            found = True
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


            print("ROOM NUMBER : ",attributes[1])
            print("NAME        : ",attributes[2])
            print("ADDRESS     : ",attributes[3])
            print("CHECK-IN    : ",attributes[4])
            print("CHECK-OUT   : ",attributes[5])
            print("ROOM-TYPE   : ",attributes[6])
            print("\n")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    if(not found):
        print("UID does not exist")

       

def book_room():
    name = input("Enter Customer Name:\n")
    addr = input("Enter Customer Address:\n")
    cin = input("Enter Check-in date:\n")
    cout = input("Enter Check-out date:\n")
    uid = random.randint(1000,9999)
 
    room_valid = False

    while not room_valid:
        print("Choose a room type\n")
        print("1.Type A [Single-bed room + Non AC] --> Rs.2500")
        print("2.Type B [Single-bed room + AC] --> Rs.3500")
        print("3.Type C [Double-bed room + Non AC]--> Rs.5000")
        print("4.Type D [Double-bed room + AC]--> Rs,6000")
        room_choice = int(input("Enter your choice: "))

        if(room_choice == 1):
            room = 'Type A'
            room_valid = True
        elif(room_choice == 2):
            room = 'Type B'
            room_valid = True
        elif(room_choice == 3):
            room = 'Type C'
            room_valid = True
        elif(room_choice == 4):
            room = 'Type D'
            room_valid = True
    print("You opted for: ", room)
    print("Your UID:  ",uid)

    fhand = open("rnumber.txt","r")
    room_number = int(fhand.read())
    fhand.close()
    fhand = open("rnumber.txt","w")
    print("your room number: ", room_number)
    new_room = str(room_number + 1)
    fhand.write(new_room)
    fhand.close()

    fhand = open("room.txt", "a+")
    buf = str(uid) +'|'+ str(room_number) +'|'+ name  +'|'+ addr  +'|'+ cin  +'|'+ cout +'|'+ room +'$'
    fhand.write(buf)
    fhand.close()




def room_modify():
    flag = False
    found = False
    uid = input("Enter UID : ")
    temp =list()
    fhand = open("room.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('$')
    for record in records:
        if record.startswith(uid):
            found = True
            items = record.split('|')
            while(True):
                print("1. Checkin Date\n2. Checkout Date")
                choice = int(input("what do you want to modify? "))
                if(choice == 1):
                    items[4] = input("Enter checkin date: ")
                    flag = True
                    print("Your details has been successfully modified\n")
                elif(choice == 2):
                    items[5] = input("Enter checkout date: ")
                    flag = True
                    print("Your details has been successfully modified\n")
                else:
                    print("Invalid entry, try again")
                    flag = False
                if(flag):
                    break
            buf = items[0] +"|"+ items[1] +"|"+ items[2] +"|"+ items[3] +"|"+ items[4] +"|"+ items[5] +"|"+ items[6]  +"$"
            temp.append(buf)
        else:
            temp.append(record)
    del temp[-1]
    fhand = open("room.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('$')
    if(not found):
        print("UID does not exist")
    

def room_delete():
    uid = input("Enter UID : ")
    deleted = False
    temp =list()
    fhand = open("room.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('$')
    del records[-1]
    for record in records:
        if record.startswith(uid):
            deleted = True
            continue
        else:
            temp.append(record)

    fhand = open("room.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('$')
    if deleted :
        print("Record was successfully deleted\n")
    else:
        print("Uid does'nt exist")


def room_sub_menu():
    print("\n\n1. Book room\n2. View Customer Details\n3. Delete Customer Details\n4. Modify Customer Details\n5. Go Back ")
    ch = int(input("Enter your choice: "))
    if(ch == 1):
        book_room()

    if(ch == 2):
        display_room()
    
    elif(ch == 3):
        room_delete()

    elif(ch == 4):
        room_modify()
    elif(ch == 5):
        return
    else:
        # print("Invalid choice...")
        return





def book_hall():
    hname = input("Enter Customer Name:\n")
    haddr = input("Enter customer address:\n")
    hdate = input("Enter the date:\n")
    hphone = input("Enter the phone number\n")
    huid = random.randint(1000, 9999)

    hall_valid = False

    while not hall_valid:
        print("Choose a Hall type\n")
        print("1.Mini Hall --> 10000")
        print("2.Maharani Hall --> 18000")
        print("3.Maharaja Hall --> 25000")

        hall_choice = int(input("Enter your choice: "))

        if (hall_choice == 1):
            hall = 'Mini Hall'
            hall_valid = True
        elif (hall_choice == 2):
            hall = 'Maharani Hall'
            hall_valid = True
        elif (hall_choice == 3):
            hall = 'Maharaja Hall'
            hall_valid = True
    print("You opted for ", hall)
    print("UID IS",huid)

    fhand = open("hbnumber.txt", "r")
    hall_number = int(fhand.read())
    fhand.close()
    fhand = open("hbnumber.txt", "w")
    print("your hall booking number: ", hall_number)
    new_hall = str(hall_number + 1)
    fhand.write(new_hall)
    fhand.close()

    fhand = open("hall.txt", "a+")
    buf = str(huid) + '|' + str(hall_number) + '|' + hname + '|' + haddr + '|' + hdate + '|' + hphone + '|' + hall + '$'
    fhand.write(buf)
    fhand.close()

def display_hall():
    found = False
    key = input("Enter your UID: ")
    fhand = open("hall.txt", "r")
    records = fhand.read().split('$')
    for record in records:
        attributes = record.split('|')
        temp = attributes[0]
        if(temp == key ):
            found = True
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("BOOKING NUMBER : ",attributes[1])
            print("NAME           : ",attributes[2])
            print("ADDRESS        : ",attributes[3])
            print("DATE           : ",attributes[4])
            print("PHONE          : ",attributes[5])
            print("HALL-TYPE      : ",attributes[6])
            print("\n")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    if(not found):
        print("UID does not exist")



def hall_delete():
    huid = input("Enter UID : ")
    deleted = False
    temp =list()
    fhand = open("hall.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('$')
    del records[-1]
    for record in records:
        if record.startswith(huid):
            deleted = True
            continue
        else:
            temp.append(record)
    # del temp[-1]

    fhand = open("hall.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('$')

    if deleted:
        print("Record was successfully deleted\n")
    else:
        print("Uid does'nt exist")



def hall_modify():
    flag = False
    found = False
    huid = input("Enter UID : ")
    temp =list()
    fhand = open("hall.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('$')
    for record in records:
        if record.startswith(huid):
            found = True
            items = record.split('|')
            while(True):
                print("1.Date\n")
                items[4] = input("enter the date")
                flag=True
                if(flag):
                    break
            buf = items[0] +"|"+ items[1] +"|"+ items[2] +"|"+ items[3] +"|"+ items[4] +"|"+ items[5] +"|"+ items[6]  +"$"
            temp.append(buf)
        else:
            temp.append(record)
    del temp[-1]
    fhand = open("hall.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('$')
    if(not found):
        print("UID does not exist")



def hall_sub_menu():
    print(
        "\n\n1. Register Customer\n2. View Customer Details\n3. Delete Customer Details\n4. Modify Customer Details\n5. Go Back ")
    ch = int(input("Enter your choice: "))
    if (ch == 1):
        book_hall()

    if (ch == 2):
        display_hall()

    elif (ch == 3):
        hall_delete()

    elif (ch == 4):
        hall_modify()

    elif (ch == 5):
        return
    else:
        print("This feature will be available soon...")
        return



def book_table():
    tname = input("Enter Customer Name:\n")
    taddr = input("Enter customer address:\n")
    tphone = input("Enter the phone number\n")
    tppl = input("Enter the no of people:\n")
    tdate = input("Enter the date:\n")
    tuid = random.randint(1000, 9999)
    print("UID is",tuid)

    fhand = open("tnumber.txt", "r")
    table_number = int(fhand.read())
    fhand.close()
    fhand = open("tnumber.txt", "w")
    print("your room number: ", table_number)
    new_table = str(table_number + 1)
    fhand.write(new_table)
    fhand.close()

    fhand = open("table.txt", "a+")
    buf = str(tuid)+ '|' + str(table_number) + '|' + tname + '|' + taddr + '|' + tphone + '|' + tppl + '|' + tdate + '$'
    fhand.write(buf)
    fhand.close()


def display_table():
    found = False
    key = input("Enter your UID: ")
    fhand = open("table.txt", "r")
    records = fhand.read().split('$')
    for record in records:
        attributes = record.split('|')
        temp = attributes[0]
        if(temp == key ):
            found = True
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("TABLE NUMBER : ",attributes[1])
            print("NAME         : ",attributes[2])
            print("ADDRESS      : ",attributes[3])
            print("PHONE        : ",attributes[4])
            print("PEOPLE COUNT : ",attributes[5])
            print("DATE         : ",attributes[6])
            print("\n")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    if(not found):
        print("UID does not exist")


def table_delete():
    table_number = input("Enter table number : ")
    deleted = False
    temp = list()
    fhand = open("table.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('$')
    for record in records:
        if record.startswith(table_number):
            deleted = True
            continue
        else:
            temp.append(record)


    fhand = open("table.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('$')

    if deleted:
        print("Record was successfully deleted\n")
    else:
        print("Uid does'nt exist")


def table_modify():
    flag = False
    found = False
    tuid = input("Enter UID : ")
    temp = list()
    fhand = open("table.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('$')
    for record in records:
        if record.startswith(tuid):
            found = True
            items = record.split('|')
            while (True):
                print("1. NO of people\n2.date")
                choice = int(input("what do you want to modify? "))
                if (choice == 1):
                    items[5] = input("Enter checkin date: ")
                    flag = True
                elif (choice == 2):
                    items[6] = input("Enter checkout date: ")
                    flag = True
                else:
                    print("Invalid entry, try again")
                    flag = False
                if (flag):
                    break
            buf = items[0] + "|" + items[1] + "|" + items[2] + "|" + items[3] + "|" + items[4] + "|" + items[5] + "|" + \
                  items[6] + "$"
            temp.append(buf)


        else:
            temp.append(record)
    del temp[-1]

    fhand = open("table.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('$')
    if (not found):
        print("UID does not exist")


def table_sub_menu():
    print(
        "\n\n1. Register Customer\n2. View Customer Details\n3. Delete Customer Details\n4.Modify Customer Details\n5. Go Back ")
    ch = int(input("Enter your choice: "))
    if (ch == 1):
        book_table()

    if (ch == 2):
        display_table()



    elif (ch == 3):
        table_delete()
    elif(ch == 4):
        table_modify()

    elif (ch == 5):
        return
    else:
        print("This feature will be available soon...")
        return


def customerOps():
      q = False
      while not q:
        choice = int(input(
            "************WELCOME TO SANDDUST HOTEL************\n----------MENU----------\n1. Room operations\n2. Hall operations\n3. Table operations\n4. Go back\nPlease Enter a Choice: \n"))
        
        if(choice == 1):
            room_sub_menu()
        elif(choice == 2):
            hall_sub_menu()
        elif(choice == 3):
            table_sub_menu()
        elif(choice == 4):
            main()
        
        else :
            print('this feature is not available yet...')


def adminOps():
    q = True
    username = input("Username: ")
    #password = getpass.getpass("password:")
    password=input("Password: ")
    if(username == "admin" and password == "admin"):
        print("\nWelcome Admin\n")
        while(q):
            print("\n1. Display Room Details\n2. Display Hall Details\n3. Display Table Details\n4. Go Back\n")
            choice = int(input("Enter choice: "))

            if(choice == 1):
                admin_room_display()
            elif(choice == 2):
                admin_hall_display()
            elif (choice == 3):
                admin_table_display()

            else:
                main()

            
    else:
        print("Authentication failed!!!!\n\n")
        main()


def main():
    print("*************************************************************************************************************************************************************************")
    print()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t$$$ WELCOME TO SANDDUST HOTEL $$$")
    print()
    print("*************************************************************************************************************************************************************************")

    print("1. Login as customer\n2. Login as admin\n3. Exit")
    user = int(input("Enter your choice: "))

    if(user == 1):
        customerOps()
    elif(user == 2):
        adminOps()
    elif(user == 3):
        exit(0)
    else:
        print("PLEASE CHOOSE A VALID OPTION!!")
        main()


main()

