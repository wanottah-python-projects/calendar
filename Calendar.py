# 10 CLS

# Dictionary of months
months = {'January': 1,
          'February': 2,
          'March': 3,
          'April': 4,
          'May': 5,
          'June': 6,
          'July': 7,
          'August': 8,
          'September': 9,
          'October': 10,
          'November': 11,
          'December': 12
          }


# 1000
def calculate_leap_year(new_month, new_year):

    new_mm = new_month - 2

    new_yy = new_year

    if new_mm <= 0:
        new_mm = new_mm + 12

        new_yy = new_yy - 1

    # century = INT(year / 100)
    century = new_year // 100

    new_yy = new_yy - 100 * century

    # dd = 1 + INT(2.6 * mm - .19) + yy + INT(yy / 4) + INT(century / 4) - 2 * century
    new_dd = 1 + int(2.6 * new_mm - .19) + new_yy + (new_yy // 4) + (century // 4) - 2 * century

    # dd = dd MOD 7
    new_dd = new_dd % 7

    return new_dd, new_mm, new_yy


# Get date
date = input("Enter month  mm/yyyy: ")

# month = VAL(LEFT$(d$, 2))
month = int(date[:2])

# year = VAL(RIGHT$(d$, 4))
year = int(date[3:])

# GOSUB 1000
dd, mm, yy = calculate_leap_year(month, year)

day = dd

month = month + 1

if month > 12:
    month = 1

    year = year + 1

# GOSUB 1000
dd, mm, yy = calculate_leap_year(month, year)

if dd < day:
    dd = dd + 7

# Display calendar
numberOfDaysInMonth = 28 + dd - day

# Position to display first day of month
p = 4 * (day - 1) + 1

# Date positions
p1 = day - 1

print()

for i in months:

    if months[i] == month - 1:
        print(' ' + i + ' ' + str(year))

print()

print('{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}'.format('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'))

print((p - 1) * ' '.format(''), end='')

for dates in range(1, numberOfDaysInMonth + 1):

    if p1 % 7 == 0:
        print()

    print('{:>3}'.format(dates), end=' ')

    p1 = p1 + 1

    if p1 > 7:
        p1 = 1
