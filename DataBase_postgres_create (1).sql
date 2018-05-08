-- Database: db2

-- DROP DATABASE db2;

CREATE DATABASE db2
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Persian_Iran.1256'
    LC_CTYPE = 'Persian_Iran.1256'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;


---------------------------------------------


CREATE TABLE public."Address"
(
    "Postal_Code" character varying COLLATE pg_catalog."default" NOT NULL,
    "Street" character varying COLLATE pg_catalog."default",
    "Avenue" character varying COLLATE pg_catalog."default",
    "City" character varying COLLATE pg_catalog."default",
    state character varying COLLATE pg_catalog."default",
    CONSTRAINT address_pk PRIMARY KEY ("Postal_Code"),
    CONSTRAINT "Address_Postal_Code_key" UNIQUE ("Postal_Code")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Address"
    OWNER to postgres;
    
    
    ----------------------------
-- Table: public."Buy"

-- DROP TABLE public."Buy";

CREATE TABLE public."Buy"
(
    "Costumer_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Factor_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Buy_pkey" PRIMARY KEY ("Costumer_ID", "Product_ID"),
    CONSTRAINT "Buy_fk0" FOREIGN KEY ("Costumer_ID")
        REFERENCES public."Costumer" ("Costumer_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Buy_fk2" FOREIGN KEY ("Product_ID")
        REFERENCES public."Product" ("Product_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Buy_fk3" FOREIGN KEY ("Factor_ID")
        REFERENCES public."Factor" ("Factor_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Buy"
    OWNER to postgres;
    
    
    ------------------------------
  -- Table: public."Costumer"

-- DROP TABLE public."Costumer";

CREATE TABLE public."Costumer"
(
    "Costumer_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "National_Code" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT costomer_pk PRIMARY KEY ("Costumer_ID"),
    CONSTRAINT "Costomer_fk0" FOREIGN KEY ("National_Code")
        REFERENCES public."Person" ("National_Code") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Costumer"
    OWNER to postgres;
    ------------------------------------
 -- Table: public."Department"

-- DROP TABLE public."Department";

CREATE TABLE public."Department"
(
    "Department_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Place" character varying COLLATE pg_catalog."default",
    "Projects_ID" character varying COLLATE pg_catalog."default",
    "End_Work_Time" abstime,
    "Start_Work_Time" abstime,
    CONSTRAINT department_pk PRIMARY KEY ("Department_Name"),
    CONSTRAINT "Department_fk0" FOREIGN KEY ("Projects_ID")
        REFERENCES public."Projects" ("Project_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Department"
    OWNER to postgres;
    -------------------------------------------
 -- Table: public."Distributor"

-- DROP TABLE public."Distributor";

CREATE TABLE public."Distributor"
(
    "Distributor_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "National_Code" character varying COLLATE pg_catalog."default" NOT NULL,
    "Account_Number" character varying COLLATE pg_catalog."default" NOT NULL,
    "Piece_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT distributor_pk PRIMARY KEY ("Distributor_ID"),
    CONSTRAINT "Distributor_fk0" FOREIGN KEY ("National_Code")
        REFERENCES public."Person" ("National_Code") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Distributor_fk1" FOREIGN KEY ("Piece_ID")
        REFERENCES public."Pieces" ("Piece_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Distributor"
    OWNER to postgres;
    -----------------------------------------
 -- Table: public."Employee"

-- DROP TABLE public."Employee";

CREATE TABLE public."Employee"
(
    "Personnel_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "National_Code" character varying COLLATE pg_catalog."default" NOT NULL,
    "Vacation" character varying COLLATE pg_catalog."default",
    "Salary" numeric,
    "Work_Shift_Name" character varying COLLATE pg_catalog."default",
    "Department_Name" character varying COLLATE pg_catalog."default",
    CONSTRAINT employee_pk PRIMARY KEY ("Personnel_ID"),
    CONSTRAINT "Employee_fk0" FOREIGN KEY ("National_Code")
        REFERENCES public."Person" ("National_Code") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Employee_fk1" FOREIGN KEY ("Work_Shift_Name")
        REFERENCES public."Work_Shift" ("Work_Shift_Name") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Employee_fk2" FOREIGN KEY ("Department_Name")
        REFERENCES public."Department" ("Department_Name") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Employee"
    OWNER to postgres;
    -------------------------------------------
    
    
-- Table: public."Factor"

-- DROP TABLE public."Factor";

CREATE TABLE public."Factor"
(
    "Factor_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Total_Price" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product_Number" character varying COLLATE pg_catalog."default" NOT NULL,
    "Payment_ID" character varying COLLATE pg_catalog."default",
    CONSTRAINT factor_pk PRIMARY KEY ("Factor_ID"),
    CONSTRAINT "Factor_fk0" FOREIGN KEY ("Product")
        REFERENCES public."Product" ("Product_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Payment_fk0" FOREIGN KEY ("Payment_ID")
        REFERENCES public."Payment" ("Payment_Num") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Factor"
    OWNER to postgres;
    ------------------------------------------
-- Table: public."Inventory"

-- DROP TABLE public."Inventory";

CREATE TABLE public."Inventory"
(
    "Product_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Inventory_num" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT inventory_pk PRIMARY KEY ("Product_ID", "Inventory_num"),
    CONSTRAINT "Inventory_Product_ID_key" UNIQUE ("Product_ID")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Inventory"
    OWNER to postgres;
    -------------------------------------------
    -- Table: public."Payment"

-- DROP TABLE public."Payment";

CREATE TABLE public."Payment"
(
    "Payment_Num" character varying COLLATE pg_catalog."default" NOT NULL,
    "Payment_Type" character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT payment_pk PRIMARY KEY ("Payment_Num")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Payment"
    OWNER to postgres;
    
    -----------------------
-- Table: public."Person"

-- DROP TABLE public."Person";

CREATE TABLE public."Person"
(
    "National_Code" character varying COLLATE pg_catalog."default" NOT NULL,
    "First_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Last_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Postal_Code" character varying(10) COLLATE pg_catalog."default" NOT NULL,
    "Phone" bigint,
    CONSTRAINT person_pk PRIMARY KEY ("National_Code"),
    CONSTRAINT "Person_fk0" FOREIGN KEY ("Postal_Code")
        REFERENCES public."Address" ("Postal_Code") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Person"
    OWNER to postgres;
    -----------------------------------------
    
   -- Table: public."Pieces"

-- DROP TABLE public."Pieces";

CREATE TABLE public."Pieces"
(
    "Piece_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Piece_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    piece_price integer,
    "Pieces_produce_Date" date,
    CONSTRAINT pieces_pk PRIMARY KEY ("Piece_ID"),
    CONSTRAINT "Pieces_fk0" FOREIGN KEY ("Product_ID")
        REFERENCES public."Product" ("Product_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Pieces"
    OWNER to postgres;
    
    --------------------------------------
    
    
   -- Table: public."Produce"

-- DROP TABLE public."Produce";

CREATE TABLE public."Produce"
(
    "Produce_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Produce_Date" date,
    CONSTRAINT produce_pk PRIMARY KEY ("Produce_ID"),
    CONSTRAINT "Produce_fk0" FOREIGN KEY ("Product_ID")
        REFERENCES public."Product" ("Product_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Produce"
    OWNER to postgres;
    
    
    -----------------------------------
    
    
    
-- Table: public."Product"

-- DROP TABLE public."Product";

CREATE TABLE public."Product"
(
    "Product_Name" character varying COLLATE pg_catalog."default",
    "Product_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Price" character varying COLLATE pg_catalog."default" NOT NULL,
    "Weight" double precision NOT NULL,
    CONSTRAINT product_pk PRIMARY KEY ("Product_ID")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Product"
    OWNER to postgres;
    
    
    
    --------------------------------------------
    
    
  -- Table: public."Projects"

-- DROP TABLE public."Projects";

CREATE TABLE public."Projects"
(
    "Project_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "Project_Name" character varying COLLATE pg_catalog."default",
    "Start_Date" date,
    "End_Date" date,
    CONSTRAINT projects_pk PRIMARY KEY ("Project_ID")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Projects"
    OWNER to postgres;
    
    
    -----------------------------------------
    
    
-- Table: public."Work_Shift"

-- DROP TABLE public."Work_Shift";

CREATE TABLE public."Work_Shift"
(
    "Work_Shift_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Start_Time" abstime,
    "End_Time" abstime,
    CONSTRAINT work_shift_pk PRIMARY KEY ("Work_Shift_Name")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Work_Shift"
    OWNER to postgres;
    
    
    ----------------------------------------------
    
    -- Table: public."Worker"

-- DROP TABLE public."Worker";

CREATE TABLE public."Worker"
(
    "Worker_ID" character varying COLLATE pg_catalog."default" NOT NULL,
    "National_Code" character varying COLLATE pg_catalog."default" NOT NULL,
    "Work_Shift_Name" character varying COLLATE pg_catalog."default",
    "Department_Name" character varying COLLATE pg_catalog."default",
    "Salary" numeric,
    CONSTRAINT worker_pk PRIMARY KEY ("Worker_ID"),
    CONSTRAINT "Worker_fk0" FOREIGN KEY ("National_Code")
        REFERENCES public."Person" ("National_Code") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "Worker_fk1" FOREIGN KEY ("Work_Shift_Name")
        REFERENCES public."Work_Shift" ("Work_Shift_Name") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT worker_fk2 FOREIGN KEY ("Department_Name")
        REFERENCES public."Department" ("Department_Name") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."Worker"
    OWNER to postgres;