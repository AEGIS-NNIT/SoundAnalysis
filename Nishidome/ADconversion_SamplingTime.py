# This program is written in Python3

from gpiozero import MCP3008            #gpiozero(モジュール)からMCP3008(ADコンバーター)の関数をインポート
import time


# Maximum input voltage = 3.3V
V0 = 3.3                                #Raspberry Pi3では3.3Vと5Vの出力電圧が使える

start = time.time()

input0 = MCP3008(channel=0)     #MCP3008では0～7までのアナログ入力が可能
input1 = MCP3008(channel=1)
input2 = MCP3008(channel=2)
input3 = MCP3008(channel=3)
input4 = MCP3008(channel=4)
input5 = MCP3008(channel=5)
input6 = MCP3008(channel=6)
input7 = MCP3008(channel=7)

voltage0 = V0 * input0.value  # V0を乗じることでinputの値をアナログ値にする
voltage1 = V0 * input1.value
voltage2 = V0 * input2.value
voltage3 = V0 * input3.value
voltage4 = V0 * input4.value
voltage5 = V0 * input5.value
voltage6 = V0 * input6.value
voltage7 = V0 * input7.value

print("A0 :", voltage0)  # A0～7の電圧値を表示する
print("A1 :", voltage1)
print("A2 :", voltage2)
print("A3 :", voltage3)
print("A4 :", voltage4)
print("A5 :", voltage5)
print("A6 :", voltage6)
print("A7 :", voltage7)

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")   #format関数