from hashlib import sha256
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    # difficulty of our PoW algorithm
    difficulty = 2

    #def __init__(self):
    #    self.unconfirmed_transactions = []
    #    self.chain = []
    #    self.create_genesis_block()

    def __init__(self,fromFile=False):
        self.unconfirmed_transactions = []
        self.chain = []
        if not fromFile:
            self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def proof_of_work(self, block):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
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
        return new_block.index

    def get_chain(self):
        chain_data = []
        for block in self.chain:
            chain_data.append(block.__dict__)
        return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
    def save_chain(self,filename):
        chain_data = []
        for block in self.chain:
            chain_data.append(block.__dict__)
        with open(filename, 'w') as outfile:
            json.dump({"length": len(chain_data),
                       "chain": chain_data},outfile)
    def load_chain(self,filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            index = 0
            for p in data['chain']:
                print('index: ' , p['index'])
                print('transactions: ' , p['transactions'])
                print('timestamp: ' , p['timestamp'])
                print('previous_hash: ' , p['previous_hash'])
                print('nonce: ' , p['nonce'])
                print('hash: ' , p['hash'])
                print('')
                if index ==0:
                    genesis_block = Block(0, [], p['timestamp'], "0")
                    genesis_block.hash = genesis_block.compute_hash()
                    self.chain.append(genesis_block)
                else :
                    new_block = Block(index=p['index'],
                                  transactions=p['transactions'],
                                  timestamp=p['timestamp'],
                                  previous_hash=p['previous_hash'])
                    proof = self.proof_of_work(new_block)
                    self.add_block(new_block, proof)

                index = index +1

    def load_and_check_chain(self,filename):
        status = True
        with open(filename) as json_file:
            data = json.load(json_file)
            index = 0
            for p in data['chain']:
                if index == 0:
                    index = index +1
                    continue
                print('index: ' , p['index'])
                #print('transactions: ' , p['transactions'])
                #print('timestamp: ' , p['timestamp'])
                #print('previous_hash: ' , p['previous_hash'])
                #print('nonce: ' , p['nonce'])
                #print('hash: ' , p['hash'])
                #print('')
                new_block = Block(index=p['index'],
                                  transactions=p['transactions'],
                                  timestamp=p['timestamp'],
                                  previous_hash=p['previous_hash'])
                proof = self.proof_of_work(new_block)
                val = self.is_valid_proof(new_block, p['hash'])
                print('isValid:',val)
                if val == False:
                    status = val
                    break

        return status
if __name__ == '__main__':
    # Test Code 1
    #blockchain = Blockchain(fromFile=False)
    #blockchain.add_new_transaction('hello')
    #blockchain.mine()
    #print(blockchain.get_chain())
    #blockchain.save_chain('block3.json')

    #Test Code 2
    # blockchain2 = Blockchain(fromFile=True)
    # blockchain2.load_chain('block.json')
    # blockchain2.add_new_transaction('test')
    # blockchain2.mine()
    # blockchain2.save_chain('block2.json')

    #Test Code 3
    blockchain3 = Blockchain(fromFile=False)
    val = blockchain3.load_and_check_chain('./static/myapp/block/2.json')
    print(val)