import streamlit as st
from google import genai
from google.genai import types
from prompt import SYSTEM_PROMPT, WELCOME_MESSAGE_TEMPLATE, SUMMARY_REQUEST_PROMPT
import smtplib
from email.mime.text import MIMEText

MODEL_NAME = "gemini-3.5-flash"
st.set_page_config(page_title="Snap & Study", page_icon="📚")


GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
GMAIL_ADDRESS = st.secrets["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]


@st.cache_resource

def get_gemini_client():
    return genai.Client(api_key = GEMINI_API_KEY)

gemini_client = get_gemini_client()


def render_message(message):
    with st.chat_message(message["role"]):
        if message["kind"] == "text":
            st.write(message["content"])
        elif message["kind"] == "image":
            st.image(message["content"])
 
 
def add_message(role, kind, content):
    st.session_state.messages.append({"role": role, "kind": kind, "content": content})
    render_message(st.session_state.messages[-1])

def ask_gemini(parts):
    try:
        return st.session_state.chat.send_message(parts).text
    except Exception as error:
        return f"sorry, something went wrong {error}"

def clean_mail_text(text):
    if not text:
        return "No Solution Founded !"
    text = " ".join(text.split())
    return text[:1500] + "..." if len(text) > 1500 else text

def send_mail(to_address, subject, body):
    try:
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = GMAIL_ADDRESS
        message["To"] = to_address

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as server:
            server.starttls()
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(message)

        return True, "Email sent successfully!"

    except Exception as error:
        return False, str(error)





if "onboarded" not in st.session_state:
    st.title("Snap & Study 📚")
    st.caption(" Snap It. Understand It. Learn It")
    with st.form("onboarding_form"):
        name = st.text_input("Your Name ", placeholder = "Karthik Raj")
        mail = st.text_input("Email ID",
            placeholder = "karthikraj@gmail.com",
            help = "This is the Email ID Snap & Study will send mail your summary"
        )

        submitted = st.form_submit_button("Get Started !")
    if submitted:
        if not name.strip() or not mail.strip():
            st.warning("please fill both Your name and Email ID")
        else:
            st.session_state.name = name.strip()
            st.session_state.mail = mail.strip()
            st.session_state.chat = gemini_client.chats.create(
                model=MODEL_NAME,
                config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
            )
            st.session_state.messages = []
            st.session_state.onboarded = True
            st.rerun()
    st.stop()

header_col,button_col =st.columns([5,2], vertical_alignment="center")
with header_col:
    st.title("Snap & Study")
with button_col:
    send_disabled=len(st.session_state.messages)<=2
    if st.button("Send to Mail" , disabled = send_disabled, use_container_width=True ):
        with st.spinner("fetching the problem...."):
            summary= ask_gemini([SUMMARY_REQUEST_PROMPT])
        success, info = send_mail(
            st.session_state.mail,
            "Your Snap & Study Summary 📚",
            summary)
        if success:
            st.success("sent ! Check your Mail ")
        else:
            st.error(f" couldn't send that : {info}")
st.caption(f"logged in as {st.session_state.name} --updates go to {st.session_state.mail}")

if not st.session_state.messages:
    add_message("assistant", "text", WELCOME_MESSAGE_TEMPLATE.format(name=st.session_state.name))
else:
    for message in st.session_state.messages:
        render_message(message)

user_input = st.chat_input(
    "Ask a question or snap a photo to learn instantly.",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
 
if user_input:
    photo = user_input.files[0] if user_input.files else None
    text = user_input.text
    parts = []
 
    if photo is not None:
        photo_bytes = photo.getvalue()
        add_message("user", "image", photo_bytes)
        parts.append(types.Part.from_bytes(data=photo_bytes, mime_type=photo.type))
    if text:
        add_message("user", "text", text)
        parts.append(text)
    elif photo is not None:
        parts.append("What is this question? Explain it in simple terms and show me the step-by-step solution.")
 
    with st.spinner("Crunching the numbers..."):
        answer = ask_gemini(parts)
    add_message("assistant", "text", answer)


