from os import link
from nltk import text
import streamlit as st
from textblob import TextBlob
from nltk_summarization import nltk_summarizer
from gensim_summarization import gensim_summarize
# from abs_summarization import abs_summarizer
from url import url_text


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def get_text():
    uploaded_file = st.file_uploader("Add text file!",type='txt')

    if uploaded_file :
        text = ''
        for line in uploaded_file:
            line = line.decode('utf8').replace("\b", "").replace("\r", "")
            text = text+line
        return text

def main():
    st.title("Extractive Text Summarization")
    
    Summarizer = st.radio('',options = ['Using NLTK', 'Using Gensim'])
    st.write('<style>div.row-widget.stRadio > div { flex-direction : row;}</style>',unsafe_allow_html = True)
    if (Summarizer == 'Using NLTK'):
        n = st.slider('Maximum Number of Sentences',1,100,value=5)
        options = st.selectbox("Type of file",['Text','File','URL'])

        if options == 'Text':
            st.subheader("Summarize your text")
            message = st.text_area("Enter your text")
            if st.button("Summarize"):
                nlp_result = nltk_summarizer(message,n)
                st.success("Summary:   \n"+nlp_result)
        elif options == 'File':
            try:
                text = get_text()
                message = st.subheader("Your text")
                st.info(text)
                if st.button("Summarize"):
                    result = nltk_summarizer(text,n)
                    st.success("Summary:   \n"+result)
            except:
                pass    
        elif options == 'URL':
            try:
                link = st.text_input("Enter the URL")
                text = url_text(link)
                message = st.subheader("Your text")
                st.info(text)
                if st.button("Summarize"):
                    result = nltk_summarizer(text,n)
                    st.success("Summary:   \n"+result)
            except:
                pass
       
    else:
        # st.subheader("Word Count")
        # n = st.slider('Number of Words ',1,100,value=0)
        
        options = st.selectbox("Type of file",['Text','File','URL'])

        if options == 'Text':
            st.subheader("Summarize your text")
            message = st.text_area("Enter your text")
            if st.button("Summarize"):
                nlp_result = gensim_summarize(message)
                st.success(nlp_result)
        elif options == 'File':
            try:
                text = get_text()
                message = st.subheader("Your text")
                st.info(text)
                if st.button("Summarize"):
                    result = gensim_summarize(text)
                    st.success(result)
            except:
                pass    
        elif options == 'URL':
            try:
                link = st.text_input("Enter the URL")
                text = url_text(link)
                message = st.subheader("Your text")
                st.info(text)
                if st.button("Summarize"):
                    result = gensim_summarize(text)
                    st.success(result)
            except:
                pass





if __name__ == '__main__':
    main()