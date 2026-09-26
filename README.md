# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_12:01:18_UTC-green)

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

**Latest saved flight:** 2026-09-26 12:01:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-26 12:01:18 UTC

- **269,916** saved flights
- **79,112** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **269,916** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,275,064.0 tonnes** estimated CO2 emissions
- **189,858,785 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10626 |
| 2 | SkyWest Airlines | 9389 |
| 3 | EJA | 5273 |
| 4 | IndiGo | 4520 |
| 5 | American Airlines | 4195 |
| 6 | Southwest Airlines | 3968 |
| 7 | Delta Air Lines | 3356 |
| 8 | ENY | 3169 |
| 9 | LATAM Airlines | 2600 |
| 10 | AZU | 2529 |
| 11 | Vueling | 2251 |
| 12 | WIF | 2197 |
| 13 | LXJ | 2118 |
| 14 | Lufthansa | 2051 |
| 15 | easyJet | 1809 |
| 16 | Swiss International | 1768 |
| 17 | QLK | 1738 |
| 18 | EJU | 1691 |
| 19 | AXM | 1674 |
| 20 | United Airlines | 1652 |
| 21 | Alaska Airlines | 1593 |
| 22 | All Nippon Airways | 1553 |
| 23 | PGT | 1520 |
| 24 | WMT | 1506 |
| 25 | GLO | 1502 |
| 26 | Air France | 1482 |
| 27 | VIV | 1471 |
| 28 | Wizz Air | 1467 |
| 29 | CXK | 1324 |
| 30 | AEE | 1295 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 224717 |
| 2 | 🇪🇸 ES | 16920 |
| 3 | 🇧🇷 BR | 15778 |
| 4 | 🇦🇺 AU | 15527 |
| 5 | 🇨🇦 CA | 15050 |
| 6 | 🇮🇹 IT | 14600 |
| 7 | 🇮🇳 IN | 14305 |
| 8 | 🇩🇪 DE | 12955 |
| 9 | 🇬🇧 GB | 12497 |
| 10 | 🇨🇴 CO | 12369 |
| 11 | 🇫🇷 FR | 10730 |
| 12 | 🇯🇵 JP | 10370 |
| 13 | 🇹🇷 TR | 8175 |
| 14 | 🇬🇷 GR | 7792 |
| 15 | 🇲🇽 MX | 7442 |
| 16 | 🇨🇭 CH | 7172 |
| 17 | 🇳🇴 NO | 6677 |
| 18 | 🇹🇭 TH | 4823 |
| 19 | 🇲🇾 MY | 4531 |
| 20 | 🇿🇦 ZA | 4514 |
| 21 | 🇵🇱 PL | 4425 |
| 22 | 🇳🇿 NZ | 3785 |
| 23 | 🇵🇭 PH | 3582 |
| 24 | 🇬🇹 GT | 3414 |
| 25 | 🇭🇷 HR | 3080 |
| 26 | 🇰🇷 KR | 3051 |
| 27 | 🇲🇦 MA | 2684 |
| 28 | 🇲🇪 ME | 2531 |
| 29 | 🇳🇱 NL | 2410 |
| 30 | 🇮🇩 ID | 2251 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5492 |
| 2 | Denver International Airport |  | US | 4390 |
| 3 | Indira Gandhi International Airport |  | IN | 3236 |
| 4 | Tokyo International Airport |  | JP | 3105 |
| 5 | El Dorado International Airport |  | CO | 2928 |
| 6 | Harry Reid International Airport |  | US | 2894 |
| 7 | Guaymaral Airport |  | CO | 2817 |
| 8 | Zurich Airport |  | CH | 2797 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2712 |
| 10 | La Aurora Airport |  | GT | 2595 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2595 |
| 12 | Salt Lake City International Airport |  | US | 2380 |
| 13 | Chicago O'Hare International Airport |  | US | 2306 |
| 14 | Congonhas Airport |  | BR | 2299 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2208 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2080 |
| 18 | Frankfurt am Main International Airport |  | DE | 2046 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2039 |
| 20 | Malpensa International Airport |  | IT | 1930 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1915 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1892 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1888 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1823 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1758 |
| 28 | Charlotte/Douglas International Airport |  | US | 1688 |
| 29 | Barcelona International Airport |  | ES | 1678 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1673 |
| 31 | Viracopos International Airport |  | BR | 1630 |
| 32 | Kuala Lumpur International Airport |  | MY | 1623 |
| 33 | Seattle-Tacoma International Airport |  | US | 1582 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1579 |
| 35 | Calgary International Airport |  | CA | 1538 |
| 36 | Don Mueang International Airport |  | TH | 1527 |
| 37 | Bengaluru International Airport |  | IN | 1522 |
| 38 | Oslo Gardermoen Airport |  | NO | 1513 |
| 39 | Vancouver International Airport |  | CA | 1510 |
| 40 | Antalya International Airport |  | TR | 1441 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1122 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1011 | 21m | 244 km | 4,257.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 744 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 682 | 1h 6m | 770 km | 9,059.8 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 676 | 24m | 225 km | 2,622.6 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 600 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 445 | 44m | 555 km | 4,261.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 433 | 27m | 275 km | 2,051.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 426 | 1h 50m | 1,423 km | 10,454.7 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 412 | 44m | 241 km | 1,711.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 385 | 24m | 218 km | 1,450.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 366 | 21m | 250 km | 1,580.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 362 | 23m | 55 km | 344.1 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 344 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 341 | 1h 6m | 706 km | 4,151.7 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 339 | 19m | 99 km | 580.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 296 | 42m | 535 km | 2,733.8 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 292 | 18m | 14 km | 73.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TOM4HD | TOM | Palma De Mallorca Airport (LEPA) | London Gatwick Airport (EGKK) | 2026-09-26 09:55 UTC | 2026-09-26 12:01 UTC | 2h 5m |
| N596LC |  | Elkhart Municipal Airport (KEKM) | Indianapolis Executive Airport (KTYQ) | 2026-09-26 11:38 UTC | 2026-09-26 12:00 UTC | 21m |
| QTR63G | Qatar Airways | Henri Coanda International Airport (LROP) | Hamad International Airport (OTHH) | 2026-09-26 07:56 UTC | 2026-09-26 11:58 UTC | 4h 2m |
| HBTDZ | HBT | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-09-26 11:08 UTC | 2026-09-26 11:53 UTC | 44m |
| THY3032 | Turkish Airlines | Antalya International Airport (LTAI) | Bezymyanka Airfield (UWWG) | 2026-09-26 08:31 UTC | 2026-09-26 11:49 UTC | 3h 17m |
| OZN946 | OZN | Miami Executive Airport (KTMB) | Miami Homestead General Aviation Airport (KX51) | 2026-09-26 11:33 UTC | 2026-09-26 11:45 UTC | 12m |
| N46390 |  | Lakeland Linder International Airport (KLAL) | Zephyrhills Municipal Airport (KZPH) | 2026-09-26 10:55 UTC | 2026-09-26 11:41 UTC | 46m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-09-26 10:42 UTC | 2026-09-26 11:34 UTC | 51m |
| DFALL | DFA | Hildesheim Airport (EDVM) | Hildesheim Airport (EDVM) | 2026-09-26 11:12 UTC | 2026-09-26 11:34 UTC | 21m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-09-26 10:37 UTC | 2026-09-26 11:29 UTC | 51m |
| PH712 |  | Twenthe Airport (EHTW) | Twenthe Airport (EHTW) | 2026-09-26 11:21 UTC | 2026-09-26 11:28 UTC | 6m |
| JAG3754 | JAG | Sharjah International Airport (OMSJ) | Tribhuvan International Airport (VNKT) | 2026-09-26 07:45 UTC | 2026-09-26 11:22 UTC | 3h 36m |
| GCKXX | GCK | Farthing Corner/Stoneacre Farm Airport (EGMF) | London Biggin Hill Airport (EGKB) | 2026-09-26 11:00 UTC | 2026-09-26 11:16 UTC | 16m |
| N5197R |  | Turlock Municipal Airport (KO15) | Truckee-Tahoe Airport (KTRK) | 2026-09-26 10:24 UTC | 2026-09-26 11:15 UTC | 51m |
| AIZ1841 | AIZ | Ben Gurion International Airport (LLBG) | Ein Yahav Airfield (LLEY) | 2026-09-26 10:51 UTC | 2026-09-26 11:09 UTC | 18m |
| JAL377 | Japan Airlines | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-26 09:55 UTC | 2026-09-26 11:05 UTC | 1h 10m |
| JST475 | JST | Newcastle Airport (YWLM) | Melbourne International Airport (YMML) | 2026-09-26 09:28 UTC | 2026-09-26 11:05 UTC | 1h 36m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-26 10:16 UTC | 2026-09-26 11:02 UTC | 45m |
| JES3142 | JES | Ministro Pistarini International Airport (SAEZ) | Bernardo De Irigoyen Airport (SATI) | 2026-09-26 09:41 UTC | 2026-09-26 10:59 UTC | 1h 17m |
| AFR87AC | Air France | Charles de Gaulle International Airport (LFPG) | Kasteli Airport (LGTL) | 2026-09-26 08:07 UTC | 2026-09-26 10:59 UTC | 2h 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
