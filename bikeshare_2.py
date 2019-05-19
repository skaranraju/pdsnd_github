import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        city = input("enter the name of the city to analyze\nchoose from chicago, new york city, washington\n").lower()
        if(city in ['chicago','new york city','washington']):
            break
        else:
            print("wrong input pls input again")
            continue
    while(True):
        choice = input("do you want to filter by month, day or not at all\n").lower()
        if(choice in ['month','day','not at all']):
            break
        else:
            print('enter valid input')
            continue
    


    if(choice == 'month'):
    # get user input for month (all, january, february, ... , june)
        while(True):
            month = input("enter the month to analyze between january and june, both included\nex:-january\n").lower()
            if(month in ['january','february','march','april','may','june']):
                return city, month, 'all'
            else:
                print("wrong input pls input again")
                continue
    if(choice == 'day'):
    # get user input for day of week (all, monday, tuesday, ... sunday)
        while(True):
            day = input("enter the day to analyze\nex:-monday\n").lower()
            if(day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']):
                return city, 'all', day
            else:
                print("wrong input pls input again")
                continue

    print('-'*40)
    return city, 'all', 'all'


def load_data(city, month, day):
   
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    # display the most popular month
    popular_month = df['month'].mode()[0]
    print('Most popular Month: ', popular_month)
    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most popular Day Of Week: ', popular_day_of_week)

    # display the most popular start hour
    df['hour'] = df['Start Time'].dt.hour


    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most popular used start station
    popular_start = df['Start Station'].mode()[0]
    print("Most popular Start Station: ",popular_start)

    # display most popular used end station
    popular_end = df['End Station'].mode()[0]
    print("Most popular End Station: ",popular_end )

    # display most popular combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + ' , ' + df['End Station']
    popular_start_end = df['Start End'].mode()[0]
    print("Most popular Start End Station Combo: ",popular_start_end )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Travel Time'].sum()
    print("Total Travel Time: ",total_travel_time)
    # display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print("Mean Travel Time: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscriber_count = df[df['User Type'] == 'Subscriber'].count()
    print("No. of users of the type subscriber are:  ",subscriber_count['Start Time'])
    customer_count = df[df['User Type'] == 'Customer'].count()
    print("No. of users of the type customer are:  ",customer_count['Start Time'])

    # Display counts of gender
    if(city in ['chicago','new york city']):
        male_count = df[df['Gender'] == 'Male'].count()
        print("No. of Male users are:  ",male_count['Start Time'])
        female_count = df[df['Gender'] == 'Female'].count()
        print("No. of Female users are:  ",female_count['Start Time'])
        # Display earliest, most recent, and most common year of birth
        
        earliest = df['Birth Year'].min()
        print("Earliest year of birth is: ",earliest)
        recent = df['Birth Year'].max()
        print("Recent year of birth is: ",recent)
        popular_birth = df['Birth Year'].mode()[0]
        print("popular year of birth is: ",popular_birth)
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """displays 5 lines of raw data to the user."""
    raw_data_choice = input("Do you want to see raw data, [y/n]:  ").lower()
    if(raw_data_choice in ['y','yes']):
        i = 0
        while(True):
            print(df.iloc[i:i+5])
            raw_data_choice = input("Do you want to see more: [y/n]:  ").lower()
            if(raw_data_choice in ['y','yes']):
                i += 5
                continue
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
