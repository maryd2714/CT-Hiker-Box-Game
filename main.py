""""
1)import modules
2)def functions
3)def main function
4)call main
---------------------------------------------------
import modules
---------------------------------------------------
"""
import random
# import turtle
"""
---------------------------------------------------def functions
---------------------------------------------------
"""
def keepChoosing():
    while True:
        print()
        answer = input("Would you like to take anything else? ")
        answer = answer.lower()
        if answer.startswith("y"):
            return True
            break
        if answer.startswith("n"):
            return False
            break
        else:
            print("Wait, I'm confused.")

def toContinue():
    while True:
        answer = input("Would you like to try again? ")
        answer = answer.lower()
        if answer.startswith("y"):
            return True
            break
        if answer.startswith("n"):
            return False
            break
        else:
            print("Wait, I'm confused.")

def isVegan():
    while True:
        answer = input("Are you a vegan? ")
        answer = answer.lower()
        if answer.startswith("y"):
            return True
            break
        if answer.startswith("n"):
            return False
            break
        else:
            print("Wait, I'm confused.")

def isShoeSize():
    while True:
        answer = input("What is your shoe size? ")
        if answer.isnumeric() and 5 <= int(answer) <= 15:
            return int(answer)
            break
        else:
            print(
                "That is not a valid shoe size. Whole numbers between 5 and 15 only, please."
            )

def player(name):
    """generate list of attributes based on player input"""
    if name.title() == "Demo":
        print("DEMO")
        print
        return "Brighticorn", True, 5, 18, 2, 0
    elif name.title() == "Test Vegan":
        print("TEST VEGAN")
        print()
        return "Touille", True, 9, 18, 2, 0
    elif name.title() == "Test Not Vegan":
        print("TEST NOT VEGAN")
        print()
        return "Galactica", False, 13, 18, 2, 0
    else:
        trail_name = name.title()
        vegan = isVegan()
        shoe_size = isShoeSize()
        pack_weight = 18
        days_of_food = 2
        days_of_fuel = 0
        return trail_name, vegan, shoe_size, pack_weight, days_of_food, days_of_fuel

def player_inventory(hikerbox):
    """list of items that can be updated when hiker box item is added"""
    inventory = []
    inventory_items = []
    for dicts in hikerbox:
        inventory.append(dicts)
        inventory_items.append(dicts.get("name"))
    if inventory_items:
        print("You now have these items in your inventory: ")
        print(inventory_items)
    else:
        print("You have no items in your inventory.")
    print()
    return inventory
    #nice to have: be able to access list whenever player wants

def player_status(character, inventory):
    """update character stats, run check to see how player is doing"""
    character_updated = list(character)
    for dicts in inventory:
        character_updated[4] = character_updated[4] + dicts.get("days food", 0)
        character_updated[5] = character_updated[5] + dicts.get("days fuel", 0)
        character_updated[3] = character_updated[3] + dicts.get(
            "pack weight", 0)
    print("Here is your status:")
    print(f"  Days of food: {character_updated[4]}")
    print(f"  Days of fuel: {character_updated[5]}")
    print(f"  Pack weight: {character_updated[3]}")
    print()
    return character_updated
    #nice to have: be able to access status whenever player wants

