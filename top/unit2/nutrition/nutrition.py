def main():
    text = input("Item: ")
    calories(text)

def calories(str):
    f = str.title()
    lookup = {
        "Apple": "130",
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50",
        "Grapefruit": "60",
        "Grapes": "90",
        "Honeydew melon": "50",
        "Kiwifruit": "90",
        "Lemon": "15",
        "Lime": "20",
        "Nectarine": "60",
        "Orange": "80",
        "Peach": "60",
        "Pear": "100",
        "Pineapple": "50",
        "Plums": "70",
        "Strawberries": "50",
        "Sweet Cherries": "100",
        "Tangerine": "50",
        "Watermelon": "80",
    }
    if f in lookup:
        print(lookup[f])

main()
