#Import pandas
import pandas as pd 
import matplotlib.pylab as plt 
import numpy as np

print("Reading the data set from the URL and adding the related headers")
filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
print("==================================================================================")
print("python list python containing name of headers")
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("=============================================================================")
print(" Use the pandas method read_csv() to load the adata from web address")
df = pd.read_csv(filename, names = headers)
print("Use the method head() to display the first five rows of the dataframe")
print(df.head())

print()
print("In the dataset missing data comes with the question mark , we replace it")
print("=============================================================")
print("replace ? to Nan")
df.replace("?",np.nan, inplace = True)
print(df.head())
print()
print("We using python built-in function to identfy these missing value")
missing_data = df.isnull()
print(missing_data.head())

print()
print("count missing values in each colume")
print("Using the loop in python we can quickly figureout the number of missing value")
print("========================================================================")
for column in missing_data.columns.values.tolist():
	print(column)
	print(missing_data[column].value_counts())
	print("")
print("==========================================================================")
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses: ", avg_norm_loss)

print("Replace NaN by mean value in normalized-losses clolumn: ")
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace = True)
print(df.head())
#Question 1
print()
print("=====================================================================")
print("According to the lab example above replace NaN in Stroke clumen by mean")
print("calculate the mean value for Stroke clolumn")
avg_storke = df["stroke"].astype("float").mean(axis = 0)
print("Avarge of the Storke: ", avg_storke)

print()
print("=======================================================================")
print("Calculate the mean value for the horsepower clumen")
avg_horsepower = df ["horsepower"].astype("float").mean(axis = 0)
print("Mean of the horsepower: ", avg_horsepower)

print("===========================================================================")
print("Replace NaN by mean value")
df["horsepower"].replace(np.nan, avg_horsepower, inplace = True)

print()
print("=============================================================================")
print("Calculate the mean for peak-rpm clumen")
avg_peakrpm = df ["peak-rpm"].astype("float").mean(axis = 0)
print("The mean value of peak-rpm: ",avg_peakrpm)

print()
print("Replace Nan by mean value")
df["peak-rpm"].replace(np.nan, avg_peakrpm, inplace = True)

print()
print()
print("To see which value are present a particular column we can see use the value_counts")
df["num-of-doors"].value_counts()
print()
print()
print("we can see that four doors are te most common type.")
df["num-of-doors"].value_counts().idxmax()
print("=============================================================================")
print("The replacement procedure is vary similar to what we have seen previsualy")
#replace the missing num-of-doors values by the most frequent
df["num-of-doors"].replace(np.nan, "four", inplace = True)
print("lets drop all rows that do not have price data:")
df.dropna(subset=["price"], axis=0, inplace=True)
print("reset index, because we droped two rows")
df.reset_index(drop=True, inplace=True)
print(df.head())

print("======================================================================================")
print(df.dtypes)

print("==================================================================================")
print("Convert data types to proper format")
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
print(df.dtypes)

print()
print("=======================================================================================")
print("convert mpg to l/100 km by mathematical operation 235/ divided by mpg")
df['city-L/100km']=235/df["city-mpg"]
#check the you transformed data
print(df.head())

print()
print("======================================================================================")
print("According to the example above, transformed mbp=g t L/100 km clumen of highway-mpg")
df ['highway-mpg'] = 235/df['highway-mpg']
# rename column name highway-mpg to highway-L/100km
df.rename(columns={'"highway-mpg"': 'highway-L/100km'}, inplace = True)
print(df.head())


output
.........................................................................................................................
Reading the data set from the URL and adding the related headers
==================================================================================
python list python containing name of headers
=============================================================================
 Use the pandas method read_csv() to load the adata from web address
Use the method head() to display the first five rows of the dataframe
   symboling normalized-losses         make fuel-type aspiration  ... horsepower peak-rpm city-mpg highway-mpg  price
0          3                 ?  alfa-romero       gas        std  ...        111     5000       21          27  13495
1          3                 ?  alfa-romero       gas        std  ...        111     5000       21          27  16500
2          1                 ?  alfa-romero       gas        std  ...        154     5000       19          26  16500
3          2               164         audi       gas        std  ...        102     5500       24          30  13950
4          2               164         audi       gas        std  ...        115     5500       18          22  17450

[5 rows x 26 columns]

In the dataset missing data comes with the question mark , we replace it
=============================================================
replace ? to Nan
   symboling normalized-losses         make fuel-type aspiration  ... horsepower peak-rpm city-mpg highway-mpg  price
0          3               NaN  alfa-romero       gas        std  ...        111     5000       21          27  13495
1          3               NaN  alfa-romero       gas        std  ...        111     5000       21          27  16500
2          1               NaN  alfa-romero       gas        std  ...        154     5000       19          26  16500
3          2               164         audi       gas        std  ...        102     5500       24          30  13950
4          2               164         audi       gas        std  ...        115     5500       18          22  17450

[5 rows x 26 columns]

We using python built-in function to identfy these missing value
   symboling  normalized-losses   make  fuel-type  aspiration  ...  horsepower  peak-rpm  city-mpg  highway-mpg  price
0      False               True  False      False       False  ...       False     False     False        False  False
1      False               True  False      False       False  ...       False     False     False        False  False
2      False               True  False      False       False  ...       False     False     False        False  False
3      False              False  False      False       False  ...       False     False     False        False  False
4      False              False  False      False       False  ...       False     False     False        False  False

[5 rows x 26 columns]

count missing values in each colume
Using the loop in python we can quickly figureout the number of missing value
========================================================================
symboling
False    205
Name: symboling, dtype: int64

normalized-losses
False    164
True      41
Name: normalized-losses, dtype: int64

