import streamlit as st

# Page Configuration
st.set_page_config(page_title="AI Personality Predictor", page_icon="🧠")

st.title("🧠 AI Personality Predictor")
st.write("Niche diye gaye sawalon ka jawab dein (1 = Bilkul Nahi, 5 = Bilkul Haan)")

# Questions List
questions = [
    "1. Aap naye logon se milna pasand karte hain?",
    "2. Aap hamesha apne kaam ko plan karke karte hain?",
    "3. Aap doosron ki madad karne mein khushi mehsoos karte hain?",
    "4. Aap aksar choti baaton par chinta (worry) karte hain?",
    "5. Aapko nayi cheezein seekhna aur imagination pasand hai?",
    "6. Aap party mein sabse zyada baatein karte hain?",
    "7. Aapka kamra aur desk hamesha saaf rehti hai?",
    "8. Aap doosron ki feelings ki parwah karte hain?"
]

# Answers storage
answers = []

# UI creation using Streamlit Sliders
for q in questions:
    val = st.slider(q, 1, 5, 3)
    answers.append(val)

if st.button("Submit Results"):
    # Calculation Logic
    ext = (answers[0] + answers[5]) / 2
    con = (answers[1] + answers[6]) / 2
    agr = (answers[2] + answers[7]) / 2
    neu = answers[3]
    opn = answers[4]

    st.divider()
    st.subheader("Aapka Personality Result:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Social (Extraversion)", f"{ext}/5")
        st.metric("Organized (Conscientiousness)", f"{con}/5")
        st.metric("Kindness (Agreeableness)", f"{agr}/5")
    with col2:
        st.metric("Sensitivity (Neuroticism)", f"{neu}/5")
        st.metric("Creative (Openness)", f"{opn}/5")
    
    st.balloons()
