import streamlit as st

# Simple sentiment analysis without heavy dependencies
def analyze_sentiment(text):
    """Simple sentiment analyzer using keyword matching"""
    text_lower = text.lower()
    
    positive_words = ['happy', 'great', 'good', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'best', 'awesome', 'perfect', 'beautiful', 'blessed', 'grateful', 'energetic', 'motivated']
    negative_words = ['sad', 'bad', 'terrible', 'awful', 'hate', 'worst', 'horrible', 'depressed', 'anxious', 'worried', 'stressed', 'angry', 'frustrated', 'devastated', 'miserable', 'lonely']
    
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    if pos_count > neg_count:
        return 'POSITIVE', 0.85
    elif neg_count > pos_count:
        return 'NEGATIVE', 0.85
    else:
        return 'NEUTRAL', 0.75

# Motivational tips based on mood
tips = {
    "POSITIVE": [
        "Keep up the great energy! 🌟",
        "Celebrate small wins today.",
        "Share your positivity with a friend."
    ],
    "NEGATIVE": [
        "Take a deep breath. 🌿",
        "Try writing down your thoughts.",
        "Listen to calming music or meditate."
    ],
    "NEUTRAL": [
        "Stay balanced and mindful. ⚖️",
        "A short walk can refresh your mind.",
        "Keep focusing on what matters."
    ]
}

# Streamlit UI
st.title("🧠 Mental Health Companion Chatbot")
st.write("A safe space for students to share feelings and get supportive responses.")

user_input = st.text_area("How are you feeling today?")

if st.button("Submit"):
    if user_input.strip():
        # Analyze sentiment
        label, score = analyze_sentiment(user_input)

        # Display sentiment
        st.subheader("Mood Detection")
        st.write(f"Detected mood: **{label}** (confidence: {score:.2f})")

        # Generate empathetic response
        st.subheader("Companion Response")
        if label == "POSITIVE":
            st.write("I'm glad you're feeling good! 🌈")
        elif label == "NEGATIVE":
            st.write("I'm here for you. It's okay to feel this way. 💙")
        else:
            st.write("Thanks for sharing. Let's keep things steady. 🌼")

        # Show relaxation tips
        st.subheader("Relaxation & Motivation Tips")
        for tip in tips.get(label, []):
            st.write(f"- {tip}")
    else:
        st.warning("Please enter your feelings before submitting.")
