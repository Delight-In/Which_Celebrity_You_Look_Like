# Probability and Statistics

## Overview

This document outlines various concepts and formulas used in **Probability and Statistics**. It covers a wide range of topics, from basic counting principles (permutations and combinations) to advanced statistical tests like the **Chi-squared test**. Each section provides a detailed explanation of the topic, assumptions, when to use specific methods, and why they are important for statistical analysis.

---

## Contents

1. **Counting (Permutations and Combinations)**
2. **Probability Axioms**
3. **Sample Space, Events, and Types of Events**
4. **Marginal, Conditional, and Joint Probability**
5. **Bayes' Theorem**
6. **Conditional Expectation and Variance**
7. **Central Tendency Measures**
8. **Correlation and Covariance**
9. **Random Variables and Probability Distributions**
10. **Key Probability Distributions (Discrete and Continuous)**
11. **Cumulative Distribution Function (CDF)**
12. **Central Limit Theorem**
13. **Statistical Tests (z-test, t-test, Chi-squared Test)**
14. **Confidence Intervals**

---

## 1. Counting (Permutations and Combinations)

### **Permutations**  
A **permutation** is an arrangement of objects in a specific order. The formula for permutations of \(n\) objects taken \(r\) at a time is:

$$
P(n, r) = \frac{n!}{(n - r)!}
$$

- **Assumption**: Order matters.
- **Why Needed**: Useful when the arrangement of elements matters (e.g., ranking or seating arrangements).
- **When to Use**: Used in cases where you need to find the number of ways to arrange \(r\) items from \(n\) distinct items.

### **Combinations**  
A **combination** is a selection of items where the order does not matter. The formula for combinations is:

$$
C(n, r) = \frac{n!}{r!(n - r)!}
$$

- **Assumption**: Order does not matter.
- **Why Needed**: Used when selecting items without regard to order (e.g., selecting a team from a group of players).
- **When to Use**: Use when you're interested in choosing subsets of items where order doesn't matter.

---

## 2. Probability Axioms

The foundation of probability theory is based on three fundamental axioms:

1. **Non-negativity**: \( P(A) \geq 0 \) for any event \(A\).
2. **Normalization**: \( P(S) = 1 \), where \(S\) is the sample space (the set of all possible outcomes).
3. **Additivity**: If \( A \) and \( B \) are mutually exclusive events, then \( P(A \cup B) = P(A) + P(B) \).

---

## 3. Sample Space, Events, and Types of Events

### **Sample Space (S)**  
The **sample space** is the set of all possible outcomes of an experiment.

### **Events**  
An **event** is a subset of the sample space, and it represents one or more outcomes.

### **Types of Events**
- **Independent Events**: Two events \(A\) and \(B\) are independent if \( P(A \cap B) = P(A)P(B) \).
- **Mutually Exclusive Events**: Two events are mutually exclusive if they cannot occur simultaneously, i.e., \( P(A \cap B) = 0 \).

---

## 4. Marginal, Conditional, and Joint Probability

- **Marginal Probability**: The probability of a single event occurring, regardless of other variables. For two events \(A\) and \(B\), the marginal probability of \(A\) is:

$$
P(A) = \sum_{B} P(A \cap B)
$$

- **Conditional Probability**: The probability of event \(A\) given that event \(B\) has occurred:

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

- **Joint Probability**: The probability of two events happening together:

$$
P(A \cap B) = P(A|B)P(B)
$$

---

## 5. Bayes' Theorem

Bayes' Theorem allows us to compute conditional probabilities in the reverse direction, using prior knowledge:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

- **Assumption**: The events \(A\) and \(B\) must be known, and \(P(B) > 0\).
- **Why Needed**: It is used when you want to update probabilities based on new information.

---

## 6. Conditional Expectation and Variance

### **Conditional Expectation**  
The expected value of a random variable \(X\) given that another event \(B\) has occurred:

$$
E[X|B] = \sum_{x} x P(X=x | B)
$$

### **Conditional Variance**  
The variance of \(X\) given that event \(B\) has occurred:

$$
Var(X|B) = E[X^2|B] - (E[X|B])^2
$$

---

## 7. Central Tendency Measures

- **Mean**: The average value, \( \mu = \frac{1}{n} \sum_{i=1}^n x_i \).
- **Median**: The middle value in a sorted data set.
- **Mode**: The most frequently occurring value.
- **Standard Deviation**: Measures the spread of data points from the mean, \( \sigma = \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i - \mu)^2} \).

---

## 8. Correlation and Covariance

- **Covariance**: Measures how two variables change together:

