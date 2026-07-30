# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_08:48:30_UTC-green)

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

**Latest saved flight:** 2026-07-30 08:48:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 08:48:30 UTC

- **159,978** saved flights
- **52,925** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **159,978** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,920,681.6 tonnes** estimated CO2 emissions
- **111,343,862 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6415 |
| 2 | SkyWest Airlines | 5837 |
| 3 | EJA | 3175 |
| 4 | IndiGo | 2817 |
| 5 | American Airlines | 2531 |
| 6 | Southwest Airlines | 2511 |
| 7 | ENY | 1994 |
| 8 | Delta Air Lines | 1904 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1502 |
| 11 | AZU | 1409 |
| 12 | WIF | 1355 |
| 13 | Vueling | 1336 |
| 14 | LXJ | 1233 |
| 15 | AXM | 1116 |
| 16 | Swiss International | 1101 |
| 17 | easyJet | 1045 |
| 18 | Alaska Airlines | 1001 |
| 19 | QLK | 991 |
| 20 | All Nippon Airways | 989 |
| 21 | EJU | 978 |
| 22 | VIV | 877 |
| 23 | CXK | 847 |
| 24 | United Airlines | 847 |
| 25 | Cathay Pacific | 843 |
| 26 | GLO | 842 |
| 27 | AEE | 841 |
| 28 | Air France | 832 |
| 29 | MXY | 832 |
| 30 | JetBlue | 820 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 138093 |
| 2 | 🇪🇸 ES | 10257 |
| 3 | 🇧🇷 BR | 9148 |
| 4 | 🇦🇺 AU | 9062 |
| 5 | 🇮🇳 IN | 8857 |
| 6 | 🇨🇦 CA | 8699 |
| 7 | 🇮🇹 IT | 8259 |
| 8 | 🇩🇪 DE | 8087 |
| 9 | 🇬🇧 GB | 7326 |
| 10 | 🇯🇵 JP | 6513 |
| 11 | 🇫🇷 FR | 6321 |
| 12 | 🇨🇴 CO | 5636 |
| 13 | 🇬🇷 GR | 4590 |
| 14 | 🇲🇽 MX | 4589 |
| 15 | 🇳🇴 NO | 4234 |
| 16 | 🇨🇭 CH | 4178 |
| 17 | 🇹🇷 TR | 3818 |
| 18 | 🇲🇾 MY | 2901 |
| 19 | 🇵🇱 PL | 2715 |
| 20 | 🇿🇦 ZA | 2577 |
| 21 | 🇳🇿 NZ | 2362 |
| 22 | 🇹🇭 TH | 2289 |
| 23 | 🇵🇭 PH | 2110 |
| 24 | 🇰🇷 KR | 2104 |
| 25 | 🇬🇹 GT | 2040 |
| 26 | 🇲🇦 MA | 1621 |
| 27 | 🇲🇪 ME | 1525 |
| 28 | 🇭🇷 HR | 1485 |
| 29 | 🇳🇱 NL | 1465 |
| 30 | 🇲🇴 MO | 1330 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3270 |
| 2 | Denver International Airport |  | US | 2663 |
| 3 | Tokyo International Airport |  | JP | 2058 |
| 4 | Guaymaral Airport |  | CO | 2006 |
| 5 | Indira Gandhi International Airport |  | IN | 1971 |
| 6 | Harry Reid International Airport |  | US | 1950 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1772 |
| 8 | Zurich Airport |  | CH | 1708 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1682 |
| 10 | La Aurora Airport |  | GT | 1583 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1493 |
| 12 | El Dorado International Airport |  | CO | 1465 |
| 13 | Frankfurt am Main International Airport |  | DE | 1465 |
| 14 | Chicago O'Hare International Airport |  | US | 1450 |
| 15 | Salt Lake City International Airport |  | US | 1440 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1337 |
| 17 | Macau International Airport |  | MO | 1330 |
| 18 | Congonhas Airport |  | BR | 1327 |
| 19 | Madrid Barajas International Airport |  | ES | 1265 |
| 20 | Capua Airport |  | IT | 1258 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1229 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1146 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1137 |
| 24 | Charlotte/Douglas International Airport |  | US | 1122 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1097 |
| 27 | Malpensa International Airport |  | IT | 1061 |
| 28 | Bengaluru International Airport |  | IN | 1055 |
| 29 | Ninoy Aquino International Airport |  | PH | 989 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 977 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 974 |
| 32 | Barcelona International Airport |  | ES | 953 |
| 33 | Daniel K Inouye International Airport |  | US | 944 |
| 34 | Seattle-Tacoma International Airport |  | US | 935 |
| 35 | Calgary International Airport |  | CA | 921 |
| 36 | Viracopos International Airport |  | BR | 915 |
| 37 | Scottsdale Airport |  | US | 904 |
| 38 | Tenerife Norte Airport |  | ES | 898 |
| 39 | Oslo Gardermoen Airport |  | NO | 889 |
| 40 | Amsterdam Airport Schiphol |  | NL | 879 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 842 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 583 | 21m | 244 km | 2,454.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 367 | 1h 9m | 770 km | 4,875.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 294 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 227 | 44m | 241 km | 942.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 218 | 1h 47m | 1,423 km | 5,350.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 201 | 20m | 250 km | 868.2 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 192 | 30m | 49 km | 162.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 189 | 18m | 144 km | 470.1 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 182 | 50m | 556 km | 1,744.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 177 | 1h 1m | 695 km | 2,121.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Macau International Airport (VMMC) | 2026-07-29 21:54 UTC | 2026-07-30 08:48 UTC | 10h 53m |
| KFN | KFN | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-07-30 08:06 UTC | 2026-07-30 08:47 UTC | 40m |
| KUR | KUR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-07-30 07:59 UTC | 2026-07-30 08:40 UTC | 40m |
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-07-29 21:39 UTC | 2026-07-30 08:36 UTC | 10h 56m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-07-30 08:25 UTC | 2026-07-30 08:36 UTC | 10m |
| ADSBTST | ADS | Luqa Airport (LMML) | Luqa Airport (LMML) | 2026-07-30 07:19 UTC | 2026-07-30 08:35 UTC | 1h 15m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-30 08:09 UTC | 2026-07-30 08:29 UTC | 20m |
| PROVA5 | PRO | Torino / Caselle International Airport (LIMF) | Varese / Venegono Airport (LILN) | 2026-07-30 08:00 UTC | 2026-07-30 08:20 UTC | 20m |
| XCN70 | XCN | Cable Creek Ranch Airport (96OR) | Sourdough Airport (5WA0) | 2026-07-30 07:00 UTC | 2026-07-30 08:19 UTC | 1h 19m |
| HSOMR2 | HSO | Emden Airport (EDWE) | Borkum Airport (EDWR) | 2026-07-30 07:50 UTC | 2026-07-30 08:19 UTC | 28m |
| AYT103 | AYT | Hatzor Air Base (LLHS) | Ein Yahav Airfield (LLEY) | 2026-07-30 07:58 UTC | 2026-07-30 08:16 UTC | 17m |
| HBPMZ | HBP | LSMF (LSMF) | Friedrichshafen Airport (EDNY) | 2026-07-30 07:12 UTC | 2026-07-30 08:16 UTC | 1h 3m |
| DIFLE | DIF | Harle Airport (EDXP) | Wangerooge Airport (EDWG) | 2026-07-30 08:06 UTC | 2026-07-30 08:10 UTC | 3m |
| BH971 |  | VGZR (VGZR) | Tejgaon Airport (VGTJ) | 2026-07-30 07:29 UTC | 2026-07-30 08:07 UTC | 37m |
| A77 |  | Perth Jandakot Airport (YPJT) | Garden Island (Military) Airport (YGAD) | 2026-07-30 07:56 UTC | 2026-07-30 08:05 UTC | 9m |
| ANE93XQ | ANE | Sevilla Airport (LEZL) | Almeria International Airport (LEAM) | 2026-07-30 07:15 UTC | 2026-07-30 08:02 UTC | 47m |
| T7AAMA |  | Nice-Cote d'Azur Airport (LFMN) | Trieste / Ronchi Dei Legionari (LIPQ) | 2026-07-30 07:11 UTC | 2026-07-30 08:00 UTC | 49m |
| OAL082 | OAL | Thessaloniki Macedonia International Airport (LGTS) | Ikaria Airport (LGIK) | 2026-07-30 06:50 UTC | 2026-07-30 07:57 UTC | 1h 7m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-07-30 07:06 UTC | 2026-07-30 07:57 UTC | 50m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-07-30 07:43 UTC | 2026-07-30 07:56 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
