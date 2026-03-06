import streamlit as st

st.title("This is a title")

st.header("This is a header")

st.subheader("This is a subheader")

st.markdown("This is a markdown")

st.text("This is plain text")

st.write("it can handle contents like bold, italic, and numbers 123...")


st.markdown('### code block example')
st.code("""#python example
        def greet(name):
            return f"Hello, {name}!"
print(greet("streamlit"))""", language="python")
        
st.markdown("#### Inline latEX : $a$")


st.success("This is a sucess message!")

st.warning("Be careful this is a warning")
st.error("This is an error message")

st.info("This is information")

st.markdown(". **Tip: ** Use feedback messages to guide the user.")