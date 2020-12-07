with open('input.txt') as f:
    seat_binaries = f.read().splitlines()


seat_ids = []

rows = [i for i in range(128)]


for seat_binary in seat_binaries:

    # 128 rows
    # 8 columns
    rows = [i for i in range(128)]
    columns = [i for i in range(8)]


    for character in seat_binary:


        if character == "F":
            rows = rows[:len(rows)//2]
        
        elif character == "B":
            rows = rows[len(rows)//2:]

        elif character == "R":
            columns = columns[len(columns)//2:]

        elif character == "L":
            columns = columns[:len(columns)//2]

    
    row = rows[0]
    column = columns[0]

    seat_ids.append((row * 8) + column)

print(max(seat_ids))