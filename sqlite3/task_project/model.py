class Task:
    def __init__(self,id,name,desc,priority):
        self.id = id
        self.name = name
        self.desc = desc
        self.priority = priority


    def __repr__(self):
        return f"{self.id},{self.name},{self.desc},{self.priority}"