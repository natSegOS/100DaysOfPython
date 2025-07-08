def weeks_left(day, month, year, birth_day, birth_month, birth_year):
    birth_date = birth_year * 365.242199 + (birth_month - 1) * 30 + birth_day
    current_date = year * 365.242199 + (month - 1) * 30 + day

    difference = current_date - birth_date
    weeks = round(difference / 7)

    print(weeks)


weeks_left(8, 7, 2025, 20, 12, 2006)
