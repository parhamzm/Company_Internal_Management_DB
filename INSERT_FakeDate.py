#01 ======================================================================
import psycopg2 as pg2
# from fake import __version__
# import factory
# print(__version__.encode.value)
from faker import Faker

fake1 = Faker()

print(fake1.name())

# print(state.env.get.mro.__call__)

def exveption():
	print("a problem has occured during connection to the data base")
	print("Bye Bye $:")
	exit()

try:
    conn = pg2.connect(database='postgres', user='postgres', password='333')
except:
	exveption()


def enter_Fake_Address():
	cur = conn.cursor()

	st1_address = """"INSERT INTO "Address"(
		VALUES ('9528814252', 'kashani', 'narges', 'kashan'));"""
	cur.execute(st1_address)
	st2_address = """"INSERT INTO "Address"(
		VALUES ('7623591485', 'rejaei', 'sh_sadeghi', 'shiraz'));"""
	cur.execute(st2_address)
	st3_address = """"INSERT INTO "Address"(
		VALUES ('9861856319', 'mosavi', 'salehi', 'natanz'));"""
	cur.execute(st3_address)
	st4_address = """"INSERT INTO "Address"(
		VALUES ('8765208432', 'tabiat', 'teymor', 'ghamsar'));"""
	cur.execute(st4_address)
	st5_address = """"INSERT INTO "Address"(
		VALUES ('8758418765', 'moshtagh', 'gonbad', 'esfahan'));"""
	cur.execute(st5_address)
	st6_address = """"INSERT INTO "Address"(
		VALUES ('8752417850', 'safaeie', 'nastaran', 'delijan'));"""
	cur.execute(st6_address)

	cur.close()
	conn.commit()
#02 ======================================================================
def enter_Fake_Buy():
	cur = conn.cursor()

	st1_buy = """INSERT INTO "Buy"(
		VALUES ('12797', '127', '961223'));"""

	cur.execute(st1_buy)

	st2_buy = """INSERT INTO "Buy"(
		VALUES ('12902', '129', '950612'));"""
	cur.execute(st2_buy)
	st3_buy = """INSERT INTO "Buy"(
		VALUES ('13895', '138', '940419'));"""
	
	cur.execute(st3_buy)

	st4_buy = """INSERT INTO "Buy"(
		VALUES ('14890', '148', '951011'));"""
		
	cur.execute(st4_buy)

	st5_buy = """INSERT INTO "Buy"(
		VALUES ('13054', '130', '960117'));"""
		
	cur.execute(st5_buy)

	st6_buy = """INSERT INTO "Buy"(
		VALUES ('14892', '147', '950928'));"""
	
	cur.execute(st6_buy)

	cur.close()
	conn.commit()

#03 ======================================================================
def enter_Fake_Product():
	cur = conn.cursor()
	st1_Product = """INSERT INTO "Product"(
		VALUES ('rangi', '68922', '500', '90'));"""
	
	cur.execute(st1_Product)

	st2_Product = """INSERT INTO "Product"(
		VALUES ('tablo', '61414', '260', '900'));"""
	
	cur.execute(st2_Product)

	st3_Product = """INSERT INTO "Product"(
		VALUES ('gelim', '60142', '490', '680'));"""
	
	cur.execute(st3_Product)

	st4_Product = """INSERT INTO "Product"(
		VALUES ('nakhi', '68936', '670', '430'));"""
	
	cur.execute(st4_Product)

	st5_Product = """INSERT INTO "Product"(
		VALUES ('abrisham', '61091', '250', '650'));"""
	
	cur.execute(st5_Product)
		
	st6_Product = """INSERT INTO "Product"(
		VALUES ('moket', '69823', '560', '740'));"""
	
	cur.execute(st6_Product)

	cur.close()
	conn.commit()

#04 ======================================================================
def enter_Fake_Customer():
	cur = conn.cursor()

	st1_costumer = """INSERT INTO "Costomer"(
		VALUES ('12797', '1259807232'));"""
	
	cur.execute(st1_costumer)
		
	st2_costumer = """INSERT INTO "Costomer"(
		VALUES ('12902', '1250982346'));"""

	cur.execute(st2_costumer)
		
	st3_costumer = """INSERT INTO "Costomer"(
		VALUES ('13895', '1270871412'));"""
	
	cur.execute(st3_costumer)
		
	st4_costumer = """INSERT INTO "Costomer"(
		VALUES ('14890', '1254309619'));"""
	
	cur.execute(st4_costumer)
		
	st5_costumer = """INSERT INTO "Costomer"(
		VALUES ('13054', '1261835034'));"""
	
	cur.execute(st5_costumer)
		
	st6_costumer = """INSERT INTO "Costomer"(
		VALUES ('14792', '1269872352'));"""
	
	cur.execute(st6_costumer)

	cur.close()
	conn.commit()

