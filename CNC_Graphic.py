import wx
import os

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

class MyFrame(wx.Frame):
    mstr = ""
    def __init__(self):   
    
        super().__init__(parent=None, title='CNC Controller', size =(410, 450))
        panel = wx.Panel(self)        
        
        # Input Steps to move in axis X direction 1
        self.stepsXDir1 = wx.TextCtrl(panel, pos=(5, 125)) 
        
        # Button Execute steps move in axis X direction 1
        here = os.path.abspath(os.path.dirname(__file__))
        pic = wx.Bitmap(os.path.join(here, "ressources", "arrows", "arrow-left.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnXDir1 = wx.BitmapButton(panel, -1, pic, pos=(5, 160))
        self.btnXDir1.Bind(wx.EVT_BUTTON, self.onButtonXDir1)
        
        # Input Steps to move in axis X direction 2
        self.stepsXDir2 = wx.TextCtrl(panel, pos=(275, 125))
        
        # Button Execute steps move in axis X direction 2
        pic = wx.Bitmap(os.path.join(here, "ressources", "arrows", "arrow-right.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnXDir2 = wx.BitmapButton(panel, -1, pic, pos=(275, 160))
        self.btnXDir2.Bind(wx.EVT_BUTTON, self.onButtonXDir2)
        
        # Input Steps to move in axis Y direction 1
        self.stepsYDir1 = wx.TextCtrl(panel, pos=(140, 5))
        
        # Button Execute steps move in axis Y direction 1
        pic = wx.Bitmap(os.path.join(here, "ressources", "arrows", "arrow-up.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnYDir1 = wx.BitmapButton(panel, -1, pic, pos=(140, 40))
        self.btnYDir1.Bind(wx.EVT_BUTTON, self.onButtonYDir1)
        
        
        # Input Steps to move in axis Y direction 2
        self.stepsYDir2 = wx.TextCtrl(panel, pos=(140, 260))
        
        # Button Execute steps move in axis Y direction 2
        pic = wx.Bitmap(os.path.join(here, "ressources", "arrows", "arrow-down.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnYDir2 = wx.BitmapButton(panel, -1, pic, pos=(140, 295))
        self.btnYDir2.Bind(wx.EVT_BUTTON, self.onButtonYDir2)
                
        self.Show()
        
    def onButtonXDir1(self, event):
        stepsXDir1 = (str(self.stepsXDir1.GetValue()))
        wx.MessageBox(stepsXDir1)

    def onButtonXDir2(self, event):
        stepsXDir2 = (str(self.stepsXDir2.GetValue()))
        wx.MessageBox(stepsXDir2)

    def onButtonYDir1(self, event):
        stepsYDir1 = (str(self.stepsYDir1.GetValue()))
        wx.MessageBox(stepsYDir1)

    def onButtonYDir2(self, event):
        stepsYDir2 = (str(self.stepsYDir2.GetValue()))
        wx.MessageBox(stepsYDir2)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()