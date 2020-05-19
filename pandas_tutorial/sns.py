import seaborn as sns
import pandas as pd

data = pd.read_csv('Default.csv')
sns.relplot('income', 'balance', hue='student', style='default', data=data)