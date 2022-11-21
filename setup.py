import cx_Freeze

executables = [cx_Freeze.Executable('jogo.py')]

cx_Freeze.setup(
    name="Newton Game",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['assets']}},

    executables = executables
    
)