$$
Cov(X, Y) = \frac{1}{n} \sum_{i=1}^n (X_i - \mu_X)(Y_i - \mu_Y)
$$

- **Correlation**: A normalized version of covariance, which quantifies the linear relationship between two variables:

$$
\rho(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}
$$

---

## 9. Random Variables and Probability Distributions

### **Random Variables**
- **Discrete Random Variable**: A variable that can take on a countable number of values.
- **Continuous Random Variable**: A variable that can take on an infinite number of values within a given range.

### **Probability Mass Function (PMF)**: For discrete random variables, the PMF gives the probability that a discrete random variable is exactly equal to some value.

### **Probability Density Function (PDF)**: For continuous random variables, the PDF describes the likelihood of the variable taking a specific value within a given interval.

---

## 10. Key Probability Distributions

### **Discrete Distributions**
- **Uniform Distribution**: Each outcome is equally likely.
- **Bernoulli Distribution**: Models binary outcomes (success/failure).
- **Binomial Distribution**: The distribution of the number of successes in a fixed number of independent trials.

### **Continuous Distributions**
- **Uniform Distribution**: A constant probability over a given range.
- **Exponential Distribution**: Models the time between events in a Poisson process.
- **Poisson Distribution**: Models the number of events occurring in a fixed interval of time or space.
- **Normal Distribution**: A symmetric distribution characterized by its mean and standard deviation.
- **t-Distribution**: Used for small sample sizes, with thicker tails than the normal distribution.
- **Chi-squared Distribution**: Used in hypothesis testing and goodness-of-fit tests.

---

## 11. Cumulative Distribution Function (CDF)

The **CDF** of a random variable \(X\) is the probability that \(X\) will take a value less than or equal to \(x\):

$$
F_X(x) = P(X \leq x)
$$

---

## 12. Central Limit Theorem

The **Central Limit Theorem (CLT)** states that the sampling distribution of the sample mean will approach a normal distribution as the sample size increases, regardless of the shape of the population distribution.

---

## 13. Statistical Tests

- **Z-Test**: Used to test the mean of a population when the population variance is known.
- **t-Test**: Used to test the mean of a population when the population variance is unknown, typically for small sample sizes.
- **Chi-Squared Test**: Used for hypothesis testing in categorical data analysis, including tests for goodness of fit and independence.

---

## 14. Confidence Intervals

A **confidence interval** gives a range of values for a population parameter (e.g., population mean) with a certain level of confidence. The general formula for a confidence interval for the mean is:

$$
\left( \bar{x} - Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}, \bar{x} + Z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right)
$$

Where:
- \( \bar{x} \) is the sample mean,
- \( Z_{\alpha/2} \) is the critical value for the desired confidence level,
- \( \sigma \) is the population standard deviation,
- \( n \) is the sample size.

---

## Conclusion

This document provides a high-level overview of key concepts in **Probability and Statistics**. Understanding these concepts and formulas is essential for performing rigorous statistical analysis in various fields such

 as data science, economics, and engineering.


 Here are some lesser-known or often overlooked **facts** about **statistics** that can deepen your understanding of the subject:

### 1. **Statistics is About Understanding Uncertainty, Not Certainty**
   - **Fact**: Statistics doesn't provide definitive answers, but rather estimates and probabilities. It’s about quantifying uncertainty and making inferences based on data.
   - **Why It’s Overlooked**: People often expect statistics to offer certainty, but in reality, statistical methods deal with trends, patterns, and probabilities that come with inherent uncertainty.

### 2. **Correlation Does Not Imply Causation**
   - **Fact**: Just because two variables are correlated (i.e., move together) doesn’t mean one causes the other. A third factor could be driving both, or the correlation could simply be coincidental.
   - **Why It’s Overlooked**: People often jump to conclusions when they see correlated data, believing that one factor must be influencing the other, without considering alternative explanations.

### 3. **Small Sample Sizes Lead to Big Errors**
   - **Fact**: When you work with small sample sizes, the results you get are much more likely to be influenced by random variation, which can lead to misleading conclusions.
   - **Why It’s Overlooked**: Small samples are sometimes easier to obtain or more convenient, but they can drastically increase the margin of error and distort your understanding of the population.

### 4. **Outliers Can Drastically Impact Statistical Results**
   - **Fact**: Outliers (data points that are significantly different from the rest of the data) can have a disproportionate impact on the mean and standard deviation, potentially skewing results.
   - **Why It’s Overlooked**: In many cases, outliers are ignored or "cleaned" from datasets, but they can also represent important data points that deserve closer examination.

