# Introduction
This documment is aimed to help us understand the big picture of how the realms of *Data Science* and *Machine Learning* fit together in the overall puzzle and to see how is the workflow of this process.

## Breaking It Down
Let's start by breaking the whole puzzle into peaces and then, diving a little deeper into each piece to grasp how the process occurs, and finally fit them together to make sense of the whole.

### What goes into a succeful model:
The process can be structured into a few steps. Depending on the situation you might start by one or another and then jump back and forward between them, but the overall structure is the following:
  
  *  Exploratory Analysis (10%)
  *  Data Cleaning (20%)
  *  Feature Engineering (25%)
  *  Algorithm Selection (10%)
  *  Model Training (15%)
  *  Other (20%)

Now That we know the structure of the process, we can start diving into each step of it.

## Chapter 1 - An overview of the workflow
What we want to do for now on, is to understand **how things work at a higher level and develop a systematic apprach to solving problems.**
Now let's take a look at key terms, processes and structures that are important to understand the workflow of applied *ML*.

### Machine Learning ≠ Algorithms 
First of all let's make this clear. *ML* is **NOT** about algorithms. It is a comprehensive approach to solving problems.
Individual algorithms are only one piece of the puzzle. The rest of the puzzle is how you apply them the right way.

### What's Machine Learning?
Is the practice of teaching computers how to learn patterns from data, often for making decisions or predictions. 
Like when a kid learns that something is dangerous by his own (normally through experience).
The opposite would the the parents of the kid showing him why something is dangerous. 
So, in summary. The computer must be able to learn patterns that it's not explicitly programmed to identify.

### Key Terminology
We want to develop our practical intuition. For this matter, we should know the following terms:
 * **Model** - a set of patterns learned from data.
 * **Algorithm** - a specific ML process used to train a model.
 * **Training data** - the dataset from which the algorithm learns the model.
 * **Test data** - a new dataset for reliably evaluating model performance.
 * **Features** - Variables (columns) in the dataset used to train the model.
 * **Target variable** - A specific variable you're trying to predict.
 * **Observations** - Data points (rows) in the dataset.

### Machine Learning Tasks
In applied *ML* you should first of all pick the right **_Ml_ task** for the job.
 * A **task** is an specific objetive for your algorithm. 
 * You can swap algorithms in and out as long as you **pick the right task**.
 * You normally want to **perform multiple algorithms** to know which one will perform best for your dataset.

The most common categories of tasks are:
 1. **Supervised Learning:**
    * Used as an advanced form of *predictive modeling* when you have **labeled data**.
    * You **must lavel your desired output/answer** and them tell the algorithm what's correct while trainning it (suppervising it) so you finally can get your desired result on yor *predictive model*.
      * **Regression** is the task for modeling continuous target variables.
      * **Classification** is the task for modeling categorical (a.k.a. "class") target variables.
 2. **Unsupervsed learning:**
    * Often used either as a form of automated data analysis or automated signal extraction. Is used for **unlabeled data**.
    * It has **no predetermined correct answer**, so you allow it to learn patterns directly from the data (without supervision). 
      * **Clustering** is the most common unsupervised learning task, and it's for finding groups within your data.
      
### The 3 Elements Of Great Machine Learning
 #### Human Guidance
  * Your guidance plays a huge roll, because you will need to **make dozens of decision along the way.**
  * The very first major decision is **how to road-map your proyect for garanteed success.**
 #### Clean, Relevant Data
  * The **quality of your data** is extremely important. after all... Garbage In = Garbage Out
  * Professionals on the field expend most of their time **cleaning, understanding and engineering new  features for the data**.
 #### Avoid Overfitting
  * This is a really dangerous area, after all. It can burn to ashes your work! **An overfitted model has "memorized" the noise in the training set, instead of learning the true underlying patterns.**
  * An overfit model within a hedge fund can cost millions of dollars in losses.
  * An overfit model within a hospital can costs thousands of lives.
  * For most applications, the stakes won't be quite that high, but **overfitting is still the single largest mistake you must avoid.**

### The Machine Learning Blueprint
The *ML* **Blueprint** is dessigned around **The 3 Elements Of Great ML**.
  1.  **Exploratory Analysis**
      - **Get to know the data.** This step should be quick, efficient, and decisive.
  2.  **Data Cleaning**
      - **Clean the data to avoid many common pitfalls.** Better data beats fancier algorithms.
  3.  **Feature Engineering**
      - **Help your algorithms focus on what's important** by creating new features.
  4.  **Algorithm Selection**
      - **Choose the best, most appropriate algorithms** without wasting your time.
  5.  **Model Training**
      - Finally, **train your models.** This step is pretty formulaic once you've done the first 4.
#### Other situational steps
  - **Project Scoping:** roadmap the project and anticipate data needs.
  - **Data Wrangling:** restructure your dataset into a format that algorithms can handle.
  - **Preprocessing:** often, transforming your features first can further improve performance.
  - **Ensembling:** you can squeeze out even more performance by combining multiple models.
#### Two key Takeaways To Remember:
  * Machine learning should not be haphazard and piecemeal. It should be systematic and organized.
  * Better data beats fancier algorithms.

