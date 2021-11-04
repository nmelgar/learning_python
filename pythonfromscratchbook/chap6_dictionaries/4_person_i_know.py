people = {
    'person1': {
        'first_name': 'marcos',
        'last_name': 'markus',
        'age': 35,
        'city': 'lerdo'
        },
    'person2':{
        'first_name': 'carl',
        'last_name': 'carlson',
        'age': 28,
        'city': 'torreon'
        },
    'person3':{
        'first_name': 'patrick',
        'last_name': 'peters',
        'age': 22,
        'city': 'gomez'
        }
}

for persons, information in people.items():
    f_name = information['first_name']
    l_name = information['last_name']
    full_name = f_name + ' ' + l_name
    print(f"\n\tIt's name is {full_name}")
    print(f"\t\tAnd he is from {information['city']}")