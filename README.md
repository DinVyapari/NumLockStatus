# NumLockStatus

Shows whether number lock is enabled or not using an icon in the system tray. Status is updated every second. Very useful for devices that do not have number lock status indicator lights.

## Instructions:

1. Ensure that you have Python 3 installed on your Windows system.
2. Install the infi.systray module.
```
pip install infi.systray
```
3. Clone the repository on your PC.
4. Edit Run.bat and update it with your Python installation directory and the directory where you have saved the repository. **Ensure that your path points to pythonw.exe and not python.exe.**
5. Create a shortcut for run.bat and save it in your startup directory. This will execute the program automatically on startup. <br>
**(C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup)**
6. Run the program. Unhide the status indicator icon by dragging it out of the system tray. It will unhide automatically from the next run.

## To Do:

- [ ] Compile to .exe
- [ ] Create Linux version
