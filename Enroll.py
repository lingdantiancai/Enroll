
import wx

class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Enroll',
                size=(500, 300))
        panel = wx.Panel(self)
        
        Enroll = wx.Button(panel, label="Enroll", pos=(300, 200),
                size=(50, 30))
        Delete = wx.Button(panel, label="Delete", pos=(370, 200),
                size=(50, 30))
        
        static1 = wx.StaticText(panel, wx.NewId(), "  Active",
                pos=(15, 20))
        #static.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 20))

        static2 = wx.StaticText(panel, wx.NewId(), "      Time:",
                pos=(200, 20))
        #static.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(270, 20))
        
        static3 = wx.StaticText(panel, wx.NewId(), "      Name:",
                pos=(10, 70))
        #static.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 70))
                
        static4 = wx.StaticText(panel, wx.NewId(), "          ID:",
                pos=(10, 100))
        #static2.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 100))
                
        static5 = wx.StaticText(panel, wx.NewId(), "Department:",
                pos=(10, 130))
        #static3.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 130))
       # self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
       # self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
