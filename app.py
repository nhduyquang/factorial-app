import math
import os

import streamlit as st


def load_users() -> list:
    '''
    This function is used to load a list of users from the 'users.txt' file.

    Returns:
        list[str]:  a list of user if the file is found and readable;
                    otherwise, an empty list
    '''
    try:
        if os.path.exists('users.txt'):
            with open(file='users.txt', mode='r', encoding='utf-8') as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
                return users
        else:
            st.error('Error: users.txt file not found.')
            return []
    except Exception as e:
        st.error(f'Error: {e}')
        return []


def greeting_page():
    '''
    This function is used to display a user greeting interface when an invalid username is entered.
    '''
    st.title(f'Hello, and welcome!')
    st.write(f'Greetings, {st.session_state.username}!')
    st.write('You do not have access to the factorial calculator app.')

    if st.button('Return to Login'):
        st.session_state.show_greeting_page = False
        st.session_state.username = ''
        st.rerun()


def login_page():
    '''
    This function is used to display the login interface and handle user authentication logic.
    '''
    st.title('Login')
    st.write('Please log in before using the factorial calculator app.')
    username = st.text_input(label='Enter username:', value='admin')

    if st.button('Log in'):
        if not username:
            st.warning('Please enter username first!')
            return None

        st.session_state.username = username

        if username in load_users():
            st.session_state.logged_in = True
        else:
            st.session_state.show_greeting_page = True

        st.rerun()


def factorial_calculator_page():
    '''
    This function is used to display factorial calculator app .
    '''
    st.title("Factorial Calculator", )

    # User greeting
    st.write(f'Welcome, {st.session_state.username}!')

    # Logout
    if st.button('Log out'):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.rerun()

    st.divider()

    # Calculate the factorial of a number
    st.write("The factorial of a number is the multiplication of all the numbers between 1 and the number itself.")
    st.latex("n! = n \\times (n-1) \\times (n-2) \\times \\cdots \\times 1")

    number = st.number_input(label="Enter a number", min_value=0, max_value=900)
    if st.button("Calculate"):
        st.write(f"The factorial of **{number}** is **{math.factorial(number)}**")
        st.balloons()


def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'username' not in st.session_state:
        st.session_state.username = ''

    if 'show_greeting_page' not in st.session_state:
        st.session_state.show_greeting_page = False

    if st.session_state.logged_in:
        factorial_calculator_page()
    elif st.session_state.show_greeting_page:
        greeting_page()
    else:
        login_page()


if __name__ == "__main__":
    main()
