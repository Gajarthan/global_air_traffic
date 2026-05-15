# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_21:31:32_UTC-green)

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

**Latest saved flight:** 2026-05-15 21:31:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 21:31:32 UTC

- **83,743** saved flights
- **30,260** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **83,743** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,030,476.4 tonnes** estimated CO2 emissions
- **59,737,762 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3587 |
| 2 | SkyWest Airlines | 3105 |
| 3 | IndiGo | 1809 |
| 4 | EJA | 1575 |
| 5 | American Airlines | 1291 |
| 6 | Southwest Airlines | 1226 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1044 |
| 9 | Delta Air Lines | 915 |
| 10 | Vueling | 794 |
| 11 | LATAM Airlines | 757 |
| 12 | AXM | 751 |
| 13 | WIF | 726 |
| 14 | AZU | 659 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 648 |
| 17 | LXJ | 615 |
| 18 | QLK | 615 |
| 19 | Alaska Airlines | 590 |
| 20 | easyJet | 551 |
| 21 | EJU | 534 |
| 22 | AEE | 529 |
| 23 | Cathay Pacific | 520 |
| 24 | VIV | 500 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 468 |
| 27 | AXB | 444 |
| 28 | CXK | 443 |
| 29 | MXY | 419 |
| 30 | United Airlines | 413 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 68670 |
| 2 | 🇪🇸 ES | 5932 |
| 3 | 🇮🇳 IN | 5658 |
| 4 | 🇦🇺 AU | 5326 |
| 5 | 🇩🇪 DE | 4664 |
| 6 | 🇮🇹 IT | 4625 |
| 7 | 🇧🇷 BR | 4619 |
| 8 | 🇯🇵 JP | 4195 |
| 9 | 🇨🇦 CA | 4167 |
| 10 | 🇬🇧 GB | 3568 |
| 11 | 🇫🇷 FR | 3322 |
| 12 | 🇨🇴 CO | 2800 |
| 13 | 🇲🇽 MX | 2543 |
| 14 | 🇬🇷 GR | 2428 |
| 15 | 🇳🇴 NO | 2334 |
| 16 | 🇨🇭 CH | 2217 |
| 17 | 🇲🇾 MY | 1890 |
| 18 | 🇿🇦 ZA | 1574 |
| 19 | 🇹🇷 TR | 1486 |
| 20 | 🇳🇿 NZ | 1467 |
| 21 | 🇹🇭 TH | 1453 |
| 22 | 🇵🇱 PL | 1392 |
| 23 | 🇵🇭 PH | 1308 |
| 24 | 🇰🇷 KR | 1272 |
| 25 | 🇬🇹 GT | 1268 |
| 26 | 🇲🇦 MA | 972 |
| 27 | 🇲🇴 MO | 959 |
| 28 | 🇲🇪 ME | 886 |
| 29 | 🇳🇱 NL | 858 |
| 30 | 🇭🇷 HR | 751 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1839 |
| 2 | Denver International Airport |  | US | 1411 |
| 3 | Tokyo International Airport |  | JP | 1406 |
| 4 | Indira Gandhi International Airport |  | IN | 1202 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1179 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1044 |
| 8 | Zurich Airport |  | CH | 993 |
| 9 | La Aurora Airport |  | GT | 962 |
| 10 | Macau International Airport |  | MO | 959 |
| 11 | Guaymaral Airport |  | CO | 946 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 933 |
| 13 | El Dorado International Airport |  | CO | 900 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 841 |
| 15 | Chicago O'Hare International Airport |  | US | 812 |
| 16 | Madrid Barajas International Airport |  | ES | 763 |
| 17 | Kuala Lumpur International Airport |  | MY | 751 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 724 |
| 19 | Salt Lake City International Airport |  | US | 699 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 21 | Malpensa International Airport |  | IT | 698 |
| 22 | Bengaluru International Airport |  | IN | 695 |
| 23 | Capua Airport |  | IT | 681 |
| 24 | Charles de Gaulle International Airport |  | FR | 654 |
| 25 | Charlotte/Douglas International Airport |  | US | 652 |
| 26 | Congonhas Airport |  | BR | 652 |
| 27 | Tenerife Norte Airport |  | ES | 606 |
| 28 | Daniel K Inouye International Airport |  | US | 604 |
| 29 | Ninoy Aquino International Airport |  | PH | 598 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 564 |
| 32 | Barcelona International Airport |  | ES | 561 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 558 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 540 |
| 35 | Vitoria/Foronda Airport |  | ES | 531 |
| 36 | Don Mueang International Airport |  | TH | 523 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 523 |
| 38 | Amsterdam Airport Schiphol |  | NL | 519 |
| 39 | O. R. Tambo International Airport |  | ZA | 494 |
| 40 | Calgary International Airport |  | CA | 490 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 302 | 21m | 244 km | 1,271.6 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 214 | 14m | 114 km | 419.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 175 | 26m | 275 km | 829.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 125 | 27m | 152 km | 326.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR43K | Qatar Airways | Chicago O'Hare International Airport (KORD) | Zhuhai Airport (ZGSD) | 2026-05-14 23:59 UTC | 2026-05-15 21:31 UTC | 21h 31m |
| N13SU |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-05-15 20:31 UTC | 2026-05-15 21:22 UTC | 51m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-05-15 21:10 UTC | 2026-05-15 21:21 UTC | 10m |
| N274MA |  | Orlando Apopka Airport (KX04) | Orlando Apopka Airport (KX04) | 2026-05-15 20:51 UTC | 2026-05-15 21:20 UTC | 29m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-05-15 17:44 UTC | 2026-05-15 21:13 UTC | 3h 29m |
| POL25 | POL | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-05-15 21:11 UTC | 2026-05-15 21:11 UTC | 0m |
| N917JG |  | Modesto City-County-Harry Sham Field (KMOD) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-15 20:51 UTC | 2026-05-15 21:11 UTC | 19m |
| N38HF |  | Newark Liberty International Airport (KEWR) | KHTO (KHTO) | 2026-05-15 20:15 UTC | 2026-05-15 21:08 UTC | 53m |
| N779RJ |  | Centennial Airport (KAPA) | CO86 (CO86) | 2026-05-15 20:47 UTC | 2026-05-15 21:06 UTC | 18m |
| N3514T |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-05-15 20:51 UTC | 2026-05-15 21:05 UTC | 13m |
| N441EH |  | Lubbock Preston Smith International Airport (KLBB) | 5TE8 (5TE8) | 2026-05-15 20:14 UTC | 2026-05-15 21:01 UTC | 47m |
| LICHEN4 | LIC | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-05-15 19:50 UTC | 2026-05-15 20:59 UTC | 1h 8m |
| CTX50 | CTX | Dekalb-Peachtree Airport (KPDK) | Dekalb-Peachtree Airport (KPDK) | 2026-05-15 20:35 UTC | 2026-05-15 20:58 UTC | 23m |
| LJY241 | LJY | Arnold Palmer Regional Airport (KLBE) | Lehigh Valley International Airport (KABE) | 2026-05-15 20:17 UTC | 2026-05-15 20:56 UTC | 38m |
| 00000000 |  | Midland Airpark (KMDD) | Eastland Municipal Airport (KETN) | 2026-05-15 20:17 UTC | 2026-05-15 20:56 UTC | 38m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-15 20:36 UTC | 2026-05-15 20:56 UTC | 19m |
| N76KQ |  | Miami-Opa Locka Executive Airport (KOPF) | South Bimini Airport (MYBS) | 2026-05-15 20:32 UTC | 2026-05-15 20:54 UTC | 22m |
| N156U |  | Logan-Cache Airport (KLGU) | Morgan County Airport (K42U) | 2026-05-15 20:21 UTC | 2026-05-15 20:54 UTC | 32m |
| HAWK247 | HAW | Kingsville Nas Airport (KNQI) | Brooks County Airport (KBKS) | 2026-05-15 20:40 UTC | 2026-05-15 20:52 UTC | 11m |
| BNOR | BNO | Mosjøen Airport Kjaerstad (ENMS) | Bardufoss Airport (ENDU) | 2026-05-15 20:01 UTC | 2026-05-15 20:51 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
