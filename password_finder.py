def solve():
    position = 50          # dial starts in the middle
    password = 0           # number of times we land on 0
    MOD = 100              # dial range is 0–99

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]        # 'R' or 'L'
            value = int(line[1:])      # number after it

            if direction == 'R':
                position = (position + value) % MOD
            elif direction == 'L':
                position = (position - value) % MOD
            else:
                raise ValueError("Invalid direction in line: " + line)

            # Check if we landed on 0
            if position == 0:
                password += 1

    print("Password:", password)


if __name__ == "__main__":
    solve()
