import streamlit as st
import subprocess

if st.button("Run CLI"):
    subprocess.run("touch created_file.py", shell=True)  # create random file
    st.write("Saved in created_file.py")
else:
    st.write("Goodbye")
