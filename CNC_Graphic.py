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
        here = os.path.abspath(os.path.dirname(__file__))
        
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(os.path.join(here, "resources", "icon", "icon.ico"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        # Input Steps to move in axis X direction 1
        self.stepsXDir1 = wx.TextCtrl(panel, pos=(5, 125)) 
        
        # Button Execute steps move in axis X direction 1
        pic = wx.Bitmap(os.path.join(here, "resources", "arrows", "arrow-left.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnXDir1 = wx.BitmapButton(panel, -1, pic, pos=(5, 160))
        self.btnXDir1.Bind(wx.EVT_BUTTON, self.onButtonXDir1)
        
        # Input Steps to move in axis X direction 2
        self.stepsXDir2 = wx.TextCtrl(panel, pos=(275, 125))
        
        # Button Execute steps move in axis X direction 2
        pic = wx.Bitmap(os.path.join(here, "resources", "arrows", "arrow-right.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnXDir2 = wx.BitmapButton(panel, -1, pic, pos=(275, 160))
        self.btnXDir2.Bind(wx.EVT_BUTTON, self.onButtonXDir2)
        
        # Input Steps to move in axis Y direction 1
        self.stepsYDir1 = wx.TextCtrl(panel, pos=(140, 5))
        
        # Button Execute steps move in axis Y direction 1
        pic = wx.Bitmap(os.path.join(here, "resources", "arrows", "arrow-up.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnYDir1 = wx.BitmapButton(panel, -1, pic, pos=(140, 40))
        self.btnYDir1.Bind(wx.EVT_BUTTON, self.onButtonYDir1)
        
        
        # Input Steps to move in axis Y direction 2
        self.stepsYDir2 = wx.TextCtrl(panel, pos=(140, 260))
        
        # Button Execute steps move in axis Y direction 2
        pic = wx.Bitmap(os.path.join(here, "resources", "arrows", "arrow-down.png"), wx.BITMAP_TYPE_PNG)
        pic = scale_bitmap(pic, 103, 103)
        self.btnYDir2 = wx.BitmapButton(panel, -1, pic, pos=(140, 295))
        self.btnYDir2.Bind(wx.EVT_BUTTON, self.onButtonYDir2)
                
        self.Show()
        
    def onButtonXDir1(self, event):
        if str(self.stepsXDir1.GetValue()).isdigit():
            stepsXDir1 = "Moving " + (str(self.stepsXDir1.GetValue())) + " steps in axis X dir 1"
            wx.MessageBox(stepsXDir1)
        else:
            wx.MessageBox("Steps input must be a digit")

    def onButtonXDir2(self, event):
        if str(self.stepsXDir2.GetValue()).isdigit():
            stepsXDir2 = "Moving " + (str(self.stepsXDir2.GetValue())) + " steps in axis X dir 2"
            wx.MessageBox(stepsXDir2)
        else:
            wx.MessageBox("Steps input must be a digit")

    def onButtonYDir1(self, event):
        if str(self.stepsYDir1.GetValue()).isdigit():
            stepsYDir1 = "Moving " + (str(self.stepsYDir1.GetValue())) + " steps in axis Y dir 1"
            wx.MessageBox(stepsYDir1)
        else:
            wx.MessageBox("Steps input must be a digit")

    def onButtonYDir2(self, event):
        if str(self.stepsYDir2.GetValue()).isdigit():
            stepsYDir2 = "Moving " + (str(self.stepsYDir2.GetValue())) + " steps in axis Y dir 2"
            wx.MessageBox(stepsYDir2)
        else:
            wx.MessageBox("Steps input must be a digit")

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()