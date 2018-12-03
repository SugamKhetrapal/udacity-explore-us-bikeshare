import pandas as pd
import constants
import stats

class BikeShare():

    def user_input(self):
        city_name = ""
        while True:
            city_name = input("Please enter city out of Chicago(C), New York(N), Washington(W)\n").upper()
            if city_name in constants.Constants.CITIES.keys():
                city_name = constants.Constants.CITIES[city_name]
                break
        print("City Selected is: ",(city_name))
        
        month_name = ""
        while True:
            month_name = input("Either Enter one month among JAN, FEB, MAR, APR, MAY, JUN (OR) Enter ALL\n").upper()
            if month_name == constants.Constants.ALL or month_name in constants.Constants.MONTHS.keys():
                break
        print("Month Selected is: ",(month_name))

        day = ""
        while True:
            day = input("Either Enter one weekday among SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY (OR) Enter ALL\n").upper()
            if day == constants.Constants.ALL or day in constants.Constants.DAYS:
                break
        print("Day Selected is: ",(day))
        return city_name, month_name, day

    def load_city_file(self, city, month, day):
        df = pd.read_csv(constants.Constants.CITY_FILES[city])
        start_time_col = 'Start Time'
        df[start_time_col] = pd.to_datetime(df[start_time_col])

        df['month'] = df[start_time_col].dt.month
        df['day_of_week'] = df[start_time_col].dt.weekday_name
        df['hour'] = df[start_time_col].dt.hour

        if month != constants.Constants.ALL:
            month_num =  constants.Constants.MONTHS[month]
            df = df[ df['month'] == month_num ]

        if day != constants.Constants.ALL:
            df = df[ df['day_of_week'] == day.title()]
        
        return df

def main():
    print('-------------------------------------')
    print('Machine Learning Foundation - Udacity')
    print('Project #1: Explore US Bikeshare Data')
    print('Student Name: Sugam Khetrapal')
    print('-------------------------------------')
    
    while True:
        bkshare = BikeShare()
        city_name, month_name, day = bkshare.user_input()
        df = bkshare.load_city_file(city_name, month_name, day)
        statistics = stats.Statistics(df)
        statistics.time_stats()
        statistics.station_stats()
        statistics.trip_duration_stats()
        statistics.user_stats()
        statistics.table_stats(city_name)

        start_again = input("Do you want to start again? (Y/N)").upper()
        if start_again == 'N':
            break
        
if __name__ == "__main__":
        main()
        