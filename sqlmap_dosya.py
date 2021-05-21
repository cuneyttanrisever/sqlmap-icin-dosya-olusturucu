import requests
import Queue
from urlparse import urlparse
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    red = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
print bcolors.yesil + """
########################################
#  Cüneyt TANRISEVER                   #
#  Sqlmap icin dosya olusturucu v.0.1  #
#                                      #
#  NoT:  sadece get url icindir        #
#                                      #
########################################"""+bcolors.ENDC
q=Queue.Queue()
qq=Queue.Queue()

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
r=requests.session()
r.headers.update(header)
url= raw_input(bcolors.red+"sqlmap icin tam urlyi girin = \n"+bcolors.ENDC)
verifty="/data/data/com.termux/files/usr/lib/python2.7/site-packages/certifi/cacert.pem"
c=r.get(url,verify=verifty)
ka=urlparse(url)

k=c.headers
vc, vv =k.keys(), k.values()
kq=vc
for i in vc:
    q.put(str(i))
la=open("sqlm.txt","w")
la.close()
for ll in vv:
        qq.put(str(ll))
G= "GET "+ka.path+"?"+ka.query+" HTTP/1.1\n"
H= "Host: "+ka.netloc+ "\n"
ls=open("sqlm.txt","a")
ls.write(G)
ls.write(H)
ls.close()
kll=[]
for d in range(len(kq)):
    pk = q.get()+": "+qq.get()+"\n"
    kll.append(pk)
    
for kl in kll:
	if not  "Transfer-Encoding:"  in kl:
		ls=open("sqlm1.txt","a")
		ls.write(kl)
ls.close()


#for d in range(len(kq)):
 #   pk = q.get()+": #"+qq.#get()+"\n"#
  #  ls=open("sqlm1.txt",#"a")
    
#    ls.write(#pk)
#ls.close()



print bcolors.yesil+"sonuclar sqlm.txt yazildi"+bcolors.ENDC

