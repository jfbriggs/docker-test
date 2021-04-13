import streamlit as st
import requests


def get_info():
    data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    data_local = requests.get("http://backend:8080/info").json()
    return data, data_local


def main():
    st.title("Hello, just testing.")

    st.subheader("Also a test.")

    data, local_data = get_info()

    st.write(data)

    st.write(local_data)

    st.write("Hi there person!")

    st.balloons()

    st.write("Goodbye!")


if __name__ == "__main__":
    main()