class city:
    def __init__(self,cityname,areaname,pincode):
        self.cityname = cityname
        self.areaname = areaname
        self.pincode = pincode

    def __repr__(self):
        return f"{self.cityname},{self.areaname},{self.pincode}"
    
class cityStatus():
    def __init__(self,statuscode,message,cityobj):
        self.statuscode = statuscode
        self.message = message
        self.cityobj = cityobj

    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.cityobj}"