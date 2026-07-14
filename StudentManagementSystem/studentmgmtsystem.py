                #Student Management System
#List to store all students details
student_list =[
    {
    "Student name":"Rohan",
    "Student id":2025,
    "Age":19,
    "Year":3,
    "Gender":"Male",
    "Phone number":987654321,
    "Email":"rohan@gmail.com"
    },
    {
    "Student name":"Riya",
    "Student id":20285,
    "Age":19,
    "Year":3,
    "Gender":"Female",
    "Phone number":857654321,
    "Email":"riya123@gmail.com"
    }
]
def view_student():
    print("----Students details are----")
    for stud in student_list:
        print(f"Name :{stud['Student name']}")
        print(f"Student id:{stud['Student id']}")
        print(f"Age :{stud['Age']}")
        print(f"Year :{stud['Year']}")
        print(f"Gender :{stud['Gender']}")
        print(f"Phone number:{stud['Phone number']}")
        print(f"Email :{stud['Email']}")
        print("-"*35)
    
#Add the new student
def Add_student():
    print("--Add student details here--")
    print("Name of the student: ",end="")
    stud_name = input().strip().title()
    print("Enter student id in number---")
    print("Student id: ",end=" ")
    while True:
        stud_id = int(input())
        id_exists = False
        for student in student_list:
            if student['Student id'] == stud_id:
                id_exists =True
        if id_exists:
            print("Student id must be unique or different from others.")
            print("Enter again: ",end=" ")
        else:
            break
    while True:
        print("Student Age: ",end=" ")
        stud_age = input().strip()
        if stud_age.isdigit() and len(stud_age) ==2:
            stud_age = int(stud_age)

            if stud_age<40:
                break
            else:
                print("Age must be less than 40.")
        else:
            print("Invalid age! Try again..")
    print("Year: ",end=" ")
    stud_Yr = int(input())
    
    while True:
        print("Student Gender:",end=" ")
        stud_gender =input().strip().title()
        if stud_gender in ["Male" , "Female"]:
            break

        else:
            print("Try Again !\nEnter Male or Female")

    while True:
        print("Student phone number (only 9 digits): ",end=" ")
        stud_numb = input().strip()
        if stud_numb.isdigit() and len(stud_numb)==9:
            numb=int(stud_numb)
            break
        else:
            print("Invalid number! Enter only 9 digits")
    domain ='@gmail.com'
    stud_mail = input(f"Enter email username(excluding {domain}) :").strip()
    print("Student details added successfully!")
    print("-"*35)

    new_student ={
    "Student name":stud_name,
    "Student id":stud_id,
    "Age":stud_age,
    "Year":stud_Yr,
    "Gender":stud_gender,
    "Phone number":numb,
    "Email":f"{stud_mail}{domain}" 
    }    
    student_list.append(new_student)
    for std in student_list:
        print(f"Name :{std['Student name']}")
        print(f"Student id:{std['Student id']}")
        print(f"Age :{std['Age']}")
        print(f"Year :{std['Year']}")
        print(f"Gender :{std['Gender']}")
        print(f"Phone number:{std['Phone number']}")
        print(f"Email :{std['Email']}")

        print("-"*35)

#search details 
def search_stud():
    while True:
        print("Enter the student id  you want to search(or 0 to exit):")
        try:
            id_confirm = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid numeric Id.")
            print("-"*30)
            continue
        if id_confirm==0:
            print("Exit from search")
            return None
        found = False
        for student in student_list:
            if student['Student id'] == id_confirm:
                print(f"Name :{student['Student name']}")
                print(f"Student id:{student['Student id']}")
                print(f"Age :{student['Age']}")
                print(f"Year :{student['Year']}")
                print(f"Gender :{student['Gender']}")
                print(f"Phone number:{student['Phone number']}")
                print(f"Email :{student['Email']}")
                print("-"*35)
                found = True
                return student
        if not found:
            print("Id not match.") 
      
# update details of student
def update_stud():
    user= input("Do you want to update the student details? ('Yes or No') : ").strip().title()
    if user == 'Yes':
       
        print("--Search student id for update the details--")
        stud = search_stud()
        if stud is None:
            print("Student not found !")
            return
        while True:
            print("What do you want to update? ")
            print("Enter 1 - 4 :")
            print("1.Age\n2.Year\n3.Phone Number\n4.Exit ")
            user_update = int(input())
            
            #return
            if user_update ==1:
                #while True:
                print("Enter Student Age: ",end=" ")
                stu_age = input().strip()
                if stu_age.isdigit() and len(stu_age) ==2:
                    stu_age = int(stu_age)

                    if stu_age<40:
                        stud['Age'] = stu_age 
                        #break
                    else:
                        print("Age must be less than 40.")
                else:
                    print("Invalid age! Try again..")
                    #break
                    continue
                print(f"Updated age = {stud['Age']} ")
            elif user_update == 2:
                print("Enter year: ",end=" ")
                stud['Year']= int(input())
                print(f"Updated year ={stud['Year']} ")
                continue
            elif user_update == 3:
                print("Enter Phone Number: ",end=" ")
                stud['Phone Number']= input()
            #while True:
                if stud['Phone Number'].isdigit() and len(stud['Phone Number']) ==9:
                    number = int(stud['Phone Number'])
                    print(f"Updated Phone number = {number}")
                    break
                else:
                    print("Enter only 9 digits number\n Try Again -- ")
                    continue
            elif user_update == 4:
                break
            else:
                print("Invalid input! Try again")
    elif user =='No':
        print("Exit from update....")
    else:
        print("Invalid input!")
    
delete_list = []
def delete_student():
    print("Do you want to delete the details of student? ('Yes or No'):")
    dlt_user = input().strip().title()
    if dlt_user =='Yes':
        print("Delete student setails--")
        print("Enter the student id:", end=" ")
        id_dlt = int(input())
        for stud in student_list:
            if stud['Student id'] == id_dlt:
                print(f"You delete {stud['Student id']} id from details")
                print(f"Name = {stud['Student name']}")
                print(f"Phone number = {stud['Phone number']}")
                print(f"Email = {stud['Email']}")
                delete_list.append(stud)
                student_list.remove(stud)
                print("-"*30)
            else:
                print("Invalid id ")
    elif dlt_user =='No':
        print("Exit from delete")
    else:
        print("Invalid !")
        
def view_menu():
    print("1.View student details\n2.Add new student details\n3.Search student")
    print("4.Update student detail\n5.Delete student details\n6.Exit")
def managementSystem():
    while True:
        view_menu()
        print("Enter your choice:")
        choice = int(input())
        if choice ==1:
            view_student()
        elif choice==2:
            Add_student()
        elif choice== 3:
            search_stud()
        elif choice== 4:
            update_stud()
        elif choice== 5:
            delete_student()
        elif choice==6:
            print("Exit")
            break
        else:
            print("Invalid choice! Try again...")
if __name__ =="__main__":           
    managementSystem()