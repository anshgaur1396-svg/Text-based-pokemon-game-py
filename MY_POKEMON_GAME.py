import random

User_name = input("Enter your name: ")
User_age = int(input("Enter your age: "))
print("\nRead the instruction:-\n1) Look up the name of the pokemon from Poke_list.\n2) Look up their move set and power from under the available pokemon section.\n")

class Pokemon:
    def __init__(self, name, P_type, level, HP, attack, defence, moves):
        self.name = name
        self.P_type = P_type
        self.level = level
        self.HP = HP
        self.attack = attack
        self.defence = defence
        self.moves = moves

    def damage_done(self, damage):
        actual_damage = max(0, damage - self.defence)
        self.HP -= random.randint(0, actual_damage)
        if self.HP < 0:
            self.HP = 0
    
    def fainted(self):
        return self.HP <= 0
    
    def choose_move(self):
        return random.choice(self.moves)
    
    def get_move_power(self, move_name):
        for move in self.moves:
            if move["name"].lower() == move_name.lower():
                return move["Power"]
            elif move['name'] == "Metronome":
                return random.randint(0, 80) 
        return 0
    
    def __str__(self):
        return self.name

def battle(pokemon1, pokemon2):
    while not pokemon1.fainted() and not pokemon2.fainted():
        print("\nAvailable moves:")
        for move in pokemon2.moves:
            print(f" - {move['name']} (Power: {move['Power']})")

        user_move = input("Choose your move: ").strip()

        # Check if move is valid
        valid_moves = [m["name"].lower() for m in pokemon2.moves]
        if user_move.lower() not in valid_moves:
            print(f"Invalid move! {pokemon2.name} got confused and lost its turn...\n")
        else:
            print(f"\n{pokemon2.name} uses {user_move}!")
            damage = pokemon2.attack + pokemon2.get_move_power(user_move)
            pokemon1.damage_done(damage)
            print(f"Wild {pokemon1.name} has HP:{pokemon1.HP} left!\n")

            if pokemon1.fainted() and not pokemon2.fainted():
                print(f"Wild {pokemon1.name} has fainted!")
                print(f"\n{User_name} earned 255 pokedollar!")
                return

        # Opponent’s turn
        move = pokemon1.choose_move()
        print(f"{pokemon1.name} uses {move['name']}!\n")
        damage = pokemon1.attack + move["Power"]
        pokemon2.damage_done(damage)
        print(f"Your {pokemon2.name} has HP:{pokemon2.HP} left!\n")

        if pokemon2.fainted():
            print(f"Your {pokemon2.name} has fainted!")
            return
        
# AVAILABLE POKEMON:-

Pikachu = Pokemon("Pikachu", "Electric", 20, 47, 30, 24,
                  [{"name":"Mega Punch", "Power":65}, 
                  {"name":"Thunderbolt", "Power":75}, 
                  {"name":"Quick Attack", "Power":40}, 
                  {"name":"Thunder Shock", "Power":40}])

Charmander = Pokemon("Charmander", "Fire", 20, 48, 28, 25, 
                    [{"name":"Mega Punch", "Power":65}, 
                    {"name":"Seismic Toss", "Power":30}, 
                    {"name":"Ember", "Power":50}, 
                    {"name":"Scratch", "Power":40}])

Bulbasaur = Pokemon("Bulbasaur", "Grass-Poison", 20, 51, 27, 27, 
                    [{"name":"Tackle", "Power":45}, 
                    {"name":"Body Slam", "Power":65}, 
                    {"name":"Leech Seed", "Power":10}, 
                    {"name":"Vine Whip", "Power":35}])

Squirtle = Pokemon("Squirtle", "Water", 20, 50, 27, 34,
                    [{"name":"Tackle", "Power":40}, 
                    {"name":"Bubblebeam", "Power":65}, 
                    {"name":"Water Gun", "Power":45}, 
                    {"name":"Bite", "Power":65}])

Eevee = Pokemon("Eevee", "Normal", 20, 55, 30, 28,
                [{"name":"Bite", "Power":60}, 
                {"name":"Swift", "Power":60}, 
                {"name":"Quick Attack", "Power":40}, 
                {"name":"Take down", "Power":75}])

Psyduck = Pokemon("Psyduck", "Water-Psychic", 20, 53, 28, 27,
                  [{"name":"Water Gun", "Power": 40},
                  {"name":"Confusion", "Power":50},
                  {"name":"Water Pulse", "Power":60},
                  {"name":"Zen Headbutt", "Power":75}])

Togepi = Pokemon("Togepi", "Fairy", 20, 47, 16, 34,
                [{"name":"Ancient Power", "Power":60},
                {"name":"Zen Headbutt", "Power":80},
                {"name":"Metronome", "Power": random.randint(0,80)}])

print("You stepped into tall grass!\n")

Poke_list = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Eevee", "Psyduck","Togepi"]
Poke_dict_comp = {"Pikachu":Pikachu, 
            "Charmander":Charmander, 
            "Bulbasaur":Bulbasaur, 
            "Squirtle":Squirtle, 
            "Eevee":Eevee,
            "Psyduck":Psyduck,
            "Togepi":Togepi}

Poke_dict_User = {"pikachu":Pikachu, 
            "charmander":Charmander, 
            "bulbasaur":Bulbasaur, 
            "squirtle":Squirtle, 
            "eevee":Eevee,
            "psyduck":Psyduck,
            "togepi":Togepi}

pokemon1 = Poke_dict_comp.get(random.choice(Poke_list))
print(f"A wild {pokemon1} appeared!\nlevel: {pokemon1.level}\nHP: {pokemon1.HP}\nType: {pokemon1.P_type}\n")

print(Poke_list)
p2 = input("Choose your pokemon: ").strip().lower()

while True:
    if p2 in Poke_dict_User: 
        pokemon2 = Poke_dict_User.get(p2)
        print(f"\nYou chose {pokemon2}!")
        print(f"Level: {pokemon2.level}")
        print(f"HP: {pokemon2.HP}")
        print(f"Type: {pokemon2.P_type}")
        print(f"Attack: {pokemon2.attack}")
        print(f"Defence: {pokemon2.defence}")
        print("Moves:")
        print()
        
        battle(pokemon1, pokemon2)
    elif p2 not in Poke_dict_User:
        print("Invalid name!")
    break

