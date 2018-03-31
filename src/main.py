import datetime as date
from block import Block

def create_genesis_block():
    # Construct a block with index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    self_index = last_block.index + 1
    self_timestamp = date.datetime.now()
    self_data = "New Block Here: " + str(self_index)
    self_hash = last_block.hash
    return Block(self_index, self_timestamp, self_data, self_hash)

# Start create our blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
# number of blocks to add to blockchain
num_of_blocks_to_add = 25
for i in range(0, num_of_blocks_to_add):
    new_block = next_block(previous_block)
    blockchain.append(new_block)
    previous_block = new_block
    print("New block " + str(new_block.index) + " has been added to blockchain")
    print(" with hash value " + str(new_block.hash))
