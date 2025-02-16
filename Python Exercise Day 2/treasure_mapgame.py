# Simple Treasure Map Game 

map = [["⬜", "⬜", "⬜"], 
       ["⬜", "⬜", "⬜"], 
       ["⬜", "⬜", "⬜"]]

for row in map:
    print(" ".join(row))


position = input("Enter position (row,col) to hide treasure (e.g., 2,3): ")
row, col = map(int, position.split(","))

map[row - 1][col - 1] = "X"


for row in map:
    print(" ".join(row))
