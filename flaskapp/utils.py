import random, string
import pyperclip


def random_keygen(size=32, chars=string.ascii_letters + string.digits):
    randkey = ''.join(random.choice(chars) for x in range(size))
    print(randkey)
    return pyperclip.copy(randkey)

def create_db():
    from flaskapp import app, db
    db.create_all()


if __name__ == "__main__":
    random_keygen()