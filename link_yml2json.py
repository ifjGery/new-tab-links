#!/usr/bin/python
import yaml
import json

def main():
    stream = open('links.yml', 'r')

    groups = yaml.safe_load(stream)

    data = [ 
        { 
            "name": links.keys()[0], 
            "links" : [ 
                {
                    "name": link["name"], 
                    "url": link["url"] 
                } for link in links[links.keys()[0]] 
            ] 
        } for links in groups 
    ]
        
    f = open('links.json', 'w')
    f.write("data = " + json.dumps(data))
    f.close()
    
if __name__ == "__main__":
    main()