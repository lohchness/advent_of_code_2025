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
                if len(str(i)) % 2 == 1: continue

                if str(i)[0:int(len(str(i))/2)] == str(i)[int(len(str(i))/2)::]:
                    invalid_sum += i
        
    return invalid_sum

if __name__ == "__main__":
    # print(day_1(sys.argv[1]))
    print(day_2(sys.argv[1]))