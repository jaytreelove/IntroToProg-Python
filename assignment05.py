# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JPlemons,5.13.2020,Added code to complete assignment 5
# JPlemons, 5.14.2020, Penultimate draft
# JPlemons,5.15.2020,Final changes made
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ""  # The task given by the user
strPriority = ""  # The priority level of the task
strRemove = ""  # A string to remove once a task is complete

# -- Processing -- #
# When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionary rows (like Lab 5-2)
textFile = open(objFile, "r")
for row in textFile:
    strTask, strPriority = row.split(",")
    dicRow = {"Task": strTask, "Priority": strPriority.strip()}
    lstTable.append(dicRow)
textFile.close()

# -- Input/Output -- #
# Display a menu of choices to the user
strMenu = """
    Menu of Options
    ---------------
     1) Show To-Do List
      2) Add a New Task.
       3) Remove a Completed Task.
        4) Save Data to File
         5) Exit Program
    """
while True:
    print(strMenu)
    strChoice = input("Which option would you like to perform? [1 to 5]: ")
    print()  # adding a new line for looks
    # Opt. 1 - Show the current items in the table
    if strChoice.strip() == "1":
        print("| Task --- Priority")
        print("--------------------")
        for dicRow in lstTable:
            print(f"| {dicRow['Task']} --- {dicRow['Priority']}")
        continue
    # Opt. 2 - Add a new item to the list/Table
    elif strChoice.strip() == "2":
        strTask = input("What do you need to do?: ")
        strPriority = input("What is the priority level?: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print(f"\n{strTask.capitalize()} has been added to the list. Let me know when it is completed.")
        continue
    # Opt. 3 - Remove a new item from the list/Table
    elif strChoice.strip() == "3":
        strData = False
        strRemove = input("Which task did you complete?: ")
        for dicRow in lstTable:
            if dicRow["Task"].lower() == strRemove.lower():
                strData = True
                lstTable.remove(dicRow)
                print(f"\nCongrats on a job well done! {strRemove.capitalize()} has been removed.")
                continue
        if not strData:
            print(f"\n{strRemove.capitalize()} not found, you must have completed it earlier.")
        print("\nHere's what's left.")
        print("\n| Task --- Priority")
        print("--------------------")
        for dicRow in lstTable:
            print(f"| {dicRow['Task']} --- {dicRow['Priority']}")
        continue
    # Opt. 4 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == "4":
        textFile = open(objFile, "w")
        for dicRow in lstTable:
            textFile.write(f"{dicRow['Task']}, {dicRow['Priority']}\n")
        print("The tasks have been saved to your To-Do list, just waiting to be completed.")
        textFile.close()
        continue
    # Opt. 5 - Exit program
    elif strChoice.strip() == "5":
        print("Now go out there and complete those tasks!")
        break  # and Exit the program
    else:
        print("Please make a selection from 1 - 5.")
