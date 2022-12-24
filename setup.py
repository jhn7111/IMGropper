from cx_Freeze import setup, Executable
base = "Win32GUI"
setup(
    name='IMGropper',
    version='0.1',
    author='jhn7111',
    description="It's a simple image cropper.",
    options={"build_exe": {"packages": ["PIL"]}},
    executables=[Executable('app.py', base=base)]
)