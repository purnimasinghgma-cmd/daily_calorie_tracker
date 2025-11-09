# Name - Purnima Singh
# Date - 09.11.2025
# Title - Daily Calorie Tracker

print("--- Welcome to the Daily Calorie Tracker! ---")


limit = int(input("Enter your daily calorie limit: "))

num_meals = int(input("How many meals will you log today? "))


meals = []
total_calories = 0


for i in range(num_meals):
    meal_name = input(f"Enter name for meal #{i + 1}: ")
    calories = int(input(f"Enter calories for {meal_name}: "))

    meals.append((meal_name, calories))
    total_calories += calories


print("\n--- Your Daily Summary ---")
for meal, cal in meals:
    print(f"- {meal}: {cal} calories")

print(f"\nTotal calories consumed: {total_calories}")
print(f"Daily calorie limit: {limit}")


if total_calories > limit:
    print("You have exceeded your daily calorie limit!")
else:
    remaining = limit - total_calories
    print(f"You have {remaining} calories remaining.")
