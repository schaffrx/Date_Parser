from datetime import datetime
#Holds string content of file
content = ""

#Build list of month acronyms:
month_acronyms: list = ["Jan","Feb","Mar","Apr","May",
"Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

#Conversion map for month string to int
month_int_map: dict = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

#open file and read individual strings for acronym inclusion
with open('missoula.txt', 'r') as file:
    content = file.read()

def get_months(target_list: list, content: str) -> list:
    """Gets the pertinent months out of the text

    Parameters
    ----------
    target_list : list
        The acronyms to compare the text to
    content: string
        The yet to be parsed string containing the original file text

    Returns
    -------
    list
        a list of all strings that contained the month acronyms as a substring
    """
    dates: list = []
    for word in content.split():
        for item in target_list:
            if item in word:
                dates.append(word)
    return(dates)

#narrow our list down to only formatted dates
def get_day_month(month_list: list) -> list:
    """Parses the provided list to include only day_month strings

    Parameters
    ----------
    month_list : list
        A list of all months returned by the get_months function

    Returns
    -------
    list
        a list of all properly formatted day_month strings
    """
    day_month: list = []
    day_list: list = str(list(range(1, 32)))
    for month in month_list:
        for day in day_list:
            if day in month:
                day_month.append(month)
    return(day_month)

#append and increment when applicable the year to the date
def set_years(day_month: list, year_index: int) -> list:
    """ Concatenate and increment the year to the day_month string

    Parameters
    ----------
    day_month : list
        The list generated by the get_day_month function
    year_index : int
        The starting year for the dates

    Returns
    -------
    list
        a list of all properly formatted year_day_month strings
    """
    year = year_index
    year_day_month: list = []
    incremented_year: bool = False
    for month in day_month:
        if "Jan" in month and not incremented_year:
            incremented_year = True
            year += 1
            year_day_month.append(str(year) + "-" + month)
        else:
            #incremented_year = False
            year_day_month.append(str(year) + "-" + month)
    return(year_day_month)

def set_date_object(ydm: list, in_fmt: str ="%Y-%d-%b" , out_fmt: str = "%Y-%m-%d"):
    date_objects: list = []
    date_output: list = []
    for date in ydm:
        date_objects.append(datetime.strptime(date, in_fmt))
    for date_object in date_objects:
        date_output.append(datetime.strftime(date_object, out_fmt))
    return(date_output)


months: list = get_months(month_acronyms, content)
day_months: list = get_day_month(months)
year_day_months: list = set_years(day_months, 2015)
final_list = set_date_object(year_day_months)
print(final_list)
