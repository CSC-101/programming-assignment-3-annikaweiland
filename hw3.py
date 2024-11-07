import data
import build_data
import county_demographics
import hw3_tests


reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

#part1
def population_total(input: list[data.CountyDemographics]) -> int:
    population = 0
    for county in input:
        population = population + county.population['2014 Population']
    return population

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


def population_by_ethnicity(counties: list[data.CountyDemographics], ethnicity: str) -> int:
    #ethnicity HAS to be any of the keys - HOW TO MAKE IT JUST RETURN ZERO
    sub_population = 0
    try:
        for county in counties:
            sub_population = sub_population + county.population['2014 Population']*(county.ethnicities[ethnicity]/100)
        return sub_population
    except:
        return "enter a valid ethnicity parameter."

def population_below_poverty_level(counties: list[data.CountyDemographics]) -> int:
    ppl_below = 0
    for county in counties:
        ppl_below = ppl_below + county.population['2014 Population']*(county.income['Persons Below Poverty Level']/100)
    return ppl_below


#part4
def percent_by_education(counties: list[data.CountyDemographics], key:str) -> float:
    try:
        population = population_total(counties)
        edulvl = population_by_education(counties, key)
        percentage = (edulvl/population)*100
        return percentage
    except:
        return "enter a valid education parameter"

def percent_by_ethnicity(counties: list[data.CountyDemographics], key:str) -> float:
    try:
        population = population_total(counties)
        ethlvl = population_by_ethnicity(counties, key)
        percentage = (ethlvl/population)*100
        return percentage
    except:
        return "enter a valid ethnicity parameter"



def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    population = population_total(counties)
    povlvl = population_below_poverty_level(counties)
    percentage = (povlvl/population)*100
    return percentage

#part5
def education_greater_than(counties: list[data.CountyDemographics], key: str, value: float) -> list[data.CountyDemographics]:
    greater_than = []
    for county in counties:
        if county.education[key] > value:
            greater_than.append(county)
    return greater_than

def education_less_than(counties: list[data.CountyDemographics], key: str, value: float) -> list[data.CountyDemographics]:
    less_than = []
    for county in counties:
        if county.education[key] < value:
            less_than.append(county)
    return less_than

def ethnicity_greater_than()

def ethnicity_less_than()

def below_poverty_level_greater_than(counties: list[data.CountyDemographics], value: float) -> list[data.CountyDemographics]:
    greater_than = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < value:
            greater_than.append(county)
    return greater_than

def below_poverty_level_greater_than()

def below_poverty_level_less_than()


