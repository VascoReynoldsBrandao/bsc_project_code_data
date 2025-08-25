Distances were chosen using the histograms in order to try and capture around 10 records. Distances were tested in increments of 50 km from 100 km up if there was not enough results (until 200 km else take the distance of first set of results), or down if there were more than 20 results.

# S7
- < 50 km > 15 records
- queries used : 
```
['org~"Ocean" and service=siemens and port=102 and country=NL and last_seen>2024-07-24']
````
- 4 different windfarms :
```
['Eneco Luchterduinen']
```

# Modbus
- < 100 km > 1 records
- queries used :
```
['org~"Suomen" and service=modbus and port=502 and country=FI and last_seen>2024-07-24']
```

- 3 different windfarms:
```
['Pori-Tahkoluoto']
```

# FTP
- < 50km > 15 results
- queries used :
```
['org~"Power" and service=ftp and port=21 and country=NL and last_seen>2024-07-24']
```

- 2 different windfarms :
```
['Westermeerdijk buitendijks', 'Eneco Luchterduinen']
```
