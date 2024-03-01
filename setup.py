from cx_Freeze import setup,Executable
import sys

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="GestoLingo-test",
    version="0.1",
    description="A GestoLingo package test ONLY FOR DEVELOPEMENT DO NOT RELEASE",
    executables = [Executable("run.py",base=base)],
    options={
        "build_exe":{
            "include_files":["main.py"]
        }
    }
)