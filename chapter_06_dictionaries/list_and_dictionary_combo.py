aliens = []

for i in range(15):
    aliens.append({'color' : 'green' , 'points' : 5 , 'speed' : 'slow'})

for alien in aliens[5 : 10] + aliens[11 : 13] : # "+" in between merges those 2
    if alien['color'] == 'green' :
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'


print(aliens)

for alien in aliens[12 :] :
    if alien['color'] == 'green' :
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == "yellow" :
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'


for i in aliens :
    print(i['color'])