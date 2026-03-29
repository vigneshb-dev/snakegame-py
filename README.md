# 🐍 2D Snake Game

A classic Snake game built with Python's `turtle` graphics library — fully playable in the terminal with keyboard controls, score tracking, and collision detection.

---

## 📸 Preview

```
┌─────────────────────────────┐
│         Score: 7            │
│                             │
│      ██                     │
│      ██ ██ ██               │
│               🔴            │
│                             │
└─────────────────────────────┘
```

---

## 🎮 Features

- Smooth snake movement with keyboard controls
- Food spawning at random positions
- Score tracking displayed on screen
- Wall collision detection
- Self-collision detection
- Snake grows longer as it eats food
- 180° reversal prevention (snake can't go back into itself)

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `←` Left Arrow | Turn Left |
| `→` Right Arrow | Turn Right |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (turtle is included in the standard library — no pip installs needed)

### Run the Game

```bash
git clone https://github.com/your-username/snake-game.git
cd snake-game
python snake.py
```

---

## 🗂️ Project Structure

```
snake-game/
│
├── snakegame.py       # Main game file
└── README.md      # Project documentation
```

---

## 🧱 Code Structure

The game is organized into four classes:

| Class | Responsibility |
|-------|---------------|
| `snake` | Manages the snake's segments, movement, growth, and turning |
| `food` | Handles food rendering and random repositioning |
| `score` | Tracks and displays the current score |
| `collision` | Renders the Game Over message |

The main game loop handles:
- Screen updates via `screen.tracer(0)` + manual `screen.update()`
- Food collision → grow snake + increment score
- Wall collision → Game Over
- Self collision → Game Over

---

## 🐛 Known Fixes Applied

This project includes several bug fixes over a naive implementation:

- **Score text color** — `.color()` set before `.write()` so text renders correctly
- **Segment alignment** — step size matches the default turtle square size (20px)
- **Key listeners** — registered once outside the game loop, not on every frame
- **180° reversal guard** — prevents the snake from turning directly into itself
- **Food bounds** — food cannot spawn behind the score display area
- **Game Over flush** — `screen.update()` called immediately after Game Over text to ensure it renders

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
