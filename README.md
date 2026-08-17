# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_22:27:12_UTC-green)

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

**Latest saved flight:** 2026-08-17 22:27:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 22:27:12 UTC

- **210,296** saved flights
- **66,928** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **210,296** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,528,351.9 tonnes** estimated CO2 emissions
- **146,571,127 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8328 |
| 2 | SkyWest Airlines | 7579 |
| 3 | EJA | 4106 |
| 4 | IndiGo | 3575 |
| 5 | American Airlines | 3519 |
| 6 | Southwest Airlines | 3380 |
| 7 | Delta Air Lines | 2719 |
| 8 | ENY | 2619 |
| 9 | LATAM Airlines | 1983 |
| 10 | AZU | 1907 |
| 11 | Lufthansa | 1769 |
| 12 | Vueling | 1751 |
| 13 | WIF | 1691 |
| 14 | LXJ | 1665 |
| 15 | easyJet | 1461 |
| 16 | Swiss International | 1403 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1335 |
| 19 | QLK | 1295 |
| 20 | Alaska Airlines | 1294 |
| 21 | EJU | 1285 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1158 |
| 24 | GLO | 1138 |
| 25 | Air France | 1133 |
| 26 | PGT | 1124 |
| 27 | JetBlue | 1076 |
| 28 | AEE | 1069 |
| 29 | WMT | 1067 |
| 30 | Wizz Air | 1044 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 178334 |
| 2 | 🇪🇸 ES | 13453 |
| 3 | 🇧🇷 BR | 12072 |
| 4 | 🇦🇺 AU | 11759 |
| 5 | 🇨🇦 CA | 11644 |
| 6 | 🇮🇳 IN | 11158 |
| 7 | 🇮🇹 IT | 11000 |
| 8 | 🇩🇪 DE | 10377 |
| 9 | 🇬🇧 GB | 9814 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8443 |
| 12 | 🇫🇷 FR | 8352 |
| 13 | 🇬🇷 GR | 6179 |
| 14 | 🇹🇷 TR | 5993 |
| 15 | 🇲🇽 MX | 5907 |
| 16 | 🇨🇭 CH | 5585 |
| 17 | 🇳🇴 NO | 5236 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3517 |
| 20 | 🇵🇱 PL | 3476 |
| 21 | 🇹🇭 TH | 3354 |
| 22 | 🇳🇿 NZ | 2901 |
| 23 | 🇵🇭 PH | 2784 |
| 24 | 🇬🇹 GT | 2701 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2262 |
| 27 | 🇲🇦 MA | 2122 |
| 28 | 🇳🇱 NL | 1872 |
| 29 | 🇲🇪 ME | 1791 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4426 |
| 2 | Denver International Airport |  | US | 3443 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2539 |
| 5 | Guaymaral Airport |  | CO | 2530 |
| 6 | Harry Reid International Airport |  | US | 2363 |
| 7 | Zurich Airport |  | CH | 2190 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2182 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2181 |
| 10 | La Aurora Airport |  | GT | 2055 |
| 11 | Chicago O'Hare International Airport |  | US | 1951 |
| 12 | El Dorado International Airport |  | CO | 1925 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1873 |
| 14 | Salt Lake City International Airport |  | US | 1865 |
| 15 | Congonhas Airport |  | BR | 1756 |
| 16 | Frankfurt am Main International Airport |  | DE | 1723 |
| 17 | Madrid Barajas International Airport |  | ES | 1644 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1595 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1591 |
| 20 | Capua Airport |  | IT | 1584 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1533 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1469 |
| 24 | Malpensa International Airport |  | IT | 1456 |
| 25 | Charles de Gaulle International Airport |  | FR | 1445 |
| 26 | Charlotte/Douglas International Airport |  | US | 1424 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1319 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1301 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1277 |
| 32 | Barcelona International Airport |  | ES | 1262 |
| 33 | Seattle-Tacoma International Airport |  | US | 1251 |
| 34 | Viracopos International Airport |  | BR | 1222 |
| 35 | Calgary International Airport |  | CA | 1194 |
| 36 | Oslo Gardermoen Airport |  | NO | 1161 |
| 37 | Vitoria/Foronda Airport |  | ES | 1160 |
| 38 | Reno/Tahoe International Airport |  | US | 1149 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1132 |
| 40 | Daniel K Inouye International Airport |  | US | 1116 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1038 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 742 | 21m | 244 km | 3,124.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 478 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 428 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 308 | 44m | 241 km | 1,279.4 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 307 | 1h 49m | 1,423 km | 7,534.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 289 | 22m | 55 km | 274.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 263 | 19m | 99 km | 450.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 250 | 1h 37m | 1,156 km | 4,987.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 250 | 1h 14m | 961 km | 4,143.9 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 248 | 13m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 241 | 19m | 144 km | 599.5 t |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 240 | 31m | 369 km | 1,527.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 231 | 28m | 152 km | 603.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 226 | 1h 49m | 1,304 km | 5,084.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BULET47 | BUL | North Island Nas (Halsey Field) Airport (KNZY) | CA84 (CA84) | 2026-08-17 22:05 UTC | 2026-08-17 22:27 UTC | 21m |
| N7693Y |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-17 21:49 UTC | 2026-08-17 22:24 UTC | 34m |
| N777GB |  | French Valley Airport (KF70) | Big Bear City Airport (KL35) | 2026-08-17 22:05 UTC | 2026-08-17 22:23 UTC | 17m |
| N733JA |  | San Gabriel Valley Airport (KEMT) | Santa Monica Municipal Airport (KSMO) | 2026-08-17 21:53 UTC | 2026-08-17 22:21 UTC | 27m |
| SFE1 | SFE | Bud Dryden Airport (TX05) | Bud Dryden Airport (TX05) | 2026-08-17 22:17 UTC | 2026-08-17 22:21 UTC | 4m |
| N496LA |  | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-08-17 20:39 UTC | 2026-08-17 22:04 UTC | 1h 24m |
| EJA506 | EJA | Norman Y Mineta San Jose International Airport (KSJC) | Truckee-Tahoe Airport (KTRK) | 2026-08-17 21:33 UTC | 2026-08-17 22:04 UTC | 30m |
| N66104 |  | Lakefront Airport (KNEW) | Slidell Airport (KASD) | 2026-08-17 21:31 UTC | 2026-08-17 22:03 UTC | 31m |
| AMMO86 | AMM | Edwards Af Aux North Base Airport (K9L2) | Edwards Af Aux North Base Airport (K9L2) | 2026-08-17 21:36 UTC | 2026-08-17 22:01 UTC | 24m |
| N2EE |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-17 21:59 UTC | 2026-08-17 22:00 UTC | 0m |
| N853AL |  | Bend Municipal Airport (KBDN) | OG05 (OG05) | 2026-08-17 21:49 UTC | 2026-08-17 21:59 UTC | 10m |
| WXN | WXN | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-08-17 21:22 UTC | 2026-08-17 21:57 UTC | 35m |
| N723AF |  | Vancouver International Airport (CYVR) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-17 19:46 UTC | 2026-08-17 21:57 UTC | 2h 10m |
| BXR831 | BXR | Redding Regional Airport (KRDD) | Weed Airport (KO46) | 2026-08-17 21:35 UTC | 2026-08-17 21:56 UTC | 20m |
| N1PX |  | Quad Cities International Airport (KMLI) | K36U (K36U) | 2026-08-17 19:11 UTC | 2026-08-17 21:56 UTC | 2h 44m |
| N24AH |  | Zamperini Field (KTOA) | Southern California Logistics Airport (KVCV) | 2026-08-17 21:17 UTC | 2026-08-17 21:54 UTC | 37m |
| AWH32H | AWH | Madrid Barajas International Airport (LEMD) | Leipzig Halle Airport (EDDP) | 2026-08-17 19:17 UTC | 2026-08-17 21:54 UTC | 2h 36m |
| N715MN |  | Kansas City Downtown/Wheeler Field (KMKC) | Scottsdale Airport (KSDL) | 2026-08-17 19:24 UTC | 2026-08-17 21:52 UTC | 2h 27m |
| N98EG |  | Laguardia Airport (KLGA) | Laguardia Airport (KLGA) | 2026-08-17 21:49 UTC | 2026-08-17 21:51 UTC | 2m |
| NTR202 | NTR | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-08-17 21:01 UTC | 2026-08-17 21:50 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
