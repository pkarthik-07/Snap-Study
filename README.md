# 📚 Snap & Study — AI-Powered Learning Assistant

**Snap It. Understand It. Learn It.**

Snap & Study is an AI-powered educational assistant built with Python and Streamlit. It helps students understand questions, learn from images, and simplify educational content using Google's Gemini AI.

## ✨ Features

- 📸 **Image-Based Learning:** Upload a photo of a question or educational material and get an explanation.
- 💬 **AI Question Answering:** Ask questions and receive clear, easy-to-understand answers.
- 🧠 **Simplified Explanations:** Break down complex topics into simpler concepts.
- 📧 **Email Summaries:** Send generated learning summaries directly to your email.
- 🎨 **Interactive Interface:** Use a simple, user-friendly Streamlit interface.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI Model:** Google Gemini API
- **Email Integration:** Python `smtplib`
- **Configuration:** Streamlit Secrets

## 📂 Project Structure

```text
Snap & Study/
├── .streamlit/
│   └── secrets.toml
├── app.py
├── prompt.py
├── requirements.txt
├── .gitignore
└── README.md
```

> Virtual environments, Python cache files, and secret configuration files are excluded from Git using `.gitignore`.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd "Snap & Study"
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys and email credentials

Create a file named `.streamlit/secrets.toml` and add your credentials:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
GMAIL_ADDRESS = "your-email@gmail.com"
GMAIL_APP_PASSWORD = "your-gmail-app-password"
```

Obtain your Gemini API key through [Google AI Studio](https://aistudio.google.com/). For Gmail SMTP authentication, use a Google App Password with 2-Step Verification enabled.

**Security:** Never upload `secrets.toml`, API keys, or passwords to GitHub.

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## 🚀 How to Use

1. Launch Snap & Study.
2. Enter an educational question or upload an image, depending on the available interface options.
3. Review the AI-generated explanation.
4. Generate a learning summary and use the email feature if needed.

## 🎯 Project Objective

The objective of Snap & Study is to make learning more accessible by combining AI-powered explanations, image-based question understanding, and convenient email summaries in one application.

## 🔒 Security Notes

- Keep API keys and email credentials private.
- Do not commit `.streamlit/secrets.toml`.
- Use a virtual environment to manage Python dependencies.
- Review uploaded content before sharing it with external AI services.

## 🔮 Future Enhancements

- Conversation history and saved notes
- Support for PDFs and additional document formats
- Personalized learning recommendations
- Quiz generation and practice questions
- Deployment as a public web application

## 👨‍💻 Author

**P Karthik**

AI & Machine Learning Student | Python Developer | AI Project Builder

---

*Snap & Study — Making learning simpler with AI.*