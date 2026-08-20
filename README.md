# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_17:35:51_UTC-green)

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

**Latest saved flight:** 2026-08-20 17:35:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 17:35:51 UTC

- **219,967** saved flights
- **69,038** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **219,967** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,648,519.8 tonnes** estimated CO2 emissions
- **153,537,378 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8822 |
| 2 | SkyWest Airlines | 7835 |
| 3 | EJA | 4264 |
| 4 | IndiGo | 3732 |
| 5 | American Airlines | 3647 |
| 6 | Southwest Airlines | 3476 |
| 7 | Delta Air Lines | 2834 |
| 8 | ENY | 2708 |
| 9 | LATAM Airlines | 2088 |
| 10 | AZU | 2014 |
| 11 | Vueling | 1852 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1761 |
| 14 | LXJ | 1734 |
| 15 | easyJet | 1526 |
| 16 | Swiss International | 1465 |
| 17 | AXM | 1444 |
| 18 | United Airlines | 1383 |
| 19 | QLK | 1375 |
| 20 | EJU | 1372 |
| 21 | Alaska Airlines | 1340 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1202 |
| 24 | VIV | 1200 |
| 25 | Air France | 1192 |
| 26 | PGT | 1191 |
| 27 | WMT | 1160 |
| 28 | Wizz Air | 1121 |
| 29 | JetBlue | 1116 |
| 30 | AEE | 1103 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 185014 |
| 2 | 🇪🇸 ES | 14110 |
| 3 | 🇧🇷 BR | 12701 |
| 4 | 🇦🇺 AU | 12418 |
| 5 | 🇨🇦 CA | 12126 |
| 6 | 🇮🇹 IT | 11716 |
| 7 | 🇮🇳 IN | 11634 |
| 8 | 🇩🇪 DE | 10881 |
| 9 | 🇬🇧 GB | 10338 |
| 10 | 🇨🇴 CO | 9027 |
| 11 | 🇯🇵 JP | 8963 |
| 12 | 🇫🇷 FR | 8761 |
| 13 | 🇬🇷 GR | 6420 |
| 14 | 🇹🇷 TR | 6333 |
| 15 | 🇲🇽 MX | 6109 |
| 16 | 🇨🇭 CH | 5824 |
| 17 | 🇳🇴 NO | 5475 |
| 18 | 🇲🇾 MY | 3819 |
| 19 | 🇿🇦 ZA | 3761 |
| 20 | 🇹🇭 TH | 3655 |
| 21 | 🇵🇱 PL | 3650 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2785 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2440 |
| 27 | 🇲🇦 MA | 2216 |
| 28 | 🇳🇱 NL | 1957 |
| 29 | 🇲🇪 ME | 1945 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4614 |
| 2 | Denver International Airport |  | US | 3587 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2667 |
| 5 | Guaymaral Airport |  | CO | 2598 |
| 6 | Harry Reid International Airport |  | US | 2422 |
| 7 | Zurich Airport |  | CH | 2285 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2257 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2235 |
| 10 | La Aurora Airport |  | GT | 2122 |
| 11 | El Dorado International Airport |  | CO | 2058 |
| 12 | Chicago O'Hare International Airport |  | US | 2013 |
| 13 | Salt Lake City International Airport |  | US | 1938 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1902 |
| 15 | Congonhas Airport |  | BR | 1860 |
| 16 | Frankfurt am Main International Airport |  | DE | 1795 |
| 17 | Madrid Barajas International Airport |  | ES | 1728 |
| 18 | Capua Airport |  | IT | 1681 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1647 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1623 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1616 |
| 22 | Macau International Airport |  | MO | 1580 |
| 23 | Malpensa International Airport |  | IT | 1546 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1513 |
| 26 | Charlotte/Douglas International Airport |  | US | 1464 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1402 |
| 29 | Barcelona International Airport |  | ES | 1350 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1337 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1306 |
| 33 | Seattle-Tacoma International Airport |  | US | 1301 |
| 34 | Viracopos International Airport |  | BR | 1288 |
| 35 | Calgary International Airport |  | CA | 1238 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1221 |
| 37 | Oslo Gardermoen Airport |  | NO | 1221 |
| 38 | Vitoria/Foronda Airport |  | ES | 1221 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1182 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1061 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 787 | 21m | 244 km | 3,313.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 493 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 370 | 27m | 275 km | 1,753.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 324 | 1h 50m | 1,423 km | 7,951.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 322 | 44m | 241 km | 1,337.5 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 272 | 24m | 218 km | 1,024.7 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 259 | 1h 14m | 961 km | 4,293.1 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 246 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SL82 |  | Rota Naval Station Airport (LERT) | Gibraltar Airport (LXGB) | 2026-08-20 15:59 UTC | 2026-08-20 17:35 UTC | 1h 36m |
| N40EA |  | 22LL (22LL) | Skydive Chicago Airport (K8N2) | 2026-08-20 16:55 UTC | 2026-08-20 17:35 UTC | 39m |
| N668PD |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Los Alamitos Army Air Field (KSLI) | 2026-08-20 16:24 UTC | 2026-08-20 17:31 UTC | 1h 6m |
| DLH5CW | Lufthansa | Leipzig Halle Airport (EDDP) | Frankfurt am Main International Airport (EDDF) | 2026-08-20 16:54 UTC | 2026-08-20 17:29 UTC | 35m |
| DILIA | DIL | Hamburg Airport (EDDH) | Antwerp International Airport (Deurne) (EBAW) | 2026-08-20 16:25 UTC | 2026-08-20 17:29 UTC | 1h 3m |
| DHX729 | DHX | Bahrain International Airport (OBBI) | Macau International Airport (VMMC) | 2026-08-20 09:22 UTC | 2026-08-20 17:24 UTC | 8h 1m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-20 17:06 UTC | 2026-08-20 17:22 UTC | 16m |
| CAP2883 | CAP | Laconia Municipal Airport (KLCI) | Laconia Municipal Airport (KLCI) | 2026-08-20 16:13 UTC | 2026-08-20 17:18 UTC | 1h 4m |
| N894SA |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-08-20 16:44 UTC | 2026-08-20 17:15 UTC | 30m |
| N387CS |  | Centennial Airport (KAPA) | Bijou Bottom Strip (9CO8) | 2026-08-20 16:28 UTC | 2026-08-20 17:12 UTC | 43m |
| AUA26 | Austrian Airlines | Narita International Airport (RJAA) | UKFB (UKFB) | 2026-08-20 04:47 UTC | 2026-08-20 17:11 UTC | 12h 24m |
| N751EC |  | Fort Worth Meacham International Airport (KFTW) | Addison Airport (KADS) | 2026-08-20 16:59 UTC | 2026-08-20 17:10 UTC | 10m |
| VTNJB | VTN | Juhu Aerodrome (VAJJ) | HAL Airport (VOBG) | 2026-08-20 15:00 UTC | 2026-08-20 17:07 UTC | 2h 6m |
| N18ZD |  | Greeley-Weld County Airport (KGXY) | Dalhart Municipal Airport (KDHT) | 2026-08-20 16:13 UTC | 2026-08-20 16:56 UTC | 43m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-20 16:37 UTC | 2026-08-20 16:55 UTC | 18m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-08-20 16:02 UTC | 2026-08-20 16:51 UTC | 48m |
| OEGRB | OEG | Leipzig Halle Airport (EDDP) | Cologne Bonn Airport (EDDK) | 2026-08-20 16:05 UTC | 2026-08-20 16:50 UTC | 44m |
| UPS118 | UPS | Narita International Airport (RJAA) | Shenzhen Bao'an International Airport (ZGSZ) | 2026-08-20 12:48 UTC | 2026-08-20 16:50 UTC | 4h 1m |
| CXK225 | CXK | Georgetown Executive Airport (KGTU) | Easterwood Field (KCLL) | 2026-08-20 16:03 UTC | 2026-08-20 16:50 UTC | 46m |
| N345WP |  | Centennial Airport (KAPA) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-20 15:21 UTC | 2026-08-20 16:49 UTC | 1h 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
