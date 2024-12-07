Nonememe_dict = {
            "depauperar": "En la RAE la definen como empobrecer, aunque también puede referirse a debilitar o extenuar.",
            "Vagido": "Gemido o llanto de un recién nacido.",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print(´no existe esa palabra´)
