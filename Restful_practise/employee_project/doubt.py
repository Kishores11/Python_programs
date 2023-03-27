class Employee(db.Model):
    __tablename__ = "emp"

    id = db.Column(db.Integer,primary_key=True)
    first = db.Column(db.Text)
    last = db.Column(db.Text)

    def __init__(self,first,last):
        self.first = first
        self.last = last

    def __repr__(self):
        return "{} - {}".format(self.first,self.last)

db.create_all()