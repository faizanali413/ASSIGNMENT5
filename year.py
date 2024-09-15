month = int(input("Enter the month number (1-12): "))

if month == 1:   # January
    days = 31
elif month == 2: # February
    days = 28
elif month == 3: # March
    days = 31
elif month == 4: # April
    days = 30
elif month == 5: # May
    days = 31
elif month == 6: # June
    days = 30
elif month == 7: # July
    days = 31
elif month == 8: # August
    days = 31
elif month == 9: # September
    days = 30
elif month == 10: # October
    days = 31
elif month == 11: # November
    days = 30
elif month == 12: # December
    days = 31
else:
    days = "Invalid month number"  

print(f"Number of days in month {month}: {days}")
