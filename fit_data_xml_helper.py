# Helper file for storing functions


def clean_gdata_fit_xml(activites_xml):
    """
    Function designed to clean the data from google's xml and pass dictionary back
    """
    cleaned_data = []

    # Check if list
    if isinstance(activites_xml['Activity'], list):
        for item in activites_xml['Activity']:
            cleaned_data.append(data_converter(item))
    else:
        cleaned_data.append(data_converter(activites_xml['Activity']))
    return cleaned_data

def data_converter(data):
    gfit_data = {}
    gfit_data['date'] = data['Id']
    gfit_data['activity'] = data['Notes']
    
    
    try:
        gfit_data['calories'] = data['Lap']['Calories']
    except:
        gfit_data['calories'] = None
    
    try:
        gfit_data['distance'] = data['Lap']['DistanceMeters']
    except:
        gfit_data['distance'] = None
    
    try:
        gfit_data['intensity'] = data['Lap']['Intensity']
    except:
        gfit_data['intensity'] = None
        
    gfit_data['total_time'] = data['Lap']['TotalTimeSeconds']
    return gfit_data
