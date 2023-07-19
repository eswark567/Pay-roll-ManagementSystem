from empDetails import Employee
from flask import Flask,render_template,jsonify,request

app=Flask(__name__)
emp=Employee()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])
def empSignup():
    if request.method=='POST':
        eid = request.form.get('eid')
        ename=request.form.get('ename')
        deptid=request.form.get('deptid')
        designation=request.form.get('designation')
        email=request.form.get('email')
        contact=request.form.get('contact')
        address=request.form.get('address')
        print(eid,ename,designation,email,contact,address)
        emp.empinsert(Eid=eid,Ename=ename,DeptId=deptid,Designation=designation,Email=email,Contact_no=contact,Address=address)
        return jsonify({'Message':"Successfully fetched the data"})
    else:
        return render_template('signup.html')
@app.route('/employees',methods=['GET','POST'])
def Esh():
    data= emp.empfetch()
    return render_template('employees.html',employees=data)

@app.route('/attendance',methods=['GET','POST'])
def attendence():
    if request.method=='POST':
        eid = request.form.get('eid')
        ename=request.form.get('ename')
        deptid=request.form.get('deptid')
        deptname=request.form.get('deptname')
        date=request.form.get('date')
        time_in=request.form.get('time_in')
        time_out=request.form.get('time_out')
        emp.attendence(Eid=eid,Ename=ename,DeptId=deptid,DeptName=deptname,Date=date,time_in=time_in,time_out=time_out)
    return render_template("attendence.html")
@app.route('/SalaryDetai',methods=['GET','POST'])
def salary():
    if request.method=='POST':
        eid = request.form.get('eid')
        deptid=request.form.get('deptid')
        account_number=request.form.get('account_number')
        pan=request.form.get('pan')
        base_sal=request.form.get('base_sal')
        emp.salary(Eid=eid,DeptId=deptid,Account_number=account_number,PAN=pan,Base_sal=base_sal)
        return jsonify({'message':'successfully inserted'})
    return render_template("SalaryDet.html")

if __name__=='__main__':
    app.run()






#emp.empinsert(Eid=1,Ename="Rakesh",DeptId=10,Designation="CEO",Email="rakesh123@gmail.com",Contact_no=789276367,Address="Pune")