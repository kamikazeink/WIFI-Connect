#!/usr/bin/env python
import subprocess
subprocess.call("clear")
print('''
   ___ _____    __ _        __ _____
| | | |_  |    /  / \|\||\||_ /   | 
|^|_|_|  _|_   \__\_/| || ||__\__ | 
         
         By KAMIKAZE v0.0.1
''')

ssid_name = input("SSID - > ")
ssid_password = input("Password  >")
subprocess.call(["nmcli", "dev", "wifi", "connect", ssid_name, "password", ssid_password])
