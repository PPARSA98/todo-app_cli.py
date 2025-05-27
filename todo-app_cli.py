# todo-app_cli.py
"""
Fully Tested CLI To-Do List App
- Stores tasks in a list
- Allows adding, viewing, deleting tasks
- Validates user input
- Handles errors gracefully
"""

def display_menu():
    """Display the main menu options."""
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def get_user_choice():
    """Prompt the user for a menu option and validate input."""
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid option. Please enter a number from 1 to 4.")
            return None
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def add_task(task_list):
    """Add a task to the list."""
    task = input("Enter task description: ").strip()
    if not task:
        print("Task description cannot be empty.")
        return
    task_list.append(task)
    print("Task added successfully.")

def view_tasks(task_list):
    """Display all tasks in the list."""
    if not task_list:
        print("No tasks to show.")
        return
    print("\nCurrent Tasks:")
    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task}")

def delete_task(task_list):
    """Delete a task by its number."""
    if not task_list:
        print("No tasks to delete.")
        return

    view_tasks(task_list)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(task_list):
            removed = task_list.pop(index - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Returning to main menu...")

def main():
    """Main loop of the application."""
    tasks = []
    print("Welcome to the CLI To-Do List App!")

    while True:
        display_menu()
        choice = get_user_choice()
        if choice is None:
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Thanks for using the To-Do List App. Goodbye!")
            break

if __name__ == "__main__":
    main()
