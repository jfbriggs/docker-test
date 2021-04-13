import streamlit as st
import requests


def get_info():
    data = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    return data


def main():
    st.title("Hello, just testing.")

    st.subheader("Also a test.")

    data = get_info()

    st.write(data)

    st.balloons()

    st.write("Goodbye!")


if __name__ == "__main__":
    main()