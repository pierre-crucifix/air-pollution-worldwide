import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

air_pollution_df = pd.read_csv(r".\air_pollution_db.csv", index_col=0)
# df_shuffled=air_pollution_df.sample(frac=1).reset_index(drop=True)#For small scale trials
# air_pollution_df = df_shuffled.head(200)#For small scale trials

# PM2.5 Swarplot (region per region)
plt.figure(figsize=(16,9))
plt.title('Categorical scatterplot of air pollution (PM2.5) by region of the world')
ax = sns.swarmplot(x=air_pollution_df["Region"], y=air_pollution_df["PM2.5 Annual mean, ug/m3"], edgecolor="gray")
ax.set_xticklabels(ax.get_xticklabels(), rotation=12, ha="right")
plt.savefig(r".\Plots\SwarmPlot2.5.png", dpi=1000)
plt.show()

# PM10 Swarplot (region per region)
plt.figure(figsize=(16,9))
plt.title('Categorical scatterplot of air pollution (PM10) by region of the world')
ax = sns.swarmplot(x=air_pollution_df["Region"], y=air_pollution_df["PM10 Annual mean, ug/m3"])
ax.set_xticklabels(ax.get_xticklabels(), rotation=12, ha="right")
plt.savefig(r".\Plots\SwarmPlot10.png", dpi=1000)
plt.show()