# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_09:34:29_UTC-green)

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

**Latest saved flight:** 2026-08-25 09:34:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 09:34:29 UTC

- **234,623** saved flights
- **71,878** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **234,623** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,826,500.6 tonnes** estimated CO2 emissions
- **163,855,105 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9404 |
| 2 | SkyWest Airlines | 8299 |
| 3 | EJA | 4553 |
| 4 | IndiGo | 3968 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3599 |
| 7 | Delta Air Lines | 2991 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2253 |
| 10 | AZU | 2184 |
| 11 | Vueling | 2008 |
| 12 | Lufthansa | 1907 |
| 13 | WIF | 1863 |
| 14 | LXJ | 1844 |
| 15 | easyJet | 1634 |
| 16 | AXM | 1571 |
| 17 | Swiss International | 1570 |
| 18 | EJU | 1500 |
| 19 | QLK | 1496 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1399 |
| 23 | GLO | 1306 |
| 24 | WMT | 1301 |
| 25 | VIV | 1294 |
| 26 | PGT | 1279 |
| 27 | Air France | 1272 |
| 28 | Wizz Air | 1242 |
| 29 | AEE | 1166 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195104 |
| 2 | 🇪🇸 ES | 15073 |
| 3 | 🇧🇷 BR | 13686 |
| 4 | 🇦🇺 AU | 13316 |
| 5 | 🇨🇦 CA | 12980 |
| 6 | 🇮🇹 IT | 12741 |
| 7 | 🇮🇳 IN | 12351 |
| 8 | 🇩🇪 DE | 11554 |
| 9 | 🇬🇧 GB | 11043 |
| 10 | 🇨🇴 CO | 9854 |
| 11 | 🇯🇵 JP | 9522 |
| 12 | 🇫🇷 FR | 9385 |
| 13 | 🇹🇷 TR | 6951 |
| 14 | 🇬🇷 GR | 6903 |
| 15 | 🇲🇽 MX | 6527 |
| 16 | 🇨🇭 CH | 6250 |
| 17 | 🇳🇴 NO | 5789 |
| 18 | 🇲🇾 MY | 4200 |
| 19 | 🇹🇭 TH | 4181 |
| 20 | 🇿🇦 ZA | 4095 |
| 21 | 🇵🇱 PL | 3910 |
| 22 | 🇳🇿 NZ | 3247 |
| 23 | 🇵🇭 PH | 3232 |
| 24 | 🇬🇹 GT | 2935 |
| 25 | 🇰🇷 KR | 2749 |
| 26 | 🇭🇷 HR | 2693 |
| 27 | 🇲🇦 MA | 2380 |
| 28 | 🇲🇪 ME | 2166 |
| 29 | 🇳🇱 NL | 2103 |
| 30 | 🇮🇩 ID | 2051 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4874 |
| 2 | Denver International Airport |  | US | 3799 |
| 3 | Indira Gandhi International Airport |  | IN | 2860 |
| 4 | Tokyo International Airport |  | JP | 2834 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2517 |
| 7 | Zurich Airport |  | CH | 2451 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2396 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2350 |
| 10 | La Aurora Airport |  | GT | 2236 |
| 11 | El Dorado International Airport |  | CO | 2197 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2069 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1973 |
| 16 | Frankfurt am Main International Airport |  | DE | 1868 |
| 17 | Capua Airport |  | IT | 1847 |
| 18 | Madrid Barajas International Airport |  | ES | 1844 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1765 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1678 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1628 |
| 25 | Macau International Airport |  | MO | 1607 |
| 26 | Ninoy Aquino International Airport |  | PH | 1560 |
| 27 | Kuala Lumpur International Airport |  | MY | 1519 |
| 28 | Charlotte/Douglas International Airport |  | US | 1515 |
| 29 | Barcelona International Airport |  | ES | 1481 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1420 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Bengaluru International Airport |  | IN | 1379 |
| 34 | Seattle-Tacoma International Airport |  | US | 1378 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1377 |
| 36 | Don Mueang International Airport |  | TH | 1360 |
| 37 | Calgary International Airport |  | CA | 1345 |
| 38 | Oslo Gardermoen Airport |  | NO | 1312 |
| 39 | Vancouver International Airport |  | CA | 1282 |
| 40 | O. R. Tambo International Airport |  | ZA | 1273 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 862 | 21m | 244 km | 3,629.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 594 | 1h 6m | 770 km | 7,890.8 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 386 | 27m | 275 km | 1,829.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 363 | 1h 50m | 1,423 km | 8,908.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 361 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 340 | 44m | 241 km | 1,412.3 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 339 | 44m | 555 km | 3,246.1 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 328 | 21m | 250 km | 1,416.8 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 313 | 24m | 218 km | 1,179.2 t |
| 15 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 308 | 1h 39m | 1,156 km | 6,144.5 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 290 | 19m | 99 km | 496.7 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 287 | 27m | 215 km | 1,062.9 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 259 | 15m | 154 km | 686.2 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HLR777 | HLR | Varna Airport (LBWN) | Sofia Airport (LBSF) | 2026-08-25 09:00 UTC | 2026-08-25 09:34 UTC | 33m |
| HSOVJ3 | HSO | De Kooy Airport (EHKD) | Rotterdam Airport (EHRD) | 2026-08-25 09:05 UTC | 2026-08-25 09:32 UTC | 27m |
| MABSU | MAB | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-25 08:56 UTC | 2026-08-25 09:31 UTC | 34m |
| GEDVL | GED | Southend Airport (EGMC) | Southend Airport (EGMC) | 2026-08-25 09:18 UTC | 2026-08-25 09:30 UTC | 11m |
| TUTOR50 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-25 09:06 UTC | 2026-08-25 09:28 UTC | 22m |
| FWYHG | FWY | Aix-en-Provence (BA 114) Airport (LFMA) | Aix-en-Provence (BA 114) Airport (LFMA) | 2026-08-25 08:51 UTC | 2026-08-25 09:27 UTC | 36m |
| FHUAM | FHU | Macon-Charnay Airport (LFLM) | Macon-Charnay Airport (LFLM) | 2026-08-25 09:02 UTC | 2026-08-25 09:17 UTC | 14m |
| HGB341 | HGB | Kansai International Airport (RJBB) | Chek Lap Kok International Airport (VHHH) | 2026-08-25 05:45 UTC | 2026-08-25 09:05 UTC | 3h 20m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-25 08:46 UTC | 2026-08-25 09:04 UTC | 17m |
| JFA10B | JFA | Courchevel Airport (LFLJ) | Meribel Airport (LFKX) | 2026-08-25 08:52 UTC | 2026-08-25 08:59 UTC | 6m |
| GCICC | GCI | Denham Aerodrome (EGLD) | Denham Aerodrome (EGLD) | 2026-08-25 08:46 UTC | 2026-08-25 08:56 UTC | 10m |
| SYERTN4 | SYE | RAF Syerston (EGXY) | RAF Syerston (EGXY) | 2026-08-25 08:50 UTC | 2026-08-25 08:54 UTC | 3m |
| HUF278 | HUF | Kecskemet Airport (LHKE) | Fetesti Air Base (LR80) | 2026-08-25 07:58 UTC | 2026-08-25 08:53 UTC | 54m |
| WWI43 | WWI | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Bob Hope Airport (KBUR) | 2026-08-25 04:05 UTC | 2026-08-25 08:52 UTC | 4h 47m |
| ANE2305 | ANE | Vigo Airport (LEVX) | Santander Airport (LEXJ) | 2026-08-25 08:19 UTC | 2026-08-25 08:52 UTC | 33m |
| R20653 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-08-25 08:39 UTC | 2026-08-25 08:52 UTC | 12m |
| THA044 | Thai Airways | Suvarnabhumi Airport (VTBS) | Khon Kaen Airport (VTUK) | 2026-08-25 08:17 UTC | 2026-08-25 08:51 UTC | 33m |
| EAI91LB | EAI | Leeds Bradford Airport (EGNM) | Dublin Airport (EIDW) | 2026-08-25 07:47 UTC | 2026-08-25 08:51 UTC | 1h 4m |
| AWH91C | AWH | Dusseldorf International Airport (EDDL) | Leipzig Halle Airport (EDDP) | 2026-08-25 08:06 UTC | 2026-08-25 08:46 UTC | 40m |
| LXC60 | LXC | Lapalisse - Perigny Airport (LFHX) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-08-25 07:21 UTC | 2026-08-25 08:46 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
