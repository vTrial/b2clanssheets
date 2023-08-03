from nkapi import get_clan_counts
from google_sheets import update_clan_counts
import time

def clan_loop():
	clan_counts = get_clan_counts()
	clan_counts += [[""] * 4] * 5
	update_clan_counts(clan_counts)

starttime = time.monotonic()
seconds_to_loop = 1800
while True:
    clan_loop()
    time.sleep(seconds_to_loop - ((time.monotonic() - starttime) % seconds_to_loop))