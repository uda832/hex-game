# Hex Game
- Author: Oyun-Undrakh Yeruultsengel
- Hex Game
- 03/25/2018

## To run:
- Run using python3
```
python3 hex.py
```

## Gameplay:
- The game represents the hexagon and lines using an adjacency matrix. A sample view is as follows.
- Here, this represents the board where there's a dashed line (the number 2) between dots 0 and 1 (at entry [0, 1] and [1, 0])
- Also, there's a solid line (the number 1)  between dots 0 and 2 (at entry [0, 2] and [2, 0])
```
[0, 2, 1, 0, 0, 0]
[2, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
```

At the start, it asks who should start. (AI or the Player). Then continues to ask the player for input and generates the AI's moves using Alpha-Beta pruning search.

```
Who should start the game?
Enter player number (1 for AI, 2 for Player): 
Starting game:

[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
```


## Sample view of the Gameplay, while the AI picks a move:
```
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]

Your turn.
Enter the name of the nodes to connect (example: 0 1): 0 1
[0, 2, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]

AI's turn.
The AI is thinking to pick a move...
```

## Note:
Please note that since the Game Tree is generated all the way to the leaf nodes, the initial few moves for the AI takes a couple minutes.
The very first move on an average laptop took approximately 5 minutes to run.

## Complexity:
- Alpha-Beta pruning has a runtime and space complexity of O((b/2)^m).
- For the hexagon game, the maximum branching factor is b = 15.
