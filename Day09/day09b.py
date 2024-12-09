import util

class Block:
    def __init__(self, block_length, pair_id):
        self.block_length = block_length
        self.pair_id = pair_id

    def __repr__(self):
        #return f"block with pair_id {self.pair_id} and length {self.block_length}"
        if self.pair_id == 'free':
            return '.' * self.block_length
        else:
            return str(self.pair_id) * self.block_length

def main():
    with open("Day09/day09.txt") as f:
        line = [line.strip() for line in f.readlines()][0]

    blocks = []
    files_to_move = []
    for idx, item in enumerate(line):
        if idx % 2 == 0:
            file_block = Block(int(item), int(idx/2))
            blocks.append(file_block)
            files_to_move.append(file_block)
        else:
            blocks.append(Block(int(item), 'free'))

    print('loaded input')

    for file in files_to_move[::-1]:
        for idx, block in enumerate(blocks):
            if block == file:
                break
            if block.pair_id == 'free' and block.block_length >= file.block_length:
                orig_len = block.block_length
                block.block_length = file.block_length
                block.pair_id = file.pair_id

                file.pair_id = 'free'

                new_block = Block(orig_len - file.block_length, 'free')
                blocks.insert(idx + 1, new_block)
                break

    print('done moving files')

    check_sum = 0
    counter = 0
    for block in blocks:
        if block.pair_id != 'free':
            for _ in range(block.block_length):
                check_sum += block.pair_id * counter
                counter += 1
        else:
            counter += block.block_length
    print(check_sum)