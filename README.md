# 🎬 Movie Success Prediction Using Decision Tree

## 📌 Project Overview

This project predicts whether a movie will be **Successful** or **Not Successful** using a **Decision Tree Classification** machine learning algorithm.

The project uses movie-related information such as:

* 💰 Budget
* 📢 Marketing Budget
* ⭐ Rating
* ⏱️ Runtime
* 🌟 Star Power
* 🎭 Genre Score

A **Streamlit** web application is used as the frontend, where users can enter movie details and receive a prediction.

---

## 🎯 Objective

The main objective of this project is to build a machine learning model that can classify a movie into two categories:

```text
1 → Successful
0 → Not Successful
```

---

## 🧠 Machine Learning Algorithm

### Decision Tree Classifier

A Decision Tree works by creating a series of conditions based on the input features.

Example:

```text
                 Rating > 7?
                /           \
              YES            NO
              /               \
      Star Power > 6?     NOT SUCCESSFUL
        /       \
      YES       NO
      /          \
 SUCCESSFUL   NOT SUCCESSFUL
```

The tree learns these decision rules from the training dataset.

---

## 📊 Dataset

The dataset is stored in:

```text
movies.csv
```

### Features

| Feature     | Description                   |
| ----------- | ----------------------------- |
| Budget      | Movie production budget       |
| Marketing   | Marketing budget              |
| Rating      | Expected/average movie rating |
| Runtime     | Movie duration in minutes     |
| Star_Power  | Popularity of lead actors     |
| Genre_Score | Genre performance score       |
| Success     | Target variable               |

### Target

```text
1 = Successful
0 = Not Successful
```

---

## 📁 Project Structure

```text
Movie_Success_Prediction/
│
├── movies.csv
├── train.py
├── app.py
├── movie_model.pkl
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib

---

## 🔧 Installation

Install the required libraries:

```bash
pip install pandas scikit-learn streamlit joblib matplotlib
```

---

## 🚀 How to Run

### Step 1: Train the model

Open the terminal in the project folder and run:

```bash
python train.py
```

This will:

1. Load `movies.csv`
2. Separate input and target columns
3. Split the dataset into training and testing data
4. Train the Decision Tree model
5. Evaluate the model
6. Save the trained model as:

```text
movie_model.pkl
```

---

### Step 2: Start Streamlit

Run:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🎬 How to Predict

Enter the movie details in the Streamlit application.

Example:

```text
Budget       = 180
Marketing    = 90
Rating       = 8.5
Runtime      = 145
Star Power   = 9
Genre Score  = 9
```

Click:

```text
🔮 Predict Movie Success
```

The application will display:

```text
🎉 MOVIE IS SUCCESSFUL
```

or:

```text
❌ MOVIE IS NOT SUCCESSFUL
```

It can also display the prediction probability.

---

## 🔄 Project Workflow

```text
                  movies.csv
                      │
                      ▼
              Data Preprocessing
                      │
                      ▼
             Train/Test Split
                      │
                      ▼
          Decision Tree Classifier
                      │
                      ▼
               Model Evaluation
                      │
                      ▼
              movie_model.pkl
                      │
                      ▼
             Streamlit Application
                      │
                      ▼
             User Enters Movie Data
                      │
                      ▼
                  Prediction
                 /          \
                /            \
               ▼              ▼
          SUCCESSFUL    NOT SUCCESSFUL
```

---

## 📈 Model Evaluation

The model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report
* Confusion Matrix

Example:

```text
Accuracy: 85%

              precision    recall    f1-score

Not Successful     0.83      0.87       0.85
Successful         0.87      0.83       0.85
```

*The actual values depend on the dataset and train/test split.*

---

## 💡 Example Predictions

### Movie 1

```text
Budget       = 200
Marketing    = 100
Rating       = 8.8
Runtime      = 150
Star Power   = 10
Genre Score  = 9
```

Prediction:

```text
🎉 SUCCESSFUL
```

### Movie 2

```text
Budget       = 20
Marketing    = 5
Rating       = 4.8
Runtime      = 90
Star Power   = 2
Genre Score  = 2
```

Prediction:

```text
❌ NOT SUCCESSFUL
```

---

## ⚠️ Important Note

The model predicts based on patterns learned from the training dataset. It does **not guarantee the actual commercial success of a real movie**.

A balanced dataset containing sufficient examples of both:

```text
Successful
Not Successful
```

is important. If the dataset contains mostly successful movies, the model may predict **Successful** too frequently.

---

## 🔮 Future Improvements

Possible improvements include:

* Add actor/actress information
* Add director information
* Add production company
* Add release year
* Add number of screens
* Add social media popularity
* Add trailer views
* Add IMDb/critic ratings
* Use a real-world movie dataset
* Compare Decision Tree with Random Forest, XGBoost and Logistic Regression
* Add interactive decision-tree visualization
* Deploy the Streamlit application online

---

## 👨‍💻 Project Type

**Machine Learning Classification Project**

### Algorithm

```text
Decision Tree Classifier
```

### Frontend

```text
Streamlit
```

### Prediction

```text
Successful / Not Successful
```


