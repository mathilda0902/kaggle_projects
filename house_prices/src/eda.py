'''part 0: section breakdown
1. Understand the problem. We'll look at each variable and do a philosophical
analysis about their meaning and importance for this problem.'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as scs

train_df = pd.read_csv('data/train.csv')

'''2. Univariable study. We'll just focus on the dependent variable
('SalePrice') and try to know a little bit more about it.'''
train_df.SalePrice.describe()
sp = train_df.SalePrice
'''Out[11]:
count      1460.000000
mean     180921.195890
std       79442.502883
min       34900.000000
25%      129975.000000
50%      163000.000000
75%      214000.000000
max      755000.000000
Name: SalePrice, dtype: float64'''

sns.distplot(sp,bins=20, hist=True, kde=True, norm_hist=True)
plt.show()

print 'Skewness: %f' % (sp.skew())
print 'Kurtosis: %f' % (sp.kurt())
'''Skewness: 1.882876
Kurtosis: 6.536282'''

'''3. Multivariate study. We'll try to understand how the dependent variable
and independent variables relate.'''

'''4. Basic cleaning. We'll clean the dataset and handle the missing data,
outliers and categorical variables.'''

'''5. Test assumptions. We'll check if our data meets the assumptions
required by most multivariate techniques.'''
'''Four assumptions should be tested:
1) Normality - When we talk about normality what we mean is that the data
should look like a normal distribution. '''

'''2) Homoscedasticity - refers to
the 'assumption that dependent variable(s) exhibit equal levels of variance
across the range of predictor variable(s)' '''

'''3) Linearity- The most common way to assess linearity is to examine scatter plots
and search for linear patterns. '''

'''4) Absence of correlated errors'''
