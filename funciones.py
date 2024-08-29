def normalizar_nombre(raw_name :str):
    id = 0
    if raw_name  == 'Total Nacional' or raw_name  == 'Nacional':
        id = 0
    elif raw_name == 'Andalucía':
        id = 1
    elif raw_name == 'Aragón':
        id = 2
    elif raw_name == 'Asturias, Principado de' or raw_name  == 'Asturias (Principado de)' or raw_name == 'Principado de Asturias' or raw_name == 'Asturias':
        id = 3
    elif raw_name == 'Balears, Illes' or raw_name == 'Balears (Illes)' or raw_name == 'Islas Baleares':
        id = 4
    elif raw_name == 'Canarias' or raw_name == 'Islas Canarias':
        id = 5
    elif raw_name == 'Cantabria':
        id = 6
    elif raw_name == 'Castilla y León':
        id = 7
    elif raw_name == 'Castilla - La Mancha' or raw_name == 'Castilla La Mancha':
        id = 8
    elif raw_name == 'Cataluña':
        id = 9
    elif raw_name == 'Comunitat Valenciana' or raw_name == 'Comunidad Valenciana':
        id = 10
    elif raw_name == 'Extremadura':
        id = 11
    elif raw_name == 'Galicia':
        id = 12
    elif raw_name == 'Madrid, Comunidad de' or raw_name == 'Madrid (Comunidad de)' or raw_name == 'Comunidad de Madrid':
        id = 13
    elif raw_name == 'Murcia, Región de' or raw_name == 'Murcia (Región de)' or raw_name == 'Región de Murcia':
        id = 14
    elif raw_name == 'Navarra, Comunidad Foral de' or raw_name == 'Navarra (Comunidad Foral de)' or raw_name == 'Comunidad Foral de Navarra' or raw_name == 'Navarra':
        id = 15
    elif raw_name == 'País Vasco':
        id = 16
    elif raw_name == 'Rioja, La' or raw_name == 'Rioja (La)' or raw_name == 'La Rioja':
        id = 17
    elif raw_name == 'Ceuta':
        id = 18
    elif raw_name == 'Melilla':
        id = 19
    else:
        raise ValueError
    return id


"""
    Limpia el nombre con este formato:
        - Total Nacional, Viajero, Total
        - 01 Andalucía, Viajero, Total
        - 02 Aragón, Viajero, Total
        - 03 Asturias, Principado de, Viajero, Total
        - 04 Balears, Illes, Viajero, Total
"""
def clean_name(string):
    main = string.split(',')[:-2]
    if main[0][:2].isdigit():
        a = list([main[0][3:]])
    else:
        a = list([main[0]])
    for x in main[1:]:
        a.append(x)
    return ','.join(a)