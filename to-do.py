"""Simple command-line to-do list application."""


def display_welcome_message():
    """Display a short welcome message when the app starts."""
    print("Welcome to the To-Do List CLI.")


def display_menu():
    """Show the main menu options."""
    print("\nMenu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Quit application")


def get_user_choice():
    """Prompt the user for a menu choice."""
    return input("Please enter your choice (1-4): ").strip()


def view_tasks(tasks):
    """Display all tasks currently stored in the list."""
    if not tasks:
        print("There are no tasks to view.")
        return

    print("Current tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    """Add a new task to the task list."""
    task = input("Enter the task you want to add: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    print(f'Task added: "{task}"')


def delete_task(tasks):
    """Delete a task selected by its task number."""
    if not tasks:
        print("There are no tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter the task number you want to delete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f'Task deleted: "{deleted_task}"')
        else:
            print("That task does not exist.")
    finally:
        print("Returning to the main menu.")


def handle_menu_choice(choice, tasks):
    """Run the action selected from the main menu."""
    if choice == "1":
        view_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        print("Quitting application.")
        return False
    else:
        print("Invalid choice. Select an option from 1 to 4.")

    return True


def main():
    """Run the to-do list command-line interface."""
    tasks = []
    display_welcome_message()

    while True:
        display_menu()
        choice = get_user_choice()

        if not handle_menu_choice(choice, tasks):
            break


if __name__ == "__main__":
    main()