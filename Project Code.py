#4231_GokulaRamanan_XII_A1_Project_Code

import pymysql as pym # connecting to mysql server

import time # for progressbar animation
from tqdm import tqdm # for progressbar animation

from tabulate import tabulate # for printing mysql table in python
import random 

con = pym.connect(host="localhost", user="root", passwd="mypass", database="taskmaster")
cur = con.cursor()
cur.execute("show tables")


def progressbar():
    for r in tqdm([1, 2]):
        time.sleep(0.5)
    return progressbar


def faultyprogressbar():
    for r in tqdm([1, 2]):
        if r > 1:
            break
        time.sleep(0.5)
    return faultyprogressbar


def helpm():

    print("-> Main controls: \n")
    print("I. login - to login to your account")
    print("II. register - to register you account")
    print("III. help - help with controls\n")
    print("IV. about - about the project")
    print("V. exit/quit - to quit the program\n")
    print("-> User-controls: \n")
    print("1. new - to add new tasks")
    print("2. edit - to edit existing task(s)")
    print("3. view - to view your task in the form of a table")
    print("4. delete - to delete your task")
    print("5. clear - to clear all tasks")
    print("6. logout - to log out of your account")
    print("7. docs - to view the brief documentation")
    print("8. help - to use the help command")
    print()
    return helpm

list_tables = []
for table_name in cur:
    list_tables += table_name
if "users" in list_tables:
    pass
else:
    cur.execute(
        "create table users (SKey integer(100) primary key not null, username varchar(200) not null, passwd char(200) not null)"
    )  # Skey (special key) is a unique identity number mapped to a specific user; a random number generated between 1 and 100
