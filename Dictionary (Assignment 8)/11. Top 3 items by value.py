d1 = {'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}

top3 = sorted(d1.items(), key=lambda x: x[1], reverse=True)[:3]

for item, price in top3:
    print(item, price)
