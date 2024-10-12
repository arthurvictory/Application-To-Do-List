# an empty tasks incomplete and complete lists
tasks = []
complete_tasks = []

# function to add a task to the to-do list
def add_task(task):
    tasks.append(task) 
    print(f"Your '{task}' task has been added!")

# function to view that current tasks, incomplete and/or complete
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Incomplete To-Do List:")
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}. {task}")
    print("*==Complete To-Do List==*")
    if not complete_tasks:
        print("No completed tasks in the list.")
    else:
        for i, complete_task in enumerate(complete_tasks, start=1):
            print(f"{i}. {complete_task}")

# function to complete a task
def complete_task():
    if not tasks:
        print("No tasks to mark as complete.")
    else:
        try:
            task_number = int(input("Enter the task number to mark as complete: "))
            if task_number in range(1, len(tasks) + 1):
                completed_task = tasks.pop(task_number - 1)
                complete_tasks.append(completed_task)
                print(f"The task {completed_task} has been marked complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

#function to delete a task from the complete list
def delete_task():
    if not complete_tasks:
        print("No task to delete")
    else:
        try:
            task_number = int(input("Enter the task number you wish to remove"))
            if task_number in range(1, len(tasks) + 1):
                removed_task = complete_tasks.pop(task_number - 1)
                print(f"{removed_task} has been removed from the complete list")
            else:
                print("That isn't a valid task number")
        except ValueError:
            print("Invalid input! Please enter a integer from completed list!")

#function to create a CLI menu for the app
def todo_menu():
    while True:
        print("""
               *===============================*
                Welcome to the To-Do List App!
               *===============================* 
                Menu:
                1. Add a task
                2. View tasks
                3. Mark a task as complete
                4. Delete a task
                5. Quit App
            """)

        option = input("Enter a valid Option: ")
        
        if option == "1":
            task = input("Please enter your current task: ")
            add_task(task)
        elif option == "2":
            view_tasks()
        elif option == "3":
            complete_task()
        elif option == "4":
            delete_task()
        elif option == "5":
            print("Exiting Application...please wait!")
            break
        else:
            print("Please enter a valid option from the menu!")

todo_menu()
        