from character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, "Mage", armour = 5)
        self.max_aura = 50
        self.current_aura = self.max_aura
        self.aura_regeneration = 15
        self.magic = 15
        self.max_hp = max_hp # type: ignore
        self.current_hp = max_hp # type: ignore
        self.spells = {
            "Basic Blast": {"method": self.basic_blast, "aura_cost": 15},
            "Fireball": {"method": self.fireball, "aura_cost": 10},
            "Arcane Blast": {"method": self.arcane_blast, "aura_cost": 50},
            "Wand strike": {"method": self.wand_strike, "aura_cost": 15},
            "Shield Spell": {"method": self.shield_spell, "aura_cost": 5},
        }

    def choose_spell(self, target):
        print(f"Choose an spell (Current Aura: {self.current_aura}):")
        spell_list = list(self.spells.items())
        for i, (spell, info) in enumerate(spell_list):
            print(f"{i + 1}. {spell} (Aura cost: {info['aura_cost']})")
        chosen_spell = int(input("Enter the number of the spell: "))
        if 1 <= chosen_spell <= len(spell_list):
            spell, spell_info = spell_list[chosen_spell - 1]
            if self.current_aura >= spell_info["aura_cost"]:
                self.current_aura -= spell_info["aura_cost"]
                spell_method = spell_info["method"]
                spell_method(target)
            else:
                print("Not enough aura for this spell.")
        else:
            print("Invalid spell.")

def regenerate_aura(self):
        self.current_aura = min(self.max_aura, self.current_aura + self.aura_regeneration)

def spell(self, target):
        damage = self.magic* self.level 
        target.take_damage(damage)  # Apply damage to the target
        return damage  # Return the amount of damage dealt

def fireball(self, target):
        print(f"{self.name} throws a fireball at {target.name}!")
        target.take_damage(self.magic)  # low magic

def basic_blast(self, target):
        damage = self.magic * 2 # does double magic as damage making it powerful earlier therefore making players change their startgeies as they go
        print(f"{self.name} performs a basic blast on {target} for {damage} damage!")
        target.take_damage(damage)

def arcane_blast(self, targets):
        total_damage = 0
        for target in targets:
            damage = self.magic ** 2  # increases exponentially making it much more powerful in later stages 
            total_damage += damage
            print(f"{self.name} blasts {target} for {damage} damage!")
            target.take_damage(damage)
        print(f"{self.name} dealt a total of {total_damage} damage with Arcane Blast!")

def wand_strike(self, target):
        damage = (self.magic + 10 ) * 3 # high multipler due to lower magic then str and dex for other classes
        print(f"{self.name} whacks {target} with their wand for {damage} damage!")
        target.take_damage(damage)

def sheild_spell(self):
        self.armor_class += 15  #massively increases amour class
        print(f"{self.name} casts sheild spell, increasing armor class!")



