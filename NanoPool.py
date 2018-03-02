import requests
from datetime import date
from time import sleep

try:
    file=open("nanopool.config","r")
    address=file.readline()
    address = address[:-1]
    file.close()

except IOError as e:
    print(e)

while True:
    try:
        content=requests.get("https://api.nanopool.org/v1/eth/user/"+address)
        payementContent=requests.get("https://api.nanopool.org/v1/eth/payments/"+address)
        #########HASHRATE INFO########
        generalInfo=content.json()
        data=generalInfo["data"]
        # print(data)
        print("\n"*5)
        print("NanoPool ----> {}\033[0m".format("\033[92mONLINE" if generalInfo["status"] else "\033[91mOUTLINE"))
        print("balance :\t\t{} ETH".format(data["balance"]))
        print("current hashrate :\t{} Mh/s".format(data["hashrate"]))
        print("\tavgH1 : {:.4} Mh/s\t avgH6 : {:.4} Mh/s".format(data["avgHashrate"]["h1"],data["avgHashrate"]["h6"]))
        print("\tavgH3 : {:.4} Mh/s\t avgH12 : {:.4} Mh/s".format(data["avgHashrate"]["h3"],data["avgHashrate"]["h12"]))
        print()
        for worker in data["workers"]:
            print("Worker [{}]".format(worker["id"]))
            print("\thashrate :\t{} Mh/s".format(worker["hashrate"]))
            print("\tWAvgH1 : {:.4} Mh/s\t WAvgH6 : {:.4} Mh/s".format(worker["h1"],worker["h6"]))
            print("\tWAvgH3 : {:.4} Mh/s\t WAvgH12 : {:.4} Mh/s".format(worker["h3"],worker["h12"]))

        #######PAYEMENT#######
        payementInfo=payementContent.json()
        payementData=payementInfo["data"]
        # print(payementInfo)
        print("\nPayements:")
        for payement in payementData :
            print("\taddress: {}\n\tamount: {} ETH\t\tconfirmed: {}\033[0m".format(payement["txHash"],payement["amount"],"\033[92mTrue" if payement["confirmed"] else "\033[91mFalse"))


        sleep(10)
    except Exception as e:
        print(e)
