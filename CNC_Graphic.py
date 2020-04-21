import wx

def onButton(event):
    print("Button pressed.")


class MyFrame(wx.Frame):    
    def __init__(self):
        
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)
        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn1 = wx.Button(panel, label='Send Message1', pos=(5, 55))
        my_btn1.Bind(wx.EVT_BUTTON, onButton)
        #wx.MessageBox( "This is a message.", "Button pressed.")
        
        self.text_ctrl = wx.TextCtrl(panel, pos=(260, 5))
        my_btn2 = wx.Button(panel, label='Send Message2', pos=(260, 55))
        my_btn2.Bind(wx.EVT_BUTTON, onButton)
        
        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 260))
        my_btn3 = wx.Button(panel, label='Send Message3', pos=(5, 315))
        my_btn3.Bind(wx.EVT_BUTTON, onButton)
        
        
        self.text_ctrl = wx.TextCtrl(panel, pos=(260, 260))
        my_btn4 = wx.Button(panel, label='Send Message4', pos=(260, 315))
        my_btn4.Bind(wx.EVT_BUTTON, onButton)
        
        
       
        
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()