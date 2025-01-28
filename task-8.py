people = [
    {
     "name": "Tom", 
     "age": 39, 
     "company": "SuperCorp", 
     "languages": ["Python", "JavaScript"]
     },

    {
     "name": "Bob", 
     "age": 43, 
     "company": "BigCorp", 
     "languages": ["Python", "C++", "C#"]
     },

    {
     "name": "Sam", 
     "age": 28, 
     "company": "LittleCorp", 
     "languages": ["Python", "Java"]
     }
]

for user in people:
    print(f"Name: {user["name"]}")
    print(f"Last language: {user["languages"][-1]}")