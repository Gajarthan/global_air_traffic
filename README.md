# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_20:13:17_UTC-green)

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

**Latest saved flight:** 2026-07-06 20:13:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-06 20:13:17 UTC

- **131,343** saved flights
- **44,639** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **131,343** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,584,709.7 tonnes** estimated CO2 emissions
- **91,867,227 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5344 |
| 2 | SkyWest Airlines | 4865 |
| 3 | EJA | 2577 |
| 4 | IndiGo | 2458 |
| 5 | American Airlines | 2038 |
| 6 | Southwest Airlines | 1980 |
| 7 | ENY | 1653 |
| 8 | Delta Air Lines | 1574 |
| 9 | Lufthansa | 1370 |
| 10 | LATAM Airlines | 1204 |
| 11 | Vueling | 1159 |
| 12 | WIF | 1146 |
| 13 | AZU | 1116 |
| 14 | LXJ | 1015 |
| 15 | AXM | 1012 |
| 16 | Swiss International | 918 |
| 17 | All Nippon Airways | 863 |
| 18 | easyJet | 842 |
| 19 | Alaska Airlines | 840 |
| 20 | QLK | 820 |
| 21 | EJU | 812 |
| 22 | VIV | 724 |
| 23 | Cathay Pacific | 716 |
| 24 | AEE | 714 |
| 25 | Air France | 714 |
| 26 | CXK | 703 |
| 27 | United Airlines | 701 |
| 28 | JetBlue | 690 |
| 29 | MXY | 685 |
| 30 | GLO | 674 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 112545 |
| 2 | 🇪🇸 ES | 8765 |
| 3 | 🇮🇳 IN | 7705 |
| 4 | 🇦🇺 AU | 7567 |
| 5 | 🇧🇷 BR | 7400 |
| 6 | 🇨🇦 CA | 6928 |
| 7 | 🇩🇪 DE | 6878 |
| 8 | 🇮🇹 IT | 6854 |
| 9 | 🇬🇧 GB | 5866 |
| 10 | 🇯🇵 JP | 5653 |
| 11 | 🇫🇷 FR | 5228 |
| 12 | 🇨🇴 CO | 4113 |
| 13 | 🇲🇽 MX | 3830 |
| 14 | 🇬🇷 GR | 3757 |
| 15 | 🇳🇴 NO | 3561 |
| 16 | 🇨🇭 CH | 3379 |
| 17 | 🇹🇷 TR | 2920 |
| 18 | 🇲🇾 MY | 2623 |
| 19 | 🇿🇦 ZA | 2171 |
| 20 | 🇵🇱 PL | 2157 |
| 21 | 🇳🇿 NZ | 2088 |
| 22 | 🇹🇭 TH | 2034 |
| 23 | 🇰🇷 KR | 1966 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1784 |
| 26 | 🇲🇦 MA | 1399 |
| 27 | 🇲🇪 ME | 1300 |
| 28 | 🇳🇱 NL | 1232 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1153 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2743 |
| 2 | Denver International Airport |  | US | 2233 |
| 3 | Tokyo International Airport |  | JP | 1856 |
| 4 | Indira Gandhi International Airport |  | IN | 1700 |
| 5 | Harry Reid International Airport |  | US | 1633 |
| 6 | Guaymaral Airport |  | CO | 1591 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1549 |
| 8 | Zurich Airport |  | CH | 1447 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1400 |
| 10 | La Aurora Airport |  | GT | 1379 |
| 11 | Frankfurt am Main International Airport |  | DE | 1327 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1271 |
| 13 | Chicago O'Hare International Airport |  | US | 1265 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1175 |
| 16 | Salt Lake City International Airport |  | US | 1166 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1125 |
| 18 | Madrid Barajas International Airport |  | ES | 1081 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1079 |
| 20 | Capua Airport |  | IT | 1077 |
| 21 | Congonhas Airport |  | BR | 1046 |
| 22 | Kuala Lumpur International Airport |  | MY | 1018 |
| 23 | Charlotte/Douglas International Airport |  | US | 976 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 952 |
| 25 | Charles de Gaulle International Airport |  | FR | 952 |
| 26 | Bengaluru International Airport |  | IN | 931 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 897 |
| 28 | Malpensa International Airport |  | IT | 879 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 822 |
| 31 | Barcelona International Airport |  | ES | 815 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 801 |
| 33 | Tenerife Norte Airport |  | ES | 793 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 772 |
| 35 | Calgary International Airport |  | CA | 767 |
| 36 | Seattle-Tacoma International Airport |  | US | 756 |
| 37 | Vitoria/Foronda Airport |  | ES | 754 |
| 38 | Viracopos International Airport |  | BR | 752 |
| 39 | Scottsdale Airport |  | US | 748 |
| 40 | Amsterdam Airport Schiphol |  | NL | 744 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 667 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 475 | 21m | 244 km | 2,000.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 328 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 317 | 1h 10m | 770 km | 4,211.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 249 | 26m | 275 km | 1,179.9 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 241 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 190 | 22m | 55 km | 180.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 184 | 44m | 241 km | 764.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 183 | 26m | 215 km | 677.8 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 178 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 173 | 1h 46m | 1,423 km | 4,245.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 162 | 18m | 144 km | 403.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 161 | 20m | 250 km | 695.4 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 158 | 44m | 452 km | 1,231.4 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 158 | 30m | 49 km | 133.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 153 | 54m | 136 km | 358.7 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 149 | 1h 38m | 1,156 km | 2,972.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 146 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG594 | BRG | Selawik Airport (PASK) | Ambler Airport (PAFM) | 2026-07-06 19:49 UTC | 2026-07-06 20:13 UTC | 23m |
| N4397Q |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-07-06 19:56 UTC | 2026-07-06 20:08 UTC | 12m |
| N341MA |  | Spirit Of St Louis Airport (KSUS) | KMO6 (KMO6) | 2026-07-06 19:05 UTC | 2026-07-06 20:03 UTC | 58m |
| AAL1528 | American Airlines | Los Angeles International Airport (KLAX) | Philadelphia International Airport (KPHL) | 2026-07-06 15:17 UTC | 2026-07-06 20:01 UTC | 4h 44m |
| N225CB |  | Riverside Airport (KRAL) | Santa Barbara Municipal Airport (KSBA) | 2026-07-06 18:49 UTC | 2026-07-06 20:01 UTC | 1h 11m |
| N595KW |  | Batesville Regional Airport (KBVX) | KL47 (KL47) | 2026-07-06 19:19 UTC | 2026-07-06 20:00 UTC | 41m |
| SJN5 | SJN | Decatur /Jones/ Airport (WA18) | Decatur Shores Airport (WN07) | 2026-07-06 19:56 UTC | 2026-07-06 19:58 UTC | 1m |
| N981CE |  | Washington Dulles International Airport (KIAD) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-07-06 18:56 UTC | 2026-07-06 19:57 UTC | 1h 1m |
| N9529G |  | Middletown Regional/Hook Field (KMWO) | Middletown Regional/Hook Field (KMWO) | 2026-07-06 19:39 UTC | 2026-07-06 19:56 UTC | 17m |
| SXS1EN | SXS | Antalya International Airport (LTAI) | UKFB (UKFB) | 2026-07-06 18:50 UTC | 2026-07-06 19:56 UTC | 1h 5m |
| N383SF |  | Mistwood Airport (24MO) | Kinsley Municipal Airport (K33K) | 2026-07-06 19:12 UTC | 2026-07-06 19:54 UTC | 41m |
| N610SP |  | San Carlos Airport (KSQL) | Hayward Executive Airport (KHWD) | 2026-07-06 19:42 UTC | 2026-07-06 19:54 UTC | 11m |
| TKR169 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-06 19:25 UTC | 2026-07-06 19:53 UTC | 28m |
| PRZTU | PRZ | Fazenda Flores Airport (SITL) | Fabrica Fortaleza Airport (SJDS) | 2026-07-06 19:39 UTC | 2026-07-06 19:53 UTC | 13m |
| ZKIKJ | ZKI | Auckland International Airport (NZAA) | Waiheke Reeve Airport (NZKE) | 2026-07-06 19:41 UTC | 2026-07-06 19:50 UTC | 8m |
| SIL1502 | SIL | King Salmon Airport (PAKN) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-06 18:41 UTC | 2026-07-06 19:48 UTC | 1h 7m |
| N320KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-06 18:53 UTC | 2026-07-06 19:46 UTC | 53m |
| LXJ261 | LXJ | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-06 18:57 UTC | 2026-07-06 19:46 UTC | 48m |
| N33CJ |  | Mefford Field (KTLR) | Big Bear City Airport (KL35) | 2026-07-06 19:16 UTC | 2026-07-06 19:46 UTC | 30m |
| N70846 |  | Ramona Airport (KRNM) | Desert Wings Sky Ranch Airport (04CL) | 2026-07-06 19:27 UTC | 2026-07-06 19:46 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
