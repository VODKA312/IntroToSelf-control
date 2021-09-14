from copy import deepcopy
import random

french_to_eng = {
    "bleu"  : "blue",
    "noir"  : "black", 
    "vert"  : "green",
    "violet": "purple",
    "gris"  : "gray",
    "rouge" : "red",
    "orange": "orange",
    "rose"  : "pink",
    "marron": "brown",
    "jaune" : "yellow",
    "blanc" : "white",
}

TICKET = {
    "type" : "bug",
    "status": "done",
    "priority": "medium",
    "resolution": "done",
    "description" : "testing 123",
    "attachments" : [],
    "people": {
        "assignee" : None,
        "reporter" : {
            "name" : "Andy Brown",
            "image": "www.example_image_url.com"
        },
        "votes" : 0,
        "watchers" : [
            {
                "name": "Andy Brown",
                "image": "www.example_image_url.com"  
            }
        ]
    },
    "dates" : {
        "created" : "6 days ago",
        "updated" : "6 days ago",
        "resolved": "6 days ago"
    }
}

def random_ticket():
    ticket = deepcopy(TICKET)
    names = [
        "Andy Brown",
        "Cezanne Camacho",
        "Andrew Paster",
        "Jonathan Sullivan",
        "Anthony Navarro",
        "Kagure Kabue",
        "Sebastian Thrun",
        "David Silver",
        "Jessica Lulovics",
        "Erika Alonzo",  
    ]
    reporter = random.choice(names)
    
    watchers = []
    for name in names:
        if random.random() > 0.5:
            watcher = {
                "name": name,
                "image": "www.example_image_url.com"
            }
            watchers.append(watcher)
    ticket['people']['watchers'] = watchers
    ticket['people']['reporter']['name'] = reporter
    return ticket

big_tickets = [random_ticket() for _ in range(250)]
    

dictionary_tickets = [
    {
        "datetime":    '2017-04-23T05:29:30', 
        "priority":     1, 
        "description": "example description 1"
    },
    {
        "datetime":    '2017-05-23T05:29:30', 
        "priority":     1, 
        "description": "example description 2"
    },
    {
        "datetime":    '2017-06-23T05:29:30', 
        "priority":     2, 
        "description": "example description 3"
    },
    {
        "datetime":    '2017-07-23T05:29:30', 
        "priority":     1, 
        "description": "example description 4"
    },
    {
        "datetime":    '2017-08-23T05:29:30', 
        "priority":     3, 
        "description": "example description 5"
    },
    {
        "priority":     2, 
        "datetime":    '2017-09-23T05:29:30', 
        "description": "example description 6"
    },
    {
        "datetime":    '2017-10-23T05:29:30', 
        "priority":     3, 
        "description": "example description 7"
    },
    {
        "datetime":    '2017-11-23T05:29:30', 
        "priority":     2, 
        "description": "example description 8"
    },
]