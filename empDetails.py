import sqlite3

conn=sqlite3.connect('pms.db')

cur=conn.cursor()

class Employee:
    def empinsert(self,**k):
        cur.execute(f'''insert into Employee_details 
                    values({k['Eid']},"{k['Ename']}",{k['DeptId']},
                    "{k['Designation']}","{k['Email']}",
                    {k['Contact_no']},"{k["Address"]}")''')
        conn.commit()
        print("Data has been inserted Successfully")
