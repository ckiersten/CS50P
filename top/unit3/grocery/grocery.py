def main():
    l = grocery_list()
    for i in sorted(l):
        print(l[i], i)

def grocery_list():
    user_list = {}
    while True:
        try:
            item = input().strip().upper()
            i = user_list[item]
            user_list.update({item: i+1})
        except EOFError:
            return user_list
        except KeyError:
            user_list.update({item: 1})
            
main()