def hiker_box(shoe_size):
  """list of items that can be taken from hiker box and added to player inventory; keys are name, type, vegan, days food, days fuel, pack weight, shoe size"""
  box = [{
        "name": "oreos",
        "type": "food",
        "vegan": True,
        "days food": 2,
        "pack weight": 1
    }, {
        "name": "tortillas",
        "type": "food",
        "vegan": True,
        "days food": 1,
        "pack weight": 0.5
    }, {
        "name": "cheese",
        "type": "food",
        "vegan": False,
        "days food": 2,
        "pack weight": 1
    }, {
        "name": "ramen",
        "type": "food",
        "vegan": True,
        "days food": 1,
        "pack weight": 0.5
    }, {
        "name": "stove",
        "type": "equipment",
        "pack weight": 1
    }, {
        "name": "fuel",
        "type": "fuel",
        "days fuel": 5,
        "pack weight": 1
    }, {
        "name": "Ultras",
        "type": "shoes",
        "pack weight": 0,
        "shoe size": character[2]
    }, {
        "name": "Salomons",
        "type": "shoes",
        "pack weight": 0,
        "shoe size": character[2] + 1
    }]
  box_items = []
  for dicts in box:
    box_items.append(dicts.get("name"))
  #nice to have: give shoes a pack weight, and if player is already wearing shoes, apply this to total pack weight
  print("This is what you find in the hiker box: ")
  print()
  #nice to have: be able to randomize what appears from this list when player opens hiker box
  taken = []
  taken_items = []
  while True:
    i = 0
    for dicts in box:
      if dicts.get("type") == "food":
        print(f"{i + 1} {dicts.get('name')} [{dicts.get('days food')} day(s) of food, {dicts.get('pack weight')} pound(s)]")
      elif dicts.get("type") == "equipment":
        print(f"{i + 1} {dicts.get('name')} [{dicts.get('pack weight')} pound(s)]")
      elif dicts.get("type") == "fuel":
        print(f"{i + 1} {dicts.get('name')} [{dicts.get('days fuel')} day(s) of fuel, {dicts.get('pack weight')} pound(s)]")
      elif dicts.get("type") == "shoes":
        print(f"{i + 1} {dicts.get('name')} [size {dicts.get('shoe size')}]")
      else:
        print("This items type has not been accounted for.")
      i += 1
    print()
    if taken == []:
      choice = input("Which items would you like to take? ")
    else:
      choice = input("What else would you like to take? ")
      print()
    if choice.title() == "Demo":
      print("DEMO")
      choice = ["oreos ", "tortillas ", "salomons "]
    else:
      choice = choice.lower() + " "
    i = 0
    for dicts in box:
      if ((str(i + 1) in choice) or (dicts.get("name").lower() + "," in choice) or (dicts.get("name").lower() + " " in choice)) and (dicts not in taken):
        taken.append(dicts)
        taken_items.append(dicts.get("name"))
      i = i + 1
    for dicts in taken:
      if dicts in box:
        box.remove(dicts)
        box_items.remove(dicts.get("name"))
    result = player_inventory(taken)
    go_on = keepChoosing()
    if go_on == True:
      print()
      print("This is what is left in the hiker box: ")
    else:
      break
  # print(f"Items taken: {taken_items}")
  # print(f"Items left: {box_items}")
  print()
  return result
  #nice to have: have list of box items outside function, and once items have been taken from box, return player inventory and box inventory

def choose_wisely(character, inventory):
    """if loop runs through player stats to determine pass/fail"""
    #check if player is carrying too much weight
    if character[3] > 20:
        # print("You are carrying too much weight.")
        return "too heavy"
    #check if player has shoes one size bigger than feet
    for dicts in inventory:
        if dicts.get("shoe size"):
            if dicts.get("shoe size") == character[2]:
                # print("Your new shoes aren't big enough.")
                return "bad shoes"
    for dicts in inventory:
        if dicts.get("shoe size"):
            shoes = "shoes"
            break
        else:
            shoes = "no shoes"
    if shoes == "no shoes":
        # print("Your shoes are too worn out.")
        return "bad shoes"
    #check if vegan has animal biproducts in inventory
    for dicts in inventory:
        if character[1] == True and dicts.get("vegan") == False:
            # print("How could you go against your own morals like that?")
            return "bad vegan"
    #check if player has enough food
    if character[4] < 5:
        # print("You are going to run out of food.")
        return "low food"
    else:
        # print("You chose wisely!")
        return "good choice"

def up_to_fate():
    """generate random outcome for 3 scenarios"""
    if random.randrange(1, 5) == 1:
        # print("Alas, you were struck by lightening.")
        return "struck"
    # else:
    # print("You were not struck by lightening.")
    if random.randrange(1, 5) == 1:
        # print("Alas, you failed to cross the river.")
        return "swept away"
    # else:
    #     print("You successfully crossed the river.")
    if random.randrange(1, 5) == 1:
        # print("Alas, a bear ate all of the food you had left.")
        return "bear encounter"
    else:
        # print("And you never had any issues with the wildlife!")
        return "lucky you"

