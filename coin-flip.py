import random
import os
os.chdir("Assignment-4/Coin-Flip")

results = []

class coinFlip:
    def __init__(self):
        pass

    def __store(self, value):
        results.append(value) # Stores heads or tails in global results variable

        
    def flipIt(self):
        while len(results) < 100: # repeats until 100 flips are completed
            flip = random.random() # Receives random value between 0 and 1
            # Determines if value is heads or tails
            if flip > 0.5:
                value = "Heads"
            else:
                value = "Tails"
            self.__store(value) # Sends value to store method
    
    def display(self):
        # Initalizing a counter to keep track of columns
        counter = 0
        for result in results: 
            # Prints the value of each coin flip
            print(result, end=" ")
            counter += 1
            if counter == 10: # Adds a newline every 10 inputs to create columns
                print()
                counter = 0 # Reset counter to start the new row
        print() # Print newline for spacing

        # Initalized variables to seperate and store values from results
        heads = []
        tails = []

        for x in results:
            if x == "Heads":
                heads.append(x)
            else:
                tails.append(x)

        # Initialize variables to store the maximum length of runs and the current length of runs for both types
        max_heads_streak = 0
        current_heads_streak = 0
        max_tails_streak = 0
        current_tails_streak = 0

        # Iterate over the results
        for result in results:
            if result == 'Heads':
                # If the result is 'Heads', increment the current streak length for heads
                current_heads_streak += 1
                # Reset the current streak length for tails
                current_tails_streak = 0
                # Update the maximum streak length for heads if necessary
                max_heads_streak = max(max_heads_streak, current_heads_streak)
            elif result == 'Tails':
                # If the result is 'Tails', increment the current streak length for tails
                current_tails_streak += 1
                # Reset the current streak length for heads
                current_heads_streak = 0
                # Update the maximum streak length for tails if necessary
                max_tails_streak = max(max_tails_streak, current_tails_streak)

        # Print outputs
        print("The total number of times the coin was flipped is {}".format(len(results)))
        print("Total Heads: {}".format(len(heads)))
        print("Total Tails: {}".format(len(tails)))
        print(f"The longest run of Head is: {max_heads_streak}.")
        print(f"The longest run of Tail is: {max_tails_streak}.")
        


def main():
    #Initialize obj
    coin_flip = coinFlip()
    #Flip coin
    coin_flip.flipIt()
    #Display results
    coin_flip.display()
main()