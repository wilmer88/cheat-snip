student_first_name = input("Enter student first name")
student_last_name = input("Enter student last name")
student_address_name = input("Enter student address")
student_email_name = input("Enter student email")
student_phone_name = input("Enter student phone#")

# print(student_first_name)
# print(student_last_name)
# print(student_address_name)
# print(student_email_name)
# print(student_phone_name)

if student_address_name and student_last_name and student_first_name and student_email_name and student_phone_name: 

 correct_info= input("Is this info correct:"+","+student_first_name +","+ student_last_name +","+ student_address_name+"," + student_phone_name +","+ student_email_name )
if correct_info == "y": exit()
    








