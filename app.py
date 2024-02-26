import streamlit as st



def load_chain():
    return load_normal_chain()

def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""

def set_send_input():
    st.session_state.send_input = True
    clear_input_field()



def main():
    st.set_page_config(page_title="Multimodal ViaGPT", page_icon=":books:")


    st.header("Multimodal ViaGPT")
    chat_container = st.container()

    #we need to first initialize the session state's user_input if it is not defined
    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        #Now we need to define the user question as the send input is also not defined
        st.session_state.user_question = ""

    user_input = st.text_input("Type your questions here", key="user_input", on_change=set_send_input)
    send_button = st.button("Send", key="send_button")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":

            #now the chat also get's displayed when you press enter
            llm_response = "This is the response from the LLM modal"

            #now we will write it into the chat container
            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                st.chat_message("ai").write("here is an answer")





if __name__ == "__main__":
    main()