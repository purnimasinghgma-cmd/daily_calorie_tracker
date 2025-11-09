# Name - Purnima Singh
# Date - 28.10.2025
# Task : Print a welcome message
print("--- Welcome to the Daily Calorie Tracker! ---")



limit = int(input("Enter your daily calorie limit: "))
num_meals = int(input("How many meals will you log today? "))



meals = []
total_calories = 0



for i in range(num_meals):
    meal_name = input(f"Enter name for meal #{i + 1}: ")
    try:
        calories = int(input(f"Enter calories for {meal_name}: "))
        meals.append((meal_name, calories))
        total_calories += calories
    except ValueError:
        print("Invalid input. Please enter a number for calories.")



print("\n--- Your Daily Summary ---")

print(f"{'Meal Name':<20} {'Calories'}")
print("-" * 30)


for meal, cal in meals:
    print(f"{meal:<20} {cal}")


if num_meals > 0:
    average_calories = total_calories / num_meals
else:
    average_calories = 0


print(f"{'Total':<20} {total_calories}")

print(f"{'Avareage':<20} {average_calories:.2f}")

if total_calories > limit:
    print("You have exceeded your daily calorie limit!")
else:
    remaining = limit - total_calories
    print(f"You have {remaining} calories remaining.")
