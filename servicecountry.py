#project: ServiceCounter.py
# author: Evan Gonzalez <egonzalez2705002@Woonsocketschools.com>
#date written: 03/12/2025
#
# description: Creating an app that will collect information through a service inbox.

print("Hi, Welcome to the Automotive Shop of the WACTC.")

name = input("What is your name? ")
print(f"Hello, {name}!")

carMake = input("What is the make and model of your vehicle? ")
print(f"{carMake}, Nice Car!")
print()

carMileage = input("How many miles are on your vehicle? ")
print(f"{carMileage}, Okay Okay!")
print()

print('''Here at the Automotive Shop of the WACTC, we offer many services such as
      Oil changes and tire Rotation, Brake pads and Front End alignment,
      Broken Glass Repair, and lastly Dent Removal.''')
print()

print('''At The WACTC Garage we offer the following services:
1. Oil and Filter change - $79.99
2. Tire Rotation - $30.00 for standard tires, $45.00 for 4WD or Truck tires
3. Brake pads and front alignment - $120.00 for the package
4. Broken glass Repair - $69.99 for large window, $39.99 for small window
5. Dent Removal - $5.00 per small dent, $15.00 per large dent
''')

# Service selection and total calculation
total = 0

while True:
    print("Please choose a service by entering the corresponding number (or type 'done' to finish):")
    print("1. Oil and Filter change")
    print("2. Tire Rotation")
    print("3. Brake pads and front alignment")
    print("4. Broken glass Repair")
    print("5. Dent Removal")
    print("Type 'done' to finish.")
    choice = input("Your choice: ").strip().lower()

    if choice == 'done':
        break

    if choice == '1':
        total += 79.99
        print("Oil and Filter change added. $79.99")
    elif choice == '2':
        tire_type = input("Is it standard tires or 4WD/Truck tires? (type 'standard' or '4WD'): ").strip().lower()
        if tire_type == 'standard':
            total += 30.00
            print("Tire Rotation for standard tires added. $30.00")
        elif tire_type == '4wd':
            total += 45.00
            print("Tire Rotation for 4WD/Truck tires added. $45.00")
        else:
            print("Invalid tire type.")
    elif choice == '3':
        total += 120.00
        print("Brake pads and front alignment added. $120.00")
    elif choice == '4':
        glass_type = input("Is it a large window or a small window? (type 'large' or 'small'): ").strip().lower()
        if glass_type == 'large':
            total += 69.99
            print("Broken glass repair for large window added. $69.99")
        elif glass_type == 'small':
            total += 39.99
            print("Broken glass repair for small window added. $39.99")
        else:
            print("Invalid window type.")
    elif choice == '5':
        dent_size = input("Is it a small dent or a large dent? (type 'small' or 'large'): ").strip().lower()
        if dent_size == 'small':
            total += 5.00
            print("Small dent removal added. $5.00")
        elif dent_size == 'large':
            total += 15.00
            print("Large dent removal added. $15.00")
        else:
            print("Invalid dent size.")
    else:
        print("Invalid choice.")

    print(f"Current total: ${total:.2f}")
    print()

print(f"Thank you for visiting the Automotive Shop of the WACTC, {name}! Your total is: ${total:.2f}")