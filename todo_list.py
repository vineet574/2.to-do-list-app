import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("5. Edit a task")
    print("6. Search tasks")
    print("7. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    priority = input("Set priority (High, Medium, Low): ").capitalize()
    tasks.append(f"{task} [Priority: {priority}]")
    print("Task added successfully!")
    save_tasks()

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully!")
            save_tasks()
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1] += " ✅"
            print("Task marked as completed!")
            save_tasks()
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def edit_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to edit: "))
        if 0 < task_num <= len(tasks):
            new_task = input("Enter the new task description: ")
            priority = input("Set priority (High, Medium, Low): ").capitalize()
            tasks[task_num - 1] = f"{new_task} [Priority: {priority}]"
            print("Task updated successfully!")
            save_tasks()
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def search_tasks():
    keyword = input("Enter a keyword to search: ").lower()
    found_tasks = [task for task in tasks if keyword in task.lower()]
    if found_tasks:
        print("\nMatching Tasks:")
        for i, task in enumerate(found_tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No matching tasks found!")

load_tasks()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        edit_task()
    elif choice == '6':
        search_tasks()
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
