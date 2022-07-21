# Provide user with 20 randomized math questions: addition, multiplication,
#  subtraction, and division. Calculate the user's score and average based 
# on getting the answer from the math quiz correct or incorrect.
#  
# Import time and random module 
import random 
import time 
# Initialize score variable to 0 
score = 0 
#Initialize total questions/total right questions variable to 0 
totalAdd_Q = 0 
totalRight_Add_Q = 0 
total_Mult_Q = 0 
totalRight_Mult_Q = 0 
total_Subt_Q = 0 
totalRight_Subt_Q = 0 
total_div_Q = 0 
totalRight_div_Q = 0 
# Display name of program to user 
print("Khurram's Magnificent Math Quiz!") 
# Wait 3 seconds 
time.sleep(3) 
print() 
# Ask user for their name and initialize to variable  
userName = input("Hey there, what's your name? ") 
print() 
# Welcome and thank user for using the program 
print("Welcome to Khurram's Magnificent Math Quiz {}, thanks for choosing us!" .format(userName)) 
# Wait 2 seconds  
time.sleep(2) 
print() 
# Start an infinite loop 
while True: 
    # Ask user if they want to receive instructions 
    # If they say y give them instructions 
    # If they say n don't give them instructions 
    # If they enter invalid value print error message 
    instruction_choice = input("{}, would you like instructions (y/n)? " .format(userName)) 
    if(instruction_choice == "y" or instruction_choice == "n"): 
        break 
    print("Error, please enter a valid input!") 
# Display instruction if y 
if (instruction_choice == "y"): 
    print() 
    print("This program will test you on 20 randomized addition, subtraction, multiplication, and division questions! You are required to press [Enter] after typing your response!") 
    # Wait 2 seconds  
    time.sleep(2) 
    print() 
    print("{} once you have answered all 20 questions, I will provide you with a score and percentage." .format(userName)) 
# Tell user to press [Enter] when they are ready to start  
print() 
print("Press [Enter] when you want to start!") 
input() 
# Start a loop for 20 questions 
for question_num in range(1,21): 
    # Choose a randomized number out of 4 to choose addition, 
    # multiplication, subtraction, and division 
    random_number = random.randint(1,4) 
    # 
    # Initialize to variable find addition numbers from 1 to 20 to add 
    randAddNum1 = random.randint(1,20) 
    randAddNum2 = random.randint(1,20) 
    # Initialize to variable find two random multiplication numbers 
    # from 1 to 10  
    randMultNum3 = random.randint(1,10)
    randMultNum4 = random.randint(1,10) 
    # Two random subtraction numbers, with the largest number being 30 
    randSubtNum5 = random.randint(1,15) 
    randSubtNum6 = random.randint(1,15) 
    # Two random division numbers, from 1 to 10 
    randDivNum7 = random.randint(1,10) 
    randDivNum8 = random.randint(1,10) 
    # Initialize correct addition answer to the sum of the two random numbers 
    correctAddResp = randAddNum1 + randAddNum2 
    # Initialize correct multiplication answer to the product of random numbers 
    correctMultResp = randMultNum3 * randMultNum4 
    # Reverse subtraction to addition in order to make the question 
    Subt_reverse = randSubtNum5 + randSubtNum6
    # Switch to subtraction by replacing the random number with the answer value 
    randSubtNum6 = Subt_reverse - randSubtNum5   
    # Reverse division to multiplication in order to make the question 
    div_reverse = randDivNum7 * randDivNum8 
    # Switch to division by replacing the random number with the answer value 
    randDivNum8 = div_reverse/randDivNum7 
    
