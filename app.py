import streamlit as st
from PIL import Image
import urllib
import markdown
import src.utility_function as ut
import src.generate_art as gen_art
#from src.generate_art import *

def main():
    
    st.set_page_config(layout="wide")
    #readme_text = st.markdown(get_file_content_as_string("instructions.md"))

    st.sidebar.title('NFT App')

    app_mode = st.sidebar.selectbox(
        "What you want to do?",
        ["Instructions", "Show Code", "Generative Art", "Assembler", "Upload Collection"])
    
    if app_mode == "Instructions":
        st.sidebar.success('To continue select "Run the app"')
    
    elif app_mode == "Show the source code":
        st.title("Code")
        #readme_text.empty()
        #st.code(get_file_content_as_string("app.py"))

    elif app_mode == "Generative Art":
        st.title("Generative Art")
        run_generative_art()

    elif app_mode == "Assembler":
        st.title("Assembler")
        run_assembler()

    elif app_mode == "Upload Collection":
        st.title("Uploader")
        run_coll_uploader()
   

def run_generative_art():
    
    ut.spacer(2, st)
    n = st.slider('How many images in the collection?', 1, 10, 2)
    st.write("Selected: ", n)
    col_name = st.text_input("Insert the collection name")
    ut.spacer(2, st)
    
    if st.button('Generate Collection'):
        st.warning("Producing Art..")
        for i in range(n):
            gen_art.generate_art(col_name, f"{col_name}_image_{i}")
        st.success("Finish!")
        st.balloons()

        for i in range(n):
            c1, c2, c3 = st.columns([0.5,1,0.5])
            with c1:
                st.write("")
            with c2:
                image = Image.open(f"output/{col_name}/{col_name}_image_{i}.png")
                st.image(image, caption=f'Image {i}')  
            with c3:
                st.write("")


def run_assembler():
    pass


def run_coll_uploader():
    pass


@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = "https://raw.githubusercontent.com/MattiaRigi97/NFT_APP/main/" + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")
    

if __name__ == "__main__":
    main()