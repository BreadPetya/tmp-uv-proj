import subprocess
import sys

# Установка пакета из GitHub
repo_url = "https://github.com/nigredon1991/tmp-uv-proj.git"
subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    f"git+{repo_url}@master#egg=tmp-uv-proj"
])
