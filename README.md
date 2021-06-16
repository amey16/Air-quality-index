# Air-quality-index-predictor
Predicting the air quality index of delhi-safdarjang in this case(can do for any state) using different regression techniques and deploying the best one using heroku :smile:
# Repository structure  
- :star: **Data folder**
     - **html-data**
          - contains the html files of data extracted from [climate_info](https://en.tutiempo.net/climate/0%7B%7D-%7B%7D/ws-421820.html) :v:
          - you can explore the same for different countries/states/years/months :wink:
          - main features for traning
          
Feature name | Feature meaning
:---: | :---:
  T | Average annual temperature
TM	| Annual average maximum temperature
Tm	| Average annual minimum temperature
PP	| Rain or snow precipitation total annual
V	  | Annual average wind speed
RA  |	Number of days with rain
SN  |	Number of days with snow
TS  |	Number of days with storm
FG  |	Number of foggy days
TN  |	Number of days with tornado
GR  | Number of days with hail

-
     - **aqi** :confused:
          - data from a paid third party API containing air quality index allocated by time and date
          - could only manage to get data of year 2013,2014,2015,2016,2018 :neutral_face:
     - **Real-Data** :unamused:
          - combined data of features and air quality index made in extract_combine.py :stuck_out_tongue_winking_eye:
          - has a complete dataset of all the years from 2013-2016 named Real_combined.csv 
          
- :star: **Data extraction/Data collection**
     - datacollection.py :smile:
          - code for extracting html files of climate based features from [climate_info](https://en.tutiempo.net/climate/0%7B%7D-%7B%7D/ws-421820.html)
          - data extracted for years 1997-2021 for delhi- palam and delhi-safdarjang
          - html files dtored in folders named dl-sf and sl-p (path - Data/html-data/{df-sf or sl-p})
     - extract_combine.py :bowtie:
          - web scraping of html files in html-data using ***Beautifulsoap***
          - feature engineering /removing unwanted features
          - combining the web scraped table from html-data and data from aqi to make combined data and store them as csv files
     - plotapi.py :smile:
          - combing the data by a particular day (originally seperated by each hour of a day)
          - plotting the average air quality index of each day using ***matplotlib***
          
- :star: glimpse of first 20 rows of final dataset
     - ![image](https://user-images.githubusercontent.com/51751926/122136041-58163f00-ce5f-11eb-8299-854e328dc134.png)
- :star: **Machine learning techniques**
     - Linear regression.ipynb :key:
          - data visualization using pairplots , ***heat maps*** and ***correlation matrix***
                - ![image](https://user-images.githubusercontent.com/51751926/122136617-76306f00-ce60-11eb-9eed-f05d33c2a907.png)
          - feature importance using ExtraTreesRegressor
          - Linear regression model implementaion
          - evaluation metrics (mae, mse, rmse)
     - Ridge-Lasso regression.ipynb :key:
          - Implementation of ridge and lasso regression
          - same steps as done in linear regression implementaion 
     - Decision_tree&Random_forest-regressor.ipynb :key:
          - implementing decision trees and random forest regression techniques
          - visualiaztion of decision tree using ***pydotplus*** and ***export_graphviz*** libraries
          - hyper-parameter tuning
          - model evaluation same as done in lnear regression using ***sklearn.metrics***
     - XGBoost_regressor.ipynb :key:
          - implementing XGBoost boosting technique to predict air quality index
          - least RMSE after hyper- parameter tuning 
          - choosed for deployment
     - ANN&KNN.ipynb :key:
          - devloped a neural network model using different hyper parameters 
          - implemented knn with hyper parameter tuning
          - model evaluation using mae , mse ,rmse
     - .pkl files :key:
          -pickle files for each regression technique used to preserve the model object
          
- :star: **front-end /flask app**
     - **static and templates folder** :moneybag:
          - staitc contains the styles.css for web page beautification
          - templates contains home.html and results.html for predicting air quality indexes of year 2018 for delhi-safdarjang
     - app.py :moneybag:
          - python flask app to show the working of webpage
     - Procfile,requirements.txt :moneybag:
          - files neccessory to deploy the app on heroku 
          - ***app link*** - [app](https://aqi-predict1.herokuapp.com/)
     - ![image](https://user-images.githubusercontent.com/51751926/122184743-24acd200-ceaa-11eb-9b2e-4344f07227f0.png)
     - ![image](https://user-images.githubusercontent.com/51751926/122184837-3e4e1980-ceaa-11eb-9604-769bf8a07e39.png)
