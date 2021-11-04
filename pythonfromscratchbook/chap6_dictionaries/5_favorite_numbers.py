favorite_numbers = {
    'sarahi':{
        'numbers': '67, 24'
    },

    'pedro':{ 
        'numbers': 54
    },
    'ana':{
        'numbers': 10
    },
    'marcos':{
        'numbers': 17
    },
    'gerardo': {
        'numbers': 9
    }
}



for person_name, fav_num in favorite_numbers.items():
    print(f"{person_name}'s and favorite numbers are {fav_num['numbers']}")




#print(f"Sarahí's favorite number is: {favorite_numbers['sarahi']}.")
#print(f"Pedro's favorite number is: {favorite_numbers['pedro']}.")
#print(f"Ana's favorite number is: {favorite_numbers['ana']}.")
#print(f"Marcos's favorite number is: {favorite_numbers['marcos']}.")
#print(f"Gerardo's favorite number is: {favorite_numbers['gerardo']}.")