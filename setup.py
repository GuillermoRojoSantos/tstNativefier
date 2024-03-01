from cx_Freeze import setup,Executable
import sys


setup(
    name="GestoLingo-test",
    version="0.1",
    description="A GestoLingo package test ONLY FOR DEVELOPEMENT DO NOT RELEASE",
    executables = [Executable("run.py",base=None)],
    options={
        "build_exe":{
            "include_files":["main.py"],
            "packages":["streamlit","cv2","mediapipe"]
        }
    }
)