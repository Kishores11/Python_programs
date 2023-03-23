class Task:
    def __init__(self,taskid,taskname,priority):
        self.id = taskid
        self.name = taskname
        self.priority = priority

    def __repr__(self):
        return f"{self.id},{self.name},{self.priority}"