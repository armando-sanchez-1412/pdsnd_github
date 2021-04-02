import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input(
                "\nPlease enter the city number:\n1. Chicago\n2. New York\n3. Washington\n").strip()
            if int(city) > 0 and int(city) <= len(CITIES):
                city = CITIES[int(city)-1]
                break
            else:
                print(
                    "Sorry, there is no data available for city with number '{}' ".format(city))
        except ValueError:
            print("Sorry, please enter a valid value from the list")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input(
                "\nPlease enter the month\n0. all\n1. january\n2. february\n3. march\n4. april\n5. may\n6. june\n").strip()
            if int(month) >= 0 and int(month) <= len(MONTHS):
                month = MONTHS[int(month)]
                break
            else:
                print("Sorry, '{}' is not a valid month number".format(month))
        except ValueError:
            print("Sorry, please enter a valid value from the list")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input(
                "\nPlease enter a day of week\n0. all\n1. monday\n2. tuesday\n3. wednesday\n4. thursday\n5. friday\n6. saturday\n7. sunday\n").strip()
            if int(day) >= 0 and int(day) <= len(DAYS)-1:
                break
            else:
                print("Sorry, '{}' is not a valid day number".format(day))
        except ValueError:
            print("Sorry, please enter a valid value from the list")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        df = pd.read_csv(CITY_DATA[city])

        # # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.dayofweek
        df['hour'] = df['Start Time'].dt.hour

        if month != 'all':
            # filter by month to create the new dataframe
            month = MONTHS.index(month)
            df = df[(df.month == month)]

        if day != '0':
            # filter by day to create the new dataframe
            df = df[(df.day_of_week == int(day)-1)]

    except Exception as e:
            print("Sorry, there was an error loading the data: {}".format(e))

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    try:
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        common_month = df['month'].mode()[0]
        print('\nThe most popular month is: {}'.format(MONTHS[common_month]))

        # TO DO: display the most common day of week
        common_day_of_week = df['day_of_week'].mode()[0]
        print('\nThe most popular day of week is: {}'.format(DAYS[common_day_of_week+1]))

        # TO DO: display the most common start hour
        common_hour = df['hour'].mode()[0]
        print("\nThe most popular hour is at: {} hrs".format(common_hour))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
            print("Sorry, there was an error calculating time stats: {}".format(e))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    try:
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        common_start_station = df['Start Station'].mode()[0]
        print('\nThe most popular start station is: {}'.format(common_start_station))

        # TO DO: display most commonly used end station
        common_end_station = df['End Station'].mode()[0]
        print('\nThe most popular end station is: {}'.format(common_end_station))

        # TO DO: display most frequent combination of start station and end station trip
        common_start_end_stations = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
        print('\nThe most frequent combination between start and end station is: {}'.format(common_start_end_stations))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
            print("Sorry, there was an error calculating station stats: {}".format(e))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    try:
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        total_travel_time = df['Trip Duration'].sum()
        print('\nThe total travel time is: {}'.format(total_travel_time))

        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        print('\nThe mean travel time is: {}'.format(mean_travel_time))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
            print("Sorry, there was an error calculating trip duration stats: {}".format(e))


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        count_per_user_types = df['User Type'].value_counts()
        print('\nCount per user type: \n{}'.format(count_per_user_types))

        # TO DO: Display counts of gender
        if(city != 'washington'): #Washington data does not has Gender or Birth Year data
            count_per_gender = df['Gender'].value_counts()
            print('\nCount per gender: \n{}'.format(count_per_gender))

            # TO DO: Display earliest, most recent, and most common year of birth
            earliest_birth_year = df['Birth Year'].min()
            most_recent_birth_year = df['Birth Year'].max()
            common_birth_year = df['Birth Year'].mode()[0]
            print('\nEarliest year of birth is: {}'.format(earliest_birth_year))
            print('\nMost recent year of birth is: {}'.format(most_recent_birth_year))
            print('\nThe most common year of birth is: {}'.format(common_birth_year))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
            print("Sorry, there was an error calculating user stats: {}".format(e))

def show_raw_data(df):
    """Displays raw lines of raw data if the user accepts"""

    try:
        start_index = 0
        end_index = 5
        message = "Would you like to see the first 5 lines of raw data? Please enter a number:"
        while True:
            raw_data = input("\n{}\n1. Yes\n2. No\n".format(message)).strip()
            if raw_data == "1":
                print(df.iloc[start_index:end_index])
                start_index = end_index
                end_index += 5
                message = "Would you like to see the next 5 lines of raw data? Please enter a number:"
            elif raw_data == "2":
                break
            else:
                print("Sorry, '{}' is not a valid option".format(raw_data))
    except Exception as e:
            print("Sorry, there was an error processing your request: {}".format(e))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
