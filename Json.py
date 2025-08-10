import json

my_data = """{
    "article" : [
        {
            "id":"10",
            "player":"sachin",
            "type":"batsman"
        },
        {
            "id":"18",
            "player":"virat",
            "type":"batsman"
        }
    ]
}"""
# print(my_data)

to_data=json.loads(my_data)
# print(to_data)
# print(type(to_data))
another_data={
            "id":"10",
            "player":"sachin",
            "type":"batsman"
        }

another_json=json.dumps(another_data)
# print(another_json)
# print(type(another_json))

with open("27th_july.json",'w') as file:
    json.dump(to_data,file)


with open('27th_july.json','r') as file:
    json_data=json.load(file)
    print(json_data)