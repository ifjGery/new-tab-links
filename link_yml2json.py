#!/usr/bin/python
import yaml
import json

def main():
    with open('links.yml', 'r') as stream:
        groups = yaml.safe_load(stream)

        data = [ make_item(links) for links in groups ]
        
        with open('links.json', 'w') as out:
            out.write("data = " + json.dumps(data))
            
def make_item(links):
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
    
if __name__ == "__main__":
    main()