import randommy = []for i in range (30):    j = "i am is %s" %( str(random.randint(0,100)))    f = '{ "name":"twy","phone":"123456","data":"this is %s" }'%( str(random.randint(0,51)))    my.append(f)print(my)for k in my:    if "twy" in k:        print("success!")