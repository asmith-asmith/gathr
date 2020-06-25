
# GATHR SHOP
### Welcome! We are GATHR, a non-traditional fundraising enviornment fostering support for cause-based organizations through unique and locally designed swag. Here we create community and unity around shared causes.




## Views During Play

![GATHR](https://i.imgur.com/jS7YDoJ.png?1

A clear message above the board indicates whose turn it is.
![Turn message](https://i.imgur.com/fXg7jSd.png)

When a player wins, a congratulatory message is displayed. Rejoice in your win!
![Win Message](https://i.imgur.com/h3Yz3MZ.png)

A button lies below the board to restart your game at any point (during a game or after a win).
![Refresh button](https://i.imgur.com/bSlCGJ7.png)




## Technologies Used:
- JavaScript
- CSS
- HTML




## Getting Started:
[GATHR SHOP](https://gathrshop.herokuapp.com/)


In Mancala, there are several rules that must be honored to move and score "points".

**Game Play Steps**

- Player in turn can click on any cup on their side of the board as long as their are player pieces in it (zero pieces in a cup means it is an invalid cup and cannot be played).
- The number of player pieces in a clicked cup will be stored in a hand and then played in a counter clockwise fashion, setting 1 pieces in each following cup until  the original hand is empty.
    - If a player's hand still has pieces in it after they've contributed to their Mancala Cup, they must continue the play around the board, placing pieces in their opponent's cups in the continuation of the counterclickwise path until their hand is empty.

**Game Rules**

- The Mancala Cups (larger scoring cups) on either end of the board belong to each player respectively
    - The left Mancala Cup belongs to Player One and the Right Mancala Cup belongs to Player Two
- During a player's turn, they can only contribute to their own Mancala Cup when applying their play to the board, but must deposit player pieces in the the opponent's playing cups is their hand still contains stone.
- If the last stone of the player's turn lands in their Mancala Cup, they get a bonus play and can click on any cup on their side of the board as long as they have stones in it. Counter-clockwise path applies to all plays.

**Scoring**

- A game ends when one of the players has no more pieces on their side of the board, *however*, the player pieces left over on the other player's side of the board are added to their Mancala Cup.
__*The player with the higher score wins*__




## Next Steps:
In a perfect world, with no project deadlines, all of the following elements would be included in initial deployment. As of now, they will be added at a later time to both optimize the player experience and entice would-be mancala players to pick up a game.
- :thinking: Add additional rule logic (there are a couple more involved rules about continuing plays that lead to more fun and user strategy)
- :musical_note: Add music upon interaction 
- :speech_balloon: Add initial message (preferably in a pop up) that shares a welcome message
- :iphone: Apply responsive design (media queries)
- :computer: Add AI for user to play against a computer opponenet 
- :fire: Add different themed boards