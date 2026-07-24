# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_23:58:51_UTC-green)

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

**Latest saved flight:** 2026-07-23 23:58:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 23:58:51 UTC

- **147,006** saved flights
- **49,149** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **147,006** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,761,389.3 tonnes** estimated CO2 emissions
- **102,109,523 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5944 |
| 2 | SkyWest Airlines | 5399 |
| 3 | EJA | 2913 |
| 4 | IndiGo | 2645 |
| 5 | American Airlines | 2347 |
| 6 | Southwest Airlines | 2225 |
| 7 | ENY | 1832 |
| 8 | Delta Air Lines | 1745 |
| 9 | Lufthansa | 1450 |
| 10 | LATAM Airlines | 1354 |
| 11 | AZU | 1268 |
| 12 | Vueling | 1245 |
| 13 | WIF | 1245 |
| 14 | LXJ | 1134 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1037 |
| 17 | easyJet | 947 |
| 18 | All Nippon Airways | 933 |
| 19 | Alaska Airlines | 922 |
| 20 | QLK | 916 |
| 21 | EJU | 900 |
| 22 | VIV | 817 |
| 23 | CXK | 788 |
| 24 | AEE | 777 |
| 25 | JetBlue | 773 |
| 26 | Cathay Pacific | 771 |
| 27 | Air France | 770 |
| 28 | MXY | 770 |
| 29 | United Airlines | 765 |
| 30 | GLO | 761 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 126972 |
| 2 | 🇪🇸 ES | 9501 |
| 3 | 🇦🇺 AU | 8371 |
| 4 | 🇧🇷 BR | 8304 |
| 5 | 🇮🇳 IN | 8285 |
| 6 | 🇨🇦 CA | 7876 |
| 7 | 🇮🇹 IT | 7620 |
| 8 | 🇩🇪 DE | 7537 |
| 9 | 🇬🇧 GB | 6687 |
| 10 | 🇯🇵 JP | 6106 |
| 11 | 🇫🇷 FR | 5817 |
| 12 | 🇨🇴 CO | 4877 |
| 13 | 🇲🇽 MX | 4275 |
| 14 | 🇬🇷 GR | 4157 |
| 15 | 🇳🇴 NO | 3908 |
| 16 | 🇨🇭 CH | 3818 |
| 17 | 🇹🇷 TR | 3440 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2468 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2231 |
| 22 | 🇹🇭 TH | 2141 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1947 |
| 25 | 🇬🇹 GT | 1908 |
| 26 | 🇲🇦 MA | 1514 |
| 27 | 🇲🇪 ME | 1454 |
| 28 | 🇳🇱 NL | 1364 |
| 29 | 🇭🇷 HR | 1337 |
| 30 | 🇲🇴 MO | 1227 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3035 |
| 2 | Denver International Airport |  | US | 2468 |
| 3 | Tokyo International Airport |  | JP | 1963 |
| 4 | Indira Gandhi International Airport |  | IN | 1841 |
| 5 | Harry Reid International Airport |  | US | 1836 |
| 6 | Guaymaral Airport |  | CO | 1812 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1659 |
| 8 | Zurich Airport |  | CH | 1614 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1550 |
| 10 | La Aurora Airport |  | GT | 1479 |
| 11 | Frankfurt am Main International Airport |  | DE | 1401 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1383 |
| 13 | Chicago O'Hare International Airport |  | US | 1367 |
| 14 | Salt Lake City International Airport |  | US | 1327 |
| 15 | El Dorado International Airport |  | CO | 1320 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1274 |
| 17 | Macau International Airport |  | MO | 1227 |
| 18 | Capua Airport |  | IT | 1190 |
| 19 | Congonhas Airport |  | BR | 1185 |
| 20 | Madrid Barajas International Airport |  | ES | 1169 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1153 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1056 |
| 24 | Charlotte/Douglas International Airport |  | US | 1050 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1030 |
| 26 | Charles de Gaulle International Airport |  | FR | 1016 |
| 27 | Bengaluru International Airport |  | IN | 991 |
| 28 | Malpensa International Airport |  | IT | 946 |
| 29 | Ninoy Aquino International Airport |  | PH | 909 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 898 |
| 31 | Barcelona International Airport |  | ES | 889 |
| 32 | Daniel K Inouye International Airport |  | US | 884 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 883 |
| 34 | Seattle-Tacoma International Airport |  | US | 846 |
| 35 | Tenerife Norte Airport |  | ES | 844 |
| 36 | Calgary International Airport |  | CA | 841 |
| 37 | Scottsdale Airport |  | US | 833 |
| 38 | Viracopos International Airport |  | BR | 832 |
| 39 | Amsterdam Airport Schiphol |  | NL | 824 |
| 40 | Oslo Gardermoen Airport |  | NO | 809 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 764 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 533 | 21m | 244 km | 2,244.3 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 356 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 354 | 24m | 225 km | 1,373.4 t |
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
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 172 | 1h 16m | 961 km | 2,851.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 170 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MRA633 | MRA | Durant Regional/Eaker Field (KDUA) | Mc Alester Regional Airport (KMLC) | 2026-07-23 23:33 UTC | 2026-07-23 23:58 UTC | 25m |
| GNJ | GNJ | Sydney Bankstown Airport (YSBK) | Cessnock Airport (YCNK) | 2026-07-23 23:14 UTC | 2026-07-23 23:56 UTC | 41m |
| N442AD |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-07-23 22:37 UTC | 2026-07-23 23:51 UTC | 1h 13m |
| CPA662 | Cathay Pacific | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-07-23 20:40 UTC | 2026-07-23 23:47 UTC | 3h 6m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Agua Dulce Airport (KL70) | 2026-07-23 23:10 UTC | 2026-07-23 23:45 UTC | 34m |
| N132CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-07-23 22:44 UTC | 2026-07-23 23:43 UTC | 58m |
| ICL851 | ICL | Ben Gurion International Airport (LLBG) | Macau International Airport (VMMC) | 2026-07-23 14:38 UTC | 2026-07-23 23:35 UTC | 8h 57m |
| CFR82 | CFR | Kistler Ranch Airport (08CL) | 6CL9 (6CL9) | 2026-07-23 23:10 UTC | 2026-07-23 23:31 UTC | 21m |
| RMRNR11 | RMR | San Clemente Island Nalf Airport (KNUC) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-23 22:49 UTC | 2026-07-23 23:30 UTC | 41m |
| N246AM |  | University Of Illinois/Willard Airport (KCMI) | Frasca Field (KC16) | 2026-07-23 23:25 UTC | 2026-07-23 23:30 UTC | 4m |
| AAL1942 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Laguardia Airport (KLGA) | 2026-07-23 21:59 UTC | 2026-07-23 23:28 UTC | 1h 28m |
| ZJF | ZJF | Bacchus Marsh Airport (YBSS) | Melbourne Moorabbin Airport (YMMB) | 2026-07-23 23:06 UTC | 2026-07-23 23:27 UTC | 21m |
| N15CT |  | Grand Haven Memorial Airpark (K3GM) | Grand Haven Memorial Airpark (K3GM) | 2026-07-23 23:12 UTC | 2026-07-23 23:27 UTC | 15m |
| PPX | PPX | Brisbane Archerfield Airport (YBAF) | Sunshine Coast Airport (YBMC) | 2026-07-23 22:35 UTC | 2026-07-23 23:24 UTC | 48m |
| N95ER |  | Oakland County International Airport (KPTK) | Lakes Of The North Airport (K4Y4) | 2026-07-23 22:45 UTC | 2026-07-23 23:23 UTC | 38m |
| AXEL21 | AXE | Robert Gray Army Air Field (KGRK) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-23 19:45 UTC | 2026-07-23 23:22 UTC | 3h 37m |
| UPS5012 | UPS | Ontario International Airport (KONT) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-23 18:24 UTC | 2026-07-23 23:20 UTC | 4h 55m |
| N445D |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-07-23 22:41 UTC | 2026-07-23 23:19 UTC | 38m |
| N39FE |  | Mc Ghee Tyson Airport (KTYS) | The Bluffs Airport (75AR) | 2026-07-23 22:19 UTC | 2026-07-23 23:17 UTC | 58m |
| CFR83 | CFR | Kistler Ranch Airport (08CL) | 6CL9 (6CL9) | 2026-07-23 23:01 UTC | 2026-07-23 23:16 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
