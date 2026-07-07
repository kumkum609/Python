import datetime
#To do list
print("Your To_do_list")
def show_task():
    print("1. For view task")
    print("2. For write task")
def Todo_task():
    tasks=[]
    while True:
        show_task()
        choice =int(input("Enter your choice:"))
        today_date=datetime.date.today()
        if choice==1:
            with open("ToDoList.txt","r") as f:
                 data=f.read()
            if not data.strip():
                print("Empty list!")
                break
            else:    
                    print(data)
                    break
        elif choice==2:
             task = input("Enter your task:")
             with open("ToDoList.txt","a") as f:
                  f.write(task+"\n")
                  date_tody=f"{today_date}:{task}"
                  print(date_tody)
                  print("Task added successfully!")
                  break
        else:
             print("Invalid choice")
             break
Todo_task()