make
False    205
Name: make, dtype: int64

fuel-type
False    205
Name: fuel-type, dtype: int64

aspiration
False    205
Name: aspiration, dtype: int64

num-of-doors
False    203
True       2
Name: num-of-doors, dtype: int64

body-style
False    205
Name: body-style, dtype: int64

drive-wheels
False    205
Name: drive-wheels, dtype: int64

engine-location
False    205
Name: engine-location, dtype: int64

wheel-base
False    205
Name: wheel-base, dtype: int64

length
False    205
Name: length, dtype: int64

width
False    205
Name: width, dtype: int64

height
False    205
Name: height, dtype: int64

curb-weight
False    205
Name: curb-weight, dtype: int64

engine-type
False    205
Name: engine-type, dtype: int64

num-of-cylinders
False    205
Name: num-of-cylinders, dtype: int64

engine-size
False    205
Name: engine-size, dtype: int64

fuel-system
False    205
Name: fuel-system, dtype: int64

bore
False    201
True       4
Name: bore, dtype: int64

stroke
False    201
True       4
Name: stroke, dtype: int64

compression-ratio
False    205
Name: compression-ratio, dtype: int64

horsepower
False    203
True       2
Name: horsepower, dtype: int64

peak-rpm
False    203
True       2
Name: peak-rpm, dtype: int64

city-mpg
False    205
Name: city-mpg, dtype: int64

highway-mpg
False    205
Name: highway-mpg, dtype: int64

price
False    201
True       4
Name: price, dtype: int64

==========================================================================
Average of normalized-losses:  122.0
Replace NaN by mean value in normalized-losses clolumn:
   symboling normalized-losses         make fuel-type aspiration  ... horsepower peak-rpm city-mpg highway-mpg  price
0          3               122  alfa-romero       gas        std  ...        111     5000       21          27  13495
1          3               122  alfa-romero       gas        std  ...        111     5000       21          27  16500
2          1               122  alfa-romero       gas        std  ...        154     5000       19          26  16500
3          2               164         audi       gas        std  ...        102     5500       24          30  13950
4          2               164         audi       gas        std  ...        115     5500       18          22  17450

[5 rows x 26 columns]

=====================================================================
According to the lab example above replace NaN in Stroke clumen by mean
calculate the mean value for Stroke clolumn
Avarge of the Storke:  3.2554228855721337

=======================================================================
Calculate the mean value for the horsepower clumen
Mean of the horsepower:  104.25615763546799
===========================================================================
Replace NaN by mean value

=============================================================================
Calculate the mean for peak-rpm clumen
The mean value of peak-rpm:  5125.369458128079

Replace Nan by mean value


To see which value are present a particular column we can see use the value_counts


we can see that four doors are te most common type.
=============================================================================
The replacement procedure is vary similar to what we have seen previsualy
lets drop all rows that do not have price data:
reset index, because we droped two rows
   symboling normalized-losses         make fuel-type aspiration  ... horsepower peak-rpm city-mpg highway-mpg  price
0          3               122  alfa-romero       gas        std  ...        111     5000       21          27  13495
1          3               122  alfa-romero       gas        std  ...        111     5000       21          27  16500
2          1               122  alfa-romero       gas        std  ...        154     5000       19          26  16500
3          2               164         audi       gas        std  ...        102     5500       24          30  13950
4          2               164         audi       gas        std  ...        115     5500       18          22  17450

[5 rows x 26 columns]
======================================================================================
symboling              int64
normalized-losses     object
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
body-style            object
drive-wheels          object
engine-location       object
wheel-base           float64
length               float64
width                float64
height               float64
curb-weight            int64
engine-type           object
num-of-cylinders      object
engine-size            int64
fuel-system           object
bore                  object
stroke                object
compression-ratio    float64
horsepower            object
peak-rpm              object
city-mpg               int64
highway-mpg            int64
price                 object
dtype: object
==================================================================================
Convert data types to proper format
symboling              int64
normalized-losses      int32
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
body-style            object
drive-wheels          object
engine-location       object
wheel-base           float64
length               float64
width                float64
height               float64
curb-weight            int64
engine-type           object
num-of-cylinders      object
engine-size            int64
fuel-system           object
bore                 float64
stroke               float64
compression-ratio    float64
horsepower            object
peak-rpm             float64
city-mpg               int64
highway-mpg            int64
price                float64
dtype: object

=======================================================================================
convert mpg to l/100 km by mathematical operation 235/ divided by mpg
   symboling  normalized-losses         make fuel-type  ... city-mpg highway-mpg    price city-L/100km
0          3                122  alfa-romero       gas  ...       21          27  13495.0    11.190476
1          3                122  alfa-romero       gas  ...       21          27  16500.0    11.190476
2          1                122  alfa-romero       gas  ...       19          26  16500.0    12.368421
3          2                164         audi       gas  ...       24          30  13950.0     9.791667
4          2                164         audi       gas  ...       18          22  17450.0    13.055556

[5 rows x 27 columns]

======================================================================================
According to the example above, transformed mbp=g t L/100 km clumen of highway-mpg
   symboling  normalized-losses         make fuel-type  ... city-mpg highway-mpg    price city-L/100km
0          3                122  alfa-romero       gas  ...       21    8.703704  13495.0    11.190476
1          3                122  alfa-romero       gas  ...       21    8.703704  16500.0    11.190476
2          1                122  alfa-romero       gas  ...       19    9.038462  16500.0    12.368421
3          2                164         audi       gas  ...       24    7.833333  13950.0     9.791667
4          2                164         audi       gas  ...       18   10.681818  17450.0    13.055556

[5 rows x 27 columns]
