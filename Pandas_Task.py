#Import libraries
import pandas as pd
import numpy as np
from scipy.stats import jarque_bera
from scipy.stats import normaltest

# Read the CSV file into a pandas dataframe
df = pd.read_csv('Telecom_customer churn.csv')

#Compute statistics for rev_Mean column
rev_mean_count = df['rev_Mean'].count()
rev_mean_min = df['rev_Mean'].min()
rev_mean_max = df['rev_Mean'].max()
rev_mean_std = df['rev_Mean'].std()
rev_mean_median = df['rev_Mean'].median()
rev_mean_quantile1 = df['rev_Mean'].quantile(0.25)
rev_mean_quantile3 = df['rev_Mean'].quantile(0.75)
rev_mean_IQR = rev_mean_quantile3 - rev_mean_quantile1
rev_mean_skew = df['rev_Mean'].skew()
rev_mean_kurtosis = df['rev_Mean'].kurtosis()
rev_mean_outliers = df[(df['rev_Mean'] < rev_mean_quantile1 - 1.5 * rev_mean_IQR) | (df['rev_Mean'] > rev_mean_quantile3 + 1.5 * rev_mean_IQR)]

#Print for rev_Mean column
print(" Mean monthly revenue (charge amount) Count:\n",rev_mean_count )
print(" Mean monthly revenue (charge amount) Min:\n",rev_mean_min )
print(" Mean monthly revenue (charge amount) Max:\n",rev_mean_max )
print(" Mean monthly revenue (charge amount) Standard Deviation:\n",rev_mean_std )
print(" Mean monthly revenue (charge amount) Median: ", rev_mean_median)
print(" Mean monthly revenue (charge amount) Quartile 1: ", rev_mean_quantile1)
print(" Mean monthly revenue (charge amount) Quartile 3: ", rev_mean_quantile3)
print(" Mean monthly revenue (charge amount) IQR: ", rev_mean_IQR)
print(" Mean monthly revenue (charge amount) Skewness: ", rev_mean_skew)
print(" Mean monthly revenue (charge amount) Kurtosis: ", rev_mean_kurtosis)
print(" Mean monthly revenue (charge amount) - Number of outliers: ", len(rev_mean_outliers))
print('==========================================================')

# Compute statistics for mou_Mean column
mou_mean_count = df['mou_Mean'].count()
mou_mean_min = df['mou_Mean'].min()
mou_mean_max = df['mou_Mean'].max()
mou_mean_std = df['mou_Mean'].std()
mou_mean_median = df['mou_Mean'].median()
mou_mean_quantile1 = df['mou_Mean'].quantile(0.25)
mou_mean_quantile3 = df['mou_Mean'].quantile(0.75)
mou_mean_IQR = mou_mean_quantile3 - mou_mean_quantile1
mou_mean_skew = df['mou_Mean'].skew()
mou_mean_kurtosis = df['mou_Mean'].kurtosis()
mou_mean_outliers = df[(df['mou_Mean'] < mou_mean_quantile1 - 1.5 * mou_mean_IQR) | (df['mou_Mean'] > mou_mean_quantile3 + 1.5 * mou_mean_IQR)]

#Print for mou_mean column
print("Mean number of monthly minutes of use Count:\n",mou_mean_count )
print("Mean number of monthly minutes of use Min:\n",mou_mean_min )
print("Mean number of monthly minutes of use Max:\n",mou_mean_max )
print("Mean number of monthly minutes of use Standard Deviation:\n",mou_mean_std )
print("Mean number of monthly minutes of use Median: ", mou_mean_median)
print("Mean number of monthly minutes of use Quartile 1: ", mou_mean_quantile1)
print("Mean number of monthly minutes of use Quartile 3: ", mou_mean_quantile3)
print("Mean number of monthly minutes of use IQR: ", mou_mean_IQR)
print("Mean number of monthly minutes of use Skewness: ", mou_mean_skew)
print("Mean number of monthly minutes of use Kurtosis: ", mou_mean_kurtosis)
print("Mean number of monthly minutes of use - Number of outliers: ", len(mou_mean_outliers))
print('=================================================================')

