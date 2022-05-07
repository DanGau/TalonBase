os: windows
app: Microsoft Visual Studio 2019
app: devenv.exe
-
param linebreak:
    user.select_next_occurrence(',')
    sleep(100ms)
    user.paste(",")
    key('enter')

method linebreak: user.add_line_breaks_to_method()
