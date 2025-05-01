# Chandler Hass
# 13 April 2025
# P4HW1
# Score Processing Program


num_scores = int(input("How many scores do you want to enter? "))
print()


score_list = []


for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                score_list.append(score)
                break  
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                print(f"Enter score #{i + 1} again:")
        except ValueError:
            print("Please enter a valid numeric score.")


lowest_score = min(score_list)
score_list.remove(lowest_score)
average_score = sum(score_list) / len(score_list)


if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"


print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {[round(score, 1) for score in score_list]}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")
