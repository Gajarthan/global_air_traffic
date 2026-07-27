# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_10:35:30_UTC-green)

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

**Latest saved flight:** 2026-07-27 10:35:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 10:35:30 UTC

- **154,389** saved flights
- **51,455** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **154,389** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,851,611.8 tonnes** estimated CO2 emissions
- **107,339,814 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6217 |
| 2 | SkyWest Airlines | 5660 |
| 3 | EJA | 3055 |
| 4 | IndiGo | 2746 |
| 5 | American Airlines | 2468 |
| 6 | Southwest Airlines | 2428 |
| 7 | ENY | 1932 |
| 8 | Delta Air Lines | 1838 |
| 9 | Lufthansa | 1494 |
| 10 | LATAM Airlines | 1434 |
| 11 | AZU | 1342 |
| 12 | WIF | 1297 |
| 13 | Vueling | 1288 |
| 14 | LXJ | 1189 |
| 15 | AXM | 1097 |
| 16 | Swiss International | 1076 |
| 17 | easyJet | 1006 |
| 18 | Alaska Airlines | 970 |
| 19 | All Nippon Airways | 966 |
| 20 | QLK | 965 |
| 21 | EJU | 944 |
| 22 | VIV | 850 |
| 23 | United Airlines | 831 |
| 24 | CXK | 820 |
| 25 | MXY | 810 |
| 26 | AEE | 809 |
| 27 | JetBlue | 806 |
| 28 | GLO | 805 |
| 29 | Air France | 804 |
| 30 | Cathay Pacific | 792 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 133270 |
| 2 | 🇪🇸 ES | 9950 |
| 3 | 🇧🇷 BR | 8772 |
| 4 | 🇦🇺 AU | 8765 |
| 5 | 🇮🇳 IN | 8629 |
| 6 | 🇨🇦 CA | 8300 |
| 7 | 🇮🇹 IT | 7966 |
| 8 | 🇩🇪 DE | 7859 |
| 9 | 🇬🇧 GB | 7066 |
| 10 | 🇯🇵 JP | 6369 |
| 11 | 🇫🇷 FR | 6105 |
| 12 | 🇨🇴 CO | 5280 |
| 13 | 🇲🇽 MX | 4441 |
| 14 | 🇬🇷 GR | 4393 |
| 15 | 🇳🇴 NO | 4066 |
| 16 | 🇨🇭 CH | 4036 |
| 17 | 🇹🇷 TR | 3677 |
| 18 | 🇲🇾 MY | 2861 |
| 19 | 🇵🇱 PL | 2634 |
| 20 | 🇿🇦 ZA | 2491 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2230 |
| 23 | 🇰🇷 KR | 2085 |
| 24 | 🇵🇭 PH | 2035 |
| 25 | 🇬🇹 GT | 1999 |
| 26 | 🇲🇦 MA | 1574 |
| 27 | 🇲🇪 ME | 1498 |
| 28 | 🇭🇷 HR | 1418 |
| 29 | 🇳🇱 NL | 1412 |
| 30 | 🇲🇴 MO | 1260 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3176 |
| 2 | Denver International Airport |  | US | 2594 |
| 3 | Tokyo International Airport |  | JP | 2017 |
| 4 | Guaymaral Airport |  | CO | 1928 |
| 5 | Indira Gandhi International Airport |  | IN | 1914 |
| 6 | Harry Reid International Airport |  | US | 1898 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1720 |
| 8 | Zurich Airport |  | CH | 1672 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1616 |
| 10 | La Aurora Airport |  | GT | 1550 |
| 11 | Frankfurt am Main International Airport |  | DE | 1442 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1441 |
| 13 | Chicago O'Hare International Airport |  | US | 1418 |
| 14 | Salt Lake City International Airport |  | US | 1395 |
| 15 | El Dorado International Airport |  | CO | 1389 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1312 |
| 17 | Macau International Airport |  | MO | 1260 |
| 18 | Congonhas Airport |  | BR | 1250 |
| 19 | Madrid Barajas International Airport |  | ES | 1229 |
| 20 | Capua Airport |  | IT | 1216 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1189 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1119 |
| 23 | Charlotte/Douglas International Airport |  | US | 1103 |
| 24 | Kuala Lumpur International Airport |  | MY | 1097 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1094 |
| 26 | Charles de Gaulle International Airport |  | FR | 1059 |
| 27 | Bengaluru International Airport |  | IN | 1031 |
| 28 | Malpensa International Airport |  | IT | 1005 |
| 29 | Ninoy Aquino International Airport |  | PH | 953 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 935 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 930 |
| 32 | Barcelona International Airport |  | ES | 920 |
| 33 | Daniel K Inouye International Airport |  | US | 917 |
| 34 | Seattle-Tacoma International Airport |  | US | 900 |
| 35 | Tenerife Norte Airport |  | ES | 884 |
| 36 | Calgary International Airport |  | CA | 882 |
| 37 | Viracopos International Airport |  | BR | 874 |
| 38 | Scottsdale Airport |  | US | 873 |
| 39 | Amsterdam Airport Schiphol |  | NL | 853 |
| 40 | Oslo Gardermoen Airport |  | NO | 844 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 810 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 556 | 21m | 244 km | 2,341.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 373 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 358 | 1h 9m | 770 km | 4,755.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 284 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 210 | 44m | 241 km | 872.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 200 | 20m | 99 km | 342.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 180 | 18m | 144 km | 447.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 179 | 31m | 369 km | 1,139.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 172 | 51m | 556 km | 1,648.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBDAR | HBD | Lodrino Air Base (LSML) | Cannes-Mandelieu Airport (LFMD) | 2026-07-27 08:57 UTC | 2026-07-27 10:35 UTC | 1h 37m |
| RYR5603 | Ryanair | Kaunas International Airport (EYKA) | Khrabrovo Airport (UMKK) | 2026-07-27 09:47 UTC | 2026-07-27 10:19 UTC | 31m |
| PLF105 | PLF | Warsaw Chopin Airport (EPWA) | Hamburg Airport (EDDH) | 2026-07-27 09:05 UTC | 2026-07-27 10:13 UTC | 1h 8m |
| BLADE53 | BLA | Prerov Air Base (LKPO) | Olomouc Glider Airport (LKOL) | 2026-07-27 09:59 UTC | 2026-07-27 10:13 UTC | 13m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-07-26 19:12 UTC | 2026-07-27 10:12 UTC | 15h 0m |
| SWR8ZB | Swiss International | Birmingham International Airport (EGBB) | Zurich Airport (LSZH) | 2026-07-27 08:41 UTC | 2026-07-27 10:08 UTC | 1h 26m |
| WZZ442V | Wizz Air | Katowice International Airport (EPKT) | Brilon/Hochsauerlandkreis Airport (EDKO) | 2026-07-27 08:35 UTC | 2026-07-27 10:07 UTC | 1h 31m |
| SXHGB | SXH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-07-27 09:32 UTC | 2026-07-27 10:00 UTC | 27m |
| OYCKP | OYC | Reykjavik Airport (BIRK) | Hrauneyjarfoss Airport (BIHX) | 2026-07-27 09:28 UTC | 2026-07-27 09:58 UTC | 30m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-27 09:28 UTC | 2026-07-27 09:51 UTC | 23m |
| SWR2WX | Swiss International | Copenhagen Kastrup Airport (EKCH) | Zurich Airport (LSZH) | 2026-07-27 08:18 UTC | 2026-07-27 09:47 UTC | 1h 29m |
| UAL182 | United Airlines | Buffalo Airport (7CO3) | Frankfurt am Main International Airport (EDDF) | 2026-07-27 01:07 UTC | 2026-07-27 09:44 UTC | 8h 37m |
| GAM419A | GAM | Celle Airport (ETHC) | Celle Airport (ETHC) | 2026-07-27 09:02 UTC | 2026-07-27 09:42 UTC | 40m |
| VAA017 | VAA | Kopitnari Airport (UGKO) | UGMS (UGMS) | 2026-07-27 09:25 UTC | 2026-07-27 09:42 UTC | 16m |
| LOT5NA | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | Berlin Brandenburg Airport (EDDB) | 2026-07-27 08:41 UTC | 2026-07-27 09:38 UTC | 56m |
| FHURI | FHU | Agen-La Garenne Airport (LFBA) | Limoges Airport (LFBL) | 2026-07-27 08:57 UTC | 2026-07-27 09:38 UTC | 40m |
| N493LG |  | CO54 (CO54) | 1CO7 (1CO7) | 2026-07-27 09:08 UTC | 2026-07-27 09:37 UTC | 29m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-07-27 07:28 UTC | 2026-07-27 09:37 UTC | 2h 9m |
| RYR39DE | Ryanair | Dublin Airport (EIDW) | Ifrane Airport (GMFI) | 2026-07-27 06:53 UTC | 2026-07-27 09:37 UTC | 2h 43m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-07-27 09:06 UTC | 2026-07-27 09:35 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
