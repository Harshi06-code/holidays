from datetime import date

def get_holidays_in_range(holidays_obj, start_date, end_date, keyword=None):
    """
    Returns holidays between start_date and end_date.
    Optionally filters results by keyword.
    """

    result = {}

    for day, name in holidays_obj.items():
        if start_date <= day <= end_date:
            if keyword:
                if keyword.lower() in name.lower():
                    result[day] = name
            else:
                result[day] = name

    return result
