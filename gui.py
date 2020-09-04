import wx
import re

class TicketCountFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="ZDTool", pos=(100,150), size=(800,600))

        self.panel = wx.Panel(self)

        self.text = wx.StaticText(self.panel, label = "Enter Tickets:", pos = (10,150))
        font = self.text.GetFont()
        font.PointSize = 12
        font = font.Bold()
        self.text.SetFont(font)
        
        self.button1 = wx.Button(self.panel, label = "Convert", pos = (150,450), size= (70,30))
        self.button2 = wx.Button(self.panel, label = "Clear", pos = (300,450), size=(70,30))
        
        self.tickets = wx.TextCtrl(self.panel, pos = (120,150), size=(300,250),
            style = wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.BORDER_NONE)
        

        self.result = wx.StaticText(self.panel, pos = (500,200),
            style = wx.TE_READONLY|wx.TE_MULTILINE|wx.BORDER_NONE|wx.TE_NO_VSCROLL)
        #self.result.Wrap(30)
        font2 = self.result.GetFont()
        font2.PointSize = 10
        self.result.SetFont(font2)
        





        self.button1.Bind(wx.EVT_BUTTON, self.Convert)
        self.button2.Bind(wx.EVT_BUTTON, self.ClearText)

   



    def Convert(self, event):
        url = self.tickets.GetValue()
        id1 = re.findall("\d+",url)
        self.result.SetLabel(','.join(id1))

        

    def ClearText(self, event):
        self.result.SetLabel("")
        self.tickets.SetValue("")

    
        

app = wx.App(False)
frame = TicketCountFrame()
frame.Show()
app.MainLoop()


        
