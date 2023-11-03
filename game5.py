import random
print("WELCOME TO P B SENTHIL KUMAR GAME WORLD")
print("Programm for PMC TECH HOSUR")
print("'w' (up), 'a' (left), 's' (down), or 'd' (right)")
# Game grid dimensions
GRID_SIZE = 5

# Initialize the player's position
player_x = random.randint(0, GRID_SIZE - 1)
player_y = random.randint(0, GRID_SIZE - 1)

# Initialize the target position
target_x = random.randint(0, GRID_SIZE - 1)
target_y = random.randint(0, GRID_SIZE - 1)

# Main game loop
while True:
    # Print the game grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if i == player_y and j == player_x:
                print("P", end=" ")  # Player's position
            elif i == target_y and j == target_x:
                print("T", end=" ")  # Target position
            else:
                print(".", end=" ")  # Empty cell
        print()

    # Check if the player has reached the target
    if player_x == target_x and player_y == target_y:
        print("Congratulations! You reached the target.")
        break

    # Get the player's move
   
    move = input("Enter a move (w/a/s/d): ").lower()

    # Update the player's position based on the move
    if move == "w" and player_y > 0:
        player_y -= 1
    elif move == "a" and player_x > 0:
        player_x -= 1
    elif move == "s" and player_y < GRID_SIZE - 1:
        player_y += 1
    elif move == "d" and player_x < GRID_SIZE - 1:
        player_x += 1
    else:
        print("Invalid move. Try again.")