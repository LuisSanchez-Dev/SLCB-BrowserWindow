import clr
from os. path import join, dirname, realpath

ScriptName  = "Browser Window"
Website     = "https://www.fiverr.com/luissanchezdev"
Description = "Display a website."
Creator     = "LuisSanchezDev"
Version     = "1.0"

def ScriptToggled(state)    : pass
def Init()                  : pass
def Execute(data)           : pass
def ReloadSettings(jsonData): pass
def Unload()                : pass
def Tick()                  : pass

def OpenReadMe():
  readmeFile = join(dirname(realpath(__file__)),'ReadMe.html')
  readme = BrowserWindow(readmeFile ,readmeFile)
  readme.Show()

class BrowserWindow:
  def __init__(self, title, url):
    clr.AddReferenceByPartialName("PresentationFramework")
    clr.AddReferenceByPartialName("PresentationCore")
    clr.AddReferenceToFile('CefSharp.Wpf.dll')
    import System.Windows
    from CefSharp.Wpf import ChromiumWebBrowser
    self.form  = System.Windows.Window()
    browser = ChromiumWebBrowser()
    browser.Address = url
    self.form.Content = browser
    self.form.Title = title
  
  def Show(self):
    self.form.Show()
