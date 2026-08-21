# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_22:11:21_UTC-green)

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

**Latest saved flight:** 2026-08-21 22:11:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 22:11:21 UTC

- **223,998** saved flights
- **69,915** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **223,998** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,698,484.5 tonnes** estimated CO2 emissions
- **156,433,884 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8981 |
| 2 | SkyWest Airlines | 7972 |
| 3 | EJA | 4342 |
| 4 | IndiGo | 3781 |
| 5 | American Airlines | 3699 |
| 6 | Southwest Airlines | 3508 |
| 7 | Delta Air Lines | 2871 |
| 8 | ENY | 2754 |
| 9 | LATAM Airlines | 2131 |
| 10 | AZU | 2062 |
| 11 | Vueling | 1889 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1769 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1491 |
| 17 | AXM | 1467 |
| 18 | United Airlines | 1407 |
| 19 | QLK | 1405 |
| 20 | EJU | 1404 |
| 21 | Alaska Airlines | 1359 |
| 22 | All Nippon Airways | 1333 |
| 23 | GLO | 1236 |
| 24 | PGT | 1228 |
| 25 | VIV | 1218 |
| 26 | Air France | 1214 |
| 27 | WMT | 1194 |
| 28 | Wizz Air | 1154 |
| 29 | JetBlue | 1125 |
| 30 | AEE | 1117 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188154 |
| 2 | 🇪🇸 ES | 14359 |
| 3 | 🇧🇷 BR | 12994 |
| 4 | 🇦🇺 AU | 12657 |
| 5 | 🇨🇦 CA | 12404 |
| 6 | 🇮🇹 IT | 11967 |
| 7 | 🇮🇳 IN | 11793 |
| 8 | 🇩🇪 DE | 11026 |
| 9 | 🇬🇧 GB | 10514 |
| 10 | 🇨🇴 CO | 9243 |
| 11 | 🇯🇵 JP | 9054 |
| 12 | 🇫🇷 FR | 8933 |
| 13 | 🇹🇷 TR | 6534 |
| 14 | 🇬🇷 GR | 6531 |
| 15 | 🇲🇽 MX | 6216 |
| 16 | 🇨🇭 CH | 5889 |
| 17 | 🇳🇴 NO | 5560 |
| 18 | 🇲🇾 MY | 3887 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3717 |
| 22 | 🇳🇿 NZ | 3096 |
| 23 | 🇵🇭 PH | 3026 |
| 24 | 🇬🇹 GT | 2842 |
| 25 | 🇰🇷 KR | 2657 |
| 26 | 🇭🇷 HR | 2503 |
| 27 | 🇲🇦 MA | 2256 |
| 28 | 🇳🇱 NL | 1992 |
| 29 | 🇲🇪 ME | 1989 |
| 30 | 🇮🇩 ID | 1909 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4694 |
| 2 | Denver International Airport |  | US | 3655 |
| 3 | Tokyo International Airport |  | JP | 2714 |
| 4 | Indira Gandhi International Airport |  | IN | 2713 |
| 5 | Guaymaral Airport |  | CO | 2628 |
| 6 | Harry Reid International Airport |  | US | 2457 |
| 7 | Zurich Airport |  | CH | 2321 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2294 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2268 |
| 10 | La Aurora Airport |  | GT | 2167 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1967 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1923 |
| 15 | Congonhas Airport |  | BR | 1902 |
| 16 | Frankfurt am Main International Airport |  | DE | 1810 |
| 17 | Madrid Barajas International Airport |  | ES | 1754 |
| 18 | Capua Airport |  | IT | 1717 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1673 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1658 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1630 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1569 |
| 25 | Charles de Gaulle International Airport |  | FR | 1547 |
| 26 | Charlotte/Douglas International Airport |  | US | 1479 |
| 27 | Ninoy Aquino International Airport |  | PH | 1441 |
| 28 | Kuala Lumpur International Airport |  | MY | 1420 |
| 29 | Barcelona International Airport |  | ES | 1383 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1359 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1327 |
| 33 | Seattle-Tacoma International Airport |  | US | 1321 |
| 34 | Viracopos International Airport |  | BR | 1315 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1301 |
| 36 | Calgary International Airport |  | CA | 1268 |
| 37 | Oslo Gardermoen Airport |  | NO | 1251 |
| 38 | Vitoria/Foronda Airport |  | ES | 1240 |
| 39 | Don Mueang International Airport |  | TH | 1239 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 806 | 21m | 244 km | 3,393.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 556 | 1h 7m | 770 km | 7,386.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 526 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 509 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 377 | 27m | 275 km | 1,786.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 353 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 333 | 1h 50m | 1,423 km | 8,172.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 283 | 1h 39m | 1,156 km | 5,645.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 279 | 24m | 218 km | 1,051.1 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 278 | 19m | 99 km | 476.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 20 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 274 | 44m | 555 km | 2,623.7 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 252 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 243 | 1h 50m | 1,304 km | 5,466.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AFR570 | Air France | Charles de Gaulle International Airport (LFPG) | HE42 (HE42) | 2026-08-21 18:27 UTC | 2026-08-21 22:11 UTC | 3h 43m |
| 6407R |  | 89LL (89LL) | 89LL (89LL) | 2026-08-21 21:49 UTC | 2026-08-21 22:10 UTC | 20m |
| CAPX313 | CAP | Stubbs Strip (TS73) | Stephens County Airport (KBKD) | 2026-08-21 21:49 UTC | 2026-08-21 22:09 UTC | 19m |
| N8188Z |  | Hazleton Regional Airport (KHZL) | Hazleton Regional Airport (KHZL) | 2026-08-21 21:44 UTC | 2026-08-21 22:09 UTC | 24m |
| N23HW |  | Desert Wings Sky Ranch Airport (04CL) | Barstow-Daggett Airport (KDAG) | 2026-08-21 19:29 UTC | 2026-08-21 22:07 UTC | 2h 37m |
| N4438U |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-08-21 21:07 UTC | 2026-08-21 22:03 UTC | 55m |
| KSF25 | KSF | Kent State University Airport (K1G3) | Akron-Canton Regional Airport (KCAK) | 2026-08-21 21:14 UTC | 2026-08-21 21:59 UTC | 45m |
| CGPPQ | CGP | Nobel / Lumsden Air Park (CNL7) | Brampton Airport (CNC3) | 2026-08-21 21:04 UTC | 2026-08-21 21:54 UTC | 50m |
| AMMO93 | AMM | California City Municipal Airport (KL71) | Boron Airstrip (57CL) | 2026-08-21 21:31 UTC | 2026-08-21 21:54 UTC | 22m |
| N5158J |  | Vowers Ranch Airport (WY29) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-08-21 21:39 UTC | 2026-08-21 21:53 UTC | 14m |
| N5218F |  | Zamperini Field (KTOA) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-08-21 21:35 UTC | 2026-08-21 21:48 UTC | 13m |
| N |  | Port Alberni Airport (CBS8) | Vancouver International Airport (CYVR) | 2026-08-21 21:17 UTC | 2026-08-21 21:48 UTC | 30m |
| SAS7956 | Scandinavian Airlines | Ohrid St. Paul the Apostle Airport (LWOH) | Khrabrovo Airport (UMKK) | 2026-08-21 19:42 UTC | 2026-08-21 21:46 UTC | 2h 4m |
| TKR103 | TKR | Boundary County Airport (K65S) | Coeur D'Alene Airport (KCOE) | 2026-08-21 21:26 UTC | 2026-08-21 21:42 UTC | 15m |
| SCU28 | SCU | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | 2026-08-21 21:39 UTC | 2026-08-21 21:39 UTC | 0m |
| N23US |  | Monterey Regional Airport (KMRY) | Santa Barbara Municipal Airport (KSBA) | 2026-08-21 20:16 UTC | 2026-08-21 21:37 UTC | 1h 21m |
| CGLTG | CGL | Saskatoon John G. Diefenbaker International Airport (CYXE) | Craik Airport (CJC2) | 2026-08-21 21:15 UTC | 2026-08-21 21:37 UTC | 22m |
| N401FN |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-21 21:22 UTC | 2026-08-21 21:37 UTC | 15m |
|  |  | Brookeridge Air Park (LL22) | Brookeridge Air Park (LL22) | 2026-08-21 21:33 UTC | 2026-08-21 21:36 UTC | 3m |
| EJA471 | EJA | Merced Yosemite Regional Airport (KMCE) | Edwards Grass Strip (2KS3) | 2026-08-21 19:09 UTC | 2026-08-21 21:32 UTC | 2h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
