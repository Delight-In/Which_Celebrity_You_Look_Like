### **Probability and Statistics**

#### **1. Counting (Permutation and Combinations)**

- **Permutations** (arrangements of objects):
  
  $$ P(n, r) = \frac{n!}{(n-r)!} $$

  Where:
  - \( n \) is the total number of items,
  - \( r \) is the number of items to arrange,
  - \( n! \) is the factorial of \( n \).

- **Combinations** (selections of objects without regard to order):

  $$ C(n, r) = \frac{n!}{r!(n-r)!} $$

  Where:
  - \( n \) is the total number of items,
  - \( r \) is the number of items to choose,
  - \( n! \) is the factorial of \( n \).

#### **2. Probability Axioms**

The probability of an event \( A \) is denoted by:

$$ P(A) \geq 0 $$

And for the sample space \( S \), we have:

$$ P(S) = 1 $$

#### **3. Bayes Theorem**

Bayes' Theorem relates conditional probabilities and is given by:

$$ P(A|B) = \frac{P(B|A)P(A)}{P(B)} $$

Where:
- \( P(A|B) \) is the conditional probability of event \( A \) given \( B \),
- \( P(B|A) \) is the conditional probability of event \( B \) given \( A \),
- \( P(A) \) and \( P(B) \) are the probabilities of \( A \) and \( B \), respectively.

#### **4. Conditional Expectation and Variance**

- **Conditional Expectation**:

  $$ E[X|Y] = \sum_x x \cdot P(X=x|Y) $$

  Where:
  - \( X \) is a random variable,
  - \( Y \) is a conditioning variable.

- **Conditional Variance**:

  $$ \text{Var}(X|Y) = E[(X - E[X|Y])^2 | Y] $$

#### **5. Mean, Median, Mode, and Standard Deviation**

- **Mean**:

  $$ \mu = E[X] = \frac{1}{n} \sum_{i=1}^{n} x_i $$

- **Median** is the middle value of a data set when sorted.

- **Mode** is the value that appears most frequently.

- **Standard Deviation**:

  $$ \sigma = \sqrt{E[(X - \mu)^2]} $$

#### **6. Random Variables & Probability Mass Functions (PMFs)**

For a **discrete random variable** \( X \), its probability mass function (PMF) is:

$$ P(X = x) $$

#### **7. Distributions (Binomial, Poisson, Normal, etc.)**

- **Binomial Distribution** (for a number of successes in a fixed number of Bernoulli trials):

  $$ P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} $$

  Where:
  - \( n \) is the number of trials,
  - \( p \) is the probability of success,
  - \( k \) is the number of successes.

- **Poisson Distribution** (for the number of events in a fixed interval):

  $$ P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!} $$

  Where:
  - \( \lambda \) is the expected number of occurrences in the interval.

- **Normal Distribution** (standard form):

  $$ f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} $$

  Where:
  - \( \mu \) is the mean,
  - \( \sigma^2 \) is the variance.

#### **8. Central Limit Theorem**

The Central Limit Theorem states that the distribution of the sum (or average) of a large number of independent, identically distributed random variables will tend toward a normal distribution:

$$ \frac{X - \mu}{\sigma / \sqrt{n}} \sim N(0, 1) $$

#### **9. Confidence Interval**

For a sample mean \( \bar{x} \), the confidence interval for the population mean \( \mu \) is:

$$ \bar{x} \pm z \cdot \frac{\sigma}{\sqrt{n}} $$

Where:
- \( \bar{x} \) is the sample mean,
- \( z \) is the z-score corresponding to the desired confidence level,
- \( \sigma \) is the population standard deviation,
- \( n \) is the sample size.

---

### **Linear Algebra**

#### **1. Vector Space**

A **vector space** is a collection of vectors that can be added together and multiplied by scalars, satisfying the following properties:
- Closure under addition and scalar multiplication.

#### **2. Eigenvalues and Eigenvectors**

An **eigenvector** \( v \) of a matrix \( A \) satisfies:

$$ A v = \lambda v $$

Where:
- \( \lambda \) is the **eigenvalue** corresponding to eigenvector \( v \).

#### **3. Determinant of a Matrix**

The **determinant** of a matrix \( A \), denoted \( \det(A) \), is a scalar value that can be computed for square matrices, and is used to determine if the matrix is invertible. For a 2x2 matrix:

$$ \det(A) = ad - bc $$

For larger matrices, the determinant involves a more complex calculation using minors and cofactors.

---

### **Calculus and Optimization**

#### **1. Derivative of a Function**

The **derivative** of a function \( f(x) \) with respect to \( x \) is:

$$ f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} $$

#### **2. Taylor Series Expansion**

The **Taylor series** expansion of a function \( f(x) \) around a point \( a \) is:

$$ f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots $$

---

### **Programming, Data Structures, and Algorithms**

#### **1. Basic Sorting Algorithms**

- **Bubble Sort** iterates over the list, compares adjacent elements, and swaps them if they are in the wrong order.

- **Insertion Sort** iterates over the list and "inserts" each element into its correct position relative to previously sorted elements.

- **Selection Sort** repeatedly selects the smallest (or largest) element from the unsorted portion and places it at the beginning of the sorted portion.

#### **2. Binary Search**

Binary search on a sorted array works by repeatedly dividing the search interval in half:

$$ \text{mid} = \frac{\text{low} + \text{high}}{2} $$

If the value at the midpoint is equal to the target value, the search ends. If the target is less than the value at the midpoint, the search continues in the left half; otherwise, it continues in the right half.

---

### **Machine Learning**

#### **1. Linear Regression**

The **simple linear regression** model is:

$$ y = \beta_0 + \beta_1 x + \epsilon $$

Where:
- \( y \) is the target variable,
- \( \beta_0 \) is the intercept,
- \( \beta_1 \) is the slope,
- \( x \) is the feature,
- \( \epsilon \) is the error term.

#### **2. K-Nearest Neighbors (KNN)**

The **K-Nearest Neighbors** algorithm classifies data based on the majority class among the \( k \) closest data points.

---

### **Database Management and Warehousing**

#### **1. SQL Query**

An example SQL query to select data from a table:

```sql
SELECT column1, column2 FROM table_name WHERE condition;
```

#### **2. Relational Algebra**

The **selection** operation in relational algebra is:

$$ \sigma_{\text{condition}}(R) $$

Where:
- \( R \) is a relation (table),
- \( \sigma \) is the selection operation.

---

### **AI and Search Algorithms**

#### **1. Informed vs. Uninformed Search**

- **Uninformed Search**: An algorithm like BFS or DFS that searches without knowledge about the goal.
  
- **Informed Search** (e.g., A* search) uses a heuristic to guide the search process more efficiently.

#### **2. Logic (Propositional and Predicate)**

- **Propositional Logic** uses variables that can be either true or false, with logical connectives like AND (\( \land \)), OR (\( \lor \)), and NOT (\( \neg \)).
  
- **Predicate Logic** extends propositional logic to handle predicates, variables, and quantifiers (e.g., \( \forall x, P(x) \)).

---
