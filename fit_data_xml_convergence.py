#%%
from pathlib import Path
import xmltodict
from pprint import pprint
import fit_data_xml_helper

#%%
# Path of where tcx files are
DATA_LOCATION = Path('gdata/Fit/Activities')

# Grab all files make into list
list_of_files = [file for file in DATA_LOCATION.glob('*.tcx')]

# Set list to capture data
cleaned_data_results = []

# Go through each file and append to results
for file in list_of_files:
    with open(file) as open_file:
        read_file = xmltodict.parse(open_file.read())
        activities = read_file['TrainingCenterDatabase']['Activities']
        cleaned_data_results.append(fit_data_xml_helper.clean_gdata_fit_xml(activities))

#%%

# Convert data to CSV
import csv
csv_location = Path("converted_data/fit_data_xml.csv")

#%%

with open(csv_location,'w',newline='') as csv_file:
    field_names = ['date', 'activity', 'calories', 'distance', 'intensity', 'total_time']
    file_writer = csv.DictWriter(csv_file, fieldnames=field_names)
    file_writer.writeheader()
    
    for results in cleaned_data_results:
        for item in results:
            file_writer.writerow(item)

# %%
