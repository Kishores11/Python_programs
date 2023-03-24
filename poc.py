from flask import Flask, request, json
from logic import areaof
from model import employee, employeeStatus

app = Flask(__name__)


@app.route('/poc/<x>', methods=['GET'])
def poc(x):
    return "poc " + x


@app.route('/poc1/', methods=['POST'])
def poc1():
    data = request.form['name']
    return "poc1 " + data


@app.route('/getsomenumber/', methods=['GET'])
def getsomenumber():
    l1 = [3, 4, 5]
    data = request.form['number']
    return l1


@app.route('/getdict/', methods=['GET'])
def getdict():
    d1 = {1: 'kishore',2: 'mahesh'}
    data = request.form['number']
    print(f"Value is {data}")
    return d1


@app.route('/mbr/', methods=['POST'])
def mbr():
    d1 = {'perimeter': 23, 'area': 45}
    a = request.json
    print(a['length'])
    print(a['breadth'])
    return d1


@app.route('/area/', methods=['POST'])
def area1():
    a = request.json
    len = a['length']
    bre = a['breadth']
    data = areaof(len, bre)
    return data


@app.route('/employeecode/<x>', methods=['GET'])
def employeecode(x):
    emp1 = employee(x, "kishore", 11, "karur")
    e = emp1.__dict__
    e1 = employeeStatus(1, "got employee", e)
    l1 = json.dumps(e1.__dict__)
    return l1


@app.route('/employeedept/', methods=['GET'])
def employeedept():
    list1 = []
    emp1 = employee(1, 'kishore', 11, 'karur')
    if int(request.form['num']) == emp1.dept_id:
        e = emp1.__dict__
        e1 = employeeStatus(1, "got employee", e)
        l1 = e1.__dict__
        list1.append(l1)
        return list1

    else:
        e2 = employeeStatus(0, "not got", None)
        l2 = e2.__dict__
        list1.append(l2)
        return list1


if __name__ == '__main__':
    app.run(debug=True)
