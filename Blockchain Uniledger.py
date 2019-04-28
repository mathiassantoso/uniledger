# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:10:49 2019

@author: mathi
"""

import datetime
import hashlib
import random

class Block:
    
    def __init__(self, previous_block_hash, nonce, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.nonce = nonce
        self.data = data
        self.timestamp = timestamp
            
    def compute_hash(self):
        hash_string = (str(self.previous_block_hash) +
                        str(self.nonce) +
                        str(self.data) +
                        str(self.timestamp))
        return hashlib.sha256(hash_string.encode()).hexdigest()
        
    def create_genesis_block():
        return Block("0", "0", "0", datetime.datetime.now())
    
    #def receive(self, name, dob, bt, age, date, wt, ht, hr, bp, diagnosis, prescription):
        
    
#    def add(self, Data("ab cd", "11/04/2000", "B", 10, "30/03/2019", 11, 1.2, 13, 19, "xyz", "abc")):
#        block_previous_hash = create_genesis_block().compute_hash()
#        block_current_hash = Block(block_previous_hash, "0", Data("ab cd", "11/04/2000", "B", 10, "30/03/2019", 11, 1.2, 13, 19, "xyz", "abc"), datetime.datetime.now().compute_hash()
#Data(name,dob,bt,age,date,wt,ht,hr,bp,diagnosis,prescription),datetime.datetime.now()).compute_hash()
        
    
class Data:
    def __init__(self, p_id, name, dob, bt, age, doc_id, date, wt, ht, hr, bp, diagnosis, prescription):
        self.name = name
        self.dob = dob
        self.bt = bt
        self.age = age
        self.date = date
        self.wt = wt
        self.ht = ht
        self.hr = hr
        self.bp = bp
        self.diagnosis = diagnosis
        self.prescription = prescription
    
    def new_block(prev_hash, p_id, name, dob, bt, age, doc_id, date, wt, ht, hr, bp, diagnosis, prescription):
        return Block(prev_hash, "0", Data(p_id, name, dob, bt, age, doc_id, date, wt, ht, hr, bp, diagnosis, prescription), datetime.datetime.now())

class Blockchain:
    blockchain = [Block.create_genesis_block()]
    genesis_hash = blockchain[-1].compute_hash()
    print("Genesis Hash:", genesis_hash)
    prev_hash = genesis_hash
    deck1 = list(range(1, 1000001))
    random.shuffle(deck1)
    deck2 = list(range(1, 1000001))
    random.shuffle(deck2)
    i = 1
    while i <= 5:
        b = Data.new_block(prev_hash, deck1.pop(), "name "+str(i), "11/04/2000", "B", random.randint(0,100), deck2.pop(), "30/03/2019", random.randint(0,150), 
                           random.uniform(1,2), random.randint(50,150), random.randint(60,120), "xyz", "abc")
        hash_no = b.compute_hash()
        blockchain.append(b)
        prev_hash = hash_no
        print("Block #%d hash: %s" % (i, hash_no))
        i+=1
    print(blockchain)
 