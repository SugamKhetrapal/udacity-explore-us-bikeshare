import numpy as np
import time
import json
class Statistics():
    df = None

    def __init__(self, df):
        self.df = df

    def time_stats(self):
        print("\n#1 Popular times of travel (i.e., occurs most often in the start time) \n")
        
        most_common_month = self.df['month'].value_counts().idxmax()
        print("Most Common Month:", most_common_month)

        most_common_day_of_week = self.df['day_of_week'].value_counts().idxmax()
        print("Most Common Day of Week:", most_common_day_of_week)

        most_common_start_hour = self.df['hour'].value_counts().idxmax()
        print("Most Common Start Hour:", most_common_start_hour)
        print('-------------------------------------------------------')

    def station_stats(self):
        print("\n#2 Popular stations and trip\n")

        most_common_start = self.df['Start Station'].value_counts().idxmax()
        print("Most Common Start Station:", most_common_start)

        most_common_end = self.df['End Station'].value_counts().idxmax()
        print("Most Common End Station:", most_common_end)

        most_common_start_end = self.df[['Start Station','End Station']].mode().loc[0]
        print("Most Common Trip from Start to End (i.e., most frequent combination of Start and End Station): {}, {}"\
                .format(most_common_start_end[0], most_common_start_end[1]))
        print('-------------------------------------------------------')

    def trip_duration_stats(self):
        print("\n#3 Trip Duration\n")

        total_time = self.df['Trip Duration'].sum()
        print("Total Travel Time:", total_time)

        mean_time = self.df['Trip Duration'].mean()
        print("Average Travel Time:", mean_time)

        max_time = self.df['Trip Duration'].max()
        print("Maximum Travel Time:", max_time)

        print("Travel time per user type:\n")
        grpByCount = self.df.groupby(['User Type']).sum()['Trip Duration']
        for i, c in enumerate(grpByCount):
            print("   {}: {}".format(grpByCount.index[i], c))
        print('-------------------------------------------------------')

    def user_stats(self):
        print("\n#4 User info\n")
        print("Counts of Each User Type:\n")
        uCount = self.df['User Type'].value_counts()
        for i, c in enumerate(uCount):
            print("{}::{}".format(uCount.index[i], c))

        if 'Gender' in self.df.columns:
            self.user_gender_stats()
        if 'Birth Year' in self.df.columns:
            self.user_birth_stats()
        print('-------------------------------------------------------')

    def user_gender_stats(self):
        print("Counts of Each Gender (only available for NYC and Chicago):\n")
        gCount = self.df['Gender'].value_counts()
        for i, c in enumerate(gCount):
            print("{}::{}".format(gCount.index[i], c))

    def user_birth_stats(self):
        birth_year = self.df['Birth Year']
        earliest_year = birth_year.min()
        print("Earliest Year of Birth: ", earliest_year)
        most_recent = birth_year.max()
        print("Most Recent Year of Birth: ",most_recent)
        most_common_year = birth_year.value_counts().idxmax()
        print("Most Common Year of Birth: ",most_common_year)

    def table_stats(self, city):
        print("\nCalculating Dataset Stats\n")
        
        num_missing = np.count_nonzero(self.df.isnull())
        print("Missing values in the {} data : {}".format(city, num_missing))

        num_nonzero = np.count_nonzero(self.df['User Type'].isnull())
        print("Missing values in the User Type column: {}".format(num_nonzero))
        print('-------------------------------------------------------')