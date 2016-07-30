import notifyme

# Example data for testing
Pokemon_ID = int(4)
Pokemon_LAT = float(12)
Pokemon_LNG = float(12)
Pokemon_ET = '1800'

# Below you can configure
# what kind of notifications do you want to send.
# 1 means it sends the notification, 0 to dont send
T_send = '1'
FBMSG_send = '1'
PB_send = '1'
CSV_wr = '1'
notifyme.main(Pokemon_ID, Pokemon_LAT, Pokemon_LNG, Pokemon_ET, T_send, FBMSG_send, PB_send, CSV_wr)

