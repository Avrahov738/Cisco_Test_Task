-- Members Table
CREATE TABLE Members (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    ADDRESS VARCHAR(100),
    PHONE_NUMBER VARCHAR(20),
    AGE INT
);

-- Organization Table
CREATE TABLE Organization (
    ID INT PRIMARY KEY,
    MEMBER_ID INT,
    LOCATION VARCHAR(50),
    DUES DECIMAL(10, 2)
);


INSERT INTO Members (ID, NAME, ADDRESS, PHONE_NUMBER, AGE)
VALUES
    (1, 'John Doe', '123 Main St', '555-1234', 35),
    (2, 'Jane Smith', '456 Oak Ave', '555-5678', 42),
    (3, 'Michael Johnson', '789 Elm Rd', '555-9876', 50),
    (4, 'Sarah Lee', '321 Pine Ln', '555-1111', 28),
    (5, 'David Brown', '654 Maple Dr', '555-2222', 38);

-- Insert random values into Organization table
INSERT INTO Organization (ID, MEMBER_ID, LOCATION, DUES)
VALUES
    (1, 1, 'New York', 100.50),
    (2, 2, 'Los Angeles', 75.25),
    (3, 3, 'Chicago', 50.75),
    (4, 4, 'Houston', 0),
    (5, 5, 'Dallas', 25.10);


/* 1. Write a query that lists each member name, address, dues, and location. */
SELECT M.NAME, M.ADDRESS, O.DUES, O.LOCATION
FROM Members M
JOIN Organization O ON M.ID = O.MEMBER_ID;

/* 2.Write a SQL Query to pull all members that are over 45.*/

SELECT *
FROM Members
WHERE AGE > 45;

/*3.Write a SQL Query to pull all members that have a dues value of 0.*/

SELECT M.*
FROM Members M
JOIN Organization O ON M.ID = O.MEMBER_ID
WHERE O.DUES = 0;