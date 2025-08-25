Distances were chosen using the histograms in order to try and capture around 10 records. Distances were tested in increments of 50 km from 100 km up if there was not enough results (until 200 km else take the distance of first set of results), or down if there were more than 20 results.

# S7
- < 100km > 14 records
- queries used : 
```
['org~"Siemens" and service=siemens and port=102 and country=DE and last_seen>2024-07-24',
       'org~"GE" and service=siemens and port=102 and country=GB and last_seen>2024-07-24']
````
- 4 different windfarms :
```
['Kriegers Flak', 'Gunfleet Sands 2', 'Gunfleet Sands 1',
       'Kentish Flats 2']
```

# Modbus
- < 100 km > 6 records
- queries used :
```
['org~"GE" and service=modbus and port=502 and country=GB and last_seen>2024-07-24']
```

- 3 different windfarms:
```
['Gunfleet Sands 2', 'Gunfleet Sands 1', 'Kentish Flats 2']
```

# Telnet

- < 100km > 1 records
- queries used :
```
['(org~"ddl" or web.html~"ddl" or banner~"ddl") and service=telnet and port=23 and country=NL and last_seen>2024-07-24']
```

- 1 different windfarms:
```
['Eneco Luchterduinen']
```

- < 200km > 9 records
- queries used :
```
['(org~"GIP" or web.html~"GIP" or banner~"GIP") and service=telnet and port=23 and country=DE and last_seen>2024-07-24',
       '(org~"eneco" or web.html~"eneco" or banner~"eneco") and service=telnet and port=23 and country=DE and last_seen>2024-07-24',
       '(org~"ddl" or web.html~"ddl" or banner~"ddl") and service=telnet and port=23 and country=NL and last_seen>2024-07-24']
```

- 7 different windfarms:
```
['Westermeerdijk buitendijks', 'Meerwind Ost', 'Meerwind Süd',
       'Kaskasi', 'Eneco Luchterduinen',
       'Hollandse Kust Noord Holland I - II', 'Thorntonbank Part 2']
```



# FTP
- < 50km > 13 results
- queries used :
```
['(org~"crosswind" or web.html~"crosswind" or banner~"crosswind") and service=ftp and port=21 and country=NL and last_seen>2024-07-24',
       '(org~"eneco" or web.html~"eneco" or banner~"eneco") and service=ftp and port=21 and country=NL and last_seen>2024-07-24',
       '(org~"windpark" or web.html~"windpark" or banner~"windpark") and service=ftp and port=21 and country=NL and last_seen>2024-07-24']
```

- 5 different windfarms :
```
['Eneco Luchterduinen', 'Westermeerdijk buitendijks',
       'Hollandse Kust Noord Holland I - II', 'Lillgrund',
       'Avedøre Holme']
```

# DNP3
- < 200 > 1 results
- queries used :
```
['(org~"siemens" or web.html~"siemens" or banner~"siemens") and service=dnp3 and port=20000 and country=DE and last_seen>2024-07-24']
```

- 1 different windfarms :
```
['Kriegers Flak']
```


- < 400km > 9 results
- queries used :
```
['org~"Siemens" and service=dnp3 and port=20000 and country=DE and last_seen>2024-07-24',
       '(org~"siemens" or web.html~"siemens" or banner~"siemens") and service=dnp3 and port=20000 and country=DE and last_seen>2024-07-24']
```

- 6 different windfarms :
```
['Eneco Luchterduinen', 'Windpark Fryslân',
       'Westermeerdijk buitendijks', 'Meerwind Ost', 'Kriegers Flak',
       'Meerwind Süd']
```