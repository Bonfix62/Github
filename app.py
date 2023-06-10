import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def count_selected_lines(text):
    lines = text.split('\n')
    selected_lines = [line for line in lines if line.strip()]
    return len(selected_lines)

def main():
    st.title("Підрахунок кількості вибраних рядків")

    st.write("Введіть текст:")
    text = st.text_area("")

    if st.button("Підрахувати"):
        count = count_selected_lines(text)
        st.write(f"Кількість вибраних рядків: {count}")

if __name__ == '__main__':
    main()
