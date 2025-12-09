from prototype_interface import Prototype
import copy

class EnemyPrototype(Prototype):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Enemy: {self.name}, Health: {self.health}, Attack Power: {self.attack_power}"
    
def client_code(prototype: Prototype):
    prototype_clone = prototype.clone()
    print(f"Cloned enemy: {prototype_clone}")
    
    # Customizing the cloned enemy
    prototype_clone.name = "Customized Enemy"
    prototype_clone.health += 50
    prototype_clone.attack_power += 1.5
    
    print(f"Customized enemy: {prototype_clone}")

if __name__ == "__main__":
    # Create a prototype enemy
    prototype_enemy = EnemyPrototype("Skeleton", 100, 5)
    print("Original enemy: ", prototype_enemy)
    # Use the prototype to clone an enemy
    client_code(prototype_enemy)
