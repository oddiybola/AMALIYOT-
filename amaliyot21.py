kinolar = {
    'umrbek':['Qashqirlar makoni','Vahshiy timsoh','Forsaj'],
    'diyorbek':['Forsaj2','Ipman','Boyka'],
    'sharafiddin':['Terminator','Bomba','Bamblbee'],
    'biloliddin':['Rombo','Jasorat']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)