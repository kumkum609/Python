"""Create Health management system, in which 2file food lock and 2file exercise lock
->write a function that when executed takes as input client name
total 4 files, 2 for harry and 2 for Rohan
->one more function to retrive exercise or food for any client."""

def getdate():
    import datetime
    return datetime.datetime.now()
a = int(input("Lock or retrive, 1 for lock & 2 for retrive:\n"))
#create function 1 for lock
x =int(input("Harry:1, Rohan:2\n"))
y =int(input("Food or Exercise:,food:1,Exercise:2\n"))
def func1():
    if x==1:
        if y==1:
            f=open("Harry_Food.txt","a")
            food = input("Enter Food:\n")
            f.write(str([str(getdate())])+":"+food+"\n")
            print("Food entered successfully")
            f.close()
        elif y==2:
            f=open("Harry_Exc.txt","a")
            ex = input("Enter Exercise:\n")
            f.write(str([str(getdate())])+":"+ex+"\n")
            print("Exercise entered successfully")
            f.close()
        else:
            print("Enter right choice")    
    if x==2:
        if y==1:
            f=open("Rohan_Food.txt","a")
            food = input("Enter Food:\n")
            f.write(str([str(getdate())])+":"+food+"\n")
            print("Food entered successfully")
            f.close()
        elif y==2:
            f=open("Rohan_Exc.txt","a")
            ex = input("Enter Exercise:\n")
            f.write(str([str(getdate())])+":"+ex+"\n")
            print("Exercise entered successfully")
            f.close()  
        else:
            print("Enter right choice")    
               
   #Create function 2 for retrive
def func2():
    if x ==1:
        if y==1:
            f=open("Harry_Food.txt","r")
            for i in f:
                print(i,end=" ")
            f.close()
    if x==1:
        if y==2:
            f=open("Harry_Exc.txt","r")
            for i in f:
                print(i,end=" ")
            f.close()    
      
    if x==2:
        if y==1:
            f=open("Rohan_Food.txt","r")
            for i in f:
                print(i,end=" ")
            f.close()
    if x==2:
        if y==2:
            f=open("Rohan_Exc.txt","r")
            for i in f:
                print(i,end=" ")
            f.close()    
        
if a==1:
    func1()
elif a==2:
    func2()
else:
    print("Enter right choice")
                          

