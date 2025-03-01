class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "[✔]" if task["done"] else "[ ]"
                print(f"{i}. {status} {task['task']}")

    def mark_done(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num - 1]["done"] = True
            print(f"Task {task_num} marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            removed_task = self.tasks.pop(task_num - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            num = int(input("Enter task number to mark as done: "))
            todo.mark_done(num)
        elif choice == "4":
            num = int(input("Enter task number to delete: "))
            todo.delete_task(num)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
