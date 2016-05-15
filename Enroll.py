# -*- coding: cp936 -*-
import wx

class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Enroll',
                size=(500, 300))
        panel = wx.Panel(self)


        panel.SetBackgroundColour("White")# huo dong xuan xiang
        prevButton = wx.Button(panel, -1, "Enroll", pos=(80, 10))
        self.Bind(wx.EVT_BUTTON, self.OnPrev, prevButton)
        nextButton = wx.Button(panel, -1, "Sign In", pos=(200, 10))
        self.Bind(wx.EVT_BUTTON, self.OnNext, nextButton)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        menuBar = wx.MenuBar()#cai dan lan she ding
        menu1 = wx.Menu()
        openMenuItem = menu1.Append(-1, "&Open", "Copy in status bar")
        self.Bind(wx.EVT_MENU, self.OnOpen, openMenuItem)
        quitMenuItem = menu1.Append(-1, "&Quit", "Quit")
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, quitMenuItem)
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        copyItem = menu2.Append(-1, "&Copy", "Copy")
        self.Bind(wx.EVT_MENU, self.OnCopy, copyItem)
        cutItem = menu2.Append(-1, "C&ut", "Cut")
        self.Bind(wx.EVT_MENU, self.OnCut, cutItem)
        pasteItem = menu2.Append(-1, "Paste", "Paste")
        self.Bind(wx.EVT_MENU, self.OnPaste, pasteItem)
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)

        
        
        panel.SetBackgroundColour("White")# xin xi shou lu lan
        Enroll = wx.Button(panel, label="Enroll", pos=(300, 200),
                size=(50, 30))
        Delete = wx.Button(panel, label="Delete", pos=(370, 200),
                size=(50, 30))

        static0 = wx.StaticText(panel, wx.NewId(), "SWJTU ROBOT CLUB",
                pos=(200, 40))

        static1 = wx.StaticText(panel, wx.NewId(), "  Active:",
                pos=(15, 70))
        #static.SetBackgroundColour("White")
        text1 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 70))

        static2 = wx.StaticText(panel, wx.NewId(), "      Time:",
                pos=(200, 70))
        #static.SetBackgroundColour("White")
        text2 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(270, 70))
        
        static3 = wx.StaticText(panel, wx.NewId(), "      Name:",
                pos=(10, 100))
        #static.SetBackgroundColour("White")
        text3 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 100))
                
        static4 = wx.StaticText(panel, wx.NewId(), "          ID:",
                pos=(10, 130))
        #static2.SetBackgroundColour("White")
        text4 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 130))
                
        static5 = wx.StaticText(panel, wx.NewId(), "Department: ",
                pos=(10, 160))
        #static3.SetBackgroundColour("White")
        text5 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 160))

        static6 = wx.StaticText(panel, wx.NewId(), "Card ID： ",#这里读取卡的序列号
                pos=(220, 160))
        
        response1 = text1.GetValue()#活动名称
        response2 = text2.GetValue()#活动时间
        response3 = text3.GetValue()#姓名
        response4 = text4.GetValue()#学号
        response5 = text5.GetValue()#部门
       # self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
       # self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(True)
    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass
    def OnFirst(self, event): pass
    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnCut(self, event): pass
    def OnPaste(self, event): pass
    def OnOptions(self, event): pass



    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
