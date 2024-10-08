def menu_options():
    print("add a new task")
    print("view sll tasks")
    print("mark task as complete")
    print("delete a task")
    print("save tasks to files")
    print("load tasks from file")
    print("exit")

while True:
    menu_options()
    choice = input("choose an option:")

    if choice == "exit":
        print("exiting")
        break
    