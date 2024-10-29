# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    view_tasks()
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number!")

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
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
