from concurrent.futures import process
import multiprocessing
import random
from rich import print
from rich.panel import Panel
from rich.console import Console
from hdwallet import HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import is_mnemonic
from lxml import html
from mnemonic import Mnemonic
from multiprocessing import Process
import requests
from lxml import html

console = Console()


def mmdrza() :
    z = 1
    w = 0
    while True :
        z += 1

        langrnd = ['english' , 'french']
        sellan = random.choice(langrnd)
        mne = Mnemonic(str(sellan))
        listno = ["128" , "256"]
        rnd = random.choice(listno)
        words = mne.generate(strength = int(rnd))
        STRENGTH = int(rnd)
        LANGUAGE: str = (sellan)
        MNEMONIC = words
        PASSPHRASE: str = "meherett"
        assert is_mnemonic(mnemonic = words , language = sellan)

        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,
                                                      address = 0)
        bip44_hdwallet.from_mnemonic(mnemonic = MNEMONIC , passphrase = PASSPHRASE , language = LANGUAGE)
        mixword = words[:32]
        addr = bip44_hdwallet.p2pkh_address()
        priv = bip44_hdwallet.private_key()
        # =======================================
        urlblock = "https://ethereum.atomicwallet.io/address/"+addr
        respone_block = requests.get(urlblock)
        byte_string = respone_block.content
        source_code = html.fromstring(byte_string)
        xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
        treetxid = source_code.xpath(xpatch_txid)
        xVol = str(treetxid[0].text_content())
        elapsed = respone_block.elapsed
        timer = elapsed
        bal = xVol

        print('Total Scan Checking -----  =', str(z*25), 'Winning --- =', str(w), end='\r')
        z += 1
        if float(bal) > 0:
            w += 1
            f1 = open('Win.txt' , 'a')
            f1.write('\nAddress     === '+str(addr))
            f1.write('\nPrivateKey  === '+str(priv))
            f1.write('\nMnemonic    === '+str(words))
            f1.write('\nTransaction === '+str(bal))
            f1.write('\n            -------[NHAT VUONG]------                   \n')
            f1.close()

    # ============================
processes = []
for i in range(25): 
    p = multiprocessing.Process(target = mmdrza)
    if __name__ == '__main__' :
        p.start()
        processes.append(p)
for p in processes:
    p.join()
