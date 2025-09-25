
to_do_list = []


def add_task():
    task = input("Add a new task: ")
    to_do_list.append({"Task": task , "Status" : "Pending"})
    print("Task added Successfully!\n")

def view_task():
    if len(to_do_list) == 0:
        print("No tasks\n")
    else:
        print("Your Task List:")
        for index, task in enumerate(to_do_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
        print("\n")

def remove_task():
    if len(to_do_list) == 0:
        print("List is Empty")
    else:
        try:
            search_index = int(input("Choose a Task number that you want to delete: ")) -1
            if 0 <= search_index < len(to_do_list):
                remove_task = to_do_list.pop(search_index)
                print(f"Task {remove_task['Task']} removed Successfully! \n")
            else:
                print("Invalid Choice of number\n")
        except ValueError:
            print("Pls enter a valid number\n")

def mark_done():
    if len(to_do_list) == 0:
        print("List is Empty\n")
    else:
        try:
            search_index = int(input("Choose a Task number that you want to mark as done: ")) -1
            if 0 <= search_index < len(to_do_list):
                to_do_list[search_index]["Status"] = "Done"
                print(f"Task {to_do_list[search_index]['Task']} has been marked as done\n")
            else:
                print("Invalid Choice of number\n")
        except ValueError:
            print("Pls enter a valid number\n")

def menu():
    while True:
        print("Welcome to Todolist!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Mark a task as Completed")
        print("5. Exit")

        choice = input("Enter your choice number: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Thank you! We are exiting To Do List" )
            exit()
        else:
            print("Invalid choice number")

menu()

