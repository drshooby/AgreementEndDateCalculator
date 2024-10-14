from datetime import datetime, timedelta

# calendar type - quarter
# date - input agreement date
def closest_agreement_end_date(calendar_type, date):

    quarter_end_dates = [
        "March 31",
        "June 30",
        "September 30",
        "December 31"
    ]

    date_types = {
        "quarter": quarter_end_dates
    }

    current_year = date.year

    formatted_dates = [
        datetime.strptime(f"{date} {current_year}", "%B %d %Y") for date in date_types[calendar_type]
    ] + [
        datetime.strptime(f"{date} {current_year - 1}", "%B %d %Y") for date in date_types[calendar_type]
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
def add_date(end_date, requirement_days):
    return end_date + timedelta(days=requirement_days)


def generate_date_ranges(calendar_type, start_date, days_until_end, requirement_days):

    if requirement_days <= 0:
        return None, None

    end_date = add_date(start_date, days_until_end)

    requirements = [] # list of date ranges

    req_date = closest_agreement_end_date(calendar_type, start_date)

    while req_date < end_date:
        lo = req_date
        hi = add_date(req_date, requirement_days)
        requirements.append((lo, hi))
        req_date = closest_agreement_end_date(calendar_type, add_date(hi, 1))

    if requirements[-1][1] > end_date:
        requirements.pop()

    return requirements[:1], requirements


if __name__ == "__main__":
    date_format = "%Y-%m-%d"  # Define the format (YYYY-MM-DD)
    date1 = datetime.strptime("2024-06-15", date_format)

    single_range, all_ranges = generate_date_ranges("quarter", date1, 365, 20)

    print(single_range)

    for date in all_ranges:
        print(date)
    



