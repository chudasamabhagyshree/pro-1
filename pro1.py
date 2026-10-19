
print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Favourite Number: {number} (Type: {type(number)})")

birth_year = 2026- age
print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

print("\nThank you for using the Personal Data Collector. Goodbye!")