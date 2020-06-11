# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:54:31 2020

@author: abdul
"""

import datetime
import math

class SkiGearRental:
    def __init__(self, inventory =0):
        self.inventory = inventory  ##constructor Class that initiates SkiGear metnod
    
    def displayInventory(self):
        #Displays Gears currently available for rent in the shop.
        print("currently  We have {} Ski Gears available to rent.".format(self.inventory))
        return self.inventory
    
    def rentGearOnHourlyBasis(self, n):
        """
        Rents Gear on hourly basis to a customer.
        """
        if n <= 0:
            print("WARNING !! Number of Gear should be positive!")
            return None
        
        elif n > self.inventory:
            print("Sorry! We have currently {} gears available to rent.".format(self.inventory))
            return None
        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} gears(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $20 for each hour per Gear.")
            print("We hope you enjoy Your Skiing Today.")

            self.inventory -= n
            return now  
        
    def rentGearOnDailyBasis(self, n):
        """
        Rents Gear on hourly basis to a customer.
        """
        if n <= 0:
            print("WARNING !! Number of Gear should be positive!")
            return None

        elif n > self.inventory:
            print("Sorry! We have currently {} gears available to rent.".format(self.inventory))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} gears(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $50 for each day per Gear.")
            print("We hope you enjoy Your Skiing Today.")

            self.inventory -= n
            return now
        
       
    def returnGear(self, request):
        """
        1. Accept a rented Gear from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rentalTime, rentalBasis, numOfGears = request
        bill = 0
        #print("The return Count is : {} ".format(numOfGears))
        print("The Gear was Rented at : {} ".format(rentalTime))
     #   print("The Gear Rental Catagory is : {} ".format(rentalBasis))
        if rentalTime and rentalBasis and numOfGears:
            self.inventory += numOfGears
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
            print("The Gear was Rented for duration : {}  Seconds".format(math.ceil(rentalPeriod)))
           
            # hourly bill calculation
            if rentalBasis == 1:
                bill = math.ceil(rentalPeriod.seconds / 3600) * 20 * numOfGears

            # daily bill calculation
            elif rentalBasis == 2:
                bill = math.ceil(rentalPeriod.days) * 50 * numOfGears
              
                          
            if (3 <= numOfGears <= 5):
                print("You are eligible for Family rental promotion of 20% discount")
                bill = bill * 0.8

            print("Thanks for returning your Gears. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented Gear with Our Company?")
            return None
        

class Customer:

    def __init__(self):
        """
        Customer constructor method which initiates  various customer objects.
        """
        
        self.gears = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestGear(self):
        """
        Takes a request from the customer for the number of Gears.
        """
                      
        gears = input("How many Gears would you like to rent?")
        try:
            gears = int(gears)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if gears < 1:
            print("Invalid input. Number of gears should be greater than zero!")
            return -1
        else:
            self.gears = gears
        return self.gears
     
    def returnGear(self):
        """
        Allows customers to return their gears to Gear shop.
      
        """
        gears = input("How many Gears would you like to Return?") 
        try:
            gears = int(gears)
            self.gears = gears
           # print("CONFIRMED !You want to return {}  Gears ".format(gears))

        except ValueError:
            print("Please enter a valid Gear Count!")
            return -1        
        
        if self.rentalBasis and self.rentalTime and self.gears:
            return self.rentalTime, self.rentalBasis, self.gears  
        else:
            return 0,0,0
        

    
    
    