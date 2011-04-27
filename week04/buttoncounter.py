import wx
import string
import sys

class ButtonCounter(wx.Frame):

    def __init__(self, parent, n_buttons, title):
        WIDTH = 75
        TEXT_HEIGHT = 30
        TEXT_SIZE = (WIDTH, TEXT_HEIGHT)
        BUTTON_HEIGHT = 50
        BUTTON_SIZE = (WIDTH, BUTTON_HEIGHT)
        MARGIN = 10
        LABELS = string.uppercase # 'ABC...'

        wx.Frame.__init__(self, parent, title=title,
                          size=(n_buttons*(MARGIN + WIDTH) + MARGIN, 
                                TEXT_HEIGHT + BUTTON_HEIGHT + 3*MARGIN))
        self.count = dict()
        self.text= dict()
        self.button = dict()
        for index, label in enumerate(LABELS[:n_buttons]):
            self.count[index] = 0
            pos_x = index*(MARGIN + WIDTH) + MARGIN
            self.text[index] = wx.StaticText(self, size=TEXT_SIZE,
                                             pos=(pos_x + WIDTH/2, MARGIN), 
                                             label=('%s' % self.count[index]))
            self.button[index] = wx.Button(self, id=index, label=label,
                                           size=BUTTON_SIZE,
                                           pos=(pos_x, TEXT_HEIGHT + MARGIN))
        self.Bind(wx.EVT_BUTTON, self.OnButton) # OnButton finds which button
        self.Show(True)

    # Event handler
    def OnButton(self, event):
        index = event.GetId()  # which button?
        self.count[index] += 1
        self.text[index].SetLabel('%s' % self.count[index])

n_buttons = 1
if len(sys.argv) > 1:
    try:
        n_buttons = int(sys.argv[1])
    except ValueError:
        pass
app = wx.App(False)
frame = ButtonCounter(None, n_buttons, '%s Buttons' % str(n_buttons))
app.MainLoop()
