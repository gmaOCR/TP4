from tinydb import TinyDB
from modules.TournamentManager import TournamentManager
from operator import itemgetter

tm = TournamentManager()

db = TinyDB("db.json", sort_keys=True, indent=4, separators=(',', ': '))
players_table = db.table("players")
tournaments_table = db.table("tournaments")
rounds_table = db.table('rounds')
match_table = db.table("matchs")


"""Tournoi deserialisé"""
tm_unser = tm.unserialize_all_tournaments(tournaments_table)

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

c = input("Choisir un round par num de ligne")

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

k = input("Choisir un round par num de match")

#Boucle des matchs
matchs = (rounds[int(k) - 1])["Liste des match du round"]
i = 0
print(matchs)
for m in matchs[i].items():
    print(m)
    print(m[0], ":", m[1])
    i = i + 1
print(i)


    #dict_as_list = sorted(dict_key_exclude.items())
    #new_index = [3, 2, 0, 1]
    #dict_sorted = dict([dict_as_list[ind] for ind in new_index])
    # for n in dict_sorted.items():
    #     print(n[0], ":", n[1])


