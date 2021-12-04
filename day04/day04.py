import numpy as np

class BingoBoard:
    
    def __init__(self, data):
        self.table = np.array(list(map(lambda x: x.split(), data)), dtype=int)
        self.crossed_table = np.zeros((5,5))
        
    def update_number(self, number):
        self.crossed_table[self.table == number] = 1
    
    def check_if_won(self, number):
        row_check = np.all(self.crossed_table, axis=0)
        col_check = np.all(self.crossed_table, axis=1)
        if True in row_check or True in col_check:
            return True
        else:
            return False
            
    def get_uncrossed_sum(self):
        return np.sum(self.table[np.where(self.crossed_table == 0)])
        
with open("input.txt", "r") as file:
    data = file.read().splitlines()
    
numbers = [int(i) for i in data[0].split(",")]
boards = [BingoBoard(data[i:i+5]) for i in np.arange(2, len(data[2:]), 6)]

def part_one(boards):
    bingo = False
    for number in numbers:
        if bingo:
            break
        for board in boards:
            board.update_number(number)
            if board.check_if_won(number):
                bingo = True
                print(board.get_uncrossed_sum() * number)
                
def part_two(boards):
    boards_with_bingo = []
    final_scores = []
    for number in numbers:
        for board in boards:
            board.update_number(number)
            if board.check_if_won(number) and board not in boards_with_bingo:
                boards_with_bingo.append(board)
                final_scores.append(board.get_uncrossed_sum() * number)
    print(final_scores[-1])
    
part_two(boards)