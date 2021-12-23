import streamlit as st
import urllib

def main():
    
    st.set_page_config(layout="wide")
    readme_text = st.markdown(get_file_content_as_string("instructions.md"))

    st.title("NFT APP")
    st.sidebar.title('Navigation')

    app_mode = st.sidebar.selectbox(
        "What you want to do?",
        ["Instructions", "Show Code", "Generative Art", "Assembler", "Upload Collection"])
    
    if app_mode == "Instructions":
        st.sidebar.success('To continue select "Run the app".')
    
    elif app_mode == "Show the source code":
        readme_text.empty()
        st.code(get_file_content_as_string_local("app.py"))

    elif app_mode == "Generative Art":
        run_generative_art()

    elif app_mode == "Assembler":
        run_assembler()

    elif app_mode == "Upload Collection":
        run_coll_uploader()
   

def run_generative_art():
    pass

def run_assembler():
    pass

def run_coll_uploader():
    pass


@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = "https://github.com/MattiaRigi97/NFT_APP/" + path
    response = urllib.requests.urlopen(url)
    return response.read().decode("utf-8")
    

if __name__ == "__main__":
    main()