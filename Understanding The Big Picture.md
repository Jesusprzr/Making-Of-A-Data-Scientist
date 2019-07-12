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

*>>> input = 'garbage'*

*>>> output = input*

*>>> print(output)*

*garbage*

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

###  Create Interaction Features
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
Now we have fewer unique classes, but with more observations on each.
Normally, a **quick overview** is enough to decide on whether or not combine certain classes together.

### Add Dummy Variables
Most *ML* algorithms can't handle categorical variables, especially text values.
What we do in this case is create **dummy variables**.
These are a set of **binary variables** that each represent a single class from a categorical feature.
With this, what you acheive is to pass the techniqual requirements for algorithms while equally representing our categorical features.
Like assigning a dummy variable (0 or 1) to each categorical variable in the example above.

### Remove Unused Features
Unused features are those that don’t make sense to pass into our machine learning algorithms. Examples include:
  * ID columns
  * Features that wouldn't be available at the time of prediction
  * Other text descriptions

**Redundant features** would typically be those that have been replaced by other features that you’ve added during feature engineering.

### ABT
When we have completed our *data cleaning* and our *feature engineering* we have just transformed our raw data into an **analytical base table (ABT).** This is called that way because here we will be **building our models on.**

**As a final tip:** You’ll often find that many of the features you engineer don’t improve your model. That’s fine because one highly predictive feature makes up for 10 duds.
The key is choosing machine learning algorithms that can **automatically select the best features among many options (built-in feature selection).**
This will allow you to **avoid overfitting** your model despite providing many input features.

##  Chapter 5 - Algorithm Selection
Most effective algorithms that leverage two specific, powerful mechanisms.
We are going straight into best practices, instead on looking at a big list of algorithms.

###  How To Pick Machine Learning Algorithms 
Now we are going to learn a few essential concepts. We will do this with five algos. The idea here is that by understanding these concepts (regularization, ensembling, automatic feature selection, etc.) we also get to understand **why** some algorithms tend to perform better thand others.
Since algorithms are implemented and eliminated based on **how they perform on the dataset and the problem**, we are going to focus on **intuition** and **practical benefits.**

### Why Linear Regression Is Flawed
Yes, it's easy to interpret and understand, but in practice the rarely perform well. 
Our goal is **NOT** to do a fancy report, but instead to build a model that can make accurate predictions.
In terms of accuracy on predicting, *simple linear regression* suffers from two major flaws:
  - Thend to **overfit** with many input features.
  - it **cannot** easily express non-linear relationships.
 
How can we address this flaws?
### Regularization In Machine Learning
The first flaw of linear models is that they are prone to be overfit with many input features.
Regularization is a technique used to **prevent overfitting** by **artificially penalizing model coefficients.**
  * It can discourage large coefficients (by dampening them).
  * It can also remove features entirely (by setting their coefficients to 0).
  * The "strength" of the penalty is tunable. (More on this tomorrow...)
  
### Regularized Regression Algos
We have three common types of regularized linear regression algos:
  - **Lasso regression:** **L**east **A**bsolute **S**hrinkage and **S**election **O**perator. 
    * Penalizes the **absolute size** of coefficients.
    * This leads to coefficients that are pushed towards practically zero.
    * It offers **automatic feature selection** because it can compeltely remove some features.
    * The **"strenght"** of the penalty should be tuned.
    * A strong penalty leads to more coefficients pushed to zero.
  - **Ridge Regression:** 
    * Penalizes the **square size** of the coefficients.
    * This leads to smallesr coefficients but not to zero.
    * So, it offers **feature shrinkage.**
    * the **"strength"** of the penalty should be tuned.
    * A stronger penalty leads to coefficients pushed closer to zero.
  - **Elastic-Net:** is a compromise between **Lasso** and **Ridge.**
    * Penalizes a mix of both **absolute and squared size.**
    * The **ratio** of the two penalty types should be tuned.
    * The overall strength should also be tuned.
  The type of penalty depends on the problem and dataset. We'll be going over it later on...
  
### Decision Tree Algos
Now we are going to adress the second major flaw of **S.L.R:**

Expressing non-linear relationships require other type of algorithm. This time the pick is a **tree of hierarchical branches.** It makes branches until reaches "leaves" that represent predictions.

A **reversal of correlation** is difficult for linear models to capture unless you explicitly add an interaction term (i.e. you can anticipate it ahead of time). Decision trees can capture this relationship naturally.

Unfortunately, decision threes have another major flaw: individual **unconstrained** decision trees are very prone to being overfit. So, **how do we use decision trees without overfitting?

