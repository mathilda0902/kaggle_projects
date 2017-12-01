part 0: Section breakdown
1. Understand the problem. We'll look at each variable and do a philosophical analysis about their meaning and importance for this problem.
  - In order to have some discipline in our analysis, we can create an Excel spreadsheet with the following columns:
    - Variable - Variable name.
    - Type - Identification of the variables' type. There are two possible values for this field: 'numerical' or 'categorical'.
    - Segment - Identification of the variables' segment. We can define three possible segments: building, space or location. When we say 'building', we mean a variable that relates to the physical characteristics of the building (e.g. 'OverallQual'). When we say 'space', we mean a variable that reports space properties of the house (e.g. 'TotalBsmtSF'). Finally, when we say a 'location', we mean a variable that gives information about the place where the house is located (e.g. 'Neighborhood').
    - Expectation - Our expectation about the variable influence in 'SalePrice'. We can use a categorical scale with 'High', 'Medium' and 'Low' as possible values.
    - Conclusion - Our conclusions about the importance of the variable, after we give a quick look at the data. We can keep with the same categorical scale as in 'Expectation'.
    - Comments - Any general comments that occured to us.
      - Time spent: ~ 2 hours.

2. Univariable study. We'll just focus on the dependent variable ('SalePrice') and try to know a little bit more about it.
```
count      1460.000000
mean     180921.195890
std       79442.502883
min       34900.000000
25%      129975.000000
50%      163000.000000
75%      214000.000000
max      755000.000000
Name: SalePrice, dtype: float64
```
Skewness: 1.882876 and Kurtosis: 6.536282.

3. Multivariate study. We'll try to understand how the dependent variable and independent variables relate.
We selected 33 features:
```
Utilities
Neighborhood
HouseStyle
OverallCond
HeatingQC
CentralAir
Electrical
KitchenQual
Functional
GarageQual
GarageCond
YearRemodAdd
LotArea
TotalBsmtSF
1stFlrSF
2ndFlrSF
GrLivArea
BsmtFullBath
BsmtHalfBath
FullBath
HalfBath
Bedroom
Kitchen
TotRmsAbvGrd
GarageCars
GarageArea
PoolArea
PoolQC
Fence
MiscFeature
MiscVal
MoSold
YrSold
```


4. Basic cleaning. We'll clean the dataset and handle the missing data, outliers and categorical variables.

5. Test assumptions. We'll check if our data meets the assumptions required by most multivariate techniques.
Four assumptions should be tested:
  1) Normality - When we talk about normality what we mean is that the data should look like a normal distribution. This is important because several statistic tests rely on this (e.g. t-statistics). In this exercise we'll just check univariate normality for 'SalePrice' (which is a limited approach). Remember that univariate normality doesn't ensure multivariate normality (which is what we would like to have), but it helps. Another detail to take into account is that in big samples (>200 observations) normality is not such an issue. However, if we solve normality, we avoid a lot of other problems (e.g. heteroscedacity) so that's the main reason why we are doing this analysis.

  2) Homoscedasticity - I just hope I wrote it right. Homoscedasticity refers to the 'assumption that dependent variable(s) exhibit equal levels of variance across the range of predictor variable(s)' (Hair et al., 2013). Homoscedasticity is desirable because we want the error term to be the same across all values of the independent variables.

  3) Linearity- The most common way to assess linearity is to examine scatter plots and search for linear patterns. If patterns are not linear, it would be worthwhile to explore data transformations. However, we'll not get into this because most of the scatter plots we've seen appear to have linear relationships.

  4) Absence of correlated errors - Correlated errors, like the definition suggests, happen when one error is correlated to another. For instance, if one positive error makes a negative error systematically, it means that there's a relationship between these variables. This occurs often in time series, where some patterns are time related. We'll also not get into this. However, if you detect something, try to add a variable that can explain the effect you're getting. That's the most common solution for correlated errors.
