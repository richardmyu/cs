foods = ['kuangfen', 'doupi', 'mantou']
firend_pizzas = foods[:]
foods.append('shaomai')
firend_pizzas.append('pizza')

for fd in foods:
    print(f'My favorite food are: {fd}')

for fd in firend_pizzas:
    print(f'My firend\'s favorite food are: {fd}')
