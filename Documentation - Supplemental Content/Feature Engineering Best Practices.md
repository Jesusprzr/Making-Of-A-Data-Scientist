# Feature Engineering Best Practices
"Coming up with features is difficult, time-consuming, requires expert knowledge. “Applied machine learning” is basically feature engineering." ~ Andrew Ng

Through feature engineering, you can isolate key information, highlight patterns, and bring in domain expertise.

### What is feature engineering?
It is creating new features from your existing ones to improve model performance.

### What is not feature engineering?
- Initial data collection.
- (Creating the target variable) <- Data Exploration or At the moment of ilumination.
- (Removing duplicates, handling missing values, fixing mislabeled classes) <- Data Cleaning.
- Scaling or normalization (that's after you have your ABT. When you are cross-validating).
- Feature selection or PCA (that's also part of the cross-validation process).

Now let's get to what matters, feature engineering best practices: 

## Indicator Variables
Here you use indicator variables to isolate key information.

Not always an algirithm will learn the key information on its own. So you can help your algorithm "focus" on what's important by highlighting it beforehand.
- **Indicator variable from threshold:** You are studying age alcohol preference, just by knowing that, you can *age>=21* (distinguish subjects who where over legal drinking age).
- **Indicator variable from multiple features:** You are predicting real state prices, you have *nºbethroom & nºbathroom* variables. If houses with 2 bethrooms and 2 bathrooms command a premium as rental properties, you can create an indicator variable to flag them.
- **Indicator variable for special eveets:** You're modeling W sales for an e-commerce site. You can create two indicator variables for the weeks of Black Friday and Christmast.
- **Indicator variable for groups/classes:** You're analyzing website conversions, you have a feature *traffic_source*. You can create an indicator varriable *paid_traffic* by flagging observations with traffic source values of  "Facebook Ads" or "Google Adwords".

## Interaction Features
This involves highlighting interactions between 2+ variables.

Sometimes "the sum is greater than its parts" and some features can be combined to provide more information than they would do individually. Specifically, you should look for opportunities to take the sum, difference, product, or quiotent of multiple features **(pure arithmetics)**.

**DANGER: Automated loops to create interactions to all of your features will lead to feature explosion**

- **Sum of two features:** You want to predict revenue based on preliminary sales data. You have features *sales_blue_pens** & *sales_black_pens*. You could easily sum those variables if you are only interested in overall *sales_pens*.
- **Difference between two features**: You have features *house_build_date* & *house_purchase_date*. You can take their difference to create the feature *house_age_at_purchase*.
- **Product of two features:** You're runing a pricing test, you have feature *price* and indicator variable *conversion*. You can take their product to create the feature *earnings*. 
- **Quotient of two features:** You have a dataset of marketing campaigns with features *n_clicks* and *n_impressions*. You can divide clicks by impressions to create *click_through_rate*, which allows you to compare across campaigns of different volume.

## Feature Representation
Is basically representing you data on a different way, maybe because it didn't come on an ideal format, or the format may be good but you find a greater way to represent the data.
- **Date and time features:** You have feature *purchase_datetime*. It might be more useful if you extract *purchase_day_of_week* and *purchase_our_of_day*. You could also aggregate observation to create features such as *purchases_over_last_30_days*.
- **Numeric to categorical mappings:** feature *years_in_school*. You might create new feature *grade* with classes such as *Elementary School*, *Mid School*, and *highh School*.
- **Grouping sparse classes:** this is basically grouping the low sample count classes. You can try grouping *similar_classes* into one and then *others* (classes with no similarity) into one.
- **Creating dummy variables:** Depending on your *ML* implementation you may need to transform categorical variables into dummy ones (i.e. north, south, east, west).This is always done **after** grouping sparse classes.

## External Data
This is commonly underused and hironically could lead to some of the biggest breakthrought in performance. 

Quantitative hedge funds perform research by layering together different streams of data.

Some examples of benefit from bringing external data:
- **Time series data:** Some form of *date* to layer in features from anotehr dataset.
- **External API's:** An example is the *Microsoft Computer Vision* API, that can return the nº of faces from an image.
- **Geocoding:** You have *street_adress*, *City*, and *State*. You can geocode them into *latitude* and *longitude*. This will allow you to calculate features such as local demographics (e.g. *median_income_Whithin_2_miles* with the help of another dataset.
- **Other sources of the same data:** like the hedge fund example. Each source can provide information that the others don’t track. Plus, any differences between the datasets could be informative (e.g. bot traffic that one source ignores while another source keeps).

## Error Analysis (post-modeling)
This one is performed **after** training your first model. It refers to analyzing the misclassified or high error observations from your model and deciding on your next steps for improvement.

Possible next steps could include: collecting more data, splitting the problem apart, or engineering new features that adress the errors. To do this you need to understand **why** your model missed its mark. Here's how:
- **Start with larger errors:** We recommend starting with those errors that had larger error scores (because we won't have time to scrutinize every observation). Look for patterns that you can formalize into new features.
- **Segment by classes:** Segment your observations and compare the average error within each segment.You can try creating indicator variables for the segments with highest errors.
- **Unsupervised clustering:** You can run an unsupervised clusterin on misclassified observations. We don't recommend blindly using those clusters as new features, but they can make it easier to spot patterns. Here the **goal** is to understand **why** observations were misclassified.
- **ask collegues of domain experts:** This is a great complement to any of the other three techniques. Asking a domain expert is especially useful if you’ve identified a pattern of poor performance (e.g. through segmentations) but don’t yet understand why.

## Conclusion
Remember these guidelines as you experiment on your own:

**Good features to engineer...**
- Can be computed for future observations.
- Are usually intuitive to explain.
- Are informed by domain knowledge or exploratory analysis.
- Must have the potential to be predictive. Don't just create features for the sake of it.
- **Never touch the target variable.** This is like cheating and will give you misleading results.

