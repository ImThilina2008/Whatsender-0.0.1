import Trans as m
import time
import subprocess as ter
import os 
import urllib
import Trans
import shutil as pil
from Trans import MSG
import wget
import requests as req
from filesplit.split import Split
#https://vod-progressive.akamaized.net/exp=1649504329~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F1962%2F23%2F584812249%2F2760499793.mp4~hmac=2c46ea5f2adcaa79ae6d6f4036738e80ac905efe1e274199b787d4a9e4d0af40/vimeo-prod-skyfire-std-us/01/1962/23/584812249/2760499793.mp4?download=1&filename=pexels-ekrulila-9117908.mp4

class main():
    Main = True
    while Main == True:
        c1 = input(m.MSG.main_menu)
        if c1 == "01" or c1 == "1":
            link1 = input(MSG.linkin)
            if "https"  in link1 or link1 in "http":
                filename = wget.filename_from_url(link1)
                print(MSG.url_download2)
                wget.download(link1, out="Down/")
                exist_file = os.path.isfile(f'Down/{filename}')
                while exist_file:
                    split_file = Split(inputfile=f"Down/{filename}", outputdir=f"Split/")
                    split_file.bysize(103809024)
                    Dsize = os.path.getsize(f"Down/{filename}")
                    Dchunks = Dsize/103809024
                    Dchunks1 = Dsize-(103809024*Dchunks)
                    if Dchunks1>0:
                        Dchunks += 1
                    chunks = []
                    Leg = 1
                    while Leg<Dchunks+1:
                        name0 = f"{filename}_{Leg}"
                        chunks.append(name0)
                        Leg += 1
                    detailes = f"""
                    class Data():
                        Name = {filename}
                        Size = {Dsize}
                        Chunks = {Dchunks}
                        Chunknames = {chunks}
                    """
                    with open("FileData.py", "w") as f:
                        f.write(detailes)
                    import Sender
            elif link1 == "0":
                pass
            else:
                print("Error 404 :(")
            
        # elif c1 == "02" or c1 == "2":
        #     mg_link = input("Enter the Magnet link => ")
        elif c1 == "00" or c1 == "0":
            Main = False
        elif not c1 == "01" or not c1 == "02" or not c1 == "03" or not c1 == "1" or not c1 == "2" or not c1 == "3":
            print("Error : Wrong option")
            time.sleep(2)