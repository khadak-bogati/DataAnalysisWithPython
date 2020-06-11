import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

print(df.head())

print("=============================================================================")
print("How to choose the right visualization method: ")
print("This will help us find the right visualization method for that variable: ")
print(df.dtypes)
print("=========================================================================")
print("What is the data type of the column peak-rpm?")
print()
print("we can calculate the correlation between variable of type int64 or float64 using the method corr.")

print(df.corr())
print("==========================================================================================")
print("Find the correlation between the following columns: bore, stroke, compression-ration and horsepower")
print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())

print("========================================================================================")
print("Continuous numerical variables: ")
print("Positive liner relationship")
print("Engine size as potential predictor variables of price: ")
sns.regplot(x='engine-size', y='price', data = df)
plt.ylim(0,)

print("========================================================================")
print(df[["engine-size", "price"]].corr())
print("=======================================================================")
print("Hightway mpg is a potential predictor variables of price")
sns.regplot(x="highway-mpg", y="price", data=df)
print(df[['highway-mpg', 'price']].corr())
print("=======================================================================")
print("weak Linear relationship")
sns.regplot(x='peak-rpm', y= "price", data=df)
print("we can exmine the correlation betwen peak-rpm and price and see it's approximately -0.101616")
print(df[['peak-rpm', 'price']].corr)
print("find the correlation between x= stroke and y = price")
print("---------------------------------------------------------------")
print(df[['stroke', 'price']].corr())

print("========================================================================")
print("Given the correlation resutl between price and storke do yo expect a liner relationship")
print("We can see this use regplot to demonstrate this")

sns.regplot(x='stroke', y='price', data=df)

print("Categorical variables")
print("Let's look at the relationship between body=style and prince")
print("=====================================================================================")
sns.boxplot(x='body-style', y='price', data=df)
#let's exmine engine location and price
sns.boxplot(x='engine-location', y='price', data=df)
#lets examine drevie while and price
sns.boxplot(x='drive-wheels', y='price', data=df)


print("Descriptive statistical Analysis")
print("we can the method describe as follows")
print(df.describe())

print("===========================================================================================")
print("The default setting describe skips variables of type object, we can apply the \nmethod describe on the varialbe of type object as follows")
print(df.describe(include=['object']))
print()
print("Value Counts")
print("lets repeat the above steps but save the results to the dataframe drive wheel_coutns and rename the column drive-wheels to value_coutnts")
drive_wheels_counts = df['drive-wheels'].value_coutnts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_coutnts'}, inplace=True)
print(drive_wheels_counts)



output
.......................
symboling  normalized-losses         make aspiration  ... city-L/100km horsepower-binned diesel gas
0          3                122  alfa-romero        std  ...    11.190476            Medium      0   1
1          3                122  alfa-romero        std  ...    11.190476            Medium      0   1
2          1                122  alfa-romero        std  ...    12.368421            Medium      0   1
3          2                164         audi        std  ...     9.791667            Medium      0   1
4          2                164         audi        std  ...    13.055556            Medium      0   1

[5 rows x 29 columns]
=============================================================================
How to choose the right visualization method:
This will help us find the right visualization method for that variable:
symboling              int64
normalized-losses      int64
make                  object
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
horsepower           float64
peak-rpm             float64
city-mpg               int64
highway-mpg            int64
price                float64
city-L/100km         float64
horsepower-binned     object
diesel                 int64
gas                    int64
dtype: object
=========================================================================
What is the data type of the column peak-rpm?

we can calculate the correlation between variable of type int64 or float64 using the method corr.
                   symboling  normalized-losses  wheel-base    length  ...     price  city-L/100km    diesel       gas
symboling           1.000000           0.466264   -0.535987 -0.365404  ... -0.082391      0.066171 -0.196735  0.196735
normalized-losses   0.466264           1.000000   -0.056661  0.019424  ...  0.133999      0.238567 -0.101546  0.101546
wheel-base         -0.535987          -0.056661    1.000000  0.876024  ...  0.584642      0.476153  0.307237 -0.307237
length             -0.365404           0.019424    0.876024  1.000000  ...  0.690628      0.657373  0.211187 -0.211187
width              -0.242423           0.086802    0.814507  0.857170  ...  0.751265      0.673363  0.244356 -0.244356
height             -0.550160          -0.373737    0.590742  0.492063  ...  0.135486      0.003811  0.281578 -0.281578
curb-weight        -0.233118           0.099404    0.782097  0.880665  ...  0.834415      0.785353  0.221046 -0.221046
engine-size        -0.110581           0.112360    0.572027  0.685025  ...  0.872335      0.745059  0.070779 -0.070779
bore               -0.140019          -0.029862    0.493244  0.608971  ...  0.543155      0.554610  0.054458 -0.054458
stroke             -0.008245           0.055563    0.158502  0.124139  ...  0.082310      0.037300  0.241303 -0.241303
compression-ratio  -0.182196          -0.114713    0.250313  0.159733  ...  0.071107     -0.299372  0.985231 -0.985231
horsepower          0.075819           0.217299    0.371147  0.579821  ...  0.809575      0.889488 -0.169053  0.169053
peak-rpm            0.279740           0.239543   -0.360305 -0.285970  ... -0.101616      0.115830 -0.475812  0.475812
city-mpg           -0.035527          -0.225016   -0.470606 -0.665192  ... -0.686571     -0.949713  0.265676 -0.265676
highway-mpg         0.036233          -0.181877   -0.543304 -0.698142  ... -0.704692     -0.930028  0.198690 -0.198690
price              -0.082391           0.133999    0.584642  0.690628  ...  1.000000      0.789898  0.110326 -0.110326
city-L/100km        0.066171           0.238567    0.476153  0.657373  ...  0.789898      1.000000 -0.241282  0.241282
diesel             -0.196735          -0.101546    0.307237  0.211187  ...  0.110326     -0.241282  1.000000 -1.000000
gas                 0.196735           0.101546   -0.307237 -0.211187  ... -0.110326      0.241282 -1.000000  1.000000

