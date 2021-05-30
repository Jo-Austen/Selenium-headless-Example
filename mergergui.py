import tkinter
from selenium import webdriver
from tkinter.scrolledtext import ScrolledText
import pandas as pd
import time
import tkinter.messagebox
# from mailmerge import MailMerge

class Autotoreport(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Web Performance By GoogleDevTools")
        width,height = 960,800
        screenwidth,screenheight = self.root.winfo_screenwidth(),self.root.winfo_screenheight()
        self.size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
        self.root.geometry(self.size)
        self.myStr = tkinter.StringVar()
        self.myStr.set("Plase Input Topic's URL")
        self.label = tkinter.Label(self.root,textvariable=self.myStr,bg='white',width = 60,height = 1)
        #URL TEXTBOX:
        self.test_url = tkinter.LabelFrame(self.root,width=460,height=120,text="Page's Url")
        self.page_url = tkinter.Entry(self.test_url,width = 60,relief='solid')
        #REQUEST URL:
        self.rqment_url = tkinter.LabelFrame(self.root,width=160,height=238,text='Requement_info')
        self.text_url = tkinter.Entry(self.rqment_url,relief='solid')
        self.button1 = tkinter.Button(self.rqment_url,text="RESET_URL",command="")
        self.button2 = tkinter.Button(self.rqment_url,text='PRINT',command="")
        self.textbox = tkinter.Text(self.rqment_url,width=20,height=10,relief='solid')
        #CHOSE PLATFORM:
        self.platform = tkinter.LabelFrame(self.root,width=96,height=96,text='platfrom')
        self.varRadio = tkinter.StringVar()
        self.platform1 = tkinter.Radiobutton(self.platform,text='APP',value = '天天基金APP',variable=self.varRadio,command=self.radiobutton_click)
        self.platform2 = tkinter.Radiobutton(self.platform,text='WEB',value = '天天基金WEB',variable=self.varRadio,command=self.radiobutton_click)
        #CHECK TESTER:
        self.tester = tkinter.LabelFrame(self.root,width=96,height=96,text='Tester')
        self.varCheck1 = tkinter.IntVar()
        self.varCheck2 = tkinter.IntVar()
        self.checkbutton1 = tkinter.Checkbutton(self.tester,text='Zhou',variable=self.varCheck1,onvalue=1,offvalue=0,command=self.checkbutton_click)
        self.checkbutton2 = tkinter.Checkbutton(self.tester,text='Zhang',variable=self.varCheck2,onvalue=1,offvalue=0,command=self.checkbutton_click)
        #GET PAGEINFO：
        self.MenuButton = tkinter.LabelFrame(self.root,width=96,height=96,text='GetInfo')
        self.button3 = tkinter.Button(self.MenuButton,text='GET',width=10,height=3,command=self.getpageinfo)
        #CONF:
        self.Listbox = tkinter.LabelFrame(self.root,width=260,height=240,text='Info')
        self.listbox = tkinter.Text(self.Listbox,height=16,width=20)
        self.button4 = tkinter.Button(self.Listbox,text="Return",height=2,command="")
        #SCROLLED：
        self.scrotext = tkinter.LabelFrame(self.root,width=935,height=410,text='Console')
        self.scroconsole = ScrolledText(self.scrotext,width=900,height=380)
        #Develope:
        # self.Develope = tkinter.LabelFrame(self.root,width=300,height=96,text='DevelopeMan')
         #START BUTTON:LableFrame and BUtton
        self.start_button = tkinter.LabelFrame(self.root,width =96,height =96,text='Write2Word')
        self.s_button = tkinter.Button(self.start_button,text='MAIN_START',width=10,height=3,command=self.Write2word)
        




    def layout_arr(self):
        self.label.grid(row=0,column=0,columnspan=6)
        #startbutton:
        self.start_button.grid(row=1,column = 0,sticky = 'w',padx = 10)
        self.s_button.place(x=6,y=1)
        #pagetesturl inputtextbox:
        self.test_url.grid(row=2,column=0,sticky='w',padx=10,columnspan=4)
        self.page_url.place(x=12,y=40)
        #requstmentinfo:
        self.rqment_url.grid(row=1, column=4, rowspan=2, padx = 6,  sticky='w')
        self.text_url.place(x=6,y=1)
        self.button1.place(x=6,y=32)
        self.button2.place(x=85,y=32)
        self.textbox.place(x=6,y=72)
        #choseplatform:
        self.platform.grid(row=1,column=2,sticky='w')
        self.platform1.place(x=6,y=0)
        self.platform2.place(x=6,y=30)
        #checktest:
        self.tester.grid(row=1,column=1,sticky='w')
        self.checkbutton1.place(x=6,y=0)
        self.checkbutton2.place(x=6,y=30)
        #onlygetpageinfo：
        self.MenuButton.grid(row=1, column=3, sticky='w')
        self.button3.place(x=6,y=2)
        #Listbox for all：
        self.Listbox.grid(row=1, column=5, rowspan=2,  sticky='w')
        self.listbox.place(x=6,y=1)
        self.button4.place(x=164,y=30)
        #end:
        self.scrotext.grid(row=4, column=0, columnspan=6, padx=10, sticky='w')
        self.scroconsole.place(x=6,y=2)
        #developeman:
        # self.Develope.grid(row=3, column=0, padx=10,sticky='w')
        # self.dename.place(x=6,y=2)
    def radiobutton_click(self):
        self.myStr.set('You have selected ' +self.varRadio.get())
        self.scroconsole.insert(tkinter.constants.INSERT,"check platform:%s"%(self.varRadio.get())+"\n")
    
    
    
    def checkbutton_click(self):
        test1,test2="Zhou","Zhang"
        if (self.varCheck1.get()==1) & (self.varCheck2.get()==1):
            self.myStr.set("ALL CHECK")
            self.scroconsole.insert(tkinter.constants.INSERT,"ALL CHECKED"+"\n")
        elif (self.varCheck1.get()==1) & (self.varCheck2.get()==0):
            self.myStr.set("CHECK:%s"%(test1))
            self.scroconsole.insert(tkinter.constants.INSERT,"check Tester:%s"%(test1)+"\n")
        elif (self.varCheck1.get()==0) & (self.varCheck2.get()==1):
            self.myStr.set("CHECK:%s"%(test2))
            self.scroconsole.insert(tkinter.constants.INSERT,"check Tester:%s"%(test2)+"\n")
        else:
            self.myStr.set("No Checked")
            self.scroconsole.insert(tkinter.constants.INSERT,"No Chose"+"\n")


    def getpageinfo(self):
        if not self.page_url.get():
            # tkinter.messagebox.showinfo(title='Error:Something null', message='Plase Input Your Testpage(url)')
            self.myStr.set("Error:Something null[page_url]")
            
        else:
            self.url = self.page_url.get()
            driver=webdriver.Chrome()
            driver.get(self.url)
            time.sleep(5)
            performance_data = driver.execute_script("return window.performance.getEntries();")
            keys_values = [keys for keys,values in performance_data[0].items()]
            df_page = pd.DataFrame(performance_data,columns = keys_values)
            pd.set_option("max_colwidth",10)
            from collections import Counter
            #Counts:
            kinds_initiatorType = Counter(df_page["initiatorType"])
            # print(kinds_initiatorType["img"]) #Counts type(img)
            page_counts = df_page.shape[0]
            if int(kinds_initiatorType["img"]) >= int(kinds_initiatorType["css"]):
                img_counts = kinds_initiatorType["img"]
                df_sortimg = df_page[df_page.initiatorType == "img"]
            else:
                img_counts = kinds_initiatorType["css"]
                df_sortimg = df_page[df_page.initiatorType == "css"]
            css_counts = kinds_initiatorType["link"]
            js_counts = kinds_initiatorType["script"]
            df_sortcss = df_page[df_page.initiatorType == "link"]
            df_sortjs = df_page[df_page.initiatorType == "script"]
            page_sizelist = [i for i in df_page["encodedBodySize"] if i >= 0]
            
            print(page_sizelist)
            page_size = sum(page_sizelist)/1024
            img_size = sum(df_sortimg["encodedBodySize"])/1024
            css_size = sum(df_sortcss["encodedBodySize"])/1024
            js_size = sum(df_sortjs["encodedBodySize"])/1024
            print("page_size:%s||img_size:%s||css_size:%s||js_size:%s"%(page_size,img_size,css_size,js_size))
            #TimeLine:
            navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            responseEnd = driver.execute_script("return window.performance.timing.responseEnd")
            # domComplete = driver.execute_script("return window.performance.timing.domComplete")
            loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")

            backendPerformance = float(responseEnd-navigationStart)
            # domperformance = float(domComplete-responseEnd)
            frontendPerformance = float(loadEventEnd-responseEnd)
            FinisheTime = float(backendPerformance+frontendPerformance)

            #title:
            page_title = driver.title

            #report:
            report_columns = ["page_title","url","page_counts","page_size[KB]","js_counts","js_size[KB]","css_counts","css_size[KB]","frontendPerformance[MS]","FinisheTime[MS]","img_counts","img_size[KB]"]
            report_data = [{"page_title":page_title,"url":self.url,"page_counts":page_counts,"page_size[KB]":page_size,"js_counts":js_counts,"js_size[KB]":js_size,"css_counts":css_counts,"css_size[KB]":css_size,"frontendPerformance[S]":frontendPerformance,"FinisheTime[S]":FinisheTime,"img_counts":img_counts,"img_size[KB]":img_size}]
            df_testreport = pd.DataFrame(report_data,columns = report_columns)
            df_testreport.set_index("page_title",inplace=True)
            from prettytable import PrettyTable
            x = PrettyTable(report_columns)
            y = PrettyTable(["页面标题","页面链接","请求资源个数","页面大小[KB]","JS_数量","JS_大小[KB]","CSS_数量","CSS_大小[KB]","响应时间[ms]","加载完成时间[ms]","图片资源数量[Neteork]","图片资源大小[KB]"])
            report_dict = {"page_title":page_title,"url":self.url,"page_counts":page_counts,"page_size[KB]":page_size,"js_counts":js_counts,"js_size[KB]":js_size,"css_counts":css_counts,"css_size[KB]":css_size,"frontendPerformance[S]":frontendPerformance,"FinisheTime[S]":FinisheTime,"img_counts":img_counts,"img_size[KB]":img_size}
            loop_list = [values for keys,values in report_dict.items()]
            x.add_row(loop_list)
            y.add_row(loop_list)
            self.scroconsole.insert(tkinter.constants.END,report_dict)
            driver.close()
            self.myStr.set("Getpageinfo Success")
            return df_testreport
    def Write2word(self):
        if not self.text_url.get():
            self.myStr.set("Error:Something null[Requestment_info]")
        elif not self.varRadio.get():
            self.myStr.set("Error:Something null[Platform]")
        elif not (self.varCheck1.get()==1 or self.varCheck2.get()==1):
            self.myStr.set("Error:Something null[Tester]")
        else:
            self.myStr.set("Start")
            self.scroconsole.insert(tkinter.constants.END, self.listbox.get('0.0', 'end'))
            list_info = [list_x for list_x in self.listbox.get('0.0', 'end').split('\n')]
            self.scroconsole.insert(tkinter.constants.END, list_info[0]+"\n")
            # Page_info = self.getpageinfo()
            template = r"C:\Users\123\Desktop\template.docx"
            document = MailMerge(template)
            document.merge(
                RequestMan = list_info[4],
                Pageinfo = self.textbox.get('0.0','end'),
                Title = list_info[0],
                DevelopMan = list_info[1],
                TestMan = "李飞,周鹏阳",
                DateTest = list_info[2],
                DateDevelop = list_info[3],
                Requestment_url = self.text_url.get(),
                Test_url = self.page_url.get(),
                Typeof = self.varRadio.get(),

            )
            document.write("C:\\Users\\123\\Desktop\\%s.docx"%(list_info[0]))
            self.scroconsole.insert(tkinter.constants.END, "take success")



def main():
    FL = Autotoreport()
    FL.layout_arr()
    tkinter.mainloop()
if __name__ == "__main__":
    main()


