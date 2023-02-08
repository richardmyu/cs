minions = ['bob', 'stuart', 'kevin', 'jorge']

# dave tim mark phil jerry

print(minions[0])
print(minions[1])
print(minions[-2])
print(minions[-1])

print('-------------')

minions[-1] = 'dave'
print(minions)

minions.append('tim')
print(minions)

minions.insert(-1, 'mark')
print(minions)

minions.insert(-1, 'mark')
print(minions)

minions.insert(0, 'phil')
print(minions)

del minions[0]
print(minions)

minions.pop()
print(minions)

minions.pop()
print(minions)

minions.pop(-1)
print(minions)

minions.remove('dave')
print(minions)

print('-------------')

minions.sort()
print(minions)

minions.sort(reverse=True)
print(minions)

print(sorted(minions))
print(minions)

print(sorted(minions, reverse=True))
print(minions)

minions.reverse()
print(minions)

print(len(minions))
