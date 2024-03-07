''' **********************************************************
Importing Libraries
***********************************************************'''
import hashlib
import datetime
import pytz
import time
timezone = pytz.timezone('America/Mexico_City')

''' **********************************************************
Defining Classes
***********************************************************'''
   

class Block:

    '''

    Class to create blockchain elements, or blocks. This contains
    any relevant information and methods needed to transmit messages

    '''

    def __init__(self, timestamp, data):
        self.index = None
        self.timestamp = timestamp
        self.data = str(data)
        self.previous_hash = None
        self.hash = None
        self.next = None

    def calc_hash(self):

        sha = hashlib.sha256()
        sha.update(self.previous_hash.encode('utf-8'))
        sha.update(self.timestamp.encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        
        return sha.hexdigest()

    def __repr__(self):

        
        Properties = [str(self.index), self.timestamp, self.data, self.hash,
                      self.previous_hash]
        Titles = ['Index: ', 'Timestamp: ', 'Data: ', 'SHA256_Hash: ',
                  'Prev_Hash: ']

        str_res = '\n'

        for title, content in zip(Titles, Properties):
            str_res += title + content + '\n'

        return str_res

        
class BlockChain:

    '''

    Class used to generate a blockchain, based on the block class.
    This class, based on linkedlist, determine the chain structure
    and fill any needed information between connected blocks.

    '''    

    def __init__(self):
        # Initializing class variables
        self.head = None

    def IncreaseChain(self, new_block):

        if self.head is None:
            self.head = new_block
            self.head.index = 0
            self.head.previous_hash = '0'
            self.head.hash = self.head.calc_hash()
            return

        block = self.head
        while (block.next is not None):
            block = block.next

        new_block.index = block.index+1
        new_block.previous_hash = block.hash
        new_block.hash = new_block.calc_hash()
        block.next = new_block


    def __repr__(self):
        
        # Method to display the list elements and their order
        if self.head is None:
            text2return = ('Empty blockchain')
            return 

        block = self.head
        txt2return = ''
        # Looping wihtin the list elements
        while block.next is not None:
            txt2return += block.__repr__() + '\n'
            block = block.next

        txt2return += block.__repr__() + '\n'

        print(txt2return)        
     

''' **********************************************************
Defining Functions
***********************************************************'''

def Generating_Blockchains(Messages, delay=0):

    '''

    Function to generate blockchains based on the blockchain class
    and the messages to be transmitted.

    Inputs:

    Messages -> List of messages to be transmitted
    delay -> Time delay between transmitted messages

    Output:

    BlcksChain -> Generated blockchain
    
    '''

    BlcksChain = BlockChain()
    for msg in Messages:
        timestamp = datetime.datetime.now(timezone).strftime("%H:%M:%S %m/%d/%Y")
        BlcksChain.IncreaseChain(Block(timestamp, msg))
        time.sleep(delay)

    return BlcksChain
        

''' **********************************************************
Running Code - Main
***********************************************************'''

if __name__ == "__main__":

    print('\n-------------------- UDACITY CASE --------------------\n')
    
    Messages = ['Some Information']*3
    BlckChain = Generating_Blockchains(Messages, 0)
    BlckChain.__repr__()

    ######################## CUSTOM CASES ###############################

    Case1 = ['Starting Blockchain', 'Message 1', 'Message 2', 'Ending Blockchain']
    Case2 = ['Starting Blockchain', '', None, '', 'Ending Blockchain']
    Case3 = ['¯|_(ツ)_/¯', '( ͡° ͜ʖ ͡°)', '(╯°□°）╯︵ ┻━┻',
             '┻━┻ ︵ ヽ(°□°ヽ)', '┻━┻ ︵ ＼( °□° )／ ︵ ┻━┻',
             '┬─┬ノ( º _ ºノ)', '(ﾉಥ益ಥ）ﾉ ┻━┻', '┬──┬ ¯|_(ツ)',
             '┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻', '┻━┻ ︵ ¯|(ツ)/¯ ︵ ┻━┻',
             'ʕノ•ᴥ•ʔノ ︵ ┻━┻']
    Cases = [Case1, Case2, Case3]
    delays = [0, .5, 1]

    for i, (case, delay) in enumerate(zip(Cases, delays)):

        print('\n--------------------- TEST CASE {}  ---------------------\n'.format(i+1))
        
        BlckChain = Generating_Blockchains(case, delay=delay)
        BlckChain.__repr__()

''' **********************************************************
END
***********************************************************'''
