input = [20, 9, 11, 0, 1, 2]


# input = [3,1,2]


def play(num):
    memory = {input[x]: x + 1 for x in range(len(input) - 1)}
    current_turn = len(input)
    current_num = input[len(input) - 1]
    while current_turn < num:

        if current_num in memory:
            temp_num = current_num
            current_num = current_turn - memory[current_num]
            memory[temp_num] = current_turn
        else:
            memory[current_num] = current_turn
            current_num = 0

        current_turn += 1
    return current_num


# part 1
print(play(2020))

# part 2
print(play(30000000))
