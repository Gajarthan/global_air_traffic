# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_23:04:39_UTC-green)

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

**Latest saved flight:** 2026-08-05 23:04:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 23:04:39 UTC

- **173,385** saved flights
- **56,242** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,385** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,088,733.7 tonnes** estimated CO2 emissions
- **121,086,009 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6885 |
| 2 | SkyWest Airlines | 6360 |
| 3 | EJA | 3447 |
| 4 | IndiGo | 3031 |
| 5 | Southwest Airlines | 2736 |
| 6 | American Airlines | 2728 |
| 7 | ENY | 2162 |
| 8 | Delta Air Lines | 2055 |
| 9 | LATAM Airlines | 1603 |
| 10 | Lufthansa | 1574 |
| 11 | AZU | 1531 |
| 12 | WIF | 1448 |
| 13 | Vueling | 1428 |
| 14 | LXJ | 1360 |
| 15 | AXM | 1184 |
| 16 | Swiss International | 1178 |
| 17 | easyJet | 1175 |
| 18 | EJU | 1059 |
| 19 | QLK | 1056 |
| 20 | Alaska Airlines | 1055 |
| 21 | All Nippon Airways | 1045 |
| 22 | VIV | 952 |
| 23 | Cathay Pacific | 937 |
| 24 | CXK | 924 |
| 25 | GLO | 912 |
| 26 | United Airlines | 904 |
| 27 | AEE | 902 |
| 28 | Air France | 888 |
| 29 | MXY | 878 |
| 30 | JetBlue | 866 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149548 |
| 2 | 🇪🇸 ES | 11092 |
| 3 | 🇧🇷 BR | 9871 |
| 4 | 🇦🇺 AU | 9655 |
| 5 | 🇮🇳 IN | 9507 |
| 6 | 🇨🇦 CA | 9498 |
| 7 | 🇮🇹 IT | 8946 |
| 8 | 🇩🇪 DE | 8585 |
| 9 | 🇬🇧 GB | 8029 |
| 10 | 🇯🇵 JP | 6941 |
| 11 | 🇫🇷 FR | 6868 |
| 12 | 🇨🇴 CO | 6395 |
| 13 | 🇬🇷 GR | 5029 |
| 14 | 🇲🇽 MX | 4961 |
| 15 | 🇨🇭 CH | 4566 |
| 16 | 🇳🇴 NO | 4507 |
| 17 | 🇹🇷 TR | 4247 |
| 18 | 🇲🇾 MY | 3081 |
| 19 | 🇵🇱 PL | 2896 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2532 |
| 22 | 🇳🇿 NZ | 2506 |
| 23 | 🇵🇭 PH | 2282 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2170 |
| 26 | 🇲🇦 MA | 1741 |
| 27 | 🇭🇷 HR | 1673 |
| 28 | 🇲🇪 ME | 1586 |
| 29 | 🇳🇱 NL | 1564 |
| 30 | 🇲🇴 MO | 1498 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3587 |
| 2 | Denver International Airport |  | US | 2877 |
| 3 | Tokyo International Airport |  | JP | 2172 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2118 |
| 6 | Harry Reid International Airport |  | US | 2075 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1882 |
| 8 | Zurich Airport |  | CH | 1832 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1823 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1600 |
| 12 | El Dorado International Airport |  | CO | 1578 |
| 13 | Chicago O'Hare International Airport |  | US | 1570 |
| 14 | Salt Lake City International Airport |  | US | 1556 |
| 15 | Frankfurt am Main International Airport |  | DE | 1536 |
| 16 | Macau International Airport |  | MO | 1498 |
| 17 | Congonhas Airport |  | BR | 1426 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1417 |
| 19 | Capua Airport |  | IT | 1351 |
| 20 | Madrid Barajas International Airport |  | ES | 1349 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1301 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1220 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1204 |
| 24 | Charlotte/Douglas International Airport |  | US | 1198 |
| 25 | Malpensa International Airport |  | IT | 1174 |
| 26 | Charles de Gaulle International Airport |  | FR | 1174 |
| 27 | Kuala Lumpur International Airport |  | MY | 1162 |
| 28 | Bengaluru International Airport |  | IN | 1128 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1079 |
| 30 | Ninoy Aquino International Airport |  | PH | 1075 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1068 |
| 32 | Barcelona International Airport |  | ES | 1025 |
| 33 | Seattle-Tacoma International Airport |  | US | 1001 |
| 34 | Daniel K Inouye International Airport |  | US | 1000 |
| 35 | Calgary International Airport |  | CA | 986 |
| 36 | Reno/Tahoe International Airport |  | US | 985 |
| 37 | Viracopos International Airport |  | BR | 984 |
| 38 | Oslo Gardermoen Airport |  | NO | 963 |
| 39 | Tenerife Norte Airport |  | ES | 960 |
| 40 | Scottsdale Airport |  | US | 945 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 632 | 21m | 244 km | 2,661.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 393 | 1h 8m | 770 km | 5,220.7 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 293 | 27m | 275 km | 1,388.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 260 | 22m | 55 km | 247.1 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 221 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 205 | 19m | 144 km | 509.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 201 | 31m | 369 km | 1,279.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 200 | 1h 38m | 1,156 km | 3,989.9 t |
| 27 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 200 | 8m | - | - |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BCS9TC | BCS | Vitoria/Foronda Airport (LEVT) | Leipzig Halle Airport (EDDP) | 2026-08-05 21:11 UTC | 2026-08-05 23:04 UTC | 1h 53m |
| G21109 |  | Long Island Mac Arthur Airport (KISP) | Long Island Mac Arthur Airport (KISP) | 2026-08-05 22:47 UTC | 2026-08-05 23:01 UTC | 14m |
| SGE | SGE | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-05 22:38 UTC | 2026-08-05 22:52 UTC | 14m |
| N442MA |  | Hastings Municipal Airport (KHSI) | Hastings Municipal Airport (KHSI) | 2026-08-05 22:52 UTC | 2026-08-05 22:52 UTC | 0m |
| N7526G |  | Cable Airport (KCCB) | Brackett Field (KPOC) | 2026-08-05 22:32 UTC | 2026-08-05 22:49 UTC | 16m |
| ERU856 | ERU | Daytona Beach International Airport (KDAB) | Arthur Dunn Air Park (KX21) | 2026-08-05 20:58 UTC | 2026-08-05 22:42 UTC | 1h 44m |
| CGKLD | CGK | Billy Bishop Toronto City Airport (CYTZ) | Billy Bishop Toronto City Airport (CYTZ) | 2026-08-05 22:26 UTC | 2026-08-05 22:38 UTC | 12m |
| N608PT |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-08-05 22:04 UTC | 2026-08-05 22:38 UTC | 33m |
| N40RZ |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-08-05 22:03 UTC | 2026-08-05 22:34 UTC | 31m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-08-05 11:57 UTC | 2026-08-05 22:32 UTC | 10h 35m |
| EJU81DF | EJU | Ibiza Airport (LEIB) | Montelimar - Ancone Airport (LFLQ) | 2026-08-05 21:08 UTC | 2026-08-05 22:30 UTC | 1h 22m |
| EZS18AR | EZS | Lisbon Portela Airport (LPPT) | Morestel Airport (LFHI) | 2026-08-05 20:28 UTC | 2026-08-05 22:30 UTC | 2h 1m |
| RYR5RN | Ryanair | Saniat Rmel Airport (GMTN) | Montpellier-Mediterranee Airport (LFMT) | 2026-08-05 20:39 UTC | 2026-08-05 22:30 UTC | 1h 51m |
| TAY6DN | TAY | Munich International Airport (EDDM) | Bar Sur Seine Airport (LFFR) | 2026-08-05 21:18 UTC | 2026-08-05 22:30 UTC | 1h 11m |
| VOE70ZZ | VOE | Nice-Cote d'Azur Airport (LFMN) | Luxeuil-Saint-Sauveur (BA 116) Air Base (LFSX) | 2026-08-05 21:28 UTC | 2026-08-05 22:30 UTC | 1h 2m |
| FFT1571 | FFT | Phoenix Sky Harbor International Airport (KPHX) | San Diego International Airport (KSAN) | 2026-08-05 21:42 UTC | 2026-08-05 22:29 UTC | 47m |
| QTR8416 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-08-05 10:24 UTC | 2026-08-05 22:29 UTC | 12h 5m |
| GRA523 | GRA | Juan Santamaria International Airport (MROC) | Juan Santamaria International Airport (MROC) | 2026-08-05 22:25 UTC | 2026-08-05 22:29 UTC | 4m |
| N1281Q |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-05 22:22 UTC | 2026-08-05 22:25 UTC | 2m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-05 21:58 UTC | 2026-08-05 22:23 UTC | 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
