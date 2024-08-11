input = list()

with open('day4.txt','r') as file:
    for line in file:
        input.append(line.rstrip())

def part1():
    total = 0
    for line in input:
        cards = line.split(' | ')
        winning = cards[0].split(':')
        winning_number = set(winning[1].split())
        numbers = set(cards[1].split())
        matches = winning_number & numbers
        if matches:
            # print(cards[0])
            # print(matches)
            total += 2 ** (len(matches) - 1)
        # print(total)
    return total


def part2():
    pass

print(f"Part 1: {str(part1())}")
print(f"Part 2: {str(part2())}")
