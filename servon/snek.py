from flask import Flask, jsonify

class Baddel:
    def __init__(self):
        self.hoho = 'ehehe'

    def rekt(self):
        return 'ownd'
    def ownd(self):
        return self.hoho

def base():
    return 'Hey'

def hi():
    return 'Hi There...'

def plus(num, pls):
    ans = num + pls
    return str(ans)

app = Flask(__name__)

b = Baddel()

app.add_url_rule('/ownd', 'Ownd', (lambda: b.ownd()))
app.add_url_rule('/rekt', 'Rekd', (lambda: b.rekt()))

app.add_url_rule('/', 'Home', (lambda: base()))
app.add_url_rule('/hi', 'Hi', (lambda: hi()))
app.add_url_rule('/plus/<int:num>/<int:pls>', 'Add',
        (lambda num, pls: plus(num, pls)))

if __name__ == "__main__":
    app.run(host='192.168.69.1', port=42069)


