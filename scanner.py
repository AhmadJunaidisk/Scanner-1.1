// Script Pribadi sy

import os
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system('cls')
    print("[!] Menginstall Bs4")
    os.system("pip install bs4" if os.name == "nt" else "pip install bs4")
try: 
    import requests_html
    from requests_html import HTMLSession
except ImportError:
    os.system('cls')
    print("[!] Menginstall Request_html()")
    os.system("pip install requests_html" if os.name == "nt" else "pip install requests_html")

from bs4 import BeautifulSoup as xe
from requests_html import HTMLSession
import os

def baca(namafile):
    with open(namafile, "r") as groups:
        isi_address = groups.readlines()
        return isi_address

def main(__url__,Choose,Options): 
    if Options == "all":
        lenght = baca("address.txt")
        for looping in range(len(lenght)):
            acc = baca("address.txt")
            akun = acc[looping].strip()
            session = HTMLSession()
            page = session.get(url=__url__+akun)
            soup = xe(page.content, 'html.parser')
            addressHeader = soup.find("span", class_="text-size-address text-secondary text-break mr-1").text
            address = soup.findAll("a", class_="link-hover d-flex justify-content-between align-items-center", href=True)
            values = soup.findAll("div", class_='col-md-8')
            est = values[0].text
            try:
                JumlahToken = soup.find("span", class_="badge badge-primary mx-1").text
                IsiToken = soup.findAll("span", class_="list-amount link-hover__item hash-tag hash-tag--md text-truncate")
                print("\nAddress ke-{} -> {}".format(looping,addressHeader))
                print("Token:")
                if Choose in [1,3,4,5]:
                    for i in range(int(JumlahToken)):
                        print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun,"").replace('/token/', '')))
                elif Choose == 2:
                    for i in range(int(JumlahToken)):
                        print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun.lower(),"").replace('/token/', '')))
                print("\nEstimasi: {}".format(est))
                print("-"*70)
            except AttributeError:
                try:
                    print("\n\nAddress ke-{} -> {}\n [!] Tidak ada token".format(looping,addressHeader))
                    print("-"*70)
                except:
                    error_handle = soup.find("h1", class_="h4 mb-0").text.strip()
                    print(error_handle+": "+akun)

    elif Options == "sort":
        lenght = baca("address.txt")
        for looping in range(len(lenght)):
            acc = baca("address.txt")
            akun = acc[looping].strip()
            session = HTMLSession()
            page = session.get(url=__url__+akun)
            soup = xe(page.content, 'html.parser')
            addressHeader = soup.find("span", class_="text-size-address text-secondary text-break mr-1").text
            address = soup.findAll("a", class_="link-hover d-flex justify-content-between align-items-center", href=True)
            values = soup.findAll("div", class_='col-md-8')
            est = values[0].text
            try:
                JumlahToken = soup.find("span", class_="badge badge-primary mx-1").text
                IsiToken = soup.findAll("span", class_="list-amount link-hover__item hash-tag hash-tag--md text-truncate")
                print("\nAddress ke-{} -> {}".format(looping,addressHeader))
                print("Token:")
                if Choose in [1,3,4,5]:
                    for i in range(int(JumlahToken)):
                        if i == 0:
                            print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun,"").replace('/token/', '')))
                        elif i > 0:
                            print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun,"").replace('/token/', '')))
                elif Choose == 2:
                    for i in range(int(JumlahToken)):
                        if i == 0:
                            print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun.lower(),"").replace('/token/', '')))
                        elif i > 0:
                            print("   [{}] {} Sc -> {}".format(i,IsiToken[i].text,address[i]["href"].replace('?a='+akun.lower(),"").replace('/token/', '')))
                print("\nEstimasi: {}".format(est))
                print("-"*70)
            except AttributeError:
                pass

def menu():
    os.system('cls')
    print("-- BLOCKSCAN --")
    print('[1] BSC\n[2] ETH\n[3] POLYGON\n[4] HECO Chain\n[5] FANTOM')
    a = int(input(">:"))
    if a == 1:
        print("-- PILIHAN --")
        print("[1] Tampilkan Semua Address")
        print("[2] Tampilkan Address yang ber-isi saja")
        input_op = int(input("->"))
        if input_op == 1:
            os.system('cls')
            print("\n --- Binance Chain -- ")
            main('https://bscscan.com/address/',Choose=1,Options="all") 
        elif input_op == 2:
            os.system('cls')
            print("\n --- Binance Chain (Sort) -- ")
            main('https://bscscan.com/address/',Choose=1,Options="sort") 

    elif a == 2:
        print("-- PILIHAN --")
        print("[1] Tampilkan Semua Address")
        print("[2] Tampilkan Address yang ber-isi saja")
        input_op = int(input("->"))
        if input_op == 1:
            os.system('cls')
            print("\n --- Ethereum -- ")
            main('https://etherscan.com/address/',Choose=1,Options="all") 
        elif input_op == 2:
            os.system('cls')
            print("\n --- Ethereum (Sort) -- ")
            main('https://etherscan.com/address/',Choose=1,Options="sort") 

    elif a == 3:
        print("-- PILIHAN --")
        print("[1] Tampilkan Semua Address")
        print("[2] Tampilkan Address yang ber-isi saja")
        input_op = int(input("->"))
        if input_op == 1:
            os.system('cls')
            print("\n --- Polygon Scan -- ")
            main('https://polygonscan.com/address/',Choose=1,Options="all") 
        elif input_op == 2:
            os.system('cls')
            print("\n --- Binance Chain (Sort) -- ")
            main('https://polygonscan.com/address/',Choose=1,Options="sort") 

    elif a == 4:
        print("-- PILIHAN --")
        print("[1] Tampilkan Semua Address")
        print("[2] Tampilkan Address yang ber-isi saja")
        input_op = int(input("->"))
        if input_op == 1:
            os.system('cls')
            print("\n --- HECO Scan -- ")
            main('https://https://hecoinfo.com/address/',Choose=1,Options="all") 
        elif input_op == 2:
            os.system('cls')
            print("\n --- Binance Chain (Sort) -- ")
            main('https://https://hecoinfo.com/address/',Choose=1,Options="sort") 

    elif a == 5:
        print("-- PILIHAN --")
        print("[1] Tampilkan Semua Address")
        print("[2] Tampilkan Address yang ber-isi saja")
        input_op = int(input("->"))
        if input_op == 1:
            os.system('cls')
            print("\n --- Fantom Scan -- ")
            main('https://ftmscan.com/address/',Choose=1,Options="all") 
        elif input_op == 2:
            os.system('cls')
            print("\n --- Fantom Scan (Sort) -- ")
            main('https://ftmscan.com/address/',Choose=1,Options="sort") 
    else:
        print('[!] Wrong')

    i = input("Back? (y/t)")
    if i in ['y','ya','Y']:
        menu()


if __name__ == '__main__':
    menu()
