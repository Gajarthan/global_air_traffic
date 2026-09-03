# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_13:39:37_UTC-green)

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

**Latest saved flight:** 2026-09-03 13:39:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-03 13:39:37 UTC

- **245,784** saved flights
- **74,221** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **245,784** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,959,044.7 tonnes** estimated CO2 emissions
- **171,538,824 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9859 |
| 2 | SkyWest Airlines | 8596 |
| 3 | EJA | 4737 |
| 4 | IndiGo | 4121 |
| 5 | American Airlines | 3943 |
| 6 | Southwest Airlines | 3678 |
| 7 | Delta Air Lines | 3123 |
| 8 | ENY | 2944 |
| 9 | LATAM Airlines | 2368 |
| 10 | AZU | 2283 |
| 11 | Vueling | 2106 |
| 12 | Lufthansa | 1967 |
| 13 | WIF | 1966 |
| 14 | LXJ | 1900 |
| 15 | easyJet | 1708 |
| 16 | Swiss International | 1657 |
| 17 | AXM | 1616 |
| 18 | EJU | 1581 |
| 19 | QLK | 1577 |
| 20 | United Airlines | 1546 |
| 21 | Alaska Airlines | 1468 |
| 22 | All Nippon Airways | 1448 |
| 23 | WMT | 1384 |
| 24 | GLO | 1371 |
| 25 | PGT | 1348 |
| 26 | VIV | 1346 |
| 27 | Air France | 1344 |
| 28 | Wizz Air | 1333 |
| 29 | AEE | 1212 |
| 30 | JetBlue | 1212 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 203556 |
| 2 | 🇪🇸 ES | 15780 |
| 3 | 🇧🇷 BR | 14338 |
| 4 | 🇦🇺 AU | 13989 |
| 5 | 🇨🇦 CA | 13673 |
| 6 | 🇮🇹 IT | 13471 |
| 7 | 🇮🇳 IN | 12841 |
| 8 | 🇩🇪 DE | 12124 |
| 9 | 🇬🇧 GB | 11588 |
| 10 | 🇨🇴 CO | 10669 |
| 11 | 🇫🇷 FR | 9924 |
| 12 | 🇯🇵 JP | 9773 |
| 13 | 🇹🇷 TR | 7303 |
| 14 | 🇬🇷 GR | 7252 |
| 15 | 🇲🇽 MX | 6775 |
| 16 | 🇨🇭 CH | 6620 |
| 17 | 🇳🇴 NO | 6101 |
| 18 | 🇹🇭 TH | 4446 |
| 19 | 🇲🇾 MY | 4329 |
| 20 | 🇿🇦 ZA | 4272 |
| 21 | 🇵🇱 PL | 4128 |
| 22 | 🇳🇿 NZ | 3370 |
| 23 | 🇵🇭 PH | 3364 |
| 24 | 🇬🇹 GT | 3077 |
| 25 | 🇰🇷 KR | 2878 |
| 26 | 🇭🇷 HR | 2832 |
| 27 | 🇲🇦 MA | 2482 |
| 28 | 🇲🇪 ME | 2300 |
| 29 | 🇳🇱 NL | 2227 |
| 30 | 🇮🇩 ID | 2142 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5058 |
| 2 | Denver International Airport |  | US | 3965 |
| 3 | Indira Gandhi International Airport |  | IN | 2996 |
| 4 | Tokyo International Airport |  | JP | 2914 |
| 5 | Guaymaral Airport |  | CO | 2719 |
| 6 | Harry Reid International Airport |  | US | 2616 |
| 7 | Zurich Airport |  | CH | 2584 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2499 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2450 |
| 10 | El Dorado International Airport |  | CO | 2433 |
| 11 | La Aurora Airport |  | GT | 2341 |
| 12 | Salt Lake City International Airport |  | US | 2178 |
| 13 | Chicago O'Hare International Airport |  | US | 2163 |
| 14 | Congonhas Airport |  | BR | 2102 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2028 |
| 16 | Frankfurt am Main International Airport |  | DE | 1937 |
| 17 | Capua Airport |  | IT | 1934 |
| 18 | Madrid Barajas International Airport |  | ES | 1929 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1851 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1804 |
| 21 | Malpensa International Airport |  | IT | 1761 |
| 22 | Charles de Gaulle International Airport |  | FR | 1730 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1725 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1725 |
| 25 | Ninoy Aquino International Airport |  | PH | 1637 |
| 26 | Macau International Airport |  | MO | 1632 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1589 |
| 28 | Charlotte/Douglas International Airport |  | US | 1565 |
| 29 | Barcelona International Airport |  | ES | 1560 |
| 30 | Kuala Lumpur International Airport |  | MY | 1560 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1492 |
| 32 | Viracopos International Airport |  | BR | 1458 |
| 33 | Seattle-Tacoma International Airport |  | US | 1444 |
| 34 | Don Mueang International Airport |  | TH | 1428 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1427 |
| 36 | Bengaluru International Airport |  | IN | 1423 |
| 37 | Calgary International Airport |  | CA | 1415 |
| 38 | Oslo Gardermoen Airport |  | NO | 1385 |
| 39 | Vancouver International Airport |  | CA | 1369 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1343 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1100 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 910 | 21m | 244 km | 3,831.8 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 638 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 625 | 24m | 225 km | 2,424.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 618 | 1h 6m | 770 km | 8,209.7 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 551 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 405 | 27m | 275 km | 1,919.1 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 390 | 1h 50m | 1,423 km | 9,571.2 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 379 | 44m | 555 km | 3,629.1 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 361 | 44m | 241 km | 1,499.5 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 350 | 21m | 250 km | 1,511.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 341 | 24m | 218 km | 1,284.7 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 329 | 1h 39m | 1,156 km | 6,563.4 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 328 | 22m | 55 km | 311.8 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 304 | 19m | 99 km | 520.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 302 | 27m | 215 km | 1,118.5 t |
| 20 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 290 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 284 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 283 | 1h 14m | 961 km | 4,690.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 279 | 19m | 144 km | 694.0 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 265 | 1h 50m | 1,304 km | 5,961.8 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 252 | 28m | 152 km | 658.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N561R |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-09-03 13:12 UTC | 2026-09-03 13:39 UTC | 26m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-09-03 13:02 UTC | 2026-09-03 13:35 UTC | 33m |
| S5DTG |  | LJSK (LJSK) | Maribor Airport (LJMB) | 2026-09-03 13:23 UTC | 2026-09-03 13:34 UTC | 10m |
| N241MP |  | Blue Grass Airport (KLEX) | Paintsville-Prestonsburg-Combs Field (9KY9) | 2026-09-03 12:11 UTC | 2026-09-03 13:32 UTC | 1h 21m |
| SPSDW | SPS | Kielce-Masłów Airport (EPKA) | Kielce-Masłów Airport (EPKA) | 2026-09-03 12:38 UTC | 2026-09-03 13:29 UTC | 50m |
| PPSGL | PPS | Helibras Airport (SIYS) | Helibras Airport (SIYS) | 2026-09-03 13:04 UTC | 2026-09-03 13:29 UTC | 24m |
| N4313D |  | 16PA (16PA) | Richard Downing Airport (KI40) | 2026-09-03 10:58 UTC | 2026-09-03 13:27 UTC | 2h 29m |
| N68BF |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-09-03 12:25 UTC | 2026-09-03 13:23 UTC | 57m |
| PPJRX | PPJ | Ministro Victor Konder International Airport (SBNF) | Ministro Victor Konder International Airport (SBNF) | 2026-09-03 13:05 UTC | 2026-09-03 13:21 UTC | 15m |
| CLOPS89 | CLO | Athanasiou Valley Airport (CO07) | Athanasiou Valley Airport (CO07) | 2026-09-03 12:51 UTC | 2026-09-03 13:19 UTC | 27m |
| TKJ5DP | TKJ | Batumi International Airport (UGSB) | Sabiha Gokcen International Airport (LTFJ) | 2026-09-03 11:58 UTC | 2026-09-03 13:18 UTC | 1h 19m |
| HALCON5 | Hawaiian Airlines | El Bosque Airport (SCBQ) | Estero Seco Airport (SCZE) | 2026-09-03 13:04 UTC | 2026-09-03 13:14 UTC | 10m |
| IGO41HP | IndiGo | Bengaluru International Airport (VOBL) | Vellore Airport (VOVR) | 2026-09-03 12:54 UTC | 2026-09-03 13:13 UTC | 19m |
| UAE9655 | Emirates | Al Maktoum International Airport (OMDW) | Heidelburg Airport (FAHG) | 2026-09-03 06:03 UTC | 2026-09-03 13:13 UTC | 7h 10m |
| ROKT11 | ROK | Pensacola Nas (Forrest Sherman Field) Airport (KNPA) | Bird Nest Airport (4MS5) | 2026-09-03 12:56 UTC | 2026-09-03 13:13 UTC | 17m |
| N422B |  | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-09-03 12:34 UTC | 2026-09-03 13:13 UTC | 38m |
| NKT100 | NKT | Oakland/Troy Airport (KVLL) | K8M8 (K8M8) | 2026-09-03 12:18 UTC | 2026-09-03 13:06 UTC | 48m |
| LOCO77 | LOC | Liberty Field (7AL5) | Liberty Field (7AL5) | 2026-09-03 12:47 UTC | 2026-09-03 13:05 UTC | 18m |
| N53SY |  | St George Regional Airport (KSGU) | Grassy Meadows/Sky Ranch Landowners Assn Airport (UT47) | 2026-09-03 12:59 UTC | 2026-09-03 13:05 UTC | 5m |
| N390CJ |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | CD97 (CD97) | 2026-09-03 11:28 UTC | 2026-09-03 13:00 UTC | 1h 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
