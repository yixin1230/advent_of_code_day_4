from queue import Queue

# Read input data from file and store it in a list
data = list()
with open('day4.txt', 'r') as file:
    for line in file:
        data.append(line.rstrip())

def calculate_total_score():
    total_score = 0
    
    # Iterate through each line in the input data
    for line in data:
        card_id, numbers = line.split(':')  # Split line into card ID and the number sequences
        winning_numbers, my_numbers = numbers.split('|')  # Split number sequences into winning and my numbers
        
        # Convert the number sequences into sets for comparison
        winning_set = set(winning_numbers.split())
        my_set = set(my_numbers.split())
        
        # Find the common numbers (matches) between the winning set and my set
        matches = winning_set & my_set
        
        # If there are any matches, calculate the score and add it to total_score
        if matches:
            total_score += 2 ** (len(matches) - 1)  # Score is 2 raised to the power of (number of matches - 1)
    
    return total_score

def calculate_propagation_effect():
    total_steps = 0
    match_counts = {}  # Dictionary to store the number of matches for each card ID
    queue = Queue()  # Queue to manage the propagation of card IDs
    
    # Iterate through each line in the input data
    for line in data:
        card_id, numbers = line.split(':')  # Split line into card ID and the number sequences
        card_number = int(card_id[4:])  # Extract numeric part of card ID (assuming format "cardXXXX")
        
        winning_numbers, my_numbers = numbers.split('|')  # Split number sequences into winning and my numbers
        
        # Convert the number sequences into sets for comparison
        winning_set = set(winning_numbers.split())
        my_set = set(my_numbers.split())
        
        # Find the common numbers (matches) between the winning set and my set
        matches = winning_set & my_set
        
        # Store the number of matches in the dictionary with card_number as the key
        match_counts[card_number] = len(matches)
        
        # Add the card number to the queue
        queue.put(card_number)
    
    # Process the queue until it's empty
    while not queue.empty():
        total_steps += 1  # Increment the total steps counter
        current_card = queue.get()  # Get the next card from the queue
        
        # Propagate the effect of matches to subsequent card IDs
        for i in range(current_card + 1, current_card + match_counts[current_card] + 1):
            queue.put(i)
    
    return total_steps


# Run both parts and print their results
print(f"Part 1: {str(calculate_total_score())}")
print(f"Part 2: {str(calculate_propagation_effect())}")
