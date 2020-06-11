

# Data Science/ML Concepts

* Recall = TP/Actual Positives ; Precision = TP/Predicted Positives ; If False Negatives have to be minimized, maximize Recall. If FP have to be minimized, maximize Precision. F1 is the harmonic mean of Precision and Recall.
* 2 examples where Recall/Precision should be maximized : 
    * Marketing Calls are expensive ->Minimize FP -> Maximize Precision
    * Marketing Calls are cheap -> Minimize FN -> Maximize Recall
* Relate Bayes Theorem to FPR and TPR? Bayes Theorem = TPR/(TPR + FPR)
* Type-1/ Type-2 Error : Type-1 is false positive (reject null hypothesis when true)means claiming something happened when its truly not while Type-2 (fail to reject null hypothesis when false)is false negative where something happened but you claim it has not.
* Fourier transform : Decompose generic functions to a super position of symmetric functions.
* Difference between Likelihood and Probability? Likelihood: Conditional probability of an event by knowing the probability of a success occurrence. Probability : Percentage of success occurrence.
* Generative v/s Discriminative Algorithms : Generative model learns the joint probability while the Discriminative model learns the conditional probability.
* Cross Validation for Time Series Data : Window method! Train : 1, Test : 2 ; Train : 1,2 Test:3; Train 1,2,3 Test 4 and so on.
* Kernel Trick: Involves Kernel functions that enable higher dimensional spaces without explicitly calculating the coordinates of the points within that dimension. Computes inner products between images of all pairs of data in a feature space.
* Hypothesis Testing : if p-value is lesser than significance level, then we reject the null hypothesis.
* Ensemble Methods:
    * Boosting : Different models built in series, reduces bias, points with errors are given higher weighting; 
        * Adaboost : Initialize all points with equal weights; Increase weights of misclassified points after first model; 
        * Gradient Boosting: Fit new model to the residual errors of the previous model
* R2 is the goodness of fit measure - ratio of reduction in variance due to model to total variance. -> 1 - (y - y^2)^2/(y - y_hat)^2
* Curse of Dimensionality : More data needed as dimension space grows due to sparsity
* More data is not always good : quality of data + model bias error high ; trade off with storage/computational cost
* Multicollinearity happens when 2 or more features are highly correlated. This will not affect predictions but affects interpretability.
* Feature selection: Regularization, build model to determine important features
* Making models more robust to outliers:
    * Regularization
    * Use tree based methods (non-parametric) versus parametric models that are more robust to outliers
    * Transform data (log) 
    * Remove anomalies if they are not important to prediction
* MAE v/s MSE : MSE penalizes more outliers but MAE harder to fit more variable data.
* Why is CLT important? Impossible to know about population - need to infer from samples. CLT directly answers calculating the population mean.
* Data Sampling: a statistical analysis technique used to select, manipulate and analyze a representative subset of data points to identify patterns and trends in the larger data set being examined. 
    * Probabilistic Methods: Simple Random, Stratified, Cluster, Multistage, Systematic
    * Non-probabilistic Methods: Convenience, Consecutive, purposive/judgemental, quota
* Statistical Inference: Effect of one variable differs among levels of another variable
* Nice def of ML: Extract patterns from data and reapply extracted patterns to new data.



* Algorithms:
    * Naive Bayes:
        * Objective Function : P(y | x_1, x_2, x_3) =[ p(x_1 | y) *  p(x_2 | y) *  p(x_3 | y) *  p(y) ] / p(x_1) * p(x_2) * p (x_3)
        * Prediction: argmax of objective function
        * If feature is continuous, its assumed to be sampled from a normal distribution.
        * Smoothing is done if a word not in train is encountered in test, making the product of probabilities zero.
    * Decision Trees:
        * Recursive splitting of the feature space to make predictions; if-else rules; Splits are formed on variables, the most important ones on top.
        * Calculate decrease in impurity measure before and after a split. Weighted avg/sum for each split. Pick the feature/value which gives highest information gain.
        * Impurity Measures:
            * ID3 algorithms uses entropy. Entropy = - sum(p_i * log(p_i)) ; Ranges from 0 - 1;
            * CART uses Gini Index, Gini Index = sum(p_i * (1 - p_i))**2 ; Ranges from 0 - 0.5;
    * Clustering: Always scale inputs to avoid giving variables with high values most weight
        * K- Means:
            * Pick k data points; Calculate distance of all other points to the k points; assign data points to closest k points; Calculate centroid; Repeat till convergence;
            * Pick best k from elbow curve of Within Group SSE v/s k.
            * Different initial points leads to different clusters.
            * K -Means ++ : Pick x as next centroid with probability proportion.
        * Hierarchical Clustering:
            * Initialize each point as a cluster
            * Calculate pair-wise distance between each cluster; Merge nearest two clusters; Terminate when all clusters merge in to one;
        * Recommendation Systems : Collaborative Filtering
            * Item based : If user likes item j, recommend items similar to item j; 
            * User based : if user u likes item j, recommend items liked by users similar to user u;


