from kivy.storage.jsonstore import JsonStore

store = JsonStore('hello.json')

"""# put some values
store.put('tito', name='Mathieu', org='kivy')
store.put('tshirtman', name='Gabriel', age=27)

# using the same index key erases all previously added key-value pairs
store.put('tito', name='Mathieu', age=30)

# get a value using a index key and key
print('tito is', store.get('tito')['age'])"""

# or guess the key/entry for a part of the key
print(store.store_get_async('tito'))