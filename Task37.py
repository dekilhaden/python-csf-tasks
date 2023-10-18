month = input("Enter a month: ")

if month in {"January", "Febraury", "March", "April", "May"}:
    print("Spring")
elif month in {"June", "July", "August"}:
    print("Summer")
elif month in {"September", "October", "Nivember"}:
    print("Fall")
elif month in {"December"}:
    print("Winter")
else:
    print("Invalid month")
    