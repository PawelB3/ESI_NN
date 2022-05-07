import numpy as np
import pandas as pd


df = pd.read_excel('data_heart_disease.xlsx')

for i in df:
    print(i)