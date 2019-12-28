cal_month_range = [(1, 'January', range(1, 31 + 1)),
            (2, 'February', range(1, 28 + 1)),
            (3, 'March', range(1, 31 + 1)),
            (4, 'April', range(1, 30 + 1)),
            (5, 'May', range(1, 31 + 1)),
            (6, 'June', range(1, 30 + 1)),
            (7, 'July', range(1, 31 + 1)),
            (8, 'August', range(1, 31 + 1)),
            (9, 'September', range(1, 30 + 1)),
            (10, 'October', range(1, 31 + 1)),
            (11, 'November', range(1, 30 + 1)),
            (12, 'December', range(1, 31 + 1))]

week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


# Get the number of days for a month specified
def num_days(month):
    month_range = cal_month_range[month - 1]
    return month_range[2]


# check if an year is leap year
def is_leap(year):
    return year % 4 and (year % 100 != 0 or year % 400 == 0)


# Get the first day of the provided month and year
# Here we will have to use the Zeller's congruence as formula to find startday of month
def start_day(month, year):
    day_name = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

    if month < 3:
        month += 12
        year -= 1

    day = 1
    first_day_of_month = ((13 * month + 3) // 5 + day + year + (year/4) - (year // 100) + (year // 400)) % 7
    
    return day_name[int(first_day_of_month)]


def cal(mon, year):
    # Determine the starting position of week in month
    start_pos = week.index(start_day(mon, year))

    if is_leap(year):
        cal_month_range[1] = (2, 'February', range(1, 29 + 1))

    print()
    for mon_val, month, days in cal_month_range:
        if mon_val == mon:
            # Print month name
            print('{0} {1}'.format(month, year).center(20, ' '))
            # Print days name
            print(''.join(['{0:<3}'.format(w) for w in week]))
            # Add spacing for non-zero starting position
            print('{0:<3}'.format('') * start_pos, end='')

            days_in_month = num_days(mon)

            for day in days_in_month:
                # Print day
                print('{0:<3}'.format(day), end='')
                start_pos += 1
                # If the start position is Saturday i.e 7 we need to create a new line and reset the counter
                if start_pos == 7:
                    print()
                    start_pos = 0
    print()



