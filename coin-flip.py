import random
import os
os.chdir("Assignment-4/Coin-Flip")

results = []

class coinFlip:
    def __init__(self):
        pass

    def __store(self):
        with open("results.txt", "w") as file:
            for value in results:
                file.write("True" if value else "False")
            file.close()

    def flipIt(self):
        while len(results) < 100:
            flip = random.random()
            if flip > 0.5:
                result = True
            else:
                result = False
            results.append(result)
        self.__store()



def main():
    coin_flip = coinFlip()
    coin_flip.flipIt()
main()