# Who wants to be a Millionaire??

# The progression in this "short" version of millionaire should be:
# 1 answer correct: $500
# 2 answers correct: $1000
# 3 answers correct: $5000
# 4 answers correct: $20000
# 5 answers correct: $50000
# 6 answers correct: $250000
# 7 answers correct: $500000
# 8 answers correct: $1000000

# Your code here!
player_name = input("Welcome to Millionaire! What is your name? ")
money_made = 0
def correct():
    return "Correct"
def incorrect():
    return "I'm sorry, you are incorrect."
answer_1 = input(">>")
answer_1 = answer_1.lower()
print (f"Currently you have made ${money_made}.")
print ("You are a millionaire!")
print (correct())

