import streamlit as st
from EdgeGPT.EdgeUtils import Query, Cookie
#import streamlit_session_state as session_state

cookie_file = "./bing_cookies_1.json"
proxy = 'http://neon:qwerty123@dc1.rbr.ru:4000'

# Функция для отправки запроса к Bing Chat
def send_request_to_bingchat(user_input):
    q = Query(user_input,
              style="precise",  # or: 'creative', 'balanced', 'precise'
              cookie_file=cookie_file,
              proxy=proxy)

    return [q.output, q.suggestions]

def authenticate(username, password):
    return username == 'dimacv' and password == 'vadgra'

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

    # Получение сеансового состояния
    session_state = st.session_state

    if "authenticated" not in session_state:
        session_state.authenticated = False

    if not session_state.authenticated:
        username_placeholder = st.empty()
        password_placeholder = st.empty()
        username = username_placeholder.text_input("Username:")
        password = password_placeholder.text_input("Password:", type="password")
        if st.button("Login"):
            if authenticate(username, password):
                session_state.authenticated = True
                username_placeholder.empty()
                password_placeholder.empty()
                app()
            else:
                st.error("Wrong credentials, please try again.")
    else:
        app()
