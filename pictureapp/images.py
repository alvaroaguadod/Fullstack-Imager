import json
image_list = [
    {'name': 'HikariOe.png','image_id': '1', 'width': '10', 'height': '20'},
    {'name': 'RicardoPastel.png','image_id': '2', 'width': '15', 'height': '25'},
]

with open("images.json", "w") as json_file:
    json.dump(image_list, json_file)