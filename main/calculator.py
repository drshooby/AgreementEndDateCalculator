from datetime import datetime

# calendar type - quarter
# date - input agreement date
def closest_agreement_date(calendar_type, date):

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

    return nearest_end_date.strftime("%Y-%m-%d")

# end_date - closest quarter-end date
# days - days after end_date
def calculate_next_date(end_date, days):
    pass

if __name__ == "__main__":
    date_format = "%Y-%m-%d"  # Define the format (YYYY-MM-DD)
    date1 = datetime.strptime("2024-10-14", date_format)
    print("End quarter date based on agreement date:", closest_agreement_date("quarter", date1))

    date2 = datetime.strptime("2024-12-31", date_format)
    print("End quarter date based on agreement date:", closest_agreement_date("quarter", date2))

    date3 = datetime.strptime("2025-02-20", date_format)
    print("End quarter date based on agreement date:", closest_agreement_date("quarter", date3))

