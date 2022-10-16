from tinydb import TinyDB
from modules.TournamentManager import TournamentManager
import pprint

tm = TournamentManager()

db = TinyDB("db.json", sort_keys=True, indent=4, separators=(',', ': '))
players_table = db.table("players")
tournaments_table = db.table("tournaments")
rounds_table = db.table('rounds')
match_table = db.table("matchs")


"""Tournoi deserialisé"""
tm_unser = tm.unserialize_all_tournaments(tournaments_table)
unserialized_players = players_table.all()

pprint.pprint(unserialized_players)

# for date in tm_unser:
#     print(tm_unser[i]["Date"])
#     i = i + 1
#
# i = 0
#
# for k in tm_unser[0].keys():
#     print(k)
#     i = i + 1
#
# for v in tm_unser[0].values():
#     print(v)
#     i = i + 1

# """Code valide"""
# for j in tm_unser:
#     for k, v in tm_unser[i].items():
#         print(k, v)
#     i = i + 1

#Boucle des tournois
i = 0
exclude = {"Liste des rounds"}
for j in tm_unser:
    print("\nTournoi N°" + str(i + 1) + ":")
    dict_key_exclude = ({k: (tm_unser[i])[k] for k in tm_unser[i] if k not in exclude})
    dict_as_list = sorted(dict_key_exclude.items())
    new_index = [4, 1, 0, 2, 3]
    dict_sorted = dict([dict_as_list[ind] for ind in new_index])
    for t in dict_sorted.items():
        print(t[0], ":", t[1])
    i = i + 1

#c = input("Choisir un round par num de tournoi")
c = 2

#BoUcle des rondes
exclude_match = {"Liste des match du round"}
rounds = (tm_unser[int(c) - 1])["Liste des rounds"]
i = 0
for r in rounds:
    print("\n")
    dict_key_exclude = ({k: rounds[i][k] for k in rounds[i] if k not in exclude_match})
    i = i + 1
    dict_as_list = sorted(dict_key_exclude.items())
    new_index = [3, 2, 0, 1]
    dict_sorted = dict([dict_as_list[ind] for ind in new_index])
    for n in dict_sorted.items():
        print(n[0], ":", n[1])

#k = input("Choisir un round par num de round")
k = 1

#Boucle des matchs
exclude_key = {"Tournoi"}
matchs = (rounds[int(k) - 1])["Liste des match du round"]
i = 0
# print(matchs)
# print("\n")
for m in matchs:
    dict_match = ({k: matchs[i][k] for k in matchs[i] if k not in exclude_key})
    dict_as_list =  sorted(dict_match.items())
    print(dict_as_list[0][1])
    i = i + 1
    # for n in dict_match.items():
    #     print(n[0], ":", n[1])



