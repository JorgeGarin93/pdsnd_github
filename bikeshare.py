#!/usr/bin/env python
# coding: utf-8

# In this comments i will be trying to explain the main structure of this code made in python.

# First of all, we'll be needing to store the choices of the user about the city he'll be wanting
#to study, and if he/she want to filter by any day of the week or month.

# After this, we need to load the data that the user wants to study so later on we can
#calculate the KPI's

import pandas as pd
import numpy as np
import time


CITY_DATA = { 'chicago': 'chicago.csv',
               'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


day_of_week = {0:  'Monday',
                1 : 'Tuesday',
                2 : 'Wednesday',
                3 : 'Thursday',
                4 : 'Friday',
                5 : 'Saturday',
                6 : 'Sunday'}

month_of_year = {
                  1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June'
                    }


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Please select the city you want to know about (Chicago, New York City or Washington)")
    city = input()
    print("Do you want to select any particular month? If you do, please choose one between January and June. If you don't insert the word ALL")
    month = input()
    print("Do you want to select any particular day of the week? If you don't, please type the word ALL")
    day = input()


    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

   
    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month2 = months.index(month.lower())+1
    
        # filter by month to create the new dataframe
        dfFilter1 = df['month'].apply(lambda x: (x == month2))
        df = df[dfFilter1]
    else:
        df = df

    # filter by day of week if applicable
    if day.lower() != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day2 = days.index(day.lower())       
        # filter by day of week to create the new dataframe
        dfFilter2 = df['day_of_week'].apply(lambda x: (x == day2))
        df = df[dfFilter2]
    else:
        df = df
    
    return df

# By now, we have accomplished our first goal, load the data using the filters given by the user
# 
# Our next step is to calculate the KPI's based on the dataframe DF 
# This KPI's can be divided by topic
#	- Time Stats
#	- Station stats
#	- Trip Duration Stats
#	- User Stats
# 
# Remember, after calculating those indicators, we need to ask the user again if he wants to start
#again with the entire excercise. So we need to build a function to do this.

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("Most Common Day of the week is: ", day_of_week.get(df['Start Time'].dt.dayofweek.mode().values[0]))
    print("Most Common Month is: ", month_of_year.get(df['Start Time'].dt.month.mode().values[0]))
    print("Most Common Starting Hour is: ", df['Start Time'].dt.hour.mode().values[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    df['Start - End Combination'] = df['Start Station'].astype(str) + ' - ' + df['End Station'].astype(str)
    print("Most Common Starting Station is: ", df['Start Station'].mode().values[0])
    print("Most Common Ending Station is: ", df['End Station'].mode().values[0])
    print("Most Common Star-End Combination is: ", df['Start - End Combination'].mode().values[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total time spent in trips is: ", df['Trip Duration'].sum())
    
    # display mean travel time
    print("Average time spent in trips is: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User counting: ", df['User Type'].value_counts())

    # Display counts of gender
    try:
        print("The most frecuent gender is: ", df['Gender'].value_counts())
        
    except :
        pass

    # Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth", df['Birth Year'].min())
        print("The most recent year of birth", df['Birth Year'].max())
        print("The most common year of birth", df['Birth Year'].mode())
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


<<<<<<< HEAD
=======
#WARNING: we have to remember, not all the csv files has the same columns so we have to addapt to that

>>>>>>> refactoring

def raw_data(df):
    print('Would you like to see individual trip data? (Yes/No)')
    trip_data = input()

    if trip_data.lower() == 'yes':
        print(df.head(10))
    else:
        print('Ok then ...')



#INPUT CONSULTA
def main():
    #consulta = True
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)       
        df = time_stats(df)
        df = station_stats(df)
        df = trip_duration_stats(df)
        df = user_stats(df)
        df = raw_data(df)
        
        print("Type yes if you want to restart (Yes/No)")
        entrada = input()
        if entrada.lower() == 'yes':
            del df
            consulta = True
            
        else:
            del df
            consulta = False
            
            print("Goodbye")
            break
        
if __name__ == "__main__":
	main()



#As we finished coding here, always remember to check if every part for every user cases works fine
