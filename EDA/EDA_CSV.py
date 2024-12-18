# Exploratory Data Analysis (EDA) is a crucial part of the data analysis pipeline. 
# It helps us understand the underlying structure, trends, and relationships in the data. 
# Here is a comprehensive list of 100 different ways to perform EDA on numerical and categorical data, 
# categorized for both discrete and continuous features.

# ### **EDA on Numerical Data**

# #### **For Continuous Features:**

# 1. **Summary Statistics**: Calculate mean, median, mode, min, max, standard deviation, and quantiles.
# 2. **Range**: Check the range (max - min) of the continuous variables.
# 3. **Distribution Shape**: Plot the histogram to visualize the shape of the distribution.
# 4. **Density Plot**: Use a kernel density estimate (KDE) plot to visualize the probability density function.
# 5. **Boxplot**: Visualize the spread and detect outliers using a boxplot.
# 6. **Violin Plot**: Combine boxplots and KDE plots to show data distribution and its probability.
# 7. **Skewness**: Calculate skewness to measure the asymmetry of the distribution.
# 8. **Kurtosis**: Calculate kurtosis to identify the tailedness of the distribution.
# 9. **Correlation Matrix**: Calculate the correlation coefficient (Pearson, Spearman, or Kendall) between continuous variables.
# 10. **Pair Plot**: Visualize pairwise relationships in the data to detect correlations.
# 11. **Scatter Plot**: Visualize two continuous variables to check for relationships.
# 12. **Heatmap**: Use a heatmap to visualize correlation or covariance between numerical features.
# 13. **Normality Test**: Apply statistical tests like the Shapiro-Wilk test to check for normality.
# 14. **Outlier Detection (IQR)**: Identify outliers by computing values outside the interquartile range (IQR).
# 15. **Outlier Detection (Z-Score)**: Identify outliers by calculating z-scores (values beyond 3 are considered outliers).
# 16. **Transformation**: Apply log, square root, or cube root transformations to reduce skewness.
# 17. **Rescaling**: Scale numerical features using normalization or standardization (min-max or Z-score).
# 18. **Rolling Mean**: Calculate the rolling mean for time-series data.
# 19. **Autocorrelation**: Plot autocorrelation to detect patterns in time-series data.
# 20. **Binned Histograms**: Divide continuous features into discrete bins and observe distribution.
# 21. **Time Series Decomposition**: Decompose the time-series into trend, seasonality, and residual components.
# 22. **Scatter Matrix**: Visualize multi-dimensional relationships between features using a scatter matrix.
# 23. **Cumulative Distribution Function (CDF)**: Plot the CDF to observe the percentage of data below a certain threshold.
# 24. **Outlier Detection (Modified Z-Score)**: Use median absolute deviation (MAD) to detect outliers.
# 25. **Trend Lines**: Fit a linear or polynomial trend line to the scatter plot.
# 26. **Cross-correlation**: Study the relationship between two time-series by calculating the cross-correlation function.
# 27. **Logistic Transformation**: Apply a logistic function to compress data for better visualization or normality.
# 28. **Principal Component Analysis (PCA)**: Reduce dimensionality to explore the variance of the data.
# 29. **Manhattan Distance**: Compute distances between points in multi-dimensional continuous data.
# 30. **Silhouette Score**: Evaluate the consistency of clusters within continuous variables.
# 31. **Fourier Transform**: Decompose data into sine and cosine functions for periodic signals (time-series).
# 32. **Variance Inflation Factor (VIF)**: Measure multicollinearity between continuous variables.
# 33. **Cumulative Sum (CUSUM)**: Use for detecting shifts in the mean of time-series data.
# 34. **Linear Regression**: Use linear regression to model the relationship between variables.
# 35. **Quartile Analysis**: Explore data via quartiles and percentiles.
# 36. **Heatmap of Rolling Statistics**: Plot a heatmap showing the rolling statistics of a continuous variable.
# 37. **Trend Analysis**: Decompose data into trend components to study its evolution over time.
# 38. **Lag Plots**: Check for autocorrelation by plotting lagged versions of time-series data.
# 39. **Quantile-Quantile Plot (Q-Q Plot)**: Compare the data distribution to a theoretical distribution.

# #### **For Discrete Features:**

