import pandas as pd

file = pd.read_csv('titanic.csv')

# __ Basic info ________________________________________________________________
# print(file.to_string())             # print the entire dataframe
# print(file)                         # prints first & last 5 rows by default
# print(pd.options.display.max_rows)  # default is 60 rows
# pd.options.display.max_rows = 9999  # increase the display limit

# print(file.head(10))  # first 10 rows (default is 5 if brackets are empty)
# print(file.tail())    # last 5 rows

print(file.info())

# __ Cleaning ________________________________________________________________
no_empty_cells = file.dropna()          # remove rows with any empty cell (original unchanged)
# file.dropna(inplace=True)            # inplace=True modifies the original dataframe directly
# file.fillna('Unknown', inplace=True) # fill all empty cells with 'Unknown' instead of dropping

print(no_empty_cells.to_string())       # print cleaned dataframe (all rows)
print(no_empty_cells.shape)  #(183,12)           # (rows, columns) after cleaning

# __ Basic stats ________________________________________________________________
print(no_empty_cells.describe())        # count, mean, std, min, max for numeric columns
# print(no_empty_cells['Age'].mean())   # average age
# print(no_empty_cells['Age'].median()) # median age
# print(no_empty_cells['Age'].mode())   # the value that appears most frequently.

# __ Filtering ________________________________________________________________
survivors = no_empty_cells[no_empty_cells['Survived'] == 1]  # rows where survived = 1
# died    = no_empty_cells[no_empty_cells['Survived'] == 0]  # rows where survived = 0

print(survivors.head())                 # first 5 survivors

#__ Correlation ________________________________________________________________
print(no_empty_cells.corr(numeric_only=True))  # correlation matrix for all numeric columns