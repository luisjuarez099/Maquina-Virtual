DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Fernando',
        'age': 23,
        'organization': 'Platzi',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization':'Platzi',
        'position': 'platzi',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 16,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'Python',
    },
]

def run():
    #all_py_devs=[worker["name"] for worker in DATA if worker["language"]== "javascript"]
    #all_plz_workers=[worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    #all_py_devs=(list(filter(lambda worker: worker["organization"] == 'Platzi' and worker["age"]>=18,DATA)))
    #all_plz_workers=(list(map(lambda worker: worker["age"] <=18,DATA  )))
    
    #adults=list(filter(lambda worker: worker["age"]>=18,DATA))#List comprehension
    #adults=list(map(lambda worker: worker["name"], adults))#List comprehension
    #old_people=list(map(lambda worker: worker | {"old":worker["age"]>70},DATA))
    
    #adults=[worker["name"] for worker in DATA if worker["age"] <=18]
    adults=[worker["name"] for worker in DATA if worker["language"] =="javascript"]


    for worker in adults:
        print(worker)


if __name__=='__main__':
    run()
