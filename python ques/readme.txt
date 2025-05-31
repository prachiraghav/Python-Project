Data Structures & Algorithms (1–15)

1. Find the maximum product of two integers in an array. Question (Using Arrays)
Hint: Sort the array or use a single-pass comparison to find the top two values.
2. Rotate a 2D matrix 90 degrees clockwise. Question (Using 2D Arrays)
Hint: Use transpose followed by reversing each row.
3. Question (Binary Search) Implement binary search on a sorted list to find a target value.
Hint: Use divide-and-conquer. Track low, mid, high pointers.
4. Question (Sorting) Implement merge sort.
Hint: Recursively split list, then merge sorted halves.
5. Question (Recursion) Generate all subsets of a list.
Hint: Include or exclude the current element and recurse.
6. Question (Sliding Window) Find the maximum sum of any subarray of size k.
Hint: Use a sliding window to avoid recomputing sums.
7. Question (Stack) Check if a string has balanced parentheses.
Hint: Use a stack to track opening and closing brackets.
8. Question (Queue) Implement a queue using two stacks.
Hint: Use one stack for enqueue, another for dequeue.
9. Question (Linked List) Reverse a singly linked list.
Hint: Change the direction of pointers iteratively.
10. Question (Hash Map) Find the first non-repeating character in a string.
Hint: Use a dictionary to track counts.
11. Question (Binary Tree) Perform inorder traversal of a binary tree.
Hint: Use recursion: left → root → right.
12. Question (Binary Tree) Check if a binary tree is symmetric.
Hint: Compare left and right subtrees recursively.
13. Question (Heap) Find the kth largest element in an array.
Hint: Use a min heap of size k.
14. Question (Graph - DFS) Find if a path exists between two nodes in a graph.
Hint: Use depth-first search recursively.
15. Question (Graph - BFS) Find the shortest path in an unweighted graph.
Hint: Use breadth-first search and track visited nodes.
String & Text Manipulation (16–25)

16. Question (String) Check if a string is a permutation of a palindrome.
Hint: Count character frequencies. Max one odd count allowed.
17. Question (Regex) Extract all email addresses from a string.
Hint: Use Python’s re module with findall().
18. Question (String Compression) Compress a string using counts of repeated characters (e.g., "aabcc" → "a2b1c2"). Hint: Track current char and count.
19. Question (Longest Substring) Find the length of the longest substring without repeating characters.Hint: Use a sliding window and set/dictionary.
20. Question (Edit Distance)Compute the minimum number of edits to convert one string to another.Hint: Use dynamic programming.
21. Question (Anagram Check)Check if two strings are anagrams.
Hint: Sort both or count characters.
22. Question (Pangram Check)Check if a string contains all letters of the alphabet.
Hint: Use a set to track unique characters.
23. Question (Text Justification)Given a list of words and a line width, justify the text.
Hint: Distribute spaces evenly between words.
24. Question (URLify)Replace spaces in a string with %20.Hint: Use .replace() or manual loop.
25. Question (Count Words)Count the number of unique words in a file.
Hint: Read file, split on spaces, use a set.

Object-Oriented Programming & Design (26–30)
26. Question (Class & Object)Design a class Rectangle with methods to compute area and perimeter.Hint: Use _init_ and define custom methods.
27. Question (Inheritance)Create a base class Animal and a derived class Dog with overridden methods.Hint: Use super() to call parent methods.
28. Question (Encapsulation)Implement private attributes with getters and setters in a class.
Hint: Use __attribute and @property.
29. Question (Polymorphism)Create a class structure that shows method overriding with two classes.Hint: Same method name, different implementations.
30. Question (Magic Methods)Implement a Vector class with overloaded + operator.
Hint: Define _add_() method.
File Handling, APIs, JSON, and Libraries (31–38)

31. Question (File I/O)Read a CSV file and print contents row-wise.Hint: Use the csv module.
32. Question (File Handling)Write to a text file line by line from a list.Hint: Use with open() and write().
33. Question (JSON)Convert a Python dictionary to JSON and back.Hint: Use json.dumps() and json.loads().
34. Question (API Requests)Make a GET request to an API and print the response JSON.
Hint: Use the requests library.
35. Question (Logging)Log different levels of messages to a file.Hint: Use the logging module.
36. Question (Zip Files)Zip multiple text files into one archive.Hint: Use zipfile.ZipFile().
37. Question (Datetime)Print the current date, time, and the difference between two dates.
Hint: Use datetime.datetime.now() and timedelta.
38. Question (Pandas)Read a CSV file and display rows where a column value > 100.
Hint: Use df[df['column'] > 100].
Functional & Advanced Python (39–50)

