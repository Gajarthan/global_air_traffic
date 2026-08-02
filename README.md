# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_20:46:51_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-08-02 20:46:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 20:46:51 UTC

- **167,657** saved flights
- **54,836** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **167,657** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,020,504.8 tonnes** estimated CO2 emissions
- **117,130,715 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6695 |
| 2 | SkyWest Airlines | 6107 |
| 3 | EJA | 3332 |
| 4 | IndiGo | 2951 |
| 5 | American Airlines | 2646 |
| 6 | Southwest Airlines | 2636 |
| 7 | ENY | 2087 |
| 8 | Delta Air Lines | 2002 |
| 9 | LATAM Airlines | 1553 |
| 10 | Lufthansa | 1543 |
| 11 | AZU | 1475 |
| 12 | WIF | 1401 |
| 13 | Vueling | 1381 |
| 14 | LXJ | 1310 |
| 15 | AXM | 1154 |
| 16 | Swiss International | 1151 |
| 17 | easyJet | 1128 |
| 18 | EJU | 1032 |
| 19 | Alaska Airlines | 1027 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1017 |
| 22 | VIV | 924 |
| 23 | CXK | 892 |
| 24 | Cathay Pacific | 889 |
| 25 | United Airlines | 884 |
| 26 | AEE | 880 |
| 27 | GLO | 878 |
| 28 | Air France | 865 |
| 29 | MXY | 863 |
| 30 | JetBlue | 844 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 144547 |
| 2 | 🇪🇸 ES | 10748 |
| 3 | 🇧🇷 BR | 9542 |
| 4 | 🇦🇺 AU | 9344 |
| 5 | 🇮🇳 IN | 9253 |
| 6 | 🇨🇦 CA | 9086 |
| 7 | 🇮🇹 IT | 8663 |
| 8 | 🇩🇪 DE | 8368 |
| 9 | 🇬🇧 GB | 7791 |
| 10 | 🇯🇵 JP | 6740 |
| 11 | 🇫🇷 FR | 6657 |
| 12 | 🇨🇴 CO | 6033 |
| 13 | 🇬🇷 GR | 4874 |
| 14 | 🇲🇽 MX | 4797 |
| 15 | 🇨🇭 CH | 4417 |
| 16 | 🇳🇴 NO | 4385 |
| 17 | 🇹🇷 TR | 4060 |
| 18 | 🇲🇾 MY | 3009 |
| 19 | 🇵🇱 PL | 2830 |
| 20 | 🇿🇦 ZA | 2723 |
| 21 | 🇳🇿 NZ | 2432 |
| 22 | 🇹🇭 TH | 2424 |
| 23 | 🇵🇭 PH | 2211 |
| 24 | 🇬🇹 GT | 2169 |
| 25 | 🇰🇷 KR | 2147 |
| 26 | 🇲🇦 MA | 1700 |
| 27 | 🇭🇷 HR | 1608 |
| 28 | 🇲🇪 ME | 1550 |
| 29 | 🇳🇱 NL | 1526 |
| 30 | 🇲🇴 MO | 1426 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3441 |
| 2 | Denver International Airport |  | US | 2783 |
| 3 | Tokyo International Airport |  | JP | 2117 |
| 4 | Guaymaral Airport |  | CO | 2090 |
| 5 | Indira Gandhi International Airport |  | IN | 2049 |
| 6 | Harry Reid International Airport |  | US | 2014 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1841 |
| 8 | Zurich Airport |  | CH | 1786 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1761 |
| 10 | La Aurora Airport |  | GT | 1676 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1545 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Chicago O'Hare International Airport |  | US | 1518 |
| 14 | Frankfurt am Main International Airport |  | DE | 1510 |
| 15 | Salt Lake City International Airport |  | US | 1500 |
| 16 | Macau International Airport |  | MO | 1426 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1392 |
| 18 | Congonhas Airport |  | BR | 1376 |
| 19 | Madrid Barajas International Airport |  | ES | 1324 |
| 20 | Capua Airport |  | IT | 1307 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1276 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1181 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1176 |
| 24 | Charlotte/Douglas International Airport |  | US | 1170 |
| 25 | Charles de Gaulle International Airport |  | FR | 1143 |
| 26 | Kuala Lumpur International Airport |  | MY | 1137 |
| 27 | Malpensa International Airport |  | IT | 1125 |
| 28 | Bengaluru International Airport |  | IN | 1095 |
| 29 | Ninoy Aquino International Airport |  | PH | 1039 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1031 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1030 |
| 32 | Barcelona International Airport |  | ES | 988 |
| 33 | Daniel K Inouye International Airport |  | US | 976 |
| 34 | Seattle-Tacoma International Airport |  | US | 972 |
| 35 | Viracopos International Airport |  | BR | 955 |
| 36 | Calgary International Airport |  | CA | 948 |
| 37 | Tenerife Norte Airport |  | ES | 935 |
| 38 | Oslo Gardermoen Airport |  | NO | 932 |
| 39 | Scottsdale Airport |  | US | 929 |
| 40 | Reno/Tahoe International Airport |  | US | 926 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 870 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 609 | 21m | 244 km | 2,564.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 401 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 316 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 245 | 19m | 165 km | 696.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 244 | 44m | 241 km | 1,013.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 221 | 20m | 250 km | 954.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 218 | 26m | 215 km | 807.4 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 215 | 31m | 49 km | 181.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 199 | 19m | 144 km | 495.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 194 | 31m | 369 km | 1,234.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 192 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 191 | 50m | 556 km | 1,830.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 187 | 1h 38m | 1,156 km | 3,730.6 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 184 | 24m | 218 km | 693.2 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 183 | 1h 1m | 695 km | 2,193.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL509 | United Airlines | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Newark Liberty International Airport (KEWR) | 2026-08-02 12:05 UTC | 2026-08-02 20:46 UTC | 8h 41m |
| N76091 |  | Riverside Airport (KRAL) | Ramona Airport (KRNM) | 2026-08-02 20:04 UTC | 2026-08-02 20:46 UTC | 42m |
| N1933T |  | Fairfield County Airport (KLHQ) | Pickaway County Memorial Airport (KCYO) | 2026-08-02 20:33 UTC | 2026-08-02 20:45 UTC | 11m |
| N122AH |  | Deering Airport (PADE) | Ralph Wien Memorial Airport (PAOT) | 2026-08-02 20:24 UTC | 2026-08-02 20:36 UTC | 12m |
| RAM801F | Royal Air Maroc | London Heathrow Airport (EGLL) | Mohammed V International Airport (GMMN) | 2026-08-02 17:44 UTC | 2026-08-02 20:30 UTC | 2h 45m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-02 20:15 UTC | 2026-08-02 20:26 UTC | 11m |
| CXK199 | CXK | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-02 19:56 UTC | 2026-08-02 20:19 UTC | 23m |
| THY7LA | Turkish Airlines | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-08-02 18:18 UTC | 2026-08-02 20:19 UTC | 2h 0m |
| N3225A |  | Marion Airport (KC17) | IA80 (IA80) | 2026-08-02 19:59 UTC | 2026-08-02 20:16 UTC | 16m |
| N883CE |  | Los Angeles International Airport (KLAX) | Minden-Tahoe Airport (KMEV) | 2026-08-02 19:25 UTC | 2026-08-02 20:14 UTC | 48m |
| STT5002 | STT | Lanai Airport (PHNY) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-08-02 19:48 UTC | 2026-08-02 20:13 UTC | 25m |
| N900BA |  | Joe Foss Field (KFSD) | Wadena Municipal Airport (KADC) | 2026-08-02 19:31 UTC | 2026-08-02 20:11 UTC | 39m |
| ASP875 | ASP | Halifax Robert L. Stanfield International Airport (CYHZ) | Toronto Pearson International Airport (CYYZ) | 2026-08-02 17:56 UTC | 2026-08-02 20:10 UTC | 2h 14m |
| RAM717X | Royal Air Maroc | Nantes Atlantique Airport (LFRS) | Mohammed V International Airport (GMMN) | 2026-08-02 17:59 UTC | 2026-08-02 20:10 UTC | 2h 10m |
| N738AJ |  | Ashland Municipal/Sumner Parker Field (KS03) | Siskiyou County Airport (KSIY) | 2026-08-02 19:55 UTC | 2026-08-02 20:09 UTC | 13m |
| N41533 |  | Bugs Airport (PA68) | Lehigh Valley International Airport (KABE) | 2026-08-02 19:30 UTC | 2026-08-02 20:07 UTC | 37m |
| RAM983 | Royal Air Maroc | Lisbon Portela Airport (LPPT) | Tit Mellil Airport (GMMT) | 2026-08-02 18:35 UTC | 2026-08-02 20:06 UTC | 1h 30m |
| RAM733M | Royal Air Maroc | Marseille Provence Airport (LFML) | Ben Slimane Airport (GMMB) | 2026-08-02 18:05 UTC | 2026-08-02 20:03 UTC | 1h 58m |
| N191DB |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Preszler Airstrip (1NA8) | 2026-08-02 18:36 UTC | 2026-08-02 20:01 UTC | 1h 24m |
| EZY826T | easyJet | London Luton Airport (EGGW) | Edinburgh Airport (EGPH) | 2026-08-02 19:10 UTC | 2026-08-02 20:00 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
