import requests
import json

# XANO Custom API to clear a table
r_clear_table = requests.get("https://xwoo-j1go-c7xy.n7.xano.io/api:ZURuvRuy/clear-all-deals")
print("Clearing deals table...")
print(r_clear_table.status_code)

# Open JSON file 
with open("deals.json") as f:
    data = json.load(f)
  
    print(json.dumps(data))

    # (optional) Test POST to webhook.site 
    # r = requests.post('https://webhook.site/e70c2315-3841-46ab-a5cc-a3dc7eff4eee',data=json.dumps(data))
    
    # POST json content to XANO bulk-add API endpoint
    r = requests.post('https://xwoo-j1go-c7xy.n7.xano.io/api:ZURuvRuy/deals-bulk-add',data=json.dumps(data))

    print("Uploading new deals...")
    print(r.status_code)


