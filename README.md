# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_15:49:39_UTC-green)

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

**Latest saved flight:** 2026-07-27 15:49:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 15:49:39 UTC

- **154,749** saved flights
- **51,545** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **154,749** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,854,725.4 tonnes** estimated CO2 emissions
- **107,520,314 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6230 |
| 2 | SkyWest Airlines | 5665 |
| 3 | EJA | 3059 |
| 4 | IndiGo | 2752 |
| 5 | American Airlines | 2469 |
| 6 | Southwest Airlines | 2432 |
| 7 | ENY | 1935 |
| 8 | Delta Air Lines | 1843 |
| 9 | Lufthansa | 1496 |
| 10 | LATAM Airlines | 1440 |
| 11 | AZU | 1347 |
| 12 | WIF | 1304 |
| 13 | Vueling | 1291 |
| 14 | LXJ | 1190 |
| 15 | AXM | 1098 |
| 16 | Swiss International | 1081 |
| 17 | easyJet | 1007 |
| 18 | Alaska Airlines | 970 |
| 19 | All Nippon Airways | 966 |
| 20 | QLK | 965 |
| 21 | EJU | 946 |
| 22 | VIV | 852 |
| 23 | United Airlines | 831 |
| 24 | CXK | 821 |
| 25 | AEE | 811 |
| 26 | MXY | 810 |
| 27 | JetBlue | 807 |
| 28 | GLO | 806 |
| 29 | Air France | 804 |
| 30 | Cathay Pacific | 793 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 133549 |
| 2 | 🇪🇸 ES | 9965 |
| 3 | 🇧🇷 BR | 8801 |
| 4 | 🇦🇺 AU | 8768 |
| 5 | 🇮🇳 IN | 8645 |
| 6 | 🇨🇦 CA | 8316 |
| 7 | 🇮🇹 IT | 7980 |
| 8 | 🇩🇪 DE | 7874 |
| 9 | 🇬🇧 GB | 7095 |
| 10 | 🇯🇵 JP | 6369 |
| 11 | 🇫🇷 FR | 6123 |
| 12 | 🇨🇴 CO | 5320 |
| 13 | 🇲🇽 MX | 4446 |
| 14 | 🇬🇷 GR | 4399 |
| 15 | 🇳🇴 NO | 4086 |
| 16 | 🇨🇭 CH | 4049 |
| 17 | 🇹🇷 TR | 3686 |
| 18 | 🇲🇾 MY | 2863 |
| 19 | 🇵🇱 PL | 2641 |
| 20 | 🇿🇦 ZA | 2507 |
| 21 | 🇳🇿 NZ | 2312 |
| 22 | 🇹🇭 TH | 2233 |
| 23 | 🇰🇷 KR | 2087 |
| 24 | 🇵🇭 PH | 2039 |
| 25 | 🇬🇹 GT | 2006 |
| 26 | 🇲🇦 MA | 1578 |
| 27 | 🇲🇪 ME | 1502 |
| 28 | 🇭🇷 HR | 1426 |
| 29 | 🇳🇱 NL | 1418 |
| 30 | 🇲🇴 MO | 1264 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3180 |
| 2 | Denver International Airport |  | US | 2597 |
| 3 | Tokyo International Airport |  | JP | 2017 |
| 4 | Guaymaral Airport |  | CO | 1944 |
| 5 | Indira Gandhi International Airport |  | IN | 1915 |
| 6 | Harry Reid International Airport |  | US | 1902 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1722 |
| 8 | Zurich Airport |  | CH | 1677 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1619 |
| 10 | La Aurora Airport |  | GT | 1555 |
| 11 | Frankfurt am Main International Airport |  | DE | 1444 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1441 |
| 13 | Chicago O'Hare International Airport |  | US | 1420 |
| 14 | Salt Lake City International Airport |  | US | 1396 |
| 15 | El Dorado International Airport |  | CO | 1395 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1313 |
| 17 | Macau International Airport |  | MO | 1264 |
| 18 | Congonhas Airport |  | BR | 1254 |
| 19 | Madrid Barajas International Airport |  | ES | 1230 |
| 20 | Capua Airport |  | IT | 1217 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1190 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1119 |
| 23 | Charlotte/Douglas International Airport |  | US | 1103 |
| 24 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1100 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1060 |
| 27 | Bengaluru International Airport |  | IN | 1032 |
| 28 | Malpensa International Airport |  | IT | 1006 |
| 29 | Ninoy Aquino International Airport |  | PH | 955 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 937 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 931 |
| 32 | Barcelona International Airport |  | ES | 920 |
| 33 | Daniel K Inouye International Airport |  | US | 918 |
| 34 | Seattle-Tacoma International Airport |  | US | 900 |
| 35 | Tenerife Norte Airport |  | ES | 886 |
| 36 | Calgary International Airport |  | CA | 885 |
| 37 | Viracopos International Airport |  | BR | 876 |
| 38 | Scottsdale Airport |  | US | 876 |
| 39 | Amsterdam Airport Schiphol |  | NL | 857 |
| 40 | Oslo Gardermoen Airport |  | NO | 848 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 817 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 557 | 21m | 244 km | 2,345.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 371 | 24m | 225 km | 1,439.3 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 358 | 1h 9m | 770 km | 4,755.8 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 286 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 228 | 22m | 55 km | 216.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 212 | 44m | 241 km | 880.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 195 | 20m | 250 km | 842.3 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 181 | 18m | 144 km | 450.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 180 | 31m | 369 km | 1,145.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 173 | 50m | 556 km | 1,658.3 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N41TE |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-07-27 15:19 UTC | 2026-07-27 15:49 UTC | 29m |
| N482SA |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-07-27 15:10 UTC | 2026-07-27 15:49 UTC | 39m |
| SVA152 | Saudia | Vienna International Airport (LOWW) | Golyama Smolnitsa Airport (LB35) | 2026-07-27 14:39 UTC | 2026-07-27 15:48 UTC | 1h 9m |
| BOBCT81 | BOB | MS74 (MS74) | G V Montgomery Airport (K2M4) | 2026-07-27 15:24 UTC | 2026-07-27 15:47 UTC | 23m |
| TGMAV | TGM | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 2026-07-27 15:29 UTC | 2026-07-27 15:46 UTC | 16m |
| ETD933 | Etihad Airways | Al Bateen Executive Airport (OMAD) | Macau International Airport (VMMC) | 2026-07-27 08:28 UTC | 2026-07-27 15:45 UTC | 7h 16m |
| N100LE |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-07-27 15:29 UTC | 2026-07-27 15:42 UTC | 12m |
| HK4813G |  | Enrique Olaya Herrera Airport (SKMD) | La Nubia Airport (SKMZ) | 2026-07-27 14:42 UTC | 2026-07-27 15:41 UTC | 58m |
| BTQ913 | BTQ | Eagle Airport (TA51) | Eagle Airport (TA51) | 2026-07-27 15:22 UTC | 2026-07-27 15:34 UTC | 11m |
| N2130R |  | St Clair County International Airport (KPHN) | St Clair County International Airport (KPHN) | 2026-07-27 14:25 UTC | 2026-07-27 15:30 UTC | 1h 4m |
| GTI518 | GTI | Ted Stevens Anchorage International Airport (PANC) | Eaglesham (South) Airport (CGL4) | 2026-07-27 13:10 UTC | 2026-07-27 15:29 UTC | 2h 18m |
| N496DS |  | Delaware Airpark (K33N) | Delaware Airpark (K33N) | 2026-07-27 15:27 UTC | 2026-07-27 15:29 UTC | 2m |
| N954B |  | Cawleys South Prairie Airport (02WA) | Renton Municipal Airport (KRNT) | 2026-07-27 15:12 UTC | 2026-07-27 15:27 UTC | 15m |
| ERU93 | ERU | Robin Airport (59AZ) | Pilots Rest Airport (AZ57) | 2026-07-27 15:15 UTC | 2026-07-27 15:26 UTC | 10m |
| N173BH |  | Pueblo Memorial Airport (KPUB) | 14CO (14CO) | 2026-07-27 15:08 UTC | 2026-07-27 15:26 UTC | 17m |
| N584M |  | Fish Creek Ranch Airport (WY19) | 6CO4 (6CO4) | 2026-07-27 14:38 UTC | 2026-07-27 15:24 UTC | 46m |
| N313NR |  | KNHZ (KNHZ) | Bangor International Airport (KBGR) | 2026-07-27 13:58 UTC | 2026-07-27 15:21 UTC | 1h 23m |
| IFJ32A | IFJ | Viseu Airport (LPVZ) | Vila Real Airport (LPVR) | 2026-07-27 13:40 UTC | 2026-07-27 15:20 UTC | 1h 39m |
| ZSDIA | ZSD | Rand Airport (FAGM) | New Largo Airport (FANL) | 2026-07-27 14:51 UTC | 2026-07-27 15:18 UTC | 27m |
| N906MD |  | Livermore Municipal Airport (KLVK) | Tracy Municipal Airport (KTCY) | 2026-07-27 15:03 UTC | 2026-07-27 15:18 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
