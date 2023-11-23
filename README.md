# OXO PROJECT (First version)

The purpose of this project is to create a simple Tic Tac Toe game with the following features:
- a three-by-three grid board
- userselected nickname and user icon
- local play and online play with unique game ID assigned
- formation of random or user-chosen couples (whether in local or in on-line version)
- Option of up to 9 rounds with same 2nd player.
- a DB saving top ranking users (opt)

The game features will be described in the following stages. 

## 1st Stage: Welcoming screenview
- Presentation of game name "OXO - Tic Tac Toe"  and company with a background image.
- It includes a box where the user types a nickname, a button to open a user icon carousel to choose someone and three buttons to select the type of play (local, meet online and random partner).
- Hits the *"Start Game"* button to continue (saving user settings in user list and assigning a user ID)

## Optional 2nd Stage: Selection of a partner
- **For local or online play with 2nd player selection:** Open a screenview with second player settings (online search by user ID or userselected icon and nickname for local player). Tap the "Join" button to search/save settings (and join a board with a unique gameid and users variables).
- **For all types of play:** Display a loading screenview when searching/saving the second player settings and configuring the game board.

## 3rd stage: Competitor's presentation
- Assign randomly a player# and mark (x / o)
- Indicate name and user icon of both player in a "player 1 vs player 2" message
- Ask for confirmation by a *Start* or a *Quit* button.
- **Start button:** Assign a game id, create an associated game board and update gameid for both players in users list.

## 4th stage: Game
- Display the three-by-three grid board (defaul blank cells status) with a players heading showing their score (update score after each round) 
- Add a message / color turn indicator.
- Player with "o" mark moves first.
- Show a black users mark when mousing available cells in a turn.
- Press the *Quit* button to leave (player within the game is declared winner )
- **Draw/Tie Case:** all marks turn black and a *Game Over* message appears.
- **Winner Case:** When a player has three consecutive marks (in a row/column/diagonal) they become the color assigned to the player and it is declared winner by showing its icon and nickname on the grid.

# 5th stage: 9 rounds option.
- After finishing first round the game asks if both users want to continue playing with same partner.
- **NO button:** Delete all data. 
- **YES button:** Save last board status in history and reset board to initial status (blank status cells). Then, display a history screenview showing history and players score so far. They start a new play with same board and game id just like 4th stage description. Displaying history after each round.
- After final round or if some player leaves, player with more rounds 

Pass to next stage.

# 6th stage: Top ranking.
- Show a table with top ranking players and position of user with its score so far.
- Ask for registration and add details by a **See more* button.
- Skip registration with a *Quit* button (delete all data).

# Final stage: Goodbye screenview.
- Show game and company names and the message "Hope to see you soon!" with a darker background picture.