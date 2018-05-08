###classes !!!

### here are the classes of the Project !!!
import psycopg2 as pg2

try:
    conn = pg2.connect(database='postgres', user='postgres', password='333')
except:
    print("a problem has occured during connection to the data base")


class Pieces:
    def __init__(self, p_id=None, p_name=None, produce_date=None, produce_id=None, p_price=0):
        # pass
        self.piece_id = p_id
        self.piece_name = p_name
        self.produce_date = produce_date
        self.produce_id = produce_id
        self.piece_price = p_price

    
    def add_Piece(self):
        # pass
        print("--- >>>> Welcome to the Add New Piece Section <<<< ---")
        self.piece_name = input("please Enter the Name of the Exact Piece : ")
        self.piece_id = input("please Enter the Code of the Exact Piece : ")
        while self.piece_id == "":
            print("<<<Attention>>> : Piece Code can't be Empty!!!")
            self.piece_id = input("please Enter the Code of the Exact Piece Again : ")
        self.produce_date = input("please Enter the Date that the Exact Piece has Produced : ")
        self.produce_id = input("please Enter the ID of the Exact Produce : ")
        self.piece_price = input("please Enter the Price of the Exact Piece : ")

        cur = conn.cursor()
        st = """    """
        cur.execute(st)
        cur.close()
        conn.commit()
    
    def edit_Piece(self):
        # pass
        print("--- >>>> Welcome to the Edit a Piece Section <<<< ---")
        edit_pic = input("please Enter the Code of the Piece that you want to Edit : ")
         cur = conn.cursor()
        st = """SELECT * FROM "Pieces" WHERE "Piece_ID" = '{0}'""".format(edit_pic)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Pieces with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_piece()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Piece ID>> ---")
                    print("2 --->>> Edit the <<Piece Name>> ---")
                    print("3 --->>> Edit the <<produce Date>> ---")
                    print("4 --->>> Edit the <<Product ID>> ---")
                    print("5 --->>> Edit the <<Piece Price>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_ip_name = input("please Enter the ID of new Piece that you want : ")
                        st_2 = """UPDATE "Pieces" SET "Piece_ID" = '{0}' WHERE "Piece_ID" = '{1}'
                        """.format(edit_ip, edit_pic)
                    
                    if loop_check == '2':
                        edit_pn = input("please Enter the new Piece Name that you want : ")
                        st_3 = """UPDATE "Pieces" SET "Piece_Name" = '{0}' WHERE "Piece_Name" = '{1}'
                        """.format(edit_pn, edit_pic)
                    
                    if loop_check == '3':
                        edit_pd = input("please Enter the new produce Date that you want : ")
                        st_4 = """UPDATE "Pieces" SET "produce_Date" = '{0}' WHERE "produce_Date" = '{1}'
                        """.format(edit_pd, edit_pic)

                    if loop_check == '4':
                        edit_pi = input("please Enter the ID of new Product that you want : ")
                        st_5 = """UPDATE "Pieces" SET "Product_ID" = '{0}' WHERE "Product_ID" = '{1}'
                        """.format(edit_pi, edit_pic)

                    if loop_check == '5':
                        edit_pp = input("please Enter the new Piece Price that you want : ")
                        st_6 = """UPDATE "Pieces" SET "Piece_Price" = '{0}' WHERE "Piece_Price" = '{1}'
                        """.format(edit_pp, edit_pic)

        cur.close()
        conn.commit()



    def delete_Piece(self):
        # pass
        print("--- >>>> Welcome to the Delete a Piece Section <<<< ---")
        del_piece_id = input("please Enter the Code if the Piece that you want to Delete : ")
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        if a == None:
            print("--->>>Error : There is No Piece with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Piece()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Piece"  WHERE "Piece_ID" = '{0}'""".format(del_piece_id)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()

class Work_Shift:
    def __init__(self, w_s_name=None, start_t=None, end_t=None):
        self.work_shift_name = w_s_name
        self.start_time = start_t
        self.end_time = end_t

    def add_WorkShift(self):
        # pass
        print("--- >>>> Welcome to the Add New Work Shift Section <<<< ---")
        self.work_shift_name = input("please Enter the Name of the Work Shift that you want to Add : ")
        while self.work_shift_name == "":
            print("<<<Attention>>> : Department Name can't be Empty!!!")
            self.work_shift_name = input("---> please Enter the Name of the Work Shift Again : ")
        self.start_time = input("please Enter the Start time of the Work Shift : ")
        self.end_time = input("please Enter the End Time of the Work Shift : ")

        cur = conn.cursor()

        # st = "insert into Work_Shift(Work_Shift_Name, Start_Time, End_Time) Values('"
        # st += self.work_shift_name + "','" + self.start_time + "','" + self.end_time + "');"
        st = """INSERT INTO "Work_Shift"(VALUES ('{0}','{1}','{2}'));""".format(self.work_shift_name, self.start_time, self.end_time)
        cur.execute(st)
        cur.close()
        conn.commit()
        # conn.close()
    
    def show_DB_Work_Shift(self):
        pass

    def edit_WorkShift(self):
        # pass
        print("--- >>>> Welcome to the Edit a Work Shift Section <<<< ---")
        edit_work_shift = input("please Enter the Name of the Work Shift that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Work_Shift" WHERE "Work_Shift_Name" = '{0}'""".format(edit_work_shift)
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Work Shift with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_work_shift()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Work Shift Name>> ---")
                    print("2 --->>> Edit the <<Start Time>> ---")
                    print("3 --->>> Edit the <<End Time>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_w_s_name = input("please Enter the new Work Shift Name that you want : ")
                        st_2 = """UPDATE "Work_Shift" SET "Work_Shift_Name" = '{0}' WHERE "Work_Shift_Name" = '{1}'
                        """.format(edit_w_s_name, edit_work_shift)
                    
                    if loop_check == '2':
                        edit_s_t = input("please Enter the new Start Time that you want : ")
                        st_3 = """UPDATE "Work_Shift" SET "Start_Time" = '{0}' WHERE "Start_Time" = '{1}'
                        """.format(edit_s_t, edit_work_shift)
                    
                    if loop_check == '3':
                        edit_e_t = input("please Enter the new End Time that you want : ")
                        st_4 = """UPDATE "Work_Shift" SET "End_Time" = '{0}' WHERE "End_Time" = '{1}'
                        """.format(edit_e_t, edit_work_shift)

        cur.close()
        conn.commit()

    def delete_WorkShift(self):
        print("--- >>>> Welcome to the Delete a Work Shift Section <<<< ---")
        del_w_s = input("please Enter the Name of the Work Shift that you want to Delete : ")
        st = """SELECT * FROM "Work_Shift" WHERE "Work_Shift_Name" = '{0}'""".format(del_w_s)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Work Shift with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_WorkShift()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Work_Shift"  WHERE "Work_Shift_Name" = '{0}'""".format(del_w_s)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()
        # pass

class Department:
    def __init__(self, dept_name=None, start_work_time=None, end_work_time=None, place=None):
        self.department_name = dept_name
        self.start_work_time = start_work_time
        self.end_work_time = end_work_time
        self.place = place
        self.projects = None
        # return self.department_name
    def __str__(self):
        return self.department_name
    
    def add_Department(self):
        print("--- >>>> Welcom to the Add New Department Section <<<< ---")

        self.department_name = input("please Enter the Name of the New Department that you want to Add : ")
        while(self.department_name == ""):
            print("<<<Attention>>> : Department Name can't be Empty!!!")
            self.department_name = input("---> please Enter the Department Name again!")
        self.start_work_time = input("please Enter the Start Work Time of the Department : ")
        self.end_work_time = input("please Enter the End Work Time of the Department : ")
        self.place = input("please Enter the place of the Department :")
        proj_check = input("if have projects in the department Enter <<1>> : ")
        if proj_check == 1:
            pass
        cur = conn.cursor()

        st = """INSERT INTO "Department"(
	VALUES ('{0}', '{1}', '{2}', '{3}', '{4}'));
    """.format(self.department_name, self.start_work_time, self.end_work_time, self.place, self.project)
        cur.execute(st)
        cur.close()
        conn.commit()
        
    def edit_Department(self):
        # pass
        
        print("--- >>>> Welcome to the Edit a Department Section <<<< ---")
        edit_dept_name = input("please Enter the Name of the Department that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Department" WHERE "Department_Name" = '{0}'""".format(edit_dept_name)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Department with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Department()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Department Name>> ---")
                    print("2 --->>> Edit the <<Start work Time>> ---")
                    print("3 --->>> Edit the <<End work Time>> ---")
                    print("4 --->>> Edit the <<Place>> ---")
                    print("5 --->>> Edit the <<Projects>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_d_name = input("please Enter the new Work Department Name that you want : ")
                        st_2 = """UPDATE "Department" SET "Department_Name" = '{0}' WHERE "Department_Name" = '{1}'
                        """.format(edit_d_name, edit_dept_name)
                    
                    if loop_check == '2':
                        edit_s_w_t = input("please Enter the new Start work Time that you want : ")
                        st_3 = """UPDATE "Department" SET "Start_Work_Time" = '{0}' WHERE "Start_Work_Time" = '{1}'
                        """.format(edit_s_w_t, edit_dept_name)
                    
                    if loop_check == '3':
                        edit_e_w_t = input("please Enter the new End work Time that you want : ")
                        st_4 = """UPDATE "Department" SET "End_Work_Time" = '{0}' WHERE "End_Work_Time" = '{1}'
                        """.format(edit_e_w_t, edit_dept_name)

                    if loop_check == '4':
                        edit_pl = input("please Enter the new place that you want : ")
                        st_5 = """UPDATE "Department" SET "Place" = '{0}' WHERE "Place" = '{1}'
                        """.format(edit_pl, edit_dept_name)
                    
                    if loop_check == '5':
                        edit_pr = input("please Enter the new projects that you want : ")
                        st_6 = """UPDATE "Department" SET "Projects" = '{0}' WHERE "Projects" = '{1}'
                        """.format(edit_pr, edit_dept_name)
        cur.close()
        conn.commit()
    
    def delete_Department(self):
        # pass
        print("--- >>>> Welcome to the Delete a Department Section <<<< ---")
        del_dep = input("please Enter the Name of the Department that you want to Delete : ")
        st = """SELECT * FROM "Department" WHERE "Department_Name" = '{0}'""".format(del_dep)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Department with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Department()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Department"  WHERE "Department_Name" = '{0}'""".format(del_dep)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()

    

class Address:
    def __init__(self, ps_code=None, st=None, ave=None, city=None):
        self.postal_code = ps_code
        self.street = st
        self.avenue = ave
        self.city = city

    def add_Address(self):
        print("--- >>>> Welcom to the Add New Address Section <<<< ---")
        self.postal_code = input("please Enter the Postal Code of the exact Address : ")
        while self.postal_code == "":
            print("<<<Attention>>> : Postal Code can't be Empty!!")
            self.postal_code = input("please Enter the Postal Code again : ")

        self.street = input("please Enter the Name of the Street of the Address : ")
        while self.street == "":
            print("<<<Attention>>> : Street Name can't be Empty!!")
            self.street = input("please Enter the Name of the Street Again : ")

        self.avenue = input("please Enter the Name of the Avenue of the exact Adrress : ")
        while self.avenue == "":
            print("<<<Attention>>> : Avenue Name can't be Empty!!")
            self.avenue = input("please Enter the Name of the Avenue of the exact Address Again : ")

        self.city = input("please Enter the Name of the exact City : ")
        while self.city == "":
            print("<<<Attention>>> : City Name can't be Empty!!")
            self.city = input("please Enter the Name of the Avenue again : ")

        st = """INSERT INTO "Address"(
	VALUES ('{0}', '{1}', '{2}', '{3}'));
    """.format(self.postal_code, self.street, self.avenue, self.city)
        return self

    def edit_Address(self):
        # pass
        
        print("--- >>>> Welcome to the Edit a Address Section <<<< ---")
        edit_adrs = input("please Enter the Postal Code of the Address that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Address" WHERE "Postal_Code" = '{0}'""".format(edit_adrs)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Address with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Address()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Postal_Code>> ---")
                    print("2 --->>> Edit the <<Street>> ---")
                    print("3 --->>> Edit the <<Avenue>> ---")
                    print("4 --->>> Edit the <<City>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_pc = input("please Enter the new Postal Code that you want : ")
                        st_2 = """UPDATE "Address" SET "Postal_Code" = '{0}' WHERE "Postal_Code" = '{1}'
                        """.format(edit_pc, edit_adrs)
                    
                    if loop_check == '2':
                        edit_s = input("please Enter the new Start Time that you want : ")
                        st_3 = """UPDATE "Address" SET "Street" = '{0}' WHERE "Street" = '{1}'
                        """.format(edit_s, edit_adrs)
                    
                    if loop_check == '3':
                        edit_a = input("please Enter the new End Time that you want : ")
                        st_4 = """UPDATE "Address" SET "Avenue" = '{0}' WHERE "Avenue" = '{1}'
                        """.format(edit_a, edit_adrs)

                    if loop_check == '4':
                        edit_c = input("please Enter the new End Time that you want : ")
                        st_5 = """UPDATE "Address" SET "City" = '{0}' WHERE "City" = '{1}'
                        """.format(edit_c, edit_adrs)

        cur.close()
        conn.commit()


    def delete_Address(self):
        # pass
        print("--- >>>> Welcome to the Delete a Address Section <<<< ---")
        del_address = input("please Enter the Postal Code of the Address that you want to Delete : ")
        st = """SELECT * FROM "Address" WHERE "Postal_Code" = '{0}'""".format(del_address)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Address with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Address()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Address"  WHERE "Postal_Code" = '{0}'""".format(del_address)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()


class Person:
    def __init__(self, national_code=None, f_name=None, l_name=None, ps_code=None, phone_num=None):
        self.national_code = national_code
        self.first_name = f_name
        self.last_name = l_name
        self.phone_number = phone_num
        self.postal_code = Address()

    def print_Data_Person(self):
        print("<<<< --- The Entered Data are Equal with : --- >>>>")
        print(">>> the First Name is Equal with : {0}".format(self.first_name))
        print(">>> the Last Name is Equal with : {0}".format(self.last_name))
        print(">>> the National Code is Equal with : {0}".format(self.national_code))
        print(">>> the Phone Number is Equal with : {0}".format(self.phone_number))
        
    def add_Person(self):
        self.first_name = input("please Enter the first name of the Person that you want to add : ")
        self.last_name = input("please Enter the last name of the Person that you want to add : ")
        self.national_code = input("please Enter the National Code of the Person that you want to add : ")
        while self.national_code == "":
            print("<<<Attention>>> : National Code can't be Empty!!")
        self.phone_number = input("please Enter the Phone Number of the Person that you want to Add : ")
        # self.postal_code = input("please Enter the Postal Code of the Person that you want to Add : ")
        self.postal_code = self.postal_code.add_Address()
        # pass
        cur = conn.cursor()
        st = """INSERT INTO "Person"(
	VALUES ('{0}', '{1}', '{2}', '{3}', '{4}'));
    """.format(self.national_code, self.first_name, self.last_name, self.phone_number, self.postal_code)

        cur.execute(st)
        cur.close()
        conn.commit()
    
    def edit_Person(self):
        # pass
        print("--- >>>> Welcom to the Edit a Person Section <<<< ---")
        edit_per = input("please Enter the National Code of the Person that you want to Edit : ")

        cur = conn.cursor()
        st = """SELECT * FROM "Person" WHERE "national_code" = '{0}'""".format(edit_per)
        
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Person with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Person()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<National_Code>> ---")
                    print("2 --->>> Edit the <<First_Name>> ---")
                    print("3 --->>> Edit the <<Last_Name>> ---")
                    print("4 --->>> Edit the <<Phone>> ---")
                    print("5 --->>> Edit the <<Postal_Code>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_nc = input("please Enter the new National Code that you want : ")
                        st_2 = """UPDATE "Person" SET "National_Code" = '{0}' WHERE "National_Code" = '{1}'
                        """.format(edit_nc, edit_per)
                    
                    if loop_check == '2':
                        edit_fn = input("please Enter the new First Name that you want : ")
                        st_3 = """UPDATE "Person" SET "First_Name" = '{0}' WHERE "First_Name" = '{1}'
                        """.format(edit_fn, edit_per)
                    
                    if loop_check == '3':
                        edit_ls = input("please Enter the new Last Name that you want : ")
                        st_4 = """UPDATE "Person" SET "Last_Name" = '{0}' WHERE "Last_Name" = '{1}'
                        """.format(edit_ls, edit_per)

                    if loop_check == '4':
                        edit_p = input("please Enter the new Phone that you want : ")
                        st_5 = """UPDATE "Person" SET "Phone" = '{0}' WHERE "Phone" = '{1}'
                        """.format(edit_p, edit_per)

                    if loop_check == '5':
                        edit_pc = input("please Enter the new Postal Code that you want : ")
                        st_6 = """UPDATE "Person" SET "Postal_Code" = '{0}' WHERE "Postal_Code" = '{1}'
                        """.format(edit_pc, edit_per)
        cur.close()
        conn.commit()

    
    def delete_Person(self):
        print("--- >>>> Welcom to the Delete a Person Section <<<< ---")
        del_person = input("please Enter the National Code of the Person that you want to delete : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Person" WHERE "national_code" = '{0}'""".format(del_person)
        
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Person with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Person()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Person"  WHERE "National_Code" = '{0}'""".format(del_person)
                cur.execute(st_2)
            else:
                pass
        cur.close()
        conn.commit()

        # pass
    
    
class Costumer(Person):
    def __init__(self, customer_id=None):
        self.customer_id = customer_id
    
    def print_Data_Costumer(self):
        self.print_Data_Person()
        print(">>> the Customer ID is Equal with : {0}".format(self.customer_id))

    def add_Customer(self):
        self.add_Person()
        self.customer_id = input("Please Enter the ID of the Exact Customer : ")
        while self.customer_id == "":
            print("<<<Attention>>> : Customer ID can't be Empty!!")
            self.customer_id = input("Please Enter the ID of the Exact Customer Again : ")
        
        cur = conn.cursor()
        st = """INSERT INTO "Costomer"(
	VALUES ('{0}', '{1}'));
    """.format(self.customer_id, self.national_code)

        cur.execute(st)
        cur.close()
        conn.commit()


    def edit_Customer(self):
        # pass

        print("--- >>>> Welcome to the Edit a Customer Section <<<< ---")
        edit_cstmr = input("please Enter the ID of the Customer that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Customer" WHERE "Customer_ID" = '{0}'""".format(edit_cstmr)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Customer with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_customer()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Customer ID>> ---")
                    print("2 --->>> Edit the <<National_Code>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_ci = input("please Enter the new Customer ID that you want : ")
                        st_2 = """UPDATE "Costumer" SET "Customer_ID" = '{0}' WHERE "Customer_ID" = '{1}'
                        """.format(edit_ci, edit_cstmr)
                    
                    if loop_check == '2':
                        edit_nc = input("please Enter the new National Code that you want : ")
                        st_3 = """UPDATE "Costumer" SET "National_Code" = '{0}' WHERE "National_Code" = '{1}'
                        """.format(edit_nc, edit_cstmr)

        cur.close()
        conn.commit()    

    
    def delete_Customer(self):
        print("--- >>>> Welcome to the Delete a Customer Section <<<< ---")
        del_customer = input("please Enter the ID of the Customer that you want to Delete : ")
        st = """SELECT * FROM "Customer" WHERE "Customer_ID" = '{0}'""".format(del_customer)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Customer with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Customer()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Customer"  WHERE "Customer_ID" = '{0}'""".format(del_customer)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()


class Worker(Person):
    def __init__(self, w_id=None, salary=None):
        self.worker_id = w_id
        self.salary = salary
        self.work_shift_name = Work_Shift()
        self.department_name = Department()

    def add_Worker(self):
        self.add_Person()
        self.worker_id = input("please Enter the ID of the Exact Worker : ")
        while self.worker_id == "":
            print("<<<Attention>>> : Worker ID can't be Empty!!")
            self.worker_id = input("please Enter the ID of the Exact Worker Again : ")
        self.salary = input("please Enter the Salary of the Exact Worker : ")
        self.work_shift_name = self.work_shift_name.add_WorkShift()
        self.department_name = self.department_name.add_Department()

        cur = conn.cursor()
        st = """INSERT INTO "Worker"(
	VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
""".format(self.worker_id, self.national_code, self.salary, self.work_shift_name, self.department_name)

        cur.execute(st)
        cur.close()
        conn.commit()

        # self.first_name = input("please Enter the first name of the Worker that you want to add : ")
        # self.last_name = input("please Enter the last name of the worker that you want to add : ")
        # self.national_code = input("please Enter the National Code of the Worker that you want to add : ")
        # self.phone_number = input("please Enter the Phone Number of the Worker that you want to Add : ")
        # self.postal_code = input("please Enter the Postal Code of the Worker that you want to Add : ")
    
    def edit_Worker(self):
        # pass
        print("--- >>>> Welcome to the Edit a Work Shift Section <<<< ---")
        edit_wrkr = input("please Enter the Personnel ID of the Worker that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Worker" WHERE "Worker_ID" = '{0}'""".format(edit_wrkr)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Worker with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Worker()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Worker ID>> ---")
                    print("2 --->>> Edit the <<National Code>> ---")
                    print("3 --->>> Edit the <<Salary>> ---")
                    print("4 --->>> Edit the <<Work Shift Name>> ---")
                    print("5 --->>> Edit the <<Department Name>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_wi = input("please Enter the new Worker ID that you want : ")
                        st_2 = """UPDATE "Worker" SET "Work_Shift_Name" = '{0}' WHERE "Work_Shift_Name" = '{1}'
                        """.format(edit_wi, edit_wrkr)
                    
                    if loop_check == '2':
                        edit_nc = input("please Enter the new National Code that you want : ")
                        st_3 = """UPDATE "Worker" SET "National_Code" = '{0}' WHERE "National_Code" = '{1}'
                        """.format(edit_nc, edit_wrkr)
                    
                    if loop_check == '3':
                        edit_s = input("please Enter the new Salary that you want : ")
                        st_4 = """UPDATE "Worker" SET "Salary" = '{0}' WHERE "Salary" = '{1}'
                        """.format(edit_s, edit_wrkr)

                    if loop_check == '4':
                        edit_wsn = input("please Enter the new Work Shift Name that you want : ")
                        st_5 = """UPDATE "Worker" SET "Work_Shift_Name" = '{0}' WHERE "Work_Shift_Name" = '{1}'
                        """.format(edit_wsn, edit_wrkr)

                    if loop_check == '5':
                        edit_dn = input("please Enter the new Department Name that you want : ")
                        st_6 = """UPDATE "Worker" SET "Department_Name" = '{0}' WHERE "Department_Name" = '{1}'
                        """.format(edit_dn, edit_wrkr)

        cur.close()
        conn.commit()


    def delete_Worker(self):
        # pass
        print("--- >>>> Welcome to the Delete a Worker Section <<<< ---")
        del_worker = input("please Enter the Personnel ID of the Worker that you want to Delete : ")
        st = """SELECT * FROM "Worker" WHERE "Worker_ID" = '{0}'""".format(del_worker)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Worker with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Worker()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Worker"  WHERE "Worker_ID" = '{0}'""".format(del_worker)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()



class Employee(Person):
    def __init__(self, personnel_id=None, vacation=None, salary=None):
        self.personnel_id = personnel_id
        self.vacation = vacation
        self.salary = salary
        self.work_shift_name = None
        self.department_name = Department()
    
    def add_Employee(self):
        # self.first_name = input("please Enter the first name of the Employee the you wnat to add : ")
        # self.last_name = input("please Enter the last name of the Employee that you want to add : ")
        # self.national_code = input("please Enter the National Code of the Employee that you want to add : ")
        # self.phone_number = input("please Enter the Phone Number of the Employee that you want to Add : ")
        # self.postal_code = input("please Enter the Postal Code of the Employee that you want to Add : ")
        self.add_Person()
        self.personnel_id = input("please Enter the Personnel ID of the Exact Employee : ")
        while self.personnel_id == "":
            print("<<<Attention>>> : Personnel ID can't be Empty!!")
            self.personnel_id = input("please Enter the Personnel ID of the Exact Employee Again : ")
        self.vacation = input("please Enter the Vacation of the Exact Employee : ")
        self.salary = input("please Enter the Amount of the Salary of the Exact Employee : ")
        self.department_name.delete_Department = input("Please Enter the Name of the Department of the Exact Employee : ")
        cur = conn.cursor()
        st = """INSERT INTO "Employee"(
VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}'));
""".format(self.personnel_id, self.national_code, self.vacation, self.salary, self.work_shift_name, self.department_name)
    
    def edit_Employee(self):
        # pass

        print("--- >>>> Welcome to the Edit a Employee Section <<<< ---")
        edit_emp = input("please Enter the Personnel ID of the Employee that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Employee" WHERE "Personnel_ID" = '{0}'""".format(edit_emp)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Employee with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Employee()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Personnel ID>> ---")
                    print("2 --->>> Edit the <<National Code>> ---")
                    print("3 --->>> Edit the <<Vacation>> ---")
                    print("4 --->>> Edit the <<Salary>> ---")
                    print("5 --->>> Edit the <<Work Shift Name>> ---")
                    print("6 --->>> Edit the <<Department Name>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_pi = input("please Enter the new Personnel ID that you want : ")
                        st_2 = """UPDATE "Employee" SET "Personnel_ID" = '{0}' WHERE "Personnel_ID" = '{1}'
                        """.format(edit_pi, edit_emp)
                    
                    if loop_check == '2':
                        edit_s_t = input("please Enter the new National Code that you want : ")
                        st_3 = """UPDATE "Employee" SET "National_Code" = '{0}' WHERE "National_Code" = '{1}'
                        """.format(edit_s_t, edit_emp)
                    
                    if loop_check == '3':
                        edit_v = input("please Enter the new Vacation that you want : ")
                        st_4 = """UPDATE "Employee" SET "Vacation" = '{0}' WHERE "Vacation" = '{1}'
                        """.format(edit_v, edit_emp)

                    if loop_check == '4':
                        edit_s = input("please Enter the new Salary that you want : ")
                        st_5 = """UPDATE "Employee" SET "Salary" = '{0}' WHERE "Salary" = '{1}'
                        """.format(edit_s, edit_emp)

                    if loop_check == '5':
                        edit_wsn = input("please Enter the new Work Shift Name that you want : ")
                        st_6 = """UPDATE "Employee" SET "Work_Shift_Name" = '{0}' WHERE "Work_Shift_Name" = '{1}'
                        """.format(edit_wsn, edit_emp)

                    if loop_check == '6':
                        edit_dn = input("please Enter the new Department Name that you want : ")
                        st_7 = """UPDATE "Employee" SET "Department_Name" = '{0}' WHERE "Department_Name" = '{1}'
                        """.format(edit_dn, edit_emp)

        cur.close()
        conn.commit()


    def delete_Employee(self):
        print("--- >>>> Welcome to the Delete a Employee Section <<<< ---")
        del_employee = input("please Enter the Personnel ID of the Employee that you want to Delete : ")
        st = """SELECT * FROM "Employee" WHERE "Personnel_ID" = '{0}'""".format(del_employee)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Employee with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Employee()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Employee"  WHERE "Personnel_ID" = '{0}'""".format(del_employee)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()

        # pass
    
class Distributer(Person):
    def __init__(self, dis_id, account_id=None):
        self.distributer_id = dis_id
        self.account_number = account_id
        self.product_pieces = None
        
    
    def add_Distributer(self):
        print("--- >>>> Welcome to the Add New Distributer Section <<<< ---")
        self.add_Person()
        self.distributer_id = input("please Enter the ID of the Distributer : ")

        while self.distributer_id == "":
            print("<<<Attention>>> : Distributer ID can't be Empty!!")
            self.distributer_id = input("please Enter the ID of the of the Distributer Again : ")
        # national_code = input("please Enter the National Code of the Distributer :")
        # while national_code = "":
        #     print("<<<Attention>>> : National Code can't be Empty!!")
        #     national_code = input("please Enter the National Code of the exact Distributer again : ")
        self.account_number = input("please Enter the Account Number of the exact Distributer : ")
        while self.account_number == "":
            print("<<<Attention>>> : Account Number can't be Empty!!")
            self.account_number = input("please Enter the Account Number of the exact Distributer again : ")
        print("Now you have to add New Pices that the Distributer Produces : ")
        # pass
        cur = conn.cursor()
        st = """INSERT INTO "Distributor"(
	VALUES ('{0}', '{1}', '{2}', '{3}'));
""".format(self.distributer_id, self.national_code, self.account_number, self.product_pieces)

        cur.execute(st)
        cur.close()
        conn.commit()


    def edit_Distributer(self):
        # pass

        print("--- >>>> Welcome to the Edit Distributor Section <<<< ---")
        edit_dsbtr = input("please Enter the ID of the Distributer that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Distributor" WHERE "Distributor_ID" = '{0}'""".format(edit_dsbtr)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Distributor with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_distributer()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Distributor ID>> ---")
                    print("2 --->>> Edit the <<National Code>> ---")
                    print("3 --->>> Edit the <<Account Number>> ---")
                    print("4 --->>> Edit the <<Product Pieces>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_di = input("please Enter the new Distributor_ID that you want : ")
                        st_2 = """UPDATE "Distributor" SET "Distributor_ID" = '{0}' WHERE "Distributor_ID" = '{1}'
                        """.format(edit_di, edit_dsbtr)
                    
                    if loop_check == '2':
                        edit_nc = input("please Enter the new National Code that you want : ")
                        st_3 = """UPDATE "Distributor" SET "National_Code" = '{0}' WHERE "National_Code" = '{1}'
                        """.format(edit_nc, edit_dsbtr)
                    
                    if loop_check == '3':
                        edit_an = input("please Enter the new Account Number that you want : ")
                        st_4 = """UPDATE "Distributor" SET "Account_Number" = '{0}' WHERE "Account_Number" = '{1}'
                        """.format(edit_an, edit_dsbtr)

                    if loop_check == '4':
                        edit_pp = input("please Enter the new Product Pieces that you want : ")
                        st_5 = """UPDATE "Distributor" SET "Product_Pieces" = '{0}' WHERE "Product_Pieces" = '{1}'
                        """.format(edit_pp, edit_dsbtr)

        cur.close()
        conn.commit()
    
    def delete_Distributer(self):
        self.delete_Person()
        print("--- >>>> Welcome to the Delete a Distributer Section <<<< ---")
        del_distributer = input("please Enter the ID of the Distributer that you want to Delete : ")
        st = """SELECT * FROM "Distributer" WHERE "Distributer_ID" = '{0}'""".format(del_distributer)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Distributer with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Distributer()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Distributer"  WHERE "Distributer_ID" = '{0}'""".format(del_distributer)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()

        # pass

class Product:
    def __init__(self, product_name=None, p_id=None, price=None, weight=None):
        self.product_name = product_name
        self.product_id = p_id
        self.price = price
        self.weight = weight

    def add_Product(self):
        print("--- >>>> Welcom to the Add New Product Section <<<< ---")
        self.product_name = input("please Enter the Name of the Product that you want to Add : ")
        self.product_id = input("please Enter the ID of the product that you want to Add : ")
        self.product_price = input("please Enter the Price of the Product that you want to Add : ")
        self.product_weight = input("please Enter the Weight of the Product that you want to Add : ")

        cur = conn.cursor()
        st = """INSERT INTO "Product"(
	VALUES ('{0}', '{1}', '{2}', '{3}'));
""".format(self.product_name, self.product_id, self.product_price, self.product_weight)
        cur.execute(st)
        cur.close()
        conn.commit()
    
    def edit_Product(self):
        # pass
        
        print("--- >>>> Welcome to the Edit a Product Section <<<< ---")
        edit_pro = input("please Enter the Code of the Product that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Product" WHERE "Product_Name" = '{0}'""".format(edit_pro)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Work Shift with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Product()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Product_Name>> ---")
                    print("2 --->>> Edit the <<Product_ID>> ---")
                    print("3 --->>> Edit the <<Price>> ---")
                    print("4 --->>> Edit the <<Weight>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_pn = input("please Enter the new Product Name that you want : ")
                        st_2 = """UPDATE "Product" SET "Product_Name" = '{0}' WHERE "Product_Name" = '{1}'
                        """.format(edit_pn, edit_pro)
                    
                    if loop_check == '2':
                        edit_pi = input("please Enter the new Product ID that you want : ")
                        st_3 = """UPDATE "Product" SET "Product_ID" = '{0}' WHERE "Product_ID" = '{1}'
                        """.format(edit_pi, edit_pro)
                    
                    if loop_check == '3':
                        edit_p = input("please Enter the new Price that you want : ")
                        st_4 = """UPDATE "Product" SET "Price" = '{0}' WHERE "Price" = '{1}'
                        """.format(edit_p, edit_pro)
                    if loop_check == '4':
                        edit_w = input("please Enter the new Weight that you want : ")
                        st_5 = """UPDATE "Product" SET "Weight" = '{0}' WHERE "Weight" = '{1}'
                        """.format(edit_w, edit_pro)

        cur.close()
        conn.commit()


    def delete_product(self):
        # pass
        self.delete_product()
        print("--- >>>> Welcome to the Delete a product Section <<<< ---")
        del_product = input("please Enter the ID of the product that you want to Delete : ")
        st = """SELECT * FROM "product" WHERE "Product_Name" = '{0}'""".format(del_product)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No product with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_product()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Product"  WHERE "Product_Name" = '{0}'""".format(del_product)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()


class Projects:
    def __init__(self, project_id=None, project_name=None, start_date=None, end_date=None):
        self.project_id = project_id
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
    
    def add_Projects(self):
        # pass
        print("--- >>>> Welcom to the Add New 'Project' Section <<<< ---")
        self.project_id = input("please Enter the ID of the Project : ")
        while project_id == "":
            print("<<<Attention>>> : Project ID can't be Empty!!")
            self.project_id = input("---> please Enter the ID of the project :")
        self.start_date_proj = input("please Enter the Start Date of the Project : ")
        self.end_date_proj = input("please Enter the End Date of the Project : ")

        cur = conn.cursor()
        st = """
INSERT INTO "Projects"(
	VALUES ('{0}', '{1}', '{2}', '{3}'));
""".format(self.project_id, self.project_name, self.start_date_proj, self.end_date_proj)
    
    def edit_Projects(self):
        # pass

        print("--- >>>> Welcome to the Edit a Projects Section <<<< ---")
        edit_proj = input("please Enter the ID of the Project that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Projects" WHERE "Project_ID" = '{0}'""".format(edit_proj)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Work Shift with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Projects()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Project ID>> ---")
                    print("2 --->>> Edit the <<Project Name>> ---")
                    print("3 --->>> Edit the <<Start Date>> ---")
                    print("4 --->>> Edit the <<End Date>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_pi = input("please Enter the new Project ID that you want : ")
                        st_2 = """UPDATE "Projects" SET "Project_ID" = '{0}' WHERE "Project_ID" = '{1}'
                        """.format(edit_pi, edit_proj)
                    
                    if loop_check == '2':
                        edit_pn = input("please Enter the new Project Name that you want : ")
                        st_3 = """UPDATE "Projects" SET "Project_Name" = '{0}' WHERE "Project_Name" = '{1}'
                        """.format(edit_pn, edit_proj)
                    
                    if loop_check == '3':
                        edit_sd = input("please Enter the new Start Date that you want : ")
                        st_4 = """UPDATE "Projects" SET "Start_Date" = '{0}' WHERE "Start_Date" = '{1}'
                        """.format(edit_sd, edit_proj)

                    if loop_check == '4':
                        edit_ed = input("please Enter the new End Date that you want : ")
                        st_5 = """UPDATE "Projects" SET "End_Date" = '{0}' WHERE "End_Date" = '{1}'
                        """.format(edit_ed, edit_proj)

        cur.close()
        conn.commit()

    
    def delete_Projects(self):
        # pass
        print("--- >>>> Welcome to the Delete a Projects Section <<<< ---")
        proj_del = input("please Enter the ID of the Project that you want to Delete : ")
        st = """SELECT * FROM "Projects" WHERE "Project_ID" = '{0}'""".format(proj_del)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Project with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Projects()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Projects"  WHERE "Project_ID" = '{0}'""".format(proj_del)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()


class Produce:
    def __init__(self):
        pass
    
    def add_Produce(self):
        pass
    
    def edit_Produce(self):
        pass
    
    def delete_Produce(self):
        pass

class Payment:
    def __init__(self, p_num=None, p_type=None):
        # pass
        self.payment_number = p_num
        self.payment_type = p_type
    
    def add_New_Payment(self):
        # pass
        self.payment_number = input("please Enter the Code of the Exact Payment : ")
        self.payment_type = input("please Enter the Type of the Exact Payment : ")
        cur = conn.cursor()
        # st """   """
        cur.execute(st)
        cur.close()
        conn.commit()
    
    def edit_Payment(self):
        print("--- >>>> Welcome to the Edit a Payment Section <<<< ---")
        edit_pay = input("please Enter the Number of the Payment that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Payment" WHERE "Payment_Num" = '{0}'""".format(edit_pay)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Payment with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Payment()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Payment Num>> ---")
                    print("2 --->>> Edit the <<Payment Type>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_pn = input("please Enter the new Payment that you want : ")
                        st_2 = """UPDATE "Payment" SET "Payment_Num" = '{0}' WHERE "Payment_Num" = '{1}'
                        """.format(edit_pn, edit_pay)
                    
                    if loop_check == '2':
                        edit_pt = input("please Enter the new Payment Type that you want : ")
                        st_3 = """UPDATE "Payment" SET "Payment_Type" = '{0}' WHERE "Payment_Type" = '{1}'
                        """.format(edit_pt, edit_pay)
                    

        cur.close()
        conn.commit()

    
    def delete_Payment(self):
        print("--- >>>> Welcome to the Delete a Payment Section <<<< ---")
        payment_del = input("please Enter the Code of the Payment that you want to Delete : ")
        st = """SELECT * FROM "Payment" WHERE "Payment_Num" = '{0}'""".format(payment_del)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Payment with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Payment()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Payment"  WHERE "Payment_Num" = '{0}'""".format(payment_del)
                cur.execute(st_2)
            else:
                pass

        cur.close()
        conn.commit()
    
class Inventory:
    def __init__(self, p_id=None, invento_num=0):
        # pass
        self.product_id = p_id
        self.inventory_number = invento_num
    
    def add_Inventory(self):
        # pass
        print("--- >>>> Welcome to the Add New Inventory Section <<<< ---")
        self.product_id = input("please Enter Enventory of the Exact Product : ")
        self.inventory_number = input("please Enter the Plenty of the Exact Product that you have : ")
    
    def __str__(self):
        return self.inventory_number
    
    def edit_Inventory(self):
        print("--- >>>> Welcome to the Edit aInventory Section <<<< ---")
        edit_inv = input("please Enter the Name of the Inventory that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Inventory" WHERE "Inventory_num" = '{0}'""".format(edit_inv)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Inventory with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Inventory()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Product ID>> ---")
                    print("2 --->>> Edit the <<Inventory num>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_pi = input("please Enter the new Product ID that you want : ")
                        st_2 = """UPDATE "Inventory" SET "Product_ID" = '{0}' WHERE "Product_ID" = '{1}'
                        """.format(edit_pi, edit_inv)
                    
                    if loop_check == '2':
                        edit_in = input("please Enter the new Inventory num that you want : ")
                        st_3 = """UPDATE "Inventory" SET "Inventory_num" = '{0}' WHERE "Inventory_num" = '{1}'
                        """.format(edit_in, edit_inv)
                    

        cur.close()
        conn.commit()
    
    def delete_Inventory(self):
        # pass
        print("--- >>>> Welcome to the Delete a Inventory Section <<<< ---")
        del_inventory = input("please Enter the Code of the Product that you want to Delete it's Inventory : ")
        st = """SELECT * FROM "Inventory" WHERE "Product_ID" = '{0}'""".format(del_inventory)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        # print(a)
        if a == None:
            print("--->>>Error : There is No Inventory with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Inventory()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Inventory"  WHERE "Product_ID" = '{0}'""".format(del_inventory)
                cur.execute(st_2)
            else:
                pass

class Factor:
    def __init__(self, f_id=None, total_p=None, product=None, product_num=0, pay_id=None):
        # pass
        self.factor_id = f_id
        self.total_price = total_p
        self.product = product
        self.product_number = product_num
        self.payment_id = payment_id

    def add_Factor(self):
        # pass
        print("--- >>>> Welcome to the Add a New Factor Section <<<< ---")
        self.factor_id = input("please Enter the ID of the Exact Factor : ")
        while self.factor_id == "":
            print("<<<Attention>>> : Factor ID can't be Empty!!")
            self.factor_id = input("please Enter the ID of the Exact Factor : ")
        self.total_price = input("please Enter the Total Price of the Exact Factor : ")
        self.product_number = input("please Enter the plenty of the Products in the Factor : ")
        self.payment_id = input("please Enter the ID of the Payment for the Exact Factor : ")
        

    def edit_Factor(self):
        print("--- >>>> Welcome to the Edit a Work Shift Section <<<< ---")
        edit_fctr = input("please Enter the Name of the Work Shift that you want to Edit : ")
        cur = conn.cursor()
        st = """SELECT * FROM "Work_Shift" WHERE "Work_Shift_Name" = '{0}'""".format(edit_fctr)
        cur.execute(st)
        a = cur.fetchone()
        print(a)
        if a == None:
            print("--->>>Error : There is No Work Shift with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.edit_Factor()
            else:
                pass
        else:
            show_ch = input("we have in the DB some data with your Discription : if you want to see it Enter <<<--1-->>> : ")
            if show_ch == '1':
                print(a)
            ed_ch = input("Are you Sure to continue Editing ? Enter <<<--1-->>> : ")
            if ed_ch == '1':
                loop_check = 100
                while loop_check != '0':
                    print("---<<< Choose witch Item you want to Edit : >>>---")
                    print("1 --->>> Edit the <<Factor ID>> ---")
                    print("2 --->>> Edit the <<Total Price>> ---")
                    print("3 --->>> Edit the <<Product>> ---")
                    print("4 --->>> Edit the <<Product Number>> ---")
                    print("5 --->>> Edit the <<Payment ID>> ---")
                    print("0 --->>> to <<Exit>> ---")
                    loop_check = input("---->>>> Make your Choice <<<<--- : ")

                    if loop_check == '1':
                        edit_fi = input("please Enter the new Factor ID Name that you want : ")
                        st_2 = """UPDATE "Factor" SET "Factor_ID" = '{0}' WHERE "Factor_ID" = '{1}'
                        """.format(edit_fi, edit_fctr)
                    
                    if loop_check == '2':
                        edit_tp = input("please Enter the new Total Price that you want : ")
                        st_3 = """UPDATE "Factor" SET "Total_Price" = '{0}' WHERE "Total_Price" = '{1}'
                        """.format(edit_tp, edit_fctr)
                    
                    if loop_check == '3':
                        edit_pr = input("please Enter the new Product that you want : ")
                        st_4 = """UPDATE "Factor" SET "Product" = '{0}' WHERE "Product" = '{1}'
                        """.format(edit_pr, edit_fctr)

                         if loop_check == '4':
                        edit_pn = input("please Enter the new Product Number that you want : ")
                        st_5 = """UPDATE "Factor" SET "Product_Number" = '{0}' WHERE "Product_Number" = '{1}'
                        """.format(edit_pn, edit_fctr)

                         if loop_check == '5':
                        edit_pi = input("please Enter the new Payment ID that you want : ")
                        st_6 = """UPDATE "Factor" SET "Payment_ID" = '{0}' WHERE "Payment_ID" = '{1}'
                        """.format(edit_pi, edit_fctr)

        cur.close()
        conn.commit()
    
    def delete_Factor(self):
        pass
         print("--- >>>> Welcome to the Delete a Factor Section <<<< ---")
        del_Factor = input("please Enter the ID of the Factor that you want to Delete it's Factor : ")
        st = """SELECT * FROM "Factor" WHERE "Product_ID" = '{0}'""".format(del_Factor)
        cur = conn.cursor()
        cur.execute(st)
        a = cur.fetchone()
        
        # print(a)
        if a == None:
            print("--->>>Error : There is No Factor with that Info. try Again --->")
            input_try = input("if you want to try Again Enter <<<1>>> : ")
            if input_try == '1':
                # print("hello")
                self.delete_Factor()
            else:
                pass
        else:
            del_check = input("There is a Row with that info in the DB if you are Sure to delete Enter <<<1>>> --- > : ")
            if del_check == '1':
                st_2 = """DELETE FROM "Factor"  WHERE "Factor_ID" = '{0}'""".format(del_Factor)
                cur.execute(st_2)
            else:
                pass


work_shift_check = Work_Shift()
# work_shift_check.add_WorkShift()
# work_shift_check.edit_WorkShift()
work_shift_check.delete_WorkShift()