# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_22:23:38_UTC-green)

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

**Latest saved flight:** 2026-09-01 22:23:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-01 22:23:38 UTC

- **244,189** saved flights
- **73,925** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **244,189** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,942,346.3 tonnes** estimated CO2 emissions
- **170,570,802 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9801 |
| 2 | SkyWest Airlines | 8558 |
| 3 | EJA | 4719 |
| 4 | IndiGo | 4095 |
| 5 | American Airlines | 3927 |
| 6 | Southwest Airlines | 3664 |
| 7 | Delta Air Lines | 3109 |
| 8 | ENY | 2935 |
| 9 | LATAM Airlines | 2341 |
| 10 | AZU | 2268 |
| 11 | Vueling | 2092 |
| 12 | Lufthansa | 1956 |
| 13 | WIF | 1946 |
| 14 | LXJ | 1886 |
| 15 | easyJet | 1698 |
| 16 | Swiss International | 1646 |
| 17 | AXM | 1609 |
| 18 | EJU | 1570 |
| 19 | QLK | 1559 |
| 20 | United Airlines | 1537 |
| 21 | Alaska Airlines | 1460 |
| 22 | All Nippon Airways | 1439 |
| 23 | WMT | 1371 |
| 24 | GLO | 1366 |
| 25 | VIV | 1336 |
| 26 | PGT | 1334 |
| 27 | Air France | 1333 |
| 28 | Wizz Air | 1326 |
| 29 | AEE | 1207 |
| 30 | JetBlue | 1205 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 202343 |
| 2 | 🇪🇸 ES | 15686 |
| 3 | 🇧🇷 BR | 14229 |
| 4 | 🇦🇺 AU | 13844 |
| 5 | 🇨🇦 CA | 13588 |
| 6 | 🇮🇹 IT | 13375 |
| 7 | 🇮🇳 IN | 12760 |
| 8 | 🇩🇪 DE | 12045 |
| 9 | 🇬🇧 GB | 11525 |
| 10 | 🇨🇴 CO | 10575 |
| 11 | 🇫🇷 FR | 9851 |
| 12 | 🇯🇵 JP | 9736 |
| 13 | 🇹🇷 TR | 7266 |
| 14 | 🇬🇷 GR | 7208 |
| 15 | 🇲🇽 MX | 6730 |
| 16 | 🇨🇭 CH | 6566 |
| 17 | 🇳🇴 NO | 6051 |
| 18 | 🇹🇭 TH | 4409 |
| 19 | 🇲🇾 MY | 4317 |
| 20 | 🇿🇦 ZA | 4247 |
| 21 | 🇵🇱 PL | 4104 |
| 22 | 🇳🇿 NZ | 3347 |
| 23 | 🇵🇭 PH | 3342 |
| 24 | 🇬🇹 GT | 3068 |
| 25 | 🇰🇷 KR | 2866 |
| 26 | 🇭🇷 HR | 2814 |
| 27 | 🇲🇦 MA | 2470 |
| 28 | 🇲🇪 ME | 2282 |
| 29 | 🇳🇱 NL | 2212 |
| 30 | 🇮🇩 ID | 2126 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5033 |
| 2 | Denver International Airport |  | US | 3931 |
| 3 | Indira Gandhi International Airport |  | IN | 2977 |
| 4 | Tokyo International Airport |  | JP | 2901 |
| 5 | Guaymaral Airport |  | CO | 2712 |
| 6 | Harry Reid International Airport |  | US | 2599 |
| 7 | Zurich Airport |  | CH | 2566 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2489 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2435 |
| 10 | El Dorado International Airport |  | CO | 2402 |
| 11 | La Aurora Airport |  | GT | 2333 |
| 12 | Salt Lake City International Airport |  | US | 2161 |
| 13 | Chicago O'Hare International Airport |  | US | 2160 |
| 14 | Congonhas Airport |  | BR | 2085 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2023 |
| 16 | Frankfurt am Main International Airport |  | DE | 1927 |
| 17 | Capua Airport |  | IT | 1922 |
| 18 | Madrid Barajas International Airport |  | ES | 1920 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1834 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1797 |
| 21 | Malpensa International Airport |  | IT | 1747 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1721 |
| 23 | Charles de Gaulle International Airport |  | FR | 1715 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1708 |
| 25 | Macau International Airport |  | MO | 1628 |
| 26 | Ninoy Aquino International Airport |  | PH | 1626 |
| 27 | Enrique Olaya Herrera Airport |  | CO | 1572 |
| 28 | Charlotte/Douglas International Airport |  | US | 1558 |
| 29 | Kuala Lumpur International Airport |  | MY | 1555 |
| 30 | Barcelona International Airport |  | ES | 1547 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1476 |
| 32 | Viracopos International Airport |  | BR | 1448 |
| 33 | Seattle-Tacoma International Airport |  | US | 1431 |
| 34 | Don Mueang International Airport |  | TH | 1420 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1414 |
| 36 | Bengaluru International Airport |  | IN | 1412 |
| 37 | Calgary International Airport |  | CA | 1404 |
| 38 | Oslo Gardermoen Airport |  | NO | 1377 |
| 39 | Vancouver International Airport |  | CA | 1359 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1337 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1099 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 901 | 21m | 244 km | 3,793.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 633 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 621 | 24m | 225 km | 2,409.2 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 615 | 1h 6m | 770 km | 8,169.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 548 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 403 | 27m | 275 km | 1,909.6 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 385 | 1h 50m | 1,423 km | 9,448.5 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 373 | 44m | 555 km | 3,571.7 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 367 | 35m | - | - |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 360 | 44m | 241 km | 1,495.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 347 | 21m | 250 km | 1,498.8 t |
| 13 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 335 | 24m | 218 km | 1,262.1 t |
| 14 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 326 | 1h 39m | 1,156 km | 6,503.6 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 325 | 22m | 55 km | 308.9 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 322 | 1h 6m | 706 km | 3,920.4 t |
| 17 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 303 | 19m | 99 km | 519.0 t |
| 19 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 297 | 26m | 215 km | 1,100.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 289 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 283 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 281 | 1h 14m | 961 km | 4,657.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 276 | 19m | 144 km | 686.5 t |
| 25 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 268 | 29m | 304 km | 1,404.9 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 268 | 15m | 154 km | 710.1 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 262 | 1h 50m | 1,304 km | 5,894.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 251 | 28m | 152 km | 656.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-09-01 12:12 UTC | 2026-09-01 22:23 UTC | 10h 11m |
| CPA300 | Cathay Pacific | Munich International Airport (EDDM) | Zhuhai Airport (ZGSD) | 2026-09-01 12:18 UTC | 2026-09-01 22:18 UTC | 9h 59m |
| N9669C |  | Akron/Jesson Field (K9G3) | Akron/Jesson Field (K9G3) | 2026-09-01 21:47 UTC | 2026-09-01 22:17 UTC | 29m |
| YGF | YGF | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-01 21:38 UTC | 2026-09-01 22:15 UTC | 37m |
| THY91J | Turkish Airlines | Detroit Metro Wayne County Airport (KDTW) | Zhuhai Airport (ZGSD) | 2026-09-01 01:02 UTC | 2026-09-01 22:13 UTC | 21h 11m |
| REH46 | REH | Ellison Onizuka Kona International At Keahole Airport (PHKO) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-09-01 22:11 UTC | 2026-09-01 22:11 UTC | 0m |
| N8327W |  | Warrenton/Fauquier Airport (KHWY) | Shannon Airport (KEZF) | 2026-09-01 21:15 UTC | 2026-09-01 22:10 UTC | 55m |
| BT617 |  | San Clemente Island Nalf Airport (KNUC) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-09-01 21:32 UTC | 2026-09-01 22:08 UTC | 36m |
| BOX728 | BOX | Leipzig Halle Airport (EDDP) | Zhuhai Airport (ZGSD) | 2026-09-01 06:50 UTC | 2026-09-01 22:05 UTC | 15h 15m |
| QLK571D | QLK | Adelaide International Airport (YPAD) | Whyalla Airport (YWHA) | 2026-09-01 21:26 UTC | 2026-09-01 22:05 UTC | 38m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-01 17:39 UTC | 2026-09-01 22:03 UTC | 4h 24m |
| N59HH |  | Bend Municipal Airport (KBDN) | OG12 (OG12) | 2026-09-01 21:06 UTC | 2026-09-01 22:01 UTC | 55m |
| CPA294 | Cathay Pacific | Melsbroek Air Base (EBMB) | Zhuhai Airport (ZGSD) | 2026-09-01 11:23 UTC | 2026-09-01 22:00 UTC | 10h 36m |
| CPA2046 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-09-01 17:22 UTC | 2026-09-01 21:56 UTC | 4h 33m |
| GRYHK11 | GRY | Hoffman Airport (0CA5) | Lake Havasu City Airport (KHII) | 2026-09-01 21:31 UTC | 2026-09-01 21:54 UTC | 22m |
| FIRE5 | FIR | Van Nuys Airport (KVNY) | Bob Hope Airport (KBUR) | 2026-09-01 20:57 UTC | 2026-09-01 21:53 UTC | 56m |
| CPA811 | Cathay Pacific | General Edward Lawrence Logan International Airport (KBOS) | Zhuhai Airport (ZGSD) | 2026-09-01 06:57 UTC | 2026-09-01 21:52 UTC | 14h 55m |
| XE1182 |  | Harry Reid International Airport (KLAS) | Santa Monica Municipal Airport (KSMO) | 2026-09-01 20:46 UTC | 2026-09-01 21:50 UTC | 1h 3m |
| N288HL |  | Center Municipal Airport (KF17) | Molair Airport (TX35) | 2026-09-01 21:34 UTC | 2026-09-01 21:50 UTC | 15m |
| N677F |  | Rocky Mountain Metro Airport (KBJC) | Sulphur Creek Ranch Airport (ID74) | 2026-09-01 19:15 UTC | 2026-09-01 21:49 UTC | 2h 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
