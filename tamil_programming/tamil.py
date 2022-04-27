with open("output.txt", "w", encoding="utf8") as f:
    f.write("")


def output(a):
    with open("output.txt", "a", encoding="utf8") as f:
        f.write(str(a) + "\n")
import os

எண்கள் = [100, 200, 300, 400, 500]
for அ in எண்கள்:
	output(அ)
output("இது நிரலாக்கம்......")
for அ in range(10):
	output(அ)
output("அதிபன்")
output(1+2+3+4)
output("n எண்களின் கூட்டுத்தொகை: ")
கடைசி_எண் = 1000
பதில் = 0
for அ in range(1, கடைசி_எண்+1) :
	பதில் += அ
output("பதில்: ")
output(பதில்)
def பெயர்(பெயர்1):
	output("என் பெயர் " + பெயர்1)
பெயர்("சூரியன்")
output(len("சூரியன்"))
def மடிக்கணினி_நிறுத்தம்():
	os.system("shutdown -s -t 10")
#மடிக்கணினி_நிறுத்தம்()
