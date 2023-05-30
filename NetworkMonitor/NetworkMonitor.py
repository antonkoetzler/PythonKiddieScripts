from scapy.all import *
import datetime

def packetCallback(packet):
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print(f"[{timestamp}] Packet captured: {packet.summary()}")
  with open("traffic.log", 'a') as logFile:
    logFile.write(f"[{timestamp}] Packet captured: {packet.summary()}\n")

sniff(prn=packetCallback, filter="ip")
