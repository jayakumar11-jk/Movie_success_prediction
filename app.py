import streamlit as st
import pandas as pd
import joblib

# ==========================================
# PAGE
# ==========================================

st.set_page_config(
    page_title="Movie Success Prediction",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("movie_model.pkl")
encoder = joblib.load("genre_encoder.pkl")

# ==========================================
# TITLE
# ==========================================

st.title("🎬 Movie Success Prediction")
st.write("Decision Tree Machine Learning Project")

st.divider()

# ==========================================
# INPUT
# ==========================================

st.sidebar.header("Enter Movie Details")

movie_name = st.sidebar.text_input(
    "Movie Name",
    "My Movie"
)

genre = st.sidebar.selectbox(
    "Genre",
    encoder.classes_.tolist()
)

budget = st.sidebar.number_input(
    "Budget (₹ Crore)",
    min_value=1.0,
    max_value=500.0,
    value=100.0,
    step=5.0
)

marketing = st.sidebar.number_input(
    "Marketing Budget (₹ Crore)",
    min_value=1.0,
    max_value=500.0,
    value=100.0,
    step=5.0
)

actor_rating = st.sidebar.slider(
    "Actor Rating",
    0.0,
    10.0,
    7.0,
    0.1
)

director_rating = st.sidebar.slider(
    "Director Rating",
    0.0,
    10.0,
    7.0,
    0.1
)

runtime = st.sidebar.slider(
    "Runtime",
    60,
    240,
    140
)

# ==========================================
# PREDICT
# ==========================================

if st.sidebar.button("🔮 PREDICT"):

    # Encode genre
    genre_value = encoder.transform([genre])[0]

    # Input dataframe
    input_data = pd.DataFrame({
        "genre": [genre_value],
        "budget_crore": [budget],
        "marketing_crore": [marketing],
        "actor_rating": [actor_rating],
        "director_rating": [director_rating],
        "runtime_min": [runtime]
    })

    # Prediction
    result = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0]

    # ======================================
    # RESULT
    # ======================================

    st.subheader("🎯 Prediction")

    if result == 1:

        st.success(
            f"🎉 {movie_name} → SUCCESSFUL MOVIE"
        )

    else:

        st.error(
            f"❌ {movie_name} → NOT SUCCESSFUL MOVIE"
        )

    # ======================================
    # PROBABILITY
    # ======================================

    classes = model.classes_

    success_probability = 0
    failure_probability = 0

    for i, c in enumerate(classes):

        if c == 1:
            success_probability = probability[i] * 100

        if c == 0:
            failure_probability = probability[i] * 100

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "✅ Successful",
            f"{success_probability:.1f}%"
        )

    with col2:
        st.metric(
            "❌ Not Successful",
            f"{failure_probability:.1f}%"
        )

    st.divider()

    # ======================================
    # INPUT DETAILS
    # ======================================

    st.subheader("🎥 Movie Details")

    st.write("**Movie:**", movie_name)
    st.write("**Genre:**", genre)
    st.write("**Budget:**", f"₹{budget} Crore")
    st.write("**Marketing:**", f"₹{marketing} Crore")
    st.write("**Actor Rating:**", actor_rating)
    st.write("**Director Rating:**", director_rating)
    st.write("**Runtime:**", f"{runtime} minutes")

    # DEBUG
    st.write("---")
    st.write("Model prediction value:", result)

else:

    st.info(
        "Enter movie details from the left side and click "
        "**PREDICT**."
    )