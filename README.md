# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_21:26:19_UTC-green)

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

**Latest saved flight:** 2026-07-13 21:26:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 21:26:19 UTC

- **140,825** saved flights
- **47,349** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **140,825** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,691,321.7 tonnes** estimated CO2 emissions
- **98,047,634 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5740 |
| 2 | SkyWest Airlines | 5152 |
| 3 | EJA | 2779 |
| 4 | IndiGo | 2576 |
| 5 | American Airlines | 2235 |
| 6 | Southwest Airlines | 2118 |
| 7 | ENY | 1752 |
| 8 | Delta Air Lines | 1669 |
| 9 | Lufthansa | 1428 |
| 10 | LATAM Airlines | 1294 |
| 11 | Vueling | 1215 |
| 12 | AZU | 1211 |
| 13 | WIF | 1210 |
| 14 | LXJ | 1080 |
| 15 | AXM | 1048 |
| 16 | Swiss International | 1005 |
| 17 | easyJet | 921 |
| 18 | All Nippon Airways | 899 |
| 19 | Alaska Airlines | 886 |
| 20 | QLK | 877 |
| 21 | EJU | 868 |
| 22 | VIV | 775 |
| 23 | AEE | 756 |
| 24 | CXK | 756 |
| 25 | Air France | 754 |
| 26 | JetBlue | 744 |
| 27 | United Airlines | 735 |
| 28 | Cathay Pacific | 731 |
| 29 | MXY | 730 |
| 30 | GLO | 720 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 121088 |
| 2 | 🇪🇸 ES | 9236 |
| 3 | 🇮🇳 IN | 8068 |
| 4 | 🇦🇺 AU | 8021 |
| 5 | 🇧🇷 BR | 7952 |
| 6 | 🇨🇦 CA | 7391 |
| 7 | 🇮🇹 IT | 7357 |
| 8 | 🇩🇪 DE | 7332 |
| 9 | 🇬🇧 GB | 6433 |
| 10 | 🇯🇵 JP | 5895 |
| 11 | 🇫🇷 FR | 5610 |
| 12 | 🇨🇴 CO | 4472 |
| 13 | 🇲🇽 MX | 4083 |
| 14 | 🇬🇷 GR | 4014 |
| 15 | 🇳🇴 NO | 3785 |
| 16 | 🇨🇭 CH | 3660 |
| 17 | 🇹🇷 TR | 3330 |
| 18 | 🇲🇾 MY | 2731 |
| 19 | 🇵🇱 PL | 2358 |
| 20 | 🇿🇦 ZA | 2308 |
| 21 | 🇳🇿 NZ | 2144 |
| 22 | 🇹🇭 TH | 2110 |
| 23 | 🇰🇷 KR | 2013 |
| 24 | 🇵🇭 PH | 1906 |
| 25 | 🇬🇹 GT | 1863 |
| 26 | 🇲🇦 MA | 1479 |
| 27 | 🇲🇪 ME | 1401 |
| 28 | 🇳🇱 NL | 1327 |
| 29 | 🇭🇷 HR | 1277 |
| 30 | 🇲🇴 MO | 1190 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2906 |
| 2 | Denver International Airport |  | US | 2353 |
| 3 | Tokyo International Airport |  | JP | 1909 |
| 4 | Indira Gandhi International Airport |  | IN | 1787 |
| 5 | Harry Reid International Airport |  | US | 1758 |
| 6 | Guaymaral Airport |  | CO | 1715 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1619 |
| 8 | Zurich Airport |  | CH | 1571 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1477 |
| 10 | La Aurora Airport |  | GT | 1441 |
| 11 | Frankfurt am Main International Airport |  | DE | 1378 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1343 |
| 13 | Chicago O'Hare International Airport |  | US | 1325 |
| 14 | Salt Lake City International Airport |  | US | 1258 |
| 15 | El Dorado International Airport |  | CO | 1247 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1215 |
| 17 | Macau International Airport |  | MO | 1190 |
| 18 | Capua Airport |  | IT | 1156 |
| 19 | Madrid Barajas International Airport |  | ES | 1142 |
| 20 | Congonhas Airport |  | BR | 1133 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1126 |
| 22 | Kuala Lumpur International Airport |  | MY | 1057 |
| 23 | Charlotte/Douglas International Airport |  | US | 1023 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1011 |
| 25 | Charles de Gaulle International Airport |  | FR | 999 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 977 |
| 27 | Bengaluru International Airport |  | IN | 966 |
| 28 | Malpensa International Airport |  | IT | 914 |
| 29 | Ninoy Aquino International Airport |  | PH | 889 |
| 30 | Barcelona International Airport |  | ES | 861 |
| 31 | Daniel K Inouye International Airport |  | US | 860 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 859 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 828 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 809 |
| 36 | Viracopos International Airport |  | BR | 800 |
| 37 | Seattle-Tacoma International Airport |  | US | 800 |
| 38 | Amsterdam Airport Schiphol |  | NL | 800 |
| 39 | Scottsdale Airport |  | US | 799 |
| 40 | Vitoria/Foronda Airport |  | ES | 781 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 723 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 510 | 21m | 244 km | 2,147.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 344 | 24m | 225 km | 1,334.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 333 | 1h 9m | 770 km | 4,423.6 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 298 | 14m | 114 km | 584.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 207 | 22m | 55 km | 196.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 188 | 1h 46m | 1,423 km | 4,613.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 188 | 20m | 99 km | 322.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 186 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 176 | 20m | 250 km | 760.2 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 170 | 31m | 369 km | 1,082.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 170 | 18m | 144 km | 422.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 163 | 1h 16m | 961 km | 2,701.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 160 | 1h 38m | 1,156 km | 3,191.9 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 157 | 13m | - | - |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N66SB |  | San Carlos Airport (KSQL) | Tracy Municipal Airport (KTCY) | 2026-07-13 20:56 UTC | 2026-07-13 21:26 UTC | 29m |
| KSF34 | KSF | Kent State University Airport (K1G3) | Jetway Airport (61OH) | 2026-07-13 20:46 UTC | 2026-07-13 21:26 UTC | 39m |
| N3570E |  | Van Nuys Airport (KVNY) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-13 20:06 UTC | 2026-07-13 21:18 UTC | 1h 11m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-13 21:07 UTC | 2026-07-13 21:17 UTC | 10m |
| N303RF |  | Porter County Regional Airport (KVPZ) | Yates Airport (IL29) | 2026-07-13 20:50 UTC | 2026-07-13 21:13 UTC | 22m |
| STT5090 | STT | Lanai Airport (PHNY) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-07-13 20:48 UTC | 2026-07-13 21:09 UTC | 21m |
| N116 |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-13 20:48 UTC | 2026-07-13 21:01 UTC | 13m |
| N761TA |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-13 20:40 UTC | 2026-07-13 20:59 UTC | 19m |
| R21230 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-07-13 19:43 UTC | 2026-07-13 20:59 UTC | 1h 16m |
| N21J |  | Lakefront Airport (KNEW) | F L Braughton Airport (LA40) | 2026-07-13 20:37 UTC | 2026-07-13 20:57 UTC | 20m |
| LJY286 | LJY | Victoria International Airport (CYYJ) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-13 19:05 UTC | 2026-07-13 20:56 UTC | 1h 51m |
| N911KP |  | 0CA3 (0CA3) | Santa Ynez/Kunkle Field (KIZA) | 2026-07-13 20:44 UTC | 2026-07-13 20:54 UTC | 9m |
| N135CK |  | Cross Keys Airport (K17N) | Cross Keys Airport (K17N) | 2026-07-13 20:37 UTC | 2026-07-13 20:51 UTC | 13m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-07-13 20:00 UTC | 2026-07-13 20:49 UTC | 49m |
| N2128E |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-07-13 19:48 UTC | 2026-07-13 20:46 UTC | 57m |
| N855FC |  | Robertson Field (NC63) | Vancouver International Airport (CYVR) | 2026-07-13 15:48 UTC | 2026-07-13 20:44 UTC | 4h 56m |
| N103GR |  | King Salmon Airport (PAKN) | Spokane International Airport (KGEG) | 2026-07-13 17:05 UTC | 2026-07-13 20:44 UTC | 3h 38m |
| RENO71 | REN | Vance Afb Airport (KEND) | Sopwith Ldg Airport (OK56) | 2026-07-13 20:12 UTC | 2026-07-13 20:44 UTC | 31m |
| N5251B |  | Winchester Regional Airport (KOKV) | Frank Field (VA52) | 2026-07-13 20:13 UTC | 2026-07-13 20:43 UTC | 29m |
| N3504P |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-07-13 20:32 UTC | 2026-07-13 20:43 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
