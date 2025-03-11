import numpy as np
import pandas as pd 
from scipy.stats import mannwhitneyu
from scipy.stats import ttest_ind
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm.auto import tqdm
from scipy.stats import pearsonr
from scipy.stats import shapiro

path = 'ab_testing.csv'
df = pd.read_csv(path)

# print(df.head())
# вывели первые 5 строк из таблицы;

# print(df.nunique())
# итоговое количество

# print(df.describe())
# Метод describe показывает основные 
# статистические характеристики данных по каждому числовому признаку