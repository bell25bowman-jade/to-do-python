def get_user_choice():
    print("1.View Tasks: ")
    print("2. Add Task: ")
    print("3. Delete Task: ")
    print("4. Quit Application: ")
    choice = input("Please enter your choice (1-4): ")
    return choice

#menu
def main():
    tasks = []
    while True:
        choice = get_user_choice()
        if choice == "1": # View Tasks
            if not tasks:
                print("No Tasks Available")
            else:
                print("Tasks Available:")

                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "2": # Add Task
            task = input("Enter the task you want to add: ")
            tasks.append(task)
        elif choice == "3": # Delete Task
            if not tasks:
                print("No Tasks Available to Delete")
            else:
                print("Tasks Available:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter the task number you want to delete: "))
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
                    continue

                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    print(f"Deleted task: {deleted_task}")
                else:
                    print("Invalid Task Number")
        elif choice == "4": # Quit Application
            print("Quitting Application.")
            break
        else:
            print("Invalid Choice. Select options 1 through 4.")


if __name__ == "__main__":
    main()