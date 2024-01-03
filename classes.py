from abc import ABCMeta, abstractmethod

class Employee(metaclass = ABCMeta):
    __counter = 0
    def __init__(self, name, SSN, marital_status, address, base_salary):
        self.__name = name
        self.__SSN = SSN
        self.__marital_status = marital_status
        self.__address = address
        self.__base_salary = base_salary
        Employee.__counter += 1
        self.__ID = Employee.__counter


    @property
    def get_name(self):
        return self.__name

    @property
    def get_SSN(self):
        return self.__SSN

    @property
    def get_ms(self):
        return self.__marital_status

    @property
    def get_adr(self):
        return self.__address

    @property
    def get_base_salary(self):
        return self.__base_salary

    @staticmethod
    def get_counter():
        return Employee.__counter

    @property
    def get_ID(self):
        return self.__ID

    @abstractmethod
    def Salary():
        pass
    
    def __str__(self):
        return f"{self.__name}; ID: {self.__ID}; SSN: {self.__SSN}; Marital Status: {self.__marital_status}; \
Address: {self.__address}; Base Salary: {self.__base_salary}"

    def __eq__(self, other):
        return self.__ID == other.__ID and self.Salary() == other.Salary()


class Boss(Employee):
    __counter = 0
    def __init__ (self, name, SSN, marital_status, address, base_salary, risk_premium):
        super().__init__(name, SSN, marital_status, address, base_salary)
        self.__risk_premium = risk_premium
        Boss.__counter += 1
        self.__ID = Employee.get_counter

    @staticmethod
    def get_counter():
        return Boss.__counter

    @property
    def get_rp(self):
        return self.__risk_premium

    def Salary(self):
        return  self.get_base_salary + self.__risk_premium


    def __str__(self):
        return f"Boss {super().__str__()} ; Risk Premium: \
{self.__risk_premium}; Salary: {self.Salary()}"


class Seller(Employee):
    __counter = 0
    def __init__ (self, name, SSN, marital_status, address, base_salary, commission, supervisor):
        super().__init__(name, SSN, marital_status, address, base_salary)
        self.__commission = commission
        self.__supervisor = supervisor
        Seller.__counter += 1
        self.__ID = Employee.get_counter

    @property
    def get_com(self):
        return self.__commission

    @staticmethod
    def get_counter():
        return Seller.__counter

    @property
    def get_supervisor(self):
        return self.__supervisor    

    def Salary(self):
        return  self.get_base_salary + self.__commission

    def __str__(self):
        return f"Seller {super().__str__()}; Commission: {self.__commission}; Salary: {self.Salary()}; \
Supervisor:({self.__supervisor.get_name}, ID: {self.__supervisor.get_ID})"
    

    
class Cashier(Employee):
    __counter = 0
    def __init__ (self, name, SSN, marital_status, address, base_salary, supervisor):
        super().__init__(name, SSN, marital_status, address, base_salary)
        self.__supervisor = supervisor
        Cashier.__counter += 1
        self.__ID = Employee.get_counter

    @staticmethod
    def get_counter():
        return Cashier.__counter

    @property
    def get_supervisor(self):
        return self.__supervisor    

    def Salary(self):
        return self.get_base_salary

    def __str__(self):
        return f"Cashier {super().__str__()}; Supervisor:({self.__supervisor.get_name},\
ID: {self.__supervisor.get_ID})"
