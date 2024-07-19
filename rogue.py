from character import Character

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, "Rogue", armour = 7)
        self.max_stamina = 150
        self.current_stamina = self.max_stamina
        self.stamina_regeneration = 50
        self.dexterity = 35
        self.max_hp = max_hp # type: ignore
        self.current_hp = max_hp # type: ignore
        self.attacks = {
            "Stab": {"method": self.stab, "stamina_cost": 50},
            "Slash": {"method": self.slash, "stamina_cost": 80},
            "Cleave": {"method": self.cleave, "stamina_cost": 100},
            "Surprise Attack": {"method": self.surprise_attack, "stamina_cost": 150},
            "Sleath": {"method": self.sleath, "stamina_cost": 30},
        }

    def choose_attack(self, target):
        print(f"Choose an attack (Current stamina: {self.current_stamina}):")
        attack_list = list(self.attacks.items())
        for i, (attack, info) in enumerate(attack_list):
            print(f"{i + 1}. {attack} (Stamina cost: {info['stamina_cost']})")
        chosen_attack = int(input("Enter the number of the attack: "))
        if 1 <= chosen_attack <= len(attack_list):
            attack, attack_info = attack_list[chosen_attack - 1]
            if self.current_stamina >= attack_info["stamina_cost"]:
                self.current_stamina -= attack_info["stamina_cost"]
                attack_method = attack_info["method"]
                attack_method(target)
            else:
                print("Not enough stamina for this attack.")
        else:
            print("Invalid attack.")
    
    def regenerate_stamina(self):
        self.current_stamina = min(self.max_stamina, self.current_stamina + self.stamina_regeneration)

    def stab(self, target):
        damage = self.dexterity * 4 #simple attakc but drops armour class because of lower stamina use
        print(f"{self.name} stabs at {target.name}!")
        target.take_damage(damage)
        self.armor_class -= 2

    def slash(self, target):
        damage = self.dexterity * 4 #same attack as above with out armour class lose 
        print(f"{self.name} slashes at {target.name}!")
        target.take_damage(damage)

    def surprise_attack(self, target):
        damage = self.dexterity ** 2 #incredibly strong but leaves you exposed to other attacks making you armour 0 and making stamina 0
        print(f"{self.name} surprises {target.name}!")
        target.take_damage(damage)
        self.armor_class = 0

    def cleave(self, target):
        damage = self.dexterity * 8 #strong but not as strong as surpirse attack becuase it doesn't attack armour class plus lower stamina
        print(f"{self.name} cleaves at {target.name}!")
        target.take_damage(damage)

    def sleath(self, target):
        damage = self.dexterity * 1.5 #small amout of attack but incredily high armour class
        print(f"{self.name} sneaks around {target.name}!")
        target.take_damage(damage)
        self.armor_class += 8


    



    

