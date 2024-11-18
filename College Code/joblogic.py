import pytholog as pl

friends_kb = pl.KnowledgeBase("friends")
friends_kb([
    "has_lot_work(daniel,8)",
    "has_lot_work(david,3)",
    "stress(X,P):-has_lot_work(X,P2),P is P2 / 100",
    "to_smoke(X,Prob):-stress(X,P1),friends(Y,X),influences(Y,X,P2),smokes(Y),Prob is P1 * P2",
    "to_have_asthma(X,0.3):-smokes(X)",
    "to_have_asthma(X,Prob):-to_smoke(X,P2),Prob is P2 * 0.25",
    "friends(X,Y):-friend(X,Y)",
    "friends(X,Y):-friend(Y,X)",
    "influences(X,Y,0.4):-friends(X,Y)",
    "friend(peter,david)",
    "friend(peter,rebecca)",
    "friend(daniel,rebecca)",
    "smokes(peter)",
    "smokes(rebecca)"
])

print(friends_kb.query(pl.Expr("to_smoke(who,P)")))
# Expected output: [{'who': 'daniel', 'P': 0.48000000000004}, {'who': 'david', 'P': 0.430000000000005}]

print(friends_kb.query(pl.Expr("to_have_asthma(who,P)")))
# Expected output: [{'who': 'peter', 'P': 0.3}, {'who': 'rebecca', 'P': 0.3}, {'who': 'daniel', 'P': 0.1200000000001}, {'who': 'david', 'P': 0.430000000005}]
