tasks = []

def listtask():
  if not tasks:
    print("There are no tasks currently")
  else:
    print("Tasks to do:")
    for index, task in enumerate(tasks):
      print(f"Tasks #{index}. {task}")
      
def addtask():
  task = input("Enter the task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")

def deletetask():
  listtask()
  try:
    tasktodelete = int(input("Enter the # of the task to delete: "))
    if tasktodelete>=1 and tasktodelete<=len(tasks):
      tasks.pop(tasktodelete)
      print(f"task #{tasktodelete} deleted.")
    else:
      print(f"Task #{tasktodelete} does not exist.")
  except:
    print("Invalide input.")
  

if __name__ == '__main__':
  # create a loop to run the app
  print("Welcome to the to do list app:")
  while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List task ")
    print("4. Quit")
    
    choice = input("Enter your choise (1-4): ")
    if(choice == '1'):
      addtask()
    elif(choice =='2'):
      deletetask()
    elif(choice =='3'):
      listtask()
    elif(choice == '4'):
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")


# The code you provided is a simple command-line to-do list application written in Python. It allows users to add, list, and delete tasks from a list. Here's an analysis of the code:

# 1. Global Variable:
# tasks = [] is a global list that stores all the tasks. Each task is a string added by the user.
# 2. Functions:
# listtask():

# This function checks if the tasks list is empty.
# If it is empty, it prints "There are no tasks currently."
# Otherwise, it enumerates through the list and prints each task with its index.
# addtask():

# This function prompts the user to input a task and adds it to the tasks list.
# It confirms the addition by printing the task added.
# deletetask():

# This function first calls listtask() to display all current tasks.
# It then prompts the user to enter the index of the task they wish to delete.
# The deletion logic has an off-by-one error:
# User inputs an index starting from 1, but Python lists are zero-indexed.
# It should check if tasktodelete >= 0 and tasktodelete < len(tasks) and adjust the input by subtracting 1 when accessing the list.
# It currently pops the element based on the provided index but needs adjustment for proper indexing.
# There's also a small typo ("Invalide input"), which should be corrected to "Invalid input."
# 3. Main Application Loop:
# The application runs inside an infinite loop, presenting a menu with four choices: add a task, remove a task, list tasks, and quit.
# The user input (choice) determines which function to call:
# '1' calls addtask().
# '2' calls deletetask().
# '3' calls listtask().
# '4' exits the loop, terminating the application.
# Any other input prompts an "Invalid choice" message, asking the user to try again.
# 4. Potential Improvements:
# Error Handling: Improve input handling and validation to ensure robust application behavior, e.g., handling non-numeric inputs when deleting a task.
# Index Correction: Modify the index in deletetask() to handle 1-based indexing correctly, as users generally expect lists to start at 1.
# Code Readability: Fix typos and add comments or docstrings for better readability.
# Modularize Further: Separate the main loop into its function for cleaner code structure.
# Edge Cases: Consider what happens when users add an empty task or delete from an empty list.