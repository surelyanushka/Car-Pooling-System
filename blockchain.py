import json
import time
import random
import string


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce


    def compute_hash(self):
        return self.random_string()




    def random_string(self, starts_with='00', stringLength=8):
        letters = string.ascii_lowercase
        return starts_with  + ''.join(random.choice(letters) for i in range(stringLength))






class Blockchain:
    # difficulty
    difficulty = 2


    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()


    def create_genesis_block(self):
   
        genesis_block = Block(0, [], 0, "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)


    @property
    def last_block(self):
        return self.chain[-1]


    def add_block(self, block, proof):
        previous_hash = self.last_block.hash


        if previous_hash != block.previous_hash:
            return False


        if not Blockchain.is_valid_proof(block, proof):
            return False


        block.hash = proof
        self.chain.append(block)
        return True


    @staticmethod
    def proof_of_work(block):


        block.nonce = 0


        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()


        return computed_hash


    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)


    def get_unconfirmed_transactions(self):
        return self.unconfirmed_transactions


    @classmethod
    def is_valid_proof(cls, block, block_hash):
   
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())


    @classmethod
    def check_chain_validity(cls, chain):
        result = True
        previous_hash = "0"


        for block in chain:
            block_hash = block.hash
            # remove the hash field to recompute the hash again
            # using `compute_hash` method.
            delattr(block, "hash")


            if not cls.is_valid_proof(block, block_hash) or \
                    previous_hash != block.previous_hash:
                result = False
                break


            block.hash, previous_hash = block_hash, block_hash


        return result


    def mine(self):
        if not self.unconfirmed_transactions:
            return False


        last_block = self.last_block


        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)


        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)


        self.unconfirmed_transactions = []
        print("New block created")
        return True
