from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testr.db'
db = SQLAlchemy(app)
app.app_context().push()



class EmployeeModel(db.Model):
    __tablename__= "emp"
    empno = db.Column(db.Integer, primary_key=True)
    empname = db.Column(db.String(100), nullable=False)
    deptid = db.Column(db.Integer, nullable=False)
    mobileno = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def __repr__(self):
	    return f"{self.empno},{self.empname},{self.deptid},{self.mobileno},{self.salary}"

db.create_all()

emp_put_args = reqparse.RequestParser()
emp_put_args.add_argument("empname", type=str, help="Name of the employee is required", required=True)
emp_put_args.add_argument("deptid", type=int, help="deptid of emp", required=True)
emp_put_args.add_argument("mobileno", type=int, help="mobile no of emp", required=True)
emp_put_args.add_argument("salary", type=int, help="salary of emp", required=True)

emp_update_args = reqparse.RequestParser()
emp_update_args.add_argument("name", type=str, help="Name of the employee is required")
emp_update_args.add_argument("deptid", type=int, help="deptid of the emp")
emp_update_args.add_argument("mobileno", type=int, help="mobileno of the emp")
emp_put_args.add_argument("salary", type=int, help="salary of emp")

resource_fields = {
	'empno': fields.Integer,
	'empname': fields.String,
	'deptid': fields.Integer,
	'mobileno': fields.Integer,
    'salary': fields.Integer,
}

class Employee(Resource):
	@marshal_with(resource_fields)
	def get(self, empno):
		result = EmployeeModel.query.filter_by(empno=empno).first()
		if not result:
			abort(404, message="Could not find employee with that id")
		return result
        
	@marshal_with(resource_fields)
	def post(self, empno):
		args = emp_put_args.parse_args()
		result = EmployeeModel.query.filter_by(empno=empno).first()
		if result:
			abort(409, message="emp id taken...")

		emp = EmployeeModel(empno=empno, empname=args['empname'], deptid=args['deptid'], mobileno=args['mobileno'], salary=args['salary'])
		db.session.add(emp)
		db.session.commit()
		return emp, 201




api.add_resource(Employee, '/data/<int:empno>')




if __name__ == '__main__':
    app.run(debug=True)