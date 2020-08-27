import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#importing data from the csv file
df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')

#Adding up the total goals from each World Cup
df["Total Goals"]= df['Home Team Goals'] + df['Away Team Goals']

#Plotting the goals onto a bar chart
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.25)
f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(x=df["Year"], y=df["Total Goals"])
ax.set_title("Average Goals Scored in World Cup Matches By Year")
plt.show()

#Plotting the distribution of goals
f, ax2 = plt.subplots(figsize=(12, 7))
ax2 = sns.boxplot(x= 'year', y= 'goals', data=df_goals, palette='Spectral')
ax2.set_title('Distribution of Goals')
plt.show()

print(df_goals.head())
print(df.head())
