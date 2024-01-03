from classes import Employee, Boss, Seller, Cashier

boss1 = Boss("Hiba", 1234, "Single", "Hay Azli", 6000, 1000)

boss2 = Boss("Aabla", 4321, "Single", "Riad Salam", 7000, 500)

seller1 = Seller("Fatima", 5647, "Married", "Gueliz", 3000, 500, boss2)

cashier1 = Cashier("Ali", 6789, "Single", "Hay Azli", 2000, boss2)

print("Bosses: ")
print(boss1)
print(boss2)
print("\nSellers: ")
print(seller1)
print("\nCashiers: ")
print(cashier1)

print("\nNumber of Employees: ", Employee.get_counter())

print("Number of Bosses: ", Boss.get_counter())

print("Number of Sellers: ", Seller.get_counter())

print("Number of Cashiers: ", Cashier.get_counter())
