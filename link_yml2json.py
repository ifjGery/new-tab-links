#!/usr/bin/python
import yaml
import json

def main():
    stream = open('links.yml', 'r')

    groups = yaml.safe_load(stream)

    data = []
    for links in groups:
        group = {
            "name": links.keys()[0],
            "links" : []
        }
        for link in links[links.keys()[0]]:
            item = {
                "name": link["name"],
                "url": link["url"]
            }
            group["links"].append(item)
        data.append(group)
        
    f = open('links.json', 'w')
    f.write("data = " + json.dumps(data))
    f.close()
    
if __name__ == "__main__":
    main()