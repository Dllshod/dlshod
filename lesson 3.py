names = ['SASHA', 'Pasha', 'Tolya']
new_name= input('Type here new name: ')
names.append(new_name)
print(names)
names = ['SASHA', 'Pasha', 'Tolya']
new_name= input('Type here new name: ')
names.insert(1,'Katya' )
print(names)
names = ['SASHA', 'Pasha', 'Tolya',]
new_name= input('Type here new name: ')
names.extend(['Masha'])
print(names)
names = ['SASHA', 'Pasha', 'Tolya']
Remove_name= input('Type here a name, what you will remove: ')
names.remove(Remove_name)
print(names)


