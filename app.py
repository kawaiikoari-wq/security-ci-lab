import hashlib, shlex, subprocess, os
 
API_KEY = os.environ.get("API_KEY")   # секрет берём из окружения, не из кода
 
def run(cmd):
    return subprocess.call(shlex.split(cmd))     # без shell=True
 
def strong_hash(p):
    return hashlib.sha256(p.encode()).hexdigest()
