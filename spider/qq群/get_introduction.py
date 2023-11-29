
import time
import pandas as pd
from appium.webdriver.I

def diver(id):
    try:
        time.sleep(2)
        driver.find_element_by_xpath(
            '//android.widget.RelativeLayout[@content-desc="搜索聊天或者联系人"]/android.widget.EditText'
        ).clear()
        driver.find_element_by_xpath(
            '//android.widget.RelativeLayout[@content-desc="搜索聊天或者联系人"]/android.widget.EditText'
        ).send_keys(id)
        time.sleep(1)
        driver.find_element_by_xpath(
            r'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.AbsListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="群聊设置"]').click()
        time.sleep(2)
        ele = driver.find_element_by_xpath('//android.widget.RelativeLayout[@content-desc="资料卡"]/android.widget.RelativeLayout/android.widget.TextView[2]')
        print(ele.text)
        list.append(ele.text)
        driver.back()
        time.sleep(0.4)
        driver.back()
    except:
        list.append('未获取')


from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "48572fa5"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


df = pd.read_csv("result.csv")
df.drop_duplicates()
list = []
driver.find_element_by_xpath('//android.widget.EditText[@content-desc="搜索"]').click()
for i in range(0, 30):
    diver(str(df['群号'][i]))

print(list)

df.insert(len(df.columns), '简介', [x for x in list])
df.to_csv('result.csv')
driver.close()


