from random import randint, choice

def find_lost_element():
     first_element = randint(0, 100)
     
     step = randint(1, 10)
     progression_length = 10 * step
     progression = [str(first_element + n) for n in range(0, progression_length, step)]
     index = randint(0, 9)
     answer = progression[index]
     progression[index] = '..'
     return ' '.join(progression), answer


if __name__ == "__main__":
    print(find_lost_element())