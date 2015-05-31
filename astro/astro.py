from datetime import date

# ordered list of astrological signs
signs12 = ['capricorn',
         'aquarius',
         'pisces',
         'aries',
         'taurus',
         'gemini',
         'cancer',
         'leo',
         'virgo',
         'libra',
         'scorpio',
         'saggitarius'
        ]

# dates of the 13-sign zodiac associated with their name
dates13 = [
    (date(1,1,1),  'sagittarius'),
    (date(1,1,20), 'capricorn'),
    (date(1,2,16), 'aquarius'),
    (date(1,3,11), 'pisces'),
    (date(1,4,18), 'aries'),
    (date(1,5,13), 'taurus'),
    (date(1,6,21), 'gemini'),
    (date(1,7,20), 'cancer'),
    (date(1,8,10), 'leo'),
    (date(1,9,16), 'virgo'),
    (date(1,10,30), 'libra'),
    (date(1,11,23), 'scorpio'),
    (date(1,11,29), 'ophiuchus'),
    (date(1,12,18), 'sagittarius')
]

def sunsign13(birthdate):
    compdate = date(1, birthdate.month, birthdate.day)

    signs = [i[1] for i in dates13 if compdate >= i[0]]
    return signs[len(signs) - 1]

def sunsign12(birthdate):
    ind = birthdate.month if (birthdate.day > 21) else birthdate.month - 1

    return signs12[ind % len(signs12)]
