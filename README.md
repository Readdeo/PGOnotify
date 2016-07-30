# Standalone notifications for any Pokemon GO map

## Supported notifications
Twitter tweet, Facebook message, Pushbullet notification


## How to make it work
Install theese to make it work: `sudo pip install -r requirements.txt`

For Twitter to work, you have to make a Twitter app, and create the four tokens you will need to set. There are documentations about this out there.

For Facebook, you have to find your Facebook profile ID.

For Pushbullet, create an account and an access token in the settings.

## The hardest part to find
The call.py is an example, to see how to set this up in your map. You have to find the variables in the map's source to make it work.
For example in the Pokeminer, you should put this code into the `add_sighting` definition's end in the `db.py`
And it should look like this:

```
def add_sighting(session, spawn_id, pokemon):  
    obj = Sighting(  
        pokemon_id=pokemon['id'],  
        spawn_id=spawn_id,  
        expire_timestamp=pokemon['disappear_time'],
        normalized_timestamp=normalize_timestamp(pokemon['disappear_time']),  
        lat=pokemon['lat'],  
        lon=pokemon['lng'],  
    )  
    # Check if there isn't the same entry already  
    existing = session.query(Sighting) \
        .filter(Sighting.pokemon_id == obj.pokemon_id) \
        .filter(Sighting.spawn_id == obj.spawn_id) \
        .filter(Sighting.expire_timestamp > obj.expire_timestamp - 10)     \
        .filter(Sighting.expire_timestamp < obj.expire_timestamp + 10) \
        .filter(Sighting.lat == obj.lat) \
        .filter(Sighting.lon == obj.lon) \
        .first()   
    if existing:  
        return  
    session.add(obj)
# Notification code goes above this line

# Set the Pokeminer's variables here:
    Pokemon_ID = pokemon['id']
    Pokemon_LAT = pokemon['lat']
    Pokemon_LNG = pokemon['lng']
    Pokemon_ET = pokemon['disappear_time']

    T_send = '1'
    FBMSG_send = '1'
    PB_send = '1'
    CSV_wr = '1'
    notifyme.main(Pokemon_ID, Pokemon_LAT, Pokemon_LNG, Pokemon_ET, T_send, FBMSG_send, PB_send, CSV_wr)

```
