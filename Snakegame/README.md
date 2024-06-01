# Snake Game

This repository contains a classic Snake game implemented using Pygame. The game logic, rendering, and control mechanisms are modularized into separate Python files for better readability and maintainability.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/SanjeevM2004/DSA_projects/tree/main/Snakegame
    cd Snakegame
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

To run the game, execute the `app.py` file:

```sh
python snakegame.py
```
## Project Structure

```bash
snake-game/
│
├── game_constants.py    # Contains constants like colors, screen dimensions, and snake speed
├── game_functions.py    # Contains helper functions for displaying score and game over
├── game_logic.py        # Contains the main game loop and logic
├── app.py               # Main entry point to run the game
├── requirements.txt     # List of dependencies
├── Dockerfile           # Docker configuration file
└── README.md            # Project documentation
```
