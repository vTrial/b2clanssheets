import requests
def get_lb_total_pages():
    homs_url = "https://data.ninjakiwi.com/battles2/homs"
    homs_data = requests.request("GET", homs_url).json()
    total_hom_players = homs_data['body'][0]["totalScores"]
    lb_page_count = (total_hom_players - 1) // 50 + 1
    return lb_page_count

def get_player_list():
    player_list = []
    lb_total_pages = get_lb_total_pages()
    for lb_page_num in range(1, lb_total_pages + 1):
        lb_url = f"https://data.ninjakiwi.com/battles2/homs/season_12/leaderboard?page={lb_page_num}"
        lb_json = requests.request("GET", lb_url).json()
        player_list += [[player["displayName"], player["score"]] for player in lb_json["body"]]
    return player_list

def get_filtered_player_list():
    player_list = get_player_list()
    filtered_player_list = [player for player in player_list if '<' in player[0] and '>' in player[0]]
    return filtered_player_list

def get_clan_counts():
    filtered_player_list = get_filtered_player_list()
    clan_counts = {}
    for entry in filtered_player_list:
        name = entry[0]
        if '<' in name and '>' in name:
            start = name.index('<')
            end = name.index('>', start)
            clan = name[start + 1:end].lower()
            clan_members = clan_counts.get(clan, [0, 0])[0] + 1
            clan_total_score = clan_counts.get(clan, [0, 0])[1] + entry[1]
            clan_counts[clan] = [clan_members, clan_total_score]
    lst_count = [[clan, clan_counts[clan][0], clan_counts[clan][1], clan_counts[clan][1] // clan_counts[clan][0]] for clan in clan_counts]
    # secondary sort: score
    sorted_count = sorted(lst_count, key=lambda x: x[2], reverse=True)
    # primary sort: member count
    sorted_count = sorted(sorted_count, key=lambda x: x[1], reverse=True)
    return sorted_count