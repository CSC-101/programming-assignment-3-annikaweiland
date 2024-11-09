import data
import build_data
import county_demographics
import hw3_tests

#Purpose: To find the total 2014 population given an input of list of CountryDemographics class.
#inputs: a list of Country Demographics
#outputs: An integer, which is the total population of the inputted CountryDemographics.
#part1
def population_total(input: list[data.CountyDemographics]) -> int:
    population = 0
    for county in input:
        population = population + county.population['2014 Population']
    return population

#Purpose: Filtering a list of inputted CountyDemographics and outputting the ones that contain the inputted state string.
#inputs: A list of CountryDemographics, as well as a string input that represents a state.
#outputs: Either a list of type CountryDemographics inside, or a str that says 'enter a valud state' if the str input is invalid.
#part2
def filter_by_state(counties: list[data.CountyDemographics], input: str) -> list[data.CountyDemographics]:
    in_state = []
    for county in counties:
        if county.state == input:
            in_state.append(county)
    if in_state != []:
        return in_state
    else:
        return 'enter a valid state.'

#Purpose: To determine the population of the inputted countydemographics by the education type.
#inputs: A list of counties (list of type CountyDemographics), as well as a string.
#outputs: Either an integer (the population by education), or if the inputted string is invalid, the string "enter a valid education parameter" is outputted.
#part3
def population_by_education(counties: list[data.CountyDemographics], education: str) -> int:
    #str HAS to be either 'Bachelor's Degree or higher' or 'High School or Higher'
    sub_population = 0
    try:
        for county in counties:
            sub_population = sub_population + county.population['2014 Population']*(county.education[education]/100)
        return sub_population
    except:
        return "enter a valid education parameter."

#Purpose: Determining the population of an inputted list of counties by ethnicity.
#inputs: A list of counties (list of type CountyDemographics), as well as a string.
#outputs: Either an integer, that is the population by ethnicity, or if the ethnicity str is invalid, the str "enter a valid ethnicity parameter." is outputted.
def population_by_ethnicity(counties: list[data.CountyDemographics], ethnicity: str) -> int:
    #ethnicity HAS to be any of the keys - HOW TO MAKE IT JUST RETURN ZERO
    sub_population = 0
    try:
        for county in counties:
            sub_population = sub_population + county.population['2014 Population']*(county.ethnicities[ethnicity]/100)
        return sub_population
    except:
        return "enter a valid ethnicity parameter."

#Purpose:  Determining the population of an inputted list of counties that are below poverty.
#inputs: A list of counties (list of type CountyDemographics)
#outputs: An integer that is the population below poverty for the given list of CountyDemographics.
def population_below_poverty_level(counties: list[data.CountyDemographics]) -> int:
    ppl_below = 0
    for county in counties:
        ppl_below = ppl_below + county.population['2014 Population']*(county.income['Persons Below Poverty Level']/100)
    return ppl_below

#part4

#Purpose: Determining the percent by education (given an education parameter) of a list of counties of type CountyDemographics.
#inputs: A list of counties (list of type CountyDemographics) and a key that is a str (has to be a valid education parameter)
#outputs: A float value that is the percent by education for the given list of CountyDemographics.
def percent_by_education(counties: list[data.CountyDemographics], key:str) -> float:
    try:
        population = population_total(counties)
        edulvl = population_by_education(counties, key)
        percentage = (edulvl/population)*100
        return percentage
    except:
        return "enter a valid education parameter"

#Purpose: Determining the percent by ethnicity (given an ethnicity parameter) of a list of counties of type CountyDemographics.
#inputs: A list of counties (list of type CountyDemographics) and a key that is a str (has to be a valid ethnicity parameter).
#outputs: A float value that is the percent by ethnicity for the given list of CountyDemographics.
def percent_by_ethnicity(counties: list[data.CountyDemographics], key:str) -> float:
    try:
        population = population_total(counties)
        ethlvl = population_by_ethnicity(counties, key)
        percentage = (ethlvl/population)*100
        return percentage
    except:
        return "enter a valid ethnicity parameter"

#Purpose: Determining the percent by ethnicity (given an ethnicity parameter) of a list of counties of type CountyDemographics.
#inputs: A list of counties (list of type CountyDemographics)
#outputs: A float value that is the percent below poverty level for the given list of CountyDemographics.
def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    population = population_total(counties)
    povlvl = population_below_poverty_level(counties)
    percentage = (povlvl/population)*100
    return percentage

#part5

#Purpose: Determining the counties that have a greater population of an education parameter than a given threshold value.
#inputs: A list of counties (list of type CountyDemographics), an education key, and a threshold value.
#outputs: A list of counties that education percentage is greater than the threshold value.
def education_greater_than(counties: list[data.CountyDemographics], key: str, value: float) -> list[data.CountyDemographics]:
    greater_than = []
    for county in counties:
        if county.education[key] > value:
            greater_than.append(county)
    return greater_than

#Purpose: Determining the counties that have a smaller population of an education parameter than a given threshold value.
#inputs: A list of counties (list of type CountyDemographics), an education key, and a threshold value.
#outputs: A list of counties that education percentage is less than the threshold value.
def education_less_than(counties: list[data.CountyDemographics], key: str, value: float) -> list[data.CountyDemographics]:
    less_than = []
    for county in counties:
        if county.education[key] < value:
            less_than.append(county)
    return less_than

#Purpose: Determining the counties that have a greater population of an ethnicity parameter than a given threshold value.
#inputs: A list of counties (list of type CountyDemographics), an ethnicity key, and a threshold value.
#outputs: A list of counties that ethnicity percentage is greater than the threshold value.
def ethnicity_greater_than(counties: list[data.CountyDemographics], key: str, value: float) -> list[data.CountyDemographics]:
    greater_than = []
    for county in counties:
        if county.ethnicities[key] > value:
            greater_than.append(county)
    return greater_than

#Purpose: Determining the counties that have a smaller population of an ethnicity parameter than a given threshold value.
#inputs: A list of counties (list of type CountyDemographics), an ethnicity key, and a threshold value.
#outputs: A list of counties that ethnicity percentage is less than the threshold value.
def ethnicity_less_than(counties: list[data.CountyDemographics], key: str, value: float) -> list[data.CountyDemographics]:
    less_than = []
    for county in counties:
        if county.ethnicities[key] < value:
            less_than.append(county)
    return less_than

#Purpose: Determining the counties that have a greater population of "below poverty level" than a given threshold value.
#inputs: A list of counties (list of type CountyDemographics) and a threshold value.
#outputs: A list of counties that below poverty level percentage is greater than the threshold value.
def below_poverty_level_greater_than(counties: list[data.CountyDemographics], value: float) -> list[data.CountyDemographics]:
    greater_than = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > value:
            greater_than.append(county)
    return greater_than


#Purpose: Determining the counties that have a smaller population of "below poverty level" than a given threshold value.
#inputs: A list of counties (list of type CountyDemographics) and a threshold value.
#outputs: A list of counties that below poverty level percentage is lower than the threshold value.
def below_poverty_level_less_than(counties: list[data.CountyDemographics], value: float) -> list[data.CountyDemographics]:
    less_than = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < value:
            less_than.append(county)
    return less_than

