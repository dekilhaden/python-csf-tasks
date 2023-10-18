day = input("Enter the day: ")
if day in {"Monday", "Tuesday", "Wednesday", "Thursday"}:
    print("Weekday")
elif day == "Friday":
    print("TGIF")
elif day in {"Saturday", "Sunday"}:
    print("Weekend")
else:
    print("Invalid input")