39. Question (Lambda Functions)Sort a list of tuples by the second element.Hint: Use sorted() with a lambda.
40. Question (Map-Filter-Reduce)Find the product of all even numbers in a list.
Hint: Use filter() and reduce().
41. Question (Decorators)Create a decorator that logs the execution time of a function.
Hint: Use time.time() and wrapper function.
42. Question (Generators)Create a generator that yields the Fibonacci sequence up to n.
Hint: Use yield instead of return.
43. Question (Comprehensions)Create a dictionary of squares for numbers 1–10 using comprehension.Hint: Use {i: i**2 for i in range(1,11)}.
44. Question (Context Manager)Create a custom context manager using a class or contextlib.
Hint: Define _enter_ and _exit_.
45. Question (Multithreading)Create threads that run two different functions in parallel.
Hint: Use threading.Thread().
46. Question (Exception Handling)Write a function that safely divides two numbers and handles exceptions.Hint: Catch ZeroDivisionError and TypeError.
47. Question (Memoization)Optimize a recursive Fibonacci function with memoization.
Hint: Use @lru_cache.
48. Question (Typing & Annotations)Add type hints to a function that returns the square of a float.
Hint: Use def square(x: float) -> float.
49. Question (Unit Testing)Write test cases for a calculator using unittest.
Hint: Use assertEqual, setUp, etc.
50. Question (Metaclass)Create a metaclass that adds a created_at attribute to classes.
Hint: Use type._new_() to customize class creation.

NumPy (1–10)
1. Question (NumPy - Array Creation)Create a 5x5 matrix filled with random integers from 1 to 100.Hint: Use np.random.randint().
2. Question (NumPy - Indexing)Extract the last column of a 2D NumPy array.Hint: Use slicing: [:, -1].
3. Question (NumPy - Statistics)Find the mean, median, and standard deviation of a NumPy array.Hint: Use np.mean(), np.median(), np.std().
4. Question (NumPy - Reshape)Reshape a 1D array of 25 elements into a 5x5 matrix.
Hint: Use .reshape(5, 5).
5. Question (NumPy - Boolean Masking)Filter all values greater than 50 in an array.
Hint: Use arr[arr > 50].
6. Question (NumPy - Matrix Operations)Multiply two matrices using NumPy.
Hint: Use np.dot() or @ operator.
7. Question (NumPy - Unique Elements)Find all unique elements in an array.
Hint: Use np.unique().
8. Question (NumPy - Missing Values)Replace NaN values in an array with the column mean.
Hint: Use np.isnan() and np.nanmean().
9. Question (NumPy - Broadcasting)Add a 1D array to each row of a 2D matrix.
Hint: Let NumPy handle broadcasting.
10. Question (NumPy - Sorting)Sort a NumPy array by rows.
Hint: Use np.sort(axis=1).
Pandas (11–25)

11. Question (Pandas - Series & DataFrame)Create a Pandas Series with random numbers and custom index.Hint: Use pd.Series(data, index).
12. Question (Pandas - Data Import)Read a CSV file and display the top 5 rows.
Hint: Use pd.read_csv() and .head().
13. Question (Pandas - Filtering)Filter rows where Salary > 50000.
Hint: Use boolean filtering: df[df['Salary'] > 50000].
14. Question (Pandas - GroupBy)Group data by Department and calculate average salary.
Hint: Use df.groupby('Department')['Salary'].mean().
15. Question (Pandas - Aggregation)Get count, min, and max salary per department.
Hint: Use .agg(['count', 'min', 'max']).
16. Question (Pandas - Merging)Merge two DataFrames on a common column.
Hint: Use pd.merge().
17. Question (Pandas - Join Types)Perform a left join between two tables on EmployeeID.
Hint: Use how='left' in merge().
18. Question (Pandas - Missing Values)Fill missing values in a column with the column median.
Hint: Use df['col'].fillna(df['col'].median()).
19. Question (Pandas - New Column)Add a new column Bonus = Salary * 0.1.
Hint: Simple assignment: df['Bonus'] = df['Salary'] * 0.1.
20. Question (Pandas - Apply Function)Apply a custom function to calculate tax (15%) on Salary.Hint: Use .apply() with a lambda function.
21. Question (Pandas - Pivot Table)Create a pivot table showing average sales per region and product.Hint: Use pd.pivot_table().
22. Question (Pandas - Value Counts)Find the frequency of values in a categorical column.
Hint: Use value_counts().
23. Question (Pandas - Sorting)Sort the DataFrame by Salary in descending order.
Hint: Use df.sort_values(by='Salary', ascending=False).
24. Question (Pandas - String Operations)Extract domain from an email column.
Hint: Use str.split('@').str[1].
25. Question (Pandas - Time Series)Convert a column to datetime and filter rows after 2020.
Hint: Use pd.to_datetime() and filtering.
Data Cleaning & EDA (26–32)

