year = eval(input("Enter year: "))

leap_year = False

if year < 1582:
    print(str(year) + " is before the adoption of the Gregorian calendar.")
else:
    if year % 4 == 0:
        if year % 400 == 0:
            if year > 2022:
                print(f"{year} will be a leap year.")
            else:
                print(f"{year} is a leap year.")
        elif year % 100 == 0:
            print(f"{year} is NOT a leap year.")
        else:
            if year > 2022:
                print(f"{year} will be a leap year.")
            else:
                print(f"{year} is a leap year.")
    else:
        print(f"{year} is NOT a leap year.")


"""
if year < 1582:
    print(f"{year} is before the adoption of the Gregorian calendar.")

else:
    if year == leap_year and year < 2022:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is NOT a leap year.")
    elif year == leap_year and year >= 2022:
        print(f"{year} will be a leap year.")
        """