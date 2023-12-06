#cnstants thatrepresetn base work hours time and overtime multiplier

base_hours = 40
over_time = 1.5

#Get the hours worked

hours = float(input("Enter the amount of time worked: "))
pay_rate = float(input("Enter hourly pay rate: "))


#Lets see the gross pay

if hours > base_hours:
    
