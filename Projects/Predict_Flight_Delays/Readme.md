# Flight-Delays Prediction


# Link to the App & Presenation
* https://samarth2506.shinyapps.io/Flight_Delays_App/


* https://www.youtube.com/watch?v=nY2MWdjGLfw&feature=youtu.be&fbclid=IwAR33isCLLIdKZmuOjyvv3p_RjkJS2rd7N6rss6M6w_B4n_bNQiWL32N3ofY

# Introduction
Welcome to the app! We chose to predict flight delays because we love everything planes. The data is from Kaggle and includes data about domestic US flight carriers for 2015. The dataset has about 6 million records and 30 features. Only 20% of the data was used to train/test the models due to constraints on computation. The prediction is made for the day and airline of the user's choice.

# How to Use the App
The app broadly includes 3 sections or pages. The first 2 sections are interactive plots that answer interesting questions pertaining to flight delays and cancellations. The third section takes in a user input to make predictions if the flight is delayed or not. The user can choose the airline, month, day of the month and either Logistic Regression or Decision Tree as the Machine Learning model. Ensure the apply button is clicked after making your choice. After a few seconds, a table confirming your choice appears in the center of the page. You can see the accuracy and mode of the model's predictions to the right of the page. Finally, the app also handles errors if there are no flights by the selected airline on the chosen day.

# Models and Predictions
The app features 2 trained models (Logistic Regression(LR) and Decision Tree(DT)). The models were trained locally and saved. The .rds file of the model is loaded at runtime to make predictions. The LR achieves an accuracy of 75% while the DT model achieves 90% on average.

# Libraries Required 
The app requires the following libraries to run - plotly, ggplot2, stringr, leaflet, maps, geosphere, tidyverse, dplyr, shinyWidgets, tidyquant

Additionally, helper functions for creating the input table and finding the classification accuracy and prediction are stored in functions.R

To run the app locally, download and put the .csv and .rds files in your current directory.

# Creators
Anusha Patel (https://github.com/apatel3112) & Samarth Marudheri (https://github.com/Samarth2506) ; Feel free to get in touch if you have suggestions or questions on our project.

# Last Updated: May 14th 2020

# References:
    * https://www.kaggle.com/usdot/flight-delays
    * https://plotly.com/r/
    * https://rmarkdown.rstudio.com/flexdashboard/using.html
    * https://github.com/joon-im/specialized_price_prediction
