import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# INITIALIZATION

# Low Memory prevents pandas from inferring column types and avoids DtypeWarnings.
df = pd.read_csv('Employee_Compensation.csv', low_memory=False)

print("\n")
print(df.head())
print(f"Total number of reports: {len(df)}")
print(df.info())

# PRE-PROCESSING

# Drops columns that arent needed, as well as any rows with NaN values.
df = df.drop(columns=["Organization Group Code", "Job Family Code", "Job Code", "Department Code", "Union Code", "Employee Name", "data_as_of", "data_loaded_at"])
df = df.dropna()

# Numerical columns are stored as objects in memory, so we need to change them into float values.
numerical_columns = [
    "Salaries",
    "Overtime",
    "Other Salaries",
    "Total Salary",
    "Total Benefits",
    "Total Compensation",
    "Hours",
]

for col in numerical_columns:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(",", "")
        )

print("\n")
print(df.head())
print(f"Total number of reports: {len(df)}")
print(df.info())

# ANALYSIS

# Here we take the average of all jobs Total Compensation to see the top 10 highest paying jobs.
job_average_skewed = df.groupby('Job')['Total Compensation'].agg(['mean', 'count']).sort_values(by='mean', ascending=False)
print("\n")
print(job_average_skewed.head(10))

job_average = df.groupby('Job')['Total Compensation'].agg(['mean', 'count'])

# We require a minimum count here so the top jobs aren't skewed toward extremely rare ones (like Executive Officers in the previous cell).
job_average = job_average[job_average['count'] > 25]

job_average = job_average.sort_values(by='mean', ascending=False)
print("\n")
print(job_average.head(10))

best_jobs = job_average.head(10) # Grabs the 10 jobs we just determined to be graphed.
best_jobs['mean'].plot(kind='bar')
plt.title('Highest Paying Jobs by Total Compensation')
plt.xlabel('Job')
plt.ylabel('Average Compensation')
plt.xticks(rotation=45, ha='right') # Rotates x axis labels for readability
plt.ylim(390000, 610000) # Changes range of y
plt.show()

# KMeans
features = df.groupby('Job')[['Total Compensation', 'Overtime']].mean()
features = features.dropna()

# The original Overtime column lists the amount of money paid for overtime, and not the hours of overtime worked.
# It's more beneficial to our analysis to see the percentage of total compensation that came from overtime hours.
features['Overtime Ratio'] = (features['Overtime'] / features['Total Compensation'])

features = features[['Total Compensation', 'Overtime Ratio']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

features['Cluster'] = clusters

scatter = plt.scatter(features['Total Compensation'], features['Overtime Ratio'], c=features['Cluster'])

plt.xlabel('Total Compensation')
plt.ylabel('Overtime Ratio')
plt.title('Job Clusters Based on Compensation and Overtime Ratio')
plt.legend(*scatter.legend_elements(), title='Cluster')
plt.show()
print("\n")
print(features.groupby('Cluster').mean(), "\n\n", features['Cluster'].value_counts())

print("\n")
print("Best Jobs Per Cluster\n")
for cluster in sorted(features['Cluster'].unique()):
  print(f"Cluster {cluster}:")
  
  clustered_jobs = features[features['Cluster'] == cluster]

  best_jobs = clustered_jobs.sort_values(by='Total Compensation', ascending=False).head(10)
  print(best_jobs[['Total Compensation', 'Overtime Ratio']])

print("\n")  
print("Worst Jobs Per Cluster\n")
for cluster in sorted(features['Cluster'].unique()):
  print(f"Cluster {cluster}:")
  
  clustered_jobs = features[features['Cluster'] == cluster]

  worst_jobs = clustered_jobs.sort_values(by='Total Compensation', ascending=True).head(10)
  print(worst_jobs[['Total Compensation', 'Overtime Ratio']])

print("\n")  
print("Jobs With The Most Overtime\n")
clustered_jobs = features[features['Cluster'] == cluster]

overtime_jobs = clustered_jobs.sort_values(by='Overtime Ratio', ascending=False).head(10)
print(overtime_jobs[['Total Compensation', 'Overtime Ratio']])