# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_11:21:33_UTC-green)

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

**Latest saved flight:** 2026-08-09 11:21:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 11:21:33 UTC

- **180,825** saved flights
- **57,814** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,825** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,174,142.6 tonnes** estimated CO2 emissions
- **126,037,254 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7160 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3170 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2817 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1680 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1610 |
| 12 | Vueling | 1497 |
| 13 | WIF | 1497 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1238 |
| 16 | Swiss International | 1235 |
| 17 | AXM | 1225 |
| 18 | QLK | 1116 |
| 19 | EJU | 1107 |
| 20 | All Nippon Airways | 1106 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 996 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 945 |
| 27 | Air France | 935 |
| 28 | United Airlines | 929 |
| 29 | PGT | 906 |
| 30 | MXY | 905 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154737 |
| 2 | 🇪🇸 ES | 11629 |
| 3 | 🇧🇷 BR | 10345 |
| 4 | 🇦🇺 AU | 10198 |
| 5 | 🇮🇳 IN | 9936 |
| 6 | 🇨🇦 CA | 9854 |
| 7 | 🇮🇹 IT | 9349 |
| 8 | 🇩🇪 DE | 8946 |
| 9 | 🇬🇧 GB | 8359 |
| 10 | 🇯🇵 JP | 7361 |
| 11 | 🇫🇷 FR | 7202 |
| 12 | 🇨🇴 CO | 6707 |
| 13 | 🇬🇷 GR | 5293 |
| 14 | 🇲🇽 MX | 5164 |
| 15 | 🇨🇭 CH | 4829 |
| 16 | 🇳🇴 NO | 4657 |
| 17 | 🇹🇷 TR | 4640 |
| 18 | 🇲🇾 MY | 3193 |
| 19 | 🇵🇱 PL | 3037 |
| 20 | 🇿🇦 ZA | 2966 |
| 21 | 🇹🇭 TH | 2775 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2401 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2260 |
| 26 | 🇲🇦 MA | 1823 |
| 27 | 🇭🇷 HR | 1800 |
| 28 | 🇲🇪 ME | 1642 |
| 29 | 🇳🇱 NL | 1625 |
| 30 | 🇲🇴 MO | 1516 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3732 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2283 |
| 4 | Guaymaral Airport |  | CO | 2223 |
| 5 | Indira Gandhi International Airport |  | IN | 2220 |
| 6 | Harry Reid International Airport |  | US | 2127 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1946 |
| 8 | Zurich Airport |  | CH | 1926 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1616 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1570 |
| 16 | Macau International Airport |  | MO | 1516 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1437 |
| 19 | Madrid Barajas International Airport |  | ES | 1421 |
| 20 | Capua Airport |  | IT | 1415 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1351 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1285 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1247 |
| 25 | Charles de Gaulle International Airport |  | FR | 1230 |
| 26 | Charlotte/Douglas International Airport |  | US | 1224 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1179 |
| 29 | Ninoy Aquino International Airport |  | PH | 1131 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1122 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1077 |
| 33 | Seattle-Tacoma International Airport |  | US | 1041 |
| 34 | Daniel K Inouye International Airport |  | US | 1040 |
| 35 | Viracopos International Airport |  | BR | 1036 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1000 |
| 39 | Tenerife Norte Airport |  | ES | 990 |
| 40 | Amsterdam Airport Schiphol |  | NL | 978 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 669 | 21m | 244 km | 2,817.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 432 | 1h 8m | 770 km | 5,738.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 304 | 27m | 275 km | 1,440.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 254 | 1h 48m | 1,423 km | 6,233.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 238 | 20m | 250 km | 1,028.0 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 228 | 26m | 215 km | 844.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 216 | 19m | 144 km | 537.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 213 | 1h 38m | 1,156 km | 4,249.3 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 210 | 31m | 369 km | 1,336.7 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 208 | 24m | 218 km | 783.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GFBPS | GFB | EG32 (EG32) | EG32 (EG32) | 2026-08-09 10:05 UTC | 2026-08-09 11:21 UTC | 1h 15m |
| NSZ3630 | NSZ | Copenhagen Kastrup Airport (EKCH) | Mollis Airport (LSZM) | 2026-08-09 09:52 UTC | 2026-08-09 11:18 UTC | 1h 25m |
| N75200 |  | Pompano Beach Airpark (KPMP) | Palm Beach County Park Airport (KLNA) | 2026-08-09 11:00 UTC | 2026-08-09 11:16 UTC | 15m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 10:54 UTC | 2026-08-09 11:08 UTC | 13m |
| DHXCF | DHX | ETIN (ETIN) | Hettstadt Airport (EDGH) | 2026-08-09 10:52 UTC | 2026-08-09 11:07 UTC | 15m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-08-09 10:20 UTC | 2026-08-09 11:05 UTC | 44m |
| NSZ4312 | NSZ | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-08-09 09:05 UTC | 2026-08-09 11:04 UTC | 1h 59m |
| DLH1RF | Lufthansa | Munich International Airport (EDDM) | Frankfurt am Main International Airport (EDDF) | 2026-08-09 10:31 UTC | 2026-08-09 11:03 UTC | 31m |
| SPVAN | SPV | Włocławek-Kruszyn Airport (EPWK) | Włocławek-Kruszyn Airport (EPWK) | 2026-08-09 10:09 UTC | 2026-08-09 11:02 UTC | 52m |
| JA01HR |  | Shikabe Airport (RJ04) | Hakodate Airport (RJCH) | 2026-08-09 10:44 UTC | 2026-08-09 10:57 UTC | 12m |
| CTN756R | CTN | Dubrovnik Airport (LDDU) | Zurich Airport (LSZH) | 2026-08-09 09:21 UTC | 2026-08-09 10:52 UTC | 1h 30m |
| DLH4P | Lufthansa | Václav Havel Airport (LKPR) | Frankfurt am Main International Airport (EDDF) | 2026-08-09 10:01 UTC | 2026-08-09 10:51 UTC | 50m |
| GAWGB | GAW | Deanland Lewes Airport (EGKL) | Deanland Lewes Airport (EGKL) | 2026-08-09 10:29 UTC | 2026-08-09 10:46 UTC | 16m |
| AM319 |  | Melbourne Essendon Airport (YMEN) | West Sale Airport (YWSL) | 2026-08-09 10:20 UTC | 2026-08-09 10:46 UTC | 26m |
| THY6889 | Turkish Airlines | Istanbul Airport (LTFM) | Bezymyanka Airfield (UWWG) | 2026-08-09 07:20 UTC | 2026-08-09 10:42 UTC | 3h 21m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 10:25 UTC | 2026-08-09 10:39 UTC | 14m |
| THY6208 | Turkish Airlines | Istanbul Airport (LTFM) | Gelendzhik Airport (URKG) | 2026-08-09 09:34 UTC | 2026-08-09 10:37 UTC | 1h 2m |
| SLG2 | SLG | Saskatoon John G. Diefenbaker International Airport (CYXE) | Leoville Airport (CJT9) | 2026-08-09 10:04 UTC | 2026-08-09 10:34 UTC | 29m |
| DLH1WC | Lufthansa | Munich International Airport (EDDM) | Sochaczew Airport (EPSO) | 2026-08-09 09:15 UTC | 2026-08-09 10:32 UTC | 1h 17m |
| FD542 |  | Adelaide International Airport (YPAD) | YCVA (YCVA) | 2026-08-09 10:03 UTC | 2026-08-09 10:31 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
