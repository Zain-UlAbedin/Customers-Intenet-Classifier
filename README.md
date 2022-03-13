# Data Scientist Salary Estimator
## Overview of the project
Created this web app which helps any businessess in classifying their customer reviews into 5 different categories. The data was gathered from amazon, to make the reviews
diverse so our model is generalized rather than specific to one domain, we gathered 10,000 reviews from different products on amazon. Afterwards, the reviews were labelled by me
and one other collegue, we went through all the 10,000 reviews to label them so our model performance doesn't get affected by poor data. The model trained was
* Naieve Bayes - achieved accuracy of 84%
* The algorithm was built with the help of only "numpy" module


## Resources
Clone this repository, and install following resources
- pip install sqllite
- pip install django==2,1.5
- pip install pickle
- pip install wordcloud (python version < 3.7)
- pip install numpy, pandas

Now you will be ready to go.



## Run the application
First you have to change the database authentication and type in settings.py (go to line 77) when that's done do the following
From terminal go to this folder on your local machine and type
**python manage.py runserver**

 now you will be good to go.
