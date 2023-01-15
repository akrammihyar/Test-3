import streamlit as st
import pandas as pd
import random

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def main():
    st.title("Random Question Generator")
    file_path = st.file_uploader("Upload your .csv file", type=["csv"])
    if file_path is not None:
        data = load_data(file_path)
        genre = st.selectbox("Select Genre",data['genre'].unique())
        questions = data[data['genre'] == genre]
        question = random.choice(questions['question'])
        st.success(question)

if __name__ == '__main__':
    main()
