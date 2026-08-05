# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_14:14:34_UTC-green)

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

**Latest saved flight:** 2026-08-05 14:14:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 14:14:34 UTC

- **172,215** saved flights
- **55,921** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **172,215** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,076,440.4 tonnes** estimated CO2 emissions
- **120,373,356 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6846 |
| 2 | SkyWest Airlines | 6294 |
| 3 | EJA | 3415 |
| 4 | IndiGo | 3024 |
| 5 | Southwest Airlines | 2712 |
| 6 | American Airlines | 2708 |
| 7 | ENY | 2141 |
| 8 | Delta Air Lines | 2045 |
| 9 | LATAM Airlines | 1592 |
| 10 | Lufthansa | 1573 |
| 11 | AZU | 1519 |
| 12 | WIF | 1439 |
| 13 | Vueling | 1417 |
| 14 | LXJ | 1345 |
| 15 | AXM | 1184 |
| 16 | Swiss International | 1170 |
| 17 | easyJet | 1166 |
| 18 | QLK | 1055 |
| 19 | EJU | 1052 |
| 20 | Alaska Airlines | 1051 |
| 21 | All Nippon Airways | 1045 |
| 22 | VIV | 948 |
| 23 | Cathay Pacific | 932 |
| 24 | CXK | 918 |
| 25 | GLO | 903 |
| 26 | United Airlines | 902 |
| 27 | AEE | 897 |
| 28 | Air France | 883 |
| 29 | MXY | 874 |
| 30 | JetBlue | 862 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 148298 |
| 2 | 🇪🇸 ES | 11032 |
| 3 | 🇧🇷 BR | 9788 |
| 4 | 🇦🇺 AU | 9642 |
| 5 | 🇮🇳 IN | 9480 |
| 6 | 🇨🇦 CA | 9413 |
| 7 | 🇮🇹 IT | 8898 |
| 8 | 🇩🇪 DE | 8560 |
| 9 | 🇬🇧 GB | 7979 |
| 10 | 🇯🇵 JP | 6936 |
| 11 | 🇫🇷 FR | 6830 |
| 12 | 🇨🇴 CO | 6295 |
| 13 | 🇬🇷 GR | 5006 |
| 14 | 🇲🇽 MX | 4923 |
| 15 | 🇨🇭 CH | 4540 |
| 16 | 🇳🇴 NO | 4487 |
| 17 | 🇹🇷 TR | 4225 |
| 18 | 🇲🇾 MY | 3081 |
| 19 | 🇵🇱 PL | 2885 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2527 |
| 22 | 🇳🇿 NZ | 2498 |
| 23 | 🇵🇭 PH | 2277 |
| 24 | 🇬🇹 GT | 2204 |
| 25 | 🇰🇷 KR | 2169 |
| 26 | 🇲🇦 MA | 1732 |
| 27 | 🇭🇷 HR | 1665 |
| 28 | 🇲🇪 ME | 1580 |
| 29 | 🇳🇱 NL | 1558 |
| 30 | 🇲🇴 MO | 1488 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3548 |
| 2 | Denver International Airport |  | US | 2850 |
| 3 | Tokyo International Airport |  | JP | 2171 |
| 4 | Guaymaral Airport |  | CO | 2136 |
| 5 | Indira Gandhi International Airport |  | IN | 2108 |
| 6 | Harry Reid International Airport |  | US | 2065 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1875 |
| 8 | Zurich Airport |  | CH | 1818 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1806 |
| 10 | La Aurora Airport |  | GT | 1701 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1591 |
| 12 | El Dorado International Airport |  | CO | 1560 |
| 13 | Chicago O'Hare International Airport |  | US | 1560 |
| 14 | Salt Lake City International Airport |  | US | 1542 |
| 15 | Frankfurt am Main International Airport |  | DE | 1534 |
| 16 | Macau International Airport |  | MO | 1488 |
| 17 | Congonhas Airport |  | BR | 1412 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1408 |
| 19 | Madrid Barajas International Airport |  | ES | 1344 |
| 20 | Capua Airport |  | IT | 1343 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1300 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1211 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1203 |
| 24 | Charlotte/Douglas International Airport |  | US | 1192 |
| 25 | Charles de Gaulle International Airport |  | FR | 1167 |
| 26 | Kuala Lumpur International Airport |  | MY | 1162 |
| 27 | Malpensa International Airport |  | IT | 1160 |
| 28 | Bengaluru International Airport |  | IN | 1126 |
| 29 | Ninoy Aquino International Airport |  | PH | 1072 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1070 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1060 |
| 32 | Barcelona International Airport |  | ES | 1019 |
| 33 | Daniel K Inouye International Airport |  | US | 998 |
| 34 | Seattle-Tacoma International Airport |  | US | 995 |
| 35 | Viracopos International Airport |  | BR | 983 |
| 36 | Calgary International Airport |  | CA | 976 |
| 37 | Reno/Tahoe International Airport |  | US | 968 |
| 38 | Oslo Gardermoen Airport |  | NO | 958 |
| 39 | Tenerife Norte Airport |  | ES | 957 |
| 40 | Scottsdale Airport |  | US | 942 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 884 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 630 | 21m | 244 km | 2,652.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 406 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 392 | 1h 8m | 770 km | 5,207.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 257 | 44m | 241 km | 1,067.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 256 | 22m | 55 km | 243.3 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 236 | 1h 48m | 1,423 km | 5,791.8 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 219 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 206 | 50m | 556 km | 1,974.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 205 | 1h 15m | 961 km | 3,398.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 201 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 200 | 31m | 369 km | 1,273.0 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 196 | 1h 38m | 1,156 km | 3,910.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 192 | 24m | 218 km | 723.3 t |
| 29 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 191 | 8m | - | - |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CARGO45 | CAR | Hidden Springs Airpark (36AL) | Hidden Springs Airpark (36AL) | 2026-08-05 13:56 UTC | 2026-08-05 14:14 UTC | 18m |
| XSN37 | XSN | Charles M Schulz/Sonoma County Airport (KSTS) | Truckee-Tahoe Airport (KTRK) | 2026-08-05 13:35 UTC | 2026-08-05 14:09 UTC | 34m |
| CAL836 | CAL | Suvarnabhumi Airport (VTBS) | Hsinchu Air Base (RCPO) | 2026-08-05 11:00 UTC | 2026-08-05 14:07 UTC | 3h 6m |
| IGO1161 | IndiGo | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-08-05 12:36 UTC | 2026-08-05 14:05 UTC | 1h 29m |
| AAL797 | American Airlines | Dane County Regional/Truax Field (KMSN) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-05 12:13 UTC | 2026-08-05 14:02 UTC | 1h 49m |
| BHA960 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-08-05 13:50 UTC | 2026-08-05 14:02 UTC | 11m |
| PAV613H | PAV | Los Martinez Del Puerto Airport (LEMP) | Bilbao Airport (LEBB) | 2026-08-05 13:04 UTC | 2026-08-05 13:59 UTC | 54m |
| SMGLR31 | SMG | Kbely Air Base (LKKB) | Kbely Air Base (LKKB) | 2026-08-05 13:11 UTC | 2026-08-05 13:58 UTC | 46m |
| ZKIME | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-08-05 13:46 UTC | 2026-08-05 13:58 UTC | 11m |
| ANGRY32 | ANG | Kickapoo Downtown Airport (KCWC) | 2XA0 (2XA0) | 2026-08-05 13:24 UTC | 2026-08-05 13:54 UTC | 30m |
| N4851P |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-05 13:39 UTC | 2026-08-05 13:53 UTC | 13m |
| RNGR707 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-08-05 13:24 UTC | 2026-08-05 13:53 UTC | 28m |
| IGO9270 | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Naypyidaw Airport (VYEL) | 2026-08-05 12:50 UTC | 2026-08-05 13:53 UTC | 1h 2m |
| HB2562 |  | Muenster Aero Airport (LSPU) | Muenster Aero Airport (LSPU) | 2026-08-05 13:42 UTC | 2026-08-05 13:52 UTC | 10m |
| BOMR746 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | XS10 (XS10) | 2026-08-05 13:23 UTC | 2026-08-05 13:51 UTC | 28m |
| N749DS |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-08-05 13:19 UTC | 2026-08-05 13:51 UTC | 31m |
| DESRT159 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-05 13:38 UTC | 2026-08-05 13:51 UTC | 12m |
| CFBSG | CFB | Woodstock Airport (CCD3) | Woodstock Airport (CCD3) | 2026-08-05 13:32 UTC | 2026-08-05 13:48 UTC | 16m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-05 13:17 UTC | 2026-08-05 13:48 UTC | 30m |
| SJX236 | SJX | Chek Lap Kok International Airport (VHHH) | Hsinchu Air Base (RCPO) | 2026-08-05 12:35 UTC | 2026-08-05 13:48 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
