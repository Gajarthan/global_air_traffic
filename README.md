# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_22:42:39_UTC-green)

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

**Latest saved flight:** 2026-07-27 22:42:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 22:42:39 UTC

- **155,642** saved flights
- **51,796** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **155,642** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,866,979.7 tonnes** estimated CO2 emissions
- **108,230,708 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6261 |
| 2 | SkyWest Airlines | 5718 |
| 3 | EJA | 3092 |
| 4 | IndiGo | 2754 |
| 5 | American Airlines | 2486 |
| 6 | Southwest Airlines | 2450 |
| 7 | ENY | 1944 |
| 8 | Delta Air Lines | 1854 |
| 9 | Lufthansa | 1499 |
| 10 | LATAM Airlines | 1448 |
| 11 | AZU | 1359 |
| 12 | WIF | 1310 |
| 13 | Vueling | 1302 |
| 14 | LXJ | 1196 |
| 15 | AXM | 1098 |
| 16 | Swiss International | 1083 |
| 17 | easyJet | 1014 |
| 18 | Alaska Airlines | 977 |
| 19 | All Nippon Airways | 967 |
| 20 | QLK | 967 |
| 21 | EJU | 955 |
| 22 | VIV | 857 |
| 23 | United Airlines | 836 |
| 24 | CXK | 824 |
| 25 | GLO | 816 |
| 26 | AEE | 813 |
| 27 | MXY | 813 |
| 28 | JetBlue | 812 |
| 29 | Air France | 807 |
| 30 | Cathay Pacific | 802 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134543 |
| 2 | 🇪🇸 ES | 10019 |
| 3 | 🇧🇷 BR | 8875 |
| 4 | 🇦🇺 AU | 8778 |
| 5 | 🇮🇳 IN | 8653 |
| 6 | 🇨🇦 CA | 8387 |
| 7 | 🇮🇹 IT | 8029 |
| 8 | 🇩🇪 DE | 7901 |
| 9 | 🇬🇧 GB | 7138 |
| 10 | 🇯🇵 JP | 6371 |
| 11 | 🇫🇷 FR | 6145 |
| 12 | 🇨🇴 CO | 5395 |
| 13 | 🇲🇽 MX | 4471 |
| 14 | 🇬🇷 GR | 4420 |
| 15 | 🇳🇴 NO | 4104 |
| 16 | 🇨🇭 CH | 4059 |
| 17 | 🇹🇷 TR | 3705 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2649 |
| 20 | 🇿🇦 ZA | 2509 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2042 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1587 |
| 27 | 🇲🇪 ME | 1510 |
| 28 | 🇭🇷 HR | 1431 |
| 29 | 🇳🇱 NL | 1424 |
| 30 | 🇲🇴 MO | 1277 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3203 |
| 2 | Denver International Airport |  | US | 2621 |
| 3 | Tokyo International Airport |  | JP | 2018 |
| 4 | Guaymaral Airport |  | CO | 1955 |
| 5 | Indira Gandhi International Airport |  | IN | 1919 |
| 6 | Harry Reid International Airport |  | US | 1915 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1725 |
| 8 | Zurich Airport |  | CH | 1681 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1635 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1451 |
| 12 | Frankfurt am Main International Airport |  | DE | 1448 |
| 13 | Chicago O'Hare International Airport |  | US | 1422 |
| 14 | Salt Lake City International Airport |  | US | 1405 |
| 15 | El Dorado International Airport |  | CO | 1405 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1319 |
| 17 | Macau International Airport |  | MO | 1277 |
| 18 | Congonhas Airport |  | BR | 1268 |
| 19 | Madrid Barajas International Airport |  | ES | 1235 |
| 20 | Capua Airport |  | IT | 1228 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1197 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1119 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1107 |
| 24 | Charlotte/Douglas International Airport |  | US | 1106 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1063 |
| 27 | Bengaluru International Airport |  | IN | 1033 |
| 28 | Malpensa International Airport |  | IT | 1017 |
| 29 | Ninoy Aquino International Airport |  | PH | 957 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 946 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 941 |
| 32 | Barcelona International Airport |  | ES | 924 |
| 33 | Daniel K Inouye International Airport |  | US | 922 |
| 34 | Seattle-Tacoma International Airport |  | US | 909 |
| 35 | Calgary International Airport |  | CA | 892 |
| 36 | Tenerife Norte Airport |  | ES | 891 |
| 37 | Viracopos International Airport |  | BR | 883 |
| 38 | Scottsdale Airport |  | US | 882 |
| 39 | Amsterdam Airport Schiphol |  | NL | 862 |
| 40 | Oslo Gardermoen Airport |  | NO | 854 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 821 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 561 | 21m | 244 km | 2,362.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 359 | 1h 9m | 770 km | 4,769.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 286 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 214 | 44m | 241 km | 888.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 199 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 196 | 20m | 250 km | 846.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 183 | 18m | 144 km | 455.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 181 | 31m | 369 km | 1,152.1 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 175 | 50m | 556 km | 1,677.5 t |
| 27 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 173 | 1h 39m | 1,156 km | 3,451.3 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 164 | 1h 50m | 1,304 km | 3,689.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N738VY |  | Reedsburg Municipal Airport (KC35) | Thiessen Field (34WI) | 2026-07-27 21:56 UTC | 2026-07-27 22:42 UTC | 46m |
| UAL941 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-07-27 15:16 UTC | 2026-07-27 22:41 UTC | 7h 25m |
| N442AD |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-07-27 21:40 UTC | 2026-07-27 22:32 UTC | 51m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-07-27 11:55 UTC | 2026-07-27 22:29 UTC | 10h 33m |
| N277CB |  | Jacksonville Executive At Craig Airport (KCRG) | Jacksonville Executive At Craig Airport (KCRG) | 2026-07-27 22:10 UTC | 2026-07-27 22:24 UTC | 13m |
| N73574 |  | Dupage Airport (KDPA) | Colonial Acres Airport (4LL8) | 2026-07-27 21:53 UTC | 2026-07-27 22:19 UTC | 26m |
| N782SR |  | Chino Airport (KCNO) | Osborne Airport (8CA0) | 2026-07-27 22:00 UTC | 2026-07-27 22:17 UTC | 16m |
| ICL857 | ICL | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-07-27 11:17 UTC | 2026-07-27 22:15 UTC | 10h 58m |
| N92887 |  | Prineville Airport (KS39) | Sunriver Airport (KS21) | 2026-07-27 21:29 UTC | 2026-07-27 22:15 UTC | 46m |
| CJT301 | CJT | Calgary International Airport (CYYC) | Vancouver International Airport (CYVR) | 2026-07-27 20:56 UTC | 2026-07-27 22:14 UTC | 1h 17m |
| N311VA |  | Albany International Airport (KALB) | Westwind Farm Airport (0NK2) | 2026-07-27 21:09 UTC | 2026-07-27 22:12 UTC | 1h 2m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Macau International Airport (VMMC) | 2026-07-27 12:05 UTC | 2026-07-27 22:12 UTC | 10h 6m |
| N622TP |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-07-27 21:43 UTC | 2026-07-27 22:11 UTC | 28m |
| YGW | YGW | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-27 21:34 UTC | 2026-07-27 22:09 UTC | 35m |
| TRP6 | TRP | Kent Fort Manor Airport (7MD8) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-07-27 21:55 UTC | 2026-07-27 22:08 UTC | 13m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-07-27 14:35 UTC | 2026-07-27 22:07 UTC | 7h 31m |
| N557GG |  | Bob Hope Airport (KBUR) | Henderson Executive Airport (KHND) | 2026-07-27 21:16 UTC | 2026-07-27 22:02 UTC | 45m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-07-27 17:27 UTC | 2026-07-27 22:00 UTC | 4h 33m |
| N5354N |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-07-27 21:37 UTC | 2026-07-27 22:00 UTC | 23m |
| N732SC |  | Chino Airport (KCNO) | Cascade Airport (KU70) | 2026-07-27 20:24 UTC | 2026-07-27 21:59 UTC | 1h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
