import pandas as pd
from PIL import Image
import os, glob

def CreateCardsDict():
    
    #Dictionnaries with the data for each card, better to make one big pandas dataframe
    FullDeck = pd.DataFrame(columns = ["Indicant","Name", "Power", "Faction", "Role", "Special","Hero"])

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Regis",
        "Name" : "Emiel Regis Rohellec Terzieff",
        "Power" : [5],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Vesemir",
        "Name" : "Vesemir",
        "Power" : [6],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Geralt",
        "Name" : "Geralt Of Rivia",
        "Power" : [15],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ves",
        "Name" : "Ves",
        "Power" : [7],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Triss",
        "Name" : "Triss Merigold",
        "Power" : [7],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Avallach",
        "Name" : "Avallac'h",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : "Spy",
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ciri",
        "Name" : "Cirilla Fiona Elen Riannon",
        "Power" : [15],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Yen",
        "Name" : "Yennefer Of Vengerberg",
        "Power" : [7],
        "Faction" : "Neutral",
        "Role" : ["Archery"],
        "Special" : "Medic",
        "Hero" : True
    }), ignore_index=True)

    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Decoy1",
        "Name" : "Decoy",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : "Decoy",
        "Special" : "Decoy",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Decoy2",
        "Name" : "Decoy",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : "Decoy",
        "Special" : "Decoy",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Decoy3",
        "Name" : "Decoy",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : "Decoy",
        "Special" : "Decoy",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Fog1",
        "Name" : "Impenetrable Fog",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Fog2",
        "Name" : "Impenetrable Fog",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Fog3",
        "Name" : "Impenetrable Fog",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Clear1",
        "Name" : "Clear Weather",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Clear2",
        "Name" : "Clear Weather",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Clear3",
        "Name" : "Clear Weather",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Rain1",
        "Name" : "Torrential Rain",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Rain2",
        "Name" : "Torrential Rain",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Rain3",
        "Name" : "Torrential Rain",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Frost1",
        "Name" : "Biting Frost",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Frost2",
        "Name" : "Biting Frost",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Frost3",
        "Name" : "Biting Frost",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Weather",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Scorch1",
        "Name" : "Scorch",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Curse",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Scorch2",
        "Name" : "Scorch",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : "Weather",
        "Special" : "Curse",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Scorch3",
        "Name" : "Scorch",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Curse",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Horn1",
        "Name" : "Commander's Horn",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Boost",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Horn2",
        "Name" : "Commander's Horn",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Boost",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Horn3",
        "Name" : "Commander's Horn",
        "Power" : [0],
        "Faction" : "Neutral",
        "Role" : ["Weather"],
        "Special" : "Boost",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Dandelion",
        "Name" : "Commander's Horn",
        "Power" : [2],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : "Boost",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Dragon",
        "Name" : "Villentretenmerth",
        "Power" : [7],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : "Burn",
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Zoltan",
        "Name" : "Zoltan Chivay",
        "Power" : [5],
        "Faction" : "Neutral",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Albrich",
        "Name" : "Albrich",
        "Power" : [2],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Arachas1",
        "Name" : "Arachas",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Arachas2",
        "Name" : "Arachas",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Arachas3",
        "Name" : "Arachas",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Assire",
        "Name" : "Assire Var Anahid",
        "Power" : [6],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "AuxArcher1",
        "Name" : "Etolian Auxiliary Archer",
        "Power" : [1],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "AuxArcher2",
        "Name" : "Etolian Auxiliary Archer",
        "Power" : [1],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Balista1",
        "Name" : "Balista",
        "Power" : [6],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Balista2",
        "Name" : "Balista",
        "Power" : [6],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Barclay",
        "Name" : "Barclay Eis",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Archery", "Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Behemoth",
        "Name" : "Arachas Behemoth",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Siege"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "BlackArcher1",
        "Name" : "Black Infantry Archer",
        "Power" : [10],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "BlackArcher2",
        "Name" : "Black Infantry Archer",
        "Power" : [10],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Botchling",
        "Name" : "Botchling",
        "Power" : [4],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)
    
    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Brewess",
        "Name" : "Crone: Brewess",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Weavess",
        "Name" : "Crone: Weavess ",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Whispess",
        "Name" : "Crone: Whispess",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Brigade1",
        "Name" : "Imperial Brigade Guard",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Brigade2",
        "Name" : "Imperial Brigade Guard",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Brigade3",
        "Name" : "Imperial Brigade Guard",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Brigade4",
        "Name" : "Imperial Brigade Guard",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Brigade5",
        "Name" : "Imperial Brigade Guard",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)


    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Bruxa",
        "Name" : "Vampire: Bruxa",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ekimmara",
        "Name" : "Vampire: Ekimmara",
        "Power" : [4],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Fleder",
        "Name" : "Vampire: Fleder",
        "Power" : [4],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Garkain",
        "Name" : "Vampire: Garkain",
        "Power" : [4],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Behemoth",
        "Name" : "Vampire: Behemoth",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Cahir",
        "Name" : "Cahrir Mawr Dyffrinarp Ceallach",
        "Power" : [6],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Catapult1",
        "Name" : "Catapult",
        "Power" : [8],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Catapult2",
        "Name" : "Catapult",
        "Power" : [8],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Cavalry1",
        "Name" : "Nausicaa Cavalry Rider",
        "Power" : [2],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Cavalry2",
        "Name" : "Nausicaa Cavalry Rider",
        "Power" : [2],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Cavalry3",
        "Name" : "Nausicaa Cavalry Rider",
        "Power" : [2],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Cavalry4",
        "Name" : "Nausicaa Cavalry Rider",
        "Power" : [2],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Celeano Harpy",
        "Name" : "Celeano Harpy",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ciaran",
        "Name" : "Ciaran aep Easnillian",
        "Power" : [3],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Cockatrice",
        "Name" : "Cockatrice",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Commando1",
        "Name" : "Blue Stripes Commando",
        "Power" : [4],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Commando2",
        "Name" : "Blue Stripes Commando",
        "Power" : [4],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Commando3",
        "Name" : "Blue Stripes Commando",
        "Power" : [4],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Cynthia",
        "Name" : "Cynthia",
        "Power" : [4],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "DBArcher",
        "Name" : "Dol Blathanna Archer",
        "Power" : [4],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Dennis",
        "Name" : "Dennis Crammer",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Dethmold",
        "Name" : "Dethmold",
        "Power" : [6],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Dijkstra",
        "Name" : "Sigismund Dijkstra",
        "Power" : [4],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Spy",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "DragonHunter1",
        "Name" : "Cinfrid Reavers Dragon Hunter",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "DragonHunter2",
        "Name" : "Cinfrid Reavers Dragon Hunter",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "DragonHunter3",
        "Name" : "Cinfrid Reavers Dragon Hunter",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Draug",
        "Name" : "Draug",
        "Power" : [10],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "DS1",
        "Name" : "Dwarven Skirmisher",
        "Power" : [3],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "DS2",
        "Name" : "Dwarven Skirmisher",
        "Power" : [3],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "DS3",
        "Name" : "Dwarven Skirmisher",
        "Power" : [3],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "EarthElemental",
        "Name" : "Earth Elemental",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Eithne",
        "Name" : "Eithné",
        "Power" : [10],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Endrega",
        "Name" : "Endrega",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)


    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "ES1",
        "Name" : "Elven Skirmisher",
        "Power" : [2],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)


    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "ES2",
        "Name" : "Elven Skirmisher",
        "Power" : [2],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)


    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "ES3",
        "Name" : "Elven Skirmisher",
        "Power" : [2],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Esterad",
        "Name" : "Esterad Thyssen",
        "Power" : [10],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Fiend",
        "Name" : "Fiend",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Filavandrel",
        "Name" : "Filavandrel aén Fidhail",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "FireElemental",
        "Name" : "Fire Elemental",
        "Power" : [6],
        "Faction" : "Monsters",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Foglet",
        "Name" : "Foglet",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Forktail",
        "Name" : "Forktail",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Frightener",
        "Name" : "Frightener",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Fringilla",
        "Name" : "Fringilla Vigo",
        "Power" : [6],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Gargoyle",
        "Name" : "Gargoyle",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ghoul1",
        "Name" : "Ghoul",
        "Power" : [1],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ghoul2",
        "Name" : "Ghoul",
        "Power" : [1],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ghoul3",
        "Name" : "Ghoul",
        "Power" : [1],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "GraveHag",
        "Name" : "Grave Hag",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Griffin",
        "Name" : "Griffin",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Harpy",
        "Name" : "Harpy",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "HeavySkorpion",
        "Name" : "Heavy Zerrikanian Fire Scorpion",
        "Power" : [10],
        "Faction" : "Nilfgaard",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "HH1",
        "Name" : "Havekar Healer",
        "Power" : [0],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "HH2",
        "Name" : "Havekar Healer",
        "Power" : [0],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "HH3",
        "Name" : "Havekar Healer",
        "Power" : [0],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "HS1",
        "Name" : "Havekar Smuggler",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "HS2",
        "Name" : "Havekar Smuggler",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "HS3",
        "Name" : "Havekar Smuggler",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "IceGiant",
        "Name" : "Ice Giant",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ida",
        "Name" : "Ida Emean aep Sivney",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Imlerith",
        "Name" : "Imlerith",
        "Power" : [10],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Infantry",
        "Name" : "Poor Fucking Infantry",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Infantry",
        "Name" : "Poor Fucking Infantry",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Infantry",
        "Name" : "Poor Fucking Infantry",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Iorveth",
        "Name" : "Iorveth",
        "Power" : [10],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Isengrim",
        "Name" : "Isengrim Faolitarna",
        "Power" : [10],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : "Reforce",
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Kayran",
        "Name" : "Kayran",
        "Power" : [8],
        "Faction" : "Monsters",
        "Role" : ["Archery", "Infantry"],
        "Special" : "Reforce",
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Keira",
        "Name" : "Keira Metz",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Leshen",
        "Name" : "Leshen",
        "Power" : [10],
        "Faction" : "Monsters",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Letho",
        "Name" : "Letho of Gulet",
        "Power" : [10],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Mangonel",
        "Name" : "Rotten Mangonel",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "MD",
        "Name" : "Mahakamam Defender",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "MD",
        "Name" : "Mahakamam Defender",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "MD",
        "Name" : "Mahakamam Defender",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "MD",
        "Name" : "Mahakamam Defender",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "MD",
        "Name" : "Mahakamam Defender",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Dun",
        "Name" : "Dun Banner Medic",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Menno",
        "Name" : "Menno Coehornn",
        "Power" : [10],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Medic",
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Milva",
        "Name" : "Milva",
        "Power" : [10],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Morteisen",
        "Name" : "Morteisen",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Morvran",
        "Name" : "Morvran Voorhis",
        "Power" : [10],
        "Faction" : "Nilfgaard",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Natalis",
        "Name" : "John Natalis",
        "Power" : [10],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Nekker",
        "Name" : "Nekker",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Nekker",
        "Name" : "Nekker",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Nekker",
        "Name" : "Nekker",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : "Muster",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Philippa Eirhart",
        "Name" : "Philippa",
        "Power" : [10],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "PlagueMaiden",
        "Name" : "Plague Maiden",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Puttkammer",
        "Name" : "Puttkammer",
        "Power" : [3],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Rainfarm",
        "Name" : "Rainfarm",
        "Power" : [4],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "RedenianFoot1",
        "Name" : "Redenian Foot Solder",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Remuald",
        "Name" : "Remuald",
        "Power" : [5],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Riordain",
        "Name" : "Riordain",
        "Power" : [1],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Sabrina",
        "Name" : "Sabrina Glevissig",
        "Power" : [4],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Saesenthessis",
        "Name" : "Saesenthessis",
        "Power" : [10],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Scorpion",
        "Name" : "Zerrikanian Fire Scorpion",
        "Power" : [5],
        "Faction" : "Nilfgaard",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Scout1",
        "Name" : "Dol Blathanna Scout",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Scout2",
        "Name" : "Dol Blathanna Scout",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Scout3",
        "Name" : "Dol Blathanna Scout",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Shillard",
        "Name" : "Shillard Fiz-Oesterlen",
        "Power" : [7],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Spy",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "SiegeEngineer",
        "Name" : "Siege Engineer",
        "Power" : [6],
        "Faction" : "Nilfgaard",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "SiegeExpert",
        "Name" : "Kaedweni Siege Expert",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : "Reforce",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "SiegeExpert",
        "Name" : "Kaedweni Siege Expert",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : "Reforce",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "SiegeExpert",
        "Name" : "Kaedweni Siege Expert",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : "Reforce",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "SiegeTech",
        "Name" : "Siege Technician",
        "Power" : [0],
        "Faction" : "Nilfgaard",
        "Role" : ["Siege"],
        "Special" : "Medic",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "SiegeTower",
        "Name" : "Siege Tower",
        "Power" : [6],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Siegfried",
        "Name" : "Siegfried of Denesle",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Sile",
        "Name" : "Sile de Tansarville",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Skaggs",
        "Name" : "Sheldon Skaggs",
        "Power" : [4],
        "Faction" : "NorthernRealms",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Skellen",
        "Name" : "Stefan Skellen",
        "Power" : [9],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Spy",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Soldier",
        "Name" : "Redanian Foot Soldier",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Stennis",
        "Name" : "Prince Stennis",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : "Spy",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Sweers",
        "Name" : "Sweers",
        "Power" : [2],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Thaler",
        "Name" : "Thaler",
        "Power" : [1],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : "Spy",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Tibor",
        "Name" : "Tibor Eggerbracht",
        "Power" : [10],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Toruviel",
        "Name" : "Toruviel",
        "Power" : [2],
        "Faction" : "Scoiatael",
        "Role" : ["Archery "],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Trebuchet1",
        "Name" : "Trebuchet",
        "Power" : [6],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Trebuchet2",
        "Name" : "Trebuchet",
        "Power" : [6],
        "Faction" : "NorthernRealms",
        "Role" : ["Siege"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Vanhemar",
        "Name" : "Vanhemar",
        "Power" : [4],
        "Faction" : "Nilfgaard",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Vattier",
        "Name" : "Vattier De Rideaux",
        "Power" : [4],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Spy",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Vernon",
        "Name" : "Vernon Roche",
        "Power" : [10],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : True
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Ves",
        "Name" : "Ves",
        "Power" : [5],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Vreemde",
        "Name" : "Vreemde",
        "Power" : [2],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Vrihedd",
        "Name" : "Vrihedd Brigade Veteran",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Vrihedd",
        "Name" : "Vrihedd Brigade Veteran",
        "Power" : [5],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "VriheddRecruit",
        "Name" : "Vrihedd Brigade Recruit",
        "Power" : [4],
        "Faction" : "Scoiatael",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Werewolf",
        "Name" : "Werewolf",
        "Power" : [5],
        "Faction" : "Monsters",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Wyvern",
        "Name" : "Wyvern",
        "Power" : [2],
        "Faction" : "Monsters",
        "Role" : ["Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Yaevinn",
        "Name" : "Yaevinn",
        "Power" : [6],
        "Faction" : "Scoiatael",
        "Role" : ["Infantry", "Archery"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "Yarpen",
        "Name" : "YarpenZigrin",
        "Power" : [2],
        "Faction" : "NorthernRealms",
        "Role" : ["Infantry"],
        "Special" : None,
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "YE1",
        "Name" : "Young Emissary",
        "Power" : [5],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)

    FullDeck = FullDeck.append( pd.DataFrame({
        "Indicant" : "YE2",
        "Name" : "Young Emissary",
        "Power" : [5],
        "Faction" : "Nilfgaard",
        "Role" : ["Infantry"],
        "Special" : "Clone",
        "Hero" : False
    }), ignore_index=True)
    return FullDeck



def CreateBossesDict():
    #Dictionnaries with the data for each card, better to make one big pandas dataframe
    Bosses = pd.DataFrame(columns = ["Indicant","Name", "Faction"])

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EmhyrEmperor",
        "Name" : "Emhyr Var Emreis Emperor of Nilfgaard",
        "Faction" : "Nilfgaard"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EmhyrImperial",
        "Name" : "Emhyr Var Emreis His Imperial Majesty",
        "Faction" : "Nilfgaard"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EmhyrRelentless",
        "Name" : "Emhyr Var Emreis the Relentless",
        "Faction" : "Nilfgaard"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EmhyrWhite",
        "Name" : "Emhyr Var Emreis the White Flame",
        "Faction" : "Nilfgaard"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FoltestComander",
        "Name" : "Foltest Lord Commander of the North",
        "Faction" : "NorthernRealms"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FoltestKing",
        "Name" : "Foltest King of Temeria",
        "Faction" : "NorthernRealms"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FoltestSiegemaster",
        "Name" : "Foltest the Siegemaster",
        "Faction" : "NorthernRealms"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FoltestSteel",
        "Name" : "Foltest the Steel-Forged",
        "Faction" : "NorthernRealms"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FrancescaBeautiful",
        "Name" : "Francesca Findabair the Beautiful",
        "Faction" : "Scoiatael"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FrancescaDaisy",
        "Name" : "Francesca Findabair Daisy of the Valley",
        "Faction" : "Scoiatael"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FrancescaPureblood",
        "Name" : "Francesca Findabair Pureblood Elf",
        "Faction" : "Scoiatael"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "FrancescaQueen",
        "Name" : "Francesca Findabair Queend of Dol Blathanna",
        "Faction" : "Scoiatael"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EredinBringer",
        "Name" : "Eredin Bringer of Death",
        "Faction" : "Monsters"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EredinDestroyer",
        "Name" : "Eredin Destroyer of Worlds",
        "Faction" : "Monsters"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EredinCommander",
        "Name" : "Eredin Commander of the Red Riders",
        "Faction" : "Monsters"
        }), ignore_index=True)

    Bosses = Bosses.append( pd.DataFrame({
        "Indicant" : "EredinKing",
        "Name" : "Eredin King of the Wild Hunt",
        "Faction" : "Monsters"
        }), ignore_index=True)
    return Bosses