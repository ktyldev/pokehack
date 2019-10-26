from flask import Flask, jsonify, request
import json
import pokepy

class Baddel:
    one = {"tag":False}
    two = {"tag":False}
    ready = False
    
    def join(self, pkmnId, name, moveIds):
        if not self.one["tag"]:
            self.one["tag"] = True
            self.one["pkmn"] = pkmnId
            self.one["name"] = name
            self.one["moves"] = moveIds
            return 'one'
        elif not self.two["tag"]:
            self.two["tag"] = True
            self.two["pkmn"] = pkmnId
            self.two["name"] = name
            self.two["moves"] = moveIds
            return 'two'
        else:
            return 'piss off'

    def start(self):
        if self.one["tag"] and self.two["tag"]:
            return 'woo'

    def sho(self):
        print(self.one, self.two)


app = Flask(__name__)

b = Baddel()


def base():
    return 'Hey'

def hi():
    b.sho()
    return 'Hi There...'

def plus(num, pls):
    ans = num + pls
    return str(ans)


@app.route('/joinson', methods = ['POST'])
def joinson():
    con = request.json
    
    res = b.join(con['pkmn'], con['name'], con['moves'])

    return res

app.add_url_rule('/', 'Home', (lambda: base()))
app.add_url_rule('/hi', 'Hi', (lambda: hi()))
app.add_url_rule('/plus/<int:num>/<int:pls>', 'Add',
        (lambda num, pls: plus(num, pls)))

if __name__ == "__main__":
    app.run(host='localhost', port=42069)


