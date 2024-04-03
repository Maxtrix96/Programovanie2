with open(R"C:\Users\anton\Desktop\compooter backups\skola\Programovanie\Python\palma strom\alg\mapa.txt", "r", encoding="UTF-8") as f:
    info = f.read()

from collections import deque

processed = info.split("\n")
rows = int(processed[0].split()[0])
columns = int(processed[0].split()[1])

mapa = processed[1:rows+1]
info_row = list(map(int, processed[rows+1].split()))
start_pos = list(map(int, processed[rows+1].split()))[0:2]
instruction_count = list(map(int, processed[rows+1].split()))[2]
instructions = [(instruction[0], int(instruction[2:])) for instruction in processed[rows+2:]]

directions = deque(["up", "left", "down", "right"])
turn_direction = {"L": 1, "P": -1}
facing = ""

print(instructions)

def main():
    for move in instructions:
        directions.rotate(turn_direction[move[0]])