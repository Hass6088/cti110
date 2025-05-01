# Your Name
# 03/16/2025
# P2HW2
# sum of grades, and the average grade formatted to two decimal places.

module_1 = float(input('Enter Grade for Module 1: '))
module_2 = float(input('Enter Grade for Module 2: '))
module_3 = float(input('Enter Grade for Module 3: '))
module_4 = float(input('Enter Grade for Module 4: '))
module_5 = float(input('Enter Grade for Module 5: '))
module_6 = float(input('Enter Grade for Module 6: '))

module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]

lowest_grade = min(module_grades)
highest_grade = max(module_grades)

total_grades = sum(module_grades)

average_grade = total_grades / len(module_grades)

print("\n-----------Results-----------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.2f}")
print(f"{'Highest Grade:':<20}{highest_grade:.2f}")
print(f"{'Sum of Grades:':<20}{total_grades:.2f}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("--------------------------------------------")