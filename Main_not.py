import json

# create an array of items
my_array = [
    "election 1",
    "election 2",
    "election 3"
]

# convert the array to a JSON string
json_string = json.dumps(my_array)

# write the JSON string to a file
with open('elections_list.json', 'w') as f:
    f.write(json_string)


