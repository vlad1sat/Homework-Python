def create_player(data, player):
    for element_data in data:
        player.append(element_data)


def union_players(user_players):
    players_union = list()
    for full_name, scores in user_players.items():
        player = list()
        create_player(full_name, player)
        create_player(scores, player)
        players_union.append(tuple(player))
    return players_union


players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
print(union_players(players))