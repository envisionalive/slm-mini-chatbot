# Mini SLM Chatbot

A beginner-friendly Small Language Model (SLM) project that runs a
compact pretrained language model locally using Python and Hugging Face Transformers.

## What is an SLM?

A Small Language Model is a language model designed to use fewer
computational resources than very large language models.

This project uses **DistilGPT2**, a smaller GPT-2 model, to demonstrate
local text generation.

## Features

- Runs from your local computer
- Simple command-line chatbot
- Uses a pretrained compact language model
- No API key required
- Easy to modify and experiment with

## Project Structure

```text
slm-mini-chatbot/
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.9+
- Internet connection for the first model download
- A few GB of free disk/RAM is recommended

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

The first run downloads the model. After that, the model files are
cached locally by Hugging Face.

## Example

```text
Mini SLM Chatbot
Type 'exit' to quit.

You: Explain cloud computing in simple words.
SLM: Cloud computing is a way to use computing resources...
```

## Technologies

- Python
- Hugging Face Transformers
- PyTorch
- DistilGPT2

## Ideas for Improvements

1. Add a web interface using Streamlit.
2. Add conversation history.
3. Add a system prompt.
4. Add PDF/document question answering.
5. Replace DistilGPT2 with another small instruction-tuned model.
6. Add response length and temperature controls.

