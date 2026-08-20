# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_16:27:36_UTC-green)

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

**Latest saved flight:** 2026-08-20 16:27:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 16:27:36 UTC

- **219,750** saved flights
- **68,997** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,750** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,645,755.0 tonnes** estimated CO2 emissions
- **153,377,099 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8813 |
| 2 | SkyWest Airlines | 7823 |
| 3 | EJA | 4257 |
| 4 | IndiGo | 3731 |
| 5 | American Airlines | 3641 |
| 6 | Southwest Airlines | 3475 |
| 7 | Delta Air Lines | 2832 |
| 8 | ENY | 2705 |
| 9 | LATAM Airlines | 2086 |
| 10 | AZU | 2011 |
| 11 | Vueling | 1848 |
| 12 | Lufthansa | 1824 |
| 13 | WIF | 1760 |
| 14 | LXJ | 1733 |
| 15 | easyJet | 1524 |
| 16 | Swiss International | 1464 |
| 17 | AXM | 1444 |
| 18 | United Airlines | 1382 |
| 19 | QLK | 1375 |
| 20 | EJU | 1371 |
| 21 | Alaska Airlines | 1340 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1199 |
| 24 | VIV | 1199 |
| 25 | Air France | 1191 |
| 26 | PGT | 1190 |
| 27 | WMT | 1158 |
| 28 | Wizz Air | 1121 |
| 29 | JetBlue | 1115 |
| 30 | AEE | 1101 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 184798 |
| 2 | 🇪🇸 ES | 14091 |
| 3 | 🇧🇷 BR | 12685 |
| 4 | 🇦🇺 AU | 12418 |
| 5 | 🇨🇦 CA | 12113 |
| 6 | 🇮🇹 IT | 11707 |
| 7 | 🇮🇳 IN | 11629 |
| 8 | 🇩🇪 DE | 10861 |
| 9 | 🇬🇧 GB | 10329 |
| 10 | 🇨🇴 CO | 9018 |
| 11 | 🇯🇵 JP | 8961 |
| 12 | 🇫🇷 FR | 8751 |
| 13 | 🇬🇷 GR | 6411 |
| 14 | 🇹🇷 TR | 6325 |
| 15 | 🇲🇽 MX | 6107 |
| 16 | 🇨🇭 CH | 5821 |
| 17 | 🇳🇴 NO | 5464 |
| 18 | 🇲🇾 MY | 3819 |
| 19 | 🇿🇦 ZA | 3759 |
| 20 | 🇹🇭 TH | 3655 |
| 21 | 🇵🇱 PL | 3647 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2785 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2436 |
| 27 | 🇲🇦 MA | 2215 |
| 28 | 🇳🇱 NL | 1956 |
| 29 | 🇲🇪 ME | 1942 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4602 |
| 2 | Denver International Airport |  | US | 3582 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2665 |
| 5 | Guaymaral Airport |  | CO | 2597 |
| 6 | Harry Reid International Airport |  | US | 2421 |
| 7 | Zurich Airport |  | CH | 2283 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2254 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2235 |
| 10 | La Aurora Airport |  | GT | 2122 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2012 |
| 13 | Salt Lake City International Airport |  | US | 1935 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1901 |
| 15 | Congonhas Airport |  | BR | 1856 |
| 16 | Frankfurt am Main International Airport |  | DE | 1790 |
| 17 | Madrid Barajas International Airport |  | ES | 1726 |
| 18 | Capua Airport |  | IT | 1679 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1643 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1622 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1615 |
| 22 | Macau International Airport |  | MO | 1579 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1511 |
| 26 | Charlotte/Douglas International Airport |  | US | 1463 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1402 |
| 29 | Barcelona International Airport |  | ES | 1347 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1336 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1299 |
| 34 | Viracopos International Airport |  | BR | 1285 |
| 35 | Calgary International Airport |  | CA | 1237 |
| 36 | Oslo Gardermoen Airport |  | NO | 1219 |
| 37 | Vitoria/Foronda Airport |  | ES | 1219 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1215 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1182 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 786 | 21m | 244 km | 3,309.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 490 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 369 | 27m | 275 km | 1,748.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 323 | 1h 50m | 1,423 km | 7,926.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 322 | 44m | 241 km | 1,337.5 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 291 | 21m | 250 km | 1,256.9 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 272 | 24m | 218 km | 1,024.7 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 258 | 1h 14m | 961 km | 4,276.5 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 250 | 19m | 144 km | 621.9 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ERU11 | ERU | AZ86 (AZ86) | Cottonwood Airport (KP52) | 2026-08-20 16:08 UTC | 2026-08-20 16:27 UTC | 19m |
| GTI9793 | GTI | Maastricht Aachen Airport (EHBK) | Macau International Airport (VMMC) | 2026-08-20 05:27 UTC | 2026-08-20 16:22 UTC | 10h 55m |
| SFY115 | SFY | Sebastian Municipal Airport (KX26) | Lakeland Linder International Airport (KLAL) | 2026-08-20 15:38 UTC | 2026-08-20 16:22 UTC | 43m |
| WMU19 | WMU | Brooks Field (KRMY) | Jackson County/Reynolds Field (KJXN) | 2026-08-20 15:57 UTC | 2026-08-20 16:19 UTC | 21m |
| N403TD |  | Linden Airport (KLDJ) | Newark Liberty International Airport (KEWR) | 2026-08-20 13:52 UTC | 2026-08-20 16:18 UTC | 2h 26m |
| N4953G |  | Casper/Natrona County International Airport (KCPR) | Casper/Natrona County International Airport (KCPR) | 2026-08-20 16:04 UTC | 2026-08-20 16:15 UTC | 10m |
| N441MG |  | Aero Country Airport (KT31) | Jones Field (KF00) | 2026-08-20 15:47 UTC | 2026-08-20 16:14 UTC | 27m |
| N945G |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-20 15:49 UTC | 2026-08-20 16:14 UTC | 25m |
| CHX67 | CHX | Wyk auf Fohr Airport (EDXY) | Husum-Schwesing Airport (EDXJ) | 2026-08-20 16:02 UTC | 2026-08-20 16:13 UTC | 10m |
| N313AM |  | Reno/Tahoe International Airport (KRNO) | CA38 (CA38) | 2026-08-20 14:52 UTC | 2026-08-20 16:12 UTC | 1h 19m |
| XBMGH | XBM | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-20 15:36 UTC | 2026-08-20 16:09 UTC | 33m |
| SXN21 | SXN | Weston Airport (EIWT) | Elstree Airfield (EGTR) | 2026-08-20 14:28 UTC | 2026-08-20 16:09 UTC | 1h 41m |
| CXK239 | CXK | Richmond International Airport (KRIC) | Richmond International Airport (KRIC) | 2026-08-20 16:08 UTC | 2026-08-20 16:09 UTC | 0m |
| N166RT |  | Barrow County Airport (KWDR) | Barrow County Airport (KWDR) | 2026-08-20 15:56 UTC | 2026-08-20 16:06 UTC | 9m |
| N162JK |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-08-20 15:49 UTC | 2026-08-20 16:05 UTC | 15m |
| N316EJ |  | Pioneer Village Field (K0V3) | Lincoln Airport (KLNK) | 2026-08-20 15:31 UTC | 2026-08-20 16:05 UTC | 33m |
| N125Z |  | Telluride Regional Airport (KTEX) | Telluride Regional Airport (KTEX) | 2026-08-20 15:40 UTC | 2026-08-20 16:04 UTC | 24m |
| N517C |  | Tierra Linda Ranch Airport (60TE) | Austin-Bergstrom International Airport (KAUS) | 2026-08-20 15:37 UTC | 2026-08-20 16:02 UTC | 24m |
| WIF6T | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-20 15:49 UTC | 2026-08-20 15:59 UTC | 10m |
| N472BL |  | Pensacola International Airport (KPNS) | Mc Kinnon Airpark (48FL) | 2026-08-20 15:45 UTC | 2026-08-20 15:59 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
