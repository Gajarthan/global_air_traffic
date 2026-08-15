# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_16:45:42_UTC-green)

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

**Latest saved flight:** 2026-08-15 16:45:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 16:45:42 UTC

- **199,068** saved flights
- **62,203** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,068** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,377,366.7 tonnes** estimated CO2 emissions
- **137,818,358 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7921 |
| 2 | SkyWest Airlines | 7130 |
| 3 | EJA | 3904 |
| 4 | IndiGo | 3443 |
| 5 | Southwest Airlines | 3077 |
| 6 | American Airlines | 3060 |
| 7 | ENY | 2456 |
| 8 | Delta Air Lines | 2354 |
| 9 | LATAM Airlines | 1875 |
| 10 | AZU | 1808 |
| 11 | Lufthansa | 1702 |
| 12 | Vueling | 1673 |
| 13 | WIF | 1639 |
| 14 | LXJ | 1578 |
| 15 | easyJet | 1367 |
| 16 | Swiss International | 1346 |
| 17 | AXM | 1308 |
| 18 | EJU | 1232 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1098 |
| 23 | GLO | 1082 |
| 24 | Air France | 1055 |
| 25 | PGT | 1048 |
| 26 | AEE | 1025 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1008 |
| 29 | WMT | 1006 |
| 30 | Wizz Air | 986 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168655 |
| 2 | 🇪🇸 ES | 12863 |
| 3 | 🇧🇷 BR | 11489 |
| 4 | 🇦🇺 AU | 11148 |
| 5 | 🇨🇦 CA | 10874 |
| 6 | 🇮🇳 IN | 10758 |
| 7 | 🇮🇹 IT | 10439 |
| 8 | 🇩🇪 DE | 9881 |
| 9 | 🇬🇧 GB | 9360 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7936 |
| 12 | 🇨🇴 CO | 7883 |
| 13 | 🇬🇷 GR | 5874 |
| 14 | 🇲🇽 MX | 5622 |
| 15 | 🇹🇷 TR | 5508 |
| 16 | 🇨🇭 CH | 5401 |
| 17 | 🇳🇴 NO | 5073 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3366 |
| 20 | 🇵🇱 PL | 3294 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2546 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2114 |
| 27 | 🇲🇦 MA | 2015 |
| 28 | 🇳🇱 NL | 1792 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4134 |
| 2 | Denver International Airport |  | US | 3231 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2458 |
| 5 | Indira Gandhi International Airport |  | IN | 2440 |
| 6 | Harry Reid International Airport |  | US | 2270 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2106 |
| 8 | Zurich Airport |  | CH | 2106 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2058 |
| 10 | La Aurora Airport |  | GT | 1950 |
| 11 | El Dorado International Airport |  | CO | 1830 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1767 |
| 13 | Salt Lake City International Airport |  | US | 1765 |
| 14 | Chicago O'Hare International Airport |  | US | 1742 |
| 15 | Congonhas Airport |  | BR | 1682 |
| 16 | Frankfurt am Main International Airport |  | DE | 1676 |
| 17 | Madrid Barajas International Airport |  | ES | 1567 |
| 18 | Macau International Airport |  | MO | 1536 |
| 19 | Capua Airport |  | IT | 1524 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1511 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1461 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1438 |
| 23 | Malpensa International Airport |  | IT | 1387 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1382 |
| 25 | Charles de Gaulle International Airport |  | FR | 1370 |
| 26 | Charlotte/Douglas International Airport |  | US | 1311 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1242 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1212 |
| 32 | Barcelona International Airport |  | ES | 1199 |
| 33 | Viracopos International Airport |  | BR | 1162 |
| 34 | Seattle-Tacoma International Airport |  | US | 1140 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Oslo Gardermoen Airport |  | NO | 1118 |
| 37 | Reno/Tahoe International Airport |  | US | 1117 |
| 38 | Daniel K Inouye International Airport |  | US | 1102 |
| 39 | Vitoria/Foronda Airport |  | ES | 1101 |
| 40 | Tenerife Norte Airport |  | ES | 1091 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1013 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 365 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 336 | 27m | 275 km | 1,592.2 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 291 | 1h 49m | 1,423 km | 7,141.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 284 | 22m | 55 km | 269.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 242 | 1h 15m | 961 km | 4,011.3 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 233 | 19m | 144 km | 579.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 216 | 28m | 152 km | 564.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1317T |  | K4A7 (K4A7) | Thomaston-Upson County Airport (KOPN) | 2026-08-15 16:13 UTC | 2026-08-15 16:45 UTC | 31m |
| N2369X |  | Pompano Beach Airpark (KPMP) | Pompano Beach Airpark (KPMP) | 2026-08-15 15:50 UTC | 2026-08-15 16:43 UTC | 53m |
| FLE601 | FLE | Toronto Pearson International Airport (CYYZ) | Vancouver International Airport (CYVR) | 2026-08-15 11:49 UTC | 2026-08-15 16:39 UTC | 4h 49m |
| N454X |  | Bridgeport/Sikorsky Airport (KBDR) | Waterbury-Oxford Airport (KOXC) | 2026-08-15 15:28 UTC | 2026-08-15 16:30 UTC | 1h 2m |
| N54FA |  | Wings Field (KLOM) | Wings Field (KLOM) | 2026-08-15 15:38 UTC | 2026-08-15 16:26 UTC | 47m |
| N930AA |  | Delta Regional Airport (KDRP) | West Memphis Municipal Airport (KAWM) | 2026-08-15 16:09 UTC | 2026-08-15 16:25 UTC | 15m |
| N1900B |  | Raleigh-Durham International Airport (KRDU) | Auburn University Regional Airport (KAUO) | 2026-08-15 15:26 UTC | 2026-08-15 16:25 UTC | 58m |
| N5QD |  | 0PA0 (0PA0) | 0PA0 (0PA0) | 2026-08-15 16:21 UTC | 2026-08-15 16:25 UTC | 3m |
| IFJ42A | IFJ | Viseu Airport (LPVZ) | Viseu Airport (LPVZ) | 2026-08-15 14:53 UTC | 2026-08-15 16:24 UTC | 1h 31m |
| CPA253 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | UKFB (UKFB) | 2026-08-15 05:41 UTC | 2026-08-15 16:23 UTC | 10h 41m |
| N5721T |  | Boeing Field/King County International Airport (KBFI) | Renton Municipal Airport (KRNT) | 2026-08-15 15:41 UTC | 2026-08-15 16:21 UTC | 39m |
| N69FX |  | Keflavik International Airport (BIKF) | Bangor International Airport (KBGR) | 2026-08-15 10:23 UTC | 2026-08-15 16:20 UTC | 5h 56m |
| FHDSA | FHD | Vannes-Meucon Airport (LFRV) | Vannes-Meucon Airport (LFRV) | 2026-08-15 16:00 UTC | 2026-08-15 16:19 UTC | 19m |
| N828CF |  | Shawano Municipal Airport (KEZS) | Shawano Municipal Airport (KEZS) | 2026-08-15 16:13 UTC | 2026-08-15 16:19 UTC | 5m |
| N252JM |  | North Perry Airport (KHWO) | Fort Lauderdale Executive Airport (KFXE) | 2026-08-15 15:41 UTC | 2026-08-15 16:16 UTC | 35m |
| N654PD |  | Rice Lake Regional/Carl's Field (KRPD) | St Paul Downtown Holman Field (KSTP) | 2026-08-15 15:51 UTC | 2026-08-15 16:12 UTC | 21m |
| AM295 |  | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-08-15 15:19 UTC | 2026-08-15 16:09 UTC | 49m |
| CGRQH | CGR | Prince George Airport (CYXS) | Prince George Airport (CYXS) | 2026-08-15 15:36 UTC | 2026-08-15 16:08 UTC | 31m |
| N640DF |  | Larned-Pawnee County Airport (KLQR) | Prichard Airstrip (1KS4) | 2026-08-15 15:43 UTC | 2026-08-15 16:05 UTC | 22m |
| N954JF |  | Burnet Municipal/Kate Craddock Field (KBMQ) | Burnet Municipal/Kate Craddock Field (KBMQ) | 2026-08-15 15:55 UTC | 2026-08-15 16:03 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
