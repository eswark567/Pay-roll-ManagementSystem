import sqlite3


class Employee:
    
    def empinsert(self,**k):
        conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f'''insert into Employee_details 
                    values({k['Eid']},"{k['Ename']}",{k['DeptId']},
                    "{k['Designation']}","{k['Email']}",
                    {k['Contact_no']},"{k["Address"]}")''')
        conn.commit()
        print("Data has been inserted Successfully")

    def empfetch(self):
        conn=sqlite3.connect('pms.db')
        #creating cursor
        cur=conn.cursor()
        cur.execute("select * from Employee_Details")
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
        return data

    def attendence(self,**k):
        conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f'''insert into Attendence Values
                    ({k['Eid']},"{k['Ename']}",{k['DeptId']},
                    "{k['DeptName']}","{k['Date']}","{k['time_in']}",
                    "{k['time_out']}") ''')
        conn.commit()
        print("DAta in attendence is inserted succesfully")
    
    def salary(self,**k):
        conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f'''insert into Salary values
                    ({k['Eid']},{k['DeptId']},{k['Account_number']},
                    "{k['PAN']}",{k['Base_sal']}) ''')
        conn.commit()

class SalaryCalci:
    def salaryCalculator(self,eid):
        conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f"select base_sal from salary where eid={eid}")
        bs=cur.fetchall()[0][0]
        cur.execute(f"select date,time_in,time_out from attendence where eid={eid}")
        wd=cur.fetchall()
        hrs=bs/(22*8)
        su=0
        for i in wd:
            c=(int(i[2][:2])-int(i[1][:2]))*hrs
            su=su+c
        return su