# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:16:50 2020

@author: abdul
"""


from SkiGearRental import SkiGearRental, Customer

def main():
    shop = SkiGearRental(100)
    customer = Customer()

    while True:
        print("""
        ====== Ski Gear Rental House =======
        1. Display available Gears
        2. Request Gear on hourly basis $20/Gear
        3. Request Gear on daily basis $50/Gear
        4. Return Gears
        5. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.displayInventory()
        
        elif choice == 2:
            customer.rentalTime = shop.rentGearOnHourlyBasis(customer.requestGear())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.rentGearOnDailyBasis(customer.requestGear())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.bill = shop.returnGear(customer.returnGear())
            customer.rentalBasis, customer.rentalTime, customer.gears = 0,0,0        
        elif choice == 5:
            break
        else:
            print("Invalid input. Please enter number between 1-5 ")        
    print("Thank you for using the Ski Gear rental system.")


if __name__=="__main__":
    main()