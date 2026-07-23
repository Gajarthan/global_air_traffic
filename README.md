# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_21:46:17_UTC-green)

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

**Latest saved flight:** 2026-07-23 21:46:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 21:46:17 UTC

- **146,707** saved flights
- **49,063** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **146,707** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,757,098.0 tonnes** estimated CO2 emissions
- **101,860,752 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5944 |
| 2 | SkyWest Airlines | 5384 |
| 3 | EJA | 2904 |
| 4 | IndiGo | 2645 |
| 5 | American Airlines | 2338 |
| 6 | Southwest Airlines | 2218 |
| 7 | ENY | 1826 |
| 8 | Delta Air Lines | 1742 |
| 9 | Lufthansa | 1450 |
| 10 | LATAM Airlines | 1349 |
| 11 | AZU | 1260 |
| 12 | Vueling | 1245 |
| 13 | WIF | 1245 |
| 14 | LXJ | 1132 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1037 |
| 17 | easyJet | 947 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 918 |
| 20 | QLK | 913 |
| 21 | EJU | 900 |
| 22 | VIV | 816 |
| 23 | CXK | 788 |
| 24 | AEE | 777 |
| 25 | JetBlue | 772 |
| 26 | Air France | 770 |
| 27 | MXY | 767 |
| 28 | United Airlines | 765 |
| 29 | Cathay Pacific | 763 |
| 30 | GLO | 757 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 126599 |
| 2 | 🇪🇸 ES | 9499 |
| 3 | 🇦🇺 AU | 8347 |
| 4 | 🇮🇳 IN | 8284 |
| 5 | 🇧🇷 BR | 8271 |
| 6 | 🇨🇦 CA | 7838 |
| 7 | 🇮🇹 IT | 7619 |
| 8 | 🇩🇪 DE | 7537 |
| 9 | 🇬🇧 GB | 6683 |
| 10 | 🇯🇵 JP | 6098 |
| 11 | 🇫🇷 FR | 5816 |
| 12 | 🇨🇴 CO | 4856 |
| 13 | 🇲🇽 MX | 4265 |
| 14 | 🇬🇷 GR | 4157 |
| 15 | 🇳🇴 NO | 3908 |
| 16 | 🇨🇭 CH | 3817 |
| 17 | 🇹🇷 TR | 3438 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2468 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2225 |
| 22 | 🇹🇭 TH | 2141 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1941 |
| 25 | 🇬🇹 GT | 1904 |
| 26 | 🇲🇦 MA | 1514 |
| 27 | 🇲🇪 ME | 1453 |
| 28 | 🇳🇱 NL | 1363 |
| 29 | 🇭🇷 HR | 1337 |
| 30 | 🇲🇴 MO | 1220 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3024 |
| 2 | Denver International Airport |  | US | 2465 |
| 3 | Tokyo International Airport |  | JP | 1960 |
| 4 | Indira Gandhi International Airport |  | IN | 1840 |
| 5 | Harry Reid International Airport |  | US | 1832 |
| 6 | Guaymaral Airport |  | CO | 1812 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1659 |
| 8 | Zurich Airport |  | CH | 1613 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1545 |
| 10 | La Aurora Airport |  | GT | 1475 |
| 11 | Frankfurt am Main International Airport |  | DE | 1401 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1380 |
| 13 | Chicago O'Hare International Airport |  | US | 1364 |
| 14 | Salt Lake City International Airport |  | US | 1326 |
| 15 | El Dorado International Airport |  | CO | 1315 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1273 |
| 17 | Macau International Airport |  | MO | 1220 |
| 18 | Capua Airport |  | IT | 1190 |
| 19 | Congonhas Airport |  | BR | 1180 |
| 20 | Madrid Barajas International Airport |  | ES | 1169 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1152 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1045 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1023 |
| 26 | Charles de Gaulle International Airport |  | FR | 1015 |
| 27 | Bengaluru International Airport |  | IN | 991 |
| 28 | Malpensa International Airport |  | IT | 946 |
| 29 | Ninoy Aquino International Airport |  | PH | 906 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 895 |
| 31 | Barcelona International Airport |  | ES | 888 |
| 32 | Daniel K Inouye International Airport |  | US | 883 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 879 |
| 34 | Tenerife Norte Airport |  | ES | 843 |
| 35 | Seattle-Tacoma International Airport |  | US | 839 |
| 36 | Calgary International Airport |  | CA | 835 |
| 37 | Scottsdale Airport |  | US | 831 |
| 38 | Viracopos International Airport |  | BR | 830 |
| 39 | Amsterdam Airport Schiphol |  | NL | 823 |
| 40 | Oslo Gardermoen Airport |  | NO | 809 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 764 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 532 | 21m | 244 km | 2,240.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 355 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 264 | 27m | 275 km | 1,251.0 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 262 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 220 | 22m | 55 km | 209.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 197 | 44m | 241 km | 818.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 196 | 1h 46m | 1,423 km | 4,810.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 193 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 171 | 1h 16m | 961 km | 2,834.4 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 168 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| POL25 | POL | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-07-23 21:29 UTC | 2026-07-23 21:46 UTC | 16m |
| N652JM |  | Austin Executive Airport (KEDC) | Hearne Municipal Airport (KLHB) | 2026-07-23 20:24 UTC | 2026-07-23 21:43 UTC | 1h 19m |
| N901CA |  | Redding Regional Airport (KRDD) | Ashland Municipal/Sumner Parker Field (KS03) | 2026-07-23 19:40 UTC | 2026-07-23 21:42 UTC | 2h 2m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Macau International Airport (VMMC) | 2026-07-23 17:53 UTC | 2026-07-23 21:42 UTC | 3h 48m |
| UAL967 | United Airlines | L'Aquila / Preturo Airport (LIAP) | Newark Liberty International Airport (KEWR) | 2026-07-23 12:27 UTC | 2026-07-23 21:36 UTC | 9h 8m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-07-23 11:12 UTC | 2026-07-23 21:35 UTC | 10h 22m |
| N300PL |  | L O Simenstad Municipal Airport (KOEO) | Cox-Coyour Memorial Field (59MN) | 2026-07-23 20:39 UTC | 2026-07-23 21:33 UTC | 53m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-07-23 10:16 UTC | 2026-07-23 21:33 UTC | 11h 16m |
| N422JC |  | Wright Field (MD11) | DE04 (DE04) | 2026-07-23 20:38 UTC | 2026-07-23 21:31 UTC | 53m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Zhuhai Airport (ZGSD) | 2026-07-23 10:49 UTC | 2026-07-23 21:31 UTC | 10h 42m |
| N272FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-23 20:42 UTC | 2026-07-23 21:27 UTC | 45m |
| N817WA |  | Benoit Airfield (77AR) | Dallas Love Field (KDAL) | 2026-07-23 20:30 UTC | 2026-07-23 21:27 UTC | 56m |
| N825TB |  | Rogers Executive - Carter Field (KROG) | San Francisco International Airport (KSFO) | 2026-07-23 17:57 UTC | 2026-07-23 21:22 UTC | 3h 25m |
| GRZLY50 | GRZ | Miramar Mcas (Joe Foss Field) Airport (KNKX) | Bishop Airport (KBIH) | 2026-07-23 19:47 UTC | 2026-07-23 21:22 UTC | 1h 34m |
| N761TA |  | Fremont County Airport (K1V6) | Ak Su Airport (CO61) | 2026-07-23 20:55 UTC | 2026-07-23 21:22 UTC | 27m |
| N383TA |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-07-23 20:37 UTC | 2026-07-23 21:16 UTC | 39m |
| N15CT |  | Grand Haven Memorial Airpark (K3GM) | Grand Haven Memorial Airpark (K3GM) | 2026-07-23 21:01 UTC | 2026-07-23 21:16 UTC | 15m |
| EJA939 | EJA | Lehigh Valley International Airport (KABE) | Atlanta Municipal Airport (KY93) | 2026-07-23 19:52 UTC | 2026-07-23 21:15 UTC | 1h 23m |
| N38657 |  | Montgomery County Airpark (KGAI) | Good Neighbor Farm Airport (MD74) | 2026-07-23 20:26 UTC | 2026-07-23 21:14 UTC | 48m |
| CXK558 | CXK | Morristown Municipal Airport (KMMU) | Morristown Municipal Airport (KMMU) | 2026-07-23 21:06 UTC | 2026-07-23 21:13 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
