def make_sandwich(*toppings):
    for top in toppings:
        print(top)


make_sandwich('pork')
make_sandwich('pork', 'mushrooms')
make_sandwich('pork', 'mushrooms', 'green peppers')
