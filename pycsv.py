Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd

# Step 1: Load CSV file
df = pd.read_csv("1experience.csv")

# Step 2: Display DataFrame
print("Dataset:")
print(df)

# Step 3: Central Tendencies
mean = df['Experience'].mean()
median = df['Experience'].median()
mode = df['Experience'].mode()[0]

print("\nCentral Tendencies:")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# Step 4: Dispersion Measures
variance = df['Experience'].var()
std_dev = df['Experience'].std()
minimum = df['Experience'].min()
maximum = df['Experience'].max()

print("\nDispersion Measures:")
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Min:", minimum)
print("Max:", maximum)
# Step 1: Load CSV file
df = pd.read_csv('C:/Users/Chandu/OneDrive/Desktop/11prog_3Salary_Data.csv')
# Step 2: Display DataFrame
print("Dataset:")
Dataset:
print(df)
# Step 3: Central Tendencies
mean = df['Experience'].mean()
SyntaxError: multiple statements found while compiling a single statement
print(df)
    YearsExperience  Salary
0               1.1   39343
1               1.3   46205
2               1.5   37731
3               2.0   43525
4               2.2   39891
5               2.9   56642
6               3.0   60150
7               3.2   54445
8               3.2   64445
9               3.7   57189
10              3.9   63218
11              4.0   55794
12              4.0   56957
13              4.1   57081
14              4.5   61111
15              4.9   67938
16              5.1   66029
17              5.3   83088
18              5.9   81363
19              6.0   93940
20              6.8   91738
21              7.1   98273
22              7.9  101302
23              8.2  113812
24              8.7  109431
25              9.0  105582
26              9.5  116969
27              9.6  112635
28             10.3  122391
29             10.5  121872
# Step 3: Central Tendencies
mean = df['YearsExperience'].mean()
median = df['YearsExperience'].median()
mode = df['Experience'].mode()[0]
Traceback (most recent call last):
  File "C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Experience'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    mode = df['Experience'].mode()[0]
  File "C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Experience'
mode = df['YearsExperience'].mode()[0]
print("\nCentral Tendencies:")

Central Tendencies:
print("Mean:", mean)
Mean: 5.3133333333333335
print("Median:", median)
Median: 4.7
print("Mode:", mode)
Mode: 3.2
# Step 4: Dispersion Measures
variance = df['Experience'].var()
Traceback (most recent call last):
  File "C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Experience'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    variance = df['Experience'].var()
  File "C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Chandu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Experience'
variance = df['YearsExperience'].var()
std_dev = df['YearsExperience'].std()
minimum = df['YearsExperience'].min()
maximum = df['YearsExperience'].max()
print("\nDispersion Measures:")

Dispersion Measures:
print("Variance:", variance)
Variance: 8.053609195402299
print("Standard Deviation:", std_dev)
Standard Deviation: 2.8378881576627184
print("Min:", minimum)
Min: 1.1
print("Max:", maximum)
Max: 10.5






... 
>>> 

>>> 

... 
... 
>>> 

>>> 

>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> # Load data
... df = pd.read_csv('C:/Users/Chandu/OneDrive/Desktop/11prog_3Salary_Data.csv')
>>> # Basic info
... print("Summary Statistics:")
Summary Statistics:
>>> print(df['YearsExperience'].describe())
count    30.000000
mean      5.313333
std       2.837888
min       1.100000
25%       3.200000
50%       4.700000
75%       7.700000
max      10.500000
Name: YearsExperience, dtype: float64
>>> 
... # Histogram (distribution)
... plt.hist(df['YearsExperience'], bins=5)
(array([6., 9., 5., 4., 6.]), array([ 1.1 ,  2.98,  4.86,  6.74,  8.62, 10.5 ]), <BarContainer object of 5 artists>)
>>> plt.title("Employee Experience Distribution")
Text(0.5, 1.0, 'Employee Experience Distribution')
>>> plt.xlabel("Years of Experience")
Text(0.5, 0, 'Years of Experience')
>>> plt.ylabel("Number of Employees")
Text(0, 0.5, 'Number of Employees')
>>> plt.show()
plt.close()
>>> # Boxplot (outliers + spread)
... plt.boxplot(df['YearsExperience'])
{'whiskers': [<matplotlib.lines.Line2D object at 0x000002A03578E490>, <matplotlib.lines.Line2D object at 0x000002A03578E5D0>], 'caps': [<matplotlib.lines.Line2D object at 0x000002A03578E710>, <matplotlib.lines.Line2D object at 0x000002A03578E850>], 'boxes': [<matplotlib.lines.Line2D object at 0x000002A03578E350>], 'medians': [<matplotlib.lines.Line2D object at 0x000002A03578E990>], 'fliers': [<matplotlib.lines.Line2D object at 0x000002A03578EAD0>], 'means': []}
>>> plt.title("Boxplot of Experience")
Text(0.5, 1.0, 'Boxplot of Experience')
>>> plt.show()
