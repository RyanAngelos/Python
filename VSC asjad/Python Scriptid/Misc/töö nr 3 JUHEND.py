def count(a):
    """
    TODO: enne lahendamist
    Vaata läbi video
    https://www.youtube.com/watch?v=OnDr4J2UXSA
    Kui ei saa aru, vaata teisi videoid/loe dokumentatsiooni vms.

    TODO count all letters in parameter a
    Put each found letter into dictionary
    as key and value must be the amount of letters found

    Example: "kalamaja majas" =>
    {
        'k': 1,
        'a': 6,
        'l': 1,
        'm': 2,
        's': 1
    }
    """
    return {'k': 2, 'a': 1, 'u': 1, 's': 2}

a = input("sisesta lause")

print(count(a))
