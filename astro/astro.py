from datetime import date

# ordered list of astrological signs
signs = ['capricorn',
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

def sunsign(timestamp):
    birthdate = date.fromtimestamp(timestamp)

    ind = birthdate.month - 1
    if (birthdate.day > 21):
        ind += 1
    ind = ind % len(signs)

    return signs[ind]
