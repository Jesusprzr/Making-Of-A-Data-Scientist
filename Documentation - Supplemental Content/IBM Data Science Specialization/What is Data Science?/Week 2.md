# Big Data & Data Mining
Here you use tools such as python, jupyter notebooks, hadoop, pandas (the python library), etc. To manipulate your data.

The Big Data definitions depends on you, there are two important attributes behind it:
- Size: Big Data is done with data in large database systems that are outside of the common data management tools.
- Usage: The techniques, models, patterns used in Big Data are pretty specific of it.

**Hadoop:**

The process:
The data is distributed through lots of servers (computers) running the same program, and this servers have each one a slice of the whole cluster of data. The server runs the program on it's individual part to finally send the results back, those are going to be sorted and redistributed to another process. The first process is the map process, and the second process is the reduce process.

These Big Data servers scale linearly.

Hadoop is an open source clone of the Google Big Data Architecture.

The tools of data sicence have been with us for decades, but the actual capability to create ML algorithms and combine them with our traditional tools (programming, databases, mathematics, statistics, probability, etc.) have open a new sea of possibilities for predicting outcomes, detecting patterns, engineering solutions, build optimization through data, etc.

Deep Learning is pretty new (less than 10 years old) and neural networks are pretty old (30+ years) but untill 2006 there wasn't much you could do with it. And now you have multi-layer neural networks that have massive improvements for what can be done in the field.

**Stablishing data mining goals:** Here you don't just identify the key questions and data to answer those questions. But also the cost and benefits of the excercise. <- The level of the accuracy expected fron the results is a benefit that influences the cost. From certain level of accuracy you don't gain much given the diminishin returns against the cost of the exercise. Everything to see of it is worth it the effort from not just an economical point of view. But also the effectiveness, efficiency and benefits of it.

**Selecting data:** This is critical, because the output depends a lot on the input (which is the data you collect). So you need to know the usability, availability, type, size, and frequency of collection of your data. This is critical for the cost of your data mining process and also the output of your project.

**Preprocessing data:** Selecting your data is the what, preprocessing is the filter of your input. On this part you spot irrelevant data that needs to be discarted, identify and deal with errors (i.e. Human errors when parsing on information). Check to ensure the integrity of the data. Develop a formal method to deal with missing data. Is a data cleaning phase. When data are missing in a systematic way, you need to determine if the impact of those missing values is relevant enough to damage the integrity of the output. If so, then you have to contemplate if there is an efficient way to fill this gap, collect data somewhere else, or even question  the viability of the project.



**Transforming data:** This is the how of your input. Here you transform your features (variables) so they can be processed more efficiently. This can be done through data reduction (reduce the number of attributes needed to explain the phenomena), variable transformation (to help explain the phenomena being studied), aggregation, etc. An example on data transformation could be to transform the numeric variable of income into a categorical one (low, medium, and high-income individuals) to capture the non-linearities of the underlying behaviors.

**Storing data:** It should be stored in a format that is conducive for data mining. The data storage scheme should facilitate efficiently the capacity of **reading** and **writing** data to the database. And it should also be stored on a **safe** and **private** place.

**Mining data:** Here you cover data analysis methods (parametric and non-parametric ones), also ML algorithms. Data visualization is a good starting point. Multidimensional views using advanced graphing capabilities of data mining software are pretty helpful on preliminary understanding the trends hidden in the dataset.

**Evaluating mining results:** This evaluation could include testing the predictive capabilities of the model on observed data to see the effectiveness and efficiency of the algorithm <- *in-sample forecast*. You should also share the results with the key stakeholders for feedback, which you incorporate in the next iterations to improve the process.

Data mining and evaluating the results are commonly an iterative process together.

# Deep Learning & Machine Learning
Neural networks are the computational approach on trying to mimic how the brain neurons actually work. Those networks can be trained with some inputs and outputs, then you try to transformate your neural networks until they get to your desired outputs.

Deep learning are neural networks on esteroids -> multiple layers of neural networks and lots of computing power. This takes an enourmus amount of matrix and linear algebra calculations <- GPU power! 

Some uses of D.L. are: speech recognition, people recognition, image recognition and classification, not only recognition or classification but also generation. It learns on its own the difference between different kinds of objects. Learns like a baby, starts slow and then with training does its task pretty accuratedly.

For D.L. You need a lot of computational power and linear algebra <- matrix related!

For becoming a Data Scientist you should know:
* Programing skills
* computational thinking
* Algebra
* Calculus
* Probability
* Statistics
* Databases

High-End D.S's work with hard computer science, statistics, and probability stuff.

**Learn by doing.**

**Understand your goal, lack of resilience and motivation is why the people who don't get it, don't get it.**

Data Scientist are mostly in companies that have data and/or research capabilities.

System recommendation is purely based on machine learning. Also classification, cluster analysis -> market basket analysis. Predictive analytics <- Decision trees, Bayesian Analysis, naive Bayes, etc.

You need to know not the details of each technique, but the trade-offs . <- over sampling, overfitting, underfitting.

IOT will be everywhere and will generate data.

# Regression
**Why tall parents don't have even taller children?**
This is the question that leaded to Sir Frances Galton studies in 1886, and that produced what we know today as *regression models.**

**Addressing real state price predictions:** The author had a thesis for his masters degree in which he developed hedonic price models for real state. Here found that larger homes sell for more than smaller homes (obvious conclusion) but also done it on a detailed and quantifiable way that shows the magnitude of each relationship. For example: an additional washroom adds more value to the house than an additional bedroom, the proximity to transport infrastructures result in higher housing proces, houses near freeways or highways sold for less than others, proximity to shopping centers had non-linear impacts on housing prices (< 2.5 Km sold for less; > 2.5 Km < 5 Km sold for more; > 5 Km sold for less than the ones around 2.5-5 Km). He also found that housing values in Toronto decline with distance from downtown.

## So, Why regress?
Here you have a few examples of what you can answer with hedonic regression models:
* How much more a house can sell for an additional bedroom?
* What's the impact of lot size on housing prices?
* Do homes with brick exterior sell for less than homes with stone exterior?
* How much does a finished basement contribute to the price of a housing unit?
* Do houses located near high-voltage power lines sell for more or less than the rest?
