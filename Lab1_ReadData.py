#Import pandas library
import pandas as pd 

#Read the online file by use the URL provides above and asign it variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header = None)

print()
print("Show the first  5 rows using dataframe.head() method")
print("The first 5 rows of the dataframe")
print(df.head(5))
print()
# Question: 1
print("Check the bottom 10 rows of data frame 'df'.")
print("===============================================================")
print(df.tail(10))

print()
print("Firstly create a list header than include all colume names in order")
#Create the headers list
print("===================================================================================================================")
headers = ["khadak0", "khadak1", "khadak2","khadak3","khadak4","khadak5","khadak6","khadak7","khadak8","khadak7","khadak8","khadak9","khadak10","khadak11","khadak12","khadak13","khadak14","khadak15","khadak16","khadak17","khadak18","khadak19","khadak20","khadak21","khadak22","khadak23","khadak24"]
df.columes = headers
print(df.head(10))
print("===================================================================================")
print(df.columes)

print()
print("if you would save the dataframe df as automobile.csv to you local you may use the systax below")
df.to_csv("automobile.csv", index=False)

#Data has a varity types 

print("=======================================================================================")
print("Check the data type of date frame df by .dtype")
print((df.dtypes))

print("if we would like to get a statical summary of each clumn such as count,colume")
print(df.describe(include = "all"))

print()
print()
print("You can select columns of a data frame by indicasting the anme of each colume:")
print(df.info)


output
..........................................................................................
Show the first  5 rows using dataframe.head() method
The first 5 rows of the dataframe
   0    1            2    3    4     5            6    7      8   ...    17    18    19    20   21    22  23  24     25
0   3    ?  alfa-romero  gas  std   two  convertible  rwd  front  ...  mpfi  3.47  2.68   9.0  111  5000  21  27  13495
1   3    ?  alfa-romero  gas  std   two  convertible  rwd  front  ...  mpfi  3.47  2.68   9.0  111  5000  21  27  16500
2   1    ?  alfa-romero  gas  std   two    hatchback  rwd  front  ...  mpfi  2.68  3.47   9.0  154  5000  19  26  16500
3   2  164         audi  gas  std  four        sedan  fwd  front  ...  mpfi  3.19  3.40  10.0  102  5500  24  30  13950
4   2  164         audi  gas  std  four        sedan  4wd  front  ...  mpfi  3.19  3.40   8.0  115  5500  18  22  17450

[5 rows x 26 columns]

Check the bottom 10 rows of data frame 'df'.
===============================================================
     0    1      2       3      4     5      6    7      8   ...    17    18    19    20   21    22  23  24     25
195  -1   74  volvo     gas    std  four  wagon  rwd  front  ...  mpfi  3.78  3.15   9.5  114  5400  23  28  13415
196  -2  103  volvo     gas    std  four  sedan  rwd  front  ...  mpfi  3.78  3.15   9.5  114  5400  24  28  15985
197  -1   74  volvo     gas    std  four  wagon  rwd  front  ...  mpfi  3.78  3.15   9.5  114  5400  24  28  16515
198  -2  103  volvo     gas  turbo  four  sedan  rwd  front  ...  mpfi  3.62  3.15   7.5  162  5100  17  22  18420
199  -1   74  volvo     gas  turbo  four  wagon  rwd  front  ...  mpfi  3.62  3.15   7.5  162  5100  17  22  18950
200  -1   95  volvo     gas    std  four  sedan  rwd  front  ...  mpfi  3.78  3.15   9.5  114  5400  23  28  16845
201  -1   95  volvo     gas  turbo  four  sedan  rwd  front  ...  mpfi  3.78  3.15   8.7  160  5300  19  25  19045
202  -1   95  volvo     gas    std  four  sedan  rwd  front  ...  mpfi  3.58  2.87   8.8  134  5500  18  23  21485
203  -1   95  volvo  diesel  turbo  four  sedan  rwd  front  ...   idi  3.01  3.40  23.0  106  4800  26  27  22470
204  -1   95  volvo     gas  turbo  four  sedan  rwd  front  ...  mpfi  3.78  3.15   9.5  114  5400  19  25  22625

[10 rows x 26 columns]

Firstly create a list header than include all colume names in order
===================================================================================================================
project.py:23: UserWarning: Pandas doesn't allow columns to be created via a new attribute name - see https://pandas.pydata.org/pandas-docs/stable/indexing.html#attribute-access
  df.columes = headers
   0    1            2    3      4     5            6    7      8   ...    17    18    19    20   21    22  23  24     25
