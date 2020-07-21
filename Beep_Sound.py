import os
beep = lambda x: os.system("echo -n '\a';sleep 0.3;" * x)
beep(10)
