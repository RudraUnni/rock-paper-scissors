# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
# RPS.py

def player(prev_play, opponent_history=[]):
    # Record the opponent's most recent move (if any)
    if prev_play:
        opponent_history.append(prev_play)
    
    # On the very first move (when there's no opponent history), choose a default.
    if not opponent_history:
        return "R"
    
    # Function to choose the counter move:
    # Rock ("R") is beaten by Paper ("P"), Paper ("P") by Scissors ("S"), and Scissors ("S") by Rock ("R")
    counter = {"R": "P", "P": "S", "S": "R"}
    
    # Composite strategy:
    # 1. If the opponent has played the same move three or more times in a row,
    #    assume a repeating pattern and counter that move.
    if len(opponent_history) >= 3:
        if opponent_history[-1] == opponent_history[-2] == opponent_history[-3]:
            return counter[opponent_history[-1]]
    
    # 2. Otherwise, look back over the most recent N moves (for instance, 5) to see which move is most frequent.
    recent_sample = opponent_history[-5:]
    frequency = {"R": recent_sample.count("R"), 
                 "P": recent_sample.count("P"), 
                 "S": recent_sample.count("S")}
    
    # Find the opponent's most common move in the recent sample
    predicted_move = max(frequency, key=frequency.get)
    
    # Use the counter move against the predicted move.
    return counter[predicted_move]


# Optional: If you use main.py for testing, you may include a simple test game.  
if __name__ == "__main__":
    # You can test your function against one of the provided bots from RPS_game.py
    from RPS_game import play, quincy, abbey, kris, mrugesh
    print("Player vs. Quincy:")
    play(player, quincy, 1000, verbose=False)
    print("Player vs. Abbey:")
    play(player, abbey, 1000, verbose=False)
    print("Player vs. Kris:")
    play(player, kris, 1000, verbose=False)
    print("Player vs. Mrugesh:")
    play(player, mrugesh, 1000, verbose=False)

