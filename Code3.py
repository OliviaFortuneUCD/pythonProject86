# The example is to create
# pandas dataframe from lists using zip.

import pandas as pd

# List1
Name = ['Peter', 'John', 'Chris', 'Stella']

# List2
Marks = [95, 63, 54, 47]

#  two lists.
# and merge them by using zip().
list_tuples = list(zip(Name, Marks))

# Assign data to tuples.
print(list_tuples)

# Converting lists of tuples into
# pandas Dataframe.
dframe = pd.DataFrame(list_tuples, columns=['Name', 'Marks'])

# Print data.
print(dframe)