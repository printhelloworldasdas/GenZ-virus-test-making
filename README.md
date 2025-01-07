This is a virus that im making whit python when i can i will make it a .exe so i hope u like my virus for the moment is in beta
C:\Users\Cristian\Downloads\GenZ virus>python GenZ.py
Exception in thread Thread-2 (upside_down_effect):
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.496.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.496.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Cristian\Downloads\GenZ virus\GenZ.py", line 55, in upside_down_effect
    root.attributes("-fullscreen", True)  # Pantalla completa
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.496.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 2160, in wm_attributes
    return self.tk.call('wm', 'attributes', self._w, *args)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_tkinter.TclError: can't set fullscreen attribute for ".": override-redirect flag is set
