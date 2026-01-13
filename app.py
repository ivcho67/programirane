import streamlit as st
import pandas as pd

# Заглавие
st.title("📊 Оценяване на хора – класна анкета")

# Инициализация на данните
if "people" not in st.session_state:
    st.session_state.people = []

if "grades" not in st.session_state:
    st.session_state.grades = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }

# Въвеждане от потребителя
st.subheader("Въведи човек и оценка")

name = st.text_input("Име на човек:")

grade = st.selectbox(
    "Оценка:",
    list(st.session_state.grades.keys())
)

# Бутон
if st.button("Запази оценката"):
    if name.strip() == "":
        st.warning("Моля, въведи име.")
    else:
        st.session_state.people.append(name)
        st.session_state.grades[grade] += 1
        st.success(f"Оценката за {name} е записана!")

st.divider()

# Резултати
st.subheader("📈 Резултати")

st.write("Разпределение на оценките")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades,
    orient="index",
    columns=["Брой"]
)
st.bar_chart(grades_df)
