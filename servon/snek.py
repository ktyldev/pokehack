from flask import Flask, jsonify, request
import json
import random
import pokepy
'''
class Pokeman:
    def __init__(self, pkmn):
'''

class Baddel:
    one = {"tag":False}
    two = {"tag":False}
    ready = False

    def setup(self):
        self.one['tag'] = True
        self.one['pkmn'] = 1
        self.one['name'] = 'bulb'
        self.one['lvl'] = 7
        self.one['moves'] = [1, 2, 3, 4]
        self.two['tag'] = True
        self.two['pkmn'] = 7
        self.two['name'] = 'sqrt'
        self.two['moves'] = [9, 8, 6, 5]
        self.two['lvl'] = 7


    def join(self, pkmnId, name, moveIds, lvl):

        if not self.one['tag']:

            self.one['tag'] = True
            self.one['pkmn'] = pkmnId
            self.one['name'] = name
            self.one['moves'] = moveIds
            self.one['lvl'] = lvl

            #pOne = Pokemanz(pkmnId)

            return 'one'
        elif not self.two['tag']:

            self.two['tag'] = True
            self.two['pkmn'] = pkmnId
            self.two['name'] = name
            self.two['moves'] = moveIds
            self.two['lvl'] = lvl

            #pTwo = Pokemanz(pkmnId)

            if self.one['tag']:
                self.ready = True

            return 'two'
        else:
            return 'piss off'

    def fite(self, name):
        if not self.one['tag'] or not self.two['tag']:
            return 'not enuff peepz'
        else:
            if name == self.one['name']:

                dudududududuel(self.one['name'])
            elif name == self.two['name']:

                dudududududuel(self.two['name'])

            else:
                return 'silly billy'

    def dudududududuel(self, name):
            if name == self.one['name']:

                print('lolole')
                #pOne.

            elif name == self.two['name']:

                dudududududuel(self.two['name'])


    def dmg(self, p):
        '''
            Damage = ((((2 * Level / 5 + 2) * AttackStat * AttackPower /\
                    DefenseStat) / 50) + 2) * STAB * Weakness/Resistance *\
                    RandomNumber / 100
        '''


        dmg = ((((2 * p.lvl / 5 + 2) * p.atkPwr * p.atkPwr /\
                p.dfn) / 50) + 2) * STAB * p.wkn / p.res*\
                random.uniform(85, 100) / 100


    def sho(self):
        print(self.one, self.two)

    def rdy(self):
        print('rdy?', self.ready)
        return str(self.ready)


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
    jayson = request.json

    con = json.loads(jayson)
    print(jayson)
    print(con)

    #print(con)
    #print(con.pkmn)
    #print(con['pkmn'])
    #print(con['name'])
    #print(con['level'])

    res = b.join(con['pkmn'], con['name'], con['moves'], con['level'])

    return res

app.add_url_rule('/', 'Home', (lambda: base()))
app.add_url_rule('/hi', 'Hi', (lambda: hi()))
app.add_url_rule('/rdy', 'rdy?', (lambda: b.rdy()))
app.add_url_rule('/plus/<int:num>/<int:pls>', 'Add',
        (lambda num, pls: plus(num, pls)))
DEBUG = False

if DEBUG:
    b.setup()

if __name__ == "__main__":
    app.run(host='localhost', port=42069)
    #app.run(host='192.168.69.1', port=42070)
