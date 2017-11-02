def process_user_query(query_string):
    places = {}
    results = []
    counter=1
    results.append(f"Top places to visit in {query_string}")
    file = open("Countries.txt",'r',encoding='utf-8')
    for line in file:
        places[line.split(' ')[0]] = line.split(' ')[1]
    final = places[query_string].split(';')
    for name in final:
        results.append(f"{counter}. {name}")
        counter += 1
    return results
