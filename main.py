tasks = []
completed_tasks = []
def addtask(task,due):
    tasks.append({"Task": task,"Due Date": due})

def removetask(task):
    for task in tasks:
        if task['Task'] == removed_task:
            completed_tasks.append(task)
            tasks.remove(task)
            print(f"Removed Task: {removed_task}\n---------------------------------------")


def completedtask():
    if completed_tasks:
        print("Completed Tasks: ")
        for completed_task in completed_tasks:
            print(f"Task: {completed_task['Task']} \t Deadline: {completed_task['Due Date']}")
    else:
        print("No Completed Task are Found\n---------------------------------------")
def viewtask():
    if tasks:
        print("View all tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Tasks: {task['Task']} \t Deadline: {task['Due Date']}")
    else:
        print("No tasks are added so far\n---------------------------------------")

while True:
    print("---------WELCOME TO TO-DO's APP--------\n---------------------------------------")
    print("Please Select Any One of the following Options\n---------------------------------------")
    print("1.Add a task")
    print("2.Remove a task")
    print("3.View all task")
    print("4.View a completed task")
    print("5.Exit")
    print("---------------------------------------")
    choice = input("Enter choice: ")
    if choice == "1":
        new_task = input("Enter a new task: ")
        due = input("Enter due date in (YYYY-MM-DD):")
        print("---------------------------------------")
        addtask(new_task,due)
    elif choice == "2":
        removed_task = input("Enter a task to remove: ")
        removetask(removed_task)
    elif choice == "3":
        viewtask()
    elif choice == "4":
        completedtask()
    elif choice == "5":
        print("Exiting")
        break
    else:
        print("Invalid Choice")

