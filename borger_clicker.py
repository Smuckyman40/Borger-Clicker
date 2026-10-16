import sys

if sys.platform == "win32":
    import os
    import time
    import msvcrt
    import json
    
    cash = 0
    cps = 0
    
    os.system('cls')
    print("\003[2J\033[H\033[?25l")
    
    def draw_screen():
        print("\033[H= BORGER CLICKER 1.0 =\033[K")
        print("==== MADE IN NP++ ====\033[K")
        print("===== FOR PYTHON =====\033[K")
        print(f"Borgers: {cash}\033[K")
        print(f"BPS: {cps:.3f}\033[K")
        print("====== Upgrades ======")
        print(f"Autoclickers: {upgrades['Autoclicker'].amount} | Cost: {upgrades['Autoclicker'].cost} | +0.333 BPS (Press A to buy)")
        print(f"Grills: {upgrades['Grill'].amount} | Cost: {upgrades['Grill'].cost} | +1 BPS (Press B to buy)")
        
    class Upgrade:
        def __init__(self, name, cost, cps, amount=0, timer=0):
            self.name = name
            self.cost = cost
            self.cps = cps
            self.amount = amount
            self.timer = 0
        
    upgrades = {
        "Autoclicker": Upgrade("Autoclicker", 15, 300),
        "Grill": Upgrade("Grill", 85, 100)
    }
    
    def save_game():
        data = {
        "cash": cash,
        "cps": cps,
        "autoclickers": upgrades["Autoclicker"].amount,
        "autocost": upgrades["Autoclicker"].cost,
        "grills": upgrades["Grill"].amount,
        "grillcost": upgrades["Grill"].cost
        }
        with open("savegame.txt", "w") as f:
            json.dump(data, f)
            
    def load_game():
        global cash
        try:
            with open("savegame.txt", "r") as f:
                data = json.load(f)
                cash = data["cash"]
                cps = data["cps"]
                upgrades["Autoclicker"].amount = data["autoclickers"]
                upgrades["Autoclicker"].cost = data["autocost"]
                upgrades["Grill"].amount = data["grills"]
                upgrades["Grill"].cost = data["grillcost"]
        except FileNotFoundError:
            pass
    
    load_game()
    
    while True:
        draw_screen()
        for upgrade in upgrades.values():
            if upgrade.amount > 0:
                upgrade.timer += 1
                if upgrade.timer > upgrade.cps:
                    cash += upgrade.amount
                    upgrade.timer = 0
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == ' ':
                cash += 1
            elif key == 'a':
                if cash >= upgrades["Autoclicker"].cost:
                    cps += 1 / 3
                    cash -= upgrades["Autoclicker"].cost
                    upgrades["Autoclicker"].amount += 1
                    upgrades["Autoclicker"].cost = int(upgrades["Autoclicker"].cost * 1.5)
            elif key == 'b':
                if cash >= upgrades["Grill"].cost:
                    cps += 1
                    cash -= upgrades["Grill"].cost
                    upgrades["Grill"].amount += 1
                    upgrades["Grill"].cost = int(upgrades["Grill"].cost * 1.5)
            elif key == '0':
                break
        time.sleep(0.01)
else:
    print("Whoops! Your system cannot run Borger Clicker. Windows only! Sorry...")
print("Thanks for playing!")
time.sleep(1)
save_game()
print("\033[?25h")