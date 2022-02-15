from machine import I2C,Pin         #从machine模块导入I2C、Pin子模块
from ssd1306 import SSD1306_I2C     #从ssd1306模块中导入SSD1306_I2C子模块
import res,time
def oneword():
    a=res.get("http://v1.hitokoto.cn")
    time.sleep(2)
    return eval(a.text)['hitokoto']
#http://192.168.2.7:9527/demo_war_exploded/chinese.jsp
#res.get("http://192.168.2.7:9527/demo_war_exploded/chinese.jsp")
i2c = I2C(sda=Pin(21), scl=Pin(22))   #pyBoard I2C初始化：sda--> Y8, scl --> Y6
#from machine import I2C, Pin
#i2c = I2C(sda=Pin(27), scl=Pin(14))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c) #OLED显示屏初始化：128*64分辨率,OLED的I2C地址是0x3c
#oled = SSD1306_I2C(128, 64, I2C(sda=Pin(21), scl=Pin(22)), addr=0x3c)
oled.font_load("GB2312-12.fon")
oled.fill(0)
help(oled.font_set)
text = oneword()
if len(text)>10:
    oled.text(text[0:10], 0,  16)
    oled.text(text[10:], 0,  32)
elif (text)>20:
    oled.text(text[0:10], 0,  16)
    oled.text(text[10:20], 0,  32)
    oled.text(text[20:], 0,  48)
else:
    oled.text(text, 0,  16)
oled.show()