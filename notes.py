"""

 Here are some of my initial thoughts:

    we drop 'id' column since we do not want it to have any impact on our prediction model,

    we drop 'episode name' column as the name of the column in the format 'Episode {number}' should not affect our prediction model 

"""

"""

Train dataset info:

                      id  Episode_Length_minutes  Host_Popularity_percentage  Guest_Popularity_percentage  Number_of_Ads  Listening_Time_minutes
    count  750000.000000           662907.000000               750000.000000                603970.000000  749999.000000           750000.000000
    mean   374999.500000               64.504738                   59.859901                    52.236449       1.348855               45.437406
    std    216506.495284               32.969603                   22.873098                    28.451241       1.151130               27.138306
    min         0.000000                0.000000                    1.300000                     0.000000       0.000000                0.000000
    25%    187499.750000               35.730000                   39.410000                    28.380000       0.000000               23.178350
    50%    374999.500000               63.840000                   60.050000                    53.580000       1.000000               43.379460
    75%    562499.250000               94.070000                   79.530000                    76.600000       2.000000               64.811580
    max    749999.000000              325.240000                  119.460000                   119.910000     103.910000              119.970000

    

    We have some off values:
        - Episode length minutes: we have a value of 0, which does not seem right,
        - Host popularity percentage: we have max value of >100% which cannot be,
        - Guest popularity percentage: same as above,
        - Number of ads: almost 104 ads in one episode seems impossible, we need to think what to do with this value



"""

"""
    Train columns info

    RangeIndex: 750000 entries, 0 to 749999
    Data columns (total 12 columns):
     #   Column                       Non-Null Count   Dtype  
    ---  ------                       --------------   -----  
     0   id                           750000 non-null  int64  
     1   Podcast_Name                 750000 non-null  object 
     2   Episode_Title                750000 non-null  object 
     3   Episode_Length_minutes       662907 non-null  float64
     4   Genre                        750000 non-null  object 
     5   Host_Popularity_percentage   750000 non-null  float64
     6   Publication_Day              750000 non-null  object 
     7   Publication_Time             750000 non-null  object 
     8   Guest_Popularity_percentage  603970 non-null  float64
     9   Number_of_Ads                749999 non-null  float64
     10  Episode_Sentiment            750000 non-null  object 
     11  Listening_Time_minutes       750000 non-null  float64
    dtypes: float64(5), int64(1), object(6)
    memory usage: 68.7+ MB
    None

    There is a few rows with values missing in columns ['Episode length', 'Guest popularity', 'Number of ads']:
        - it is not possible that the episode length was 0 - we need to somehow replace this values
            i do not think, that we can remove these rows because we will be missing almost 100k rows of data, which will greatly effect our prediction model accuracy.

        - on the other hand missing values in Guestr popularity could mean that there was no Guest present on the show? We could run some tests how the model will behave if we act like there was no Guest present on the show.
            we can do it like this: we change all the missing values to 0, and add another column called (was_guest_present) and set it to false everywhere the value is 0

        - 1 value missing seems to be missing, we could delete this row and not think much about replacing it at the beggining of the project. Later we can try replacing it for example with average value from all the cells in ads column
"""
