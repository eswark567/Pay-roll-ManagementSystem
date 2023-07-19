import sqlite3
#creating connection 
conn=sqlite3.connect('pms.db')
#creating cursor
cur=conn.cursor()

cur.execute(f"create table Employee_Details (Eid int primary key,Ename varchar(45),DeptId int,Designation Varchar(40),Email varchar(40),Contact_no longint,Address varchar(70))")
cur.execute(f"create table Salary(Eid int,DeptId int primary key,Account_number int, PAN varchar(15),Base_sal int, FOREIGN KEY (Eid) REFERENCES Employee_Details(Eid))")
cur.execute(f"create table Attendence(Eid int,Ename varchar(40),DeptId int, DeptName varchar(20),Date datetime,time_in datetime,time_out datetime,FOREIGN KEY (Eid) REFERENCES Employee_Details(Eid),FOREIGN KEY (DeptId) REFERENCES Salary(DeptId))")
conn.commit()
conn.close()

