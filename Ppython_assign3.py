# Defining the Task class
class Task:
    def __init__(self, title, description=None, status="incomplete"):
        """
        Constructor to initialize the task with title, description, and status.
        Default status is set to "incomplete".
        This method act as constructor for the Task class, encapsulating attributes within the object
        """
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        """
        Method to mark the task as complete.
        Changes the status from "incomplete" to "complete".
        """
        self.status = "complete"
    
    def __str__(self):
        """
        String representation of the Task object.
        Displays the task title and its status.
        Method overriding: This method is overriding the default __str__() method to give a user defined string representation for task objects.
        """
        return "Task: " + self.title + " - Status: " + self.status

# Defining the TaskList class to manage tasks
class TaskList:
    def __init__(self):
        """
        Constructor to initialize the task list, an empty list to hold tasks.
        It is encapsulated as a class attribute
        """
        self.tasks = []

    def add_task(self, title, description=None):
        """
        Method to add a regular task to the task list.
        Takes the title and description of the task as input.
        """
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def add_priority_task(self, title, description=None, priority="low"):
        """
        Method to add a priority task to the task list.
        It takes the title, description, and priority level (low, medium, high).
        It handles tasks of different types using polymorphism 
        """
        new_task = PriorityTask(title, description, priority=priority)
        self.tasks.append(new_task)

    def mark_task_complete(self, title):
        """
        Method to mark a task as complete by searching for the task by its title.
        If the task is found, its status is changed to complete.
        It is an example of using polymorphism because here we are dealing with both Task and 
        PriorityTask objects, both having the `mark_complete()` method.
        """
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                break

    def remove_task(self, title):
        """
        Method to remove a task from the list.
        Searches for the task, if found then removes it.
        """
        task_found = False
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                task_found = True
                break
        if task_found:
            print(f"Task '{title}' has been removed.")
        else:
            print(f"No task found with the title: {title}")

    def list_tasks(self):
        """
        Method to list all tasks in the task list.
        If no tasks exist, inform the user.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def find_task(self, title):
        """
        Method to find a task by its title.
        Finds the task by title & prints it if found.
        """
        for task in self.tasks:
            if title.lower() in task.title.lower():
                print(task)
                return
        print(f"No task found with title: {title}")
    
    def find_priority_task(self, title):
        """
        Method to find a priority task.
        Finds specifically priority tasks and prints if found.
        """
        for task in self.tasks:
            if isinstance(task, PriorityTask) and title.lower() in task.title.lower():
                print(task)
                return
        print(f"No priority task found with title: {title}")

# Defining the class PriorityTask that inherits from Task
class PriorityTask(Task):
    def __init__(self, title, description=None, status="incomplete", priority="low"):
        """
        Constructor to initialize a priority task with title, description, status, and priority.
        priority can be (low, medium, or high.)
        Inheritance: PriorityTask inherits from Task and extends the functionality
        with the `priority` attribute.
        """
        super().__init__(title, description, status)
        self.priority = priority

    def __str__(self):
        """
        Overriding the __str__ method to include priority level in the task details.
        Method overriding: This method is overriding the default __str__() method
        from the parent class to give overridden behavior in the derived class.
   
        """
        return "Priority Task: " + self.title + " - Status: " + self.status + " - Priority: " + self.priority


# Example usage of Task List Application with user interaction
if __name__ == "__main__":
    task_list = TaskList()                       #an instance of TaskList to hold tasks.

    while True:
        print("\nTask List Application")
        print("1. Add Task")
        print("2. Add Priority Task")
        print("3. Mark Task Complete")
        print("4. List Tasks")
        print("5. Find Task")
        print("6. Find Priority Task")
        print("7. Remove Task")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (or leave empty): ")
            task_list.add_task(title, description if description else None)

        elif choice == "2":
            title = input("Enter priority task title: ")
            description = input("Enter priority task description (or leave empty): ")
            priority = input("Enter priority (low, medium, high): ").lower()
            task_list.add_priority_task(title, description if description else None, priority)

        elif choice == "3":
            title = input("Enter task title to mark as complete: ")
            task_list.mark_task_complete(title)

        elif choice == "4":
            task_list.list_tasks()

        elif choice == "5":
            title = input("Enter task title to search for: ")
            task_list.find_task(title)

        elif choice == "6":
            title = input("Enter priority task title to search for: ")
            task_list.find_priority_task(title)

        elif choice == "7":
            title = input("Enter task title to remove: ")
            task_list.remove_task(title)

        elif choice == "8":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice, please try again.")

'''
Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 1
Enter task title: Do homework
Enter task description (or leave empty): 

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 1
Enter task title: Go to the gym
Enter task description (or leave empty): cardio workout

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 2
Enter priority task title: Buy groceries
Enter priority task description (or leave empty): Milk and eggs
Enter priority (low, medium, high): High

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 4
Tasks:
Task: Do homework - Status: incomplete
Task: Go to the gym - Status: incomplete
Priority Task: Buy groceries - Status: incomplete - Priority: high

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 3
Enter task title to mark as complete: Go to the gym

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 4
Tasks:
Task: Do homework - Status: incomplete
Task: Go to the gym - Status: complete
Priority Task: Buy groceries - Status: incomplete - Priority: high

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 5
Enter task title to search for: Do homework
Task: Do homework - Status: incomplete

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 6
Enter priority task title to search for: Buy groceries
Priority Task: Buy groceries - Status: incomplete - Priority: high

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 7
Enter task title to remove: Go to the gym
Task 'Go to the gym' has been removed.

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 4
Tasks:
Task: Do homework - Status: incomplete
Priority Task: Buy groceries - Status: incomplete - Priority: high

Task List Application
1. Add Task
2. Add Priority Task
3. Mark Task Complete
4. List Tasks
5. Find Task
6. Find Priority Task
7. Remove Task
8. Exit
Enter your choice: 8
Exiting the application.
'''            
