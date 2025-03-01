from structural.proxy.EmployeeImpl import EmployeeImpl
from structural.proxy.IEmployee import IEmployee


class AuthProxy(IEmployee):

    def create(self,role,childDetails, childObj):
        if role == "ADMIN":
            childObj.create(childDetails,childObj)
        else:
            print("Create operation with given user role not accepted!!")

