# Tic Tac Toe

This repository contains a Tic Tac Toe game implemented using Python and Pygame. The game logic is encapsulated in a class, and a simple graphical user interface is provided using Pygame.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/tic-tac-toe.git
    cd tic-tac-toe
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the game, execute the `main.py` file:

```sh
python main.py
```

## Project Structure
```bash
tic-tac-toe/
│
├── tictactoe.py          # Contains the TicTacToe class
├── main.py               # Main entry point to run the game
├── ui.py                 # UI functions using Pygame
├── requirements.txt      # List of dependencies
├── Dockerfile            # Docker configuration file
└── README.md             # Project documentation
```