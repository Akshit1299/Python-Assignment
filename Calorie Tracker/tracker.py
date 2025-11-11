# ------------------------------------------------------------
# Project Title : Daily Calorie Tracker CLI
# Name          : Akshit Rajput
# Course        : Programming for Problem Solving using Python
# Date          : 09 Nov 2025
# ------------------------------------------------------------
# Description:
# This Python CLI app helps users track their daily calorie intake.
# The user can enter multiple meals and their calorie values,
# view a formatted summary, compare against their daily calorie limit,
# and optionally save the session to a text file.
# ------------------------------------------------------------

import datetime

print("------------------------------------------------------------")
print("           Welcome to Daily Calorie Tracker CLI          ")
print("------------------------------------------------------------")
print("This tool helps you log your meals and calories,\ncalculate total & average intake, and compare it with your daily limit.\n")

meals = []
calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter name of meal {i+1}: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_amount)

total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_calories > daily_limit:
    status = " You have exceeded your daily limit!"
else:
    status = " You are within your daily limit!"

print("\n---------- DAILY CALORIE SUMMARY ----------")
print(f"{'Meal Name':<20}{'Calories':>10}")
print("-" * 35)
for i in range(len(meals)):
    print(f"{meals[i]:<20}{calories[i]:>10.2f}")
print("-" * 35)
print(f"{'Total:':<20}{total_calories:>10.2f}")
print(f"{'Average:':<20}{average_calories:>10.2f}")
print("-" * 35)
print(status)
print("--------------------------------------------")

#  Task 6 (Simplified): Save Session Log
save = input("\nDo you want to save this report? (yes/no): ")

if save.lower() == "yes":
    file = open("calorie_log.txt", "w")   # simple open/write method
    file.write("Daily Calorie Tracker Report\n")
    file.write("--------------------------------------------\n")
    file.write(f"{'Meal Name':<15}{'Calories':>10}\n")
    for i in range(len(meals)):
        file.write(f"{meals[i]:<15}{calories[i]:>10.2f}\n")

    file.write("--------------------------------------------\n")
    file.write(f"Total: {total_calories}\n")
    file.write(f"Average: {average_calories}\n")
    file.write(status + "\n")
    file.write("Saved on: " + str(datetime.datetime.now()) + "\n")
    file.close()
    print("\n Report saved to calorie_log.txt")
else:
    print("\nReport not saved. Goodbye!")

print("\nHave a nice day! ")
