tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found in the list.")

def view_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    else:
        break
