import streamlit as st
import random
import time

class ChemistryStudentBot:
    def __init__(self, name="Alex"):
        self.name = name
        self.questions = [
            "What is the difference between an ionic and a covalent bond?",
            "Can you explain what the periodic table groups represent?",
            "How do I calculate the molar mass of a compound?",
            "Why is water a polar molecule?",
            "What happens during a chemical reaction?",
            "What are the steps to balance a chemical equation?",
            "How do you convert grams to moles?",
            "Can you give an example of an acid-base reaction?",
            "What does the term 'oxidation' mean in chemistry?",
            "How does temperature affect reaction rate?"
        ]
        self.responses = [
            "Oh, that makes sense now! Thank you!",
            "Can you give another example of that?",
            "I see, so it's similar to... oh wait, can you clarify that part?",
            "Interesting! I've never thought of it that way before.",
            "Could you explain it in simpler terms?",
            "Got it! Thanks for the explanation."
        ]

    def ask_question(self):
        return random.choice(self.questions)

    def react_to_answer(self):
        return random.choice(self.responses)

# Streamlit Web App
st.title("Chemistry Student Bot")

bot = ChemistryStudentBot(name="Taylor")

st.write(f"Hi! I'm {bot.name}, a curious chemistry student. I'll be asking some questions today!")
num_questions = st.slider("How many questions should I ask?", min_value=1, max_value=10, value=5)

if st.button("Start Asking Questions"):
    for _ in range(num_questions):
        question = bot.ask_question()
        st.write(f"**{bot.name}:** {question}")
        time.sleep(1)  # Simulate a short delay for realism
        response = bot.react_to_answer()
        st.write(f"**{bot.name}:** {response}")
        st.write("---")

st.write("Thanks for answering my questions! See you next time!")
