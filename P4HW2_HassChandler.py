# Chandler Hass
# 13 April 2025
# P4HW2 
# Payroll Calculation in python



total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

 
    if hours_worked > 40:
        overtime_hours = hours_worked - 40  
        overtime_pay = overtime_hours * pay_rate * 1.5  
        regular_pay = 40 * pay_rate  
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate  

    gross_pay = regular_pay + overtime_pay

 
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    print('--------------------------------')
    print('Employee name:  ', employee_name)
    print()
    print(f"{'Hours Worked':<15} {'Pay Rate':<15} {'Overtime Hours':<20} {'Overtime Pay':<20} {'Regular Pay':<20} {'Gross Pay':<20}")
    print('-------------------------------------------------------------------------------------------------------------')
    print(f"{hours_worked:<15.2f} {pay_rate:<14.2f} {overtime_hours:<19.2f} ${overtime_pay:<19.2f} ${regular_pay:<19.2f} ${gross_pay:<19.2f}")
    print()


print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

