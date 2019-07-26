# Chapter 2 - Descriptive Statistics
## Who was the best baseball player of all time?
Descriptive statistics are the numbers and calculations we use to **summarize** raw data.

There are two questions to address that have the similarity of being able to show us the strenghts and limitations of descriptive statistics:
1. What is happening to the economic health of America's middle class?
2. Who was the greatest baseball player of all times?

Derek Jeter had a career batting average of .313. That's a descriptive/summary statistic. <- This batting average is a gross simplification of Jeter's seventeen seasons. It is easy to understand, elegant in its simplicity AND limited in what it can tell us.

Let's change to a less trivial subject.

Ideally, we would like a simple but accurate measure of how the economic well-being of the typical american worker has been changing in recent years. A reasonable answer would be to calculate the per capita income over the course of a generation (which is approximately 30 years).

Per capita income is a simple average calculated dividing the total income divided by population size. It climbed from 7787$ in 1980 to 26487$ in 2010 (latest year from which government had data by the time of writing this book). This calculation is technically correct and totally incorrect in terms of the asked question:
1. He didn't took inflation in count, so these 7787 dollars from 1980 would be 19600 nowdays.
2. Average income in America is NOT equal to the income of the average American.
   * Average income in America takes the WHOLE income and divides it by the population but this isn't telling my nothing about who is earning how much of that income in none of both years.

Here we see that in both answers, the outcome is non-to-parcially correct. In both cases, what the author did is ask experts in both fields -> which statistics they would use to measure the related questions. 

Descriptive statistics are the way we have to encapsulate a raw array of data, i.e. There are 330 million residents in the U.S. A spreadsheet with the name of income of every american would contain the information we could ever want about the economic health of the country, but it tells us nothing at all for how unwieldy it is.

Descriptive statistics give us manageable and meaningful summary of the underlying phenomenon. BUT any simplification invites abuse.

There are 10 guys sitting on bar stools in a stablishment in Seattle, each ones income is 35K so the mean income is 35K. Then Bill Gates enters with a talking parrot perched on his shoulder and sits on the 11 bench. Bill's income is 1 billion (is not), so the mean income increases to about 91 million dollars <- **This is because the mean is really sensitive to outliers.** And this is the perfect explanation why we shouldn't use the per capita income to calculate the change in economic health in middle class americans.

We have another summary statistic that is not the mean and can help us to calculate **the middle of a distribution.** This statistic is called the median, which divides a distribution in the half of its observations (if observations are even, then our median is the midpoint calculated between the two middle observations).

With the median being our descriptive stat. Even with Warren Buffet comming in and sitting next to Bill, the median would still be 35K (it would be the guy sitting on the sixth stool).

A frequency distribution is as the name suggests, a way to see the frequency of each observation of the variable completely distributed through the entire axis (it has to sum to 1/100%).

We can also divide our distribution in quartiles (25% each) or even deciles (10% each). What about dividing the distribution into percentiles (1% each) it will be a lot more separated, detailed, and accurated. The benefit of these kinds of distributions is that they tell you where an observation lies **compared** with every other observation of the distribution. If I know that my song is in the 91 percentile on a test then I know I don't have to much to worry about his studies. It provides a ranking of my children's score relative to that of all other test takers.

    Absolute value = I shoot 83 for eighteen holes on golf <- Has value on its own, intrinsic meaning.
    Relative value = I place ninth in the golf tournament <- Has meaning only in comparison to something else.
 
 One of the most important, helpful, and common distributions in stats is the normal distribution A.K.A. Bell shape distribution. It is a distribution bell shaped with the mean at the center of it and with **standard deviations** which tells us how spreaded the distribution is, and how common a value is depending of how many standard devations it is away from the mean.

**This is the foundation on which much of statistics is build!**

    1 S.D. = 68.2% range = 34.1% each side
    2 S.D. = 95.4% range = 34.1% + 13.6% each side
    3 S.D. = 99.7% range = 34.1% + 13.6% + 2.3% each side
    mean =  µ
    Standard Deviation = σ


### There are comparisons that make sense to us because we recognize the scale of the units involved, for example:
- 1 inch difference isn't much difference when is related to comparing two persons heights <- WE KNOW the context of the scales involved
- 9 degrees is a significant temperature deviation in any climate in any year <- WE KNOW the context of the scales involved
    
### Now, if I give you a comparison in which you don't have any context:
- Granola cereal A contains 31 milligrams more sodium than granolla cerial B <- ONLY IF you know a lot about sodium and granola serving size, this won't be particularly informative
- My cousin Al earned 53,000$ less this year than last year <- Should we be worried about Al? Or is he a W.S. Millionaire and 53K is just what the water he drinks costs?
    
### The easiest way to give meaning to these comparisons is by using percentages:
- Granola Bar A has 50% more sodium than Granola Bar B
- Uncle Al’s income fell 47% last year
 
### Percentage changes could be potentially confusing and deceptive, for example:
- X store sells a dress by 100$
  * Assitant manager takes prices down a 25%
    * Dress value = 100$ - 25% = 75$
    * Assistant manager gets fired for hanging out drunk with Bill Gates in a pub
  * New Assitant comes in and takes prices up by 25%
    * Dress value = 75$ + 25% = 93.75$ NOT 100$
    
### A percentage change gives the value of some figure, relative to something else!
- I invest a some money on my roommate investment fund
  * I recieve a mail telling me that the firm's profit where 46% higher than the year before
    * Suppose that last year the firm earned 27 cents—essentially nothing.
    * This year the firm earned 39 cents—also essentially nothing.
  * Yet the company profits had a 46% increase compared to last year, even if that means that those profits aren't even a Starbucks cup of coffe.
  
### Now, percentage change != change in percentaje points
- Illinois personal income tax raised from 3% to 5%
  * Democrats (who engineered the increase) pointed out (correctly) that tax rate was increased by 2 percentage points
  * Republicans pointed out (correctly) that state income tax had been raised by 67 percent!
    * Democrats focus on absolute change in text rate
    * Republicans focus on percentage change in tax burden
- Both descriptions are correct, BUT the republicans one more accuratedly conveys the impact of the tax change

### Superpills
An index is a highly sensitive pill of the descriptive statistics that it encapsulates. Any minor change on the weight given to its components can change partially to totally the outcome.

This is why -> **indices range from useful but imperfect tools to complete charades.**
And not only indices, descriptive statistics in general can be misleading if not treated properly, so remember that descriptive statistics are a summary to help understand and describe things better, but also there is loss of information so don't relly totally on them, be skeptical and analyze what they are telling you about the subject and what they aren't taking in count about it.
