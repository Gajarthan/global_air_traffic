# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_06:43:12_UTC-green)

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

**Latest saved flight:** 2026-08-24 06:43:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 06:43:12 UTC

- **231,027** saved flights
- **71,201** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **231,027** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,785,575.6 tonnes** estimated CO2 emissions
- **161,482,641 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9264 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3905 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3574 |
| 7 | Delta Air Lines | 2957 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2224 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1963 |
| 12 | Lufthansa | 1877 |
| 13 | LXJ | 1824 |
| 14 | WIF | 1815 |
| 15 | easyJet | 1608 |
| 16 | Swiss International | 1540 |
| 17 | AXM | 1536 |
| 18 | EJU | 1471 |
| 19 | United Airlines | 1470 |
| 20 | QLK | 1466 |
| 21 | Alaska Airlines | 1396 |
| 22 | All Nippon Airways | 1379 |
| 23 | GLO | 1290 |
| 24 | VIV | 1271 |
| 25 | WMT | 1267 |
| 26 | PGT | 1262 |
| 27 | Air France | 1253 |
| 28 | Wizz Air | 1213 |
| 29 | AEE | 1151 |
| 30 | JetBlue | 1151 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192827 |
| 2 | 🇪🇸 ES | 14796 |
| 3 | 🇧🇷 BR | 13515 |
| 4 | 🇦🇺 AU | 13105 |
| 5 | 🇨🇦 CA | 12759 |
| 6 | 🇮🇹 IT | 12497 |
| 7 | 🇮🇳 IN | 12150 |
| 8 | 🇩🇪 DE | 11343 |
| 9 | 🇬🇧 GB | 10849 |
| 10 | 🇨🇴 CO | 9611 |
| 11 | 🇯🇵 JP | 9393 |
| 12 | 🇫🇷 FR | 9223 |
| 13 | 🇹🇷 TR | 6813 |
| 14 | 🇬🇷 GR | 6790 |
| 15 | 🇲🇽 MX | 6430 |
| 16 | 🇨🇭 CH | 6118 |
| 17 | 🇳🇴 NO | 5666 |
| 18 | 🇲🇾 MY | 4099 |
| 19 | 🇹🇭 TH | 4042 |
| 20 | 🇿🇦 ZA | 4019 |
| 21 | 🇵🇱 PL | 3831 |
| 22 | 🇳🇿 NZ | 3206 |
| 23 | 🇵🇭 PH | 3171 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2720 |
| 26 | 🇭🇷 HR | 2640 |
| 27 | 🇲🇦 MA | 2339 |
| 28 | 🇲🇪 ME | 2114 |
| 29 | 🇳🇱 NL | 2059 |
| 30 | 🇮🇩 ID | 2005 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2814 |
| 4 | Tokyo International Airport |  | JP | 2803 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2491 |
| 7 | Zurich Airport |  | CH | 2405 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2326 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2148 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2038 |
| 14 | Congonhas Airport |  | BR | 1970 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1844 |
| 17 | Madrid Barajas International Airport |  | ES | 1808 |
| 18 | Capua Airport |  | IT | 1808 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1738 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1719 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1655 |
| 22 | Malpensa International Airport |  | IT | 1652 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1629 |
| 24 | Macau International Airport |  | MO | 1602 |
| 25 | Charles de Gaulle International Airport |  | FR | 1598 |
| 26 | Ninoy Aquino International Airport |  | PH | 1525 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1485 |
| 29 | Barcelona International Airport |  | ES | 1445 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1400 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Seattle-Tacoma International Airport |  | US | 1363 |
| 34 | Bengaluru International Airport |  | IN | 1363 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1323 |
| 37 | Calgary International Airport |  | CA | 1316 |
| 38 | Oslo Gardermoen Airport |  | NO | 1284 |
| 39 | Vancouver International Airport |  | CA | 1255 |
| 40 | Vitoria/Foronda Airport |  | ES | 1252 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 844 | 21m | 244 km | 3,553.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 582 | 1h 6m | 770 km | 7,731.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 577 | 24m | 225 km | 2,238.5 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 380 | 27m | 275 km | 1,800.7 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 356 | 1h 50m | 1,423 km | 8,736.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 334 | 44m | 241 km | 1,387.4 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 318 | 44m | 555 km | 3,045.0 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 301 | 24m | 218 km | 1,134.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 299 | 1h 38m | 1,156 km | 5,964.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 281 | 27m | 215 km | 1,040.7 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 24 | Bodø Airport (ENBO) | ENEN (ENEN) | 265 | 13m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 262 | 19m | 144 km | 651.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 244 | 15m | 154 km | 646.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UAL1083 | United Airlines | Vancouver International Airport (CYVR) | San Francisco International Airport (KSFO) | 2026-08-24 04:50 UTC | 2026-08-24 06:43 UTC | 1h 52m |
| CS055491 |  | Montréal (Mirabel) Airport (CYMX) | Montréal (Mirabel) Airport (CYMX) | 2026-08-24 06:14 UTC | 2026-08-24 06:35 UTC | 21m |
| TSC382 | TSC | Ottawa / Macdonald-Cartier International Airport (CYOW) | London Gatwick Airport (EGKK) | 2026-08-23 23:57 UTC | 2026-08-24 06:27 UTC | 6h 30m |
| LHK06 | LHK | Haifa International Airport (LLHA) | Haifa International Airport (LLHA) | 2026-08-24 06:05 UTC | 2026-08-24 06:27 UTC | 21m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-08-24 05:08 UTC | 2026-08-24 06:25 UTC | 1h 16m |
| HAKAR | HAK | Medulin Campanoz Airport (LDPM) | Zemunik Airport (LDZD) | 2026-08-24 06:11 UTC | 2026-08-24 06:22 UTC | 10m |
| DLH4AN | Lufthansa | Munich International Airport (EDDM) | Bremen Airport (EDDW) | 2026-08-24 05:25 UTC | 2026-08-24 06:21 UTC | 55m |
| WF3BR |  | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-24 05:47 UTC | 2026-08-24 06:16 UTC | 28m |
| 5YMJC |  | Nairobi Wilson Airport (HKNW) | Nyeri Airport (HKNI) | 2026-08-24 06:00 UTC | 2026-08-24 06:15 UTC | 14m |
| WMT8LX | WMT | Catania / Fontanarossa Airport (LICC) | Malpensa International Airport (LIMC) | 2026-08-24 04:22 UTC | 2026-08-24 06:14 UTC | 1h 52m |
| OKCUN20 | OKC | Brno-Turany Airport (LKTB) | Brno-Turany Airport (LKTB) | 2026-08-24 06:07 UTC | 2026-08-24 06:08 UTC | 0m |
| QLK207D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-08-24 05:12 UTC | 2026-08-24 06:07 UTC | 55m |
| RYR8VD | Ryanair | Catania / Fontanarossa Airport (LICC) | Malpensa International Airport (LIMC) | 2026-08-24 04:14 UTC | 2026-08-24 06:06 UTC | 1h 51m |
| IGO7671 | IndiGo | Safdarjung Airport (VIDD) | Adampur Air Force Station (VIAX) | 2026-08-24 04:55 UTC | 2026-08-24 06:04 UTC | 1h 8m |
| WIF4DB | WIF | Bergen Airport Flesland (ENBR) | Sandane Airport Anda (ENSD) | 2026-08-24 05:42 UTC | 2026-08-24 06:02 UTC | 20m |
| VLG3FP | Vueling | Ibiza Airport (LEIB) | Bilbao Airport (LEBB) | 2026-08-24 05:08 UTC | 2026-08-24 06:02 UTC | 54m |
| T03 |  | Kuopio Airport (EFKU) | Jyvaskyla Airport (EFJY) | 2026-08-24 05:45 UTC | 2026-08-24 06:01 UTC | 15m |
| SWR99F | Swiss International | Oslo Gardermoen Airport (ENGM) | Zurich Airport (LSZH) | 2026-08-24 04:01 UTC | 2026-08-24 06:01 UTC | 1h 59m |
| ZUNOW | ZUN | Grand Central Airport (FAGC) | Grand Central Airport (FAGC) | 2026-08-24 05:39 UTC | 2026-08-24 06:01 UTC | 22m |
| HFA801 | HFA | Haifa International Airport (LLHA) | Larnaca International Airport (LCLK) | 2026-08-24 05:17 UTC | 2026-08-24 06:00 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
