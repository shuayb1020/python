# nesting a list in a dictionary
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Harmburg","Stuttgart"],
}
# Nesting a dictionary in a ditionary
travel_log = {
    "France":{"citie_visited": ["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Harmburg","Stuttgart"], "total_visits":20}   
}
# nesting dictionary in a list
travel_log = [
    {
    "country":"France",
    "cities_visited": ["Paris","Lille","Dijon"],
    "total_visits":12
    },
    {
    "country":"Germany",
    "cities_visited":["Berlin","Harmburg","Stuttgart"], 
    "total_visits":20
     }
] 