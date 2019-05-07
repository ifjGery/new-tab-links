#!/usr/bin/python
import yaml

stream = open('links.yml', 'r')

lnk = yaml.safe_load(stream)

f = open('links.json', 'w')
f.write("data = [" + "\n")
for i in lnk:
    f.write("    {" + "\n")
    f.write("        'name': '" + i.keys()[0] + "'," + "\n")
    f.write("        'links': [" + "\n")
    for j in i[i.keys()[0]]:
        f.write("            {" + "\n")
        f.write("                'name': '" + j["name"] + "'," + "\n")
        f.write("                'url': '" + j["url"] + "'," + "\n")
        f.write(("            }," if j != i[i.keys()[0]][-1] else "        }") + "\n")
    f.write("        ]" + "\n")
    f.write(("    }," if i != lnk[-1] else "    }") + "\n")
f.write("]" + "\n")