
data = list()
with open('day4.txt', 'r') as file:
    for line in file:
        data.append(line.rstrip())

def part1():
    total = 0
    
    for line in data:
        card_id, numbers = line.split(':')
        winning_numbers, my_numbers = numbers.split('|')
        winning_set = set(winning_numbers.split())
        my_set = set(my_numbers.split())
        matches = winning_set & my_set
        if matches:
            total += 2 ** (len(matches) - 1)
    
    return total

print(f"Part 1: {str(part1())}")
