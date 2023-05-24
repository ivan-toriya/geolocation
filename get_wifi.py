# %%
import subprocess
import re

# %%
cmd = '(netsh wlan show networks mode=Bssid | Out-String) -split "`r`n" | Select-String -Pattern "SSID|BSSID|Signal"'

cmd_result = (
    subprocess.run(["powershell.exe", "-Command", cmd], capture_output=True, text=True)
    .stdout.replace(" ", "")
    .replace("\n", "")
)


def parse_wifi_data(input: str):
    pattern = r"BSSID\d:([0-9a-f:]+)Signal:(\d+)%"
    matches = re.findall(pattern, input, re.IGNORECASE)

    wifi_list = [
        {"macAddress": mac, "signalStrength": -90 + (int(sig) / 100) * 55}
        for mac, sig in matches
    ]

    return wifi_list


def get_wifi_data():
    return parse_wifi_data(cmd_result)
