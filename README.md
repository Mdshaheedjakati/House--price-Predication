# House--price-Predication
Overview
This project aims to predict house prices in the USA based on various features such as average area income, house age, number of rooms, number of bedrooms, and other relevant details. The model is built using Linear Regression and is deployed as a Streamlit web application, allowing users to input house features and get an estimated price prediction.

Features
Predict house prices based on the following features:

Avg. Area Income: Average income in the area where the house is located.

Avg. Area House Age: Average age of houses in the area.

Avg. Area Number of Rooms: Average number of rooms in the houses in the area.

Avg. Area Number of Bedrooms: Average number of bedrooms in the houses in the area.

Area Population: Population of the area.

Built using Linear Regression.

Interactive web interface using Streamlit for easy user input.

Dataset: USA House Price Prediction dataset.





Dataset
The project uses the USA House Price Prediction dataset, which contains the following columns:

Avg. Area Income: The average income in the area.

Avg. Area House Age: The average age of houses in the area.

Avg. Area Number of Rooms: The average number of rooms in the houses in the area.

Avg. Area Number of Bedrooms: The average number of bedrooms in the houses in the area.

Area Population: The population of the area.

Price: The target variable, representing the house price.

Address: The location address of the property.

The dataset is stored in the data/ folder (USA_House_Price.csv).

Model Training
The model is trained using Linear Regression to predict house prices. The following steps are executed:

Load the dataset.

Preprocess the data (handle missing values, encode categorical variables, etc.).

Split the data into training and testing sets.

Train the model using Linear Regression.

Evaluate the model using metrics like Mean Squared Error (MSE) and R² score.




Web Application (Streamlit)
Once the model is trained, the project includes a simple Streamlit web app where users can input house features and get a predicted price.

To run the web app, use the following command:

bash
Copy
Edit
streamlit run app.py
This will launch the Streamlit app, where users can enter details such as:

Avg. Area Income

Avg. Area House Age

Avg. Area Number of Rooms

Avg. Area Number of Bedrooms

Area Population

And the app will return the predicted house price.

Evaluation Metrics
The model’s performance is evaluated using the following metrics:

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

R² score (Coefficient of determination)

Conclusion
This project demonstrates how to build a house price prediction model using Linear Regression and deploy it on a Streamlit web application for easy interaction. Further improvements can be made by:

Adding more advanced features like interaction with users for real-time data.

Improving data preprocessing or using more advanced machine learning models.

License
This project is licensed under the MIT License - see the LICENSE file for details.