#05 ======================================================================
def enter_Fake_Department():
	cur = conn.cursor()

	st1_Department = """INSERT INTO "Department"(
		VALUES ('mashini', '06', '14', 'mashini', 'rangi'));"""
	
	cur.execute(st1_Department)
		
	st2_Department = """INSERT INTO "Department"(
		VALUES ('dasti', '14', '22', 'dasti', 'tablo'));"""
	
	cur.execute(st2_Department)
		
	st3_Department = """INSERT INTO "Department"(
		VALUES ('edari', '22', '06', 'edari', 'gelim'));"""
	
	cur.execute(st3_Department)
		
	st4_Department = """INSERT INTO "Department"(
		VALUES ('tasisat', '06', '14', 'tasisat', 'abrisham'));"""
	
	cur.execute(st4_Department)

		
	st5_Department = """INSERT INTO "Department"(
		VALUES ('mavad', '14', '22', 'mavad', 'moket'));"""
	
	cur.execute(st5_Department)
		
	st6_Department = """INSERT INTO "Department"(
		VALUES ('anbar', '22', '06', 'anbar', 'nakhi'));"""
	
	cur.execute(st6_Department)

	cur.close()
	conn.commit()

#06 ======================================================================
def enter_Fake_Distributor():
	cur = conn.cursor()

	st1_Distributor = """INSERT INTO "Distributor"(
		VALUES ('0237', '1259807232', '781234257823', 'abi'));"""
	
	cur.execute(st1_Distributor)
		
	st2_Distributor = """INSERT INTO "Distributor"(
		VALUES ('0564', '1250982346', '365078124043', 'sabz'));"""
	
	cur.execute(st2_Distributor)
		
	st3_Distributor = """INSERT INTO "Distributor"(
		VALUES ('0193', '1270871412', '254714076762', 'sefid'));"""
	
	cur.execute(st3_Distributor)
		
	st4_Distributor = """INSERT INTO "Distributor"(
		VALUES ('0563', '1254309619', '365473135867', 'ghermez'));"""
	
	cur.execute(st4_Distributor)
		
	st5_Distributor = """INSERT INTO "Distributor"(
		VALUES ('0781', '1261835034', '235647568262', 'ghahveii'));"""
	
	cur.execute(st5_Distributor)
		
	st6_Distributor = """INSERT INTO "Distributor"(
		VALUES ('0564', '1269872352', '769674456454', 'zard'));"""
	
	cur.execute(st6_Distributor)

	cur.close()
	conn.commit()

#07 ======================================================================
def enter_Fake_Employee():
	cur = conn.cursor()

	st1_Employee = """INSERT INTO "Employee"(
	VALUES ('276346', '1259807232', '2', 'Salary', 'sobh', 'mashini'));"""

	cur.execute(st1_Employee)

	st2_Employee = """INSERT INTO "Employee"(
	VALUES ('268496', '1250982346', '4', 'Salary', 'zohr', 'dasti'));"""

	cur.execute(st2_Employee)

	st3_Employee = """INSERT INTO "Employee"(
	VALUES ('206645', '1270871412', '1', 'Salary', 'shab', 'edari'));"""

	cur.execute(st3_Employee)

	st4_Employee = """INSERT INTO "Employee"(
	VALUES ('210571', '1254309619', '5', 'Salary', 'sob', 'tasisat'));"""

	cur.execute(st4_Employee)

	st5_Employee = """INSERT INTO "Employee"(
	VALUES ('278450', '1261835034', '7', 'Salary', 'zohr', 'mavad'));"""

	cur.execute(st5_Employee)

	st6_Employee = """INSERT INTO "Employee"(
	VALUES ('287691', '1269872352', '3', 'Salary', 'shab', 'anbar'));"""

	cur.execute(st6_Employee)

	cur.close()
	conn.commit()

