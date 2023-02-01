# deauth-attack
: Deauthentication/Authentication Attack을 수행하는 프로그램

<br><br>

## Install
```
pip3 install scapy argparse
```

## Usage
- **Deauth Attack**
```
sudo python3 deauth-attack.py <interface> <AP Mac Address>
``` 
: AP에 있는 **모든** Station 연결 해제
<br><br>

```
sudo python3 deauth-attack.py <interface> <AP Mac Address> <Station Mac Address>
``` 
: AP에 있는 **특정** Station 연결 해제
<br><br>

- **Auth Attack**
```
sudo python3 deauth-attack.py <interface> <AP Mac Address> <Station Mac Address> -auth
```
: AP에 있는 **특정** Station 연결 해제

<br><br>

## Reference
[Python Deauth Attack](https://python.plainenglish.io/deauthentication-attacks-with-python-aa5cc6eeb331)

[Python Auth Attack](https://wlan1nde.wordpress.com/2016/08/24/fake-a-wlan-connection-via-scapy)
