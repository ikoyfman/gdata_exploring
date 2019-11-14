from pathlib import Path
import xmltodict
from pprint import pprint
import data_helper

# Path of where tcx files are
DATA_LOCATION = Path('/home/ikadmin/Downloads/takeout-20191113T152724Z-001(1)/Takeout/Fit/Activities')

# Grab all files make into list
list_of_files = [file for file in DATA_LOCATION.glob('*.tcx')]

# Set list to capture data
cleaned_data_results = []

# Go through each file and append to results
for file in list_of_files:
    with open(file) as open_file:
        read_file = xmltodict.parse(open_file.read())
        activities = read_file['TrainingCenterDatabase']['Activities']
        cleaned_data_results.append(data_helper.clean_gdata_fit_xml(activities))

# check data

pprint(cleaned_data_results)