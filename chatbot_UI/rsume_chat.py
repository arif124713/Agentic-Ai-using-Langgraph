import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage
import uuid




#*************************utility function*********************************


def generate_thread_id():
    thread_id= uuid.uuid4()
    return thread_id


def reset_chat():
    thread_id= generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(thread_id)

def load_conversations(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    values = state.values or {}
    return values.get('messages', [])


def get_conversation_name(thread_id, max_len=40):
    messages = load_conversations(thread_id)
    for msg in messages:
        if isinstance(msg, HumanMessage) and msg.content:
            title = str(msg.content).strip().replace("\n", " ")
            if len(title) > max_len:
                return title[:max_len - 3] + "..."
            return title
    return "New conversation"


#***********************************************
# st.session_state -> dict -> 


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']= generate_thread_id()

if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread']=[]

add_thread(st.session_state['thread_id'])

#***************************** sidebar *******************************************************

st.sidebar.title("langraph chatbot")
if st.sidebar.button("new chat"):
    if st.session_state['message_history']:
        reset_chat()
    else:
        st.sidebar.info("Current chat is already empty. Send a message first.")
    
st.sidebar.header("All conversation")
for idx, thread_id in enumerate(st.session_state['chat_thread'], start=1):
    convo_name = get_conversation_name(thread_id)
    button_label = f"{idx}. {convo_name}"
    if st.sidebar.button(button_label, key=f"thread_{thread_id}"):
        st.session_state['thread_id']=thread_id
        messages= load_conversations(thread_id)

        temp_messages= []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role= "assistant"

            temp_messages.append({'role':role, 'content':msg.content})

        st.session_state['message_history']= temp_messages



#**************************************************************************



# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)


    with st.chat_message('assistant'):
        ai_message= st.write_stream(
            message_chunk.content for message_chunk, metadata in  chatbot.stream(
            {'messages': [HumanMessage(content=str(user_input))]},
            config={'configurable': {'thread_id': st.session_state['thread_id']}},
            stream_mode='messages'
        )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
