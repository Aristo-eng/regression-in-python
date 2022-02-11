# Regression Implementation in Python
Basics of linear regression and its implementation in the Python programming language.

# Install required packages
- pip install sklearn
- pip install quandl
- pip install pandas

# Prediction of a stock price

* Use Quandl to get WIKI data set
* Data used are from Google stock market: WIKI/GOOGL

* The data set has features:
- Open
- High 
- Low
- Close
- ...
- ...
-  ...
- Adj. Volume

‘High’ denotes the highest value of the day.
‘Low’ denotes the lowest.
‘Open’ is the opening Price
and
‘Close’ is the closing for that Date. 

Now, sometimes close values are regulated by the companies.
The final value is the ‘Adj Close’ which is the same as ‘Close’ Value if the stock price is not regulated. 

# Regression and label selection


