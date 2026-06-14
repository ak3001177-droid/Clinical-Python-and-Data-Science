## 📊 Matplotlib Syntax Cheatsheet (Clinical Data Visualization)

Below is a quick reference guide for the core `matplotlib.pyplot` functions I use to render and format medical data visualizations:

### 1. Figure Setup & Output Management
* **`plt.figure(figsize=(10, 6))`**: Initializes the plot canvas and defines its dimensions (width, height).
* **`plt.show()`**: Renders and displays the compiled visualization on the screen.
* **`plt.savefig('filename.png')`**: Exports the current figure to the local directory as a high-resolution image file.

### 2. Core Visualization Types (Data Representation)
* **`plt.bar()`**: Generates a bar chart; ideal for categorical comparisons (e.g., CT vs. MRI scan volumes).
* **`plt.pie()`**: Creates a pie chart; used for displaying proportional data or percentages of a whole.
* **`plt.plot()`**: Renders a line graph; optimal for tracking trends over a continuous variable, like time.
* **`plt.hist()`**: Constructs a histogram; essential for visualizing the frequency distribution of continuous data (e.g., patient age demographics).
* **`plt.scatter()`**: Produces a scatter plot; used to identify correlations between two continuous variables (e.g., patient age vs. recovery time).

### 3. Plot Formatting & Aesthetics (Enhancing Readability)
* **`plt.title("Title")`**: Assigns a primary heading to the visualization.
* **`plt.xlabel("Text")` & `plt.ylabel("Text")`**: Defines the labels for the X and Y axes, respectively.
* **`plt.legend()`**: Adds an explanatory legend to decode colors, markers, or line styles used in the plot.

### 4. Advanced Annotations
* **`plt.bar_label(bars, padding=3, fontweight='bold')`**: Automatically annotates bars with their precise numerical values. 
  > *Note: `padding` controls the spacing between the label and the bar margin, while `fontweight` adjusts text thickness for better visibility.*


## 🐼 Pandas Syntax Cheatsheet (Clinical Data Manipulation)

Below is a quick reference guide for the core `pandas` functions I use to clean, process, and analyze clinical datasets:

### 1. Initial Data Inspection (System Vitals Check)
* **`pd.read_csv()` / `pd.read_excel()`**: Imports external datasets into the script environment for processing.
* **`df.head()`**: Returns the first 5 rows of the DataFrame for a quick structural and data overview.
* **`df.info()`**: Provides a concise summary of the DataFrame, including row/column counts and data types.
* **`df.describe()`**: Generates descriptive statistics (e.g., mean, count, min, max) for numerical columns.

### 2. Data Cleaning & Preprocessing
* **`print(df.isnull().sum())`**: Calculates and displays the exact count of missing (null) values in each column.
* **`df.fillna()`**: Imputes or replaces missing/null values with a specified value to prevent data loss.
* **`df.dropna()`**: Eliminates entire rows (or columns) that contain null or missing values to ensure data integrity.
* **`df.drop_duplicates()`**: Identifies and removes duplicate entries from the dataset.

### 3. Data Filtering & Slicing (The Surgeon's Scalpel)
* **`df[df['Column'] == 'Value']`**: Filters the DataFrame based on a specific boolean condition.
* **`df.loc[]` / `df.iloc[]`**: Extracts specific rows or columns using label-based (`.loc`) or index-based (`.iloc`) selection.

### 4. Aggregation, Merging & Exporting (Data Reporting)
* **`df.groupby()`**: Groups data based on specified categories to perform aggregate functions (like sum or mean).
* **`pd.merge()`**: Joins two distinct DataFrames based on a common key/column (e.g., merging patient vitals with billing records).
* **`df.to_csv()`**: Exports the final, cleaned DataFrame to a local directory as a new CSV file.
