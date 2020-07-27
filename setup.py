from cx_Freeze import setup, Executable

setup(
    name = "test",
    version = "0.1",
    description = "premier test",
    executables = [Executable("mainwindow.py")]
)