##  Chapter 2 - Exploratory Analysis
For this chapter we will start completely diving into the first step of all the five steps of the process of modeling.
This step should **NOT** be confused with data visualization or summary statistics. Those are merely tools that we have to achieve an end. **Proper exploratory analysis** is about answering questions. It's about **extracting enough insights** from your dataset to course correct before you get lost in the weeds.

### Why Explore Your Dataset Upfront?
Your purpose here is to **"get to know"** the dataset. Doing this from an up-front approach have some advantages:
  1.  You'll gain valuable hints for *data cleaning* (which can make or break your models).
  2.  You'll think of ideas for *feature engineering* (which can take your models from good to great).
  3.  You'll get a **"feel"** for the dataset (which will help you to communicate results and deliver greater impact).

However, a **pretty important fact** is that exploratory analysis for *ML* should be **quick, efficient and decisive.**
There are infinite possible plots, charts, and tables, but you only need a handful to **"get to know"** the data well enough to work with it. 

#### Start With Basics
The first and most basic questions you want to answer are:
  - How many observations do I have?
  - How many features?
  - What are the data types of my features?
  - Do I have a target variable?
#### Example Observations
Then you want to display **example observations** from the dataset. This will give you a **"feel"** of the values in each feature and to see if everything makes sense. 
**Example observation** is **NOT** for rigurous analysis, just to give you a **qualitative "feel"** of the dataset. here you should ask:
  - Do the columns make sense?
  - Do the values in those columns make sense?
  - Are the values on the right scale?
  - Based on this overview, is missing data going to be a big problem?

####  Plot Numerical Distributions
Often, a quick dirty grid of **histograms** is enough to understand the distribution.
Here you should look out for: 
  - Unexpected **distributions** 
  - Potential **outliers**
  - Features that **should be binary**
  - Boundaries that don't make sense
  - Potential measurement errors
At this point, is pretty important that **you make notes and/or point out** potential fixes you'd like to make. This will be pretty useful when we reach our *data cleaning* stage. 

#### Plot Categorical Distributions
Now, instead of **histograms**, we use **bar plots**.
Particularly, you want to look out for **sparse classes** (have very small number of observations).
A **class** is a unique value for a categorical feature.
You want to look out for **sparse classes** because those tend to be problematic when building a model.
  - In the best case they don't influence the model much
  - In the worse case, they can **overfit** the model and game over. 
Here you want to **make a note** to *combine* or *reassign* some of these classes later (on *feature engineering*). 

#### Plot Segmentation
These are powerful ways to **observe the relationship between categorical and numerical features**.
**Box Plots** Allow us to do so, they have some interesting indicators such as:
  * The median
  * The min and max 
  * Inter Quartile Range
These are pretty important to make a comparisson between different types of variables and suggest possible data truncation, outliers, skewed patters, clusters, etc. This is very important when **assessing the generalizability of your models later!**
#### Study correlations 
Correlation allows you to **observe the relationship between numeric features.**
What you need to know about correlation:
  * **Positive** correlation means that as one feature increases, the other increases. 
  * **Negative** correlation means that as one feature increases, the other decreases. 
  * Correlations near -1 or 1 indicate a **strong relationship.**
  * Those closer to 0 indicate a **weak relationship.**
  * 0 indicates **no relationship.**
  * Correlation **headmaps**  allow you to visualize this information.
#### In general you should look out for:
   * Which features are **strongly correlated** with the **target variable?**
   * Are there **interesting or unexpected** strong correlations between other features?

Remember that your aim here is to **gain intuition** about the data. 
By the end of your Exploratory Analysis step, you'll have a pretty good understanding of the dataset, some notes for data cleaning, and possibly some ideas for feature engineering.

## Chapter 3 - Data Cleaning
Depending of the quality of your data, your projects will **live** or **die**.
The steps and techniques for data cleaning vary from dataset to dataset. Here, we are going to learn a **reliable starting framework** that can ve used every time. 

### Better Data > Fancier Algorithms
Proper data cleaning can make or break your project. This is why professional *DS* spend a very large portion of the time on this step.
Because a simple boolean statement:

*>>> Better Data > Fancier algorithms*

*True*

**_Congratulations, you just learned python boolean expressions!_**

Don't get it yet? try reasoning with this, we already mentioned it:

*>>> input = garbage*

*>>> output = garbage*

*>>> input == output*

*True*

####  Remember this because if we reiterate over it that much is for something:
  - Garbage in gets you garbage out.
  - From a properly cleaned dataset, even simple algorithms can learn impressive insights from the data.
  - Different types of data, require different types of cleanin, **BUT**. The systematic approach laid out in this lessons can always serve as a good starting point. 

### Remove Unwanted Observations
This include **duplicate** or **irrelevant** observations. Wipe them out!
  - **Duplicate observations:** Most frequently arise during **data collection**, such as when you:
    * Combine datasets from multiple places
    * Scrape data
    * Receive data from clients/other departments
  - **Irrelevant observations:** Are those that **don't actually fit** the specific problem that you are trying to solve.
    * This is a great time to review the distribution of your categorical features (in your exploratory analysis charts), to see if there are any classes that shouldn't be there.
    * Checking for irrelevant observations **before engineering features** can save you many headaches down the road.
    
