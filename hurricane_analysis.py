# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def damages_conversion(list):
  updated_damages_list = []
  for element in list:
    if element == "Damages not recorded":
      updated_damages_list.append("Damages not recorded")
    elif "M" in element:
      replace1 = float(element.replace("M", ""))*conversion.get("M")
      updated_damages_list.append(replace1)
    elif "B" in element:
      replace2 = float(element.replace("B", "000000000"))*conversion.get("B")
      updated_damages_list.append(replace2)
  return updated_damages_list  

print(damages_conversion(damages))

# 2 
# Create a Table
all_data = list(zip(names, months, years, max_sustained_winds, areas_affected, deaths))
print("--------ALL DATA--------: " + str(all_data))


# Create and view the hurricanes dictionary
def create_dict_from_list_name(data):
  # main dictionary: Key = Names
  dict1 = {}
  # secundary dictionary: Key = keys_dict2
  keys_dict2 = ["Name" , "Month", "Year", "Max Sustained Wind", "Areas Affected, Damage", "Death"]
  for element in data:
    dict2 = {}
    for i in range(len(element)):
      dict2.update({keys_dict2[i]: element[i]})
    dict1.update({element[0]:dict2})
  return dict1

print("---- DICTIONARY----: " + str(create_dict_from_list_name(all_data)))

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def create_dict_from_list_year(data):
  # main dictionary: Key = Names
  dict1 = {}
  # secundary dictionary: Key = keys_dict2
  keys_dict2 = ["Name" , "Month", "Year", "Max Sustained Wind", "Areas Affected, Damage", "Death"]
  for element in data:
    dict2 = {}
    for i in range(len(element)):
      dict2.update({keys_dict2[i]: element[i]})
    dict1.update({element[2]:dict2})
  return dict1
print("---- DICTIONARY----: " + str(create_dict_from_list_year(all_data)))


# 4
# Counting Damaged Areas
areas_affected_simple = []
for element in areas_affected:
  areas_affected_simple = areas_affected_simple + element
print("----AFFECTED AREAS----" + str(areas_affected_simple))

# create dictionary of areas to store the number of hurricanes involved in
def counts_affected_areas(data):
  affected_areas = {}
  for element in data:
    if element not in affected_areas:
      affected_areas.update({element: data.count(element)})
  return affected_areas

print("COUNTS AFFECTED AREAS" + str(counts_affected_areas(areas_affected_simple)))



# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def area_most_affected(data_dict):
  save_most_affected_areas = {}
  for key,value in data_dict.items():
    if value == max(data_dict.values()):
    # save_most_affected_areas.update({key: value})
      save_most_affected_areas[key] = value
  return save_most_affected_areas

print("MOST AFFECTED AREA: " + str(area_most_affected(counts_affected_areas(areas_affected_simple))))

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
# creates a dictionary with the name of the hurricane as key and the number of deaths as value 
hurricane_deaths = {key:value for key,value in zip(names, deaths)}
print("--------Hurricane_Deaths--------: " + str(hurricane_deaths))

def deadliest_huricane(data_dict):
  save_deadliest_huricanes = {}
  for key, value in data_dict.items():
    if value == max(data_dict.values()):
      save_deadliest_huricanes[key]=value
  return save_deadliest_huricanes

print("DEADLIEST HURRICANE: " + str(deadliest_huricane(hurricane_deaths)))



# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key

all_data_dict = create_dict_from_list_name(all_data)
#print("ALL DATA DICT " + str(all_data_dict))

def categorize_by_mortality_severity(data):
  # main dictionary: Key = mortality_scale
  dict_rating = {1:[], 2:[], 3:[], 4:[], 5:[]}
  for key, value in data.items():
    if value > 0 and value <= 100:
       dict_rating[1].append(all_data_dict[key])
    elif value > 100 and value <= 500:
      dict_rating[2].append(all_data_dict[key])
    elif value > 500 and value <= 1000:
      dict_rating[3].append(all_data_dict[key])
    elif value > 1000 and value <= 10000:
      dict_rating[4].append(all_data_dict[key])
    elif value > 10000:
      dict_rating[5].append(all_data_dict[key])
  return dict_rating

print("---- MORTALITY_SEVERITY----: " + str(categorize_by_mortality_severity(hurricane_deaths)))

mortality_severity = categorize_by_mortality_severity(hurricane_deaths)
print("-----MORTALITY -----" + str(mortality_severity.get(2)[0].get("Death")))


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
converted_damage = damages_conversion(damages)
print("CONVERTED DAMAGE: " + str(converted_damage))

hurricane_damage = {key: value for key,value in zip(names,converted_damage)} 
print("HURRICANE DAMAGE: " + str(hurricane_damage))

def most_damaging_hurricane(data_dict):
  max_value = -1
  key_max_value = ""
  for key, value in data_dict.items():
    if type(value) != str and max_value < value:
      max_value = value
      key_max_value = key
  return {key_max_value: max_value}
       
print("--- MOST DAMAGING HURRICANE---: " + str(most_damaging_hurricane(hurricane_damage)))



# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}



# categorize hurricanes in new dictionary with damage severity as key
def categorize_by_damage_scale(data):
  dict_rating = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for key, value in data.items():
    if type(value) == str:
      dict_rating[0].append(all_data_dict[key])
    elif value > 0 and value <= 100000000:
       dict_rating[1].append(all_data_dict[key])
    elif value > 100000000 and value <= 1000000000:
       dict_rating[2].append(all_data_dict[key])
    elif value > 1000000000 and value <= 10000000000:
      dict_rating[3].append(all_data_dict[key])
    elif value > 10000000000 and value <= 50000000000:
      dict_rating[4].append(all_data_dict[key])
    elif value > 50000000000:
      dict_rating[5].append(all_data_dict[key])
  return dict_rating

print("---- DAMAGE_SCALE----: " + str(categorize_by_damage_scale(hurricane_damage)))

damage = categorize_by_damage_scale(hurricane_damage)

print("-----DAMAGE -----" + str(damage.get(1)[0]))#.get("Damage")))