from sha256bit import Sha256bit
import random
import time

def generateHash():
    block = ""
    for i in range(50):
        x = str(random.randrange(10))
        block = block + x
        continue
    return block

def difficulty():
    difficulty = random.randrange(1,4)
    return difficulty

def encrypt(text):
    text = Sha256bit(text.encode("ascii")).hexdigest()
    return text

def solveHash():
    prefix_zeroes = "0"*difficulty()
    data = generateHash()
    start = time.time()
    for nonce in range(10000000):
        text = str(data) + str(nonce)
        new_hash = encrypt(text)
        if new_hash.startswith(prefix_zeroes):
            total_time = str((time.time()-start))
            print(f"Block was solved with nonce: {nonce}\nMining at a speed of {total_time} per block.")
            return new_hash

solveHash()