### Fix Structural Errors
Structural errors are those that arise during measurement, data transfer, or other types of **"poor housekeeping."**
For instance, you can check for **typos** or **inconsistent capitalization**. This is mostly a concern for categorical features, and you can look at your bar plots to check.
Finally, check for **mislabeled classes**, i.e. separate classes that should really be the same.
  - e.g. If ’N/A’ and ’Not Applicable’ appear as two separate classes, you should combine them.
  - e.g. ’IT’ and ’information_technology’ should be a single class.

### Filter Unwanted Outliers
Linear regression is less robust to outliers than decision three models. So, in general. If you have a **legitimate** reason to remove outliers, it will help in your model's performance.
**IMPORTANT: outliers are innocent until proven guilty.** You should never remove an outlier just because it’s a "big number." That big number could be very informative for your model.
####  We can’t stress this enough:
you must have a good reason for removing an outlier, such as suspicious measurements that are unlikely to be real data.

### Handle Missing Data
**You cannot simply ignore missing values in your dataset.**
There is a practical reason behinf that: most algorithms do not accept missing values.
**Common sense** is not sensible her.
The two most commonly recommended ways of dealing with this type of problem are:
  1.  **Dropping** observations that have missing values.
      * This is really sub-optimal. Because when you **drop observations**, you **drop information.**
        * The fact that the value was missing may be informative in itself.
        * In the real world, you often need to make predictions on new data even if some of the features are missing!      
  2-  **Imputing** the missing values based on the observations.
      * This is also sub-optimal because because it mostly leats to a loss of information since you are not certain about the true exact value that is missing. 
        * **"Missingness"** is almost always informative itself, and you should tell your algorithm if a value was missing.
        * Even if you build a model to impute your values, you’re not adding any real information. **You’re just reinforcing the patterns already provided by other features.**

####  If missing a value is informative, and I should always tell my algorithm. What can I do?
  - **Missing categorical data:** In this case, the best is to label them as 'Missing'!
    - You're essentially adding a *new class* for **the feature**.
    - This **tells the algorithm** that the value was missing.
    - This also gets around the technical requirement for no missing values.
  - **Missing numeric data:** In this case, **flag and fill** the values.
    - **Flag the observation** with an indicator variable of missingness.
    - Then, **fill the original missing value** with 0 just to meet the technical requirement of no missing values.
   
#### *Doing data cleaning properly can really save you from a ton of headaches down the road, so please don't rush this step.*

##  Chapter 4 - Feature Engineering
Remember that of the process of doing *ML* this is the part on which *DS's* spend more time.
Feature engineering is about **creating new input features from your existing ones.**
You can remember it as:

*Data Cleaning = Subtraction*

*Data Engineering = Addition*

There are three reasons why this is one of the most valuable tasks a *DS* can do to improve their project:
  - You can **isolate and highlight key information**, which helps your algorithms "focus" on what’s important.
  - You can bring in your **own domain expertise.**
  - once you understand the "vocabulary" of feature engineering, you can bring in **other people’s domain expertise!**

Now we are going to introduce several **heuristics** that can help spark new ideas.

### Infuse Domain Knowledge
You can **engineer informative features** by tapping into your/others **expertise about the domain.**
Try to think of specific information you might want to **isolate.** Since here you have a lot of freedom, it is better if you have a certain **"domain knowledge"** of where you are stepping into. 
As you might suspect, "domain knowledge" is very broad and open-ended. At some point, you'll get stuck or exhaust your ideas.
That's where these next few steps come in. These are a few **specific heuristics** that can help spark more.

####  Create Interaction Features
This means to check if you can create any **interaction features that make sense.** These are combinations of two or more features.
By the way, in some contexts, "interaction terms" must be **products between two variables.** In our context, interaction features can be **products, sums, or differences between two features**
You can ask yourself:*"could I combine this information in any way that might be even more useful?"*
A simple example could be:
  * Let's say we already had a feature called 'num_schools', i.e. the number of schools within 5 miles of a property.
  * Let's say we also had the feature 'median_school', i.e. the median quality score of those schools.
  * However, we might suspect that what's really important is having many school options, but only if they are good.
  * Well, to capture that interaction, we could simple create a new feature 'school_score' = 'num_schools' x 'median_school' 

### Combine Sparse Classes
Since they can cause overfitting, it is good to consider grouping **sparse classes**.
  - There's no formal rule of how many each class needs.
  - It also depends on the size of your dataset and the number of other features you have.
  - As a rule of thumb, we recommend combining classes until each one has at least ~50 observations. As with any "rule" of thumb, use this as a guideline (not actually as a rule).
![SparseClasses](https://elitedatascience.com/wp-content/uploads/2017/06/grouping-sparse-classes-before.png)
![CombinedSparseClasses](https://elitedatascience.com/wp-content/uploads/2017/06/grouping-sparse-classes-after.png)

