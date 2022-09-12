import rolimons

# initialize client
client = rolimons.Client('cookie')

# declare items
offering = [1029025]
requesting = [1365767, 'adds']

# post trade ad
status = client.post_trade_ad(offering, requesting, 1) # <-- 1 is the id of user you are posting from
print(status)
