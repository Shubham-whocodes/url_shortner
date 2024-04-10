import streamlit as st
import pyshorteners
from log_to_db import authenticate_user ,create_user,push_new_url_entry ,get_user_history

def generate_short_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url

def generate_new_user():
    username = st.text_input("Please Enter new username")
    password = st.text_input("Please Enter new password") 
    generate = st.button('Create new User')

    if generate:
        create_user(username, password)
        st.success('User Created Successfully')

def generate_new_short_url():
    username = st.text_input("Please Enter your username")
    original_url = st.text_input("Please Enter you URL here")
    generate = st.button('Generate short URL')

    if generate:
        short_url = generate_short_url(original_url)
        st.divider()
        st.write('Your Short URL :')
        st.code(short_url, language='bash')
        push_new_url_entry(username,original_url,short_url)

def get_url_analysis():
    username = st.text_input("Please Enter your username")
    analysis = st.button('Proceed')

    if analysis:
        user_history  = get_user_history(username)
        if len(user_history):
            st.table(user_history)
        else:
            st.error('No Data Found for User {}'.format(username))


def main():
    st.title("Welcome to URL shortner and Analytical Dashboard")
    page = st.radio("Please Select any option...", ["Create New User","Existing User","User Analysis (Only Existing Users)"])

    if page == 'Create New User':
        generate_new_user()
    elif page == 'Existing User':
        generate_new_short_url()
    elif page == 'User Analysis (Only Existing Users)':
        get_url_analysis()
            

if __name__=="__main__":
    main()