# 40. **Frequency Table**: Calculate the frequency distribution of discrete numerical data.
# 41. **Bar Plot**: Visualize the counts or proportions of discrete data.
# 42. **Pie Chart**: Show the percentage distribution of categories in discrete data.
# 43. **Mode**: Find the most common value(s) in a discrete variable.
# 44. **Chi-Square Test**: Test the independence of categorical variables.
# 45. **Proportions**: Calculate and plot proportions for each category in a discrete feature.
# 46. **Contingency Table**: Create a contingency table to explore the relationship between discrete variables.
# 47. **Cross-tabulation**: Generate a cross-tabulation table for two or more categorical variables.
# 48. **Stacked Bar Plot**: Display multiple categorical features stacked within the same bar.
# 49. **Dot Plot**: Represent the frequency of discrete events or values.
# 50. **Crosstab with Aggregation**: Aggregate discrete variables using functions like sum, mean, count, etc.
# 51. **Cross-feature Relationship**: Investigate how a discrete feature influences other features in the dataset.
# 52. **Benford's Law**: Check if the distribution of digits in a dataset follows Benford's Law.
# 53. **Fisher's Exact Test**: Perform Fisher's exact test to determine if two categorical variables are independent.
# 54. **Spearman's Rank Correlation**: Measure the correlation between two discrete variables.
# 55. **Shannon Entropy**: Calculate the entropy of a discrete feature to measure its uncertainty.
# 56. **Cohen's Kappa**: Evaluate inter-rater reliability for discrete features.
# 57. **Cluster Analysis**: Perform clustering to identify patterns in discrete data.
# 58. **Association Rule Mining**: Discover relationships between discrete items using algorithms like Apriori.
# 59. **Mode Comparison**: Compare the mode across different groups or categories.
# 60. **Survival Analysis**: Investigate the duration and time until an event occurs in discrete features (like failures).
# 61. **Cumulative Frequency Plot**: Show cumulative frequencies of different discrete categories.
# 62. **Odds Ratio**: Calculate the odds ratio to assess the strength of association between two discrete features.
# 63. **Conditional Probability**: Estimate the probability of one event occurring given another.
# 64. **Log-Linear Model**: Fit a log-linear model to examine relationships between categorical variables.
# 65. **Multinomial Logistic Regression**: Model multi-category discrete features.
# 66. **Random Forest Feature Importance**: Assess feature importance in predicting discrete outcomes.
# 67. **Factorization**: Use factor analysis to uncover latent variables in categorical data.
# 68. **Multiple Correspondence Analysis (MCA)**: Visualize and analyze relationships between multiple categorical variables.
# 69. **Non-parametric Tests**: Apply tests like the Kruskal-Wallis test for discrete data comparisons.
# 70. **Cluster Heatmap**: Use heatmaps to cluster similar discrete values.
# 71. **Outlier Detection**: Use interquartile range (IQR) or z-score methods to detect outliers in discrete data.
# 72. **Gini Index**: Calculate the Gini index to measure the inequality of categorical feature distributions.
# 73. **Permutation Test**: Perform permutation tests to assess the significance of a categorical variable.

# ---

# ### **EDA on Categorical Data**

# #### **For Nominal Features:**

# 74. **Frequency Distribution**: Display how often each category appears.
# 75. **Bar Plot**: Plot bar charts to visualize the frequency of different categories.
# 76. **Pie Chart**: Show proportions of different categories in the data.
# 77. **Stacked Bar Plot**: Show distribution of categories across multiple groups.
# 78. **Cross-tabulation**: Show the interaction between two or more categorical variables.
# 79. **Chi-Square Test**: Test the relationship between two nominal features.
# 80. **Stacked Area Plot**: Visualize the composition of categories over time or by groups.
# 81. **Heatmap**: Create a heatmap for categorical features to visualize relationships.
# 82. **Association Rule Mining**: Explore association rules between categories using Apriori or FP-growth.
# 83. **Mosaic Plot**: Visualize the relationship between two or more categorical variables.
# 84. **Clustered Bar Plot**: Visualize categorical data grouped by different categories.
# 85. **Venn Diagram**: Use a Venn diagram to explore the relationship between categories.
# 86. **Cross-tab with Aggregation**: Aggregate numerical features based on categorical groups.
# 87. **Anova Test**: Test differences between categorical groups based on numerical data.
# 88. **Stratified Sampling**: Use stratified sampling to ensure the representation of categories in the dataset.
# 89. **Groupby Operations**: Group data by category and aggregate the numeric columns accordingly.
# 90. **Cohen's Kappa**: Measure the agreement between categorical variables (raters).
# 91. **Kruskal-Wallis Test**: Use for comparing more than two categorical groups.
# 92. **Permutation Test**: Use to determine the significance of categorical data.
# 93. **Multiple Correspondence Analysis (MCA)**: Use to visualize relationships in multi-categorical data.
# 94. **Gini Index**: Measure the purity of categorical distributions.
# 95. **Jaccard Similarity**: Compute the Jaccard index to quantify similarities between sets of categorical variables.
# 96. **Log-linear Modeling**: Use to model the relationships between multiple nominal variables.
# 97. **Random Forest Feature Importance**: Use random forest to identify important categorical features for prediction.
# 98. **Null Hypothesis Testing**: Test the distribution of categorical variables using tests like Fisher’s Exact Test.
# 99. **PCA on Categorical Data**: Use dimensionality reduction techniques for high cardinality categorical variables (like one-hot encoding).
# 100. **LDA (Linear Discriminant Analysis)**: Classify and visualize categorical variables by maximizing class separability.

# ---

# These methods can help reveal key insights from both numerical and categorical data, whether discrete or continuous. They are useful for identifying trends, outliers, relationships, and hidden patterns in datasets.

