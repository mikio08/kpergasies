import urllib2
import json
import  datetime 


cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s

numbers=[]
maxx=0
epit=0
for i in range(10):
    numbers.append(int(input("Dwse arithmo :"  )))



m=[]
lucky_day=""
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(numbers,tmp))
        m.append(r.count(r>3))
        lucky_date=""
        

        if (r.count(r>3)==max(m)):
            epit=epit+1
   
        if (epit>maxx):
            maxx=epit
            lucky_day=date_str



print ("h tyxerh sou mera einai: ", lucky_day)


        
    

     
    
