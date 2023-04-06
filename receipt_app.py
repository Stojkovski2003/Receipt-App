from requests import get

response = get('https://interview-task-api.mca.dev/qr-scanner-codes/alpha-qr-gFpwhsQ8fkY1')
produce_list = response.json()
domestic = []
imported = []
dom_cost = 0
imp_cost = 0

for item in produce_list:
    item["description"] = item["description"][:10] + "..."
    if "weight" not in item:
        item["weight"] = "N/A"
    if item["domestic"]:
        domestic.append(item)
        dom_cost += item["price"]
    else:
        imported.append(item)
        imp_cost += item["price"]

domestic.sort(key=lambda k: k["name"])
imported.sort(key=lambda k: k["name"])



