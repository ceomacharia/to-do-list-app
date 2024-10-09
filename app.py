def menu_options():
    print("1. add a new task")
    print("2. view all tasks")
    print("3. mark task as complete")
    print("4. delete a task")
    print("5. clear all tasks")
    print("6. exit")

task_list = {}

while True:
    menu_options()
    choice = input("choose an option (1-7):")

    if choice == "7": #exit
        print("exiting")
        break
    elif choice == "1":  #add new task
        task = input("enter task name: ")
        description = input("enter task description: ")

        task_list[task] = description
        print(f"'{task}' task added successfully")

    elif choice == "2":  #view all tasks
        if task_list:
            print(task_list.items())
        else:
            print("No current tasks")

    elif choice == "4": #delete a task