### 5. **The "Law of Large Numbers" Is Not Just About Size**
   - **Fact**: While the Law of Large Numbers states that the sample mean will converge to the population mean as the sample size increases, this convergence happens in the *long term* and may not be immediately obvious with smaller datasets.
   - **Why It’s Overlooked**: Many people expect large datasets to immediately eliminate variability, but it actually takes large enough samples and time for the "true" population mean to emerge.

### 6. **The Median is More Resistant to Skewness Than the Mean**
   - **Fact**: The **median** (the middle value in a dataset) is less sensitive to extreme values (outliers) compared to the **mean**. This makes the median a better measure of central tendency in skewed distributions.
   - **Why It’s Overlooked**: Many people rely on the mean without considering the effects of skewed data or outliers, leading to misleading interpretations.

### 7. **The Central Limit Theorem is One of the Most Powerful Results in Statistics**
   - **Fact**: The **Central Limit Theorem (CLT)** states that, regardless of the shape of the population distribution, the sampling distribution of the sample mean will be approximately normal for a sufficiently large sample size.
   - **Why It’s Overlooked**: While the CLT is fundamental, its full implications are often ignored. It explains why the normal distribution is so prevalent in statistical analysis and hypothesis testing, even for non-normal data.

### 8. **P-Values Are Not the Only Metric for Statistical Significance**
   - **Fact**: A **p-value** measures the strength of evidence against the null hypothesis, but it is not the sole criterion for assessing significance. Confidence intervals, effect sizes, and power analysis should also be considered.
   - **Why It’s Overlooked**: The p-value is often misunderstood or overemphasized, leading to the "p-hacking" phenomenon, where researchers manipulate data or analyses to achieve a statistically significant result.

### 9. **Randomness and Probability Are Often Misunderstood**
   - **Fact**: People often misinterpret random processes, such as the "Gambler’s Fallacy" (believing that past events affect future random outcomes) or underestimating the role of randomness in everyday life.
   - **Why It’s Overlooked**: Many believe that random events can "balance out" in the short term, but randomness doesn’t work this way. Past events don’t influence future random events.

### 10. **Confidence Intervals Are More Informative Than p-Values**
   - **Fact**: A **confidence interval** gives a range of values that likely contain the true population parameter, offering more context than a simple p-value. It reflects both the effect size and the variability of the estimate.
   - **Why It’s Overlooked**: People often focus on p-values for hypothesis testing, overlooking the fact that confidence intervals can provide more nuanced information about the precision of an estimate.

### 11. **Statistical Power Depends on Effect Size, Sample Size, and Significance Level**
   - **Fact**: **Statistical power** is the probability of detecting a true effect if it exists, and it depends on several factors, including the effect size (how big the difference is), sample size, and the chosen significance level (alpha).
   - **Why It’s Overlooked**: Power analysis is often ignored when designing experiments, leading to studies that are too small to detect real effects (Type II errors).

### 12. **Bayesian Statistics is More Flexible Than Frequentist Statistics**
   - **Fact**: **Bayesian statistics** treats probabilities as subjective beliefs and allows for the updating of these beliefs as new evidence is collected. It provides more flexibility than frequentist methods, especially when data is sparse.
   - **Why It’s Overlooked**: Bayesian methods are less intuitive and mathematically more complex than frequentist approaches, so they are often overlooked in favor of simpler, more widely taught methods.

### 13. **Simulations Can Be a Powerful Tool in Statistics**
   - **Fact**: **Monte Carlo simulations** and other computational methods can be used to approximate statistical results and test hypotheses when analytical methods are difficult or impossible.
   - **Why It’s Overlooked**: Many people underestimate the power of simulations in solving complex statistical problems and rely too heavily on analytical solutions.

### 14. **Statistics Can Reveal Patterns, But Not Always Causality**
   - **Fact**: Statistical methods can help identify correlations or patterns in data, but they do not prove that one event causes another. Additional methods like experimental design or causal inference are needed to establish causality.
   - **Why It’s Overlooked**: Statistics can identify relationships between variables, but without appropriate methods, conclusions about causality can be misleading.

### 15. **Data Can Be Misleading Even with Proper Analysis**
   - **Fact**: Statistics can be manipulated or misinterpreted in ways that give misleading results, such as through selective reporting, biased sampling, or cherry-picking data points. **Ethical statistical practice** is crucial.
   - **Why It’s Overlooked**: People may focus solely on the numbers, ignoring how the data was collected, analyzed, or presented, which can lead to false conclusions.

