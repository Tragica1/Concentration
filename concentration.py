import random

def is_web():
    return "__BRYTHON__" in globals()

def write(message, end='\n'):
    if is_web():
        from browser import document
        console = document.getElementById('console')
        p = document.createElement('p')
        p.textContent = '> ' + message
        console.appendChild(p)
        console.scrollTop = console.scrollHeight
    else:
        print(message, end=end)


async def read():
    if is_web():
        from browser import document, aio
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value
                event.target.value = ''
                write(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        from browser import aio
        aio.run(function())
    else:
        import asyncio
        asyncio.run(function())


async def concentration():
    write('\t\t\t CONCENTRATION')
    write('\t       CREATIVE COMPUTING  MORRISTOWN NEW JERSEY')
    write('\n\n\n')
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
                write('FIRST CARD?', end=' ')
                u = int(await read())
                if u < 0 or u > 52:
                    write(f'THERE ARE ONLY 52 CARDS IN THE DECK, NOT {u}')
                elif cards[u-1] == ' ':
                    write('YOU HAVE ALREADY MATCHED THAT CARD.')
            while((w < 0 or w > 52) or u==w or cards[w-1] == ' '):
                write('SECOND CARD?', end=' ')
                w = int(await read())
                if w < 0 or w > 52:
                    write(f'THERE ARE ONLY 52 CARDS IN THE DECK, NOT {w}')
                elif u == w:
                    write("YOU CAN'T PICK THE SAME CARD TWICE!")
                elif cards[w-1] == ' ':
                    write('YOU HAVE ALREADY MATCHED THAT CARD.')
            if (cards[u-1][0] == cards[w-1][0]):
                write(f"THAT'S A MATCH --{cards[u-1]}\t {cards[w-1]}")
                cards[u-1] = ' '
                cards[w-1] = ' '
                score += 1
                write(f"YOUR SCORE IS NOW {score}  YOU HAVE HAD  {n+1} PICKS.")
            else:
                write(f"# {u} IS {cards[u-1]}        # {w} IS {cards[w-1]}")
                write('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                write('\n')
                u = -1
                w = -1

        s1 = score/((n+1)/4)
        write(f"YOU SCORED {score} OUT OF {n+1}. THAT IS ", end="")
        if s1 <= 2:
            write("POOR.")
        elif s1 <= 3:
            write("FAIR.")
        elif s1 <= 4:
            write("GOOD.")
        elif s1 <= 5:
            write("EXCELLENT ! ! !")
        else:
            write(". . . AAAH . . . UH....YOU MUST HAVE CHEATED!")

        write('DO YOU WANT TO PLAY AGAIN? ', end='')
        z = await read()
        if z != "YES":
            write('\nCOME BACK AGAIN!!')
            break
            

run(concentration)