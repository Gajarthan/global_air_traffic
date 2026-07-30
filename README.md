# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_15:06:39_UTC-green)

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

**Latest saved flight:** 2026-07-30 15:06:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 15:06:39 UTC

- **160,407** saved flights
- **53,010** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **160,407** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,925,795.8 tonnes** estimated CO2 emissions
- **111,640,338 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6427 |
| 2 | SkyWest Airlines | 5840 |
| 3 | EJA | 3178 |
| 4 | IndiGo | 2827 |
| 5 | American Airlines | 2534 |
| 6 | Southwest Airlines | 2514 |
| 7 | ENY | 1995 |
| 8 | Delta Air Lines | 1906 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1504 |
| 11 | AZU | 1412 |
| 12 | WIF | 1359 |
| 13 | Vueling | 1336 |
| 14 | LXJ | 1236 |
| 15 | AXM | 1120 |
| 16 | Swiss International | 1108 |
| 17 | easyJet | 1050 |
| 18 | Alaska Airlines | 1001 |
| 19 | QLK | 991 |
| 20 | All Nippon Airways | 990 |
| 21 | EJU | 983 |
| 22 | VIV | 881 |
| 23 | CXK | 854 |
| 24 | United Airlines | 847 |
| 25 | Cathay Pacific | 846 |
| 26 | GLO | 845 |
| 27 | AEE | 843 |
| 28 | Air France | 836 |
| 29 | MXY | 833 |
| 30 | JetBlue | 821 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 138324 |
| 2 | 🇪🇸 ES | 10289 |
| 3 | 🇧🇷 BR | 9168 |
| 4 | 🇦🇺 AU | 9078 |
| 5 | 🇮🇳 IN | 8892 |
| 6 | 🇨🇦 CA | 8710 |
| 7 | 🇮🇹 IT | 8276 |
| 8 | 🇩🇪 DE | 8114 |
| 9 | 🇬🇧 GB | 7374 |
| 10 | 🇯🇵 JP | 6529 |
| 11 | 🇫🇷 FR | 6355 |
| 12 | 🇨🇴 CO | 5664 |
| 13 | 🇬🇷 GR | 4599 |
| 14 | 🇲🇽 MX | 4598 |
| 15 | 🇳🇴 NO | 4245 |
| 16 | 🇨🇭 CH | 4215 |
| 17 | 🇹🇷 TR | 3831 |
| 18 | 🇲🇾 MY | 2908 |
| 19 | 🇵🇱 PL | 2726 |
| 20 | 🇿🇦 ZA | 2593 |
| 21 | 🇳🇿 NZ | 2364 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2117 |
| 24 | 🇰🇷 KR | 2108 |
| 25 | 🇬🇹 GT | 2045 |
| 26 | 🇲🇦 MA | 1625 |
| 27 | 🇲🇪 ME | 1526 |
| 28 | 🇭🇷 HR | 1498 |
| 29 | 🇳🇱 NL | 1474 |
| 30 | 🇲🇴 MO | 1338 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3273 |
| 2 | Denver International Airport |  | US | 2665 |
| 3 | Tokyo International Airport |  | JP | 2063 |
| 4 | Guaymaral Airport |  | CO | 2016 |
| 5 | Indira Gandhi International Airport |  | IN | 1977 |
| 6 | Harry Reid International Airport |  | US | 1951 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1776 |
| 8 | Zurich Airport |  | CH | 1717 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1683 |
| 10 | La Aurora Airport |  | GT | 1587 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1493 |
| 12 | El Dorado International Airport |  | CO | 1469 |
| 13 | Frankfurt am Main International Airport |  | DE | 1467 |
| 14 | Chicago O'Hare International Airport |  | US | 1453 |
| 15 | Salt Lake City International Airport |  | US | 1442 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1341 |
| 17 | Macau International Airport |  | MO | 1338 |
| 18 | Congonhas Airport |  | BR | 1331 |
| 19 | Madrid Barajas International Airport |  | ES | 1271 |
| 20 | Capua Airport |  | IT | 1262 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1229 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1147 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1137 |
| 24 | Charlotte/Douglas International Airport |  | US | 1123 |
| 25 | Kuala Lumpur International Airport |  | MY | 1111 |
| 26 | Charles de Gaulle International Airport |  | FR | 1101 |
| 27 | Malpensa International Airport |  | IT | 1063 |
| 28 | Bengaluru International Airport |  | IN | 1057 |
| 29 | Ninoy Aquino International Airport |  | PH | 993 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 977 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 977 |
| 32 | Barcelona International Airport |  | ES | 957 |
| 33 | Daniel K Inouye International Airport |  | US | 945 |
| 34 | Seattle-Tacoma International Airport |  | US | 935 |
| 35 | Calgary International Airport |  | CA | 922 |
| 36 | Viracopos International Airport |  | BR | 917 |
| 37 | Scottsdale Airport |  | US | 904 |
| 38 | Tenerife Norte Airport |  | ES | 901 |
| 39 | Oslo Gardermoen Airport |  | NO | 892 |
| 40 | Amsterdam Airport Schiphol |  | NL | 885 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 846 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 584 | 21m | 244 km | 2,459.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 380 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 369 | 1h 9m | 770 km | 4,901.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 295 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 282 | 27m | 275 km | 1,336.3 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 235 | 22m | 55 km | 223.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 229 | 44m | 241 km | 951.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 220 | 1h 47m | 1,423 km | 5,399.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 202 | 20m | 250 km | 872.5 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 192 | 30m | 49 km | 162.3 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 190 | 18m | 144 km | 472.6 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 190 | 27m | 152 km | 496.5 t |
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
| HB2562 |  | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-07-30 10:40 UTC | 2026-07-30 15:06 UTC | 4h 25m |
| N407GX |  | Fuller Airport (TS00) | Fuller Airport (TS00) | 2026-07-30 14:42 UTC | 2026-07-30 15:03 UTC | 21m |
| HK4646G |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-07-30 14:35 UTC | 2026-07-30 15:02 UTC | 26m |
| OTLW64 | OTL | Southport Airport (CYPG) | Southport Airport (CYPG) | 2026-07-30 13:55 UTC | 2026-07-30 15:00 UTC | 1h 5m |
| N7660U |  | Mason County Airport (K3I2) | Ohio University Airport (KUNI) | 2026-07-30 14:40 UTC | 2026-07-30 14:59 UTC | 18m |
| N361LU |  | Lewis University Airport (KLOT) | Lewis University Airport (KLOT) | 2026-07-30 14:24 UTC | 2026-07-30 14:57 UTC | 33m |
| VTE3051 | VTE | Veterans Airport Of Southern Illinois Airport (KMWA) | Chicago O'Hare International Airport (KORD) | 2026-07-30 13:46 UTC | 2026-07-30 14:54 UTC | 1h 8m |
| HBXDA | HBX | Muenster Aero Airport (LSPU) | Raron Airport (LSTA) | 2026-07-30 14:35 UTC | 2026-07-30 14:54 UTC | 18m |
| N673MA |  | Lewis University Airport (KLOT) | 3IL2 (3IL2) | 2026-07-30 14:31 UTC | 2026-07-30 14:52 UTC | 21m |
| CXK430 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-30 14:28 UTC | 2026-07-30 14:50 UTC | 22m |
| N571JA |  | Aurora Municipal Airport (KARR) | Humm Airport (06IL) | 2026-07-30 14:26 UTC | 2026-07-30 14:42 UTC | 15m |
| TGOZI | TGO | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-07-30 14:11 UTC | 2026-07-30 14:38 UTC | 27m |
| CD11 |  | 23CN (23CN) | Loma Madera Ranch Airport (25CA) | 2026-07-30 14:10 UTC | 2026-07-30 14:34 UTC | 24m |
| N313EC |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-07-30 14:03 UTC | 2026-07-30 14:34 UTC | 31m |
| EZY149Y | easyJet | Belfast International Airport (EGAA) | Glasgow International Airport (EGPF) | 2026-07-30 14:04 UTC | 2026-07-30 14:34 UTC | 30m |
| CXK1050 | CXK | Gwinnett County/Briscoe Field (KLZU) | Gwinnett County/Briscoe Field (KLZU) | 2026-07-30 13:46 UTC | 2026-07-30 14:33 UTC | 46m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-07-30 14:20 UTC | 2026-07-30 14:31 UTC | 10m |
|  |  | K1J0 (K1J0) | Marianna Municipal Airport (KMAI) | 2026-07-30 14:22 UTC | 2026-07-30 14:31 UTC | 8m |
| FD607 |  | Perth Jandakot Airport (YPJT) | Quairading Airport (YQDG) | 2026-07-30 14:05 UTC | 2026-07-30 14:30 UTC | 25m |
| N802HB |  | Platteville Municipal Airport (KPVB) | Platteville Municipal Airport (KPVB) | 2026-07-30 12:53 UTC | 2026-07-30 14:30 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
