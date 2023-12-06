#cnstants thatrepresetn base work hours time and overtime multiplier

base_hours = 40
over_time = 1.5

#Get the hours worked

hours = float(input("Enter the amount of time worked: "))
pay_rate = float(input("Enter hourly pay rate: "))


#Lets see the gross pay

if hours > base_hours:
    #gross pay with overtime

    overtime_hrs = hours - base_hours

    #Amount of overtime pay\
    overtime_pay = overtime_hrs * pay_rate * over_time

    #calculate the gross pay 
    gross_pay = base_hours * pay_rate + overtime_hrs

else:
    gross_pay = hours * pay_rate

#Display the gross pay

print(f'The gross pay is ${gross_pay:,.2f}. ')