# If the random number of 1/4 is chosen ask addition question 
    if (random_number == 1): 
        # Ask user addition question with two random numbers 
        additionResponse = int(input("Get ready {}! What is {} + {}? " .format(userName,randAddNum1,randAddNum2))) 
        # Increase total questions by 1 
        totalAdd_Q = totalAdd_Q+1 
        if (additionResponse == correctAddResp): 
            # If the user is correct congratulate 
            print() 
            print("Nicely done {}, {} is the right answer!" .format(userName,additionResponse)) 
            print() 
            # Increase score by 1 
            score = score+1 
            # Increase total correct questions by 1 
            totalRight_Add_Q = totalRight_Add_Q + 1 
        else: 
            # If wrong tell user the correct answer 
            print() 
            print("Sorry you are incorrect, the correct answer is {}!" .format(correctAddResp)) 
            print() 
    # Elif random number is 2: ask multiplication question of two numbers 
    # between 1 and 10 
    elif (random_number == 2): 
         # Ask user to answer multiplication question 
        multiplicationResponse = int(input("Get ready {}! What is {} X {}? " .format(userName,randMultNum3,randMultNum4))) 
        # Increase total multiplication questions by 1 
        total_Mult_Q = total_Mult_Q + 1 
        if (multiplicationResponse == correctMultResp): 
            # If the user is correct congratulate 
            print() 
            print("Nicely done {}, {} is the right answer!" .format(userName,multiplicationResponse)) 
            print() 
            # Increase score by 1 
            score = score+1 
            # Increase total correct multiplication questions by 1 
            totalRight_Mult_Q = totalRight_Mult_Q + 1 
        else: 
             # If wrong tell user the correct answer 
            print() 
            print("You are incorrect {}, Multiplication can be quite difficult, the correct answer is {}!" .format(userName,correctMultResp)) 
            print() 
    # Elif random number is 3: ask subtraction question of two numbers 
    # with the largest being 30 
    elif (random_number == 3): 
        # Ask user to answer subtraction question 
        subtractionResponse = int(input("Get ready {}! What is {} - {}? " .format(userName,Subt_reverse,randSubtNum5))) 
        # Increase total subtractions questions asked 
        total_Subt_Q = total_Subt_Q + 1 
        # If the answer is correct congratulate 
        if (subtractionResponse == randSubtNum6): 
            print() 
            print("Nicely done {}, {} is the right answer!" .format(userName,randSubtNum6)) 
            print() 
            # Increase total score by 1 
            score=score+1 
            # Increase total right subtraction questions by 1 
            totalRight_Subt_Q = totalRight_Subt_Q + 1 
        else: 
            # If incorrect tell user they are incorrect and the correct answer 
            print() 
            print("You are incorrect {}, the correct answer is {}!" .format(userName,randSubtNum6)) 
            print() 
    # Elif random number is 4: ask division question of two random numbers with 
    # the largest being 10 
    elif (random_number == 4): 
        # Ask user for answer to division question 
        divisionResponse = int(input("Get ready {}! What is {} / {}? " .format(userName,div_reverse,randDivNum7))) 
        # Increase total division questions asked by 1 
        total_div_Q = total_div_Q + 1 
        # If the user response is correct congratulate  
        if (divisionResponse == randDivNum8): 
            print() 
            print("Nicely done {}, {} is the right answer!" .format(userName,divisionResponse)) 
            print() 
            # Increase total score by 1 
            score = score+1 
            # Increase total right division questions by 1 
            totalRight_div_Q = totalRight_div_Q + 1 
        else: 
            # If incorrect tell user they are incorrect and the correct answer 
            print() 
            print("You are incorrect {}, the correct answer is {}!" .format(userName,randDivNum8)) 
# Initialize average variable 
# Calculate average by dividing score by 20 and multiplying by 100 
average = (score/20)*100 
# 
# Tell the user you will analyze the results of their quiz 
print("Finally {}, this quiz is over, let's analyze how you did." .format(userName)) 
print() 
# 
# If the users average is 100 tell user that it was perfect, 
# as well as their percentage and score out of 20 
if (average == 100): 
    print("Wow congratulations {}, you scored perfectly {}/20 questions correct, and had a percentage of {}%!" .format(userName,score,average)) 
    print() 
# 
# If the users average is 85 or above tell user they exceeded expectations 
# as well as their percentage and score out of 20 
elif (average >= 85): 
    print("You exceeded expectations {}, you scored {}/20 questions correct, and had a percentage of {}%!" .format(userName,score,average)) 
    print() 
# 
# If the users average is 70 or below tell them they did not meet expectations 
# as well as their percentage and score out of 20 
elif (average >= 70): 
    print("Well done {}, you met the expectations of this quiz scoring {}/20 questions correct, and achieving a percentage of {}%!" .format(userName,score,average)) 
    print() 
elif (average < 70): 
    print("Work harder {}, you did not meet the expectations for this quiz scoring {}/20 questions correct, and achieving a percentage of {}%." .format(userName,score,average)) 
    print() 
# Display the amount of addition, multiplication, subtraction and division 
# questions the user got correct 
print("Out of the {} addition questions you were given, you got {} correct!" .format(totalAdd_Q,totalRight_Add_Q)) 
print() 
print("Out of the {} multiplication questions you were given, you got {} correct!" .format(total_Mult_Q,totalRight_Mult_Q)) 
print() 
print("Out of the {} subtraction questions you were given, you got {} correct!" .format(total_Subt_Q,totalRight_Subt_Q)) 
print() 
print("Out of the {} division questions you were given, you got {} correct!" .format(total_div_Q,totalRight_div_Q)) 
print() 
print("Thanks again for using Khurram's Magnificent Math Quiz!") 
