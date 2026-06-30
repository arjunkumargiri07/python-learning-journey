# 🐍 Snake Water Gun Game

A simple command-line implementation of the classic **Snake, Water, Gun** game using Python. Play against the computer, which makes a random choice each round.

---

## 📖 Overview

Snake Water Gun is a fun game similar to Rock Paper Scissors.

### Game Rules

* 🐍 **Snake** drinks **Water** → Snake wins.
* 💧 **Water** drowns **Gun** → Water wins.
* 🔫 **Gun** kills **Snake** → Gun wins.
* If both players choose the same option, the game ends in a **Draw**.

The computer randomly selects its move, while the player enters their choice through the terminal.

---

## ✨ Features

* 🎮 Interactive command-line gameplay
* 🤖 Random computer opponent
* 🐍 Three possible choices: Snake, Water, Gun
* 🏆 Automatic winner detection
* 📚 Beginner-friendly Python project

---

## 🛠️ Technologies Used

* Python 3
* `random` module

---

## 📂 Project Structure

```text
Snake-Water-Gun/
│── main.py
│── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your computer

### Clone the Repository

```bash
git clone https://github.com/yourusername/Snake-Water-Gun.git
```

### Navigate to the Project

```bash
cd Snake-Water-Gun
```

### Run the Program

```bash
python main.py
```

---

## 🎮 How to Play

Enter one of the following characters when prompted:

| Input | Choice   |
| ----- | -------- |
| `s`   | Snake 🐍 |
| `w`   | Water 💧 |
| `g`   | Gun 🔫   |

### Example

```text
Enter your choice: s

You chose Snake
Computer chose Water

You Win!
```

---

## 🧠 Game Logic

| Player      | Computer    | Result         |
| ----------- | ----------- | -------------- |
| Snake       | Water       | ✅ Player Wins  |
| Water       | Gun         | ✅ Player Wins  |
| Gun         | Snake       | ✅ Player Wins  |
| Same Choice | Same Choice | 🤝 Draw        |
| Otherwise   |             | ❌ Player Loses |

---

## 📌 Future Improvements

* Add score tracking
* Multiple rounds
* Best-of-three mode
* Input validation
* Graphical User Interface (GUI)
* Sound effects
* Multiplayer mode

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.
---

## 👨‍💻 Author

**Arjun Kumar Giri**

* 💻 Computer Science Student
* 🐍 Python Developer
* 🤖 IoT & Embedded Systems Enthusiast
* ☁️ Cloud Enthusiast

---

## ⭐ Support

If you enjoyed this project:

* ⭐ Star this repository
* 🍴 Fork it
* 🐞 Report bugs
* 💡 Suggest new features
* 🤝 Contribute to the project

Happy Coding! 🚀

