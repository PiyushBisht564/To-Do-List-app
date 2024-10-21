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


