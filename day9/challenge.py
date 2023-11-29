travel_log = [
    {
    "country":"France",
    "visits":12,
    "cities": ["Paris","Lille","Dijon"],
    },
    {
    "country":"Germany",
    "visits":20,
    "cities":["Berlin","Harmburg","Stuttgart"],
     }
] 

def add_new_country(country_visited,visit_time,city_visited):
    new = {}
    new["country"] = country_visited
    new["visit"] = visit_time
    new["cities"]= city_visited
    travel_log.append(new)

add_new_country("Russia",2,["Moscow","saint Petersburg"])
print(travel_log)
    