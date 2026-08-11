import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("movie_success_dataset.csv")

# ==========================================
# ENCODE GENRE
# ==========================================

encoder = LabelEncoder()
df["genre"] = encoder.fit_transform(df["genre"])

# ==========================================
# FEATURES
# ==========================================

features = [
    "genre",
    "budget_crore",
    "marketing_crore",
    "actor_rating",
    "director_rating",
    "runtime_min"
]

X = df[features]
y = df["success"]

# ==========================================
# CHECK BOTH CLASSES
# ==========================================

print("\nSUCCESS = 1")
print("NOT SUCCESS = 0")

print("\nClass Distribution:")
print(y.value_counts())

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=10,
    stratify=y
)

# ==========================================
# DECISION TREE
# ==========================================

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    min_samples_leaf=2,
    random_state=10
)

model.fit(X_train, y_train)

# ==========================================
# ACCURACY
# ==========================================

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

# ==========================================
# SAVE
# ==========================================

joblib.dump(model, "movie_model.pkl")
joblib.dump(encoder, "genre_encoder.pkl")

print("\nModel created successfully!")