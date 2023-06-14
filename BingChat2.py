import streamlit as st
from EdgeGPT.EdgeUtils import Query, Cookie
#import streamlit_session_state as session_state

cookie_file = "./bing_cookies_1.json"
proxy = ''

# Функция для отправки запроса к Bing Chat
def send_request_to_bingchat(user_input):
    q = Query(user_input,
              style="precise",  # or: 'creative', 'balanced', 'precise'
              cookie_file=cookie_file,
              #proxy=proxy
             )

    return [q.output, q.suggestions]



# Главная функция для создания веб-приложения с использованием Streamlit
def app():
    # Заголовок и описание приложения
    st.title("Bing Chat - Веб-приложение")
    st.write("Введите ваш запрос и нажмите Enter для отправки")

    # Ввод запроса
    user_input = st.text_area("Ваш запрос:")

    # Обработка запроса и вывод ответа
    if st.button("Отправить"):
        response = send_request_to_bingchat(user_input)
        st.title("Ответ:")
        st.write(response[0])
        st.title("____________________________________________")
        st.title("Подсказки для следующего возможного вопроса:")
        st.write(response[1])

# Запуск приложения
if __name__ == "__main__":

    # 
    app()
