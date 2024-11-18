from dotenv import load_dotenv
import os
import random
import math
import requests

load_dotenv()

participants = []
hat = []
particpantsPhone = []

partipantMapping = []

    
def get_random_person(par_arr, current_selector):
    random_person = par_arr[math.floor((random.random() * len(par_arr)))]
    if (random_person == current_selector):
        get_random_person(par_arr, current_selector)

    return random_person


for idx, particpant in enumerate(participants):
    current_selector = participants[idx]
    random_person = get_random_person(hat, current_selector)
    partipantMapping.append({
        'selector': current_selector,
        'assignedPerson': random_person,
        'selectorPhone': particpantsPhone[idx]
    })

    removalIdx = 0
    for jdx, hatItem in enumerate(hat): 
        if (hatItem == random_person):
            removalIdx = jdx
    hat.pop(removalIdx)


auth_token = os.getenv('TEXTBELT_AUTH_TOKEN')

for map in partipantMapping:
    resp = requests.post('https://textbelt.com/text', {
        'phone': map['selectorPhone'],
        'message': f"Hello, this is your Family Party Bot! \n You have been assigned a person!! Your person will be {map['assignedPerson']}",
        'key': auth_token,
    })
    print(resp.json())