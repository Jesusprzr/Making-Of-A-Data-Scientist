# How does Netflix knows what movies I like?
It's all based on correlation. It recommends filmes that are similar to the other ones that i've liked, and also recommends films that are highly rated by other customers whose ratings are similar to mine.

Correlation measures the degree from which two phenomenas are related to one another. There is a positive correlation when two variables have a positive change in relation to the other; i.e. Height x Weight. On the other hand, there is a negative correlation when two variables have opposite changes in relation to the other; i.e. Exercise x Weight -> The more you exercise, the less you weight.

We can encapsulate the association between two variables in a single descriptive statistic -> The correlation coefficient.
- Negative correlation -> -1 No correlation -> 0 Positive correlation -> 1
- It has no unit attached to it, which means you can calculate the correlation between extremely different things.
- It collapses a complex mess of data measured in different units into a single, elegant descriptive statistic.

To calculate the correlation coefficient we do the following:
1. Calculate the mean and stardard deviation.
2. Calculate each observation's distance in standard devation from the mean.
3. Calculate the relationship of all observations measured by standard units.
   - If the distance from the mean of one variable tends to be broadly consistent with the distance from the mean of the other variable and in the same direction -> Then we would expect a strong positive correlation.
   - If the distance from the mean of one variable tends to be broadly consistent with the distance from the mean of the other variable but on the opposite direction -> Then we would expect a strong negative correlation.
   - If two variables do not tend to deviate from the mean in ani meaningful pattern -> Then we would expect little or no correlation.
   
**Correlation doesn't mean causation** remember that! i.e. Students with more tvs at their house have better SAT scores, but that doesn't mean that the more tvs you have the better your kid will be at school. The underlying causality of both could be that the parents education is great which allows them to have a greater income, buy more tvs, and educate better their kids. 
