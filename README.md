# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_13:39:42_UTC-green)

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

**Latest saved flight:** 2026-08-11 13:39:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 13:39:42 UTC

- **186,738** saved flights
- **59,237** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **186,738** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,241,440.0 tonnes** estimated CO2 emissions
- **129,938,550 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7422 |
| 2 | SkyWest Airlines | 6785 |
| 3 | EJA | 3678 |
| 4 | IndiGo | 3261 |
| 5 | Southwest Airlines | 2925 |
| 6 | American Airlines | 2903 |
| 7 | ENY | 2319 |
| 8 | Delta Air Lines | 2194 |
| 9 | LATAM Airlines | 1748 |
| 10 | AZU | 1675 |
| 11 | Lufthansa | 1640 |
| 12 | WIF | 1546 |
| 13 | Vueling | 1541 |
| 14 | LXJ | 1460 |
| 15 | easyJet | 1284 |
| 16 | Swiss International | 1276 |
| 17 | AXM | 1247 |
| 18 | EJU | 1154 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1027 |
| 23 | GLO | 998 |
| 24 | Air France | 971 |
| 25 | AEE | 966 |
| 26 | CXK | 960 |
| 27 | PGT | 958 |
| 28 | United Airlines | 952 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 925 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159196 |
| 2 | 🇪🇸 ES | 12026 |
| 3 | 🇧🇷 BR | 10706 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇮🇳 IN | 10223 |
| 6 | 🇨🇦 CA | 10184 |
| 7 | 🇮🇹 IT | 9675 |
| 8 | 🇩🇪 DE | 9248 |
| 9 | 🇬🇧 GB | 8694 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7480 |
| 12 | 🇨🇴 CO | 7045 |
| 13 | 🇬🇷 GR | 5481 |
| 14 | 🇲🇽 MX | 5321 |
| 15 | 🇨🇭 CH | 5013 |
| 16 | 🇹🇷 TR | 4921 |
| 17 | 🇳🇴 NO | 4806 |
| 18 | 🇲🇾 MY | 3262 |
| 19 | 🇿🇦 ZA | 3142 |
| 20 | 🇵🇱 PL | 3105 |
| 21 | 🇹🇭 TH | 2887 |
| 22 | 🇳🇿 NZ | 2666 |
| 23 | 🇵🇭 PH | 2471 |
| 24 | 🇬🇹 GT | 2375 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1902 |
| 27 | 🇭🇷 HR | 1892 |
| 28 | 🇲🇪 ME | 1677 |
| 29 | 🇳🇱 NL | 1670 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3867 |
| 2 | Denver International Airport |  | US | 3069 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2300 |
| 5 | Guaymaral Airport |  | CO | 2284 |
| 6 | Harry Reid International Airport |  | US | 2187 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1992 |
| 8 | Zurich Airport |  | CH | 1991 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1932 |
| 10 | La Aurora Airport |  | GT | 1822 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1695 |
| 12 | El Dorado International Airport |  | CO | 1675 |
| 13 | Salt Lake City International Airport |  | US | 1662 |
| 14 | Chicago O'Hare International Airport |  | US | 1653 |
| 15 | Frankfurt am Main International Airport |  | DE | 1609 |
| 16 | Congonhas Airport |  | BR | 1557 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1472 |
| 19 | Capua Airport |  | IT | 1459 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1454 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1389 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1335 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1286 |
| 25 | Charles de Gaulle International Airport |  | FR | 1276 |
| 26 | Charlotte/Douglas International Airport |  | US | 1256 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1206 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1167 |
| 30 | Ninoy Aquino International Airport |  | PH | 1166 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1143 |
| 32 | Barcelona International Airport |  | ES | 1110 |
| 33 | Seattle-Tacoma International Airport |  | US | 1074 |
| 34 | Reno/Tahoe International Airport |  | US | 1073 |
| 35 | Viracopos International Airport |  | BR | 1072 |
| 36 | Calgary International Airport |  | CA | 1059 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1044 |
| 39 | Tenerife Norte Airport |  | ES | 1024 |
| 40 | Vitoria/Foronda Airport |  | ES | 1012 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 941 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 432 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 329 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 313 | 27m | 275 km | 1,483.2 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 303 | 14m | 114 km | 594.3 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 280 | 44m | 241 km | 1,163.1 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 266 | 1h 49m | 1,423 km | 6,528.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 233 | 27m | 215 km | 862.9 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 221 | 1h 38m | 1,156 km | 4,408.9 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
|  |  | Jacksonville Nas (Towers Field) Airport (KNIP) | St Simons Island Airport (KSSI) | 2026-08-11 13:21 UTC | 2026-08-11 13:39 UTC | 18m |
| RANDOM41 | RAN | Laughlin Afb Aux Nr 1 Airport (KT70) | Dunbar Ranch Airport (0XS8) | 2026-08-11 13:24 UTC | 2026-08-11 13:37 UTC | 12m |
| DHXFV | DHX | Halle-Oppin Airport (EDAQ) | Halle-Oppin Airport (EDAQ) | 2026-08-11 12:37 UTC | 2026-08-11 13:35 UTC | 57m |
| THUD51 | THU | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-08-11 12:52 UTC | 2026-08-11 13:32 UTC | 40m |
| ERU450 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-08-11 13:19 UTC | 2026-08-11 13:32 UTC | 12m |
| N725ZN |  | Laramie Regional Airport (KLAR) | Laramie Regional Airport (KLAR) | 2026-08-11 13:15 UTC | 2026-08-11 13:32 UTC | 16m |
| ELY312 | ELY | London Luton Airport (EGGW) | Ben Gurion International Airport (LLBG) | 2026-08-11 09:09 UTC | 2026-08-11 13:28 UTC | 4h 19m |
| RTY284 | RTY | Northern Colorado Regional Airport (KFNL) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-08-11 12:41 UTC | 2026-08-11 13:18 UTC | 36m |
| N4431R |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-11 12:45 UTC | 2026-08-11 13:17 UTC | 31m |
| JEDI73 | JED | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Trent Lott International Airport (KPQL) | 2026-08-11 12:56 UTC | 2026-08-11 13:16 UTC | 20m |
| N8334N |  | Cottonwood Farm Airport (87VA) | Root Field (82VA) | 2026-08-11 13:02 UTC | 2026-08-11 13:13 UTC | 10m |
| FHDSA | FHD | Vannes-Meucon Airport (LFRV) | Vannes-Meucon Airport (LFRV) | 2026-08-11 12:51 UTC | 2026-08-11 13:13 UTC | 21m |
| N692CJ |  | Stones River Airport (7TN3) | Lebanon Municipal Airport (KM54) | 2026-08-11 12:23 UTC | 2026-08-11 13:11 UTC | 48m |
| DMSJU | DMS | Donaueschingen-Villingen Airport (EDTD) | Donaueschingen-Villingen Airport (EDTD) | 2026-08-11 12:58 UTC | 2026-08-11 13:08 UTC | 9m |
| BOXER04 | BOX | Bertani Ranch Airport (23TS) | J R Ranch Airport (15TA) | 2026-08-11 12:52 UTC | 2026-08-11 13:06 UTC | 14m |
| HBZEA | HBZ | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-08-11 12:56 UTC | 2026-08-11 13:06 UTC | 9m |
| SEKHP | SEK | Bielefeld Airport (EDLI) | Munster Osnabruck Airport (EDDG) | 2026-08-11 12:29 UTC | 2026-08-11 13:05 UTC | 35m |
| N525RA |  | Dane County Regional/Truax Field (KMSN) | 4WI2 (4WI2) | 2026-08-11 12:32 UTC | 2026-08-11 13:05 UTC | 32m |
| ZKIWG | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-11 12:35 UTC | 2026-08-11 13:03 UTC | 27m |
| DRAG381 | DRA | Grenoble Le Versoud Airport (LFLG) | Grenoble Le Versoud Airport (LFLG) | 2026-08-11 13:01 UTC | 2026-08-11 13:02 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
