Iteration = *repeating a set of tasks to achieve a result*

    Common pattern (in teaching) = load data -> preprocess data -> fit models -> make preductions
    Distinct cyclical nature = (((((model level) micro level) macro level) meta level) human level)

# The Model Level: Fitting Parameters
This is the first level where iteration plays a big role. Every model is defined by its parameters. i.e. a regression model is defined by its feature coefficients, a decision tree is defined by its branch locations, a neural network by the weights connecting its layers.

The iterative algorithm helps the machine learn the right values for all the model parameters

### Fitting parameters with Gradient Descent
G.D. Is an iterative method for finding the minimum of a fuction. Here, that function is commonly the **loss/cost function.** This function is a metric that quantifies the cost of wrong predictions.

The loss achieved is calculated by Gradient Descent by a model with a given set of parameters, and then it alters those parameters to reduce the loss. It keeps repeating this process until that loss can't substantially be reduced further.

That final set of parameters that minimize the loss defines our fitted model.

### Gradient Descent intuition
- Imagine a mountain range with hills and valleys (loss function).
- Each location (parameter set) on the mountain has an altitude (loss).
- Drop a ball somewhere on a mountain (initialization).
- The ball will roll in the stepest direction (the gradient).
- It continues to roll (iteration) until it gets stuck in a valley (local minimum).
- Ideally you want to find the lowest possible valley (global minimum).
- You can prevent the ball from getting stop in a local minima. i.e. initializing multiple balls, giving it more momentum so it can traverse small hills, etc.
- If the mountain terrain is shaped like a bowl (convex function), the ball is garantied to reach the global minima (lowest point).

In practice with libraries like Scikit-Learn you won't need to implement G.D. From scratch.

# The Micro Level: Tuning Hyperparameters
The micro level is also known as the general model or model family.

Model family = broad category of models with customizable structures (i.e. logistic regression, decision trees, and neural networks are different model families). Each family has a set of structural choices (i.e. The depth of the tree, pruning threshold, or even the splitting criteria).

**Those structural choices are called hyperparameters.**

### Why hyperparameters are special
These are high level parameters that cannot be learned directly from the data using G.D. Or other optimization algorithms. They describe structural information about a model that **must** be decided before fitting model parameters.

When people says that they are going to train a *logistic regression model*, they really mean a two stage process:
1. Decide hyperparameters for the model family. i.e. Should the model have  L1 or L2 penalty to prevent overfitting?
2. Fit the model parameters to the data. i.e. What are the model coefficients that minimize the loss function?

As you see in the steps hierarchy, in order to fit model parameters using G.D. The user must first set the hyperparameters from model family. **How can we find the best hyperparameters for the model family?**

### Tuning hyperparameters with cross-validation
**Cross-validation works in a lot of scenarios.**

In this context, it is an iterative method for evaluating the performance of models built with a given set of hyperparameters.

With cross-validation you can fit and evaluate your models with different sets of model hyperparameters using only your training data, and save your test data (the untouched one) for your final model selection.

[Here is a video explaining K-fold cross validation (the most popular form)](https://www.youtube.com/watch?v=TIgfjmp-4BA)

Let's remember the cross-validation stepts, in this case using 10-fold cross-validation:
1. Split your training data in 10 equal parts (folds).
2. From all sets of hyperparameters you wish to consider, choose a set.
3. Train your model with that set of hyperparameters on the first 9 folds.
4. Evaluate it on the hold-out fold.
5. Repeat steps 3 and 4 with that exact same set of hyperparameters, each time holding a different fold out.
6. Aggregate the performance across all 10 folds. <- This becomes your performance metric for the set of hyperparameters.
7. Repeat steps from 2 to 6 for all sets of hyperparameters you wish to consider.

Here's how that look in pseudocode:
    
        all_folds = split_into_k_parts(all_training_data)
        
        for set_p in hyperparameters_sets:
            model = InstanceFromModelFamily()
            
            for fold_k in all_folds:
                training_folds = all_folds besides fold_k
                fit_model on training_folds using set_p
                fold_K_performance = evaluate model on fold_k
                
            set_p_performance = average all k fold_performances for set_p
        
        select set from hyperparameters_sets with best set_p_performance

# The Macro Level: Solving Your Problem
Often, the first model you build for a problem won't be the best possible, even if you tune it perfectly with cross-validation. This is because fitting model parameters and tuning hyperparameters are only two parts of the entire problem-solving workflow.

There are more iterative techniques that you can leverage to find the best performing solution. The next two tecniques are low-hanging fruits for improving your predictive performance.

### Trying different model families
Remember the **No Free Lunch Theorem:** There is no one model family that works best for every problem.

Depending on a variety of factors such as the type of data, problem domain, sparsity of data, and even the amount of data you've collected, different model families will perform better. This is why, one of the easiest ways of improving your solution for a given problem is to try different model families. This level of iteration sits nicely above the previous level.

Here is how that looks in pseudocode:

        training_data, test_data = randomly_split(all_data)
        
        list_of_families = logistic regression,
                           decision tree,
                           SVM,
                           neural network, etc...
                           
        for model_family in list_of_families:
            best_model = tuned with cross-validation on training_data
            
        evaluate best_model from each_model_family on test_data
        select final model

Notice how we are doign a neasted iteration with the cross-validation process inside this one. This is a really effective way of solving problems with ML.

### Ensembling models
This is another way of improving your solution in which you combine multiple models into an **ensemble**. This is a direct extension of the iterative process needed to fit those models.

A common form of ensembling is simply averaging the predictions from your multiple models. There are more advanced ways to combine your models, but the iteration needed to fit multiple models is the same.

This combined prediction will often see a small improvement in performance over any of the individual models. Here is the pseudocode for building a simple ensemble model:

        training_data, test_data = randomly_split(all_data)
        
        list_of_families = logistic regression,
                           decision tree,
                           SVM,
                           neural network, etc...
        
        for moddel_family in list_of_families:
            best_model = tuned with cross-validation on traning_data
            
        average predictions by best_model from each model_family
        ... profit! (often)
        
The process is almost exactly the same as the previous technique.

Since both are almost equal, this means that you can easily double-up in those two techniques. First, you can build the best model from a variety of different models. Then you can ensemble them.
Finally, you can evaluate the individual model and the ensemble model on the same test set.

**As a final word of caution:** ALWAYS keep an untainted test set to select your final model. It is really recommended to split your data into train and test sets from the very beggining of the modeling process. Don't touch the test set until the very end.

# The Meta Level: Improving Your Data
As we already know -> Better Data > Better Algorithms

But that **doesn't** mean more data > better algorithms. Yes, better data often implies more data, but it also implies cleaner data, mroe relevant data, and better features engineered from the data.

Improving your data is another iterative process since you will find it pretty damn hard to get your data completely right from the start. 

Maybe there is some key features you didn't think to collect. Maybe you didn't collect enough data. Maybe you misunderstood one of the columns in the dataset and need to circle back with a collegue to explain it.

A great machine learning practitioner always keep an open mind towards continuously improving the dataset.

### Collecting better data
This ability is something that is developed with time, experience, and more domain expertise. Because this is more of a holistic/intuitive reasoning that you develop as you practice and dig more into the field you are working on.

Another element is the overall cleanliness of the data. This means having less missing data, lower measurement error, and doing your best to replace proxy metrics with primary metrics.

The following are questions that if you ask yourself can spark ideas for improving your data:
- Are you collecting all the features that you need?
- Can you clean the data better?
- Can you reduce measurement error?
- Are there outliers that can be removed?
- Is it cheap to collect more data?
