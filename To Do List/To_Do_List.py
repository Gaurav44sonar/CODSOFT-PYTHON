class To_Do_List:
    def __init__(self):
        self.task_list=[]
        self.count=0
        self.user_task=""
        self.remove_task_index=0
    
    def addTask(self):
        print()
        self.user_task=input("Enter task to add: ") 
        self.task_list.append(self.user_task)
        print("Task is added....")
        self.count+=1
        print()

    def removeTask(self):
        print()
        self.remove_task_index=int(input("Enter task index to remove: "))
        self.task_list.pop(self.remove_task_index-1)
        print("Task is removed")
        self.count-=1
        print()
        
    def viewTask(self):
        print()
        if self.count==0:
            print("To-Do list is empty")
        else:
            print("Your tasks are ")
            for t in range(0,self.count):
                print((t+1),":",self.task_list[t])
        print()
        

print("             TO-DO LIST                ")

list=To_Do_List()

while True:
    print("\nTo-Do List Menu")
    print("Enter 1: Add Task\nEnter 2: View Tasks\nEnter 3: Remove Task\nEnter 4: Exit")
    user_choice=int(input())
    if user_choice==1:
        list.addTask()
    elif user_choice==2:
        list.viewTask()
    elif user_choice==3:
        list.removeTask()
    elif user_choice==4:
        break
    else:
        print("Invalid option")