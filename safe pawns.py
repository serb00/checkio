def safe_pawns(pawns: set) -> int:
    # add your code here
    pawn_coords = [(int(pawn[1]), ord(pawn[0])) for pawn in pawns]
    safe = 0
    for x, y in pawn_coords:
        if (x - 1, y - 1) in pawn_coords or (x - 1, y + 1) in pawn_coords:
            safe += 1
    return safe


def safe_pawns_opt(pawns: set) -> int:
    return sum((any(chr(ord(p) + i) + str(int(d) - 1)
                    in pawns for i in [-1, 1])) for p, d in pawns)


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns_opt({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
