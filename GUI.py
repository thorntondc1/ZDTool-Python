import wx
import re
from datetime import date

class TicketCountFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="ZDTool", pos=(100,150), size=(800,500), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        
        #setting up panel and static text
        self.panel = wx.Panel(self)
        self.text = wx.StaticText(self.panel, label = "Enter Tickets:", pos = (10,50))
        font = self.text.GetFont()
        font.PointSize = 12
        font = font.Bold()
        self.text.SetFont(font)
    

        #setting up buttons
        self.button1 = wx.Button(self.panel, label = "Convert", pos = (150,350), size= (70,30))
        self.button2 = wx.Button(self.panel, label = "Clear", pos = (300,350), size=(70,30))
        
        #user text setup
        self.tickets = wx.TextCtrl(self.panel, pos = (120,50), size=(350,300),
            style = wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.BORDER_NONE)
        
        

        #bind tasks to buttons 
        self.button1.Bind(wx.EVT_BUTTON, self.Convert)
        self.button2.Bind(wx.EVT_BUTTON, self.ClearText)

        #create a menu and status bar 
        self.MenuBar()

        self.CreateStatusBar()
        self.SetStatusText("Use this tool to strip ticket numbers from URLs!")

   
        #Giving menu bar items 
    def MenuBar(self):
        fileMenu = wx.Menu()
 
        exportItem = fileMenu.Append(-1, "&Export\tAlt-E",
                "Export text file with IDs")
        fileMenu.AppendSeparator()
        closeItem = fileMenu.Append(-1, "&Quit\tEsc","Quit the application")

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

 
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)


        #Giving buttons functionality 
        self.Bind(wx.EVT_MENU, self.CloseApp, closeItem)
        self.Bind(wx.EVT_MENU, self.About, aboutItem)
        self.Bind(wx.EVT_MENU, self.Export, exportItem)

        
        #Closes app
    def CloseApp(self,event):
        self.Close(True)    


        #Pulls ticket numbers from URLs, if there is no URL and just a number, it should pull that and place it into a string that is a list. 
    def Convert(self, event):
        url = self.tickets.GetValue()
        id1 = re.findall("\d+",url)
        self.tickets.SetValue(','.join(id1))


            
        #clears user input or output for more URLs. 
    def ClearText(self, event):
        self.tickets.SetValue("")

    def About(self,event):
        wx.MessageBox("Use this to pull ticket numbers from ticket URLs. Export function should create a text file.",
                        "About ZDTOOL - Python",
                        wx.OK|wx.ICON_INFORMATION)


    def Export(self,event):
        if self.tickets.GetValue() != "":
            file = open("ZDTOOL Exports.txt","a")
            today = date.today()
            file.write(today.strftime("%b-%d-%Y:  \n "))
            file.write("{} \n".format(self.tickets.GetValue()))
            file.write('\n')
            file.close()
        else: 
            wx.MessageBox("Ticket field is empty. Please paste and convert tickets to export.","ZDTOOL Export",
                            wx.OK|wx.ICON_INFORMATION)

    
        

app = wx.App(False)
frame = TicketCountFrame()
frame.Show()
app.MainLoop()


        
