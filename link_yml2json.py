#!/usr/bin/python
import yaml
import json

def makeItem(links):
    name = links.keys()[0]
    return { 
        "name": name, 
        "links" : [ 
            {
                "name": link["name"], 
                "url": link["url"] 
            } for link in links[name]
        ] 
    }

def main():
    with open('links.yml', 'r') as stream:
        groups = yaml.safe_load(stream)

        data = [ makeItem(links) for links in groups ]
        
        with open('links.json', 'w') as file:
            file.write("data = " + json.dumps(data))
    
if __name__ == "__main__":
    main()