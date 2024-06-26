import random

class River:
    def __init__(self):
        self.rivers = ["Amazonka",
                        "Nil",
                        "Mississippi",
                        "Jang-c’-ťiang",
                        "Ob",
                        "Mekong",
                        "Volha",
                        "Kongo",
                        "Amur",
                        "Léna",
                        "Murray",
                        "Tigris",
                        "Eufrat",
                        "Indus",
                        "Ganga",
                        "Don",
                        "Madeira",
                        "Purus",
                        "Jukon",
                        "São Francisco",
                        "Syr-darja",
                        "Amudarja",
                        "Irtiš",
                        "Orinoko",
                        "Colorado",
                        "Dunaj",
                        "Vistula",
                        "Ren",
                        "Loire",
                        "Rýn",
                        "Elba",
                        "Odra",
                        "Dněpr",
                        "Doněc",
                        "Seina",
                        "Pád",
                        "Po",
                        "Tajo",
                        "Douro",
                        "Guadalquivir",
                        "Thames",
                        "Clyde",
                        "Liffey",
                        "Shannon",
                        "Dněstr",
                        "Wisconsin",
                        "Arkansas",
                        "Alabama",
                        "Snake",
                        "Columbia",
                        "Platte",
                        "Missouri",
                        "Ohio",
                        "Brahmaputra",
                        "Salween",
                        "Chao Phraya",
                        "Zambězi",
                        "Senegal",
                        "Niger",
                        "Limpopo",
                        "Orange",
                        "Cauvery",
                        "Godavari",
                        "Krishna",
                        "Yamuna",
                        "Narmada",
                        "Indigirka",
                        "Kolyma",
                        "Pechora",
                        "Jenisej",
                        "Paraná",
                        "Uruguay",
                        "Xingu",
                        "Tapajós",
                        "Guaporé",
                        "Tocantins",
                        "Paraguai",
                        "Fraser",
                        "Saskatchewan",
                        "Churchill",
                        "Mackenzie",
                        "Peace",
                        "Athabasca",
                        "Liard",
                        "Gila",
                        "Bear",
                        "Green",
                        "Pee Dee",
                        "Susquehanna",
                        "Allegheny",
                        "Monongahela",
                        "Sava",
                        "Drina",
                        "Timiș",
                        "Prut",
                        "Tisza",
                        "Maritsa",
                        "Aliakmon",
                        "Struma",
                        "Vardar",
                       "Danube",
                       "Nile",
                       "Thames",
                       "Seine",
                       "Hudson",
                       "Yangtze",
                       "Mississippi",
                       "Amazon",
                       "Rhine",
                       "Mekong",
                       "Volga",
                       "Zambezi",
                       "Euphrates",
                       "Tigris",
                       "Indus",
                       "Ganges",
                       "Missouri",
                       "Ohio",
                       "Columbia",
                       "Yukon",
                       "Paraná",
                       "Orinoco",
                       "Mackenzie",
                       "Niger",
                       "Murray",
                       "Brahmaputra",
                       "Amur",
                       "Lena",
                       "Ob",
                       "Irtysh",
                       "Congo",
                       "Colorado",
                       "Danube",
                       "Po",
                       "Douro",
                       "Elbe",
                       "Loire",
                       "Oder",
                       "Pearl",
                       "Platte",
                       "Red River",
                       "Rio Grande",
                       "Salween",
                       "São Francisco",
                       "Saskatchewan",
                       "Senegal",
                       "Snake River",
                       "Tagus",
                       "Tennessee",
                       "Tocantins",
                       "Tumen",
                       "Ural",
                       "Vistula",
                       "Yellow River",
                       "Yenisei",
                       "Zhujiang",
                       "Alazani",
                       "Aragvi",
                       "Aras",
                       "Arkansas",
                       "Beni",
                       "Berezina",
                       "Biya",
                       "Brahmani",
                       "Cauca",
                       "Chindwin",
                       "Churchill",
                       "Desna",
                       "Dniester",
                       "Donets",
                       "Draa",
                       "Dunajec",
                       "Dwarka",
                       "Ebro",
                       "Essequibo",
                       "Fly",
                       "Fraser",
                       "Gambia",
                       "Godavari",
                       "Gomti",
                       "Guaviare",
                       "Helmand",
                       "Hunza",
                       "Ichamati",
                       "Imjin",
                       "Irrawaddy",
                       "Japura",
                       "Kagera",
                       "Kama",
                       "Kasai",
                       "Khatanga",
                       "Kizilirmak",
                       "Kolyma",
                       "Krishna",
                       "Kuban",
                       "Kura",
                       "Limpopo",
                       "Litani",
                       "Loa",
                       "Logone"
                         ]

    def get_random_river(self):
        print(random.choice(self.rivers))