#Compute statistics for totmrc_Mean column
totmrc_Mean_count = df['totmrc_Mean'].count()
totmrc_Mean_min = df['totmrc_Mean'].min()
totmrc_Mean_max = df['totmrc_Mean'].max()
totmrc_Mean_std = df['totmrc_Mean'].std()
totmrc_Mean_median = df['totmrc_Mean'].median()
totmrc_Mean_quantile1 = df['totmrc_Mean'].quantile(0.25)
totmrc_Mean_quantile3 = df['totmrc_Mean'].quantile(0.75)
totmrc_Mean_IQR = totmrc_Mean_quantile3 - totmrc_Mean_quantile1
totmrc_Mean_skew = df['totmrc_Mean'].skew()
totmrc_Mean_kurtosis = df['totmrc_Mean'].kurtosis()
totmrc_Mean_outliers = df[(df['totmrc_Mean'] < totmrc_Mean_quantile1 - 1.5 * totmrc_Mean_IQR) | (df['totmrc_Mean'] > totmrc_Mean_quantile3 + 1.5 * totmrc_Mean_IQR)]

#Print for totmrc_Mean column
print("Mean total monthly recurring charge Count:\n",totmrc_Mean_count )
print("Mean total monthly recurring charge Min:\n",totmrc_Mean_min )
print("Mean total monthly recurring charge Max:\n",totmrc_Mean_max )
print("Mean total monthly recurring charge Standard Deviation:\n",totmrc_Mean_std )
print("Mean total monthly recurring charge Median: ", totmrc_Mean_median)
print("Mean total monthly recurring charge Quartile 1: ", totmrc_Mean_quantile1)
print("Mean total monthly recurring charge Quartile 3: ", totmrc_Mean_quantile3)
print("Mean total monthly recurring charge IQR: ", totmrc_Mean_IQR)
print("Mean total monthly recurring charge Skewness: ", totmrc_Mean_skew)
print("Mean total monthly recurring charge Kurtosis: ", totmrc_Mean_kurtosis)
print("Mean total monthly recurring charge - Number of outliers: ", len(totmrc_Mean_outliers))
print('=================================================================')

#Compute statistics for da_Mean column
da_Mean_count = df['da_Mean'].count()
da_Mean_min = df['da_Mean'].min()
da_Mean_max = df['da_Mean'].max()
da_Mean_std = df['da_Mean'].std()
da_Mean_median = df['da_Mean'].median()
da_Mean_quantile1 = df['da_Mean'].quantile(0.25)
da_Mean_quantile3 = df['da_Mean'].quantile(0.75)
da_Mean_IQR = da_Mean_quantile3 - da_Mean_quantile1
da_Mean_skew = df['da_Mean'].skew()
da_Mean_kurtosis = df['da_Mean'].kurtosis()
da_Mean_outliers = df[(df['da_Mean'] < da_Mean_quantile1 - 1.5 * da_Mean_IQR) | (df['da_Mean'] > da_Mean_quantile3 + 1.5 * da_Mean_IQR)]

#Print for da_Mean column
print("Mean number of directory assisted calls Count:\n",totmrc_Mean_count )
print("Mean number of directory assisted calls Min:\n",totmrc_Mean_min )
print("Mean number of directory assisted calls Max:\n",totmrc_Mean_max )
print("Mean number of directory assisted calls Standard Deviation:\n",totmrc_Mean_std )
print("Mean number of directory assisted calls Median: ", totmrc_Mean_median)
print("Mean number of directory assisted calls Quartile 1: ", totmrc_Mean_quantile1)
print("Mean number of directory assisted calls Quartile 3: ", totmrc_Mean_quantile3)
print("Mean number of directory assisted calls IQR: ", totmrc_Mean_IQR)
print("Mean number of directory assisted calls Skewness: ", totmrc_Mean_skew)
print("Mean number of directory assisted calls  Kurtosis: ", totmrc_Mean_kurtosis)
print("Mean number of directory assisted calls- Number of outliers: ", len(totmrc_Mean_outliers))
print('=================================================================') 


# Calculate correlation matrix
corr_matrix = df[['rev_Mean', 'mou_Mean','totmrc_Mean','da_Mean']].corr()

#Print for Correlation
print('\nCorrelation Matrix:')
print(corr_matrix)


# Extract the columns of interest
rev_mean = df['rev_Mean']
mou_mean = df['mou_Mean']

# Perform the Jarque-Bera test for normality
jb_rev_mean = jarque_bera(rev_mean)
jb_mou_mean = jarque_bera(mou_mean)

# Print the results
print("Jarque-Bera test for rev_Mean:", jb_rev_mean)
print("Jarque-Bera test for mou_Mean:", jb_mou_mean)
