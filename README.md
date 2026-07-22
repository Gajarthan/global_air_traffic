# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--22_14:37:56_UTC-green)

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

**Latest saved flight:** 2026-07-22 14:37:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-22 14:37:56 UTC

- **143,742** saved flights
- **48,166** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **143,742** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,723,551.2 tonnes** estimated CO2 emissions
- **99,916,014 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5847 |
| 2 | SkyWest Airlines | 5255 |
| 3 | EJA | 2832 |
| 4 | IndiGo | 2612 |
| 5 | American Airlines | 2302 |
| 6 | Southwest Airlines | 2168 |
| 7 | ENY | 1784 |
| 8 | Delta Air Lines | 1705 |
| 9 | Lufthansa | 1439 |
| 10 | LATAM Airlines | 1325 |
| 11 | AZU | 1237 |
| 12 | Vueling | 1233 |
| 13 | WIF | 1228 |
| 14 | LXJ | 1103 |
| 15 | AXM | 1063 |
| 16 | Swiss International | 1023 |
| 17 | easyJet | 939 |
| 18 | All Nippon Airways | 922 |
| 19 | Alaska Airlines | 909 |
| 20 | QLK | 906 |
| 21 | EJU | 880 |
| 22 | VIV | 801 |
| 23 | CXK | 769 |
| 24 | AEE | 764 |
| 25 | Air France | 761 |
| 26 | JetBlue | 761 |
| 27 | MXY | 748 |
| 28 | United Airlines | 746 |
| 29 | Cathay Pacific | 745 |
| 30 | GLO | 735 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 123678 |
| 2 | 🇪🇸 ES | 9349 |
| 3 | 🇦🇺 AU | 8242 |
| 4 | 🇮🇳 IN | 8187 |
| 5 | 🇧🇷 BR | 8117 |
| 6 | 🇨🇦 CA | 7592 |
| 7 | 🇮🇹 IT | 7492 |
| 8 | 🇩🇪 DE | 7424 |
| 9 | 🇬🇧 GB | 6583 |
| 10 | 🇯🇵 JP | 6036 |
| 11 | 🇫🇷 FR | 5718 |
| 12 | 🇨🇴 CO | 4616 |
| 13 | 🇲🇽 MX | 4182 |
| 14 | 🇬🇷 GR | 4081 |
| 15 | 🇳🇴 NO | 3840 |
| 16 | 🇨🇭 CH | 3736 |
| 17 | 🇹🇷 TR | 3384 |
| 18 | 🇲🇾 MY | 2775 |
| 19 | 🇵🇱 PL | 2422 |
| 20 | 🇿🇦 ZA | 2345 |
| 21 | 🇳🇿 NZ | 2209 |
| 22 | 🇹🇭 TH | 2129 |
| 23 | 🇰🇷 KR | 2037 |
| 24 | 🇵🇭 PH | 1934 |
| 25 | 🇬🇹 GT | 1883 |
| 26 | 🇲🇦 MA | 1498 |
| 27 | 🇲🇪 ME | 1427 |
| 28 | 🇳🇱 NL | 1349 |
| 29 | 🇭🇷 HR | 1308 |
| 30 | 🇲🇴 MO | 1203 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2966 |
| 2 | Denver International Airport |  | US | 2413 |
| 3 | Tokyo International Airport |  | JP | 1942 |
| 4 | Indira Gandhi International Airport |  | IN | 1816 |
| 5 | Harry Reid International Airport |  | US | 1802 |
| 6 | Guaymaral Airport |  | CO | 1749 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1639 |
| 8 | Zurich Airport |  | CH | 1593 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1507 |
| 10 | La Aurora Airport |  | GT | 1458 |
| 11 | Frankfurt am Main International Airport |  | DE | 1388 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1356 |
| 13 | Chicago O'Hare International Airport |  | US | 1339 |
| 14 | Salt Lake City International Airport |  | US | 1287 |
| 15 | El Dorado International Airport |  | CO | 1270 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1259 |
| 17 | Macau International Airport |  | MO | 1203 |
| 18 | Capua Airport |  | IT | 1167 |
| 19 | Congonhas Airport |  | BR | 1153 |
| 20 | Madrid Barajas International Airport |  | ES | 1149 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1134 |
| 22 | Kuala Lumpur International Airport |  | MY | 1072 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1043 |
| 24 | Charlotte/Douglas International Airport |  | US | 1035 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1006 |
| 26 | Charles de Gaulle International Airport |  | FR | 1006 |
| 27 | Bengaluru International Airport |  | IN | 977 |
| 28 | Malpensa International Airport |  | IT | 928 |
| 29 | Ninoy Aquino International Airport |  | PH | 903 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 882 |
| 31 | Daniel K Inouye International Airport |  | US | 874 |
| 32 | Barcelona International Airport |  | ES | 874 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 855 |
| 34 | Tenerife Norte Airport |  | ES | 827 |
| 35 | Seattle-Tacoma International Airport |  | US | 821 |
| 36 | Calgary International Airport |  | CA | 818 |
| 37 | Viracopos International Airport |  | BR | 817 |
| 38 | Scottsdale Airport |  | US | 812 |
| 39 | Amsterdam Airport Schiphol |  | NL | 810 |
| 40 | Vitoria/Foronda Airport |  | ES | 787 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 737 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 523 | 21m | 244 km | 2,202.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 349 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 340 | 1h 9m | 770 km | 4,516.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 260 | 26m | 275 km | 1,232.0 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 255 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 213 | 22m | 55 km | 202.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 193 | 26m | 215 km | 714.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 193 | 1h 46m | 1,423 km | 4,736.5 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 191 | 44m | 241 km | 793.4 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 179 | 20m | 250 km | 773.2 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 168 | 1h 16m | 961 km | 2,784.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 164 | 1h 38m | 1,156 km | 3,271.7 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 164 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK284 | CXK | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-22 14:27 UTC | 2026-07-22 14:37 UTC | 10m |
| N172FR |  | Lawrence Regional Airport (KLWC) | Flory Airport (SN21) | 2026-07-22 13:59 UTC | 2026-07-22 14:36 UTC | 37m |
| VXS3 | VXS | Bremen Airport (EDDW) | Durham Tees Valley Airport (EGNV) | 2026-07-22 13:07 UTC | 2026-07-22 14:34 UTC | 1h 26m |
| BSM21 | BSM | Madill Municipal Airport (K1F4) | Diamond J Airport (TS85) | 2026-07-22 14:14 UTC | 2026-07-22 14:28 UTC | 14m |
| N860VA |  | Randolph Afb Aux Airport (KSEQ) | Randolph Afb Aux Airport (KSEQ) | 2026-07-22 14:14 UTC | 2026-07-22 14:27 UTC | 13m |
| LXJ448 | LXJ | Monmouth Executive Airport (KBLM) | Teterboro Airport (KTEB) | 2026-07-22 13:59 UTC | 2026-07-22 14:25 UTC | 26m |
| N280FG |  | Trenton Mercer Airport (KTTN) | Lancaster Airport (KLNS) | 2026-07-22 13:25 UTC | 2026-07-22 14:21 UTC | 55m |
| MILAN80 | MIL | Nimes-Arles-Camargue Airport (LFTW) | Mont-Dauphin - St-Crepin Airport (LFNC) | 2026-07-22 13:58 UTC | 2026-07-22 14:21 UTC | 23m |
| N43020 |  | Lake In The Hills Airport (K3CK) | Lake In The Hills Airport (K3CK) | 2026-07-22 14:19 UTC | 2026-07-22 14:20 UTC | 1m |
| 9MKEN |  | Senai International Airport (WMKJ) | Senai International Airport (WMKJ) | 2026-07-22 13:19 UTC | 2026-07-22 14:17 UTC | 58m |
| N62770 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-22 13:38 UTC | 2026-07-22 14:17 UTC | 38m |
| HB1934 |  | Zweisimmen Airport (LSTZ) | Saanen Airport (LSGK) | 2026-07-22 12:21 UTC | 2026-07-22 14:13 UTC | 1h 52m |
| SWA2981 | Southwest Airlines | Louis Armstrong New Orleans International Airport (KMSY) | Rattlesnake Ridge Airport (TN81) | 2026-07-22 13:01 UTC | 2026-07-22 14:13 UTC | 1h 12m |
| SWR1KA | Swiss International | Václav Havel Airport (LKPR) | Zurich Airport (LSZH) | 2026-07-22 13:10 UTC | 2026-07-22 14:13 UTC | 1h 2m |
| N678SS |  | Scottsdale Airport (KSDL) | Sedona Airport (KSEZ) | 2026-07-22 13:52 UTC | 2026-07-22 14:12 UTC | 19m |
| EJA524 | EJA | Boyne Mountain Airport (KBFA) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-22 13:09 UTC | 2026-07-22 14:10 UTC | 1h 1m |
| SWA3686 | Southwest Airlines | Austin-Bergstrom International Airport (KAUS) | Rattlesnake Ridge Airport (TN81) | 2026-07-22 12:26 UTC | 2026-07-22 14:09 UTC | 1h 43m |
| SCU24 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-07-22 14:06 UTC | 2026-07-22 14:09 UTC | 2m |
| N67973 |  | Denton Enterprise Airport (KDTO) | Rocket Ranch Airport (OK90) | 2026-07-22 13:17 UTC | 2026-07-22 14:08 UTC | 50m |
| HDB1 | HDB | Al Minhad Air Base (OMDM) | Dubai International Airport (OMDB) | 2026-07-22 14:05 UTC | 2026-07-22 14:07 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
