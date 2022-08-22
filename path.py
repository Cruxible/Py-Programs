
#from pathlib import Path

#fpath = Path('bin2').absolute()

#print(fpath)

import os
import getpass
user = getpass.getuser()
print(os.path.join('C:',os.sep, 'Users',os.sep, user))