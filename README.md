# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_11:08:28_UTC-green)

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

**Latest saved flight:** 2026-06-24 11:08:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-24 11:08:28 UTC

- **118,667** saved flights
- **40,911** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **118,667** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,438,814.7 tonnes** estimated CO2 emissions
- **83,409,549 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4892 |
| 2 | SkyWest Airlines | 4383 |
| 3 | EJA | 2293 |
| 4 | IndiGo | 2291 |
| 5 | American Airlines | 1846 |
| 6 | Southwest Airlines | 1769 |
| 7 | ENY | 1484 |
| 8 | Delta Air Lines | 1398 |
| 9 | Lufthansa | 1303 |
| 10 | Vueling | 1075 |
| 11 | WIF | 1050 |
| 12 | LATAM Airlines | 1049 |
| 13 | AZU | 992 |
| 14 | AXM | 973 |
| 15 | LXJ | 900 |
| 16 | Swiss International | 836 |
| 17 | All Nippon Airways | 815 |
| 18 | Alaska Airlines | 789 |
| 19 | easyJet | 765 |
| 20 | QLK | 763 |
| 21 | EJU | 745 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 662 |
| 24 | Air France | 652 |
| 25 | VIV | 652 |
| 26 | United Airlines | 649 |
| 27 | CXK | 636 |
| 28 | MXY | 623 |
| 29 | AXB | 589 |
| 30 | GLO | 582 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 100257 |
| 2 | 🇪🇸 ES | 8102 |
| 3 | 🇮🇳 IN | 7199 |
| 4 | 🇦🇺 AU | 7014 |
| 5 | 🇧🇷 BR | 6548 |
| 6 | 🇮🇹 IT | 6336 |
| 7 | 🇩🇪 DE | 6332 |
| 8 | 🇨🇦 CA | 6240 |
| 9 | 🇯🇵 JP | 5317 |
| 10 | 🇬🇧 GB | 5211 |
| 11 | 🇫🇷 FR | 4734 |
| 12 | 🇨🇴 CO | 4000 |
| 13 | 🇲🇽 MX | 3479 |
| 14 | 🇬🇷 GR | 3387 |
| 15 | 🇳🇴 NO | 3261 |
| 16 | 🇨🇭 CH | 3049 |
| 17 | 🇲🇾 MY | 2529 |
| 18 | 🇹🇷 TR | 2434 |
| 19 | 🇿🇦 ZA | 2003 |
| 20 | 🇵🇱 PL | 1954 |
| 21 | 🇳🇿 NZ | 1926 |
| 22 | 🇹🇭 TH | 1907 |
| 23 | 🇰🇷 KR | 1898 |
| 24 | 🇵🇭 PH | 1712 |
| 25 | 🇬🇹 GT | 1661 |
| 26 | 🇲🇦 MA | 1287 |
| 27 | 🇲🇪 ME | 1177 |
| 28 | 🇲🇴 MO | 1170 |
| 29 | 🇳🇱 NL | 1138 |
| 30 | 🇭🇷 HR | 1028 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2500 |
| 2 | Denver International Airport |  | US | 1989 |
| 3 | Tokyo International Airport |  | JP | 1761 |
| 4 | Indira Gandhi International Airport |  | IN | 1581 |
| 5 | Guaymaral Airport |  | CO | 1490 |
| 6 | Harry Reid International Airport |  | US | 1474 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1442 |
| 8 | Zurich Airport |  | CH | 1326 |
| 9 | La Aurora Airport |  | GT | 1283 |
| 10 | Frankfurt am Main International Airport |  | DE | 1263 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1258 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1177 |
| 13 | El Dorado International Airport |  | CO | 1171 |
| 14 | Macau International Airport |  | MO | 1170 |
| 15 | Chicago O'Hare International Airport |  | US | 1161 |
| 16 | Capua Airport |  | IT | 1025 |
| 17 | Salt Lake City International Airport |  | US | 1013 |
| 18 | Madrid Barajas International Airport |  | ES | 1001 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 993 |
| 20 | Kuala Lumpur International Airport |  | MY | 978 |
| 21 | Congonhas Airport |  | BR | 912 |
| 22 | Charlotte/Douglas International Airport |  | US | 900 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 897 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 883 |
| 25 | Charles de Gaulle International Airport |  | FR | 873 |
| 26 | Bengaluru International Airport |  | IN | 871 |
| 27 | Malpensa International Airport |  | IT | 834 |
| 28 | Ninoy Aquino International Airport |  | PH | 792 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 776 |
| 30 | Daniel K Inouye International Airport |  | US | 768 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 755 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Vitoria/Foronda Airport |  | ES | 697 |
| 35 | Calgary International Airport |  | CA | 694 |
| 36 | Amsterdam Airport Schiphol |  | NL | 691 |
| 37 | Don Mueang International Airport |  | TH | 690 |
| 38 | Seattle-Tacoma International Airport |  | US | 680 |
| 39 | Viracopos International Airport |  | BR | 674 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 672 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 619 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 430 | 21m | 244 km | 1,810.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 314 | 24m | 225 km | 1,218.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 304 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 290 | 1h 25m | 910 km | 4,550.8 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 287 | 1h 10m | 770 km | 3,812.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 234 | 26m | 275 km | 1,108.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 234 | 19m | 165 km | 665.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 221 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 176 | 22m | 55 km | 167.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 171 | 26m | 215 km | 633.3 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 162 | 44m | 241 km | 672.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 149 | 1h 44m | 1,423 km | 3,656.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 148 | 18m | 144 km | 368.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 139 | 1h 39m | 1,156 km | 2,773.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 134 | 1h 17m | 961 km | 2,221.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PXR31L | PXR | Rouen Airport (LFOP) | St Valery Vittefleur Airport (LFOS) | 2026-06-24 09:31 UTC | 2026-06-24 11:08 UTC | 1h 36m |
| EXS8T | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-06-24 10:19 UTC | 2026-06-24 11:07 UTC | 48m |
| TMN1 | TMN | Auckland International Airport (NZAA) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-24 07:58 UTC | 2026-06-24 11:07 UTC | 3h 8m |
| N845ME |  | Washington County Airport (KAFJ) | Rostraver Airport (KFWQ) | 2026-06-24 10:49 UTC | 2026-06-24 11:05 UTC | 15m |
| JBU716 | JetBlue | Buffalo Niagara International Airport (KBUF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-24 10:00 UTC | 2026-06-24 10:59 UTC | 58m |
| YGU | YGU | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-24 10:13 UTC | 2026-06-24 10:58 UTC | 44m |
| SHA124 | SHA | Manang Airport (VNMA) | Tribhuvan International Airport (VNKT) | 2026-06-24 10:21 UTC | 2026-06-24 10:51 UTC | 29m |
| HBSYP | HBS | Ecuvillens Airport (LSGE) | Ecuvillens Airport (LSGE) | 2026-06-24 10:37 UTC | 2026-06-24 10:50 UTC | 13m |
| AFR256 | Air France | Charles de Gaulle International Airport (LFPG) | Kijang Airport (WIDN) | 2026-06-23 21:39 UTC | 2026-06-24 10:40 UTC | 13h 1m |
| SEKXT | SEK | Borlange Airport (ESSD) | Borlange Airport (ESSD) | 2026-06-24 10:37 UTC | 2026-06-24 10:40 UTC | 3m |
| VOLPE20 | VOL | Pratica Di Mare Airport (LIRE) | Frosinone Military Airport (LIRH) | 2026-06-24 10:14 UTC | 2026-06-24 10:40 UTC | 26m |
| UPS768 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Dallas-Fort Worth International Airport (KDFW) | 2026-06-24 09:00 UTC | 2026-06-24 10:39 UTC | 1h 38m |
| ZAM15 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-24 09:53 UTC | 2026-06-24 10:37 UTC | 44m |
| GCLDA | GCL | Sleap Airport (EGCV) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-06-24 10:11 UTC | 2026-06-24 10:33 UTC | 21m |
| EAI64B | EAI | Dublin Airport (EIDW) | Birmingham International Airport (EGBB) | 2026-06-24 09:43 UTC | 2026-06-24 10:33 UTC | 50m |
| IGO6226 | IndiGo | Indira Gandhi International Airport (VIDP) | Dehradun Airport (VIDN) | 2026-06-24 09:57 UTC | 2026-06-24 10:30 UTC | 33m |
| LHX3VJ | LHX | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-06-24 09:39 UTC | 2026-06-24 10:28 UTC | 48m |
| ZAM12 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-24 09:55 UTC | 2026-06-24 10:26 UTC | 31m |
| SJX235 | SJX | Taiwan Taoyuan International Airport (RCTP) | Chek Lap Kok International Airport (VHHH) | 2026-06-24 09:08 UTC | 2026-06-24 10:24 UTC | 1h 15m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-24 10:15 UTC | 2026-06-24 10:23 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
