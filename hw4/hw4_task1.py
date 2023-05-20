"""
there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: euro}
"""

person = ' name=Amanda=sssss&age=32&&salary=1500&currency=euro '
person = person.strip()
params = person.split('&')
pair_dict = {}
for param in params:
    if param:
        key, value = param.split('=', maxsplit=1)
        pair_dict[key] = value

temp_name = str(pair_dict['name']).rstrip('=sssss')
pair_dict['name'] = temp_name
print(f'Dictionary: {pair_dict}')
