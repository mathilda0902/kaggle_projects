'''part 0: section breakdown
1. Understand the problem. We'll look at each variable and do a philosophical
analysis about their meaning and importance for this problem.'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as scs

df_train = pd.read_csv('data/train.csv')

'''2. Univariable study. We'll just focus on the dependent variable
('SalePrice') and try to know a little bit more about it.'''
df_train.SalePrice.describe()
sp = df_train.SalePrice
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
'''Relationship of 'SalePrice' with numerical features'''
    num_features = ['LotArea', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea',
                    'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
                    'BedroomAbvGr',  'KitchenAbvGr', 'TotRmsAbvGrd', 'GarageCars',
                    'GarageArea', 'PoolArea']

'''plat scatters with respect to each of numerical features:'''

x_num = df_train[num_features]
for feature in num_features:
    plt.scatter(x_num[feature],sp)
    plt.xlabel('%s' % feature)
    plt.ylabel('Sale Price')
    plt.savefig('scatter_%s_saleprice' % feature)
    plt.show()


'''Relationship of 'SalePrice' with categorical features'''
    cat_features = ['Utilities', 'HouseStyle', 'OverallCond',
                    'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual',
                    'Functional', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence',
                    'MiscFeature', 'MiscVal', 'OverallQual']

'''plat scatters with respect to each of numerical features:'''
x_cat = df_train[cat_features]
for feature in cat_features:
    sns.boxplot(x_cat[feature], sp)
    plt.savefig('%s' % feature)
    plt.show()

fig = sns.boxplot(df_train['Neighborhood'], sp)
fig.set_xticklabels(fig.get_xticklabels(), rotation=30)
plt.savefig('Neighborhood')
plt.show()

'''datetime type features:'''
    date_features = ['MoSold', 'YrSold']

'''In [63]: df_train[date_features].describe()
Out[63]:
       YearRemodAdd       MoSold       YrSold
count   1460.000000  1460.000000  1460.000000
mean    1984.865753     6.321918  2007.815753
std       20.645407     2.703626     1.328095
min     1950.000000     1.000000  2006.000000
25%     1967.000000     5.000000  2007.000000
50%     1994.000000     6.000000  2008.000000
75%     2004.000000     8.000000  2009.000000
max     2010.000000    12.000000  2010.000000'''

x_date = df_train[date_features]
for feature in date_features:
    sns.boxplot(x_date[feature], sp)
    plt.savefig('%s' % feature)
    plt.show()

fig = sns.boxplot(df_train['YearRemodAdd'], sp)
fig.set_xticklabels(fig.get_xticklabels(), rotation=90)
plt.savefig('YearRemodAdd')
plt.show()


'''4. Basic cleaning. We'll clean the dataset and handle the missing data,
outliers and categorical variables. How prevalent is the missing data? Is
missing data random or does it have a pattern?'''

'''Detect missing values from all data:'''
missing_total = df_train.isnull().sum().sort_values(ascending=False)
missing_total[missing_total!=0]
 
missing_perc = (df_train.isnull().sum()/ df_train.isnull().count()).sort_values(ascending=False)
missing_perc[missing_perc != 0]

missing_data = pd.concat([missing_total, missing_perc], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)

'''              Total   Percent
PoolQC         1453  0.995205
MiscFeature    1406  0.963014
Alley          1369  0.937671
Fence          1179  0.807534
FireplaceQu     690  0.472603
LotFrontage     259  0.177397
GarageCond       81  0.055479
GarageType       81  0.055479
GarageYrBlt      81  0.055479
GarageFinish     81  0.055479
GarageQual       81  0.055479
BsmtExposure     38  0.026027
BsmtFinType2     38  0.026027
BsmtFinType1     37  0.025342
BsmtCond         37  0.025342
BsmtQual         37  0.025342
MasVnrArea        8  0.005479
MasVnrType        8  0.005479
Electrical        1  0.000685
Utilities         0  0.000000'''



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
