# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_19:40:04_UTC-green)

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

**Latest saved flight:** 2026-08-16 19:40:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 19:40:04 UTC

- **205,915** saved flights
- **65,683** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **205,915** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,475,445.3 tonnes** estimated CO2 emissions
- **143,504,075 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8119 |
| 2 | SkyWest Airlines | 7394 |
| 3 | EJA | 3993 |
| 4 | IndiGo | 3521 |
| 5 | American Airlines | 3426 |
| 6 | Southwest Airlines | 3315 |
| 7 | Delta Air Lines | 2644 |
| 8 | ENY | 2569 |
| 9 | LATAM Airlines | 1933 |
| 10 | AZU | 1864 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1706 |
| 13 | WIF | 1656 |
| 14 | LXJ | 1626 |
| 15 | easyJet | 1425 |
| 16 | Swiss International | 1373 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1299 |
| 19 | Alaska Airlines | 1277 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1130 |
| 24 | GLO | 1107 |
| 25 | Air France | 1101 |
| 26 | PGT | 1099 |
| 27 | JetBlue | 1055 |
| 28 | AEE | 1051 |
| 29 | WMT | 1039 |
| 30 | CXK | 1015 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 174960 |
| 2 | 🇪🇸 ES | 13168 |
| 3 | 🇧🇷 BR | 11787 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11361 |
| 6 | 🇮🇳 IN | 10986 |
| 7 | 🇮🇹 IT | 10742 |
| 8 | 🇩🇪 DE | 10196 |
| 9 | 🇬🇧 GB | 9604 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇨🇴 CO | 8161 |
| 12 | 🇫🇷 FR | 8157 |
| 13 | 🇬🇷 GR | 6064 |
| 14 | 🇹🇷 TR | 5836 |
| 15 | 🇲🇽 MX | 5787 |
| 16 | 🇨🇭 CH | 5508 |
| 17 | 🇳🇴 NO | 5130 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3398 |
| 21 | 🇹🇭 TH | 3246 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2614 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2202 |
| 27 | 🇲🇦 MA | 2078 |
| 28 | 🇳🇱 NL | 1836 |
| 29 | 🇲🇪 ME | 1733 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4325 |
| 2 | Denver International Airport |  | US | 3360 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Indira Gandhi International Airport |  | IN | 2492 |
| 5 | Guaymaral Airport |  | CO | 2490 |
| 6 | Harry Reid International Airport |  | US | 2326 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2150 |
| 8 | Zurich Airport |  | CH | 2150 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2137 |
| 10 | La Aurora Airport |  | GT | 1994 |
| 11 | Chicago O'Hare International Airport |  | US | 1909 |
| 12 | El Dorado International Airport |  | CO | 1876 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1839 |
| 14 | Salt Lake City International Airport |  | US | 1822 |
| 15 | Congonhas Airport |  | BR | 1716 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1616 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1572 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1568 |
| 20 | Capua Airport |  | IT | 1564 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1489 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1419 |
| 25 | Charles de Gaulle International Airport |  | FR | 1412 |
| 26 | Charlotte/Douglas International Airport |  | US | 1404 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1271 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1239 |
| 32 | Barcelona International Airport |  | ES | 1226 |
| 33 | Seattle-Tacoma International Airport |  | US | 1220 |
| 34 | Viracopos International Airport |  | BR | 1193 |
| 35 | Calgary International Airport |  | CA | 1163 |
| 36 | Reno/Tahoe International Airport |  | US | 1139 |
| 37 | Oslo Gardermoen Airport |  | NO | 1137 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1106 |
| 40 | Daniel K Inouye International Airport |  | US | 1103 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1025 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 469 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 397 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 248 | 19m | 99 km | 424.8 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 242 | 1h 37m | 1,156 km | 4,827.8 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 222 | 1h 49m | 1,304 km | 4,994.4 t |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 222 | 28m | 152 km | 580.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGRQH | CGR | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-16 19:26 UTC | 2026-08-16 19:40 UTC | 13m |
| AAL3167 | American Airlines | 14MI (14MI) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-16 17:30 UTC | 2026-08-16 19:32 UTC | 2h 1m |
| N6212F |  | Watsonville Municipal Airport (KWVI) | Castle Airport (KMER) | 2026-08-16 18:40 UTC | 2026-08-16 19:29 UTC | 48m |
| N19650 |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-16 19:10 UTC | 2026-08-16 19:29 UTC | 19m |
| N2745G |  | Mitchell Municipal Airport (KMHE) | Harold Davidson Field (KVMR) | 2026-08-16 19:04 UTC | 2026-08-16 19:27 UTC | 23m |
| TKR137 | TKR | NV17 (NV17) | K9U3 (K9U3) | 2026-08-16 19:15 UTC | 2026-08-16 19:26 UTC | 10m |
| ISR825 | ISR | Ben Gurion International Airport (LLBG) | Białystok-Krywlany Airport (EPBK) | 2026-08-16 16:07 UTC | 2026-08-16 19:26 UTC | 3h 18m |
| FFL1411 | FFL | Georgetown County Airport (KGGE) | Ocean City Municipal Airport (KOXB) | 2026-08-16 17:50 UTC | 2026-08-16 19:25 UTC | 1h 35m |
| XCGEQ | XCG | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-16 19:06 UTC | 2026-08-16 19:22 UTC | 15m |
| UAL1149 | United Airlines | San Francisco International Airport (KSFO) | Newark Liberty International Airport (KEWR) | 2026-08-16 14:25 UTC | 2026-08-16 19:15 UTC | 4h 50m |
| CGRQH | CGR | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-16 19:01 UTC | 2026-08-16 19:13 UTC | 11m |
| N331RF |  | Prince George Airport (CYXS) | Chetwynd Airport (CYCQ) | 2026-08-16 15:52 UTC | 2026-08-16 19:12 UTC | 3h 20m |
| N89PS |  | Gary/Chicago International Airport (KGYY) | Chicago Midway International Airport (KMDW) | 2026-08-16 19:01 UTC | 2026-08-16 19:08 UTC | 7m |
| BOE962 | BOE | Boeing Field/King County International Airport (KBFI) | Warden Airport (K2S4) | 2026-08-16 17:48 UTC | 2026-08-16 19:06 UTC | 1h 18m |
| AUA26Z | Austrian Airlines | Berlin Brandenburg Airport (EDDB) | Vienna International Airport (LOWW) | 2026-08-16 18:09 UTC | 2026-08-16 19:00 UTC | 51m |
| N317ZE |  | Northern Colorado Regional Airport (KFNL) | Elk Park Ranch Airport (34CD) | 2026-08-16 18:25 UTC | 2026-08-16 19:00 UTC | 34m |
| SCU2 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-16 18:59 UTC | 2026-08-16 18:59 UTC | 0m |
| N29GB |  | Double Eagle Ii Airport (KAEG) | Double Eagle Ii Airport (KAEG) | 2026-08-16 18:58 UTC | 2026-08-16 18:59 UTC | 1m |
| N44SN |  | Central Florida Airpark (2FA6) | Leeward Air Ranch Airport (FD04) | 2026-08-16 18:43 UTC | 2026-08-16 18:59 UTC | 15m |
| N1600U |  | AL15 (AL15) | Holk Field At Foley Municipal Airport (K5R4) | 2026-08-16 18:56 UTC | 2026-08-16 18:58 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
