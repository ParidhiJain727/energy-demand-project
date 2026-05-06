CSS_STRING = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Space Mono', monospace !important;
    color: #000000 !important;
}

.stApp {
    background-color: #fdf5e6;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Space Mono', monospace !important;
    font-weight: 700 !important;
    color: #000000 !important;
    text-transform: uppercase !important;
}

[data-testid="stSidebar"] {
    background-color: #cce0ff !important;
    border-right: 4px solid #000000 !important;
}

div.stTextInput > div > div > input,
div.stSelectbox > div > div > div,
div.stNumberInput > div > div > input {
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 4px 4px 0px 0px #000000 !important;
    background-color: #ffffff !important;
    color: #000000 !important;
    transition: all 0.2s ease !important;
}

/* Enhanced focus state for inputs */
div.stTextInput > div > div > input:focus,
div.stNumberInput > div > div > input:focus {
    background-color: #fffdf0 !important;
    box-shadow: 6px 6px 0px 0px #000000 !important;
    transform: translate(-2px, -2px) !important;
}

/* Make placeholder text (the cursor) more visible */
::placeholder {
    color: #888888 !important;
    opacity: 0.8 !important;
    font-weight: bold !important;
}

div.stButton > button {
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    background-color: #bdfcc9 !important;
    color: #000000 !important;
    font-weight: bold !important;
    font-family: 'Space Mono', monospace !important;
    text-transform: uppercase !important;
    transition: all 0.1s ease !important;
}

div.stButton > button:active {
    box-shadow: 0px 0px 0px 0px #000000 !important;
    transform: translate(5px, 5px) !important;
}

div.stButton > button:hover {
    border: 3px solid #000000 !important;
    color: #000000 !important;
}

div[data-testid="stMetric"] {
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    background-color: #ffd6e0 !important;
    padding: 15px !important;
    color: #000000 !important;
}

div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] {
    font-family: 'Space Mono', monospace !important;
    color: #000000 !important;
}

[data-testid="stDataFrame"] > div {
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
}

[data-testid="stImage"] img {
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
}

div.stAlert {
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    font-family: 'Space Mono', monospace !important;
}

/* Force text color in dataframes and other elements */
div[data-testid="stTable"] td, div[data-testid="stTable"] th, .stMarkdown p, .stMarkdown li, .stMarkdown span, label, div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] {
    color: #000000 !important;
}
/* Style Plotly charts to match neo-brutalist theme */
div[data-testid="stPlotlyChart"] {
    background-color: #ffffff !important;
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    padding: 5px !important;
    margin-bottom: 20px !important;
    overflow: hidden !important;
}

div[data-testid="stPlotlyChart"] iframe {
    border-radius: 10px !important;
}

/* Chat Input Styling */
div[data-testid="stChatInput"] {
    background-color: #ffffff !important;
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 5px 5px 0px 0px #000000 !important;
    padding: 0px !important;
    margin-bottom: 20px !important;
}

div[data-testid="stChatInput"] textarea {
    color: #000000 !important;
    font-weight: bold !important;
    font-family: 'Space Mono', monospace !important;
}

div[data-testid="stChatInput"] button {
    color: #000000 !important;
    background-color: #bdfcc9 !important;
    border-radius: 0 5px 5px 0 !important;
}

div[data-testid="stChatInput"] button:hover {
    background-color: #8ff19d !important;
}

/* Chat Message Styling */
div[data-testid="stChatMessage"] {
    background-color: #ffffff !important;
    border: 3px solid #000000 !important;
    border-radius: 10px !important;
    box-shadow: 4px 4px 0px 0px #000000 !important;
    padding: 15px !important;
    margin-bottom: 15px !important;
}

div[data-testid="stChatMessage"] .stMarkdown p {
    color: #000000 !important;
    font-size: 1.1rem !important;
}

div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background-color: #ffd6e0 !important;
}

div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background-color: #cce0ff !important;
}

</style>
"""