0   3    ?  alfa-romero  gas    std   two  convertible  rwd  front  ...  mpfi  3.47  2.68   9.0  111  5000  21  27  13495
1   3    ?  alfa-romero  gas    std   two  convertible  rwd  front  ...  mpfi  3.47  2.68   9.0  111  5000  21  27  16500
2   1    ?  alfa-romero  gas    std   two    hatchback  rwd  front  ...  mpfi  2.68  3.47   9.0  154  5000  19  26  16500
3   2  164         audi  gas    std  four        sedan  fwd  front  ...  mpfi  3.19  3.40  10.0  102  5500  24  30  13950
4   2  164         audi  gas    std  four        sedan  4wd  front  ...  mpfi  3.19  3.40   8.0  115  5500  18  22  17450
5   2    ?         audi  gas    std   two        sedan  fwd  front  ...  mpfi  3.19  3.40   8.5  110  5500  19  25  15250
6   1  158         audi  gas    std  four        sedan  fwd  front  ...  mpfi  3.19  3.40   8.5  110  5500  19  25  17710
7   1    ?         audi  gas    std  four        wagon  fwd  front  ...  mpfi  3.19  3.40   8.5  110  5500  19  25  18920
8   1  158         audi  gas  turbo  four        sedan  fwd  front  ...  mpfi  3.13  3.40   8.3  140  5500  17  20  23875
9   0    ?         audi  gas  turbo   two    hatchback  4wd  front  ...  mpfi  3.13  3.40   7.0  160  5500  16  22      ?

[10 rows x 26 columns]
===================================================================================
['khadak0', 'khadak1', 'khadak2', 'khadak3', 'khadak4', 'khadak5', 'khadak6', 'khadak7', 'khadak8', 'khadak7', 'khadak8', 'khadak9', 'khadak10', 'khadak11', 'khadak12', 'khadak13', 'khadak14', 'khadak15', 'khadak16', 'khadak17', 'khadak18', 'khadak19', 'khadak20', 'khadak21', 'khadak22', 'khadak23', 'khadak24']

if you would save the dataframe df as automobile.csv to you local you may use the systax below
=======================================================================================
Check the data type of date frame df by .dtype
0       int64
1      object
2      object
3      object
4      object
5      object
6      object
7      object
8      object
9     float64
10    float64
11    float64
12    float64
13      int64
14     object
15     object
16      int64
17     object
18     object
19     object
20    float64
21     object
22     object
23      int64
24      int64
25     object
dtype: object
if we would like to get a statical summary of each clumn such as count,colume
                0    1       2    3    4     5      6   ...    19          20   21    22          23          24   25
count   205.000000  205     205  205  205   205    205  ...   205  205.000000  205   205  205.000000  205.000000  205
unique         NaN   52      22    2    2     3      5  ...    37         NaN   60    24         NaN         NaN  187
top            NaN    ?  toyota  gas  std  four  sedan  ...  3.40         NaN   68  5500         NaN         NaN    ?
freq           NaN   41      32  185  168   114     96  ...    20         NaN   19    37         NaN         NaN    4
mean      0.834146  NaN     NaN  NaN  NaN   NaN    NaN  ...   NaN   10.142537  NaN   NaN   25.219512   30.751220  NaN
std       1.245307  NaN     NaN  NaN  NaN   NaN    NaN  ...   NaN    3.972040  NaN   NaN    6.542142    6.886443  NaN
min      -2.000000  NaN     NaN  NaN  NaN   NaN    NaN  ...   NaN    7.000000  NaN   NaN   13.000000   16.000000  NaN
25%       0.000000  NaN     NaN  NaN  NaN   NaN    NaN  ...   NaN    8.600000  NaN   NaN   19.000000   25.000000  NaN
50%       1.000000  NaN     NaN  NaN  NaN   NaN    NaN  ...   NaN    9.000000  NaN   NaN   24.000000   30.000000  NaN
75%       2.000000  NaN     NaN  NaN  NaN   NaN    NaN  ...   NaN    9.400000  NaN   NaN   30.000000   34.000000  NaN
max       3.000000  NaN     NaN  NaN  NaN   NaN    NaN  ...   NaN   23.000000  NaN   NaN   49.000000   54.000000  NaN

[11 rows x 26 columns]


You can select columns of a data frame by indicasting the anme of each colume:
<bound method DataFrame.info of      0    1            2       3      4     5            6    7   ...    18    19    20   21    22  23  24     25
0     3    ?  alfa-romero     gas    std   two  convertible  rwd  ...  3.47  2.68   9.0  111  5000  21  27  13495
1     3    ?  alfa-romero     gas    std   two  convertible  rwd  ...  3.47  2.68   9.0  111  5000  21  27  16500
2     1    ?  alfa-romero     gas    std   two    hatchback  rwd  ...  2.68  3.47   9.0  154  5000  19  26  16500
3     2  164         audi     gas    std  four        sedan  fwd  ...  3.19  3.40  10.0  102  5500  24  30  13950
4     2  164         audi     gas    std  four        sedan  4wd  ...  3.19  3.40   8.0  115  5500  18  22  17450
..   ..  ...          ...     ...    ...   ...          ...  ...  ...   ...   ...   ...  ...   ...  ..  ..    ...
200  -1   95        volvo     gas    std  four        sedan  rwd  ...  3.78  3.15   9.5  114  5400  23  28  16845
201  -1   95        volvo     gas  turbo  four        sedan  rwd  ...  3.78  3.15   8.7  160  5300  19  25  19045
202  -1   95        volvo     gas    std  four        sedan  rwd  ...  3.58  2.87   8.8  134  5500  18  23  21485
203  -1   95        volvo  diesel  turbo  four        sedan  rwd  ...  3.01  3.40  23.0  106  4800  26  27  22470
204  -1   95        volvo     gas  turbo  four        sedan  rwd  ...  3.78  3.15   9.5  114  5400  19  25  22625

[205 rows x 26 columns]>
