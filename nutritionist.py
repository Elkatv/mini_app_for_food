import sys
from recipes import Main_class
from recipes import Dayly_menu
from copy import deepcopy

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Из такого набора продуктов сложно что то пригтовить")
        return

    if args[0] == "dayly":
        Dayly_menu().dayly_menu()
        return
    
    args = list(map(lambda x: x.replace(',', ''), args))
    
    l1 = deepcopy(args)
    l2 = deepcopy(args)
    l3 = deepcopy(args)
    
    a = Main_class()

    print("I. OUR FORECAST")
    a.rating(l1)

    print("II. NUTRITION FACTS")
    a.nutrientions_fact(l2)

    print("III. TOP-3 SIMILAR RECIPES:")
    a.similar_reciept(l3)


if __name__ == "__main__":
    main()