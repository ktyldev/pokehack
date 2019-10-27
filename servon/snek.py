from flask import Flask, jsonify, request
import json
import random
import pokepy

dex = pokepy.V2Client()

type_lookup = ['normal','fire','water','electric','grass','ice','fighting',\
        'poison','ground','flying','psychic','bug','rock','ghost','dragon',\
        'dark','steel','fairy']

type_matchups = {'normal':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1, 1],
        'fire':[1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1, 1],
        'water':[1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1, 1],
        'electric':[1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1],
        'grass':[1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1, 1],
        'ice':[1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1, 1],
        'fighting':[2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5, 1],
        'poison':[1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2, 1],
        'ground':[1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1, 1],
        'flying':[1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
        'psychic':[1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1, 1],
        'bug':[1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5, 1],
        'rock':[1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1],
        'ghost':[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5, 1, 1],
        'dragon':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0, 1],
        'dark':[1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5, 0.5, 1],
        'steel':[1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2, 1],
        'fairy':[1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1, 1, 1]}

class Muve:
    def __init__(self, moveId):
        move = dex.get_move(moveId)

class Pokeman:
    def __init__(self, pkmnId):
        pkmn = dex.get_pokemon(pkmnId)

class Baddel:
    one = {"tag":False}
    two = {"tag":False}
    one['moov'] = False
    two['moov'] = False
    ready = False
    
    def setup(self):
        self.one['tag'] = True
        self.one['pkmn'] = 1
        self.one['name'] = 'bulb'
        self.one['moves'] = [1, 2, 3, 4]
        self.one['lvl'] = 7
        pOne = Pokeman(1)
        #for i in self.one['moves']:
            
        self.two['tag'] = True
        self.two['pkmn'] = 7
        self.two['name'] = 'sqrt'
        self.two['moves'] = [9, 8, 6, 5]
        self.two['lvl'] = 7 
        pTwo = Pokeman(7)


    def join(self, pkmnId, name, moveIds, lvl):

        if not self.one['tag']:

            self.one['tag'] = True
            self.one['pkmn'] = pkmnId
            self.one['name'] = name
            self.one['moves'] = moveIds
            self.one['lvl'] = lvl

            pOne = Pokemanz(pkmnId)

            return 'one'
        elif not self.two['tag']:

            self.two['tag'] = True
            self.two['pkmn'] = pkmnId
            self.two['name'] = name
            self.two['moves'] = moveIds
            self.two['lvl'] = lvl

            pTwo = Pokemanz(pkmnId)

            if self.one['tag']:
                self.ready = True

            return 'two'
        else:
            return 'piss off'

    def fite(self, name, moveId):
        if self.ready:
            return 'not enuff peepz'
        if self.one['moov'] and self.two['moov']:
            dudududududuel(name, moveId)
        else:
            if name == self.one['name']:
                
                one_nom = name
                one_mov = moveId

                self.one['moov'] = True

            elif name == self.two['name']:

                two_nom = name
                two_mov = moveId

                self.two['moov'] = True
            
            else:
                return 'silly billy'

    def dudududududuel(self, name, moveId):
            if name == self.one['name']:
                
                dmg(pOne, pTwo, <move>)

            elif name == self.two['name']:

                dudududududuel(self.two['name'])


    def dmg(self, p, po, m):
        '''
            Damage = ((((2 * Level / 5 + 2) * AttackStat * AttackPower /\
                    DefenseStat) / 50) + 2) * STAB * Weakness/Resistance *\
                    RandomNumber / 100
        '''
        
        # STAB if m.type == p.type[s] 1.5


        STAB = 1
        TYPE = 1

        for t in p.pkmn.types:
            if t.type.name == m.type.name:
                STAB = 1.5

        for t in p.pkmn.types:
            for i in range(type_lookup):
                if t.type.name == type_lookup:
                    n = i
                    break
            TYPE *= type_matchup[m.type.name, n]



        dmg = ((((2 * p.lvl / 5 + 2) * p.pkmn.stats[4].base_stat * m.move.power /\
                p.pkmn.stats[3].base_stat) / 50) + 2) * STAB * TYPE *\
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
    print(con)
    
    res = b.join(con['pkmn'], con['name'], con['moves'], con['level'])

    return res

app.add_url_rule('/', 'Home', (lambda: base()))
app.add_url_rule('/hi', 'Hi', (lambda: hi()))
app.add_url_rule('/rdy', 'rdy?', (lambda: b.rdy()))
app.add_url_rule('/plus/<int:num>/<int:pls>', 'Add',
        (lambda num, pls: plus(num, pls)))

DEBUG = True

if DEBUG:
    b.setup()

if __name__ == "__main__":
    #app.run(host='localhost', port=42069)
    app.run(host='192.168.69.1', port=42069)

