import time
import pandas as pd
import numpy as np

# Set the data
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
# Set general variables
months = ['junuary', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# Load the data
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington).
    

    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('Among Chicago, New York, Washington, which city you want to look into?: ').lower()

    while city not in CITY_DATA.keys():
        city = input('Sorry, select an available option. Choose a city between: Chicago, New York, Washington').lower()

    # Get a filter type from users
    filter_type = input('Would you like to filter the info by the month, day, both or none? : ').lower()

    while filter_type not in ['month', 'day', 'both']:
        filter_type = input('Wrong option, enter it again: ')

    if filter_type == 'month' or filter_type == 'both':
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('What month would you like to get information, from january through june or all?: ').lower()
        while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            month = input('Sorry, select an available month option.').lower()
    else:
        month = 'all'

    print('-' * 40)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day you want to retrieve info for or enter all for complete data: ").lower()
        if day not in days and day != "all":
            print(" The day you looking for is not part of the study. Please check your spelling")
            continue
        else:
            break

    print('-' * 40)
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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Start and End Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # columns month and weekday
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime((df['Start Time']))
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0] - 1
    # mode() The mode of a set of values is the value that appears most often. It can be multiple values.
    print("The most common month is: {}".format(common_month))
    #################################################

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common weekday: {}'.format(common_day))

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common used start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common used end station is: {} '.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " to " + df['End Station']
    print('The most common combination of start and end station is: {}'.format(
        df['combination'].mode()[0]
    ))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is {}'.format(total_travel))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The total travel time is: {}'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print('Distribution for user types:', user_types)
    if 'Gender' in df.columns:
        df['User Type'].value_counts()
        # TO DO: Display counts of gender
        df['Gender'].value_counts()
        # TO DO: Display earliest, most recent, and most common year of birth
        # Display earliest
        print('The earliest birth is: {}'.format(str(df['Birth Year'].min())))
        # Display the most common
        print('The most common birth is: {}'.format(str(df.mode()['Birth Year'][0])))
        # Display the most recent year
        print('The most recent year birthh is: {}'. format(str(df.mode()['Birth Year'].max())))
    else:
        print('The Column Gender or User Type was not found.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_data(df):
    """Ask for raw data to get the first 5 rows and then the next 5 raw data rows"""
    global i
    while True:
        display_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no: ')
        if display_data.lower() in ('yes', 'y'):
            i = 0
            print(df.iloc[i:i + 5])
        i += 5
        break
    while True:
        view_more_data = input('Do you wish to continue to see the next 5 rows of data? ').lower()
        if view_more_data == ('yes', 'y'):
            i += 5
            print(df.iloc[i:i + 10, :])
        else:
            break
    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you for checking!')
            break


if __name__ == "__main__":
    main()
