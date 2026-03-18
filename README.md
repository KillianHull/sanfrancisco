# San Francisco

Data Mining course project based on the data sets from https://data.sfgov.org/

## Dataset

The dataset is too large to upload to GitHub itself, you can download it from the link below.

- [Employee Compensation: Database of salary and benefits paid to City employees since fiscal year 2013](https://data.sfgov.org/City-Management-and-Ethics/Employee-Compensation/88g8-5mnd/about_data)

If you're running the code locally, save the CSV to the same directory as main.py. If you're running the code in Colab, simply upload it to the notebooks files.

**Note: I ran into many EOF issues when using the default CSV filetype, but using the CSV for Excel filetype worked flawlessly. If you have any issues, try that.**

## Introduction

This project aims to analyze employee salary and compensation data from San Francisco to identify the highest paying jobs and understand how compensation and benefits differ among careers. The goal is to provide insight to individuals, such as new residents or those seeking a job, about what the best jobs in their area are.

## Disclaimer

This project was implemented and tested in Google Colab. While the code should run locally, Google Colab includes many pre-installed Python libraries that you may need to install first:
```bash
pip install pandas matplotlib scikit-learn
```

## Data Mining Techniques Used

### 1. Preprocessing

- Removed unnecessary columns that weren't relevant to the analysis
- Filtering out rows with any missing values
- Standardizing numerical object-type columns into float columns

### 2. Standard Analysis

- Found the average total compensation of each job
- Counted the number of records per job to detect and filter out anomalies and outliers

### 3. Clustering

- Applied K-means clustering to group jobs based on compensation
- Created an Overtime Ratio feature from the data to distinguish jobs that have high salaries vs jobs that require high overtime hours

### 4. Visualization

- Bar Charts for the highest paying job categories
- Scatter plots to visualize clusters and view patterns

**Further explanations can be found in the ipynb notebook.**

## Conclusions

The analysis showcased several insights into the job market of San Francisco:

- Executive jobs and specialized roles consistently have the highest total compensation, making a minimum of $231000 in the dataset.
- Many jobs follow a pattern where benefits increase proportionally with salary.
- Clustering analysis revealed three distinct categories of jobs:
	- Salary-based jobs with average compensation and low overtime are the most common (Avg: $129000, Overtime: ~1.3%, Job Market: ~75.4%)
	- High compensation jobs, such as executives, make the most with minimal overtime and are the most rare (Avg: $334000, Overtime: ~0.6%, Job Market: ~9.3%)
	- Salary-based jobs with slightly above-average compensation with high overtime (Avg: $188000, Overtime: ~13.8%, Job Market: ~15.2%)

The results also show that compensation isn't purely reliant on salary, and some jobs with an average base pay make more due to a heavy reliance on overtime, such as Law Enforcement.

## Limitations

This analysis is based solely on jobs provided by the city itself, and doesn't reflect trends of other types of businesses that may be more common, such as food service.
