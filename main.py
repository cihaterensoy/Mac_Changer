import subprocess  # shellde komut çalıştırmaya yarayan bir kütüphane
import argparse
import random


class MAC_Changer:


    def parseinfo(self):
        # kullanıcıdan parametre almamızı sağlar
        parse_o = argparse.ArgumentParser()
        # dest = argümanı nesnenin hangi özelliğine atayacağımızı söyler
        parse_o.add_argument("-i", "--interface", dest="interface", help="please enter the interface")

        self.data = parse_o.parse_args()  # alınan parametrelerin herbirini bir değere atıyoruz

        return self.data

    def random_mac(self):
        # random bir şekilde mac adresi oluşturacağız
        hex_number = "0123456789ABCDEF"
        self.hex_sutun = ""
        for i in range(6):
            for j in range(2):
                self.hex_sutun = self.hex_sutun + random.choice(hex_number)
            if i < 5:
                self.hex_sutun = self.hex_sutun + ":"

        return self.hex_sutun

    def Change_mac(self):
        # shellde istediğimiz komutları çalıştırmamıza yarar
        subprocess.call(["ifconfig", self.data.interface, "down"])
        subprocess.call(["ifconfig", self.data.interface, "hw", "ether", self.hex_sutun])
        subprocess.call(["ifconfig", self.data.interface, "up"])


if __name__ == "__main__":  # çağrılan dosya main olduğu sürece çalıştır
    mac_changer = MAC_Changer()
    mac_changer.parseinfo()
    mac_changer.random_mac()
    print("Yeni MAC Adresi:", mac_changer.hex_sutun)
    mac_changer.Change_mac()
