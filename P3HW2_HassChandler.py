# Chandler Hass
# 30 March 2025
# P3HW2
# This program calculates how much a employee will be paid for the hours worked

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter Employee's pay rate: "))


if hours_worked > 40:
    overtime_hours = hours_worked - 40  
    overtime_pay = overtime_hours * pay_rate * 1.5  
    regular_pay = 40 * pay_rate  
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate  


gross_pay = regular_pay + overtime_pay

print('--------------------------------')

print('Employee name:  ', employee_name)
print()
print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'Overtime Hours':<20} {'Overtime Pay':<20} {'Regular Pay':<20} {'Gross Pay':<20}")
print('-------------------------------------------------------------------------------------------------------------')
print(f"{hours_worked:<15.2f} {pay_rate:<14.2f} {overtime_hours:<19.2f} ${overtime_pay:<19.2f} ${regular_pay:<19.2f} ${gross_pay:<19.2f}")
