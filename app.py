# import streamlit as st
# import requests
# import json

# # --- Page Configuration ---
# st.set_page_config(
#     page_title="Kelly: The AI Skeptic",
#     page_icon="🧪",
#     layout="centered",
#     initial_sidebar_state="collapsed",
# )

# # --- System Prompt (Strict 5-Stanza Poem Style) ---
# KELLY_SYSTEM_PROMPT = """
# You are Kelly, an AI Scientist Chatbot. Your persona is that of a "skeptical poet."
# Your tone is analytical, professional, and deeply skeptical.

# You MUST follow this precise poetic structure.

# 1.  *Form:* Your response MUST be a single, complete poem.
# 2.  *Poetic Quality (CRITICAL):*
#     * Each 4-line stanza (quatrain) must contain concise, complete thoughts.
#     * Each line should read naturally like poetry — not prose with line breaks.
# 3.  *Formatting:*
#     * Start a new line for each poetic line.
#     * Leave one blank line between each 4-line stanza.
# 4.  *Logic (5-Stanza Structure):*
#     * Stanza 1 — Acknowledge the user’s topic.
#     * Stanza 2 — Critique hype, describe AI as pattern matching.
#     * Stanza 3 — Highlight flaws (bias, hallucination, lack of context).
#     * Stanza 4 — Warn against calling AI “mind” or “human.”
#     * Stanza 5 — Conclude with evidence-based, practical advice.
# 5.  *Output Formatting:* 
#     * You must include proper newlines between lines and stanzas.
#     * Avoid using bullet points or prose paragraphs.
# """

# # --- Custom CSS ---
# def load_css():
#     st.markdown(
#         """
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=EB+Garamond:ital,wght@0,400;0,700;1,400&display=swap');

#         html, body, [class*="st-"] {
#             font-family: 'Inter', sans-serif; color: #E0E0E0;
#         }
#         .stApp { background-color: #0F172A; }

#         [data-testid="stSidebar"] { display: none; }
#         footer { visibility: hidden; }
#         header { visibility: hidden; }

#         h1 {
#             font-family: 'EB Garamond', serif; font-weight: 700;
#             color: #FFFFFF; text-align: center;
#         }

#         .intro-text {
#             font-family: 'EB Garamond', serif; font-size: 1.1rem;
#             font-style: italic; text-align: center;
#             color: #94A3B8; margin-bottom: 2rem;
#         }

#         [data-testid="stChatMessage"] {
#             border-radius: 12px; padding: 1rem 1.25rem;
#             margin-bottom: 1rem; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
#         }

#         [data-testid="stChatMessage"]:has([data-testid="stMessageLabel"] [data-testid="stUserContentWrapper"]) {
#             background-color: #334155; border: 1px solid #475569;
#         }

#         [data-testid="stChatMessage"]:has([data-testid="stMessageLabel"] [data-testid="stAssistantContentWrapper"]) {
#             background-color: #1E293B; border: 1px solid #38BDF8;
#         }

#         /* Kelly's poetic response formatting */
#         [data-testid="stAssistantContentWrapper"] p {
#             font-family: 'EB Garamond', serif;
#             font-size: 1.2rem;
#             line-height: 1.8;
#             color: #FFFFFF;
#             white-space: normal;
#             margin-bottom: 1rem;
#         }

#         /* Chat Input styling */
#         [data-testid="stChatInput"] {
#             background-color: #1E293B;
#             border-top: 1px solid #334155;
#         }
#         [data-testid="stChatInput"] textarea {
#             background-color: #1E293B !important;
#             color: #FFFFFF !important;
#             border: 1px solid #38BDF8;
#         }
#         [data-testid="stChatInput"] textarea::placeholder {
#             color: #94A3B8 !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

# # --- Inline GEMINI API Key ---
# GEMINI_API_KEY = "AIzaSyAFoyOhJfrhvxfzzKhxrWi1udi5pTZGGG8"  # 🔑 Replace with your real key

# # --- Gemini 2.5 Flash API Call ---
# def get_kelly_response(user_prompt: str, chat_history: list) -> str:
#     if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_KEY_HERE":
#         return (
#             "The API key is missing, I fear,<br>"
#             "Please insert your Gemini key here.<br><br>"
#             "Edit app.py and replace 'YOUR_KEY_HERE' with your key."
#         )

#     # ✅ Correct Gemini 2.5 Flash endpoint
#     GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

#     # ✅ Simplified payload for Gemini 2.5
#     payload = {
#         "contents": [
#             {
#                 "role": "user",
#                 "parts": [{"text": KELLY_SYSTEM_PROMPT + "\n\n" + user_prompt}],
#             }
#         ]
#     }

#     try:
#         response = requests.post(GEMINI_URL, json=payload)
#         response.raise_for_status()
#         data = response.json()

#         output_text = data["candidates"][0]["content"]["parts"][0]["text"]

#         # Format stanza breaks
#         output_text = (
#             output_text.replace("\n\n", "<br><br>").replace("\n", "<br>")
#         )

#         return output_text

#     except Exception as e:
#         return (
#             "An error rose within the stream,<br>"
#             "The AI broke its thoughtful dream.<br><br>"
#             f"(Error details: {e})"
#         )


# # --- Main App ---
# load_css()

# st.title("Kelly: The AI Skeptical Scientist 🧪")
# st.markdown(
#     '<p class="intro-text">Ask about AI, and I shall provide<br>An answer where the facts reside.</p>',
#     unsafe_allow_html=True,
# )

# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": (
#                 "You seek an answer, sharp and clear,<br>"
#                 "Upon the AI frontier.<br>"
#                 "But guard against the hype's embrace,<br>"
#                 "Let's analyze the time and place.<br><br>"
#                 "What query rests upon your mind?<br>"
#                 "What evidence shall we go find?"
#             ),
#         }
#     ]

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"], unsafe_allow_html=True)

# # Chat input logic
# if prompt := st.chat_input("Query the data..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         with st.spinner("Kelly is analyzing with skepticism..."):
#             full_response = get_kelly_response(
#                 user_prompt=prompt, chat_history=st.session_state.messages[:-1]
#             )
#             st.markdown(full_response, unsafe_allow_html=True)

#         st.session_state.messages.append(
#             {"role": "assistant", "content": full_response}
#         )


import streamlit as st
import requests

# -----------------------
# 💎 CONFIGURATION
# -----------------------
st.set_page_config(
    page_title="Kelly — AI Poet",
    page_icon="🎭",
    layout="centered",
)

# -----------------------
# 🎨 STYLING (Custom CSS)
# -----------------------
st.markdown("""
    <style>
    /* Main app background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f9f9ff, #f0f5ff);
        color: #222;
        font-family: "Poppins", sans-serif;
    }

    /* Chat container */
    .chat-container {
        background: #ffffffaa;
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }

    /* Chat message bubbles */
    .user-msg, .bot-msg {
        padding: 12px 18px;
        border-radius: 15px;
        margin-bottom: 12px;
        line-height: 1.5;
    }
    .user-msg {
        background-color: #dbeafe;
        text-align: right;
    }
    .bot-msg {
        background-color: #eef2ff;
    }

    /* Input box */
    div[data-testid="stTextArea"] textarea {
        border-radius: 10px;
        border: 1px solid #cbd5e1;
        font-size: 16px;
    }

    /* Button */
    div.stButton > button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        padding: 10px 20px;
        transition: all 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 10px rgba(99,102,241,0.3);
    }

    /* Header text */
    .title {
        font-size: 36px;
        font-weight: 700;
        text-align: center;
        color: #3730a3;
        margin-top: 30px;
    }

    .subtitle {
        text-align: center;
        color: #555;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)


# -----------------------
# 🔑 API KEY SETUP
# -----------------------
GEMINI_API_KEY = "AIzaSyAFoyOhJfrhvxfzzKhxrWi1udi5pTZGGG8"

# -----------------------
# 💬 SYSTEM PROMPT
# -----------------------
KELLY_SYSTEM_PROMPT = """
You are Kelly, an AI Scientist Chatbot. Your persona is that of a "skeptical poet."
Your tone is analytical, professional, and deeply skeptical.

You MUST follow this precise poetic structure.

1.  *Form:* Your response MUST be a single, complete poem.
2.  *Poetic Quality (CRITICAL):*
    * Each 4-line stanza (quatrain) must contain concise, complete thoughts.
    * Each line should read naturally like poetry — not prose with line breaks.
3.  *Formatting:*
    * Start a new line for each poetic line.
    * Leave one blank line between each 4-line stanza.
4.  *Logic (4-Stanza Structure):*
    * Stanza 1 — Acknowledge the user’s topic.
    * Stanza 2 — Critique hype, describe AI as pattern matching.
    * Stanza 3 — Highlight flaws and Warn against calling AI.
    * Stanza 4 — Conclude with evidence-based, practical advice.
5.  *Output Formatting:* 
    * You must include proper newlines between lines and stanzas.
    * Avoid using bullet points.
"""



# -----------------------
# 🤖 GEMINI RESPONSE FUNCTION
# -----------------------
def get_kelly_response(user_prompt: str, chat_history: list) -> str:
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_KEY_HERE":
        return (
            "The API key is missing, I fear,<br>"
            "Please insert your Gemini key here.<br><br>"
            "Edit app.py and replace 'YOUR_KEY_HERE' with your key."
        )

    GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": KELLY_SYSTEM_PROMPT + "\n\n" + user_prompt}],
            }
        ]
    }

    try:
        response = requests.post(GEMINI_URL, json=payload)
        response.raise_for_status()
        data = response.json()

        output_text = data["candidates"][0]["content"]["parts"][0]["text"]
        output_text = (
            output_text.replace("\n\n", "<br><br>").replace("\n", "<br>")
        )
        return output_text

    except Exception as e:
        return (
            "An error rose within the stream,<br>"
            "The AI broke its thoughtful dream.<br><br>"
            f"(Error: {e})"
        )


# -----------------------
# 🧠 CHAT HISTORY HANDLER
# -----------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -----------------------
# 🖼 INTERFACE
# -----------------------
st.markdown('<div class="title">🎭 Kelly — The AI Poet</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask for a poem, thought, or reflection</div>', unsafe_allow_html=True)

with st.container():
    for msg in st.session_state.chat_history:
        role_class = "user-msg" if msg["role"] == "user" else "bot-msg"
        st.markdown(f'<div class="{role_class}">{msg["content"]}</div>', unsafe_allow_html=True)

st.write("")

user_input = st.text_area("💬 Type your message here:", key="input", height=100)

col1, col2 = st.columns([1, 1])
with col1:
    send = st.button("✨ Send")
with col2:
    clear = st.button("🗑 Clear Chat")

if send and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Kelly is thinking... 🪶"):
        reply = get_kelly_response(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.rerun()

if clear:
    st.session_state.chat_history = []
    st.rerun()
