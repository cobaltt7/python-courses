food_amount = float(input("Price of item ($): "))
tip_percentage = float(input("Tip percentage (%): ")) / 100
tip_amount = food_amount * tip_percentage
total = food_amount + tip_amount

print("\n\n")
print("---------------------------")
print(f"💵 Price: ${food_amount}")
print(f"💸 Tip: ${tip_amount}")
print("\n")
print(f"💰 Total: ${total}")
print("---------------------------")
