from colorama import Fore
import time
import secrets
from random import randint

continuing = True

btcval = 27186.30

while True:
  if continuing == True:
    time.sleep(.01)
    ranInt = randint(0, 6000)
    if ranInt <= 1:
      randomBTC = randint(5, 10)
      print(Fore.RED + "> 0x" + secrets.token_hex(20) + Fore.GREEN + " > " +
            str(randomBTC) + " BTC (€" +
            str("{:,}".format(round(btcval * randomBTC, 2))) +
            ") has been send to your crypto wallet")
      answer = input("> Would you like to continue? (Y/N): ")
      if answer.lower() == "y":
        continuing = True
      else:
        continuing = False
    else:
      print(Fore.RED + "> 0x " + secrets.token_hex(20) + Fore.RED +
            " > 0.00 BTC ($0.00")
  else:
    break