26. Question (Outliers)Remove rows where a column value is more than 3 standard deviations from the mean.Hint: Use Z-score or IQR.
27. Question (Duplicates)Remove duplicate rows from a DataFrame.Hint: Use df.drop_duplicates().
28. Question (EDA - Describe)Summarize statistics for numerical columns.
Hint: Use df.describe().
29. Question (EDA - Info)Get column types and non-null counts.Hint: Use df.info().
30. Question (EDA - Correlation)Find correlation between Age and Salary.
Hint: Use df.corr().
31. Question (EDA - Frequency Plot)Plot value counts of a categorical variable.
Hint: Use df['col'].value_counts().plot(kind='bar').
32. Question (Data Binning)Bin Age into categories (e.g., child, teen, adult).
Hint: Use pd.cut().
Visualization (Matplotlib/Seaborn) (33–40)
33. Question (Matplotlib - Line Plot)Plot sales over time.Hint: Use plt.plot(dates, sales).
34. Question (Matplotlib - Bar Chart)Create a bar chart of average sales by region.
Hint: Use plt.bar().
35. Question (Matplotlib - Histogram)Plot distribution of Salary.Hint: Use plt.hist(df['Salary']).
36. Question (Seaborn - Boxplot)Draw boxplot for Salary grouped by Department.
Hint: Use sns.boxplot(x='Department', y='Salary', data=df).
37. Question (Seaborn - Heatmap)Visualize correlation matrix using a heatmap.
Hint: Use sns.heatmap(df.corr()).
38. Question (Seaborn - Countplot)Countplot of categorical variable Gender.
Hint: Use sns.countplot(x='Gender', data=df).
39. Question (Seaborn - Pairplot)Plot pairwise relationships in DataFrame.
Hint: Use sns.pairplot(df).
40. Question (Dual Axis Plot)Plot revenue and profit on the same plot with dual Y axes.
Hint: Use twinx() in matplotlib.
Statistics & SQL-like Analysis (41–45)
41. Question (Mean/Median Mode)Compute mean, median, and mode of a column.
Hint: Use mean(), median(), mode().
42. Question (Hypothesis Testing)Perform a t-test between two groups (e.g., Male vs Female salaries).Hint: Use scipy.stats.ttest_ind().
43. Question (Group Percentiles)Calculate the 90th percentile salary per department.
Hint: Use groupby().quantile(0.9).
44. Question (SQL - GroupBy Aggregates)"SELECT Department, AVG(Salary) FROM table GROUP BY Department" in pandas.Hint: Use df.groupby('Department')['Salary'].mean().
45. Question (SQL - WHERE Clause)Filter all employees where Age > 30 and Gender = 'Male'.
Hint: Use logical filtering with &.
pplied Case-Based Analysis (46–50)
46. Question (Customer Churn)Find % of customers who churned grouped by subscription plan.Hint: Group by plan, calculate mean on churn == 1.
47. Question (Sales Trend)Calculate month-over-month sales growth.
Hint: Use .pct_change() after resampling by month.
48. Question (Top N)Find top 5 products by total revenue.Hint: Use groupby() then .nlargest(5).
49. Question (Cohort Analysis)Assign users to a cohort based on their first purchase month.
Hint: Use groupby(user)['date'].min().
50. Question (Retention Rate)Calculate user retention rate for second and third month after signup.Hint: Use cohorts and user tracking across months.

