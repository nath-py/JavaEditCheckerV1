import hashlib
import requests
from colorama import init, Fore as cc
import time

dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

banner = f'''
{c}

       _                    ______    _ _ _                                       
      | |                  |  ____|  | (_) |                                      
      | | __ ___   ____ _  | |__   __| |_| |_                                     
  _   | |/ _` \ \ / / _` | |  __| / _` | | __|                                    
 | |__| | (_| |\ V / (_| | | |___| (_| | | |_ _____ _               _             
  \____/ \__,_| \_/ \__,_| |______\__,_|_|\__/ ____| |             | |            
                                            | |    | |__   ___  ___| | _____ _ __ 
                                            | |    | '_ \ / _ \/ __| |/ / _ \ '__|
                                            | |____| | | |  __/ (__|   <  __/ |     
                                             \_____|_| |_|\___|\___|_|\_\___|_|      {c}~ {w}dev by Assoh {c}~{w}
                                                                                  
                                                                                  


'''

sha256v = "https://pastebin.com/raw/k7trqG6H"

dec256v = requests.get(sha256v)

print(banner)

filename = input(f"[{y}?{w}] Enter the jar(version) with his path: ")
sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(f"[{c}!{w}] SHA256: ", sha256_hash.hexdigest())

getfile = input(f"[{y}?{w}] Enter the SHA256: ")
print(f"[{c}!{w}] {c}Scanning... {w}")

try:
    if getfile in dec256v.text:
        print(f"[{c}!{w}] {g}Java Edit Not Found, Legit.")
        time.sleep(1)
        pass
    else:
        print(f"[{c}!{w}] {r}Java Edit Found, Unlegit")
        time.sleep(10)
        exit()
except:
    print(f"[{c}!{w}] Something didn't work as it should! Try later")
    time(10)
    exit()

print(f"{w}Press enter to exit.")
input()