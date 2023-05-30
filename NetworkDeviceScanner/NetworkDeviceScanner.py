import subprocess
import re
import platform

def scanNetwork(ipPrefix):
  regexPattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}"
  if not re.fullmatch(regexPattern, ipPrefix): return

  pingCount = None
  if platform.system() == "Windows": pingCount = "-n"
  else:                              pingCount = "-c"

  for host in range(1, 256):
    ip     = f"{ipPrefix}.{host}"
    ping   = ["ping", pingCount, "1", ip]
    result = subprocess.call(ping, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result == 0: print(f"{ip} is active.")

if __name__ == "__main__":
  ip = input("Enter IP Prefix (i.e. 192.168.0): ")
  scanNetwork(ip)
