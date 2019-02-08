import math
import json

minorSecond   = 1.067
majorSecond   = 1.125
minorThird    = 1.2
majorThird    = 1.25
perfectFourth = 1.33333
augFourth     = 1.414
perfectFifth  = 1.5
minorSixth    = 1.6
goldenRatio = 1.61803398875
majorSixth    = 1.667
minorSeventh  = 1.778
majorSeventh  = 1.875
octave        = 2
majorTenth    = 2.5
majorEleventh = 2.667
majorTwelfth  = 3
doubleOctave = 4

base = 8

def calculator(base, ratio):
    print "\nYou have selected a %s baseline and a ratio of %s \n" % (base, ratio)

    fontSize = [];

    for counter in range(-3,5):
        scale = math.pow(ratio,counter) * base
        result = str(round(scale / base, 3))
        result = result + 'em'
        fontSize.append(result)

    print "Here is your results and output to json:"
    print fontSize
    print "\n"

    data = {
        "font":{
            "size":{
                "xxsmall": fontSize[0],
                "xsmall": fontSize[1],
                "small": fontSize[2],
                "medium": fontSize[3],
                "large": fontSize[4],
                "xlarge": fontSize[5],
                "xxlarge": fontSize[6],
                "xxxlarge": fontSize[7]
            }
        }
    }

    with open('text-size.json', 'w') as f:
     json.dump(data, f)

def inputBase(message):
    while True:
        try:
            userInputBase = int(input(message))
        except ValueError:
            print("This is not a number")
            continue
        else:
            return userInputBase
            break

base = inputBase('Enter a baseline height:\n')
print ('\n Minor Second = 1 \n Major Second = 2 \n Minor Third = 3 \n Major Third = 4 \n Perfect Fourth = 5 \n Aug Fourth = 6 \n Perfect Fifth = 7 \n Minor Sixth = 8 \n Golden Ratio = 9 \n Major Sixth = 10 \n Minor Seventh = 11 \n Major Secenth = 12 \n Octave = 13 \n Major Tenth = 14 \n Major Eleventh = 15 \n Major Tweltfth = 16 \n Double Octave = 17')
ratio = int(input("\nEnter a number that corelates to the ratio: (See table above)\n"))

if ratio == 1:
    ratio = minorSecond
elif ratio == 2:
    ratio = majorSecond
elif ratio == 3:
    ratio = minorThird
elif ratio == 4:
    ratio = majorThird
elif ratio == 5:
    ratio = perfectFourth
elif ratio == 6:
    ratio = augFourth
elif ratio == 7:
    ratio = perfectFifth
elif ratio == 8:
    ratio = minorSixth
elif ratio == 9:
    ratio = goldenRatio
elif ratio == 10:
    ratio = majorSixth
elif ratio == 11:
    ratio = minorSeventh
elif ratio == 12:
    ratio = majorSeventh
elif ratio == 13:
    ratio = octave
elif ratio == 14:
    ratio = majorTenth
elif ratio == 15:
    ratio = majorEleventh
elif ratio == 16:
    ratio = majorTwelfth
elif ratio == 17:
    ratio = doubleOctave
else:
    print('Looks like you did not select an option that is avaliable')

calculator(base, ratio)
