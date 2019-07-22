Iteration = *repeating a set of tasks to achieve a result*

    Common pattern (in teaching) = load data -> preprocess data -> fit models -> make preductions
    Distinct cyclical nature = model level -> micro level -> macro level -> meta level -> human level

# The Model Level: Fitting Parameters
This is the first level where iteration plays a big role. Every model is defined by its parameters. i.e. a regression model is defined by its feature coefficients, a decision tree is defined by its branch locations, a neural network by the weights connecting its layers.

The iterative algorithm helps the machine learn the right values for all the model parameters

### Fitting parameters with Gradient Descent
Gradient Descent & its modified counterpart Stochastic G.D. = Shining successes

G.D. Is an iterative method for findinf the minimum of a fuction. Here, that function is commonly the **loss/cost function.** This function is a metric that quantifies the cost of wrong predictions.

The loss achieved is calculated by Gradient Descent by a model with a given set of parameters, and then it alters those parameters to reduce the loss. It keeps repeating this process until that loss can`t substantially be reduced further.