#08 ======================================================================
def enter_Fake_Factor():
	cur = conn.cursor()

	st1_Factor = """INSERT INTO "Factor"(
		VALUES ('961223', '32000', 'ghoghnoos', '5624', '176345936'));"""

	cur.execute(st1_Factor)
		
	st2_Factor = """INSERT INTO "Factor"(
		VALUES ('950612', '56000', 'mahan', '9843', '182353694'));"""
	
	cur.execute(st2_Factor)
		
	st3_Factor = """INSERT INTO "Factor"(
		VALUES ('940419', '12000', 'mahnoos', '1713', '186756239'));"""
	
	cur.execute(st3_Factor)
		
	st4_Factor = """INSERT INTO "Factor"(
		VALUES ('951011', '146000', 'poorsam', '7635', '107685420'));"""

	cur.execute(st4_Factor)
		
	st5_Factor = """INSERT INTO "Factor"(
		VALUES ('960117', '90000', 'mahvash', '1091', '189460987'));"""
	
	cur.execute(st5_Factor)
		
	st6_Factor = """INSERT INTO "Factor"(
		VALUES ('950928', '67000', 'sepid', '8725', '123842308'));"""
	
	cur.execute(st6_Factor)

	cur.close()
	conn.commit()

# 09 ======================================================================
def enter_Fake_Inventory():
	cur = conn.cursor()

	st1_Inventory = """INSERT INTO "Inventory"(
		VALUES ('68922', '43'));"""
	
	cur.execute(st1_Inventory)
		
	st2_Inventory = """INSERT INTO "Inventory"(
		VALUES ('61414', '12'));"""
	
	cur.execute(st2_Inventory)
		
	st3_Inventory = """INSERT INTO "Inventory"(
		VALUES ('60142', '39'));"""
	
	cur.execute(st3_Inventory)
		
	st4_Inventory = """INSERT INTO "Inventory"(
		VALUES ('68936', '70'));"""
	
	cur.execute(st4_Inventory)
		
	st5_Inventory = """INSERT INTO "Inventory"(
		VALUES ('61091', '21'));"""
	
	cur.execute(st5_Inventory)
		
	st6_Inventory = """INSERT INTO "Inventory"(
		VALUES ('69823', '64'));"""
	
	cur.execute(st6_Inventory)

	cur.close()
	conn.commit()

# 10 ======================================================================

def enter_Fake_Payment():
	cur = conn.cursor()

	st1_Payment ="""INSERT INTO "Payment"(
		VALUES ('673458', 'naghdi'));"""
	
	cur.execute(st1_Payment)
		
	st2_Payment ="""INSERT INTO "Payment"(
		VALUES ('917485', 'online'));"""

	cur.execute(st2_Payment)
		
	st3_Payment ="""INSERT INTO "Payment"(
		VALUES ('089147', 'check'));"""
	
	cur.execute(st3_Payment)
		
	st4_Payment ="""INSERT INTO "Payment"(
		VALUES ('865400', 'naghdi'));"""
	
	cur.execute(st4_Payment)
		
	st5_Payment ="""INSERT INTO "Payment"(
		VALUES ('751175', 'online'));"""
	
	cur.execute(st5_Payment)
		
	st6_Payment ="""INSERT INTO "Payment"(
		VALUES ('657140', 'check'));"""
	
	cur.execute(st6_Payment)

	cur.close()
	conn.commit()

# 11 ======================================================================

def enter_Fake_Person():
	cur = conn.cursor()

	st1_Person = """INSERT INTO "Person"(
		VALUES ('1259807232', 'saeed', 'zamani', '09137658294', '9528814252'));"""
	
	cur.execute(st1_Person)
		
	st2_Person = """INSERT INTO "Person"(
		VALUES ('1250982346', 'reza', 'moheb', '09128365746', '7623591485'));"""
	
	cur.execute(st2_Person)
		
	st3_Person = """INSERT INTO "Person"(
		VALUES ('1270871412', 'mohammad', 'tayebi', '09138985512', '9861856319'));"""
	
	cur.execute(st3_Person)
		
	st4_Person = """INSERT INTO "Person"(
		VALUES ('1254309619', 'ali', 'maleki', '09196548293', '8765208432'));"""
	
	cur.execute(st4_Person)
		
	st5_Person = """INSERT INTO "Person"(
		VALUES ('1261835034', 'saleh', 'zahed', '09100067431', '8758418765'));"""
	
	cur.execute(st5_Person)
		
	st6_Person = """INSERT INTO "Person"(
		VALUES ('1269872352', 'gholam', 'noori', '09368234194', '8752417850'));"""
	
	cur.execute(st6_Person)

	cur.close()
	conn.commit()

