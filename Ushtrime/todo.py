print("Task list")

print("\nNO TASKS")

print("\n(1) Add Task")
print("(2) Delete Task")
print("(3) Edit Task")
print("(4) Quit")

a = int(input("\nWhat do you want to do: "))

while a == 1:
    lista = []
    task = input("Enter a task: ")
    lista.append(task)
    print(lista)
    b = input("enter again: ")
    b = b.lower()
    
    while b == "y":
    	task = input("Enter task: ")
    	lista.append(task)
    	print(lista)
    	b = input("enter again: ")
    	b = b.lower()
    	
    while b == "s":
    	
      
