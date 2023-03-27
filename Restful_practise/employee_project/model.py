from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.model):
    __tablename__= "emp"
    empno = db.Column(db.Integer, primary_key=True)
    empname = db.Column(db.String(100), nullable=False)
    deptid = db.Column(db.Integer, nullable=False)
    mobileno = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def __repr__(self):
	    return f"{self.empno},{self.empname},{self.deptid},{self.mobileno},{self.salary}"