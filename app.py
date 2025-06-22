import math

import streamlit as st


def main():
    st.title("Factorial Calculator", )
    st.write("The factorial of a number is the multiplication of all the numbers between 1 and the number itself.")
    st.latex("n! = n \\times (n-1) \\times (n-2) \\times \\cdots \\times 1")

    number = st.number_input(label="Enter a number", min_value=0, max_value=900)
    if st.button("Calculate"):
        st.write(f"The factorial of **{number}** is **{math.factorial(number)}**")
        st.balloons()


if __name__ == "__main__":
    main()
