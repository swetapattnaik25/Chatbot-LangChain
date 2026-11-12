# Google Gemini AI Chatbot

## Overview

A simple AI-powered chatbot built using Python and Google's Gemini models. It uses LangChain to interact with the Gemini model and generate responses to user questions. The project also includes a script to retrieve and display available Gemini models using the Google GenAI SDK.

## Features

- Interactive command-line chatbot.
- Generates AI responses using Google Gemini.
- Integrates Gemini with LangChain.
- Uses environment variables to securely manage API keys.
- Lists available Gemini models using the Google GenAI SDK.

## Technologies Used

- **Programming Language:** Python
- **LLM:** Google Gemini
- **Framework:** LangChain
- **Libraries:** 
  - `langchain-google-genai`
  - `langchain-core`
  - `google-genai`
  - `python-dotenv`

## Project Structure

```text
Google-Gemini-Chatbot/
│
├── chatbot.py
├── modellist.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Google-Gemini-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_google_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 6. Run the chatbot

```bash
python chatbot.py
```

To list available Gemini models:

```bash
python modellist.py
```

## Usage

- Run `chatbot.py` to start the interactive chatbot.
- Enter your questions in the terminal.
- The Gemini model generates responses.
- Type `exit` to terminate the chatbot.
- Run `modellist.py` to view available models.

## Security

API keys are stored in a local `.env` file and should never be uploaded to GitHub. Use `.env.example` as a configuration template.

## Future Improvements

- Add conversation history and memory.
- Implement a graphical user interface.
- Add support for multiple Gemini models.
- Improve response handling and error management.
