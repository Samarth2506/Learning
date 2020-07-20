# Automated Trading Strategy with Reinforcement Learning

An automated trading strategy is developed using Reinforcement Learrning with an Actor Critic model. We propose Deep Learning models to capture sentiment and major events that affect the price of a stock. Signals from models along with a point estimate from a Time Series model are input as the state of the RL Model. The agent maps the state to one of three actions: sell, hold or buy to maximize returns. The approach yields an average profit of 14% on training data.

The _code_ folder contains all the relevant code used in the project. The _deliverables_ folder contains the paper and presentation of the project.

## Code

The code folder contains the following scripts:

**Data_Pre-Processing.ipynb:** The script crawls through the SEC and Wikipedia websites to scrape financial data and text from documents of interest.

**Data_Pre-Processing.ipynb:** The script pre-processes text (lower case conversion, stop words and punctuation removal, lemmatization) in documents of interest.

**Text_Classification_Deep_Learning.ipynb:** The script classifies if the stock will go up or down based on the text and timestamp of the 8-K document parsed.

**Time_Series_Forecasting.ipynb:** The script implememts a Time Series LSTM model to predict a point estimate of the stock price.

**nlp_signals_reinforcement_learning_for_trading.ipynb** : The script implements an actior-critic model to map the state of the agent to discrete actions for automated trading.

## Write-Up

Click [here](https://samarth2506.github.io/projects/first_project/) for an informal introduction to the project. 