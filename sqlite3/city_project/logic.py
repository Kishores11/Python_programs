from db import addCityInfo, changeCityInfo, changeAreaInfo, viewCityInfo, pincodeInfo, sortCityInfo, sortAreaInfo, sortPinInfo

def addCity(info):
    msg = addCityInfo(info)
    return msg

def changeCity(a,b):
    msg = changeCityInfo(a,b)
    return msg

def changeArea(a,b):
    msg = changeAreaInfo(a,b)
    return msg   

def viewCity(info):
    msg = viewCityInfo(info)
    return msg   

def pincode(info):
    msg = pincodeInfo(info)
    return msg  

def sortCity():
    msg = sortCityInfo()
    return msg

def sortArea():
    msg = sortAreaInfo()
    return msg

def sortPin():
    msg = sortPinInfo()
    return msg