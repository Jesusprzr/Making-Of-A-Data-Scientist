# Introduction
This documment is aimed to help us understand the big picture of how the realms of *Data Science* and *Machine Learning* fit together in the overall puzzle and to see how is the workflow of this process.

## Breaking It Down
Let's start by breaking the whole puzzle into peaces and then, diving a little deeper into each piece to grasp how the process occurs, and finally fit them together to make sense of the whole.

### What goes into a succeful model:
The process can be structured into a few steps. I won't enummerate it, because depending on the situation you might start by one or another and then jump back and forward between them. I'll just put first the steps that normally come first.
  
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
In applied *ML* you should first of all pick the right *__Ml* task__ for the job.
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
