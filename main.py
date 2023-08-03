from nkapi import get_clan_counts
from google_sheets import update_clan_counts

clan_counts = get_clan_counts()
clan_counts += [[""] * 4] * 5

update_clan_counts(clan_counts)