Beginner Level (1–25)
Basic SELECT & WHERE
1. SELECT all records from a table named employees.
2. SELECT only the name and salary columns from employees.
3. Get all employees with a salary greater than 50000.
4. Get employees in the 'Sales' department.
5. Find employees hired after January 1st, 2020.
6. Use LIKE to find employee names that start with 'A'.
7. Get employees whose names end with 'son'.
8. Select employees whose salary is between 40000 and 60000.
9. Find employees who are not in the 'HR' department.
10. Sort the employees by hire_date descending.
Aggregate Functions
1. Count the total number of employees.
12. Get the average salary of employees.
13. Find the highest salary in the company.
14. Find the minimum hire date.
15. Sum the total salary paid.
GROUP BY & HAVING
16. Group employees by department and count how many in each.
17. Group by department and calculate average salary.
18. Get departments with average salary > 60000.
19. Group by job_title and get min and max salary.
20. Group by hire year and count employees hired each year.
Joins
21. Inner join employees and departments on dept_id.
22. Left join employees and projects on emp_id.
23. Right join orders and customers on customer_id.
24. Find employees who haven’t been assigned to any project.
25. Join three tables: employees, departments, and locations.
Intermediate Level (26–50)
Subqueries
6. Find employees earning more than the average salary.
27. Get the names of departments where no employees are assigned.
28. Get the second highest salary using subquery.
29. Find employees who earn more than their manager.
30. Select employees whose department is in a given city.
Window Functions
31. Add a row number for each employee ordered by hire_date.
32. Rank employees based on salary in each department.
33. Get running total of salary ordered by hire_date.
34. Calculate average salary over last 3 rows (rolling average).
35. Show salary difference from department average.
Set Operations
36. UNION two tables: current_employees and ex_employees.
37. Get records in A but not in B using EXCEPT.
38. Get common records from two tables using INTERSECT.
Date Functions
39. Get employees hired in the last 90 days.
40. Extract month and year from hire_date.
41. Calculate number of days since hire for each employee.
42. Find employees with birthday this month.
String Functions
43. Get first 5 characters of employee names.
44. Concatenate first and last names as full name.
45. Convert all names to uppercase.
Data Cleaning & NULL Handling
46. Find records with NULL salary.
47. Replace NULL salary with 0 using COALESCE.
48. Count how many employees have no manager assigned.
Case Statements
49. Create a column: 'High' if salary > 70000, else 'Low'.
50. Bucket employees into 'Junior', 'Mid', 'Senior' based on experience.

1–10. Advanced Subquerie
1. Get employees whose salary is above the average salary of their department.
2. Find departments where no employee has a salary below 40000.
3. Get the top 3 earners in each department.
4. Return employees whose manager earns less than themselves.
5. List employees who have the same salary as someone in a different department.
6. Find all employees hired before the earliest hire date in the 'HR' department.
7. Get the name of the department with the highest average salary.
8. Get names of employees who have never submitted a timesheet (assume a timesheets table).
9. Find products whose price is more than the average of products in the same category.
10. Find customers who placed more orders than the average number of orders per customer
11–20. Advanced Joins and Relationships
11. Find customers who placed an order but never paid for it.
12. Join three tables: orders, order_items, and products to get total quantity per product.
13. Find employees whose department and project locations are different.
14. List employees who share the same manager.
15. Get a list of duplicate email addresses in the users table.
16. Identify employees assigned to more than 2 projects.
17. Find the latest order per customer using JOIN and not window functions.
18. Return users who have never logged in (assume logins table).
19. Get orders that contain both Product A and Product B.
20. List customers who have ordered every product in category ‘Electronics’.
21–30. Window Functions21. Rank employees within each department based on salary.
22. Find the difference between each employee’s salary and the department average.
23. Get cumulative sales per customer over time.
24. Find how many orders each customer has placed before their current one.
25. Use NTILE(4) to segment customers into quartiles based on total spending.
26. Identify days when sales were higher than the previous day.
27. Find employees who have the same hire date as the person before them in the table.
28. Calculate moving average of sales for the past 7 days.
29. Show top 2 products by sales within each category.
30. List employees whose salary change (compared to the previous year) is negative.
31–40. Case Statements, Pivoting, and Formatting31. Create a column labeling sales as 'Low', 'Medium', or 'High'.
32. Pivot monthly sales data into columns for each month.
33. Unpivot sales columns into a long format (e.g., Jan, Feb, Mar columns → rows).
34. Count orders per customer and label them: ‘New’, ‘Loyal’, ‘VIP’ based on count.
35. Write a query to return "Weekday" or "Weekend" for order dates.
36. Create a derived column showing performance status using salary and experience.
37. Create a flag column that shows if a customer’s total spend is in top 10%.
38. Assign a bonus percent based on sales amount using CASE WHEN.
39. Calculate percentage contribution of each product to total sales.
40. Calculate year-over-year growth in sales.
41–50. Optimization, Analysis & Logic Challenge
41. Write an efficient query to return the 10 most common error codes from a log table.
42. Optimize a query joining large orders and products tables (hint: indexing, filtering).
43. Return the last N rows from a large table with a timestamp column.
44. Use EXISTS instead of IN to improve performance on a subquery.
45. Detect anomalies in daily sales (days where sales were 3x the average).
46. Find customers who have churned (no orders in last 6 months).
47. Detect gaps in sequential data (e.g., missing order numbers).
48. Simulate a running balance using window functions.
49. Return the total hours worked per employee for projects they worked on in parallel.
50. Compare current month vs previous month revenue per product.