# Programming/Implementation/Algorithms

* A/B Testing : Create B version or new change version (Hypothesis). Send 50% of the traffic to B. Collect enough data to be statistically different. Using significance testing, if significant, incorporate the change on website.
* Differences between Linked List and Array : A Linked List is a series of objects with pointers that direct how to process them sequentially. An array is an ordered collection of objects. Array assumes all objects have the same size. An array has pre-defined or re-defined size while LL are dynamic arrays.
* Familiarize with technical tools in JD.
* Read about visualization libraries and relative advantages.
* **OOP concepts** :https://career.guru99.com/top-50-oops-interview-questions/
    * OOP - Program is considered a collection of objects and each object is an instance of a class.
    * Basic concepts of OOP:
        * Abstraction
        * Encapsulation: Wrapping of data and methods that work on data within one unit. Class is an example of encapsulation (Has member funcs, variables,etc.) Hidden data is restricted members of that class.
        * Inheritance: Child class inherits attributes and methods defined in the parent class. Super() function needed in init to call parent class methods.
        * Polymorphism: Assigning behavior of a child class that is different from parent and vice-versa (Overriding)
    * Class : Representation of a type of object. Blueprint describing  details of an object.
    * All classes in Python inherit object class. Methods provided by object class:
        * __new__() : Creates the object
        * __init__() :  Methods to initialize the instances of the object - Calls __init__()
        * __str__() : Return a formatted string representation of an object
    * Manipulators: Functions which can be used in conjunction with insertion(<<) and extraction(>>) operators like endl,setw.
    * Constructor : Method to initialize the state of an object ; Gets invoked at object creation; Should have same name as class and no return type.
    * Destructor: Method that is automatically called when object is destroyed.
    * Inline Function :  Technique used by compilers and instructs to insert complete body of function when its called in the source code.
    * Virtual Function: Member function defined in base class that can be over ridden by the derived class.
    * Friend Function: Allowed to access public/private or protected data in the same class.
    * Function Overloading: Same function can be called with different parameters (some will take the default value)
    * Operator Overloading: Giving extended meaning for operators beyond their predefined operational meaning.
    * Abstract Class : A class that has declaration but no implementation (Acts as blueprint for sub classes) (ABC in Python)
    * Ternary Operator: Conditional expressions that evaluate something based on condition being true or false
    * REST APIs in Python:
        * To expose databases to clients ; Representational State Transfer; Does not leverage as much bandwidth as SOAP - better fit for the internet;
        * HTTP request methods:
            * GET : Obtain information about a resource
            * POST : Create a new resource
            * PUT: Update a resource
            * DELETE: Delete a resource


* **Python Questions** : https://www.edureka.co/blog/interview-questions/python-interview-questions/#oops
    * Memory allocation (Python): Garbage collector already implemented by the Python Memory Manager.  This is done using pointers in C.
    * Memory can be stored in a stack - inside a function or method call (static) or heap (dynamic) - global level. For Python, objects are located in a private heap.
    * Best practices for memory allocation in Python:
        * Avoid slicing a list - new array must be created - try using function parameters or separate variables
        * Consider using for i in array instead of for i in range(len(array)) - avoid list indexing'
        * Avoid string concatenation (join or .format instead of '+')
        * Use iterators/generators
        * Use libraries when possible
    * Tuples are faster than lists
    * Python is an interpreted language (does not need need to be compiled like C) ; Dynamically typed
    * Python functions are first-class objects : They can be assigned to variables, returned and passed on to other functions
    * Python is capable of scripting but is considered a general-purpose programming language.
    * Python is an interpreted language because it is not at machine level code before runtime.
    * Namespace: Naming system to ensure names are unique and avoid naming conflicts.
    * Pythonpath: Environment variable which is looked up whenever a module is imported.
    * Lambda function : An anonymous function. Can have multiple parameters but only one statement.
    * self : self is an instance or an object of a class. It allows the user to access attributes and methods of a class. Binds attributes with given arguments.
    * Python Iterators:
        *  Objects which can be traversed through or iterated upon. Not reusable
        * Class contains __iter__ and __next__. if no more items to return, it should raise StopIteration exception.
    * Python Generators:
        * Functions that return an iterable set of items.
        * Iterates by using yield keyword from a function. Not reusable. Can be made resuable using the iter method.
        * Advantage is that it doesn't hold it in memory and it returns the iterator as and when needed.
    * Range v/s xrange : range returns a static list at run time and xrange returns xrange object which is memory efficient using the yield method.
    * Pickling and Unpickling : Converts all python objects to string representation and dumps to a file using dump function. Retrieving original objects from stored string rep is called unpickling.
    * *args and **kargs is used when we are not sure of how many arguments to a function. *args is for stored list or tuple while *kargs is used to pass values of a dictionary.
    * Monkey patch : Refers to dynamic modification of a class or module at run time.
    * Python supports multiple inheritance : A class can be derived from multiple parent classes.
    * Access specifiers in Python:
        * Public : All variables public by default. Accessible from any part of the program
        * Private : Single underscore; 
        * Protected : Double underscore; can be accessed only by the class.

