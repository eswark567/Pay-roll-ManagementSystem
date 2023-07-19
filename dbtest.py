import sqlite3
#creating connection 


#cur.execute(f"create table Employee_Details (Eid int primary key,Ename varchar(45),DeptId int,Designation Varchar(40),Email varchar(40),Contact_no longint,Address varchar(70))")
#cur.execute(f"create table Salary(Eid int,DeptId int primary key,Account_number int, PAN varchar(15),Base_sal int, FOREIGN KEY (Eid) REFERENCES Employee_Details(Eid))")
#cur.execute(f"create table Attendence(Eid int,Ename varchar(40),DeptId int, DeptName varchar(20),Date datetime,time_in datetime,time_out datetime,FOREIGN KEY (Eid) REFERENCES Employee_Details(Eid),FOREIGN KEY (DeptId) REFERENCES Salary(DeptId))")
#def show_employees(self):
conn=sqlite3.connect('pms.db')
    #creating cursor
cur=conn.cursor()
cur.execute("delete from employee_details")
print("Delete succesfully")
conn.commit()

'''cur.execute("select * from employee_details")
data=[]

for i in cur.fetchall():
    context={}
    context['Eid']=i[0]
    context['Ename']=i[1]
    context['DeptId']=i[2]
    context['Designation']=i[3]
    context['Email']=i[4]
    context['Contact_no']=i[5]
    context['Address']=i[6]
    data.append(context)
print (data)'''

#from empDetails import Employee

#emp2=Employee()
#emp2.attendence(Eid=245,Ename="hfhgv",DeptId=78,DeptName="CSE",Date="07/12/2000",time_in="09:00",time_out="17:00")
#emp2.salary(Eid=123,DeptId=456,Account_number=1121,PAN="hvhuhb675",Base_sal=24615)

from empDetails import SalaryCalci
emp1=SalaryCalci()
emp1.salaryCalculator(eid=1)