print("\n              Task Master")
print("MySQL based Task Management Application\n")
print("Main controls: ")
print("1. login")
print("2. register")
print("3. help")
print("4. about")
print("5. exit/quit\n")
emaster = 1
while emaster > 0:
    print("=================")
    input1 = input("Enter main control: ")
    print("=================\n")
    if input1 in ["1", "login"]:
        # print("---------------------------------")
        print(
            "---------------------------------\n               Login\n---------------------------------\n"
        )
        usern = input("Enter username: ")
        passww = input("Enter password: ")
        print()
        cur.execute("Select username,passwd from users")
        listuser = []
        for i in cur:
            listuser += i
        # print(listuser)
        if usern in listuser and passww in listuser:
            if listuser.index(usern) == (listuser.index(passww) - 1):
                progressbar()
                print("\nLogin successful\n")
                str1 = "select Skey from users where username = '{}'".format(usern)
                cur.execute(str1)
                for j in cur:
                    l = j
                skey = int(
                    str(j)[1:][::-1][2:][::-1]
                )  # for eg, l = (21,) => int(l) is giving error, so this kind of conversion
                print(
                    "Welcome back :-)\n\nUsername: ",
                    usern,
                    "\nSpecial key: ",
                    skey,
                    "\n",
                )
                print("Your tasks are shown below\n")
                cur.execute("show tables")
                list_tables = []
                for table_name in cur:
                    list_tables += table_name
                # print(a)
                tablename = "tasktable" + str(skey)
                if (tablename in list_tables):  # assigning one tasktable to each user. Each table has the table name as "tasktable<skey>" 
                    pass
                else:
                    str2 = (
                        "create table "
                        + tablename
                        + " (SNo integer(20) primary key not null, Task varchar(40) not null, Priority char(10) not null)"
                    )
                    cur.execute(str2)

                def view():
                    str5 = "select * from " + tablename
                    cur.execute(str5)
                    data = cur.fetchall()
                    count = cur.rowcount
                    print(
                        tabulate(
                            data,
                            headers=["SNo", "Task", "Priority"],
                            tablefmt="grid",
                            stralign="center",
                        )
                    )
                    return view

                view()
                str8high = (
                    "select count(Task) from " + tablename + "where Priority = 'high'"
                )
                
                print(
                    "\nControls: \n 1. new (New Task) \n 2. edit (Edit tasks) \n 3. view (View Tasks) \n 4. delete (Delete tasks) \n 5. clear (Clear all your tasks) \n 6. logout \n 7. doc (Docs)\n 8. help\n"
                )
                ecurrentuser = 1
                while ecurrentuser > 0:
                    print("================")
                    control = input("Enter user control: ")
                    print("================\n")
                    # control - 4
                    if control in ["4", "delete", "del"]:
                        edel = 1
                        print("Delete command selected, your tasks are shown below")
                        view()
                        while edel > 0:
                            sinput10 = int(
                                input("Enter the serial no of the task to delete: ")
                            )
                            str7 = "select SNo from " + tablename
                            cur.execute(str7)
                            snolist = []
                            for q in cur:
                                snolist += q
                            if sinput10 in snolist:
                                str8 = "delete from {} where Sno = {}".format(
                                    tablename, sinput10
                                )
                                cur.execute(str8)
                                print("Task deleted succesfully...")
                            else:
                                print("Given sno does not exist. Try again.")
                            input11 = input("Continue deleting tasks? (y/n): ")
                            if input11 in ["y", "yes"]:
                                continue
                            elif input11 in ["n", "no"]:
                                print("Returning to user menu...\n")
                                edel = 0
                            con.commit()
                    # control - 5
                    elif control in ["clear", "5"]:
                        print()
                        input12 = input("Do you want to clear all your tasks? (y/n): ")
                        if input12 in ["y", "yes"]:
                            str9 = "truncate table " + tablename
                            cur.execute(str9)
                            print("All tasks cleared")
                            print("Returing to user menu...\n")
                        elif input12 in ["n", "no"]:
                            print("Returing to user menu...\n")
                    # control - 1
                    elif control in ["new", "New", "1"]:
                        enew = 1
                        loopconstant = (
                            1  # just the number of times the loop has been executed
                        )
                        while enew > 0:
                            task = input("Enter new task: ")
                            str10 = "select * from "+tablename
                            cur.execute(str10)
                            sno = cur.rowcount
                            e = 1
                            # while e>0:
                            input3 = input(
                                "Enter priority level (i.e. 1 for low  2 for medium  3 for high):"
                            )
                            if input3 == "1":
                                priority = "low"

                            elif input3 == "2":
                                priority = "medium"

                            elif input3 == "3":
                                priority = "high"
                            else:
                                print("Incorrect input. Try again.\n")
                            values = (
                                "insert into "
                                + tablename
                                + " (SNo,Task,Priority) values ({},'{}','{}')".format(
                                    sno + 1, task, priority
                                )
                            )
                            cur.execute(values)
                            input4 = input("Continue adding new tasks? (y/n): ")
                            if input4 in ["y", "yes"]:
                                continue
                                loopconstant += 1
                            elif input4 in ["n", "no"]:
                                if loopconstant == 1:
                                    print(
                                        "Query successfully executed. Task added to database.\n"
                                    )
                                    break
                                else:
                                    print(
                                        "Quries successfully executed. "
                                        + str(loopconstant)
                                        + " tasks added to database."
                                    )
                                    print("Returning to user menu...\n")
                                    enew = 0
                            con.commit()
                    # control - 2
                    elif control in ["edit", "2"]:
                        print("Edit command selected\n")
                        view()
                        print()
                        eedit = 1
                        while eedit > 0:
                            loopconstant = 1
                            sno = int(input("Enter the serial number of the task: "))
                            task = input("Enter new task: ")
                            input3 = input(
                                "Enter priority level (i.e. 1 for low  2 for medium  3 for high):"
                            )
                            eedit2 = 1
                            while eedit2 > 0:
                                if input3 == "1":
                                    priority = "low"
                                    eedit2 = 0
                                elif input3 == "2":
                                    priority = "medium"
                                    eedit2 = 0
                                elif input3 == "3":
                                    priority = "high"
                                    eedit2 = 0
                                else:
                                    print("Incorrect input. Try again.\n")
                            str4 = (
                                "update "
                                + tablename
                                + " set Task = '{}', Priority='{}' where SNo= {}"
                            ).format(task, priority, sno)
                            cur.execute(str4)
                            input5 = input("Continue editing tasks? (y/n): ")
                            if input5 in ["y", "yes", "ye", "Y", "Yes", "Ye"]:
                                enew = 1
                                loopconstant += 1
                            else:
                                if loopconstant == 1:
                                    print(
                                        "Query successfully executed. Task modified in the database."
                                    )

                                else:
                                    print(
                                        "Quries successfully executed. "
                                        + str(loopconstant)
                                        + " tasks modified in the database."
                                    )
                                print("Returning to user menu...\n")
                                eedit = 0
                    # control - 3
                    elif control in ["view", "3"]:
                        print("View command selected\n")
                        view()
                        print()
                    # control - 6
                    elif control in ["6", "logout"]:
                        input13 = input("Please confirm to logout (y/n): ")
                        if input13 in ["y","yes"]:
                            progressbar()
                            print("Logged out successfully.\n")
                            ecurrentuser = 0
                        else:
                            print("Logout aborted...\nReturning to user menu\n")
                    # control - 7
                    elif control in ["7", "doc", "docs"]:
                        print(
                            "--------------\nPython Project\n--------------\n\n Title: Task Master, a MySQL based Task Management Application"
                        )
                        print(
                            " Name: Gokula Ramanan R S\n Class and Section: XII A1\n ID No: 4231\n School: Suguna PIP School, Coimbatore\n"
                        )
                    # control - 7
                    elif control in ["8", "help"]:
                        print("Help menu\n")
                        helpm()
        else:
            faultyprogressbar()
            print("\n :-( Username or password incorrect. Try again. \n")
    elif input1 in ["2", "register"]:
        print(
            "---------------------------------\n               Register\n---------------------------------\n"
        )
        # print("Register menu")
        print("Requirements: username and password must atleast have 4 characters\n")
        eregister = 1
        while eregister > 0:
            input8 = input("Enter a username: ")
            input9 = input("Enter a password: ")
            cur.execute("select username from users")
            userlist = []
            for o in cur:
                userlist += o
            if len(input8) >= 4 and len(input9) >= 4:
                if input8 not in userlist:
                    eregister = 0
                else:
                    print("Username already exists. Try again.\n")
            else:
                print("Username or password not meeting the requirements. Try again.\n")
        while True:
            skeygenerator = random.randint(0, 100)
            cur.execute("select SKey from users")
            listkey = []
            for p in cur:
                listkey += p
            if skeygenerator not in listkey:
                break
        str6 = "insert into users (SKey,username,passwd) values({},'{}','{}')".format(skeygenerator, input8, input9)
        cur.execute(str6)
        print()
        progressbar()
        print("\nNew user successfully created. Redirecting to main menu....\n")
    elif input1 in ["quit", "exit", "5"]:
        print("Quitting the program")
        progressbar()
        emaster = 0
    elif input1 in ["3", "help"]:
        print("Help menu\n")
        helpm()
    elif input1 in ['about',"4"]:
        print(
                            "--------------\nPython Project\n--------------\n\n Title: Task Master, a MySQL based Task Management Application"
                        )
        print(
                            " Name: Gokula Ramanan R S\n Class and Section: XII A1\n ID No: 4231\n School: Suguna PIP School, Coimbatore\n"
                        )    
    else:
        print("Control not recognized!\n")
        a88 = input("Want help with controls? (y/n): ")
        print()
        if a88 in ["y", "yes", "Yes"]:
            print()
            helpm()
        else:
            continue
con.commit()
con.close()
