//Address:----------------------------------------------------------------------------------

INSERT INTO "Address"(
	VALUES ('9528814252', 'kashani', 'narges', 'kashan'));
    
INSERT INTO "Address"(
	VALUES ('7623591485', 'rejaei', 'sh_sadeghi', 'shiraz'));
    
INSERT INTO "Address"(
	VALUES ('9861856319', 'mosavi', 'salehi', 'natanz'));
   
INSERT INTO "Address"(
	VALUES ('8765208432', 'tabiat', 'teymor', 'ghamsar'));
    
INSERT INTO "Address"(
	VALUES ('8758418765', 'moshtagh', 'gonbad', 'esfahan'));
    
INSERT INTO "Address"(
	VALUES ('8752417850', 'safaeie', 'nastaran', 'delijan'));


//Person--------------------------------------------------------------------------------------

INSERT INTO "Person"(
	VALUES ('1259807232', 'saeed', 'zamani', '09137658294', '9528814252'));
    
    INSERT INTO "Person"(
	VALUES ('1250982346', 'reza', 'moheb', '09128365746', '7623591485'));
    
    INSERT INTO "Person"(
	VALUES ('1270871412', 'mohammad', 'tayebi', '09138985512', '9861856319'));
    
    INSERT INTO "Person"(
	VALUES ('1254309619', 'ali', 'maleki', '09196548293', '8765208432'));
    
    INSERT INTO "Person"(
	VALUES ('1261835034', 'saleh', 'zahed', '09100067431', '8758418765'));
    
    INSERT INTO "Person"(
	VALUES ('1269872352', 'gholam', 'noori', '09368234194', '8752417850'));



//Buy----------------------------------------------------------------------------------------

INSERT INTO "Buy"(
	VALUES ('12797', '127', '961223'));
    
INSERT INTO "Buy"(
	VALUES ('12902', '129', '950612'));
    
INSERT INTO "Buy"(
	VALUES ('13895', '138', '940419'));
    
INSERT INTO "Buy"(
	VALUES ('14890', '148', '951011'));
    
INSERT INTO "Buy"(
	VALUES ('13054', '130', '960117'));
    
INSERT INTO "Buy"(
	VALUES ('14892', '147', '950928'));



//Product-------------------------------------------------------------------------------------

INSERT INTO "Product"(
	VALUES ('rangi', '68922', '500', '90'));
    
    INSERT INTO "Product"(
	VALUES ('tablo', '61414', '260', '900'));
    
    INSERT INTO "Product"(
	VALUES ('gelim', '60142', '490', '680'));
    
    INSERT INTO "Product"(
	VALUES ('nakhi', '68936', '670', '430'));
    
    INSERT INTO "Product"(
	VALUES ('abrisham', '61091', '250', '650'));
    
    INSERT INTO "Product"(
	VALUES ('moket', '69823', '560', '740'));





//Costomer-------------------------------------------------------------------------------------

INSERT INTO "Costomer"(
	VALUES ('12797', '1259807232'));
    
    INSERT INTO "Costomer"(
	VALUES ('12902', '1250982346'));
    
    INSERT INTO "Costomer"(
	VALUES ('13895', '1270871412'));
    
    INSERT INTO "Costomer"(
	VALUES ('14890', '1254309619'));
    
    INSERT INTO "Costomer"(
	VALUES ('13054', '1261835034'));
    
    INSERT INTO "Costomer"(
	VALUES ('14792', '1269872352'));



//Department-----------------------------------------------------------------------------------

INSERT INTO "Department"(
	VALUES ('mashini', '06', '14', 'mashini', 'rangi'));
    
    INSERT INTO "Department"(
	VALUES ('dasti', '14', '22', 'dasti', 'tablo'));
    
    INSERT INTO "Department"(
	VALUES ('edari', '22', '06', 'edari', 'gelim'));
    
    INSERT INTO "Department"(
	VALUES ('tasisat', '06', '14', 'tasisat', 'abrisham'));
    
    INSERT INTO "Department"(
	VALUES ('mavad', '14', '22', 'mavad', 'moket'));
    
    INSERT INTO "Department"(
	VALUES ('anbar', '22', '06', 'anbar', 'nakhi'));





//Distributor-----------------------------------------------------------------------------------

INSERT INTO "Distributor"(
	VALUES ('0237', '1259807232', '781234257823', 'abi'));
    
        INSERT INTO "Distributor"(
	VALUES ('0564', '1250982346', '365078124043', 'sabz'));
    
        INSERT INTO "Distributor"(
	VALUES ('0193', '1270871412', '254714076762', 'sefid'));
    
        INSERT INTO "Distributor"(
	VALUES ('0563', '1254309619', '365473135867', 'ghermez'));
    
        INSERT INTO "Distributor"(
	VALUES ('0781', '1261835034', '235647568262', 'ghahveii'));
    
        INSERT INTO "Distributor"(
	VALUES ('0564', '1269872352', '769674456454', 'zard'));




//Employee-------------------------------------------------------------------------------------

INSERT INTO "Employee"(
VALUES ('276346', '1259807232', '2', 'Salary', 'sobh', 'mashini'));

INSERT INTO "Employee"(
VALUES ('268496', '1250982346', '4', 'Salary', 'zohr', 'dasti'));

INSERT INTO "Employee"(
VALUES ('206645', '1270871412', '1', 'Salary', 'shab', 'edari'));

INSERT INTO "Employee"(
VALUES ('210571', '1254309619', '5', 'Salary', 'sob', 'tasisat'));

