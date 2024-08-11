from queue import Queue
input = list()

with open('day4.txt','r') as file:
    for line in file:
        input.append(line.rstrip())

def part1():
    total = 0
    for line in input:
        card_id, numbers = line.split(':')
        winner, my = numbers.split('|')
        winner_set = set(winner.split())
        my_set = set(my.split())
        matches = winner_set & my_set
        if matches:
            # print(cards[0])
            # print(matches)
            total += 2 ** (len(matches) - 1)
        # print(total)
    return total


def part2():
    total = 0
    d = {}
    q = Queue()
    for line in input:
        card_id, numbers = line.split(':')
        card_id = int(card_id[4:])
        winner, my = numbers.split('|')
        winner_set = set(winner.split())
        my_set = set(my.split())
        matches = winner_set & my_set
        d[card_id] = len(matches)
        q.put(card_id)

    while not q.empty():
        total += 1
        k = q.get()
        for i in range(k+1, k+d[k] + 1):
            q.put(i)
    return total




print(f"Part 1: {str(part1())}")
print(f"Part 2: {str(part2())}")
