<<<<<<< HEAD
#to do list 

tasks = []

def addTask():
    task = input("Please enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def listTasks():
    if not tasks:
        print("there are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()

    try:
        taskToDelete = int(input("Chose task for deletion: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been deleted.")

        else:
            print(f"Task #{taskToDelete} was not found. ")
    except:
        print("invalid input")
  

if __name__ == "__main__":
    ### create a loop to run the app
    print("Welcome to the to do app :)")
    while True:
        print("\n")
        print("please select one if the following")
        print("----------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List task")
        print("4. Quit")

        choice = input("Enter your choice:")

        if(choice == "1"):
             addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
             listTasks()
        elif(choice == "4"):
             break
        else:
             print("Invalid input. ")

=======
#to do list 

tasks = []

def addTask():
    task = input("Please enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def listTasks():
    if not tasks:
        print("there are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()

    try:
        taskToDelete = int(input("Chose task for deletion: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been deleted.")

        else:
            print(f"Task #{taskToDelete} was not found. ")
    except:
        print("invalid input")
  

if __name__ == "__main__":
    ### create a loop to run the app
    print("Welcome to the to do app :)")
    while True:
        print("\n")
        print("please select one if the following")
        print("----------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List task")
        print("4. Quit")

        choice = input("Enter your choice:")

        if(choice == "1"):
             addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
             listTasks()
        elif(choice == "4"):
             break
        else:
             print("Invalid input. ")

>>>>>>> a3ca2687d0b49ff006ceb8b7d52d3e44b0b322dd
        print("Goodbye.")