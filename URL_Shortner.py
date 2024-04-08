import streamlit as st
import pyshorteners
from log_to_db import authenticate_user ,create_user

def generate_short_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url

def main():
    st.sidebar.title("URL Shortner")
    page = st.sidebar.radio("Please Select any option...", ["Get short URL", "URL Analysis"])

    if page == "Get short URL":
        st.title("Create Your own short url")
        original_url = st.text_input("Enter Your URL :")
        if st.button("Generate Short URL"):
            if original_url:
                short_url = generate_short_url(original_url)
                st.divider()
                st.write('Your Short URL :')
                st.code(short_url, language='bash')
            else:
                st.error("Please enter a valid URL.")

    elif page == "URL Analysis":

        st.title("Analysis Dashboard Login")
        username = st.text_input("Username.....")
        password = st.text_input("Password.....")

        col1,col2 = st.columns(2)

        with col1:
            login = st.button(' Login ')
        with col2:
            signup = st.button('Signup')

        if login:
            if username and password:
                user_id = authenticate_user(username, password)
                if user_id:
                    st.success("Login successful! User ID: {}".format(user_id))
                    url_to_check = st.text_input("Enter Your Short URL :")
                    if st.button('Get URL Analysis'):
                        pass

                    
                else:
                    st.error("Invalid username or password.")
            else:
                st.error("Please enter username and password.")

        if signup:
            new_user_id = create_user(username, password)
            if new_user_id:
                st.success("User created successfully! User ID: {}".format(new_user_id))
            else:
                st.error("Failed to create user.")
        


if __name__=="__main__":
    main()