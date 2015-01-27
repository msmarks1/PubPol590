## 2. Create a new python script and initialize it with the import etc. commands
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

## 3. Assign the main directory and files to a path.
main_dir = "/Users/mirandamarks/Documents/Documents/My Documents/Duke/Spring 2015/PubPol590/GitHub/PubPol590" #assigning to main directory
txt_file = "/File1_small.txt"

## 4. Use appropriate import function to import the data.
df = pd.read_table(main_dir + txt_file, sep = "\s")

## 5. Extract rows 60 to 99 of the DataFrame using row slicing
df[60:100]

## 6. Extract all the rows where electricity consumption (kwh) is greater than 30
df[df.kwh > 30]