
# 🤖 Auto-Reply AI Chatbot

An AI-powered Python chatbot that automatically reads chat history, detects new messages from a target user, generates humorous responses using OpenAI GPT models, and sends the reply automatically through desktop automation.

> ⚠️ **Disclaimer:** This project is developed for educational purposes only. Use it responsibly and only with applications and accounts where automation is permitted.

---

## 📌 Features

- 🤖 Automated chat interaction using `pyautogui`
- 📋 Reads and analyzes chat history
- 👤 Detects messages from a specific user
- 🧠 Generates AI-powered responses using OpenAI GPT
- 📋 Clipboard automation with `pyperclip`
- 💬 Automatically pastes and sends replies
- 🔄 Continuous chat monitoring

---

## 🛠️ Tech Stack

- Python 3.x
- OpenAI API
- PyAutoGUI
- Pyperclip

---

## 📦 Libraries Used

Install the required libraries:

```bash
pip install pyautogui pyperclip openai
```

---

## 📁 Project Structure

```
Auto-Reply-AI-Chatbot/
│
├── main.py              # Main application
├── requirements.txt     # Required Python packages
├── README.md            # Project documentation
└── assets/              # Images (optional)
```

---

## 🚀 How It Works

1. Opens the chat application.
2. Selects and copies recent chat history.
3. Reads the copied text from the clipboard.
4. Checks whether the latest message is from the target user.
5. Sends the conversation to the OpenAI GPT model.
6. Generates a humorous AI response.
7. Pastes the response into the chat.
8. Presses **Enter** to send the message.
9. Repeats the process continuously.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Auto-Reply-AI-Chatbot.git
```

### Navigate to the project folder

```bash
cd Auto-Reply-AI-Chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set your OpenAI API Key

Replace:

```python
api_key = "YOUR_API_KEY"
```

with your own API key.

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💡 Skills Demonstrated

- Python Automation
- Desktop Automation
- AI Integration
- OpenAI API
- Clipboard Management
- Prompt Engineering
- Python Programming

---

## 🔮 Future Improvements

- GUI using Tkinter or CustomTkinter
- Support for multiple users
- Voice-controlled responses
- Conversation memory
- Sentiment analysis
- Local AI model support
- Cross-platform compatibility

---

## ⚠️ Limitations

- Works only with supported desktop chat applications.
- Requires a valid OpenAI API key.
- Screen coordinates may need adjustment for different screen sizes.
- Interface changes in the chat application may require updating the automation script.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Arjun Kumar Giri**

- 🌐 GitHub: https://github.com/arjunkumargiri07
- 📧 Email: arjunkumargiri07@gmail.com

---

⭐ If you found this project helpful, don't forget to **Star** the repository!