### 16. **Large Datasets Do Not Guarantee Accuracy**
   - **Fact**: Having a large dataset doesn’t automatically mean your results are more accurate or meaningful. It’s crucial to ensure that the data is of high quality and appropriately representative of the population.
   - **Why It’s Overlooked**: Large datasets are often perceived as more reliable, but their size doesn’t necessarily guarantee that they are free from biases or errors.

### 17. **Sampling Methods Are Critical for Representing the Population**
   - **Fact**: **Random sampling** is essential to ensure that the sample is representative of the population. Poor sampling methods can lead to biased results and inaccurate conclusions.
   - **Why It’s Overlooked**: People sometimes assume that a large sample automatically leads to accurate results, ignoring potential biases introduced during sampling.

### 18. **Multicollinearity Can Distort Regression Results**
   - **Fact**: In multiple regression analysis, if independent variables are highly correlated with each other (multicollinearity), it can inflate standard errors and make the model's coefficients unreliable.
   - **Why It’s Overlooked**: Multicollinearity is often not checked rigorously in simple regression models, leading to inaccurate interpretations of relationships between variables.

### 19. **Ethics Are Vital in Data Collection and Analysis**
   - **Fact**: Ethical considerations in data collection (such as consent, privacy, and fairness) and analysis (such as avoiding manipulation or misrepresentation) are crucial for ensuring integrity in statistical practice.
   - **Why It’s Overlooked**: In the rush to find results, ethical concerns may be neglected, which can lead to misuse of data and loss of public trust.

---

### Final Thoughts

Statistics is a field rich with nuances, and many of these overlooked facts highlight how vital it is to approach statistical analysis thoughtfully and ethically. Understanding the deeper aspects of statistical methods ensures more accurate interpretations of data and ultimately leads to better decision-making.


Here are some **key facts** about **different statistical tests** that are commonly used across various fields. These facts help to better understand when and how these tests are applied, and what they actually measure.

---

### 1. **t-Test (Student’s t-Test)**

- **Fact**: The t-test compares the means of two groups to determine if they are statistically different from each other. It’s used when the sample size is small (typically \( n < 30 \)) and the population variance is unknown.
- **Why It’s Important**: It is widely used in comparing the means of two independent or related groups (e.g., comparing the average test scores of two groups of students).
- **Types**:  
  - **Independent t-test**: Used when comparing two independent groups.
  - **Paired t-test**: Used when the same group is measured at two different times or under two different conditions.
- **Assumptions**:  
  - The data is normally distributed.
  - The two groups are independent (for independent t-test).
  - The data points are independent and identically distributed (i.i.d.).

---

### 2. **Z-Test**

- **Fact**: A Z-test is used to compare sample means to a population mean or to compare the means of two populations when the sample size is large (typically \( n > 30 \)) and the population variance is known.
- **Why It’s Important**: The Z-test is often used when sample sizes are large enough to assume that the sampling distribution of the mean is approximately normal due to the **Central Limit Theorem**.
- **Types**:
  - **One-sample Z-test**: Used when comparing the sample mean to a known population mean.
  - **Two-sample Z-test**: Used when comparing two population means.
- **Assumptions**:
  - The sample size is large.
  - The population variance is known or can be reasonably estimated.
  - The data is approximately normally distributed.

---

### 3. **Chi-Squared Test**

- **Fact**: The Chi-squared test is used to assess the relationship between categorical variables. It is commonly used for **goodness-of-fit** tests or to test **independence** between two categorical variables.
- **Why It’s Important**: This test is crucial when you have categorical data and you want to know whether the observed frequencies in each category deviate significantly from what was expected.
- **Types**:
  - **Goodness-of-fit test**: Tests if a sample data matches a population with a specific distribution.
  - **Test for independence**: Tests whether two categorical variables are independent of each other (e.g., is gender independent of voting preference?).
- **Assumptions**:
  - Data should be categorical (nominal or ordinal).
  - Observations should be independent.
  - Expected frequency for each category should ideally be 5 or more.

---

### 4. **ANOVA (Analysis of Variance)**

- **Fact**: ANOVA is used to compare the means of three or more groups to determine if at least one group mean is significantly different from the others. It tests for **between-group variance** relative to **within-group variance**.
- **Why It’s Important**: ANOVA is commonly used in experiments where you have more than two groups to compare (e.g., testing different treatments or conditions).
- **Types**:
  - **One-way ANOVA**: Used when there is one independent variable with more than two levels (groups).
  - **Two-way ANOVA**: Used when there are two independent variables, and it can assess both individual and interaction effects.
  - **Repeated measures ANOVA**: Used when the same subjects are exposed to different conditions.
