import json
from pprint import pprint
from decimal import Decimal
pos_inf = Decimal('Infinity')
neg_inf = Decimal('-Infinity')


with open('../Dataset/annotation.json') as f:
    data = json.load(f)

d = {}
terminate = 0;
for key, vlist in data.items():
    max_x = neg_inf;
    max_y = neg_inf;
    min_x = pos_inf;
    min_y = pos_inf;
    for i in vlist:
        if i[0]> max_x:
            max_x = i[0];
        if  i[0]< min_x:
            min_x = i[0];
        if i[1]> max_y:
            max_y = i[1];
        if  i[1]< min_y:
            min_y = i[1];
    d[key] = [(min_x + max_x)/2,(min_y + max_y)/2,(max_x - min_x),(max_y - min_y)];

# write key to a new file
with open('../Dataset/new_annotation.json', 'w') as f:
    f.write(json.dumps(d))