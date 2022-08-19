from curses.ascii import isalpha


my_file = open(r"masterlist.txt", "r")
#full_list = my_file.read().replace('\n', ',').split(",")
word_list = my_file.read().replace('\n', ',').split(",")


def cycle_inputs(letters, option):
    if option == 1:
        for i in letters:
            remove_words_with_letters(i)

    elif option == 2:
        for i in letters:
            remove_words_without_letters(i)
    
    print(word_list)


def remove_words_with_letters(letter):  
    for i in reversed(word_list):
        for alpha in range(0,5):
            if letter == i[alpha]:
                word_list.remove(i)
                break


def remove_words_without_letters(letter):

    for i in reversed(word_list):
        flag = -2
        
        for alpha in range(0,5):   
            
            if letter == i[alpha]:
                flag = 1
                break
            
        if flag == -2:
            word_list.remove(i)

def remove_words_without_specified_letter_position(letter, index):
     
    index -= 1
    
    for i in reversed(word_list):
        flag = -2
        
        if letter == i[index]:
            flag = 1
            #break
            
        if flag == -2:
            word_list.remove(i)
    
    print(word_list)


def remove_words_with_specified_letter_position(letter, index):
     
    index -= 1
    
    for i in reversed(word_list):
        #flag = -2
        
        if letter == i[index]:
            #flag = 1
            word_list.remove(i)
            #break
            
        #if flag == -2:
            
    
    print(word_list)

while True:

    print("\nMenu")
    print("1. Remove words with certain letters")
    print("2. Remove words without certain letters")
    print("3. Find words with letters in specific positions")
    print("4. Remove words with letters in specific positions")
    print("5. Print masterlist")
    print("6. Exit")
    
    option = int(input("Please enter your choice: "))

    if option == 1:

        letters = input("Please enter letters: ")
        letters = letters.replace(" ", "")
        
        if letters.isalpha(): 
            cycle_inputs(letters, 1)
        
        else:
            print("Enter an alphabet")

    
    elif option == 2:
        
        letters = input("Please enter letters: ")
        letters = letters.replace(" ", "")
        
        if letters.isalpha(): 
            cycle_inputs(letters, 2)

        else:
            print("Enter an alphabet")
        

    elif option == 3:
       
        letters = input("Please enter one letter: ")

        if letters.isalpha():
            
            if len(letters) == 1:
                
                occurances_of_letter = int(input("Please enter number of times the letter appears: "))
                for x in range(0, occurances_of_letter):

                    position = int(input("\nPlease enter the position: "))
                    
                    if position > 0 and position < 6:
                        remove_words_without_specified_letter_position(letters, position)
                    
                    else: 
                        print("Out of bounds! Input must be between 1 and 5")
                
            else:
                print("Input only one character!")
        
        else:
            print("Enter an alphabet!")

    elif option == 4:
        
        letters = input("Please enter one letter: ")

        if letters.isalpha():
            
            if len(letters) == 1:
                occurances_of_letter = int(input("Please enter number of times the letter appears: "))
                for x in range(0, occurances_of_letter):

                    position = int(input("Please enter the position: "))
                    
                    if position > 0 and position < 6:
                        remove_words_with_specified_letter_position (letters, position)
                    
                    else: 
                        print("Out of bounds! Input must be between 1 and 5")
                
            else:
                print("Input only one character!")
        
        else:
            print("Enter an alphabet!")

   
    elif option == 5:
        #print(full_list)
        pass

    
    elif option == 6:
        print("Quiting...")
        quit()

    
    else:
        print("Wrong option")

