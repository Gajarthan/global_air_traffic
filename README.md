# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_21:52:21_UTC-green)

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

**Latest saved flight:** 2026-07-05 21:52:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 21:52:21 UTC

- **130,420** saved flights
- **44,358** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **130,420** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,573,763.2 tonnes** estimated CO2 emissions
- **91,232,652 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5309 |
| 2 | SkyWest Airlines | 4832 |
| 3 | EJA | 2559 |
| 4 | IndiGo | 2443 |
| 5 | American Airlines | 2014 |
| 6 | Southwest Airlines | 1967 |
| 7 | ENY | 1641 |
| 8 | Delta Air Lines | 1565 |
| 9 | Lufthansa | 1368 |
| 10 | LATAM Airlines | 1188 |
| 11 | Vueling | 1154 |
| 12 | WIF | 1138 |
| 13 | AZU | 1107 |
| 14 | AXM | 1009 |
| 15 | LXJ | 1007 |
| 16 | Swiss International | 910 |
| 17 | All Nippon Airways | 860 |
| 18 | Alaska Airlines | 837 |
| 19 | easyJet | 836 |
| 20 | QLK | 817 |
| 21 | EJU | 805 |
| 22 | VIV | 722 |
| 23 | Cathay Pacific | 713 |
| 24 | Air France | 709 |
| 25 | AEE | 708 |
| 26 | CXK | 697 |
| 27 | United Airlines | 695 |
| 28 | JetBlue | 683 |
| 29 | MXY | 680 |
| 30 | GLO | 669 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 111717 |
| 2 | 🇪🇸 ES | 8695 |
| 3 | 🇮🇳 IN | 7654 |
| 4 | 🇦🇺 AU | 7523 |
| 5 | 🇧🇷 BR | 7331 |
| 6 | 🇨🇦 CA | 6888 |
| 7 | 🇩🇪 DE | 6846 |
| 8 | 🇮🇹 IT | 6818 |
| 9 | 🇬🇧 GB | 5801 |
| 10 | 🇯🇵 JP | 5624 |
| 11 | 🇫🇷 FR | 5185 |
| 12 | 🇨🇴 CO | 4102 |
| 13 | 🇲🇽 MX | 3810 |
| 14 | 🇬🇷 GR | 3721 |
| 15 | 🇳🇴 NO | 3538 |
| 16 | 🇨🇭 CH | 3350 |
| 17 | 🇹🇷 TR | 2875 |
| 18 | 🇲🇾 MY | 2616 |
| 19 | 🇿🇦 ZA | 2159 |
| 20 | 🇵🇱 PL | 2144 |
| 21 | 🇳🇿 NZ | 2080 |
| 22 | 🇹🇭 TH | 2014 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1813 |
| 25 | 🇬🇹 GT | 1773 |
| 26 | 🇲🇦 MA | 1394 |
| 27 | 🇲🇪 ME | 1295 |
| 28 | 🇳🇱 NL | 1226 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1144 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2723 |
| 2 | Denver International Airport |  | US | 2212 |
| 3 | Tokyo International Airport |  | JP | 1851 |
| 4 | Indira Gandhi International Airport |  | IN | 1690 |
| 5 | Harry Reid International Airport |  | US | 1621 |
| 6 | Guaymaral Airport |  | CO | 1587 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1539 |
| 8 | Zurich Airport |  | CH | 1438 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1390 |
| 10 | La Aurora Airport |  | GT | 1372 |
| 11 | Frankfurt am Main International Airport |  | DE | 1324 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1265 |
| 13 | Chicago O'Hare International Airport |  | US | 1254 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1160 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1108 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1073 |
| 19 | Madrid Barajas International Airport |  | ES | 1070 |
| 20 | Capua Airport |  | IT | 1069 |
| 21 | Congonhas Airport |  | BR | 1037 |
| 22 | Kuala Lumpur International Airport |  | MY | 1015 |
| 23 | Charlotte/Douglas International Airport |  | US | 973 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 950 |
| 25 | Charles de Gaulle International Airport |  | FR | 945 |
| 26 | Bengaluru International Airport |  | IN | 926 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 882 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 841 |
| 30 | Daniel K Inouye International Airport |  | US | 820 |
| 31 | Barcelona International Airport |  | ES | 809 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 795 |
| 33 | Tenerife Norte Airport |  | ES | 792 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 765 |
| 35 | Calgary International Airport |  | CA | 761 |
| 36 | Seattle-Tacoma International Airport |  | US | 750 |
| 37 | Vitoria/Foronda Airport |  | ES | 750 |
| 38 | Scottsdale Airport |  | US | 747 |
| 39 | Viracopos International Airport |  | BR | 746 |
| 40 | Amsterdam Airport Schiphol |  | NL | 742 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 666 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 473 | 21m | 244 km | 1,991.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 327 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 315 | 1h 10m | 770 km | 4,184.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 240 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 183 | 44m | 241 km | 760.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 174 | 27m | 152 km | 454.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 169 | 1h 45m | 1,423 km | 4,147.5 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 160 | 20m | 250 km | 691.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 160 | 18m | 144 km | 398.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 156 | 30m | 49 km | 131.9 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 150 | 54m | 136 km | 351.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 146 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9588V |  | Draughon-Miller Central Texas Regional Airport (KTPL) | Stampede Valley Airport (6TS4) | 2026-07-05 21:23 UTC | 2026-07-05 21:52 UTC | 28m |
| N6731P |  | Vance Brand Airport (KLMO) | Laramie Regional Airport (KLAR) | 2026-07-05 21:13 UTC | 2026-07-05 21:48 UTC | 34m |
| N4393Z |  | Ted Stevens Anchorage International Airport (PANC) | Grand Home Airport (AK99) | 2026-07-05 20:47 UTC | 2026-07-05 21:47 UTC | 59m |
| DLH8P | Lufthansa | Munich International Airport (EDDM) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-05 13:45 UTC | 2026-07-05 21:45 UTC | 8h 0m |
| N779SH |  | Portland-Troutdale Airport (KTTD) | 74OR (74OR) | 2026-07-05 21:04 UTC | 2026-07-05 21:41 UTC | 36m |
| N182KQ |  | 61WA (61WA) | Boeing Field/King County International Airport (KBFI) | 2026-07-05 21:13 UTC | 2026-07-05 21:38 UTC | 25m |
| TKR168 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | Animas Air Park (K00C) | 2026-07-05 20:23 UTC | 2026-07-05 21:35 UTC | 1h 11m |
| N125CL |  | Green Valley Airfield (WA25) | Easton State Airport (KESW) | 2026-07-05 20:49 UTC | 2026-07-05 21:34 UTC | 45m |
| DAL257 | Delta Air Lines | Amsterdam Airport Schiphol (EHAM) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-05 14:16 UTC | 2026-07-05 21:34 UTC | 7h 17m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Kenai Municipal Airport (PAEN) | 2026-07-05 20:09 UTC | 2026-07-05 21:33 UTC | 1h 23m |
| TKR184 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-07-05 20:54 UTC | 2026-07-05 21:31 UTC | 37m |
| UAL2644 | United Airlines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-05 21:07 UTC | 2026-07-05 21:30 UTC | 22m |
| POL21 | POL | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-07-05 21:01 UTC | 2026-07-05 21:27 UTC | 26m |
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-07-05 20:53 UTC | 2026-07-05 21:26 UTC | 32m |
| TKR101 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-07-05 20:54 UTC | 2026-07-05 21:22 UTC | 27m |
| STT5002 | STT | Lanai Airport (PHNY) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-07-05 20:57 UTC | 2026-07-05 21:21 UTC | 24m |
| N202RL |  | Nantucket Memorial Airport (KACK) | Ashford Field (7TX9) | 2026-07-05 17:44 UTC | 2026-07-05 21:18 UTC | 3h 33m |
| IJA309 | IJA | Centennial Airport (KAPA) | Granite Mountain Lodge Airport (CO11) | 2026-07-05 20:45 UTC | 2026-07-05 21:17 UTC | 32m |
| N667LB |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-07-05 20:28 UTC | 2026-07-05 21:13 UTC | 45m |
| EJA449 | EJA | Mud Lake/West Jefferson County Airport (K1U2) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-05 19:14 UTC | 2026-07-05 21:11 UTC | 1h 56m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