### Tree Ensembles
**Ensembles** are *ML* methods used to combine predictions from multiple separate models. The two most common methods for ensembling are:
  - **Bagging:** attempts to reduce the change of overfitting complex models.
    * Trains a large number of **"strong" learners** in parallel.
    * A **strong learner** is a model that is relatively unconstrained.
    * Then. bagging combines all the **strong learners** together in order to *smooth out* their predictions. 
  - **Boosting:** attempts to improve the predictive flexibility of simple models. 
    * Trains a large number of **'weak' learners** in sequence.
    * A **weak learner** is a constrained model (i.e. you could limit the max depth of each decision tree).
    * Each one on the sequence centers on learning from the mistakes of the one before it.
    * Boosting then combines all the weak learners into a single strong learner.

Comparing them:
  - Both are ensemble methods.
  - Both approach the problem from opposite directions.
  - Bagging -> complex base models -> smooth out predictions.
  - Boosting -> simple base models -> boost their aggregate complexity.
 
General Ensembling = Bagging and Boosting

Decision Tree Ensembling = Random Forest and Boosted Trees

#### Random Forests
Does what bagging does. In addition there are two sources of randomness:
  1. Each tree is only allowed to choose from a random subset of features to split on (leading to feature selection).
  2. Each tree is only trained on a random subset of observations (a process called resampling).

On the pragmatical approach, random forests tend to perform really well right out of the box.
  - Often beat many other models that take up to weeks to develop.
  - They are the perfect **"swiss-army-knife"** algorithm that almost always gets good results.
  - They don’t have many complicated parameters to tune.

####  Boosted trees
Does what boosting does.

In practice, they tend to have the highest performance ceilings.
  - They often beat many other types of models after proper tuning.
  - They are more complicated to tune than random forests.

####  Key takeaway
The most effective algorithms typically offer a combination of regularization, automatic feature selection, ability to express nonlinear relationships, and/or ensembling. Those algorithms include:
  * Lasso regression
  * Ridge regression
  * Elastic-Net
  * Random forest
  * Boosted tree
 
## Chapter 6 - Model Training
Now we are going throught the model training process with some of the considered best practices on the field.

### How To Train Machine Learning Models
Remember that professional *DS's* spend most of their time on the stages that lead to this point:
  - Exploring the data
  - Cleaning the data
  - Engineering new features

This is because of our dear boolean: *Better Data > Fancier Algos*
Now, what we will do is learn how to set up the entire modeling process to **maximize performance** while **safeguarding against overfitting.** We will swap algorithms in and out and automatically find the best parameters for each one.

### Split Dataset 
A.K.A. Spending your data. Think of it as limited resources:
  - You **can** spend some of it to train your model (i.e. feed it to the algorithm). 
  - You **can** spend some of it to evaluate (test) your model.
  - But you **can’t** reuse the same data for both!

A model should be used to predict new unseen data. If you use the same data for both you could overfit the model without even knowing!
So, have separated sets of your data. One for training (fit and tune) and the other ("unseen") for testing your models.
  - You should always split your data before doing anything else.
  - This is the best way to get reliable estimates of your models’ performance.
  - After splitting your data, **don’t touch your test set** until you’re ready to choose your final model!

Comparing test Vs Training performance allows us to know if the model is overfitted. 

    >>> if model in training_data == well and if model in test == poor:
          Overfit = True
          
### What Are Hyperparameters
When we say 'tuninng models' we **specifically** mean 'tuning hyperparameters'.
There are two types of models:
  1.  **Model Parameters:** learned attributes that define individual models.
      * e.g. regression coefficients
      * e.g. decision tree split locations
      * They **CAN** be learned directly from the training data.
  2.  Hyperparameters:  express "higher-level" structural settings for algorithms.
      * e.g. strength of the penalty used in regularized regression
      * e.g. the number of trees to include in a random forest
      * **CAN'T** learn directly from the training data, that's why we tune them before fitting the model. 
      
### What Is Cross-Validation?
is a method for getting a reliable estimate of model performance using only your training data.
The most common way to cross-validate is called **10-fold cross-validation**, breaks your data into 10 equal folds, essentially creating 10 miniature train/test splits. 

These are the steps for 10-fold cross-validation:
  1. Split your data into 10 equal parts, or "folds".
  2. Train your model on 9 folds (e.g. the first 9 folds).
  3. Evaluate it on the 1 remaining **"hold-out"** fold.
  4. Perform steps (2) and (3) 10 times, each time holding out a different fold.
  5. Average the performance across all 10 **hold-out** folds.
     -  This average is your **cross-validated score**. This score is usually pretty reliable.
     
