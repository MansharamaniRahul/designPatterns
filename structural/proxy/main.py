from structural.proxy.AuthProxy import AuthProxy
from structural.proxy.EmployeeImpl import EmployeeImpl


def main():
    authProxcy=AuthProxy()
    authProxcy.create("ADMIN",{"name":"XYZ"}, EmployeeImpl())
    authProxcy.create("Normal User", {"name": "XYZ"}, EmployeeImpl())

if __name__ == "__main__":
    main()