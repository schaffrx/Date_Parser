from date_parser import *
from story_parser import *

target_file = 'missoula.txt'
header_title = 'Missoulian'

#Instantiating a new Date_Parser object to format dates
parser: object = Date_Parser(target_file)
months: list = parser.get_months()
day_months: list = parser.get_day_month(months)
year_day_months: list = parser.set_years(day_months, 2015)
date_list = parser.set_date_object(year_day_months)

#Instantiating a new Story_Parser object to format stories
story_obj: object = Story_Parser(target_file)
prepped_story: list = story_obj.get_stories()
curated_stories: list = story_obj.remove_targets(day_months, prepped_story)

#Combining the currated date and story list
zipped_list: object = zip(date_list, curated_stories)
iterable_list = (list(zipped_list))

#Printing the results to the console
print("paper    date    headline")
for i in iterable_list:
    print(header_title + "    " + i[0] + "    " + i[1])