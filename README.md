# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_14:27:11_UTC-green)

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

**Latest saved flight:** 2026-08-17 14:27:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 14:27:11 UTC

- **208,161** saved flights
- **66,166** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **208,161** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,504,039.9 tonnes** estimated CO2 emissions
- **145,161,732 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8222 |
| 2 | SkyWest Airlines | 7463 |
| 3 | EJA | 4042 |
| 4 | IndiGo | 3565 |
| 5 | American Airlines | 3460 |
| 6 | Southwest Airlines | 3335 |
| 7 | Delta Air Lines | 2670 |
| 8 | ENY | 2586 |
| 9 | LATAM Airlines | 1967 |
| 10 | AZU | 1882 |
| 11 | Lufthansa | 1759 |
| 12 | Vueling | 1730 |
| 13 | WIF | 1677 |
| 14 | LXJ | 1644 |
| 15 | easyJet | 1436 |
| 16 | Swiss International | 1387 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1308 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1269 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1145 |
| 24 | GLO | 1122 |
| 25 | Air France | 1117 |
| 26 | PGT | 1115 |
| 27 | AEE | 1064 |
| 28 | JetBlue | 1064 |
| 29 | WMT | 1053 |
| 30 | Wizz Air | 1029 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176271 |
| 2 | 🇪🇸 ES | 13317 |
| 3 | 🇧🇷 BR | 11934 |
| 4 | 🇦🇺 AU | 11745 |
| 5 | 🇨🇦 CA | 11479 |
| 6 | 🇮🇳 IN | 11125 |
| 7 | 🇮🇹 IT | 10881 |
| 8 | 🇩🇪 DE | 10292 |
| 9 | 🇬🇧 GB | 9702 |
| 10 | 🇯🇵 JP | 8643 |
| 11 | 🇨🇴 CO | 8271 |
| 12 | 🇫🇷 FR | 8249 |
| 13 | 🇬🇷 GR | 6134 |
| 14 | 🇹🇷 TR | 5922 |
| 15 | 🇲🇽 MX | 5844 |
| 16 | 🇨🇭 CH | 5552 |
| 17 | 🇳🇴 NO | 5195 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3500 |
| 20 | 🇵🇱 PL | 3431 |
| 21 | 🇹🇭 TH | 3349 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2771 |
| 24 | 🇬🇹 GT | 2667 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2235 |
| 27 | 🇲🇦 MA | 2101 |
| 28 | 🇳🇱 NL | 1851 |
| 29 | 🇲🇪 ME | 1767 |
| 30 | 🇮🇩 ID | 1723 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4368 |
| 2 | Denver International Airport |  | US | 3395 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2530 |
| 5 | Guaymaral Airport |  | CO | 2503 |
| 6 | Harry Reid International Airport |  | US | 2348 |
| 7 | Zurich Airport |  | CH | 2172 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2170 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2152 |
| 10 | La Aurora Airport |  | GT | 2029 |
| 11 | Chicago O'Hare International Airport |  | US | 1923 |
| 12 | El Dorado International Airport |  | CO | 1899 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1857 |
| 14 | Salt Lake City International Airport |  | US | 1838 |
| 15 | Congonhas Airport |  | BR | 1737 |
| 16 | Frankfurt am Main International Airport |  | DE | 1715 |
| 17 | Madrid Barajas International Airport |  | ES | 1634 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1582 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1577 |
| 20 | Capua Airport |  | IT | 1574 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1516 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1467 |
| 24 | Malpensa International Airport |  | IT | 1444 |
| 25 | Charles de Gaulle International Airport |  | FR | 1429 |
| 26 | Charlotte/Douglas International Airport |  | US | 1413 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1313 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1285 |
| 30 | Bengaluru International Airport |  | IN | 1284 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1259 |
| 32 | Barcelona International Airport |  | ES | 1245 |
| 33 | Seattle-Tacoma International Airport |  | US | 1239 |
| 34 | Viracopos International Airport |  | BR | 1207 |
| 35 | Calgary International Airport |  | CA | 1175 |
| 36 | Oslo Gardermoen Airport |  | NO | 1152 |
| 37 | Vitoria/Foronda Airport |  | ES | 1147 |
| 38 | Reno/Tahoe International Airport |  | US | 1144 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1114 |
| 40 | Don Mueang International Airport |  | TH | 1111 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1029 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 472 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 404 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 348 | 27m | 275 km | 1,649.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 344 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 304 | 1h 49m | 1,423 km | 7,460.6 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 265 | 24m | 218 km | 998.4 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 258 | 19m | 99 km | 441.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 255 | 27m | 215 km | 944.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 238 | 19m | 144 km | 592.0 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 228 | 28m | 152 km | 595.8 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 223 | 1h 49m | 1,304 km | 5,016.9 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N33TV |  | Witham Field (KSUA) | FL48 (FL48) | 2026-08-17 13:05 UTC | 2026-08-17 14:27 UTC | 1h 22m |
| TSC695 | TSC | Eleftherios Venizelos International Airport (LGAV) | LDSR (LDSR) | 2026-08-17 13:03 UTC | 2026-08-17 14:26 UTC | 1h 23m |
| SWA992 | Southwest Airlines | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Griffith-Merrillville Airport (K05C) | 2026-08-17 12:44 UTC | 2026-08-17 14:25 UTC | 1h 41m |
| CNS17 | CNS | Westchester County Airport (KHPN) | 6MI0 (6MI0) | 2026-08-17 11:40 UTC | 2026-08-17 14:25 UTC | 2h 44m |
| QTR68T | Qatar Airways | Seattle-Tacoma International Airport (KSEA) | King Fahd International Airport (OEDF) | 2026-08-17 00:14 UTC | 2026-08-17 14:24 UTC | 14h 10m |
| N937WH |  | Spencer Municipal Airport (KSPW) | Pocahontas Municipal Airport (KPOH) | 2026-08-17 14:08 UTC | 2026-08-17 14:24 UTC | 16m |
| QTR46M | Qatar Airways | Hamad International Airport (OTHH) | Relizane Airport (DAAZ) | 2026-08-17 07:53 UTC | 2026-08-17 14:23 UTC | 6h 30m |
| N761PC |  | Boise Air Trml/Gowen Field (KBOI) | Gooding Municipal Airport (KGNG) | 2026-08-17 14:03 UTC | 2026-08-17 14:22 UTC | 18m |
| ETH3750 | Ethiopian Airlines | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-08-17 00:56 UTC | 2026-08-17 14:22 UTC | 13h 25m |
| SEG13 | SEG | Dunkerque Les Moeres Airport (LFAK) | Dunkerque Les Moeres Airport (LFAK) | 2026-08-17 13:38 UTC | 2026-08-17 14:21 UTC | 42m |
| N116AV |  | Laurinburg/Maxton Airport (KMEB) | Richmond County Airport (KRCZ) | 2026-08-17 13:59 UTC | 2026-08-17 14:21 UTC | 21m |
| EPI254 | EPI | Tallahassee International Airport (KTLH) | Tallahassee International Airport (KTLH) | 2026-08-17 13:03 UTC | 2026-08-17 14:20 UTC | 1h 17m |
| N29251 |  | Hattiesburg Bobby L Chain Municipal Airport (KHBG) | Beets Airport (9MS9) | 2026-08-17 14:09 UTC | 2026-08-17 14:19 UTC | 10m |
| CPA419 | Cathay Pacific | Incheon International Airport (RKSI) | Macau International Airport (VMMC) | 2026-08-17 11:16 UTC | 2026-08-17 14:19 UTC | 3h 3m |
| N5419F |  | Aurora Municipal Airport (KARR) | Wade Airport (56LL) | 2026-08-17 13:53 UTC | 2026-08-17 14:19 UTC | 26m |
| N711SB |  | Tri-Cities Airport (KTRI) | Livingston Municipal Airport (K8A3) | 2026-08-17 13:31 UTC | 2026-08-17 14:19 UTC | 47m |
| N137BF |  | Asheville Regional Airport (KAVL) | Bacon County Airport (KAMG) | 2026-08-17 12:35 UTC | 2026-08-17 14:18 UTC | 1h 42m |
| N63PS |  | Sarasota/Bradenton International Airport (KSRQ) | Squires Aviation Ranch Airport (FD63) | 2026-08-17 12:58 UTC | 2026-08-17 14:18 UTC | 1h 19m |
| JAF6VK | JAF | Melsbroek Air Base (EBMB) | Dubrovnik Airport (LDDU) | 2026-08-17 12:33 UTC | 2026-08-17 14:18 UTC | 1h 44m |
| N737TY |  | Mckinney Ntl Airport (KTKI) | Dillard Ranch Airport (TE01) | 2026-08-17 13:05 UTC | 2026-08-17 14:17 UTC | 1h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