### Fit And Tune Models
Now that we have done all of this, we are ready to fit out model.
What we do now. is perform the entire cross-validation loop detailed above in each set of hyperparameter values we'd like to try. 
The high level pseudo code looks like this:
      
    for each algorithm (i.e. regularized regression, random forest, etc.):
      for each set of hyperparameter values to try:
        perform cross-validation using the training set.
        calculate cross-validation score.
        
At the end of this process you will have a cross-validation score for each set of hyperparameters, for each algorithm.

Then we pick the best set of hyperparameters within each algorithm:

    for each algorithm:
      keep the set of hyperparameter values with best cross-validated score.
      Re-train the algorithm on the entire training set (without cross-validation).

Like the hunger games, each district(algorithm) sends their candidates to the final selection, which is coming up next.

### Select Winning Model
For now, we have two remarkable achievements to point:
  - We have **one** best model for each algorithm that has been tuned throught cross-validation.
  - We've **only** used the training data so far.
  
Since we haven't used the **test dataset**, this will be the perfect scenario for our final hunger games. It will give us a reliable estimate of each model's performance. 
There are a variety of these, but in general for **performance metric** we will recommend:
  - {For **regression** tasks **Mean Squared Error(MSE)** or **Mean Absolute Error (MAE)**.} -> lower values are better
  - {For **classification** tasks **Area Under ROC Curve (AUROC)**.} -> Higher values are better
  
The overall process:
  - For each of your models, make predictions on your test set.
  - Calculate performance metrics using those predictions and the "ground truth" target variable from the test set.

####  Finally, use these questions to help you pick the winning model:
  * Which model had the best performance on the test set? (performance)
  * Does it perform well across various performance metrics? (robustness)
  * Did it also have (one of) the best cross-validated scores from the training set? (consistency)
  * Does it solve the original business problem? (win condition)

# Modern Machine Learning Algorithms
We will categorize our algorithms by *ML task*. This approach is focused on what's usually the end goal of all. Which is the expected result! It could be something like predicting an outcome or classifying our observations.

##  No Free Lunch Theorem
This is a theorem that states that no algorithm works best for every problem. This is specially relevant for supervised learning (i.e. predictive modeling). There are many factors at play to already state which algorithm is the best. This is why you should **try many different algirithms for your problem**. Of course, the algorithms you try should be appropiated for your problem, and that's when picking the right machine learning task comes in.

## Machine Learning Tasks
Here we'll cover the big three:
  1. Regression
  2. Classification
  3. Clustering
  
Another think to take in count:
  * We will not cover domain specific adaptations.
  * We will not cover every algorithm. What this list will give you is representative overview of successful contemporary algorithms for each task.

### 1 - Regression
Is the supervised learning task for modeling and predicting **continuos, numeric** variables.
These tasks are caracterized for having **labeled datasets that have a numeric target variable.**
So you have values of each observation that you can use to **supervise** your algorithm.

### 1.1 - (Regularized) Linear Regression
It attemps to fit a straight hyperplane or line (when have only two vars). It works well when there is a linear relationship between your variables.

In practice simple linear regression is simply outcassed by its regularized versions (LASSO, Ridge, and Elastic-Net).
Regularization is a technique utilized for penalizing large coefficients in order to avoid overfitting, and the strenght of the penalty should be tuned.
  * **Strenghts:** Is straightforward to understand and explain, and **can** be regularized to avoid overfitting. It also can be updated easily with new data using **stochastic gradient descent.**
  * **Weaknesses:** Performs poorly when there is non-linear relationship. It is **not** naturally flexible enough to capture more compplex patterns. Also adding the right interaction terms of polynomials can be tricky and time-consuming.
  * **Implementations:** Python/R
  
### 1.2 - Regression Trees (Ensembles)
A.K.A. Decision trees, a tree like branching structure that allows it to fit non-linear relationships.

Ensamble method, such as **Random Forests (RF)** and **Gradient Boosted Trees (GBM)**, combine predictions from many individual trees. **RF's** perform very well out of the box, while **GBM's** are harder to tune but tend to have **higher performance ceilings.**
  * **Strenghts:** They **can** learn non-linear relationships and are fairly **robust** to outliers. Ensembles perform really well in practice! They win lots of *ML* competitions (non-deep-learning).
  * **Weaknesses:** Unconstrained, individual trees are prone to overfitting because they **can keep branching** until they memorize the training data. <- This can ve alleviated by using **ensembles.**
  * **Implementations:** RF: Python/R GBM: Python/R
### 1.3 - Deep Learning

  * **Strenghts:**
  * **Weaknesses:**
  * **Implementations:**
  
  * **Strenghts:**
  * **Weaknesses:**
  * **Implementations:**
