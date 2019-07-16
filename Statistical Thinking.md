#   Book procedures
The organization of this book follows the same process that the author uses when he starts working with datasets:
1.  Importing and cleaning
2.  Single variable explorations
3.  Pair-wise explorations
4.  Multivariate Analysis
5.  Estimation and hypothesis testing
6.  Visualization

The book presents a computational approach instead of a mathematical one:
-   Most ideas are presented in python code, rather than mathematical notation.
-   Each chapter includes exercises for effective learning.
-   Some exercises include experiments to test statistical behavior.
-   Mathematically hard to grasp ideas = easy to understand by simulation (So True!)
-   Since the book is based on python, readers can import data from almost any source.

The book presents a project based approach, in which we will be working on a case study that runs through all the chapters using data from two sources:
1.  The National Survey of Family Growth (NSFG)
2.  The Behavioral Risk Factor Surveillance System (BRFSS)
    
#   Chapter 1 - Exploratory Data Analysis

Our thesis, is that even **under uncertainty** we can **answer questions** and **guide decisions** combining **data** with **practical methods.**

The question that we will be answering during this process is the following: **Do first babies tend to arrive late?**

##  Approach
We will be answering it from an **statistical approach:**
1.  Data Collection
2.  Descriptive Statistics
3.  Exploratory Data Analysis
4.  Estimation
5.  Hypothesis Testing

##  Understanding the design of the study
In order to use the data effectively, we have to understand the design of the study:
-   Is a cross-sectional study
-   Has been conducted 7 times, we will use data from cycle 6 (6 time): 01/2002 - 03/2003
-   U.S. Citizens (age 15-44) = respodents; The subset of data from which we will collect information = sample. 
-   Cross selectional studies are representative, but the ideal of equal participation chance is hard to achieve. This is **not** the case of the NSFG, our data is **deliverately oversampled**, which means that each groups is large enough to draw valid statistical inferences.
-   Oversampling drawback = not easy to draw conclusion about general population based on statistics from the survey.
-   It is **important** to work with the [documentation of the experiment](https://www.cdc.gov/nchs/nsfg/index.htm) while working with this data.

##  Importing data
Code available on [Git Hub](https://github.com/AllenDowney/ThinkStats2).

2002FemPreg.dat.gz = Pregnancy data from cycle 6
-   a gzip-compressed data file in plain text (ASCII)
-    fixed width columns
-   Each line in the file is a record that contains data about one pregnancy
    
File format **documented** in -> 2002FemPreg.dct
-   .dct = Stata dictionary file
    -   Stata = Statistical Software System
    -   Dictionary (in this context) =  list of variable names, types, and indices that identify where in each line to find each variable.
    
Run *nsfg.py* in order to be able to open dct files. It contains the *thinkstats2.py* module which contains the functions necessary to read the stata dictionary.
        
##  Dataframes
    
