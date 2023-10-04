# Diamond Price Estimation Data Analysis

## Project Overview

In this data analysis project, I explored the diamond pricing using a dataset sourced from Kaggle. My primary objective was to create a robust model for estimating diamond prices based on a diverse set of attributes, including carat weight, cut quality, color, clarity, and physical dimensions. Below, I outline the key steps and insights from this analysis:

## Technologies and Tools Used

- **Programming Language:** Python 3.7
- **Libraries and Frameworks:** pandas, matplotlib, seaborn, scikit-learn, Flask
- **Data Source:** Kaggle (Diamonds dataset)
- **Machine Learning Models:** Linear Regression, Polynomial Regression, Random Forest Regression
- **Web Hosting Platform (for Flask API):** Local development environment

## Data Collection

- Acquired a comprehensive dataset containing details on thousands of diamonds, including carat weight, cut quality, color, clarity, and physical dimensions.
- The dataset was sourced from Kaggle, a reputable data platform known for its high-quality datasets.

## Data Analysis and Model Development

- Utilized Python and popular libraries such as pandas, matplotlib, seaborn, and scikit-learn for data analysis.
- Conducted exploratory data analysis (EDA) to gain insights into the distribution and relationships among different diamond attributes.
- Created data visualizations, including histograms and count plots, to visualize price distributions, cut quality frequencies, color variations, and clarity levels.
- Encoded categorical features like "cut," "color," and "clarity" into numerical values to prepare them for modeling.
- Developed predictive models to estimate diamond prices, including Linear Regression and Polynomial Regression.
- Evaluated model performance using metrics like Mean Squared Error (MSE), R-squared (R2), Mean Absolute Error (MAE), Median Absolute Error (MedAE), and Root Mean Squared Error (RMSE).

## Feature Engineering

- Created additional features to potentially enhance model performance.
- Experimented with polynomial features to capture potential non-linear relationships between carat weight and price.
- Analyzed the relationship between price and carat weight using scatter plots to visualize data patterns.

## Results

- The analysis provided insights into the distribution and relationships of various diamond attributes, aiding in understanding the factors influencing diamond prices.
- The models, including Linear Regression, Polynomial Regression, and Random Forest Regression, enabled the prediction of diamond prices with varying levels of accuracy.
- The Random Forest Regression model demonstrated the highest predictive accuracy, explaining approximately 98.14% of the variance in diamond prices.
- Feature importance analysis revealed that carat weight was the most influential attribute, followed by cut quality, clarity, and color, in determining diamond prices.

## Visulization Hightlights
## Visualization Highlights

Explore key visualizations that provide insights into the world of diamond pricing:

### Distribution of Diamond Prices

![Distribution of Diamond Prices](Distribution%20of%20Diamond%20Prices.png)

Gain a better understanding of how diamond prices are distributed within the dataset.

### Correlation Matrix

![Correlation Matrix](Correlation%20Matrix.png)

Discover the relationships between various attributes, such as carat weight, cut quality, and clarity, and their impact on diamond prices.

### Price vs. Carat

![Price vs. Carat](Price%20vs.%20Carat.png)

Visualize the relationship between diamond price and carat weight, a crucial factor in determining diamond value.

### Actual Prices vs. Predicted Prices (Random Forest)

![Actual Prices vs. Predicted Prices (Random Forest)](Actual%20Prices%20vs.%20Predicted%20Prices%20(Random%20Forest).png)

See how well the Random Forest Regression model predicts diamond prices compared to actual prices.

### Random Forest Feature Importance

![Random Forest Feature Importance](Random%20Forest%20Feature%20Importance.png)

Identify which attributes have the most influence on predicting diamond prices according to the Random Forest model.

These visualizations offer valuable insights into the world of diamonds and pricing dynamics, helping consumers and industry professionals make informed decisions.


## Conclusion

This analysis serves as a valuable resource for consumers, jewelers, and industry professionals seeking to make informed decisions regarding diamond purchases and pricing strategies. While the code and analysis did not explicitly address missing values, outliers, or data validation, it provided essential insights into the diamond market's pricing dynamics and predictive modeling techniques.

## Flask API Development

- Developed a Flask API to serve as the user interface for diamond price estimation.
- The API accepts input parameters such as carat weight, cut quality, color, clarity, and physical dimensions to predict diamond prices.
- Leveraged the Flask web framework in Python for building the API endpoints.
- Integrated a trained machine learning model into the API to make real-time predictions based on user inputs.
- Created a dedicated endpoint, `/predict`, where users can submit their input data for price estimation.
- Implemented error handling to ensure graceful handling of exceptions and errors during API interactions.

## User-Friendly Interface

- Designed a simple and intuitive user interface for users to interact with the API.
- Users can make HTTP POST requests to the `/predict` endpoint with their diamond attribute data in JSON format.
- The API responds with the estimated diamond price, providing a seamless user experience.
