import wx
import os
import sys
import glob
import serial

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class MyFrame(wx.Frame):
    serialport = ""
    usedSerialPort = ""
    ser = serial.Serial()
    def __init__(self):   
    
        super().__init__(parent=None, title='CNC Controller', size =(410, 450))
        panel = wx.Panel(self)        
        here = os.path.abspath(os.path.dirname(__file__))
        
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(os.path.join(here, "resources", "icon", "icon.ico"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        # Combobox for serial port options
        self.Combobox = wx.ComboBox(panel, choices = serial_ports(), pos = (1, 1));
        self.Combobox.Bind(wx.EVT_COMBOBOX, self.onCombo)

        # Connect Button
        self.ConnectBtn = wx.Button(panel, -1,  label="CONNECT" , pos=(1, 30))
        self.ConnectBtn.Bind(wx.EVT_BUTTON, self.onButtonSerialConnect)

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
            if self.ser.is_open:
                strStepsXDir1 = "Moving " + (str(self.stepsXDir1.GetValue())) + " steps in axis X dir 1"
                self.ser.write(b'X1' + str(self.stepsXDir1.GetValue()).encode())
                wx.MessageBox(strStepsXDir1)
        else:
            wx.MessageBox("Steps input must be a digit")

    def onButtonXDir2(self, event):
        if str(self.stepsXDir2.GetValue()).isdigit():
            if self.ser.is_open:
                strStepsXDir2 = "Moving " + (str(self.stepsXDir2.GetValue())) + " steps in axis X dir 2"
                self.ser.write(b'X2' + str(self.stepsXDir2.GetValue()).encode())
                wx.MessageBox(strStepsXDir2)
        else:
            wx.MessageBox("Steps input must be a digit")

    def onButtonYDir1(self, event):
        if str(self.stepsYDir1.GetValue()).isdigit():
            if self.ser.is_open:
                strStepsYDir1 = "Moving " + (str(self.stepsYDir1.GetValue())) + " steps in axis Y dir 1"
                self.ser.write(b'Y1' + str(self.stepsYDir1.GetValue()).encode())
                wx.MessageBox(strStepsYDir1)
        else:
            wx.MessageBox("Steps input must be a digit")

    def onButtonYDir2(self, event):
        if str(self.stepsYDir2.GetValue()).isdigit():
            if self.ser.is_open:
                strStepsYDir2 = "Moving " + (str(self.stepsYDir2.GetValue())) + " steps in axis Y dir 2"
                self.ser.write(b'Y2' + str(self.stepsYDir2.GetValue()).encode())
                wx.MessageBox(strStepsYDir2)
        else:
            wx.MessageBox("Steps input must be a digit")

    def onCombo(self, event):
        comboValue = self.Combobox.GetValue()
        self.serialport = comboValue
        
    def onButtonSerialConnect(self, event):
        if self.ConnectBtn.GetLabel() == "CONNECT":
            if self.serialport != "":
                if self.ser.is_open == False:
                    self.ser.baudrate = 9600
                    self.ser.port = self.serialport
                    self.ser.open()
                    if (self.ser.is_open):
                        wx.MessageBox("Connection to serial port " + self.serialport + " established")
                        self.usedSerialPort = self.serialport
                        self.ConnectBtn.SetLabel("DISCONNECT")
                    else:
                        wx.MessageBox("Could not connect to serial port " + self.serialport)
                else:
                    wx.MessageBox("The port is busy")                
            else:
                wx.MessageBox("Please select a port")
        else:
            self.ser.close()
            if (self.ser.is_open == True):
                wx.MessageBox("Could not disconnect serial port " + self.usedSerialPort)
            else:
                wx.MessageBox("Serial port " + self.usedSerialPort + " is disconnected")
                self.ConnectBtn.SetLabel("CONNECT")

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
