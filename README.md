# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_21:41:40_UTC-green)

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

**Latest saved flight:** 2026-08-19 21:41:40 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-19 21:41:40 UTC

- **217,470** saved flights
- **68,571** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **217,470** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,616,940.2 tonnes** estimated CO2 emissions
- **151,706,676 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8708 |
| 2 | SkyWest Airlines | 7783 |
| 3 | EJA | 4238 |
| 4 | IndiGo | 3692 |
| 5 | American Airlines | 3627 |
| 6 | Southwest Airlines | 3454 |
| 7 | Delta Air Lines | 2810 |
| 8 | ENY | 2687 |
| 9 | LATAM Airlines | 2058 |
| 10 | AZU | 1992 |
| 11 | Vueling | 1826 |
| 12 | Lufthansa | 1813 |
| 13 | WIF | 1738 |
| 14 | LXJ | 1719 |
| 15 | easyJet | 1511 |
| 16 | Swiss International | 1448 |
| 17 | AXM | 1417 |
| 18 | United Airlines | 1378 |
| 19 | EJU | 1354 |
| 20 | QLK | 1346 |
| 21 | Alaska Airlines | 1330 |
| 22 | All Nippon Airways | 1304 |
| 23 | VIV | 1191 |
| 24 | GLO | 1182 |
| 25 | PGT | 1178 |
| 26 | Air France | 1177 |
| 27 | WMT | 1142 |
| 28 | JetBlue | 1109 |
| 29 | Wizz Air | 1105 |
| 30 | AEE | 1088 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 183465 |
| 2 | 🇪🇸 ES | 13937 |
| 3 | 🇧🇷 BR | 12540 |
| 4 | 🇦🇺 AU | 12169 |
| 5 | 🇨🇦 CA | 11982 |
| 6 | 🇮🇹 IT | 11555 |
| 7 | 🇮🇳 IN | 11494 |
| 8 | 🇩🇪 DE | 10763 |
| 9 | 🇬🇧 GB | 10212 |
| 10 | 🇨🇴 CO | 8930 |
| 11 | 🇯🇵 JP | 8870 |
| 12 | 🇫🇷 FR | 8665 |
| 13 | 🇬🇷 GR | 6345 |
| 14 | 🇹🇷 TR | 6254 |
| 15 | 🇲🇽 MX | 6072 |
| 16 | 🇨🇭 CH | 5768 |
| 17 | 🇳🇴 NO | 5405 |
| 18 | 🇲🇾 MY | 3744 |
| 19 | 🇿🇦 ZA | 3683 |
| 20 | 🇵🇱 PL | 3592 |
| 21 | 🇹🇭 TH | 3539 |
| 22 | 🇳🇿 NZ | 3002 |
| 23 | 🇵🇭 PH | 2898 |
| 24 | 🇬🇹 GT | 2760 |
| 25 | 🇰🇷 KR | 2608 |
| 26 | 🇭🇷 HR | 2388 |
| 27 | 🇲🇦 MA | 2188 |
| 28 | 🇳🇱 NL | 1940 |
| 29 | 🇲🇪 ME | 1907 |
| 30 | 🇮🇩 ID | 1818 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4571 |
| 2 | Denver International Airport |  | US | 3553 |
| 3 | Tokyo International Airport |  | JP | 2662 |
| 4 | Indira Gandhi International Airport |  | IN | 2628 |
| 5 | Guaymaral Airport |  | CO | 2595 |
| 6 | Harry Reid International Airport |  | US | 2408 |
| 7 | Zurich Airport |  | CH | 2258 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2237 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2211 |
| 10 | La Aurora Airport |  | GT | 2100 |
| 11 | El Dorado International Airport |  | CO | 2035 |
| 12 | Chicago O'Hare International Airport |  | US | 2003 |
| 13 | Salt Lake City International Airport |  | US | 1922 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1897 |
| 15 | Congonhas Airport |  | BR | 1832 |
| 16 | Frankfurt am Main International Airport |  | DE | 1778 |
| 17 | Madrid Barajas International Airport |  | ES | 1702 |
| 18 | Capua Airport |  | IT | 1655 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1638 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1613 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1594 |
| 22 | Macau International Airport |  | MO | 1563 |
| 23 | Malpensa International Airport |  | IT | 1532 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1516 |
| 25 | Charles de Gaulle International Airport |  | FR | 1493 |
| 26 | Charlotte/Douglas International Airport |  | US | 1461 |
| 27 | Kuala Lumpur International Airport |  | MY | 1378 |
| 28 | Ninoy Aquino International Airport |  | PH | 1376 |
| 29 | Barcelona International Airport |  | ES | 1332 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1328 |
| 31 | Bengaluru International Airport |  | IN | 1315 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1298 |
| 33 | Seattle-Tacoma International Airport |  | US | 1287 |
| 34 | Viracopos International Airport |  | BR | 1271 |
| 35 | Calgary International Airport |  | CA | 1224 |
| 36 | Oslo Gardermoen Airport |  | NO | 1205 |
| 37 | Vitoria/Foronda Airport |  | ES | 1204 |
| 38 | Enrique Olaya Herrera Airport |  | CO | 1197 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1173 |
| 40 | Reno/Tahoe International Airport |  | US | 1167 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 775 | 21m | 244 km | 3,263.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 534 | 1h 7m | 770 km | 7,093.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 507 | 24m | 225 km | 1,966.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 491 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 483 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 363 | 27m | 275 km | 1,720.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 318 | 1h 49m | 1,423 km | 7,804.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 316 | 44m | 241 km | 1,312.6 t |
| 11 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 12 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 310 | 1h 7m | 706 km | 3,774.3 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 294 | 22m | 55 km | 279.4 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 285 | 21m | 250 km | 1,231.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 271 | 19m | 99 km | 464.2 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 269 | 1h 38m | 1,156 km | 5,366.4 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 267 | 27m | 215 km | 988.9 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 267 | 24m | 218 km | 1,005.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 258 | 13m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 257 | 1h 14m | 961 km | 4,259.9 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 253 | 31m | 369 km | 1,610.4 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 247 | 19m | 144 km | 614.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 245 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 234 | 1h 49m | 1,304 km | 5,264.4 t |
| 29 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 233 | 44m | 555 km | 2,231.1 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Zhuhai Airport (ZGSD) | 2026-08-19 11:29 UTC | 2026-08-19 21:41 UTC | 10h 12m |
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-19 16:59 UTC | 2026-08-19 21:38 UTC | 4h 38m |
| N432CE |  | Long Beach (Daugherty Field) Airport (KLGB) | Big Bear City Airport (KL35) | 2026-08-19 21:10 UTC | 2026-08-19 21:36 UTC | 26m |
| N3376E |  | Camarillo Airport (KCMA) | Santa Monica Municipal Airport (KSMO) | 2026-08-19 21:11 UTC | 2026-08-19 21:33 UTC | 21m |
| N530LP |  | Boise Air Trml/Gowen Field (KBOI) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-19 18:33 UTC | 2026-08-19 21:33 UTC | 3h 0m |
| N300PL |  | Flying Cloud Airport (KFCM) | Cox-Coyour Memorial Field (59MN) | 2026-08-19 20:31 UTC | 2026-08-19 21:27 UTC | 56m |
| N789LE |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-19 21:00 UTC | 2026-08-19 21:21 UTC | 21m |
| N959RW |  | Hopewell Airpark (90NY) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-19 20:33 UTC | 2026-08-19 21:20 UTC | 47m |
| FXC66 | FXC | Elizabeth Field (K0B8) | Laguardia Airport (KLGA) | 2026-08-19 20:19 UTC | 2026-08-19 21:20 UTC | 1h 1m |
| N930F |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Palo Alto Airport (KPAO) | 2026-08-19 20:07 UTC | 2026-08-19 21:18 UTC | 1h 11m |
| N75HF |  | Willow Run Airport (KYIP) | Indian Springs Airport (3TN0) | 2026-08-19 20:25 UTC | 2026-08-19 21:16 UTC | 51m |
| N716LD |  | Spirit Of St Louis Airport (KSUS) | Twentynine Palms Airport (KTNP) | 2026-08-19 17:54 UTC | 2026-08-19 21:16 UTC | 3h 22m |
| N2441D |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-08-19 21:00 UTC | 2026-08-19 21:16 UTC | 16m |
| CPA260 | Cathay Pacific | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-08-19 10:40 UTC | 2026-08-19 21:16 UTC | 10h 35m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-08-19 10:59 UTC | 2026-08-19 21:15 UTC | 10h 15m |
| N336MC |  | Lewis University Airport (KLOT) | Corn Field (IL95) | 2026-08-19 20:39 UTC | 2026-08-19 21:14 UTC | 35m |
| N488K |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-08-19 20:44 UTC | 2026-08-19 21:14 UTC | 30m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | Harrington Airport (20ID) | 2026-08-19 21:06 UTC | 2026-08-19 21:14 UTC | 7m |
| N555BG |  | North Fork Valley Airport (K7V2) | Telluride Regional Airport (KTEX) | 2026-08-19 20:58 UTC | 2026-08-19 21:13 UTC | 14m |
| N855MK |  | Trenton Mercer Airport (KTTN) | Linden Airport (KLDJ) | 2026-08-19 19:52 UTC | 2026-08-19 21:13 UTC | 1h 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
