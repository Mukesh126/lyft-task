from datetime import datetime, timedelta

def add_years_to_date(base_date, years_to_add):
    """
    Add a specified number of years to a given date.

    Args:
        base_date (datetime): The original date.
        years_to_add (int): The number of years to add.

    Returns:
        datetime: The new date after adding the specified years.
    """
    new_date = base_date + timedelta(days=365 * years_to_add)
    return new_date
