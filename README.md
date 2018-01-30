# FlaSi
Deze API dient als brug voor het verbinden van een specifieke HomeLynk installatie met de buitenwereld.
Het kan in deze data ophalen uit de database van de HomeLynk installatie alswel domotica objecten via het huis aansturen.

## Requirements
Python 3.5.2+

Libraries in requirements.txt (pip3 install -r requirements.txt)

## Paths & Usage
De FlaSi kan op de huidige versie een MySQL database uitlezen en de domotica objecten aansturen.
Het maakt hier gebruik van de variabelen zoals aangegeven in de config.py.

De definitieve paths van de API draaien altijd op de volgende URL via een graphic interface.

```
http://localhost:8080/ui/
```


Om integration tests te draaien, gebruik tox:
```
sudo pip install tox
tox
```

## Starten met of zonder Docker
Check allereerst of je alle dependencies vanuit de requirements.txt hebt geinstalleerd met 
```
pip3 install -r requirements.txt
```

Om de server normaal te starten gebruik je het volgende commando vanaf de root:
```
python3 -m swagger_server
```

Om de docker container te starten gebruik je de volgende commando van de root
```bash
# Container bouwen
docker build -t swagger_server .

# Container opstarten
docker run -p 8080:8080 swagger_server
```

## Changelog & Documentation
De documentatie is te vinden op de volgende url:
```
https://github.com/selficient/docs/blob/master/Systeem%20Architectuur/Technisch%20ontwerp.pdf
```

Current version:

| Version  | Release Date  |
| -------- |:-------------:|
| 0.1      | 20 November   |
| 0.2      | 20 December   |
| 0.3      | 15 Januari    |
| 0.4      | 23 Januari    |
| 1.0*     | 29 Januari    |

* Latest stable build
