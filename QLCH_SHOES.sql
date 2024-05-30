DROP DATABASE IF EXISTS QLCH_SHOES;
CREATE DATABASE QLCH_SHOES;
USE QLCH_SHOES;

DROP TABLE IF EXISTS CUSTOMER; 
CREATE TABLE CUSTOMER(
	CustomerId CHAR(4) PRIMARY KEY,
    CustomerName NVARCHAR(50) ,
    CustomerPhone INT ,
    CustomerEmail VARCHAR(50) ,
    CustomerAddress NVARCHAR(100)
);

DROP TABLE IF EXISTS INVOICE_DETAILS;
CREATE TABLE INVOICE_DETAILS (
	ProductId INT ,
    InvoiceId INT ,
    Quantity INT ,
    
    PRIMARY KEY(ProductId, InvoiceId)
);

DROP TABLE IF EXISTS INVOICE;
CREATE TABLE INVOICE (
	InvoiceId INT PRIMARY KEY,
    CustomerName NVARCHAR(50),
    StaffId CHAR(4) ,
    Payments NVARCHAR(50),
    Date_ DATETIME DEFAULT NOW(),
    Total INT 
    
);

DROP TABLE IF EXISTS PRODUCT;
CREATE TABLE PRODUCT (
	ProductId INT PRIMARY KEY,
    ProductName NVARCHAR(30),
    ProductDescription NVARCHAR(50),
    ProductPrice INT
);

DROP TABLE IF EXISTS STAFF;
CREATE TABLE STAFF (
	StaffId CHAR(4) PRIMARY KEY,
    StaffName NVARCHAR(25),
    StaffAddress NVARCHAR(100),
    StaffRole NVARCHAR(30),
    StaffPhone CHAR(10),
    RankSalary INT,
    BankAccNumber BIGINT,
    BankName NVARCHAR(30),
    Status_ boolean,
    Username varchar(50),
    Password_ varchar(50),
    isAdmin boolean
);



DROP TABLE IF EXISTS STORE;
CREATE TABLE STORE (
	StoreId CHAR(4) PRIMARY KEY,
    StoreHotline INT ,
    StoreAddress NVARCHAR(100),
    StaffQuantity INT
);


-- ALTER TABLE INVOICE ADD CONSTRAINT fk_CustomerId
-- FOREIGN KEY (CustomerId) REFERENCES CUSTOMER(CustomerId);


ALTER TABLE INVOICE_DETAILS ADD CONSTRAINT fk_InvoiceId
FOREIGN KEY (InvoiceId) REFERENCES INVOICE(InvoiceId);

ALTER TABLE INVOICE_DETAILS ADD CONSTRAINT fk_ProductId
FOREIGN KEY (ProductId) REFERENCES PRODUCT(ProductId);


ALTER TABLE INVOICE ADD CONSTRAINT fk_StaffIdV2
FOREIGN KEY (StaffId) REFERENCES STAFF(StaffId);

INSERT INTO STAFF (
	StaffId,
    StaffName,
    StaffAddress,
    StaffRole,
    StaffPhone,
    RankSalary,
    BankAccNumber,
    BankName,
    Status_,
    Username,
    Password_,
    isAdmin 
)
VALUES (
"0001",
"Nguyễn Thành Tài",
"Bach khoa",
"Admin",
"0987654321",
10,
987654321,
"vietin",
1,
"ntt01",
"123456",
1
);

INSERT INTO CUSTOMER (CustomerId, CustomerName, CustomerPhone, CustomerEmail, CustomerAddress)
VALUES ('0', 'Khách lẻ', 123456789, 'cus_mail@gmail.com', ' ');
