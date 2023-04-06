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

print(". Domestic")
for item in domestic:
    print(f"... {item['name']}\n    Price: ${item['price']}\n    {item['description']}")
    if item['weight'] == "N/A":
        print(f"    Weight: {item['weight']}")
    else:
        print(f"    Weight: {item['weight']}g")
print(". Imported")
for item in imported:
    print(f"... {item['name']}\n    Price: ${item['price']}\n    {item['description']}")
    if item['weight'] == "N/A":
        print(f"    Weight: {item['weight']}")
    else:
        print(f"    Weight: {item['weight']}g")
print(f"Domestic cost: ${dom_cost}\nImported cost: ${imp_cost}\nDomestic count: {len(domestic)}\nImported count: {len(imported)}")

