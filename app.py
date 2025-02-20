import streamlit as st

   st.title("Расчет стоимости проекта")
   st.write("Добро пожаловать в приложение для расчета стоимости проекта!")
   length = st.number_input("Длина (мм):", value=1000)
   width = st.number_input("Ширина (мм):", value=500)
   if st.button("Рассчитать"):
       cost = length * width * 0.01  # Пример расчета
       st.success(f"Примерная стоимость: {cost:.2f} руб.")
