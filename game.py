champ = ["Lizard", "Bird", "Wizard"]
print(str(champ) + " Select one of these!")
user = input("Choose your character: ")

if user == "Lizard" or user == "lizard":
    print("Selected Lizard! " + " Nice Choice!")
    liz = input("Continue? y/n: ")
    if liz == "y":
        print("You spawned near lake called Lizardius, you need to choose your first weapon!")
        lweap = input("1) sword, 2) axe or 3) boomerang? ")
        if lweap == "1" or lweap == "sword":
            print("You chosen sword, which means you now have +2 attack!")
        elif lweap == "2" or lweap == "axe":
            print("You chosen axe, which means you now have +1 attack!")
        elif lweap == "3" or lweap == "boomerang":
            print("You chosen boomerang, which means you now have +3 attack!")

