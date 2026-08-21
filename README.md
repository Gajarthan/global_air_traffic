# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_23:01:28_UTC-green)

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

**Latest saved flight:** 2026-08-21 23:01:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-21 23:01:28 UTC

- **224,132** saved flights
- **69,944** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **224,132** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,699,835.4 tonnes** estimated CO2 emissions
- **156,512,199 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8985 |
| 2 | SkyWest Airlines | 7981 |
| 3 | EJA | 4350 |
| 4 | IndiGo | 3781 |
| 5 | American Airlines | 3700 |
| 6 | Southwest Airlines | 3509 |
| 7 | Delta Air Lines | 2873 |
| 8 | ENY | 2756 |
| 9 | LATAM Airlines | 2134 |
| 10 | AZU | 2070 |
| 11 | Vueling | 1890 |
| 12 | Lufthansa | 1842 |
| 13 | WIF | 1787 |
| 14 | LXJ | 1772 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1491 |
| 17 | AXM | 1467 |
| 18 | United Airlines | 1410 |
| 19 | EJU | 1405 |
| 20 | QLK | 1405 |
| 21 | Alaska Airlines | 1359 |
| 22 | All Nippon Airways | 1333 |
| 23 | GLO | 1240 |
| 24 | PGT | 1229 |
| 25 | VIV | 1220 |
| 26 | Air France | 1214 |
| 27 | WMT | 1194 |
| 28 | Wizz Air | 1154 |
| 29 | JetBlue | 1125 |
| 30 | AEE | 1117 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188297 |
| 2 | 🇪🇸 ES | 14363 |
| 3 | 🇧🇷 BR | 13026 |
| 4 | 🇦🇺 AU | 12657 |
| 5 | 🇨🇦 CA | 12430 |
| 6 | 🇮🇹 IT | 11972 |
| 7 | 🇮🇳 IN | 11793 |
| 8 | 🇩🇪 DE | 11026 |
| 9 | 🇬🇧 GB | 10515 |
| 10 | 🇨🇴 CO | 9246 |
| 11 | 🇯🇵 JP | 9056 |
| 12 | 🇫🇷 FR | 8933 |
| 13 | 🇹🇷 TR | 6535 |
| 14 | 🇬🇷 GR | 6531 |
| 15 | 🇲🇽 MX | 6227 |
| 16 | 🇨🇭 CH | 5889 |
| 17 | 🇳🇴 NO | 5560 |
| 18 | 🇲🇾 MY | 3887 |
| 19 | 🇿🇦 ZA | 3861 |
| 20 | 🇹🇭 TH | 3774 |
| 21 | 🇵🇱 PL | 3717 |
| 22 | 🇳🇿 NZ | 3104 |
| 23 | 🇵🇭 PH | 3027 |
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
| 1 | Dallas-Fort Worth International Airport |  | US | 4701 |
| 2 | Denver International Airport |  | US | 3660 |
| 3 | Tokyo International Airport |  | JP | 2715 |
| 4 | Indira Gandhi International Airport |  | IN | 2713 |
| 5 | Guaymaral Airport |  | CO | 2628 |
| 6 | Harry Reid International Airport |  | US | 2458 |
| 7 | Zurich Airport |  | CH | 2321 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2299 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2268 |
| 10 | La Aurora Airport |  | GT | 2167 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1967 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1923 |
| 15 | Congonhas Airport |  | BR | 1905 |
| 16 | Frankfurt am Main International Airport |  | DE | 1810 |
| 17 | Madrid Barajas International Airport |  | ES | 1754 |
| 18 | Capua Airport |  | IT | 1717 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1674 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1662 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1630 |
| 22 | Macau International Airport |  | MO | 1589 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1571 |
| 24 | Malpensa International Airport |  | IT | 1570 |
| 25 | Charles de Gaulle International Airport |  | FR | 1547 |
| 26 | Charlotte/Douglas International Airport |  | US | 1480 |
| 27 | Ninoy Aquino International Airport |  | PH | 1442 |
| 28 | Kuala Lumpur International Airport |  | MY | 1420 |
| 29 | Barcelona International Airport |  | ES | 1385 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1361 |
| 31 | Bengaluru International Airport |  | IN | 1334 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1330 |
| 33 | Seattle-Tacoma International Airport |  | US | 1322 |
| 34 | Viracopos International Airport |  | BR | 1320 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1275 |
| 37 | Oslo Gardermoen Airport |  | NO | 1251 |
| 38 | Vitoria/Foronda Airport |  | ES | 1240 |
| 39 | Don Mueang International Airport |  | TH | 1239 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 806 | 21m | 244 km | 3,393.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 557 | 1h 7m | 770 km | 7,399.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 538 | 24m | 225 km | 2,087.2 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
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
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 253 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASP869 | ASP | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Toronto Pearson International Airport (CYYZ) | 2026-08-21 22:08 UTC | 2026-08-21 23:01 UTC | 53m |
| FFL1109 | FFL | Philadelphia International Airport (KPHL) | Morristown Municipal Airport (KMMU) | 2026-08-21 22:23 UTC | 2026-08-21 22:54 UTC | 31m |
| ZKICU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-21 22:37 UTC | 2026-08-21 22:52 UTC | 15m |
| CXK569 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-08-21 21:41 UTC | 2026-08-21 22:50 UTC | 1h 9m |
| N3033T |  | Purdue University Airport (KLAF) | Purdue University Airport (KLAF) | 2026-08-21 22:49 UTC | 2026-08-21 22:49 UTC | 0m |
| CFR83 | CFR | Columbia Airport (KO22) | Columbia Airport (KO22) | 2026-08-21 22:45 UTC | 2026-08-21 22:48 UTC | 2m |
| ES805 |  | Sacramento Mather Airport (KMHR) | Stockton Metro Airport (KSCK) | 2026-08-21 21:14 UTC | 2026-08-21 22:45 UTC | 1h 31m |
| N7108G |  | Little Falls/Morrison County-Lindbergh Field (KLXL) | Little Falls/Morrison County-Lindbergh Field (KLXL) | 2026-08-21 22:29 UTC | 2026-08-21 22:43 UTC | 14m |
| CNK645 | CNK | Bellingham International Airport (KBLI) | Calgary International Airport (CYYC) | 2026-08-21 21:36 UTC | 2026-08-21 22:35 UTC | 58m |
| N892KC |  | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-08-21 21:28 UTC | 2026-08-21 22:29 UTC | 1h 0m |
| XSN82 | XSN | Gnoss Field (KDVO) | Truckee-Tahoe Airport (KTRK) | 2026-08-21 21:58 UTC | 2026-08-21 22:28 UTC | 30m |
| BRG2644 | BRG | Ralph Wien Memorial Airport (PAOT) | Deering Airport (PADE) | 2026-08-21 21:59 UTC | 2026-08-21 22:25 UTC | 25m |
| RMX5303 | RMX | Almaza Air Force Base (HEAZ) | Almaza Air Force Base (HEAZ) | 2026-08-21 22:23 UTC | 2026-08-21 22:24 UTC | 0m |
| N308PH |  | Medina Municipal Airport (K1G5) | Ashland County Airport (K3G4) | 2026-08-21 22:11 UTC | 2026-08-21 22:24 UTC | 12m |
| CNS1919 | CNS | Paso Robles Municipal Airport (KPRB) | 8CL0 (8CL0) | 2026-08-21 21:38 UTC | 2026-08-21 22:15 UTC | 36m |
| N711DE |  | Napa County Airport (KAPC) | Truckee-Tahoe Airport (KTRK) | 2026-08-21 21:35 UTC | 2026-08-21 22:14 UTC | 38m |
| N882KB |  | Charles M Schulz/Sonoma County Airport (KSTS) | Lake Tahoe Airport (KTVL) | 2026-08-21 21:55 UTC | 2026-08-21 22:13 UTC | 18m |
| N917SH |  | Joe Foss Field (KFSD) | SD75 (SD75) | 2026-08-21 21:49 UTC | 2026-08-21 22:11 UTC | 22m |
| AFR570 | Air France | Charles de Gaulle International Airport (LFPG) | HE42 (HE42) | 2026-08-21 18:27 UTC | 2026-08-21 22:11 UTC | 3h 43m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-08-21 21:59 UTC | 2026-08-21 22:10 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
