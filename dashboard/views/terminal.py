import streamlit as st
import time
from dashboard.utils.bot_logic import process_query

def render_terminal_page():
    st.markdown("""
    <div class="terminal-header-container" style="margin-bottom: 20px;">
        <h1 style='color: #000000 !important; margin: 0; font-size: 3rem; text-shadow: 4px 4px 0px #bdfcc9;'>POWER-PULSE ASSISTANT</h1>
        <div style='font-size: 1.2rem; font-weight: bold; letter-spacing: 2px; background: #000; color: #bdfcc9; display: inline-block; padding: 5px 15px; border-radius: 8px; margin-top: 10px;'>
            SYSTEM TERMINAL ONLINE
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border: 2px solid #000;'>", unsafe_allow_html=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "SYSTEM INITIALIZED. I am the Power-Pulse Assistant. Query the grid or ask about demand forecasting."}
        ]

    # Container for messages to ensure it looks like a terminal
    chat_container = st.container()
    
    with chat_container:
        # Display chat messages from history on app rerun
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                if msg["content"] == "I am sorry, this information seems to be out of scope.":
                    st.markdown(f"<span style='color: #ff4b4b; font-weight: bold;'>⚠️ {msg['content']}</span>", unsafe_allow_html=True)
                else:
                    st.markdown(msg["content"])

    # Accept user input
    if prompt := st.chat_input("QUERY THE SYSTEM..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Process query with history to maintain context
            bot_response = process_query(prompt, st.session_state.messages[:-1]) # Don't include the current prompt in history yet as it's sent separately
            
            # Simulate stream of response
            for chunk in bot_response.split():
                full_response += chunk + " "
                time.sleep(0.05) # Add a slight delay for "typing" effect
                
                # Render differently if it's the guardrail message
                if full_response.strip() == "I am sorry, this information seems to be out of scope.":
                     message_placeholder.markdown(f"<span style='color: #ff4b4b; font-weight: bold;'>⚠️ {full_response}▌</span>", unsafe_allow_html=True)
                else:
                     message_placeholder.markdown(f"{full_response}▌")
            
            # Final message without cursor
            if bot_response == "I am sorry, this information seems to be out of scope.":
                 message_placeholder.markdown(f"<span style='color: #ff4b4b; font-weight: bold;'>⚠️ {bot_response}</span>", unsafe_allow_html=True)
            else:
                 message_placeholder.markdown(bot_response)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
