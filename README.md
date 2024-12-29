# US State Name Guess Game

A fun and educational game to test your knowledge of US states! Built using Python's Turtle and Pandas modules, this game challenges users to guess state names and provides a visual map.

## Features
- **Interactive Gameplay**: Guess US state names and see them displayed on a map.
- **Visual Feedback**: Correct guesses are marked on the map, and missing states are displayed in red after the game ends.
- **Exit and Save**: Users can exit the game anytime. A CSV file is generated listing the states they did not guess.

## Requirements
- Python 3.x
- Pandas module
- Turtle module (built into Python's standard library)
- A US map image (included in the project files)

## How to Run
1. Clone the repository or download the source code and required map image.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the Pandas module if not already installed:
   ```bash
   pip install pandas
   ```
4. Run the script:
   ```bash
   python main.py
   ```

## How to Play
1. The game starts with a blank map of the US.
2. Type the name of a state in the input box.
   - Correct guesses will appear on the map above the state location.
3. To exit the game, type "exit."
   - The game will stop asking for guesses and generate a CSV file listing the states you did not guess.
   - Missing state names will be displayed in red on the map for visual feedback.

## Screenshot
![Screenshot of the game](blank_states_img.gif)

---

Enjoy playing and learning with the US State Name Guess Game! 🗺️
