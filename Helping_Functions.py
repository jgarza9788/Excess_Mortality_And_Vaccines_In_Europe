# This section defines utility functions that streamline repetitive tasks and improve code readability. 
# These functions will be used throughout the notebook to simplify operations, enhance modularity, and reduce redundancy.

##################################################

def df_column_uniquify(df):
    '''
    renames columns that are the same
    '''
    df_columns = df.columns
    new_columns = []
    for item in df_columns:
        counter = 0
        newitem = item
        while newitem in new_columns:
            counter += 1
            newitem = "{}_{}".format(item, counter)
        new_columns.append(newitem)
    df.columns = new_columns
    return df

##################################################

import pycountry
def abbr_to_isoalpha3(abbr):
    """
    Convert a European country ISO Alpha-2 code to ISO Alpha-3 code.

    Parameters:
        abbreviation (str): ISO Alpha-2 country code (e.g., 'DE' for Germany).

    Returns:
        str: ISO Alpha-3 country code (e.g., 'DEU'), or None if not found.
    """
    try:
        country = pycountry.countries.get(alpha_2=abbr.upper())
        if country:
            return country.alpha_3
        else:
            return None
    except KeyError:
        return None
    
##################################################

# this if for converting between the abbreviation andand the names of the countries

country_dict = {
    "AD": "Andorra",
    "AL": "Albania",
    "AM": "Armenia",
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CH": "Switzerland",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "EL": "Greece",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "GE": "Georgia",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IS": "Iceland",
    "IT": "Italy",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "ME": "Montenegro",
    "MT": "Malta",
    "NL": "Netherlands",
    "NO": "Norway",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "RS": "Serbia",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
    "UK": "United Kingdom"
}

def abbr_to_name(abbreviation):
    return country_dict.get(abbreviation.upper(), "Abbreviation not found")

def name_to_abbr(name):
    reverse_dict = {v: k for k, v in country_dict.items()}
    return reverse_dict.get(name, "Unknown")

if __name__ == '__main__':
    # testing
    print( abbr_to_name("BE") )  # Output: 'Belgium'
    print( name_to_abbr("Belgium") )  # Output: 'BE'

##################################################

def bar(num,denom=100.0,length=25,fillchar='#',emptychar='_'):
    fillnum = ((int)( (num/denom) * length))
    return '[' + ( fillnum * fillchar ).ljust(length,emptychar)  + ']' # + f" {(num/denom)*100.0:.2f}%     " 

if __name__ == '__main__':
    print(bar(5,50))
    print(bar(25,50))
    print(bar(40,50))
    print(bar(50,50))

    # ▼
def spearmansrank_bar(spearmansrank, length=120, markchar='*', emptychar='_'):
    position = int((spearmansrank + 1) / 2 * length)
    numbar = ' ' * position + f"{spearmansrank:.3f}"
    bar = emptychar * position + markchar + emptychar * (length - position - 1 ) 
    qlength = int(length * 0.25)
    elength = int(length * 0.125)
    scale = "-1".ljust(qlength) + "-0.5".ljust(qlength) + "0".ljust(qlength) + "0.5".ljust(qlength) + "1"
    # scale2 = " ".ljust(elength) + "-0.75".ljust(qlength) + "-0.25".ljust(qlength) + "0.25".ljust(qlength) + "0.75".ljust(qlength) 

    return f"\n\nSpearman's Rank: {spearmansrank:.3f}\n{numbar}\n{bar}\n{scale}\n"


if __name__ == '__main__':
    print(spearmansrank_bar(-1.0,120))
    print(spearmansrank_bar(-0.5))
    print(spearmansrank_bar(0.0))
    print(spearmansrank_bar(0.5))
    print(spearmansrank_bar(0.75))
    print(spearmansrank_bar(1.0))

