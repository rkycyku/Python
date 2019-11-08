fjalori = {}

emri = input("Si e keni emrin? ")
emri = emri.lower()

fjalori["rilind"] = "043701401"
fjalori["melos"] = "043702402"
fjalori["besnik"] = "043703403"
fjalori["majlinda"] = "043704404"


if emri not in fjalori:
    print("E keni shkruar emrin gabim! ")
else:
    print(fjalori.get(emri))
