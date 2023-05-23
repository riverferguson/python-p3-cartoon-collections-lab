CHEESE = ["cheddar", "gouda", "camembert"]

def roll_call_dwarves(dwarves):
    i = 1
    for name in dwarves:
        print(f'{i}. {name}')
        i += 1

def summon_captain_planet(planteer_calls):
    return [f'{call.title()}!' for call in planteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    for snack in snacks:
        if snack in CHEESE:
            return snack
    return None
    
    