INSERT INTO "Employee"(
VALUES ('278450', '1261835034', '7', 'Salary', 'zohr', 'mavad'));

INSERT INTO "Employee"(
VALUES ('287691', '1269872352', '3', 'Salary', 'shab', 'anbar'));




//Factor--------------------------------------------------------------------------------------

INSERT INTO "Factor"(
	VALUES ('961223', '32000', 'ghoghnoos', '5624', '176345936'));
    
    INSERT INTO "Factor"(
	VALUES ('950612', '56000', 'mahan', '9843', '182353694'));
    
    INSERT INTO "Factor"(
	VALUES ('940419', '12000', 'mahnoos', '1713', '186756239'));
    
    INSERT INTO "Factor"(
	VALUES ('951011', '146000', 'poorsam', '7635', '107685420'));
    
    INSERT INTO "Factor"(
	VALUES ('960117', '90000', 'mahvash', '1091', '189460987'));
    
    INSERT INTO "Factor"(
	VALUES ('950928', '67000', 'sepid', '8725', '123842308'));



//Inventory------------------------------------------------------------------------------------


INSERT INTO "Inventory"(
	VALUES ('68922', '43'));
    
    INSERT INTO "Inventory"(
	VALUES ('61414', '12'));
    
    INSERT INTO "Inventory"(
	VALUES ('60142', '39'));
    
    INSERT INTO "Inventory"(
	VALUES ('68936', '70'));
    
    INSERT INTO "Inventory"(
	VALUES ('61091', '21'));
    
    INSERT INTO "Inventory"(
	VALUES ('69823', '64'));



//Payment-------------------------------------------------------------------------------------

INSERT INTO "Payment"(
	VALUES ('673458', 'naghdi'));
    
    INSERT INTO "Payment"(
	VALUES ('917485', 'online'));
    
    INSERT INTO "Payment"(
	VALUES ('089147', 'check'));
    
    INSERT INTO "Payment"(
	VALUES ('865400', 'naghdi'));
    
    INSERT INTO "Payment"(
	VALUES ('751175', 'online'));
    
    INSERT INTO "Payment"(
	VALUES ('657140', 'check'));








//Pieces--------------------------------------------------------------------------------------

INSERT INTO "Pieces"(
	VALUES ('5718894021', 'rang', '961206', '68922'));
    
    INSERT INTO "Pieces"(
	VALUES ('8794514508', 'nakh', '950312', '61414'));
    
    INSERT INTO "Pieces"(
	VALUES ('8762459392', 'chasb', '940824', '60142'));
    
    INSERT INTO "Pieces"(
	VALUES ('9815647571', 'dook', '961017', '68936'));
    
    INSERT INTO "Pieces"(
	VALUES ('9801245425', 'soozan', '950311', '61091'));
    
    INSERT INTO "Pieces"(
	VALUES ('7625589114', 'takhte', '941208', '69823'));




//Produce-------------------------------------------------------------------------------------

INSERT INTO "Produce"(
	VALUES ('93456', '68922', '961206'));
    
    INSERT INTO "Produce"(
	VALUES ('95643', '61414', '950312'));
    
    INSERT INTO "Produce"(
	VALUES ('97021', '60142', '940824'));
    
    INSERT INTO "Produce"(
	VALUES ('91753', '68936', '961017'));
    
    INSERT INTO "Produce"(
	VALUES ('98712', '61091', '950311'));
    
    INSERT INTO "Produce"(
	VALUES ('94230', '69823', '941208'));




//Work_Shift----------------------------------------------------------------------------------

INSERT INTO "Work_Shift"(
	VALUES ('sobh', '06', '14'));
    
    INSERT INTO "Work_Shift"(
	VALUES ('zohr', '14', '22'));
    
    INSERT INTO "Work_Shift"(
	VALUES ('shab', '22', '06'));
    
    INSERT INTO "Work_Shift"(
	VALUES ('sobh', '06', '14'));
    
    INSERT INTO "Work_Shift"(
	VALUES ('zohr', '14', '22'));
    
    INSERT INTO "Work_Shift"(
	VALUES ('shab', '22', '06'));




//Worker-------------------------------------------------------------------------------------

INSERT INTO "Worker"(
	VALUES ('71654', '1259807232', '600000', 'sobh', 'mashini');
    
    INSERT INTO "Worker"(
	VALUES ('75140', '1250982346', '950000', 'zohr', 'dasti');
        
    INSERT INTO "Worker"(
	VALUES ('76451', '1270871412', '750000', 'shab', 'edari');
            
    INSERT INTO "Worker"(
	VALUES ('74562', '1254309619', '800000', 'sobh', 'tasisat');
                
    INSERT INTO "Worker"(
	VALUES ('70543', '1261835034', '650000', 'zohr', 'mavad');
                    
    INSERT INTO "Worker"(
	VALUES ('78542', '1269872352', '950000', 'shab', 'anbar');




//Projects-----------------------------------------------------------------------------------

INSERT INTO "Projects"(
	VALUES ('68922', 'rangi', '970909', '950918'));
    
    INSERT INTO "Projects"(
	VALUES ('61414', 'tablo', '960120', '961015'));
    
    INSERT INTO "Projects"(
	VALUES ('60142', 'gelim', '940329', '950322'));
    
    INSERT INTO "Projects"(
	VALUES ('68936', 'nakhi', '950717', '961108'));
    
    INSERT INTO "Projects"(
	VALUES ('61091', 'abrisham', '961112', '940603'));
    
    INSERT INTO "Projects"(
	VALUES ('69823', 'moket', '951130', '961209'));