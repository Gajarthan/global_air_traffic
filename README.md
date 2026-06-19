# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_21:06:44_UTC-green)

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

**Latest saved flight:** 2026-06-19 21:06:44 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-19 21:06:44 UTC

- **115,114** saved flights
- **39,916** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **115,114** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,400,041.4 tonnes** estimated CO2 emissions
- **81,161,823 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4748 |
| 2 | SkyWest Airlines | 4283 |
| 3 | EJA | 2234 |
| 4 | IndiGo | 2216 |
| 5 | American Airlines | 1803 |
| 6 | Southwest Airlines | 1711 |
| 7 | ENY | 1432 |
| 8 | Delta Air Lines | 1361 |
| 9 | Lufthansa | 1278 |
| 10 | Vueling | 1040 |
| 11 | WIF | 1022 |
| 12 | LATAM Airlines | 1014 |
| 13 | AZU | 963 |
| 14 | AXM | 950 |
| 15 | LXJ | 875 |
| 16 | Swiss International | 813 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 773 |
| 19 | QLK | 748 |
| 20 | easyJet | 740 |
| 21 | EJU | 723 |
| 22 | Cathay Pacific | 671 |
| 23 | AEE | 646 |
| 24 | United Airlines | 639 |
| 25 | VIV | 635 |
| 26 | Air France | 633 |
| 27 | CXK | 613 |
| 28 | MXY | 609 |
| 29 | AXB | 563 |
| 30 | GLO | 562 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97213 |
| 2 | 🇪🇸 ES | 7856 |
| 3 | 🇮🇳 IN | 6996 |
| 4 | 🇦🇺 AU | 6817 |
| 5 | 🇧🇷 BR | 6354 |
| 6 | 🇮🇹 IT | 6163 |
| 7 | 🇩🇪 DE | 6146 |
| 8 | 🇨🇦 CA | 6061 |
| 9 | 🇯🇵 JP | 5159 |
| 10 | 🇬🇧 GB | 4995 |
| 11 | 🇫🇷 FR | 4572 |
| 12 | 🇨🇴 CO | 3972 |
| 13 | 🇲🇽 MX | 3391 |
| 14 | 🇬🇷 GR | 3279 |
| 15 | 🇳🇴 NO | 3178 |
| 16 | 🇨🇭 CH | 2929 |
| 17 | 🇲🇾 MY | 2458 |
| 18 | 🇹🇷 TR | 2325 |
| 19 | 🇿🇦 ZA | 1945 |
| 20 | 🇳🇿 NZ | 1888 |
| 21 | 🇵🇱 PL | 1885 |
| 22 | 🇰🇷 KR | 1878 |
| 23 | 🇹🇭 TH | 1871 |
| 24 | 🇵🇭 PH | 1667 |
| 25 | 🇬🇹 GT | 1633 |
| 26 | 🇲🇦 MA | 1254 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1132 |
| 29 | 🇳🇱 NL | 1114 |
| 30 | 🇭🇷 HR | 1000 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2436 |
| 2 | Denver International Airport |  | US | 1946 |
| 3 | Tokyo International Airport |  | JP | 1712 |
| 4 | Indira Gandhi International Airport |  | IN | 1529 |
| 5 | Guaymaral Airport |  | CO | 1470 |
| 6 | Harry Reid International Airport |  | US | 1448 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1413 |
| 8 | Zurich Airport |  | CH | 1284 |
| 9 | La Aurora Airport |  | GT | 1260 |
| 10 | Frankfurt am Main International Airport |  | DE | 1248 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1236 |
| 12 | El Dorado International Airport |  | CO | 1170 |
| 13 | Macau International Airport |  | MO | 1168 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1148 |
| 15 | Chicago O'Hare International Airport |  | US | 1134 |
| 16 | Capua Airport |  | IT | 1001 |
| 17 | Salt Lake City International Airport |  | US | 985 |
| 18 | Madrid Barajas International Airport |  | ES | 984 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 965 |
| 20 | Kuala Lumpur International Airport |  | MY | 952 |
| 21 | Charlotte/Douglas International Airport |  | US | 883 |
| 22 | Congonhas Airport |  | BR | 881 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 856 |
| 24 | Bengaluru International Airport |  | IN | 847 |
| 25 | Charles de Gaulle International Airport |  | FR | 846 |
| 26 | General Edward Lawrence Logan International Airport |  | US | 837 |
| 27 | Malpensa International Airport |  | IT | 823 |
| 28 | Ninoy Aquino International Airport |  | PH | 768 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 755 |
| 30 | Tenerife Norte Airport |  | ES | 750 |
| 31 | Daniel K Inouye International Airport |  | US | 749 |
| 32 | Barcelona International Airport |  | ES | 736 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 723 |
| 34 | Don Mueang International Airport |  | TH | 678 |
| 35 | Vitoria/Foronda Airport |  | ES | 678 |
| 36 | Amsterdam Airport Schiphol |  | NL | 678 |
| 37 | Calgary International Airport |  | CA | 676 |
| 38 | Seattle-Tacoma International Airport |  | US | 664 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Viracopos International Airport |  | BR | 657 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 610 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 415 | 21m | 244 km | 1,747.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 306 | 24m | 225 km | 1,187.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 298 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 282 | 1h 25m | 910 km | 4,425.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 274 | 1h 10m | 770 km | 3,639.9 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 230 | 26m | 275 km | 1,089.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 213 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 173 | 22m | 55 km | 164.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 151 | 44m | 241 km | 627.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 137 | 1h 1m | 695 km | 1,642.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 135 | 1h 43m | 1,423 km | 3,313.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 131 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 130 | 1h 17m | 961 km | 2,154.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 128 | 12m | 99 km | 219.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N18JC |  | KHTO (KHTO) | Francis S Gabreski Airport (KFOK) | 2026-06-19 19:40 UTC | 2026-06-19 21:06 UTC | 1h 26m |
| N7876U |  | Oxnard Airport (KOXR) | Oxnard Airport (KOXR) | 2026-06-19 20:51 UTC | 2026-06-19 21:06 UTC | 15m |
| TKR132 | TKR | Valle Airport (K40G) | Mesquite Airport (K67L) | 2026-06-19 20:39 UTC | 2026-06-19 21:00 UTC | 21m |
| N16058 |  | Harvey's Acres Airport (OR28) | Harvey's Acres Airport (OR28) | 2026-06-19 19:43 UTC | 2026-06-19 20:56 UTC | 1h 13m |
| N929KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-19 20:30 UTC | 2026-06-19 20:54 UTC | 24m |
| N36JC |  | Olympia Regional Airport (KOLM) | Wissler's Airport (65WA) | 2026-06-19 20:33 UTC | 2026-06-19 20:54 UTC | 20m |
| N984GB |  | Indianapolis Executive Airport (KTYQ) | Ingersoll Airport (KCTK) | 2026-06-19 20:12 UTC | 2026-06-19 20:51 UTC | 39m |
| WSN50 | WSN | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-06-19 20:31 UTC | 2026-06-19 20:49 UTC | 17m |
| ASA378 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Greater Cumberland Regional Airport (KCBE) | 2026-06-19 16:30 UTC | 2026-06-19 20:46 UTC | 4h 16m |
| N386ST |  | Rocky Hollow Field (PN72) | Ickes Airport (1PS0) | 2026-06-19 20:05 UTC | 2026-06-19 20:46 UTC | 41m |
| RPA4455 | Republic Airways | Eppley Airfield (KOMA) | Mifflin County Airport (KRVL) | 2026-06-19 18:37 UTC | 2026-06-19 20:46 UTC | 2h 9m |
| RPA5685 | Republic Airways | John F Kennedy International Airport (KJFK) | PS98 (PS98) | 2026-06-19 19:18 UTC | 2026-06-19 20:46 UTC | 1h 28m |
| UAL2340 | United Airlines | San Francisco International Airport (KSFO) | Lincoln Farms Airport (5PN8) | 2026-06-19 16:13 UTC | 2026-06-19 20:46 UTC | 4h 33m |
| N55FA |  | Chester County G O Carlson Airport (KMQS) | Chester County G O Carlson Airport (KMQS) | 2026-06-19 20:30 UTC | 2026-06-19 20:45 UTC | 15m |
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-06-19 20:32 UTC | 2026-06-19 20:45 UTC | 12m |
| GERMANO | GER | El Bosque Airport (SCBQ) | El Bosque Airport (SCBQ) | 2026-06-19 20:10 UTC | 2026-06-19 20:44 UTC | 33m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-19 20:30 UTC | 2026-06-19 20:43 UTC | 12m |
| N137RJ |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-06-19 19:45 UTC | 2026-06-19 20:43 UTC | 57m |
| N393BW |  | Fond Du Lac County Airport (KFLD) | Jackson County/Reynolds Field (KJXN) | 2026-06-19 20:12 UTC | 2026-06-19 20:42 UTC | 30m |
| SWA1892 | Southwest Airlines | Gerald R Ford International Airport (KGRR) | Keystone Airport (9PA7) | 2026-06-19 19:28 UTC | 2026-06-19 20:41 UTC | 1h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
