# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_14:52:19_UTC-green)

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

**Latest saved flight:** 2026-08-10 14:52:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 14:52:19 UTC

- **184,165** saved flights
- **58,638** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **184,165** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,212,885.4 tonnes** estimated CO2 emissions
- **128,283,213 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7309 |
| 2 | SkyWest Airlines | 6686 |
| 3 | EJA | 3631 |
| 4 | IndiGo | 3231 |
| 5 | Southwest Airlines | 2883 |
| 6 | American Airlines | 2869 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2174 |
| 9 | LATAM Airlines | 1721 |
| 10 | AZU | 1653 |
| 11 | Lufthansa | 1625 |
| 12 | WIF | 1526 |
| 13 | Vueling | 1521 |
| 14 | LXJ | 1451 |
| 15 | easyJet | 1265 |
| 16 | Swiss International | 1264 |
| 17 | AXM | 1235 |
| 18 | QLK | 1135 |
| 19 | EJU | 1133 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1015 |
| 23 | GLO | 985 |
| 24 | AEE | 958 |
| 25 | CXK | 955 |
| 26 | Air France | 954 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 941 |
| 29 | PGT | 938 |
| 30 | MXY | 916 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 157243 |
| 2 | 🇪🇸 ES | 11840 |
| 3 | 🇧🇷 BR | 10567 |
| 4 | 🇦🇺 AU | 10306 |
| 5 | 🇮🇳 IN | 10120 |
| 6 | 🇨🇦 CA | 10018 |
| 7 | 🇮🇹 IT | 9522 |
| 8 | 🇩🇪 DE | 9119 |
| 9 | 🇬🇧 GB | 8554 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7362 |
| 12 | 🇨🇴 CO | 6894 |
| 13 | 🇬🇷 GR | 5403 |
| 14 | 🇲🇽 MX | 5257 |
| 15 | 🇨🇭 CH | 4934 |
| 16 | 🇹🇷 TR | 4805 |
| 17 | 🇳🇴 NO | 4743 |
| 18 | 🇲🇾 MY | 3219 |
| 19 | 🇿🇦 ZA | 3084 |
| 20 | 🇵🇱 PL | 3082 |
| 21 | 🇹🇭 TH | 2860 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2439 |
| 24 | 🇬🇹 GT | 2360 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1858 |
| 27 | 🇭🇷 HR | 1847 |
| 28 | 🇲🇪 ME | 1663 |
| 29 | 🇳🇱 NL | 1651 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2267 |
| 5 | Guaymaral Airport |  | CO | 2245 |
| 6 | Harry Reid International Airport |  | US | 2153 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1975 |
| 8 | Zurich Airport |  | CH | 1974 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1910 |
| 10 | La Aurora Airport |  | GT | 1810 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1649 |
| 13 | Salt Lake City International Airport |  | US | 1639 |
| 14 | Chicago O'Hare International Airport |  | US | 1638 |
| 15 | Frankfurt am Main International Airport |  | DE | 1591 |
| 16 | Congonhas Airport |  | BR | 1531 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 19 | Madrid Barajas International Airport |  | ES | 1447 |
| 20 | Capua Airport |  | IT | 1444 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1317 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1273 |
| 25 | Charles de Gaulle International Airport |  | FR | 1255 |
| 26 | Charlotte/Douglas International Airport |  | US | 1247 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1200 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1151 |
| 30 | Ninoy Aquino International Airport |  | PH | 1150 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1092 |
| 33 | Viracopos International Airport |  | BR | 1060 |
| 34 | Seattle-Tacoma International Airport |  | US | 1057 |
| 35 | Reno/Tahoe International Airport |  | US | 1050 |
| 36 | Calgary International Airport |  | CA | 1049 |
| 37 | Daniel K Inouye International Airport |  | US | 1047 |
| 38 | Oslo Gardermoen Airport |  | NO | 1026 |
| 39 | Tenerife Norte Airport |  | ES | 1005 |
| 40 | Amsterdam Airport Schiphol |  | NL | 996 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 926 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 675 | 21m | 244 km | 2,842.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 428 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 309 | 27m | 275 km | 1,464.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 274 | 44m | 241 km | 1,138.1 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 269 | 22m | 55 km | 255.7 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 260 | 1h 49m | 1,423 km | 6,380.8 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 258 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 221 | 19m | 144 km | 549.7 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 218 | 1h 38m | 1,156 km | 4,349.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 217 | 24m | 218 km | 817.5 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6279V |  | Reedville Airport (VA98) | Federhart-Ophelia Airport (VA99) | 2026-08-10 14:16 UTC | 2026-08-10 14:52 UTC | 35m |
| N49TT |  | Creech Afb Airport (KINS) | Creech Afb Airport (KINS) | 2026-08-10 14:36 UTC | 2026-08-10 14:47 UTC | 11m |
| N755K |  | Centennial Airport (KAPA) | Chaparral Airport (CO18) | 2026-08-10 14:30 UTC | 2026-08-10 14:47 UTC | 17m |
| N278DS |  | York Airport (KTHV) | 1PA9 (1PA9) | 2026-08-10 14:19 UTC | 2026-08-10 14:44 UTC | 25m |
| N929CD |  | Rocky Mountain Metro Airport (KBJC) | Greeley-Weld County Airport (KGXY) | 2026-08-10 14:07 UTC | 2026-08-10 14:44 UTC | 37m |
| N92XF |  | Pompano Beach Airpark (KPMP) | Pompano Beach Airpark (KPMP) | 2026-08-10 14:26 UTC | 2026-08-10 14:42 UTC | 15m |
| SYERTN3 | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-08-10 14:13 UTC | 2026-08-10 14:40 UTC | 27m |
| XBJOR | XBJ | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-08-10 13:57 UTC | 2026-08-10 14:35 UTC | 38m |
| ENSAIO73 | ENS | Fazenda Fittipaldi Citrus Airport (SDFF) | Mirassol Airport (SDMH) | 2026-08-10 13:56 UTC | 2026-08-10 14:33 UTC | 37m |
| N525JN |  | Salinas Municipal Airport (KSNS) | K36U (K36U) | 2026-08-10 13:07 UTC | 2026-08-10 14:33 UTC | 1h 25m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-08-10 13:48 UTC | 2026-08-10 14:31 UTC | 42m |
| WIF3LA | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-08-10 13:38 UTC | 2026-08-10 14:31 UTC | 52m |
| N156WL |  | St Paul Downtown Holman Field (KSTP) | Voyager Village Airstrip (9WN2) | 2026-08-10 14:07 UTC | 2026-08-10 14:28 UTC | 20m |
| FTO381 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-10 13:57 UTC | 2026-08-10 14:27 UTC | 29m |
| N165EA |  | Carson City Airport (KCXP) | Carson City Airport (KCXP) | 2026-08-10 14:17 UTC | 2026-08-10 14:23 UTC | 6m |
| XCDPF | XCD | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-08-10 13:43 UTC | 2026-08-10 14:23 UTC | 40m |
| A7GQB |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-10 12:06 UTC | 2026-08-10 14:23 UTC | 2h 16m |
| N3BA |  | Smyrna Airport (KMQY) | Auburn University Regional Airport (KAUO) | 2026-08-10 13:33 UTC | 2026-08-10 14:23 UTC | 49m |
| CXK454 | CXK | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-08-10 13:15 UTC | 2026-08-10 14:21 UTC | 1h 6m |
| N49TT |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-08-10 13:59 UTC | 2026-08-10 14:19 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
