import psycopg2 as pg2

import INSERT_FakeDate as fkd

import company_management_classes_update1 as cmcu

try:
    conn = pg2.connect(database='postgres', user='postgres', password='333')
except:
    print("a problem has occured during connection to the data base")
cur = conn.cursor()

choice_1 = 100


## main menue for select for your option :

while choice_1 != '0':
    print(">>> if you want to add the Assumption data Enter '1' <<<")
    print(">>> if you want to add new Items to your DataBase Enter '2' <<<")
    print(">>> if you want to Edit the Existing data Enter '3' <<<")
    print(">>> if you want to Delete the Existing data Enter '4' <<<")
    print(">>> if you want to Exit the program Enter '0' <<<")
    choice_1 = input(">>>>> Make your Choice : <<<<< ------>>> : ")

    if choice_1 == '1':
        print(">>> --- Welcom to the Inserting Assumption Data --- <<<")
        fkd.main()

    if choice_1 == '3':
        choice = 100
        while choice != '0':
            print(">>> --- Welcome to the Edit Section --- <<<")
            print(">>> if you want to Edit the Customers Enter '1' <<<")
            print(">>> if you want to Edit the Workers Enter '2' <<<")
            print(">>> if you want to Edit the Employeis Enter '3' <<<")
            print(">>> if you want to Edit Products Enter '4' <<<")
            print(">>> if you want to Edit Department's Enter '5' <<<")
            print(">>> if you want to Edit Work Shift's Enter '6' <<<")
            print(">>> if you want to Edit a Project Enter '7' <<<")
            print(">>> if you want to Edit a Address Enter '8' <<<")
            print(">>> if you want to Edit a Distributer Enter '9' <<<")
            print(">>> Enter '1' if you want to <<Exit>> Edit section! <<<")
            if choice == '0':
                break
            if choice == '1':
                # national_code = input("Please Enter the National Code of the Costumer that you want to edit!")
                # pass
                cus = cmcu.Costumer()
                cus.edit_Customer()

            if choice == '2':
                # pass
                wor = cmcu.Worker()
                wor.edit_Worker()

            if choice == '3':
                # pass
                emp = cmcu.Employee()
                emp.edit_Employee()

            if choice == '4':
                # pass
                prod = cmcu.Product()
                prod.edit_Product()

            if choice == '5':
                # pass
                dep = cmcu.Department()
                dep.edit_Department()

            if choice == '6':
                # pass
                ws = cmcu.Work_Shift()
                ws.edit_WorkShift()

            if choice == '7':
                # pass
                proj = cmcu.Projects()
                proj.edit_Projects()

            if choice == '8':
                # pass
                addr = cmcu.Address()
                addr.edit_Address()

            if choice == '9':
                # pass
                dist = cmcu.Distributer()
                dist.edit_Distributer()
            

    if choice_1 == '2':
        choice = 100
        while(choice != '0'):
            print(">>> if you want to add a new Customer Enter '1' <<<")
            print(">>> if you want to add a new Worker Enter '2' <<<")
            print(">>> if you want to add a new Employee Enter '3' <<<")
            print(">>> if you want to add a new Product Enter '4' <<<")
            print(">>> if you want to add a new Department Enter '5' <<<")
            print(">>> if you want to add a new Work Shift Enter '6' <<<")
            print(">>> if you want to add a new Project Enter '7' <<<")
            print(">>> if you want to add a new Address Enter '8' <<<")
            print(">>> if you want to add a new Distributer Enter '9' <<<")
            print(">>> if you want to <<Exit>> Enter '0' <<<")
            choice = input(">>>>> Please Make your Choice : <<<<< ------>>> : ")

            if choice == '0':
                break

            ### Customer Part :
            if choice == '1':
                cu = cmcu.Costumer()
                cu.add_Customer()
                # first_name = input("please Enter the first name of the Customer that you want to add : ")
                # last_name = input("please Enter the last name of the Customer that you want to add : ")
                # national_code = input("please Enter the National Code of the costomer that you want to add : ")
                # phone_num = input("please Enter the Phone Number of the Costumer that you want to Add : ")
                # postal_code = input("please Enter the Postal Code of the Costumer that you want to Add : ")


                pass
            ### Worker Part :
            if choice == '2':
                # first_name = input("please Enter the first name of the Worker that you want to add : ")
                # last_name = input("please Enter the last name of the worker that you want to add : ")
                # national_code = input("please Enter the National Code of the Worker that you want to add : ")
                # phone_num = input("please Enter the Phone Number of the Worker that you want to Add : ")
                # postal_code = input("please Enter the Postal Code of the Worker that you want to Add : ")
                wor = cmcu.Worker()
                wor.add_Worker()

                pass
            ### Employee Part :
            if choice == '3':
                emp = cmcu.Employee()
                emp.add_Employee()
                # first_name = input("please Enter the first name of the Employee the you wnat to add : ")
                # last_name = input("please Enter the last name of the Employee that you want to add : ")
                # national_code = input("please Enter the National Code of the Employee that you want to add : ")
                # phone_num = input("please Enter the Phone Number of the Employee that you want to Add : ")
                # postal_code = input("please Enter the Postal Code of the Employee that you want to Add : ")
                # pass

            ### Product Part :
            if choice == '4':
                # print("--- >>>> Welcom to the Add New Product Section <<<< ---")
                # product_name = input("please Enter the Name of the Product that you want to Add : ")
                # product_id = input("please Enter the ID of the product that you want to Add : ")
                # product_price = input("please Enter the Price of the Product that you want to Add : ")
                # product_weight = input("please Enter the Weight of the Product that you want to Add : ")
                # pass
                pro = cmcu.Product()
                pro.add_Product()

            ### Add Department Part :
            if choice == '5':
                # print("--- >>>> Welcom to the Add New Department Section <<<< ---")
                dep = cmcu.Department()
                dep.add_Department()
                # dept_name = input("please Enter the Name of the New Department that you want to Add : ")
                # while(dept_name == ""):
                #     print("<<<Attention>>> : Department Name can't be Empty!!!")
                #     dept_name = input("---> please Enter the Department Name again!")
                # start_work_time = input("please Enter the Start Work Time of the Department : ")
                # end_work_tiem = input("please Enter the End Work Time of the Department : ")
                # place = input("please Enter the place of the Department :")
                # proj_check = input("if have projects in the department Enter <<1>> : ")
                # if proj_check == 1:
                #     pass

            ### Add Work shift Part :
            if choice == '6':
                # print("--- >>>> Welcom to the Add New Work Shift Section <<<< ---")
                # work_shift_name = input("please Enter the Name of the Work Shift that you want to Add : ")
                # while work_shift_name == "":
                #     print("<<<Attention>>> : Department Name can't be Empty!!!")
                #     work_shift_name = input("---> please Enter the Name of the Work Shift Again : ")
                # start_time = input("please Enter the Start time of the Work Shift : ")
                # end_time = input("please Enter the End Time of the Work Shift : ")
                ws = cmcu.Work_Shift()
                ws.add_WorkShift()


            if choice == '7':
                # print("--- >>>> Welcom to the Add New 'Project' Section <<<< ---")
                # project_id = input("please Enter the ID of the Project : ")
                # while project_id == "":
                #     print("<<<Attention>>> : Project ID can't be Empty!!")
                #     project_id = input("---> please Enter the ID of the project :")
                # start_date_proj = input("please Enter the Start Date of the Project : ")
                # end_date_proj = input("please Enter the End Date of the Project : ")
                proj = cmcu.Projects()
                proj.add_Projects()
            

            if choice == '8':
                # print("--- >>>> Welcom to the Add New Address Section <<<< ---")
                # postal_code = input("please Enter the Postal Code of the exact Address : ")
                # while postal_code == "":
                #     print("<<<Attention>>> : Postal Code can't be Empty!!")
                #     postal_code = input("please Enter the Postal Code again : ")
                # street = input("please Enter the Name of the Street of the Address : ")
                # while street == "":
                #     print("<<<Attention>>> : Street Name can't be Empty!!")
                #     street = input("please Enter the Name of the Street Again : ")
                # avenue = input("please Enter the Name of the Avenue of the exact Adrress : ")
                # while avenue == "":
                #     print("<<<Attention>>> : Avenue Name can't be Empty!!")
                #     avenue = input("please Enter the Nae of the Avenue of the exact Address Again : ")
                # city = input("please Enter the Name of the exact City : ")
                # while city == "":
                #     print("<<<Attention>>> : City Name can't be Empty!!")
                #     city = input("please Enter the Name of the Avenue again : ")
                addr = cmcu.Address()
                addr.add_Address()
                

            if choice == '9':
                # print("--- >>>> Welcom to the Add New Distributer Section <<<< ---")
                # distributer_id = input("please Enter the ID of the Distributer : ")
                # while distributer_id == "":
                #     print("<<<Attention>>> : Distributer ID can't be Empty!!")
                #     distributer_id = input("please Enter the ID of the of the Distributer Again : ")
                
                # national_code = input("please Enter the National Code of the Distributer :")
                # while national_code == "":
                #     print("<<<Attention>>> : National Code can't be Empty!!")
                #     national_code = input("please Enter the National Code of the exact Distributer again : ")
                # account_number = input("please Enter the Account Number of the exact Distributer : ")
                # while account_number == "":
                #     print("<<<Attention>>> : Account Number can't be Empty!!")
                #     account_number = input("please Enter the Account Number of the exact Distributer again : ")
                # print("Now you have to add New Pices that the Distributer Produces : ")

                # pass
                dist = cmcu.Distributer()
                dist.add_Distributer()

            else:
                print("**** You choose a wrong item please Make your Choice Again! ****")
                choice = input("please Enter your choice Again --->>> : ")


    if choice_1 == 4:
        choice = 100
        while choice != '0':
            print(">>> if you want to Delete a Customer Enter '1' <<<")
            print(">>> if you want to Delete a Worker Enter '2' <<<")
            print(">>> if you want to Delete a Employee Enter '3' <<<")
            print(">>> if you want to Delete a Product Enter '4' <<<")
            print(">>> if you want to Delete a Department Enter '5' <<<")
            print(">>> if you want to Delete a Work Shift Enter '6' <<<")
            print(">>> if you want to Delete a Project Enter '7' <<<")
            print(">>> if you want to <<Exit>> Enter '0' <<<")
            choice = input(">>>>> Please Make your Choice : <<<<< ------>>> : ")

            if choice == '0':

                break
            if choice == '1':
                # national_code = input("please Enter the National Code of the Costumer that you want to Delete : ")
                cus = cmcu.Costumer()
                cus.delete_Customer()

                # pass

            if choice == '2':
                # national_code = input("pleasr Enter the National Code of the Worker that you want to delete : ")
                worker = cmcu.Worker()
                worker.delete_Worker()
                # pass
            if choice == '3':
                # national_code = input("please Enter the National Code of the Eployee that you want to Delete : ")
                emp = cmcu.Employee()
                emp.delete_Employee()

            if choice == '4':
                # product_id = input("please Enter the id of the product that you want to delete : ")
                prod = cmcu.Product()
                prod.delete_product()

            if choice == '5':
                # dep_name = input("please Enter the name of the Department that tou want to Delete : ")
                # pass
                dep = cmcu.Department()
                dep.delete_Department()

            if choice == '6':
                # work_shift_name = input("please Enter the name of the Work Shift that you want to delete : ")
                # pass
                ws = cmcu.Work_Shift()
                ws.delete_WorkShift()

            if choice == '7':
                # project_id = input("please Enter the ID of the Project that you want to remove : ")
                # pass
                proj = cmcu.Projects()
                proj.delete_Projects()

            if choice == '8':

                pass
            if choice == '9':
                pass

cur.close()
conn.commit()
conn.close()