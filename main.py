from gingerit.gingerit import GingerIt
import streamlit as st

st.title("Grammar and Spell checker")
text = st.text_area("Enter your Text: ",
                    value='',
                    height=None,
                    max_chars=None,
                    key=None)

parser = GingerIt()

if st.button("Check Grammar"):
    if text == '':
        st.write("Please enter some text")
    else:
        # result = parser.parse(text)
        st.subheader("\n**Corrected Sentence:**\n" + parser.parse(text)["result"])

if st.button("clear answer"):
    st.stop()

if st.download_button(label='download text',data = parser.parse(text)["result"]):
    st.write("Downloading...")
    st.write("Thank you for using this app")
    st.stop()

