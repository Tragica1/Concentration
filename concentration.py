import random


def concentration():
    print('\t\t\t CONCENTRATION')
    print('\t       CREATIVE COMPUTING  MORRISTOWN NEW JERSEY')
    print('\n\n\n')
    z = 'YES'

    while z == 'YES':
        score = 0
        cards = [
            "AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS", "KS",
            "AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH", "KH",
            "AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD", "KD",
            "AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC", "KC"
        ]
        random.shuffle(cards)
        u, w = -1, -1

        for n in range(26):
            while((u < 0 or u > 52) or cards[u-1] == ' '):
                print('FIRST CARD?', end=' ')
                uu = input()
                u = int(uu)
                if u < 0 or u > 52:
                    print(f'THERE ARE ONLY 52 CARDS IN THE DECK, NOT {u}')
                elif cards[u-1] == ' ':
                    print('YOU HAVE ALREADY MATCHED THAT CARD.')
            while((w < 0 or w > 52) or u==w or cards[w-1] == ' '):
                print('SECOND CARD?', end=' ')
                ww = input()
                w = int(ww)
                if w < 0 or w > 52:
                    print(f'THERE ARE ONLY 52 CARDS IN THE DECK, NOT {w}')
                elif u == w:
                    print("YOU CAN'T PICK THE SAME CARD TWICE!")
                elif cards[w-1] == ' ':
                    print('YOU HAVE ALREADY MATCHED THAT CARD.')
            if (cards[u-1][0] == cards[w-1][0]):
                print(f"THAT'S A MATCH --{cards[u-1]}\t {cards[w-1]}")
                cards[u-1] = ' '
                cards[w-1] = ' '
                score += 1
                print(f"YOUR SCORE IS NOW {score}  YOU HAVE HAD  {n+1} PICKS.")
            else:
                print(f"# {u} IS {cards[u-1]}        # {w} IS {cards[w-1]}")
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                print('\n')
                u = -1
                w = -1

        s1 = score/((n+1)/4)
        print(f"YOU SCORED {score} OUT OF {n+1}. THAT IS ", end="")
        if s1 <= 2:
            print("POOR.")
        elif s1 <= 3:
            print("FAIR.")
        elif s1 <= 4:
            print("GOOD.")
        elif s1 <= 5:
            print("EXCELLENT ! ! !")
        else:
            print(". . . AAAH . . . UH....YOU MUST HAVE CHEATED!")

        print('DO YOU WANT TO PLAY AGAIN? ', end='')
        z = input()
        if z != "YES":
            print('\nCOME BACK AGAIN!!')
            break
            
if __name__ == '__main__':
    concentration()


'''
pip install pyinstaller 

# Затем перейти в папку с Вашим файлом .py в командной строке (при помощи команды cd) 
# Запустить команду pyinstaller не забудьте указать имя вашего скрипта 

pyinstaller --onefile <your_script_name>.py 
'''