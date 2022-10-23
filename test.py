#from technical_analysis.src.data_fetcher.zerodha_endpoints import ZerodhaEndpoint

#print(ZerodhaEndpoint.STOCK_LISTING_BROWSER)

import json
import requests
import pdb

def main():
    data = requests.get("https://kite.zerodha.com/static/js/chunk-2d22c101.6fbdfb55.js").text
    jsonind = data.find("JSON.parse(") + len("JSON.parse(")
    jsondata = data[jsonind:]
    ind = 1
    nquote = 1
    while (nquote != 0):
        if jsondata[ind] == '\'':
            break
        ind += 1
    jsondata = jsondata[1: ind]
    jsondict = json.loads(jsondata)
    with open("./data/zerodha-listings.json","w") as f:
        data = json.dumps(jsondict)
        f.write(data)
        
    toparse = []
    toparse.append((jsondict,"root"))
    while len(toparse) != 0:
        currdict,fname = toparse[0]
        if type(currdict) == dict:
            for key in currdict.keys():
                toparse.append((currdict[key], f"{fname}.{key}"))
        else:
            with open(f"./data/{fname}.json", "w") as f:
                f.write(json.dumps(currdict))
        toparse = toparse[1:]


main()
