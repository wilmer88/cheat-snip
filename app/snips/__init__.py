student_first_name = input("Enter student first name")
student_last_name = input("Enter student last name")
student_address_name = input("Enter student address")
student_email_name = input("Enter student email")
student_phone_name = input("Enter student phone#")
# show_student_info_print = (student_first_name)
# print(student_last_name)
# print(student_address_name)
# print(student_email_name)
# print(student_phone_name)

students = []


while True: 
 student = dict.fromkeys(["first_name", "last_name", "address", "email", "phone#"])

 if student_address_name and student_last_name and student_first_name and student_email_name and student_phone_name: 
    correct_info = input("Is this info correct:"+","+student_first_name +","+ student_last_name +","+ student_address_name+"," + student_phone_name +","+ student_email_name )
 if correct_info=="n": 
    continue
 if correct_info == "y": 
    student["first_name"]= student_first_name
    student["last_name"] = student_last_name
    student["address"] = student_address_name
    student["email"] = student_email_name
    student["phone#"] = student_phone_name
    students.append(student)
    add_more = input("would you like to add more students?")
 if add_more == "y": 
    student_first_name = input("Enter student first name")
    student_last_name = input("Enter student last name")
    student_address_name = input("Enter student address")
    student_email_name = input("Enter student email")
    student_phone_name = input("Enter student phone#")
    other_student = input("Is this info correct:"+","+student_first_name +","+ student_last_name +","+ student_address_name+"," + student_phone_name +","+ student_email_name )
    if other_student == "y":
      student["first_name"]= student_first_name
    student["last_name"] = student_last_name
    student["address"] = student_address_name
    student["email"] = student_email_name
    student["phone#"] = student_phone_name
    students.append(student)
    continue
 if add_more=="n": 
    print(students)
    exit()

    








