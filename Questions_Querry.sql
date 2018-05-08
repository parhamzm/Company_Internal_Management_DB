select "Costumer_ID",max ("Total_Price")
from "Buy" natural join "Factor"
group by "Costumer_ID"

------------------------------------
SELECT "Total_Price"
FROM "Factor" INNER JOIN "Payment"
USING("Payment_ID")
ORDER BY "Total_Price" DESC
FETCH FIRST 10 ROWS ONLY;

-----------------------------------
select"First_Name","Last_Name" "Postal_Code","Street","Avenue","City"
from "Person" natural join "Employee"
	 natural join "Address"
     
where "City"='کاشان'     
----------------------------------------------
---Q-7
with max_salary(value) as
	(select E."Salary", W."Salary"
    from "Employee" as E, "Worker" as W)

select D."Department_Name" , max_salary."value"
from "Department" as D, "Worker" as W, "Employee" as E, "max_salary"
where W."Department_Name" = D."Department_Name" or E."Department_Name" = D."Department_Name" 
    And (W."Salary" = max_salary.value or E."Salary" = max_salary.value)

---Q8
select "Piece_Name", Max("Piece_Price")
from "Pieces"
where "Piece_Price" >= all(select "Piece_Price"
                          from "Pieces")
group by "Piece_Name"
---------------------------------------

select "Produce_Date",count("Product_ID")
from "Product" natural join "Produce"
group by "Produce_Date";

--------------------------------
select "Pieces_produce_Date","Product_Name" ,"Piece_Name"
from "Produce" natural join 
	 "Product" natural join 
     "Pieces"
     -------------------------------------
select "Payment_Type",count("Product_ID")
from  "Payment" natural join "Factor"
	  natural join  "Product"
      natural join  "Produce"
      where "Produce_ID" between 10::varchar and 20::varchar
      group by "Payment_Type"
      -------------------------------------
      
      select "Department_Name","avg_salary"
from (select "Department_Name" ,avg("Salary")as "avg_salary"
     from "Worker"
     group by "Department_Name" )as "salary_worker" 
where "avg_salary">10   
----------------------------------------
select "Postal_Code","First_Name"
from "Person" natural join "Worker" 
	 natural join "Work_Shift"
where "Work_Shift_Name"='عصر'and
		"Postal_Code" in (select "Postal_Code"
						 from "Person" natural join "Worker" 
						 natural join "Work_Shift"
                         where "Work_Shift_Name"='شب' )
    ------------------------------------
    select count("Personnel_ID"),"Work_Shift_Name"
from "Employee" natural join "Work_Shift"
where "Salary"<2000
group by "Work_Shift_Name"
---------------------------------------

select "First_Name","Postal_Code"
from "Person" as p1 natural join "Costumer"
	natural join "Buy"
    natural join "Factor"
    where "Total_Price">1000::varchar and exists (select *
                                                 from "Person" as p2 natural join "Costumer"
												 natural join "Buy"
                                                 natural join "Factor"
                                                 natural join "Payment"
                                                  where p1."First_Name" = p2."First_Name"
                                                 and "Payment_Type"='چک'
                                                )
        ---------------------------------------------------------------------                        
select "First_Name","Postal_Code"
from "Person" as p1 natural join "Costomer"
	natural join "Buy"
    natural join "Factor"
    where "Total_Price">1000::varchar 
    -------------------------------------------
    
    
    (select "Product_Name", min("Price")as "قیمت "
from "Product"
where "Price" <= all(select "Price"
                     from "Product")
group by "Product_Name")
union
(select "Product_Name", max("Price")
 from "Product"
 where "Price" >= all(select "Price"
                      from "Product")
group by "Product_Name")

---------------------------------------------------------------
---q-5
select count("Produce_ID")
from "Produce"
where "Produce_Date" between 20::varchar and 30::varchar

----------------------------------------------------------------

select "First_Name", sum("Total_Price"::int)
from "Person" natural join "Costumer"
	natural join "Buy"
    natural join "Factor"
group by "First_Name"    
------------------------------------------------
--Q-24
select max("sum"::int)
from
(
    select "First_Name", sum("Total_Price"::int)
 	 from "Person" natural join "Costumer"
	 natural join "Buy"
     natural join "Factor"
 group by "First_Name"
) as test

------------------------------------------

select "City", count ("Personnel_ID")
from "person" natural join "Employee"
             natural join "Address"
             group by "City"

------------------------------------------

select "First_Name","Product_Name","Product_Number"
from  "Person" natural join "Costumer"
		natural join "Buy"
        natural join "Product"
        natural join "Factor"
        
------------------------------------------
