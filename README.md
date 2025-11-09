# Intelligent Chatbot with Ollama and LangChain
An intelligent chatbot built with Ollama3 and LangChain. **This bot is designed to provide incorrect responses.**

## 🛠️ Technologies

- **Python 3.13**
- **LangChain** - Framework for LLM applications
- **Ollama** - Platform for running local models
- **LangChain-Ollama** - Official Ollama-LangChain integration

## 🚀 Installation and Execution Guide

### Step 1: Install and Run Ollama

Ensure the Ollama service is running in the background.

1.  **Download and Install Ollama:** (Visit the official Ollama website for the specific installer for your OS).
2.  **Start the Service (Debian/Linux):**
   
    ```bash
    sudo systemctl start ollama
    ```
4.  **Verify Status:**
   
    ```bash
    sudo systemctl status ollama
    ```

### Step 2: Set Up and Activate the Virtual Environment

It is essential to work inside a virtual environment to avoid system dependency conflicts.

1.  **Navigate to your project directory:**
   
    ```bash
    cd path/to/your/project
    ```
3.  **Create the virtual environment:**
   
    ```bash
    python3 -m venv venvChat
    ```
5.  **Activate the virtual environment:**
   
    ```bash
    source venvChat/bin/activate
    ```
    *(Your terminal prompt should now start with `(venvChat)`).*

### Step 3: Install Python Dependencies

With the virtual environment active, install the necessary libraries.

```bash
pip install langchain
pip install -qU langchain-ollama
```
### Step 4: Pull the Llama 3 Model

```bash
ollama pull llama3
```

### Step 5: Run the Program

```bash
python SImpleChatBot.py
```
