import csv

def write_into_csv(info_list):
    with open('student_info.csv' 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() ==0:
            writer.writerow(["Name", "age", "Contact Number", "E-mail ID"])
        writer.writerow(info_list)

if__name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter information for student #{} in the following format (Name Age Contact_Number e_mail_ID):".format())

        #split
        student_info_list = student_info.split(' ')

        print("\nthe entered information is -\nName: {}\nAge: {}\nContact number: {}\nEmail ID: "{}"
                .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check  = input("Is the entered student information is correct? (yes/no):")

        if choice_check == "yes":
            write_into_csv(student_inf0_list)

            condition_check = input("Enter (yes/no) if you want to enter information for another student:")
            if condition_check == "yes":
                condition= True
                student_num = student_num + 1
            elif condition_check == "No":
                condition = False
        elif choice_check == "no":
            print("\nPlease re enter the values!")
