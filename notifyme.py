import time
import csv
import os
import time
import fbchat
import twitter
from datetime import datetime
from datetime import timedelta

import sys

def main(Pokemon_ID, Pokemon_LAT, Pokemon_LNG, Pokemon_ET, T_send, FBMSG_send, PB_send, CSV_wr):

# CONFIG OF VALUES
# Your city's name to be displayed in the text
    city = ''
# This is the language of the Pokemon's name. You can pick it from the /locales directory
    pokenamelanguage = 'locales/pokemon.en.json'
#  Twitter
    Tconsumer_key = ""
    Tconsumer_secret=""
    Taccess_token_key=""
    Taccess_token_secret=""

#  Pushbullet
    PB_api_key = ''

# Facebook messenger
    profile_id_from = ''
    profile_pw = ''
    profile_id_to = ''


    def gmaps_link(lat, lng):
                    latLon = '{},{}'.format(repr(lat), repr(lng))
		    return 'http://maps.google.com/maps?q={}'.format(latLon)

    def get_pokemon_name(pokemon_id):
        if not hasattr(get_pokemon_name, 'names'):
            file_path = os.path.join(os.getcwd()+'/pokemon.json')

            with open(file_path, 'r') as f:
                get_pokemon_name.names = json.loads(f.read())

        return get_pokemon_name.names[int(pokemon_id)]

    with open(pokenamelanguage, 'r') as f:
        mydict = eval(f.read())
        inv_map = dict(zip(mydict.values(), mydict.keys()))

    pokename = inv_map.keys()[inv_map.values().index(str(Pokemon_ID))]

    print pokename

# Formatting

    expsec = int(float(Pokemon_ET) - time.time())
    m, s = divmod(expsec, 60)
    expat = datetime.fromtimestamp(float(Pokemon_ET)).strftime('%H:%M')

    google_maps_link = gmaps_link(Pokemon_LAT, Pokemon_LNG)

#DEBUG negative time till expire

    negtime = ')'

    if float(Pokemon_ET) < time.time(): 
         Pokemon_ET = time.time()+1800
         negtime = ') Doublespawn, timer is not correct' 


#Here you can filter what to show:
    goodlist = [4,5,6,9,22,23,24,25,26,36,37,38,53,58,59,74,75,76,77,78,83,87,88,89,91,94,97,101,102,103,104,105,
                110,111,112,115,126,127,128,130,131,134,135,136,137,138,139,140,141,142,143,144,145,
                146,147,148,149,150,151]
    print int(Pokemon_ID)
    
    if int(Pokemon_ID) in goodlist:
        print 'IN GOODLIST'

# Facebook message
        if FBMSG_send == '1':
            print 'FB SEND'
            try:
                client = fbchat.Client(profile_id_from, profile_pw)
                sent = client.send(profile_id_to, 'A wild ' + pokename.title() + ' has appeared in '+str(city)+'!'+'\n'
                                   +'Expires in: '+str(m)+'m'+str(s)+'s ('+str(expat)+negtime+'\n'+
                                   google_maps_link)
            except:
                   pass
        else:
            pass

# Twitter tweet
        if T_send == str('1'):
            print 'TWEET SEND'
            try:
                api = twitter.Api(consumer_key=Tconsumer_key,
                                  consumer_secret=Tconsumer_secret,
                                  access_token_key=Taccess_token_key,
                                  access_token_secret=Taccess_token_secret)

                status = api.PostUpdate(status='A wild ' + pokename.title() + ' has appeared in '+str(city)+'!'+'\n'
                                        +'Expires in: '+str(m)+'m'+str(s)+'s ('+str(expat)+negtime+'\n'+google_maps_link)
            except:
                   pass
        else:
            pass

# Pushbullet notification
        if PB_send == str('1'):
            print 'PB SEND'
            try:
                pb = Pushbullet(PB_api_key)

                push = pb.push_link('A wild ' + pokename.title() + ' has appeared in '+str(city)+'!',google_maps_link,
                                    'Expires in: '+str(m)+'m'+str(s)+'s ('+str(expat)+negtime)
            except:
                   pass
# Write to CSV
    if CSV_wr == 1:
        print 'CSV WRITE'
        try:
            f = open(os.getcwd()+'\spawn_locationPminer.csv', "a")
            out = csv.writer(f, delimiter=",")
            out.writerow([str(Pokemon_ID),str(Pokemon_LAT),str(Pokemon_LNG),str(Pokemon_ET)])
            f.close()
        except:
            pass
    else:
        pass








