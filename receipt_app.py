from requests import get

response = get('https://interview-task-api.mca.dev/qr-scanner-codes/alpha-qr-gFpwhsQ8fkY1')
produce_list = response.json()
produce_list.sort(key=lambda k: k["name"])
dom_cost = 0
imp_cost = 0
dom_count = 0
imp_count = 0

print(". Domestic")
for item in produce_list:
    if item["domestic"]:
        dom_count += 1
        dom_cost += item["price"]
        print(f"... {item['name']}\n    Price: ${item['price']}\n    {item['description'][:10]}...")
        if "weight" in item:
            print(f"    Weight: {item['weight']}g")
        else:
            print(f"    Weight: N/A")

print(". Imported")
for item in produce_list:
    if not item["domestic"]:
        imp_count += 1
        imp_cost += item["price"]
        print(f"... {item['name']}\n    Price: ${item['price']}\n    {item['description'][:10]}...")
        if "weight" in item:
            print(f"    Weight: {item['weight']}g")
        else:
            print(f"    Weight: N/A")

print(f"Domestic cost: ${dom_cost}\nImported cost: ${imp_cost}\nDomestic count: {dom_count}\nImported count: {imp_count}")

