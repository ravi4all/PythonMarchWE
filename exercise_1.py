data = [
    {"p_id":101,"p_name":"Apple","p_price":56000,"p_color":"White"},
    {"p_id":102,"p_name":"Redmi","p_price":15000,"p_color":"Silver"},
    {"p_id":103,"p_name":"Samsung","p_price":60000,"p_color":"Black"},
    {"p_id":104,"p_name":"Apple","p_price":85000,"p_color":"Black"},
    {"p_id":105,"p_name":"Samsung","p_price":45000,"p_color":"Gray"},
    {"p_id":106,"p_name":"Vivo","p_price":22000,"p_color":"Black"},
    {"p_id":107,"p_name":"Vivo","p_price":216000,"p_color":"White"},
    {"p_id":108,"p_name":"Oppo","p_price":18000,"p_color":"Black"},
    {"p_id":109,"p_name":"Samsung","p_price":18000,"p_color":"White"},
    {"p_id":110,"p_name":"Redmi","p_price":12000,"p_color":"Silver"},
    {"p_id":111,"p_name":"Apple","p_price":32000,"p_color":"Black"},
]

print("""
Shoes | Clothes | Mobile | Other
""")

userInput = input("Enter product name : ")
'''
Eg - Enter product name : Apple
{},{},{}
'''

category = input("Enter category : ")
print("""
Filter
1. Price
2. Brand
3. Color
""")