* Common approaches to algorithms/Math puzzles

* Basic Probability Questions
    * p(A or B) = p(A) + p(B) - p(A and B) ; Disjoint if p(A and B) = 0 ;
    * P(A|B) = P(A,B)/P(B)
    * P(A|B) = P(B|A)*P(A)/P(B)

## Deploying ML Models

* Factors to consider while deploying ML models:
    * Latency requirements of the application
    * Number/kind of applications that will access model (database/CRM app)
    * Are predictions required for a single instance or a batch of instances?
    * Frequency of predictions required
* Challenges of AI in production: Outliers, Concept Drift, Bias (Directly/Indirectly), Privacy

* Ref:
    * https://mlinproduction.com/deploying-machine-learning-models/

## General Reading 

* Significant improvement in perception and automated judgement problems but none in predicting social outcomes.


## Case Studies/Company Specific

### General Case Studies

* How could you use GPS data from a car to determine the quality of a driver?
* Given accelerometer, altitude, and fuel usage data from a car, how would you determine the optimum acceleration pattern to drive over hills?
* Given position data of NBA players in a season’s games, how would you evaluate a basketball player’s defensive ability?
* How would you quantify the influence of a Twitter user?
    * Goes beyond simply number of followers. Examine how likely they will be retweeted, liked, links inside tweet will be clicked.
    * Important refinement is influence within a topic.
    * Page rank style algo for Twitter influence.
* Given location data of golf balls in games, how would construct a model that can advise golfers where to aim?
* You have 100 mathletes and 100 math problems. Each mathlete gets to choose 10 problems to solve. Given data on who got what problem correct, how would you rank the problems in terms of di culty
    * Problem difficulty obtained by sorting number of correct solutions. 
    * Skill level by Proportion of hard problems solved or total number solved.
    * Maximize likelihood of data to find hidden skills and difficulty levels.
* How would you design the people you may know feature on LinkedIn or Facebook?
* How would you predict who someone may want to send a Snapchat or Gmail to?
    * For each user, assign a score of how likely someone would send an email to.
    * Feature engg: no. of past emails, no. of responses, last time they exchanged an email, whether last email ends with a question mark, features about other users.
* How would you suggest to a franchise where to open a new store?
    * Master dataset with local demographic location:
        * Local income levels, traffic, population density, proximity to other businesses, weather;
        * Macro economic conditions : Unemployment, inflation, interest rates, etc.
        * Any data on locally owned franchises
    * Identify KPIs acceptable to the management on most important metrics : ROI, down payment, etc.
    * Run ML model to predict performance of each local candidate.
* You’re Uber and you want to design a heatmap to recommend to drivers where to wait for a passenger. How would you approach this?
    * Based on previous pickup location of passengers (time/day/month) - account for periodicity
    * Special events based on tweets/social media 

### Ellucian Specific
* Given a database of all previous alumni donations to your university, how would you predict which recent alumni are most likely to donate?
    * Supervised regression or classification. Features : Past donations (frequency and amount), industry, graduation year, major, salary, age.
* Boost student retention - Proactive than reactive
    * Could be financial issues, family matters or dissatisfaction in academic performance
    * Early detection of highly probable students and early intervention by university could help.
    * Collect demographical and academic information about student and run a classification algorithm. 
* Student Admissions:
    * College admissions can be made efficient and personalized.
    * Can get better insight in to eligibility of student and figure out better fits of students to universities.
    * Spot characteristics of successful students early
* Monitor student performance 
    * Personalized learning experience - Learning styles, abilities and challenges
* Better career services of students for find better fits to companies
* Identify the most interesting avenues of research for professors given all the literature available (NLP)

AI Limitations

* Should be seen as a tool to automative repetitive/administrative tasks. Should make better decisions with AI as a tool, not replace human’s critical thinking.
* Rule based subjects like math could be thought by AI but leverage by providing precision feedback. Cannot replace nuances.
* Data bias and ethical concerns. 

Product Metrics
* What would be good metrics of success for an advertising-driven consumer product? For service based?
    * Advertising : Page views, daily actives, Cost per Click, Click ads, Display ads
    * Services: Number of purchases, conversion rate
* What would be good metrics of success for a productivity tool? MOOC?
    * Productivity : No. Of premium subscriptions
    * MOOC : No. Of premium subscriptions, Completion rate


### _References_

* https://www.springboard.com/blog/data-science-interview-questions/



