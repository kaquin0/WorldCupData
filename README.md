# WorldCupData
Using data to figure out trends in the World Cup from the past 80+ years

Grabbing data from Kaggle, used Panda, Seaborn and Maplotlib to create a series of plots, discover aggregates and distribution across the goals scored in World Cup games from 1930 to 2014. I want to show the average number of goals for each World Cup so we can see some sort of upwards or downwards trend of goals scored.  And as mentioned earlier to go along with the average goals is the distribution of goals for each World Cup

After importing the data using Panda, I went ahead and calculated the 'Total Goals Scored' for every World Cup game from 1930 to 2014:

f["Total Goals"]= df['Home Team Goals'] + df['Away Team Goals']

Then using Seaborn, I started to plot the bar chart giving a visualization of how many goals were scored in all those World Cups to it will be easier to read:

ns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.25)

With Maplotlib, I went ahead to set the size of the subplots for the bar chart:

f, ax = plt.subplots(figsize=(12, 7))

Back to Seaborn, I grabbed the data to visualize the "Total Goals Scored" on the y-axis and along the x-axis I plotted the "Year":

ax = sns.barplot(x=df["Year"], y=df["Total Goals"])
ax.set_title("Average Goals Scored in World Cup Matches By Year")
plt.show()

Lastly after showing the average number of goals of each World Cup, I also wanted to show the distrubution of goals scored for each World Cup, so using Seaborn and Maplotlib again, I formulated the following to visualize how the goals were distributed:

f, ax2 = plt.subplots(figsize=(12, 7))
ax2 = sns.boxplot(x= 'year', y= 'goals', data=df_goals, palette='Spectral')
ax2.set_title('Distribution of Goals')
plt.show()

