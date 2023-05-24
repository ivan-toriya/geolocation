# geolocation
Fetch lat, lng, accuracy from Geolocation API using only wifi MAC addresses (BSSIDs) around you.

## Example output

```
-------- Google Maps Link --------
https://www.google.com/maps/?q=57.7023999,11.9691114
-------- Response --------
{
    "location": {
        "lat": 57.7023999,
        "lng": 11.9691114
    },
    "accuracy": 30.025
}
-------- Requested MAC Addresses --------
Number of MAC Addresses: 36
Strongest signal strength: -39.4
Weakest signal strength: -80.1
Average signal strength: -54.6625
{
    "wifiAccessPoints": [
        {
            "macAddress": "MM:MM:MM:SS:SS:SS",
            "signalStrength": -50.4
        },
        {
            "macAddress": "MM:MM:MM:SS:SS:SS",
            "signalStrength": -69.1
        }
    ]
}
```