[19 rows x 19 columns]
==========================================================================================
Find the correlation between the following columns: bore, stroke, compression-ration and horsepower
                       bore    stroke  compression-ratio  horsepower
bore               1.000000 -0.055390           0.001263    0.566936
stroke            -0.055390  1.000000           0.187923    0.098462
compression-ratio  0.001263  0.187923           1.000000   -0.214514
horsepower         0.566936  0.098462          -0.214514    1.000000
========================================================================================
Continuous numerical variables:
Positive liner relationship
Engine size as potential predictor variables of price:
========================================================================
             engine-size     price
engine-size     1.000000  0.872335
price           0.872335  1.000000
=======================================================================
Hightway mpg is a potential predictor variables of price
             highway-mpg     price
highway-mpg     1.000000 -0.704692
price          -0.704692  1.000000
=======================================================================
weak Linear relationship
we can exmine the correlation betwen peak-rpm and price and see it's approximately -0.101616
<bound method DataFrame.corr of      peak-rpm    price
0      5000.0  13495.0
1      5000.0  16500.0
2      5000.0  16500.0
3      5500.0  13950.0
4      5500.0  17450.0
..        ...      ...
196    5400.0  16845.0
197    5300.0  19045.0
198    5500.0  21485.0
199    4800.0  22470.0
200    5400.0  22625.0

[201 rows x 2 columns]>
find the correlation between x= stroke and y = price
---------------------------------------------------------------
         stroke    price
stroke  1.00000  0.08231
price   0.08231  1.00000
========================================================================
Given the correlation resutl between price and storke do yo expect a liner relationship
We can see this use regplot to demonstrate this
Categorical variables
Let's look at the relationship between body=style and prince
=====================================================================================
Descriptive statistical Analysis
we can the method describe as follows
        symboling  normalized-losses  wheel-base      length  ...         price  city-L/100km      diesel         gas
count  201.000000          201.00000  201.000000  201.000000  ...    201.000000    201.000000  201.000000  201.000000
mean     0.840796          122.00000   98.797015    0.837102  ...  13207.129353      9.944145    0.099502    0.900498
std      1.254802           31.99625    6.066366    0.059213  ...   7947.066342      2.534599    0.300083    0.300083
min     -2.000000           65.00000   86.600000    0.678039  ...   5118.000000      4.795918    0.000000    0.000000
25%      0.000000          101.00000   94.500000    0.801538  ...   7775.000000      7.833333    0.000000    1.000000
50%      1.000000          122.00000   97.000000    0.832292  ...  10295.000000      9.791667    0.000000    1.000000
75%      2.000000          137.00000  102.400000    0.881788  ...  16500.000000     12.368421    0.000000    1.000000
max      3.000000          256.00000  120.900000    1.000000  ...  45400.000000     18.076923    1.000000    1.000000

[8 rows x 19 columns]
===========================================================================================
The default setting describe skips variables of type object, we can apply the
method describe on the varialbe of type object as follows
          make aspiration num-of-doors body-style  ... engine-type num-of-cylinders fuel-system horsepower-binned
count      201        201          201        201  ...         201              201         201               200
unique      22          2            2          5  ...           6                7           8                 3
top     toyota        std         four      sedan  ...         ohc             four        mpfi               Low
freq        32        165          115         94  ...         145              157          92               115

[4 rows x 10 columns]

Value Counts
lets repeat the above steps but save the results to the dataframe drive wheel_coutns and rename the column drive-wheels to value_coutnts
Traceback (most recent call last):
  File "project.py", line 73, in <module>
    drive_wheels_counts = df['drive-wheels'].value_coutnts().to_frame()
  File "C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'value_coutnts'
