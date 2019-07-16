library(SDSFoundations)
#Question 1
#How has mobile phone usage in Brazil changed since 1995?
wbd <- WorldBankData
BR <- wbd[wbd$Country.Code == 'BRA',]
View(BR)
?WorldBankData
BR95 <- BR[BR$year >= 1995,]
BRY <- BR95$year - 1995
BRM <- BR95$mobile.users/1000000
#Generate a scatterplot and fit a linear, exponential and logistic model to the data. 
#Which model best describes the increase in mobile users in Brazil since 1995?
plot(BRY, BRM)
linFit(BRY, BRM)
expFit(BRY, BRM)
logisticFit(BRY, BRM)
#What proportion of the variation in mobile users is explained by years since 1995 in the best‐fitting model?
R-squared =  0.99785
#predict the number of mobile users (in millions) in Brazil in 2025.
logisticFitPred(BRY, BRM, 30)

#Question 2
#Records at the Center for Disease Control show that the total number of flu cases in Spring, 2009 looked like this:
'
Date	    Day	  Flu Cases
April 27	0	    73
April 28	1	    105
April 29	2	    137
April 30	3	    257
May 1	    4	    367
May 2	    5	    658
May 3	    6	    898
May 4	    7	    1,085
May 5	    8	    1,490
May 6	    9	    1,893
'
'
Exponential Model	Logistic Growth Model
a = 76.64	        C = 3,273.31
b = 1.46	        a = 43.59
R-squared = 0.984	b = 1.57
                  R-squared = 0.996
'
#2Looking at the raw data, what is the rate of change in flu cases from April 30 to May 1? 
367/257
#Predict the number of cases of flu on Day 14 (when "Day" is equal to 14), using the exponential model.
Day <-c(0:9)
FluClases <-c(73,105,137,257,367,658,898,1085,1490,1893)
expFitPred(Day, FluClases, 14)
#Correct answer should be: 15325 <-My answer was 15466.356 Really close, it may be a problem with the raw data.
#The actual number of flu cases on Day 14 was 4,379. Find the residual of the exponential model prediction.
4379 - 15325 
#Using the logistic model, predict the total number of flu cases on Day 14.
logisticFitPred(Day, FluClases, 14)
4379-3036
#Correct answer should be: 1345 Almost the same value as for: 4379-3036 = 1343
#Seems like my approaches were correct. It is just a little difference.
#The cause of that difference should be the rounding in the raw data vs my data.

#Question 3
#Yellowstone National Park began a project to restore its native wolf population in the mid 1990's. 
#Below are the number of wolves soon after the start of the project:
'
Year	Years since Project Began	Number of Wolves
1996	1	                        25
1998	3	                        45
'
y <-c(1,3)
w <-c(25,45)
#Researchers fit a linear model to the wolf data. Using this model, 
#how many wolves were being added to the park each year? 
10
#According to their linear model, what was the size of the original wolf population when the project began?
15
#Another researcher assumed that the wolves would experience exponential growth because there were no predators. 
#He fit an exponential model to this data. What is the growth factor for this model? 
(45/25)*(1/3)
#Correct answer is 1.34
expFit(y,w)
b =  1.34164 
#What is the annual growth rate of these wolves each year, according to this model? 
0.34
#Assuming exponential growth, find the initial number of wolves when the project began. 
a = 18
#By 2002, there were 147 wolves in Yellowstone Park. Which model was determined to fit the data better?
expFitPred(y, w, 17)
#exp = 2754
linFitPred(y, w, 17)
#lin = 185
#So neither model appears to fit the data well.
linFitPred(w, y, 325) #<- You know that's not correct. CAN'T put the y variable on the x-axis on a regression.
linFit(y,w)
325 = 10(x) + 15
310/10 = x
x = 31

325 = 18.6339*1.34164^x
325/18.6339 = 1.34164^x
log(17.44133) = log(1.34164)x
x = log(17.44133)/log(1.34164)
9.7275 = 10 #But how the fuck would the exp model fit the data better than the linear one? 
#This just means one thing... Since the reproduction of the wolves is just beginning, exponential works.
#Then when there is more data the logistic model should be the one that fits the data better.

#Question 4
#4. A group of hedgehogs was released in the south‐Austin area. Each year, the size of the population was recorded. 
#Their population growth over time was modeled with a logistic growth curve. The model fit was 0.972.
#Here are the model parameters: 
C = 2000
a = 152.10
b = 2.17
#According to this model, what will be the maximum number of hedgehogs in South Austin?
2000
#What was the size of the hedgehog population when the growth rate began to slow down?
1000
#How many years had passed when the population growth rate began to slow down? (Round to 1 decimal place.)
1000 = 2000/(1 + 152.10*2.17^-t)
1000/2000 = (1 + 152.10*2.17^-t)
-0.5/152.10 = 2.17^-t
log(-0.003287311)/log(2.17) = -t
-7.380257 = -t
t = 7.380257
#Correct answer = 6.5 Gotta check the calculations.
#The hedgehogs were released in South Austin in 2001. 
#How many hedgehogs were living in South Austin by 2010, according to the model? 
x = 2000/(1 + 152.1*2.17^-9)
x = 1750
