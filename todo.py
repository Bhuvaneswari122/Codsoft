
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            self.view_tasks()
            task_number = int(input("Enter task number to delete: "))
            if 1 <= task_number <= len(self.tasks):
                del self.tasks[task_number - 1]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")

    def update_task(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            self.view_tasks()
            task_number = int(input("Enter task number to update: "))
            if 1 <= task_number <= len(self.tasks):
                new_task = input("Enter new task: ")
                self.tasks[task_number - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid task number.")

def main():
    todo = TodoList()
    while True:
        print("\nTodo List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Update task")
        print("5. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.delete_task()
        elif choice == "4":
            todo.update_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

