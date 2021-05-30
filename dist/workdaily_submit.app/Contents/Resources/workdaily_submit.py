import tkinter
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
import os
import json
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

import threading

scheduler = BlockingScheduler()

#scheduler = BlockingScheduler()

Test_JsonDataPath = r"%s/%s" % (os.path.dirname(
    os.path.realpath(__file__)), 'config.json')
with open(Test_JsonDataPath, encoding='utf-8') as f:
    TestData_Get = json.load(f, strict=False)


def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


class Autotoreport(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("AutoMation DailyWork")
        width, height = 960, 800
        screenwidth, screenheight = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.size = '%dx%d+%d+%d' % (width, height,
                                     (screenwidth - width)/2, (screenheight - height)/2)
        self.root.geometry(self.size)
        self.myStr = tkinter.StringVar()
        # self.myStr.set("当前配置信)

        self.label = tkinter.Label(
            self.root, textvariable=self.myStr, bg='white', width=60, height=1)
        # URL TEXTBOX:
        self.test_url = tkinter.LabelFrame(
            self.root, width=460, height=120, text="账号密码-逗号分割")
        self.page_url = tkinter.Entry(self.test_url, width=40, relief='solid')
        # REQUEST URL:
        self.rqment_url = tkinter.LabelFrame(
            self.root, width=160, height=238, text='工作项目')
        self.text_url = tkinter.Entry(
            self.rqment_url, width=15, relief='solid')
        self.button1 = tkinter.Button(
            self.rqment_url, text="RESET_URL", command="")
        self.button2 = tkinter.Button(
            self.rqment_url, text='PRINT', command="")
        self.textbox = tkinter.Text(
            self.rqment_url, width=10, height=10, relief='solid')
        # CHOSE PLATFORM:
        self.platform = tkinter.LabelFrame(
            self.root, width=96, height=96, text='platfrom')
        self.varRadio = tkinter.StringVar()
        self.platform1 = tkinter.Radiobutton(
            self.platform, text='APP', value='天天基金APP', variable=self.varRadio, command=self.radiobutton_click)
        self.platform2 = tkinter.Radiobutton(
            self.platform, text='WEB', value='天天基金WEB', variable=self.varRadio, command=self.radiobutton_click)
        # CHECK TESTER:
        self.tester = tkinter.LabelFrame(
            self.root, width=96, height=96, text='Tester')
        self.varCheck1 = tkinter.IntVar()
        self.varCheck2 = tkinter.IntVar()
        self.checkbutton1 = tkinter.Checkbutton(
            self.tester, text='Zhou', variable=self.varCheck1, onvalue=1, offvalue=0, command="")
        self.checkbutton2 = tkinter.Checkbutton(
            self.tester, text='Zhang', variable=self.varCheck2, onvalue=1, offvalue=0, command="")
        # GET PAGEINFO：
        self.MenuButton = tkinter.LabelFrame(
            self.root, width=200, height=96, text='工作内容')
        self.worktext = tkinter.Entry(
            self.MenuButton, width=20, relief='solid')
        # CONF:
        self.Listbox = tkinter.LabelFrame(
            self.root, width=260, height=240, text='时间-点')
        self.listbox = tkinter.Entry(self.Listbox, width=20, relief='solid')
        self.button4 = tkinter.Button(
            self.Listbox, text="saveConfig", height=2, command=self.change_dailyinfo)
        # SCROLLED：
        self.scrotext = tkinter.LabelFrame(
            self.root, width=935, height=410, text='Console')
        self.scroconsole = ScrolledText(self.scrotext, width=900, height=380)
        # Develope:
        # self.Develope = tkinter.LabelFrame(self.root,width=300,height=96,text='DevelopeMan')
        # START BUTTON:LableFrame and BUtton
        self.start_button = tkinter.LabelFrame(
            self.root, width=96, height=96, text='手动运行提交日志')
        self.s_button = tkinter.Button(
            self.start_button, text='MAIN_START', width=10, height=3, command=lambda: thread_it(self.start_submit)).pack()

    def layout_arr(self):
        self.label.grid(row=0, column=0, columnspan=6)
        # startbutton:
        self.start_button.grid(row=1, column=0, sticky='w', padx=10)
        # self.s_button.place(x=6, y=1)
        # pagetesturl inputtextbox:
        self.test_url.grid(row=2, column=0, sticky='w', padx=10, columnspan=4)
        self.page_url.place(x=12, y=40)
        # requstmentinfo:
        self.rqment_url.grid(row=1, column=4, rowspan=2, padx=6,  sticky='w')
        self.text_url.place(x=6, y=1)
        # self.button1.place(x=6, y=32)
        # self.button2.place(x=85, y=32)
        self.textbox.place(x=6, y=72)
        self.MenuButton.grid(row=1, column=2, sticky='w')
        self.worktext.place(x=6, y=2)
        # Listbox for all：
        self.Listbox.grid(row=1, column=5, rowspan=2,  sticky='w')
        self.listbox.place(x=6, y=1)
        self.button4.place(x=164, y=30)
        # end:
        self.scrotext.grid(row=4, column=0, columnspan=6, padx=10, sticky='w')
        self.scroconsole.place(x=6, y=2)
        # developeman:
        # self.Develope.grid(row=3, column=0, padx=10,sticky='w')
        # self.dename.place(x=6,y=2)

    def radiobutton_click(self):
        self.myStr.set('You have selected ' + self.varRadio.get())
        self.scroconsole.insert(tkinter.constants.INSERT,
                                "check platform:%s" % (self.varRadio.get())+"\n")

    def change_dailyinfo(self):
        if self.page_url.get() or self.text_url.get() or self.listbox.get() or self.worktext.get():
            if self.page_url.get():
                # self.scroconsole.insert(tkinter.constants.INSERT,"action:%s"%(self.page_url.get())+"\n")
                userinfo = self.page_url.get().split(",", 1)
                TestData_Get['username'], TestData_Get['password'] = userinfo[0], userinfo[1]

            if self.text_url.get():
                workdaily = self.text_url.get()
                TestData_Get['workitem'] = workdaily

            if self.listbox.get():
                duration = self.listbox.get()
                TestData_Get['duration'] = duration

            if self.worktext.get():
                workdaily = self.worktext.get()
                TestData_Get['workdaily'] = workdaily

            Run_JsonDataPath = r"%s/%s" % (os.path.dirname(
                os.path.realpath(__file__)), 'config.json')
            with open(Run_JsonDataPath, "w") as f:
                json.dump(TestData_Get, f, ensure_ascii=False)
                f.close()
            self.myStr.set("保存成功,3s钟后重启")

            for i in range(3):
                time.sleep(1)

            self.restart_program()

            # self.scroconsole.insert(tkinter.constants.INSERT,"action:%s"%(TestData_Get)+"\n")
        else:
            self.scroconsole.insert(tkinter.constants.INSERT, "当前配置信息:%s" % (
                TestData_Get)+"\n")
            self.myStr.set("没有要更新的信息")

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def start_submit(self):
        print("1")
        try:
            number = 0
            for i, j in TestData_Get.items():
                if j == "":
                    number += 1
                    self.scroconsole.insert(
                        tkinter.constants.INSERT, "缺少配置:%s" % (i)+"\n")
            if number == 0:

                self.myStr.set("运行开始")
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--window-size=1920,1050')

                # 创建浏览器对象
                driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"%s/%s" % (
                    os.path.dirname(os.path.realpath(__file__)), 'chromedriver'))
                # driver = webdriver.Chrome()  # 不加 chrome_options 参数就是正常的打开一个浏览器，进行操作
                print(os.path.dirname(os.path.realpath(__file__)))
                driver.implicitly_wait(10)
                driver.get('https://app.77hub.com/cn-global/login')
                username = driver.find_element_by_css_selector(
                    "#root > div > div._3PTQO6SSLkfkhgUDSNnMsG > div._11shczH-kuHWdF4aBACbNJ > div._3gtWl95XzmToV3rB8ytqiX > div > div > div.D2N9CcrtDp7Re5jCZU7qj > div.ms-LayoutGroup.css-1 > div.ms-LayoutGroup-item.css-0 > div > div.atx-input-group__bundle > div > input")
                username.send_keys(TestData_Get['username'])
                password = driver.find_element_by_css_selector(
                    "#root > div > div._3PTQO6SSLkfkhgUDSNnMsG > div._11shczH-kuHWdF4aBACbNJ > div._3gtWl95XzmToV3rB8ytqiX > div > div > div.D2N9CcrtDp7Re5jCZU7qj > div.ms-LayoutGroup.css-1 > div:nth-child(2) > div > div.atx-input-group__bundle > div > input")
                password.send_keys(TestData_Get['password'])

                driver.find_element_by_css_selector(
                    "#root > div > div._3PTQO6SSLkfkhgUDSNnMsG > div._11shczH-kuHWdF4aBACbNJ > div._3gtWl95XzmToV3rB8ytqiX > div > div > div.D2N9CcrtDp7Re5jCZU7qj > button > span").click()

                time.sleep(5)

                close_button = driver.find_element_by_css_selector(
                    "body > div:nth-child(17) > div > div.bp3-dialog-container.bp3-overlay-content.bp3-overlay-enter-done > div > div.bp3-dialog.atx-dialog._1ydevlj2oOiyYgwpjV-YQZ.css-1lz4uyl > div > div.advance-dialog-footer._131YhmYtWVPNjmPxq8T1WB > button.bp3-button.bp3-minimal.atx-button.atx-button--raised.atx-button-secondary > span")
                close_button.click()
                self.myStr.set("登陆成功")
                driver.find_element_by_css_selector(
                    "body > div.bp3-portal > div > div._31ajromK3XvJ7oOYpi4M1J.bp3-overlay-content.bp3-overlay-enter-done > div > div.custom-swiper-control > div.custom-swiper-control__action.custom-swiper-control__action--right").click()
                driver.find_element_by_css_selector(
                    "body > div.bp3-portal > div > div._31ajromK3XvJ7oOYpi4M1J.bp3-overlay-content.bp3-overlay-enter-done > div > div.custom-swiper-control > div.custom-swiper-control__action.custom-swiper-control__action--right").click()

                driver.find_element_by_css_selector(
                    "body > div.bp3-portal > div > div._31ajromK3XvJ7oOYpi4M1J.bp3-overlay-content.bp3-overlay-enter-done > div > div.swiper-container.swiper-container-initialized.swiper-container-horizontal.swiper-container-pointer-events > div.swiper-wrapper > div.swiper-slide.swiper-slide-active > div > div._-3jkSXRG9I4shaOd6H1v > div > a:nth-child(1)").click()

                layer_frist = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div[1]/div/div[2]/div[1]')
                layer_frist.click()

                time.sleep(2)
                driver.save_screenshot("screenshot01.png")
                # print(driver.page_source)

                # daily_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[2]/div/div[2]")
                driver.find_elements_by_css_selector("body > div.bp3-portal")
                daily_button = driver.find_element_by_css_selector(
                    "body > div.bp3-portal > div > div > div > div > div > div._1PGk-m9ck6DowacnraCWLP > div > div:nth-child(2)")

                daily_button.click()

                # print("跳转到填写页面")

                time.sleep(3)
                self.myStr.set("开始填写内")

                item_input = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[7]/div[2]/div/span/span/div/div[1]/div/input')
                item_input.click()
                item_input.send_keys(TestData_Get['workitem'])
                ActionChains(driver).send_keys(Keys.ENTER).perform()
                time.sleep(2)
                driver.save_screenshot("screenshot01.png")

                item_progess = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]')
                item_progess.click()
                time.sleep(2)

                # item_progess.send_keys("d")
                ActionChains(driver).double_click(item_progess).perform()
                time.sleep(2)
                ActionChains(driver).send_keys(Keys.ENTER).perform()
                driver.save_screenshot("screenshot02.png")

                time_len = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[8]')

                time_len.click()
                time.sleep(2)
                time_len.send_keys("8")
                driver.save_screenshot("screenshot03.png")

                work_info = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[9]')
                work_info.click()

                work_info.send_keys(TestData_Get['workdaily'])

                # work_info.send_keys("这次会成功吗")

                time.sleep(5)
                driver.save_screenshot("screenshot04.png")

                # driver.save_screenshot("screenshot03.png")

                submit = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/main/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[3]/div/div[2]/span[2]/span/button/span')
                submit.click()
                time.sleep(10)
                self.myStr.set("%s已提交" % time.ctime())
                driver.save_screenshot("screenshot05.png")
                self.myStr.set("检查是否提交成功")
                self.scroconsole.insert(
                    tkinter.constants.INSERT, "%s:已提交" % (time.ctime())+"\n")
                driver.quit()

                # driver.save_screenshot("screenshot.png"
            else:
                self.myStr.set("先填写所有信息")

        except Exception as e:

            self.scroconsole.insert(
                tkinter.constants.INSERT, "%s:运行发生错误,请手动运行一次%s%s" % (time.ctime(), "\n", e)+"\n")



if __name__ == "__main__":
    # RunClass = Autotoreport()

    FL = Autotoreport()
    FL.layout_arr()
    
    def job1():
        try:
            thread_it(FL.start_submit())
        except Exception as e:
            print(e)
            
    scheduler.add_job(job1, trigger=CronTrigger(hour=int(TestData_Get['duration']),minute="0",day_of_week='mon-fri'))
    try:
    
        scheduler.start()
        while True:
            
            print("start")
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("定时没有启动")
        scheduler.shutdown()
        
    tkinter.mainloop()
        