def outcome(choice, fate):
    print(
        "After gathering your treasures from the hiker box and leaving town, you walk to the base of an intimidating mountain pass."
    )
    input("Press enter to continue...")
    print()
    if choice == "too heavy":
        print(
            "You are carrying too much weight. You can't make it over the mountain. Game over."
        )
        return "game over choice"
    print(
        "It takes an entire day, but you eventually manage to reach the summit. You are rewarded with an awesome view of an inpending storm."
    )
    input("Press enter to continue...")
    print()
    if fate == "struck":
        print(
            "You are struck by lightning at the top of the mountain. Game over."
        )
        return "game over fate"
    print(
        "The lightning storm takes you by surprise, but you deftly sweep down the other side of the mountain in record time, only to discover a raging river at the bottom."
    )
    input("Press enter to continue...")
    print()
    if fate == "swept away":
        print("You are not able to cross the river. Game over.")
        return "game over fate"
    print(
        "You shamble across the river on a fallen tree that wobbles as you move. At one point water rushes over the tree, soaking your shoes."
    )
    input("Press enter to continue...")
    print()
    if choice == "bad shoes":
        print(
            "You get to the other side of the river, but your wet feet swell and now your shoes are too small. Game over."
        )
        return "game over choice"
    print(
        "Your shoes dry in the sun, and you walk in an amiable trance for an entire day without incident..."
    )
    input("Press enter to continue...")
    print()
    if choice == "low food":
        print(
            "Only to discover you have eaten your last morsel of food and the next town is still two days away. Game over."
        )
        return "game over choice"
        #nice to have: be able to calc on which day they ran out of food
    print(
        "You are growing weary, but remain excited by how close you are to your next destination."
    )
    input("Press enter to continue...")
    print()
    if choice == "bad vegan":
        print(
            "To celebrate, you take a bite of the cheese you were saving just in case. Immediately you are flooded with shame for having gone against your creed never to eat animal biproducts. Game over."
        )
        return "game over choice"
    print("Town is now only one day away.")
    input("Press enter to continue...")
    print()
    if fate == "bear encounter":
        print(
            "Alas, you grow careless and leave your food in your pack when you take the pack into your tent for the night. You wake in the wee hours to find a bear ripping your tent to shreds. You run into the woods, screaming. Game over."
        )
        return "game over fate"
    print(
        "You cross paths with someone else on the trail who says they saw a bear in these here parts, but you see no such animal as you walk your final mile, exultant, into town."
    )
    input("Press enter to continue...")
    print()
    return "you win"

"""
---------------------------------------------------
def main
---------------------------------------------------
"""
print("Welcome to the Colorado Trail Hiker-Box Game!")
print()
player_du_jour = input("What is your trail name? ")
character = player(player_du_jour)
print()
print(f"Hi, {character[0]}.")
# print(character)
print()
inventory = []
player_inventory(inventory)
player_status(character, inventory)
print()
input("Press enter to continue...")
print()
print(
    "You have traveled far on your journey along the Colorado Trail, and this last stretch was particularily trying. It is with much relief that you see the next town materialize on the horizon. You skip up to the Post Office and yank on the handle of the door, but the door doesn't open."
)
input("Press enter to continue...")
print()
print(
    "You go through the days of the week in your head and realize with sickening dread that today is Sunday. You cannot get the next package of supplies you had so carefully mailed to yourself."
)
input("Press enter to continue...")
print()
print(
    "You look about in solemn dispair, and lo, a small hiker box sits along the building's front wall. Any hope you have of making it to the next town - which is 5 days away - is contained within."
)
input("Press enter to continue...")
while True:
    print()
    inventory = hiker_box(character[2])
    #returns list of dictionary items
    character_updated = player_status(character, inventory)
    print()
    input("Press enter to continue...")
    print()
    choice = choose_wisely(character_updated, inventory)
    fate = up_to_fate()
    result = outcome(choice, fate)
    print()
    if result == "game over choice":
        print("You chose poorly.")
        print()
        go_on = toContinue()
        if go_on == True:
            continue
        else:
            break
    elif result == "game over fate":
        print("Bad luck, old sport.")
        print()
        go_on = toContinue()
        if go_on == True:
            continue
        else:
            break
    elif result == "you win":
        print("You've made it to the next town!")
        break
print()
print("End game.")

#nice to have: turtle graphic showing player journey as diff pass/fail scenarios play out
#nice to have:message displayed about whether they would have made it if random chance did not cause them to fail
# ex. "It's too bad you got struck by lightening, 'cause otherwise you would have made it"
