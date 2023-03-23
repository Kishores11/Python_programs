from db import ifPresent, addTaskInfo, updateTaskInfo, viewTaskInfo, removeTaskInfo


def present(id):
    msg = ifPresent(id)
    return msg


def addTask(info):
    msg = addTaskInfo(info)
    return msg

def updateTask(info):
    msg = updateTaskInfo(info)
    return msg

def viewTask(info):
    msg = viewTaskInfo(info)
    return msg

def removeTask(info):
    msg = removeTaskInfo(info)
    return msg
