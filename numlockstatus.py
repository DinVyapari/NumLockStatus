from time import sleep
from infi.systray import SysTrayIcon
from ctypes import WinDLL
hllDll = WinDLL("User32.dll")
status=hllDll.GetKeyState(0x90)
if status:
    systray = SysTrayIcon("yes.ico", "Num Lock is ON", None)
    systray.start()
else:
    systray = SysTrayIcon("no.ico", "Num Lock is OFF", None)
    systray.start()
while True:
    stchk=hllDll.GetKeyState(0x90)
    if stchk:
        systray.update(icon="yes.ico")
        systray.update(hover_text="Num Lock is ON")
    else:
        systray.update(icon="no.ico")
        systray.update(hover_text="Num Lock is OFF")
    sleep(1)