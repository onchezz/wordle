import random
print('wellcome to wordle')

word_file = open('words.txt', 'r');


def get_data(file):
    word_list =[];
    data = file.readlines();
    for word in data:
        word_strip = word.strip()
        word_list.append(word_strip) 
    return word_list;


def get_radom_word(words):
    random_idx = random.randint(0, words.__len__()-1)
    random_word = words[random_idx]
    return random_word;


def letters(word):
   
    letters =[]
    for letter  in  word:
        letters.append(letter)
    return letters;

def hide_unkwon_letters():
    guess = []
    words = get_data(word_file)
    word = get_radom_word(words)
    myletters = letters(word)
    generate_string = ''.join(map(str,myletters))
    print(generate_string)
    user_guess = input("Enter guess your word guess ")
    user_letters = letters(user_guess.strip())
    for let in myletters:
        for char in user_letters:
            if let == char:
                guess.append(let)
             
            else:
                guess.append('_')
    return guess;
    
    

print(f'{hide_unkwon_letters()}')
    