- **Assumptions**:
  - The data in each group is normally distributed.
  - The variances across groups are equal (homogeneity of variance).
  - The samples are independent.

---

### 5. **Mann-Whitney U Test**

- **Fact**: The **Mann-Whitney U test** is a non-parametric test that compares the medians of two independent groups, testing whether one group tends to have larger values than the other.
- **Why It’s Important**: This test is useful when the data does not meet the assumptions for a t-test (e.g., non-normal distribution or ordinal data).
- **Assumptions**: 
  - Data must be at least ordinal.
  - The two groups must be independent of each other.
  - Data from both groups should come from populations that have the same shape of distribution.

---

### 6. **Wilcoxon Signed-Rank Test**

- **Fact**: The **Wilcoxon Signed-Rank Test** is the non-parametric equivalent of the paired t-test. It is used to test the difference between paired or matched samples.
- **Why It’s Important**: It’s useful when the differences between paired observations are not normally distributed, or the data is ordinal.
- **Assumptions**:
  - The data is paired or matched.
  - The data is at least ordinal.
  - The differences between the pairs should be symmetric around the median.

---

### 7. **Pearson Correlation Coefficient (r)**

- **Fact**: The **Pearson correlation coefficient** is a measure of the linear relationship between two continuous variables. It ranges from -1 (perfect negative correlation) to +1 (perfect positive correlation), with 0 indicating no linear relationship.
- **Why It’s Important**: This is one of the most common ways to quantify the strength and direction of a linear relationship between two variables.
- **Assumptions**:
  - Both variables are continuous.
  - The relationship between the variables is linear.
  - The data is normally distributed.
  
---

### 8. **Spearman Rank Correlation**

- **Fact**: The **Spearman Rank Correlation** is a non-parametric measure of rank correlation. It assesses how well the relationship between two variables can be described using a monotonic function (increasing or decreasing).
- **Why It’s Important**: Unlike Pearson, it doesn’t require the data to be normally distributed and can be used with ordinal data or non-linear relationships.
- **Assumptions**:
  - Data is at least ordinal.
  - It assesses monotonic relationships (not necessarily linear).

---

### 9. **Fisher’s Exact Test**

- **Fact**: **Fisher's Exact Test** is used to determine if there are nonrandom associations between two categorical variables in small sample sizes, typically in \( 2 \times 2 \) contingency tables.
- **Why It’s Important**: Unlike the Chi-square test, which is not valid for small sample sizes or low-frequency data, Fisher’s Exact Test provides a precise p-value when sample sizes are small.
- **Assumptions**:
  - Data is categorical.
  - The test is ideal for small sample sizes and when expected cell frequencies are less than 5.

---

### 10. **Regression Analysis (Linear and Logistic)**

- **Fact**: **Regression analysis** is used to understand the relationship between a dependent variable and one or more independent variables.
  - **Linear Regression** models the relationship between a continuous dependent variable and continuous or categorical independent variables.
  - **Logistic Regression** is used when the dependent variable is binary (e.g., yes/no, 0/1 outcomes).
- **Why It’s Important**: Regression allows for prediction, modeling, and understanding the relationship between variables.
- **Assumptions** (for Linear Regression):
  - The relationship between variables is linear.
  - The residuals (errors) are normally distributed.
  - Homoscedasticity: constant variance of residuals.
  - Independence of residuals.
  
---

### 11. **Kruskal-Wallis Test**

- **Fact**: The **Kruskal-Wallis test** is the non-parametric equivalent of one-way ANOVA. It is used when the assumptions of normality and homogeneity of variance for ANOVA are not met, particularly with ordinal data.
- **Why It’s Important**: It allows you to compare more than two independent groups without assuming a normal distribution.
- **Assumptions**:
  - Data is at least ordinal.
  - The groups being compared are independent.
  - The data from each group are drawn from the same distribution shape.

---

### 12. **Log-Rank Test**

- **Fact**: The **Log-Rank test** is used to compare survival distributions of two or more groups. It is most commonly used in **survival analysis** to compare the time to an event (such as death or failure) between groups.
- **Why It’s Important**: This test is essential in medical research, particularly for comparing the effectiveness of different treatments over time.
- **Assumptions**:
  - The groups being compared have similar survival curves.
  - The survival times are independent within each group.

---

### Final Thoughts

Each statistical test has specific assumptions and is designed for particular types of data and research questions. Understanding when and why to use each test is crucial for making valid inferences from your data and avoiding misleading conclusions. Statistical testing isn't just about applying the correct formula—it’s about understanding the underlying assumptions and ensuring that your data meet those assumptions.