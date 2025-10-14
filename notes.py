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
