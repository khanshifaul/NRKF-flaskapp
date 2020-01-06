import random, string
import pyperclip


def random_keygen(size=16, chars=string.ascii_letters + string.digits):
    randkey = ''.join(random.choice(chars) for x in range(size))
    pyperclip.copy(randkey)

if __name__ == "__main__":
    random_keygen()