# 12 ======================================================================

def enter_Fake_Pieces():
	cur = conn.cursor()

	st1_Pieces = """INSERT INTO "Pieces"(
		VALUES ('5718894021', 'rang', '961206', '68922'));"""
	
	cur.execute(st1_Pieces)
		
	st2_Pieces = """INSERT INTO "Pieces"(
		VALUES ('8794514508', 'nakh', '950312', '61414'));"""
	
	cur.execute(st2_Pieces)	
		
	st3_Pieces = """INSERT INTO "Pieces"(
		VALUES ('8762459392', 'chasb', '940824', '60142'));"""
	
	cur.execute(st3_Pieces)
		
	st4_Pieces = """INSERT INTO "Pieces"(
		VALUES ('9815647571', 'dook', '961017', '68936'));"""
	
	cur.execute(st4_Pieces)

	st5_Pieces = """INSERT INTO "Pieces"(
		VALUES ('9801245425', 'soozan', '950311', '61091'));"""
	
	cur.execute(st5_Pieces)
		
	st6_Pieces = """INSERT INTO "Pieces"(
		VALUES ('7625589114', 'takhte', '941208', '69823'));"""
	
	cur.execute(st6_Pieces)

	cur.close()
	conn.commit()

# 13 ======================================================================

def enter_Fake_Produce():
	cur = conn.cursor()

	st1_Produce = """INSERT INTO "Produce"(
		VALUES ('93456', '68922', '961206'));"""
	
	cur.execute(st1_Produce)
		
	st2_Produce = """INSERT INTO "Produce"(
		VALUES ('95643', '61414', '950312'));"""
	
	cur.execute(st2_Produce)
		
	st3_Produce = """INSERT INTO "Produce"(
		VALUES ('97021', '60142', '940824'));"""
	
	cur.execute(st3_Produce)
		
	st4_Produce = """INSERT INTO "Produce"(
		VALUES ('91753', '68936', '961017'));"""
	
	cur.execute(st4_Produce)
		
	st5_Produce = """INSERT INTO "Produce"(
		VALUES ('98712', '61091', '950311'));"""
	
	cur.execute(st5_Produce)
		
	st6_Produce = """INSERT INTO "Produce"(
		VALUES ('94230', '69823', '941208'));"""
	
	cur.execute(st6_Produce)

	cur.close()
	conn.commit()

# 14 ======================================================================

def enter_Fake_WS():
	cur = conn.cursor()
	st1_Work_Shift = """INSERT INTO "Work_Shift"(
		VALUES ('sobh', '06', '14'));"""
	
	cur.execute(st1_Work_Shift)
		
	st2_Work_Shift = """INSERT INTO "Work_Shift"(
		VALUES ('zohr', '14', '22'));"""
	
	cur.execute(st2_Work_Shift)
		
	st3_Work_Shift = """INSERT INTO "Work_Shift"(
		VALUES ('shab', '22', '06'));"""
	
	cur.execute(st3_Work_Shift)
		
	st4_Work_Shift = """INSERT INTO "Work_Shift"(
		VALUES ('sobh', '06', '14'));"""
	
	cur.execute(st4_Work_Shift)
		
	st5_Work_Shift = """INSERT INTO "Work_Shift"(
		VALUES ('zohr', '14', '22'));"""
	
	cur.execute(st5_Work_Shift)
		
	st6_Work_Shift = """INSERT INTO "Work_Shift"(
		VALUES ('shab', '22', '06'));"""
	
	cur.execute(st6_Work_Shift)

	cur.close()
	conn.commit()

# 15 ======================================================================
def enter_Fake_Worker():
	curr = conn.cursor()
	st1_Worker = """INSERT INTO "Worker"(
		VALUES ('71654', '1259807232', '600000', 'sobh', 'mashini');"""
	
	cur.execute(st1_Worker)
		
	st2_Worker = """INSERT INTO "Worker"(
		VALUES ('75140', '1250982346', '950000', 'zohr', 'dasti');"""
	
	cur.execute(st2_Worker)
			
	st3_Worker = """INSERT INTO "Worker"(
		VALUES ('76451', '1270871412', '750000', 'shab', 'edari');"""
	
	cur.execute(st3_Worker)
				
	st4_Worker = """INSERT INTO "Worker"(
		VALUES ('74562', '1254309619', '800000', 'sobh', 'tasisat');"""
	
	cur.execute(st4_Worker)
					
	st5_Worker = """INSERT INTO "Worker"(
		VALUES ('70543', '1261835034', '650000', 'zohr', 'mavad');"""
	
	cur.execute(st5_Worker)
						
	st6_Worker = """INSERT INTO "Worker"(
		VALUES ('78542', '1269872352', '950000', 'shab', 'anbar');"""
	
	cur.execute(st6_Worker)
	cur.close()
	conn.commit()

