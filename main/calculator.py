import pendulum

# calendar type - quarter
# date - input agreement date
def closest_agreement_end_date(calendar_type, date):

    quarter_end_dates = [
        "03-31",
        "06-30",
        "09-30",
        "12-31"
    ]

    date_types = {
        "quarter": quarter_end_dates
    }

    current_year = date.year

    formatted_dates = [
        pendulum.parse(f"{current_year}-{d}") for d in date_types[calendar_type]
    ] + [
        pendulum.parse(f"{current_year - 1}-{d}") for d in date_types[calendar_type]
    ]

    nearest_end_date = None
    for i in range(len(formatted_dates)):
        this_end = formatted_dates[i]
        last_end = formatted_dates[(i - 1) % len(formatted_dates)]
        if last_end < date <= this_end:
            nearest_end_date = this_end
            break
        elif last_end == date:
            nearest_end_date = last_end
            break

    return nearest_end_date

# end_date - closest quarter-end date
# days - days after end_date
def add_date(end_date, days):
    return end_date.add(days=days)


def generate_date_ranges(calendar_type, start_date, end_date, requirement_days):
    if requirement_days <= 0:
        return [], []

    requirements = []  # list of date ranges

    req_date = closest_agreement_end_date(calendar_type, start_date)

    while req_date < end_date:
        lo = req_date
        hi = add_date(req_date, requirement_days)
        requirements.append((lo, hi))
        req_date = closest_agreement_end_date(calendar_type, add_date(hi, 1))

    if requirements[-1][1] > end_date:
        requirements.pop()

    return requirements[:1], requirements
