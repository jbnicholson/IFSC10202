from random import randint

print("Winner and Losers - Human is Even, Computer is Odd")

remainder = 0
human_score = 0
pc_score = 0
for i in range(1,6):
    print(f"Round: {i}")
    x = int(input("Enter your Guess: "))
    pc_num = randint(1,6)
    print(f"Human Guess: {x} - Computer Guess: {pc_num}")
    total_sum = x + pc_num
    remainder = total_sum % 2
    if remainder != 0:
        print("Sum is Odd")
        pc_score += 1
    elif remainder == 0:
        print("Sum is Even")
        human_score += 1
    
if human_score > pc_score:
    print("Human Wins")
else:
    print("Computer Wins")