# 16 ======================================================================
def enter_Fake_Projects():
	cur = conn.cursor()

	st1_Projects = """INSERT INTO "Projects"(
		VALUES ('68922', 'rangi', '970909', '950918'));"""
	
	cur.execute(st1_Projects)
		
	st2_Projects = """INSERT INTO "Projects"(
		VALUES ('61414', 'tablo', '960120', '961015'));"""
	
	cur.execute(st2_Projects)
		
	st3_Projects = """INSERT INTO "Projects"(
		VALUES ('60142', 'gelim', '940329', '950322'));"""
	
	cur.execute(st3_Projects)
		
	st4_Projects = """INSERT INTO "Projects"(
		VALUES ('68936', 'nakhi', '950717', '961108'));"""
	
	cur.execute(st4_address)
		
	st5_Projects = """INSERT INTO "Projects"(
		VALUES ('61091', 'abrisham', '961112', '940603'));"""
	
	cur.execute(st5_Projects)
		
	st6_Projects = """INSERT INTO "Projects"(
		VALUES ('69823', 'moket', '951130', '961209'));"""
	
	cur.execute(st6_Projects)

	cur.close()
	conn.commit()

# END======================================================================

def main():
	loop_check_fake = 1000
	while loop_check_fake != '0':
		print(">>> ---- Welcome to Enter Assumption Data to the DataBase : ")
		print("<<< to Enter Assumption Data for Address --->> 1 <<--- ")
		print("<<< to Enter Assumption Data for Person --->> 2 <<--- ")
		print("<<< to Enter Assumption Data for Worker --->> 3 <<--- ")
		print("<<< to Enter Assumption Data for Distributer --->> 4 <<--- ")
		print("<<< to Enter Assumption Data for Projects --->> 5 <<--- ")
		print("<<< to Enter Assumption Data for Work Shift --->> 6 <<--- ")
		print("<<< to Enter Assumption Data for Pieces --->> 7 <<--- ")
		print("<<< to Enter Assumption Data for Produce --->> 8 <<--- ")
		print("<<< to Enter Assumption Data for Product --->> 9 <<--- ")
		print("<<< to Enter Assumption Data for Buy --->> 10 <<--- ")
		print("<<< to Enter Assumption Data for Department --->> 11 <<--- ")	
		print("***** <<< to Exit --->> 0 <<--- *****")
		pick_choice = input("Please Pick your Favorite : ")

		if pick_choice == '0':
			print("Bye Bye :)")
			break

		if pick_choice == '1':
			print(">>> ---- Assumption Address ----<<<")
			enter_Fake_Address()
		
		if pick_choice == '2':
			print(">>> ---- Assumption Person ----<<<")		
			enter_Fake_Person()

		if pick_choice == '3':
			print(">>> ---- Assumption Worker ----<<<")		
			enter_Fake_Worker()
		
		if pick_choice == '4':
			print(">>> ---- Assumption Distributer ----<<<")		
			enter_Fake_Distributor()

		if pick_choice == '5':
			print(">>> ---- Assumption Projects ----<<<")		
			enter_Fake_Projects()

		if pick_choice == '6':
			print(">>> ---- Assumption Work Shift ----<<<")		
			enter_Fake_WS()
		
		if pick_choice == '7':
			print(">>> ---- Assumption Pieces ----<<<")		
			enter_Fake_Pieces()

		if pick_choice == '8':
			print(">>> ---- Assumption Produce ----<<<")		
			enter_Fake_Produce()
		
		if pick_choice == '9':
			print(">>> ---- Assumption Product ----<<<")
			enter_Fake_Product()
		
		if pick_choice == '10':
			print(">>> ---- Assumption Buy ----<<<")		
			enter_Fake_Buy()

		if pick_choice == '11':
			print(">>> ---- Assumption Department ----<<<")		
			enter_Fake_Department()

conn.close()