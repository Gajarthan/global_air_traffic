# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_09:34:34_UTC-green)

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

**Latest saved flight:** 2026-08-24 09:34:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 09:34:34 UTC

- **231,328** saved flights
- **71,247** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **231,328** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,789,235.9 tonnes** estimated CO2 emissions
- **161,694,836 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9287 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3915 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3574 |
| 7 | Delta Air Lines | 2958 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2224 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1972 |
| 12 | Lufthansa | 1880 |
| 13 | LXJ | 1824 |
| 14 | WIF | 1824 |
| 15 | easyJet | 1617 |
| 16 | Swiss International | 1544 |
| 17 | AXM | 1543 |
| 18 | EJU | 1476 |
| 19 | QLK | 1474 |
| 20 | United Airlines | 1471 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1384 |
| 23 | GLO | 1291 |
| 24 | WMT | 1275 |
| 25 | VIV | 1272 |
| 26 | PGT | 1264 |
| 27 | Air France | 1255 |
| 28 | Wizz Air | 1214 |
| 29 | AEE | 1153 |
| 30 | JetBlue | 1152 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192837 |
| 2 | 🇪🇸 ES | 14833 |
| 3 | 🇧🇷 BR | 13517 |
| 4 | 🇦🇺 AU | 13144 |
| 5 | 🇨🇦 CA | 12761 |
| 6 | 🇮🇹 IT | 12551 |
| 7 | 🇮🇳 IN | 12185 |
| 8 | 🇩🇪 DE | 11365 |
| 9 | 🇬🇧 GB | 10873 |
| 10 | 🇨🇴 CO | 9612 |
| 11 | 🇯🇵 JP | 9425 |
| 12 | 🇫🇷 FR | 9240 |
| 13 | 🇹🇷 TR | 6824 |
| 14 | 🇬🇷 GR | 6813 |
| 15 | 🇲🇽 MX | 6431 |
| 16 | 🇨🇭 CH | 6138 |
| 17 | 🇳🇴 NO | 5690 |
| 18 | 🇲🇾 MY | 4116 |
| 19 | 🇹🇭 TH | 4062 |
| 20 | 🇿🇦 ZA | 4025 |
| 21 | 🇵🇱 PL | 3836 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3179 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2722 |
| 26 | 🇭🇷 HR | 2651 |
| 27 | 🇲🇦 MA | 2343 |
| 28 | 🇲🇪 ME | 2123 |
| 29 | 🇳🇱 NL | 2064 |
| 30 | 🇮🇩 ID | 2007 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2817 |
| 4 | Tokyo International Airport |  | JP | 2812 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2491 |
| 7 | Zurich Airport |  | CH | 2412 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2330 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2148 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2039 |
| 14 | Congonhas Airport |  | BR | 1970 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1847 |
| 17 | Madrid Barajas International Airport |  | ES | 1814 |
| 18 | Capua Airport |  | IT | 1814 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1738 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1719 |
| 21 | Malpensa International Airport |  | IT | 1659 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1656 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Macau International Airport |  | MO | 1602 |
| 25 | Charles de Gaulle International Airport |  | FR | 1601 |
| 26 | Ninoy Aquino International Airport |  | PH | 1529 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1489 |
| 29 | Barcelona International Airport |  | ES | 1453 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1400 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Bengaluru International Airport |  | IN | 1368 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1328 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1291 |
| 39 | Vancouver International Airport |  | CA | 1255 |
| 40 | Vitoria/Foronda Airport |  | ES | 1253 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 845 | 21m | 244 km | 3,558.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 584 | 1h 6m | 770 km | 7,758.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 381 | 27m | 275 km | 1,805.4 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 356 | 1h 50m | 1,423 km | 8,736.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 335 | 44m | 241 km | 1,391.5 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 325 | 21m | 250 km | 1,403.8 t |
| 12 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 320 | 44m | 555 km | 3,064.2 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 305 | 24m | 218 km | 1,149.1 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 300 | 1h 38m | 1,156 km | 5,984.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 281 | 27m | 215 km | 1,040.7 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 267 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 263 | 19m | 144 km | 654.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 247 | 15m | 154 km | 654.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| UFX64 | UFX | Humberside Airport (EGNJ) | Blackpool International Airport (EGNH) | 2026-08-24 08:49 UTC | 2026-08-24 09:34 UTC | 44m |
| FGTYC | FGT | Avignon-Caumont Airport (LFMV) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-08-24 08:38 UTC | 2026-08-24 09:32 UTC | 54m |
| SWR2TM | Swiss International | Malpensa International Airport (LIMC) | Zurich Airport (LSZH) | 2026-08-24 08:51 UTC | 2026-08-24 09:31 UTC | 39m |
| UAL228 | United Airlines | Washington Dulles International Airport (KIAD) | Dublin Airport (EIDW) | 2026-08-24 02:35 UTC | 2026-08-24 09:31 UTC | 6h 55m |
| R72097 |  | Hohenfels Army Air Field (ETIH) | Hohenfels Army Air Field (ETIH) | 2026-08-24 09:09 UTC | 2026-08-24 09:30 UTC | 21m |
| BTN701 | BTN | Suvarnabhumi Airport (VTBS) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-08-24 07:00 UTC | 2026-08-24 09:09 UTC | 2h 8m |
| QSUAV | QSU | Stade Airport (EDHS) | Stade Airport (EDHS) | 2026-08-24 08:36 UTC | 2026-08-24 09:08 UTC | 32m |
| SIA959 | Singapore Airlines | Soekarno-Hatta International Airport (WIII) | Hang Nadim Airport (WIDD) | 2026-08-24 07:54 UTC | 2026-08-24 09:05 UTC | 1h 11m |
| THA322 | Thai Airways | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-24 07:56 UTC | 2026-08-24 09:02 UTC | 1h 5m |
| SUMCC | SUM | El Alamein International Airport (HEAL) | El Alamein International Airport (HEAL) | 2026-08-24 08:58 UTC | 2026-08-24 09:00 UTC | 1m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-24 08:42 UTC | 2026-08-24 08:58 UTC | 15m |
| AGUS149 | AGU | Vergiate Airport (LILG) | Vergiate Airport (LILG) | 2026-08-24 08:48 UTC | 2026-08-24 08:57 UTC | 8m |
| EZY73EH | easyJet | Belfast International Airport (EGAA) | Bristol International Airport (EGGD) | 2026-08-24 08:02 UTC | 2026-08-24 08:52 UTC | 49m |
| 8AX |  | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-24 08:41 UTC | 2026-08-24 08:52 UTC | 10m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-08-24 08:29 UTC | 2026-08-24 08:50 UTC | 20m |
| GBSVG | GBS | Hawarden Airport (EGNR) | Hawarden Airport (EGNR) | 2026-08-24 08:39 UTC | 2026-08-24 08:47 UTC | 8m |
| MCUZU | MCU | Paris-Le Bourget Airport (LFPB) | Southampton Airport (EGHI) | 2026-08-24 08:05 UTC | 2026-08-24 08:47 UTC | 42m |
| RYR4GC | Ryanair | Dublin Airport (EIDW) | Farnborough Airport (EGLF) | 2026-08-24 07:32 UTC | 2026-08-24 08:46 UTC | 1h 13m |
| VLG457W | Vueling | Jerez Airport (LEJR) | Palma De Mallorca Airport (LEPA) | 2026-08-24 07:33 UTC | 2026-08-24 08:46 UTC | 1h 12m |
| NOZ30BF | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Kiruna Airport (ESNQ) | 2026-08-24 07:17 UTC | 2026-08-24 08:42 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
