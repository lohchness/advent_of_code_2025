import sys


def day_1(instructions: str):
    with open(instructions, "r") as f:
        number = 50
        times_at_zero = 0

        # for i in f.readlines():
        #     direction = i[0]
        #     length = int(''.join(i[1:]))

        #     number += length if direction == "R" else -length
        #     number = number % 100
        #     if number == 0: times_at_zero += 1

        # Naive part two - 6616
        for i in f.readlines():
            direction = i[0]
            length = int(''.join(i[1:]))

            start = number
            end = number + length if direction == "R" else number - length

            for i in range(start, end, 1 if direction == "R" else -1):
                if i % 100 == 0:
                    times_at_zero += 1
                    # print(start, direction+str(length),end)
            
            number += length if direction == "R" else -length
            number = number % 100
    
    return times_at_zero

def day_2(ids: str):

    invalid_sum = 0

    with open(ids, "r") as f:
        ranges_list = f.readline().split(",")
        for i in ranges_list:
            start, end = map(int, i.split("-"))
            for i in range(start, end + 1):
                # if len(str(i)) % 2 == 1: continue

                # if str(i)[0:int(len(str(i))/2)] == str(i)[int(len(str(i))/2)::]:
                #     invalid_sum += i

                # Part 2 - Repeating substring pattern
                if str(i) in (str(i)+str(i))[1:-1]:
                    invalid_sum += i
        
    return invalid_sum

def day_3(inp: str):
    sum_jolts = 0

    def recursive_joltage(digits: list[int], length: int) -> list[int]:
        if length == 1:
            return [max(digits)]
        
        best = max(digits[:-(length  - 1)])
        next_best = digits.index(best)
        
        return [best] + recursive_joltage(digits[next_best + 1:], length - 1)



    with open(inp, "r") as f:
        for bank in f.readlines():
            bank = bank.strip()
            nums = [int(i) for i in bank]
            
            sum_jolts += int("".join(map(str, recursive_joltage(nums, 12))))
            
            # tenth = max(nums[:-1])
            # tenth_index = nums.index(tenth)
            # unit = max(nums[tenth_index + 1:])

            # sum_jolts += tenth * 10 + unit
    
    return sum_jolts

if __name__ == "__main__":
    # print(day_1(sys.argv[1]))
    # print(day_2(sys.argv[1]))
    print(day_3(sys.argv[1]))