# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_22:57:49_UTC-green)

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

**Latest saved flight:** 2026-06-04 22:57:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-04 22:57:49 UTC

- **102,491** saved flights
- **36,295** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **102,491** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,251,508.5 tonnes** estimated CO2 emissions
- **72,551,219 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4214 |
| 2 | SkyWest Airlines | 3853 |
| 3 | IndiGo | 2045 |
| 4 | EJA | 1965 |
| 5 | American Airlines | 1657 |
| 6 | Southwest Airlines | 1548 |
| 7 | ENY | 1273 |
| 8 | Delta Air Lines | 1205 |
| 9 | Lufthansa | 1189 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 909 |
| 12 | WIF | 901 |
| 13 | AXM | 881 |
| 14 | AZU | 828 |
| 15 | LXJ | 772 |
| 16 | Swiss International | 741 |
| 17 | All Nippon Airways | 720 |
| 18 | Alaska Airlines | 716 |
| 19 | QLK | 687 |
| 20 | easyJet | 666 |
| 21 | EJU | 643 |
| 22 | Cathay Pacific | 616 |
| 23 | AEE | 595 |
| 24 | VIV | 590 |
| 25 | Air France | 587 |
| 26 | United Airlines | 570 |
| 27 | MXY | 556 |
| 28 | CXK | 550 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 505 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 86207 |
| 2 | 🇪🇸 ES | 7066 |
| 3 | 🇮🇳 IN | 6472 |
| 4 | 🇦🇺 AU | 6217 |
| 5 | 🇧🇷 BR | 5625 |
| 6 | 🇩🇪 DE | 5507 |
| 7 | 🇮🇹 IT | 5445 |
| 8 | 🇨🇦 CA | 5329 |
| 9 | 🇯🇵 JP | 4711 |
| 10 | 🇬🇧 GB | 4332 |
| 11 | 🇫🇷 FR | 4066 |
| 12 | 🇨🇴 CO | 3536 |
| 13 | 🇲🇽 MX | 3092 |
| 14 | 🇬🇷 GR | 2913 |
| 15 | 🇳🇴 NO | 2853 |
| 16 | 🇨🇭 CH | 2629 |
| 17 | 🇲🇾 MY | 2247 |
| 18 | 🇹🇷 TR | 1938 |
| 19 | 🇿🇦 ZA | 1776 |
| 20 | 🇳🇿 NZ | 1723 |
| 21 | 🇹🇭 TH | 1695 |
| 22 | 🇰🇷 KR | 1661 |
| 23 | 🇵🇱 PL | 1638 |
| 24 | 🇬🇹 GT | 1506 |
| 25 | 🇵🇭 PH | 1497 |
| 26 | 🇲🇦 MA | 1135 |
| 27 | 🇲🇴 MO | 1076 |
| 28 | 🇳🇱 NL | 1015 |
| 29 | 🇲🇪 ME | 968 |
| 30 | 🇭🇷 HR | 902 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2224 |
| 2 | Denver International Airport |  | US | 1757 |
| 3 | Tokyo International Airport |  | JP | 1561 |
| 4 | Indira Gandhi International Airport |  | IN | 1408 |
| 5 | Harry Reid International Airport |  | US | 1314 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1307 |
| 7 | Guaymaral Airport |  | CO | 1284 |
| 8 | Frankfurt am Main International Airport |  | DE | 1189 |
| 9 | Zurich Airport |  | CH | 1169 |
| 10 | La Aurora Airport |  | GT | 1159 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1110 |
| 12 | El Dorado International Airport |  | CO | 1081 |
| 13 | Macau International Airport |  | MO | 1076 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1041 |
| 15 | Chicago O'Hare International Airport |  | US | 1026 |
| 16 | Madrid Barajas International Airport |  | ES | 898 |
| 17 | Kuala Lumpur International Airport |  | MY | 887 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 882 |
| 19 | Salt Lake City International Airport |  | US | 861 |
| 20 | Capua Airport |  | IT | 853 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 796 |
| 22 | Charlotte/Douglas International Airport |  | US | 796 |
| 23 | Charles de Gaulle International Airport |  | FR | 781 |
| 24 | Congonhas Airport |  | BR | 781 |
| 25 | Bengaluru International Airport |  | IN | 773 |
| 26 | Malpensa International Airport |  | IT | 772 |
| 27 | Daniel K Inouye International Airport |  | US | 708 |
| 28 | Tenerife Norte Airport |  | ES | 702 |
| 29 | Ninoy Aquino International Airport |  | PH | 684 |
| 30 | Barcelona International Airport |  | ES | 673 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 666 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 664 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 656 |
| 34 | Amsterdam Airport Schiphol |  | NL | 627 |
| 35 | Don Mueang International Airport |  | TH | 620 |
| 36 | Vitoria/Foronda Airport |  | ES | 620 |
| 37 | Calgary International Airport |  | CA | 605 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 591 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 580 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 530 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 376 | 21m | 244 km | 1,583.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 269 | 24m | 225 km | 1,043.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 247 | 28m | 304 km | 1,294.8 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 234 | 1h 10m | 770 km | 3,108.5 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 215 | 19m | 165 km | 611.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 143 | 27m | 152 km | 373.7 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 137 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 135 | 20m | 250 km | 583.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 133 | 18m | 144 km | 330.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 116 | 44m | 241 km | 481.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| NZJ | NZJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-06-04 22:45 UTC | 2026-06-04 22:57 UTC | 12m |
| LBQ197 | LBQ | New Century Aircenter Airport (KIXD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-06-04 21:52 UTC | 2026-06-04 22:56 UTC | 1h 3m |
| N4381Q |  | Decatur Municipal Airport (KLUD) | Vance Field (TE76) | 2026-06-04 22:39 UTC | 2026-06-04 22:54 UTC | 15m |
| N454NC |  | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-06-04 22:13 UTC | 2026-06-04 22:49 UTC | 35m |
| N500GP |  | Northeast Philadelphia Airport (KPNE) | Doylestown Airport (KDYL) | 2026-06-04 22:19 UTC | 2026-06-04 22:44 UTC | 25m |
| N800FW |  | Republic Airport (KFRG) | Republic Airport (KFRG) | 2026-06-04 21:51 UTC | 2026-06-04 22:44 UTC | 52m |
| N904RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-06-04 21:32 UTC | 2026-06-04 22:44 UTC | 1h 11m |
| N135DT |  | Nephi Municipal Airport (KU14) | KU42 (KU42) | 2026-06-04 22:27 UTC | 2026-06-04 22:42 UTC | 15m |
| N908FG |  | Williamsport Regional Airport (KIPT) | Lancaster Airport (KLNS) | 2026-06-04 21:43 UTC | 2026-06-04 22:40 UTC | 56m |
| N21SZ |  | Whiteman Airport (KWHP) | Meadows Field (KBFL) | 2026-06-04 21:44 UTC | 2026-06-04 22:40 UTC | 55m |
| EJA800 | EJA | Teterboro Airport (KTEB) | Austin-Bergstrom International Airport (KAUS) | 2026-06-04 19:28 UTC | 2026-06-04 22:40 UTC | 3h 12m |
| N171RA |  | Sarasota/Bradenton International Airport (KSRQ) | Albert Whitted Airport (KSPG) | 2026-06-04 21:52 UTC | 2026-06-04 22:38 UTC | 46m |
| KAL432 | Korean Air | Incheon International Airport (RKSI) | Incheon International Airport (RKSI) | 2026-06-04 07:38 UTC | 2026-06-04 22:32 UTC | 14h 53m |
| N29BY |  | Coeur D'Alene/Pappy Boyington Field (KCOE) | 4WA6 (4WA6) | 2026-06-04 22:02 UTC | 2026-06-04 22:31 UTC | 29m |
| CGSSC | CGS | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-06-04 22:01 UTC | 2026-06-04 22:31 UTC | 30m |
| N6062L |  | Lincoln County Regional Airport (KIPJ) | Lincoln County Regional Airport (KIPJ) | 2026-06-04 21:30 UTC | 2026-06-04 22:27 UTC | 57m |
| N298MC |  | Princeton Airport (K39N) | Sky Manor Airport (KN40) | 2026-06-04 21:50 UTC | 2026-06-04 22:22 UTC | 32m |
| N8021D |  | Skid Marks Airport (AK67) | West Papoose Lake Airpark (44AK) | 2026-06-04 22:13 UTC | 2026-06-04 22:22 UTC | 8m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-06-04 14:05 UTC | 2026-06-04 22:21 UTC | 8h 16m |
| MXY207 | MXY | Harry Reid International Airport (KLAS) | Akron-Canton Regional Airport (KCAK) | 2026-06-04 18:28 UTC | 2026-06-04 22:20 UTC | 3h 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
