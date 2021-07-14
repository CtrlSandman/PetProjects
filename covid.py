import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Creating the basic dataframe from the JHU data on Covid
df = pd.read_csv("covid-data.csv", error_bad_lines=False, comment="#",
                 low_memory=False)

# What do we have
print(df.head)
print(df.columns)

# Making dataframe with the latest numbers
today = max(df['date'])
df_latest = df.loc[df['date'] == today]

# Selecting European region
df_eur = df_latest.loc[df_latest['continent'] == 'Europe']

# Finding the missing values in the columns to be used
print('Median age is missing', df_eur[df_eur['median_age'].isnull()])
print('HDI is missing', df_eur[df_eur['human_development_index'].isnull()])
print('Total deaths per million is missing',
      df_eur[df_eur['total_deaths_per_million'].isnull()])

# Filling the missing data
df_eur = df_eur.drop(df_eur[df_eur.location == 'Vatican'].index)
df_eur.loc[df_eur.location == 'Andorra', 'median_age'] = 46.2
df_eur.loc[df_eur.location == 'Liechtenstein', 'median_age'] = 41.4
df_eur.loc[df_eur.location == 'Isle of Man', 'median_age'] = 44.6
df_eur.loc[df_eur.location == 'Kosovo', 'median_age'] = 30.5
df_eur.loc[df_eur.location == 'San Marino', 'median_age'] = 45.2
df_eur.loc[df_eur.location == 'Monaco', 'median_age'] = 55.4
df_eur.loc[df_eur.location == 'Monaco', 'human_development_index'] = 0.956
df_eur.loc[df_eur.location == 'Isle of Man', 'human_development_index'] = 0.849
df_eur.loc[df_eur.location == 'Kosovo', 'human_development_index'] = 0.787
df_eur.loc[df_eur.location == 'San Marino', 'human_development_index'] = 0.961
df_eur.loc[df_eur.location == 'Isle of Man',
           'total_deaths_per_million'] = 292.96


# Plotting the data
tot_case_eur = np.array(df_eur.total_cases)
countries = np.array(df_eur.location)

plt.figure(figsize=(16, 10), dpi=100)
sns.set_style('whitegrid')
g = sns.scatterplot(x='human_development_index',
                    y='total_deaths_per_million',
                    data=df_eur, hue='location', size=tot_case_eur,
                    sizes=(20, 2000), legend=False, alpha=0.8)
g.set(xlabel='Human development index', ylabel='Total deaths per million')
plt.title('Death rate vs HDI')

# Normalization for bubbles
min_cases = min(tot_case_eur)
print(min_cases)
max_cases = max(tot_case_eur)
print(max_cases)
a1 = 20+(100000-27)*(2000-20)/(4175757-27)
a2 = 20+(500000-27)*(2000-20)/(4175757-27)
a3 = 20+(2500000-27)*(2000-20)/(4175757-27)

# Legend
sm = plt.scatter([], [], s=a1, marker='o', color='#555555')
med = plt.scatter([], [], s=a2, marker='o', color='#555555')
big = plt.scatter([], [], s=a3, marker='o', color='#555555')
plt.legend((sm, med, big),
           ('100 000', '500 000', '   2 500 000'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8,
           title='Total cases',
           title_fontsize='large',
           labelspacing=2,
           borderpad=2)

# Adding the name of countries and median age to the bubbles
for country in countries:
    x1 = df_eur.loc[df_eur['location'] == country, 'human_development_index']
    y1 = df_eur.loc[df_eur['location'] == country, 'total_deaths_per_million']
    median_age = df_eur.loc[df['location'] == country, 'median_age']
    g.text(x1-0.005, y1, str(country)+' '+str(median_age.values),
           horizontalalignment='left', size='small', color='black')
plt.text(0.74, 50, '[] - median age')
plt.savefig('eur_death_hdi_5.png')
plt.show()
