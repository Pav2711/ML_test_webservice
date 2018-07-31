#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from Tkinter import *
import urllib2
import json 

data =  {
        "Inputs": {
                "input1":
                {
                    "ColumnNames": ["p01", "p02", "p03", "p04", "p05", "p06", "p07", "p08", "p09", "p10", "p11", "p12", "p13", "p14", "p15", "p16", "p17", "p18", "p19", "p20", "p21", "p22", "p23", "p24", "p25", "p26", "p27", "p28", "p29", "p30", "p31", "p32", "p33", "p34", "p35", "p36", "p37", "p38", "p39", "p40", "p41", "p42", "p43", "p44", "p45", "p46", "p47", "p48", "p49", "p50", "p51", "p52", "p53", "p54", "p55", "p56", "p57", "p58", "p59", "p60", "p61", "p62", "p63", "p64", "digit"],
                    "Values":    [ [ "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], [ "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

class Example(Canvas):
    def change_rect(self, event):
        self.itemconfigure(CURRENT, fill='green')
        
    def change_reset(self, event):    
        self.itemconfigure(CURRENT, fill='white')
            
    def clear_rec(self):
        for k in range(1, 65):
            self.itemconfigure(k, fill='white')
        self.lab2["text"] = ""
       
    def submit(self):
        self.arr = []
        for k in range(1, 65):
            if self.itemcget(k, 'fill' ) == "green": 
                self.arr.append("15")
            else:
                self.arr.append("0")

        self.arr.append("0") #Field - digit
        data['Inputs']['input1']['Values'][0]  = self.arr
        data['Inputs']['input1']['Values'][1]  = self.arr
        body = str.encode(json.dumps(data))
        
# Replace url - url for your webservice
        
        url = 'https://europewest.services.azureml.net/workspaces/95b5351d65844c1c9b81a0797541d35a/services/ee48970c81504b4699189ba479421f23/execute?api-version=2.0&details=true'

# Replace api_key - key for your webservice

        api_key = 'BGWCMzeEn2DjN8TJpjA3d9/tN1XhSw4X5tHehdrmuhzDJ9JGeRpDT39a3gE/In8BHxTSTU+Yff/O7i7XgoFkXw==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
 
        req = urllib2.Request(url, body, headers) 

        try:
            response = urllib2.urlopen(req)

            # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
            # req = urllib.request.Request(url, body, headers) 
            # response = urllib.request.urlopen(req)

            result = response.read()
            
            s = json.loads(result) #Convert in dict
            ks = s['Results']['output1']['value']['Values'][0][75] #Read field - digit 
            self.lab2["text"]=ks
        except urllib2.HTTPError, error:
            ks = "The request failed - code: " + str(error.code)
         
        
    def __init__(self, parent):
        Canvas.__init__(self, parent, bg="White", width="4i", height=300, relief=SUNKEN)   
        self.parent = parent
        self.bind("<Button-1><Motion>", self.change_rect)
        self.bind("<Button-3><Motion>", self.change_reset)
        self.arr = []
        self.initUI()
    
    def initUI(self):
        self.parent.title("Simple")
        i = 1
        for k in range(8):
            for l in range(8):
                self.create_rectangle((l+1)*30,(k+1)*30,(l+1)*30+28,
                        (k+1)*30+28,fill="white",outline="red")
        self.clButton = Button(self, text="Clear", command = self.clear_rec)
        self.clButton.place(x=200, y=300)
        self.suButton1 = Button(self, text="Submit", command = self.submit)
        self.suButton1.place(x=250, y=300)
        self.lab1 = Label(text="Predict digit:", bg='white')
        self.lab1.place(x=10, y = 300)
        self.lab2 = Label(bg = 'white')
        self.lab2.place(x=80, y = 300)
        
        self.pack(fill=BOTH, expand=1)

def main():
    root = Tk()
    root.geometry("300x350+300+300")
    root.resizable(False, False)
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()
