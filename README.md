# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_04:54:41_UTC-green)

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

**Latest saved flight:** 2026-06-15 04:54:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-15 04:54:41 UTC

- **111,026** saved flights
- **38,718** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **111,026** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,358,016.7 tonnes** estimated CO2 emissions
- **78,725,606 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4586 |
| 2 | SkyWest Airlines | 4152 |
| 3 | IndiGo | 2175 |
| 4 | EJA | 2150 |
| 5 | American Airlines | 1749 |
| 6 | Southwest Airlines | 1662 |
| 7 | ENY | 1381 |
| 8 | Delta Air Lines | 1312 |
| 9 | Lufthansa | 1255 |
| 10 | Vueling | 1020 |
| 11 | LATAM Airlines | 980 |
| 12 | WIF | 979 |
| 13 | AXM | 935 |
| 14 | AZU | 920 |
| 15 | LXJ | 851 |
| 16 | Swiss International | 795 |
| 17 | All Nippon Airways | 772 |
| 18 | Alaska Airlines | 754 |
| 19 | QLK | 730 |
| 20 | easyJet | 714 |
| 21 | EJU | 706 |
| 22 | Cathay Pacific | 659 |
| 23 | AEE | 628 |
| 24 | VIV | 623 |
| 25 | Air France | 621 |
| 26 | United Airlines | 617 |
| 27 | MXY | 593 |
| 28 | CXK | 580 |
| 29 | AXB | 546 |
| 30 | GLO | 544 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 93435 |
| 2 | 🇪🇸 ES | 7614 |
| 3 | 🇮🇳 IN | 6860 |
| 4 | 🇦🇺 AU | 6604 |
| 5 | 🇧🇷 BR | 6134 |
| 6 | 🇮🇹 IT | 5982 |
| 7 | 🇩🇪 DE | 5940 |
| 8 | 🇨🇦 CA | 5831 |
| 9 | 🇯🇵 JP | 5025 |
| 10 | 🇬🇧 GB | 4754 |
| 11 | 🇫🇷 FR | 4436 |
| 12 | 🇨🇴 CO | 3775 |
| 13 | 🇲🇽 MX | 3296 |
| 14 | 🇬🇷 GR | 3158 |
| 15 | 🇳🇴 NO | 3070 |
| 16 | 🇨🇭 CH | 2834 |
| 17 | 🇲🇾 MY | 2416 |
| 18 | 🇹🇷 TR | 2204 |
| 19 | 🇿🇦 ZA | 1887 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1830 |
| 22 | 🇵🇱 PL | 1822 |
| 23 | 🇳🇿 NZ | 1822 |
| 24 | 🇵🇭 PH | 1614 |
| 25 | 🇬🇹 GT | 1588 |
| 26 | 🇲🇦 MA | 1221 |
| 27 | 🇲🇴 MO | 1151 |
| 28 | 🇲🇪 ME | 1088 |
| 29 | 🇳🇱 NL | 1084 |
| 30 | 🇭🇷 HR | 965 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2366 |
| 2 | Denver International Airport |  | US | 1884 |
| 3 | Tokyo International Airport |  | JP | 1665 |
| 4 | Indira Gandhi International Airport |  | IN | 1492 |
| 5 | Guaymaral Airport |  | CO | 1405 |
| 6 | Harry Reid International Airport |  | US | 1400 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1380 |
| 8 | Zurich Airport |  | CH | 1246 |
| 9 | Frankfurt am Main International Airport |  | DE | 1229 |
| 10 | La Aurora Airport |  | GT | 1221 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1193 |
| 12 | Macau International Airport |  | MO | 1151 |
| 13 | El Dorado International Airport |  | CO | 1135 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1113 |
| 15 | Chicago O'Hare International Airport |  | US | 1102 |
| 16 | Madrid Barajas International Airport |  | ES | 969 |
| 17 | Capua Airport |  | IT | 963 |
| 18 | Salt Lake City International Airport |  | US | 941 |
| 19 | Kuala Lumpur International Airport |  | MY | 941 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 934 |
| 21 | Charlotte/Douglas International Airport |  | US | 854 |
| 22 | Congonhas Airport |  | BR | 854 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 836 |
| 24 | Charles de Gaulle International Airport |  | FR | 832 |
| 25 | Bengaluru International Airport |  | IN | 828 |
| 26 | Malpensa International Airport |  | IT | 810 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 756 |
| 28 | Ninoy Aquino International Airport |  | PH | 744 |
| 29 | Daniel K Inouye International Airport |  | US | 737 |
| 30 | Tenerife Norte Airport |  | ES | 731 |
| 31 | Barcelona International Airport |  | ES | 727 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 726 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 711 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 659 |
| 37 | Calgary International Airport |  | CA | 656 |
| 38 | Seattle-Tacoma International Airport |  | US | 639 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 638 |
| 40 | Viracopos International Airport |  | BR | 628 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 405 | 21m | 244 km | 1,705.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 286 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 261 | 1h 10m | 770 km | 3,467.2 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 221 | 26m | 275 km | 1,047.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 166 | 20m | 99 km | 284.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 161 | 27m | 215 km | 596.3 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 158 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 150 | 31m | 369 km | 954.8 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 140 | 44m | 241 km | 581.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 134 | 1h 1m | 695 km | 1,606.3 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 124 | 1h 2m | 611 km | 1,307.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-06-14 14:26 UTC | 2026-06-15 04:54 UTC | 14h 28m |
| PQR | PQR | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-06-15 03:20 UTC | 2026-06-15 04:52 UTC | 1h 32m |
| DIV | DIV | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-06-15 03:48 UTC | 2026-06-15 04:37 UTC | 49m |
| MVJ93 | MVJ | Columbus Airport (KCSG) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-14 23:59 UTC | 2026-06-15 04:37 UTC | 4h 38m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-15 04:20 UTC | 2026-06-15 04:34 UTC | 14m |
| MTNG305 | MTN | Kamphaeng Saen Airport (VTBK) | Takhli Airport (VTPI) | 2026-06-15 04:13 UTC | 2026-06-15 04:31 UTC | 17m |
| KGJ | KGJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-15 03:57 UTC | 2026-06-15 04:30 UTC | 32m |
| UAL3915 | United Airlines | George Bush Intcntl/Houston Airport (KIAH) | 5TA4 (5TA4) | 2026-06-15 03:23 UTC | 2026-06-15 04:28 UTC | 1h 4m |
| CXK170 | CXK | Flying Cloud Airport (KFCM) | Rochester International Airport (KRST) | 2026-06-15 03:11 UTC | 2026-06-15 04:27 UTC | 1h 16m |
| N638DS |  | Skypark Airport (KBTF) | Wendover Airport (KENV) | 2026-06-15 03:48 UTC | 2026-06-15 04:25 UTC | 37m |
| VTNJP | VTN | Dehradun Airport (VIDN) | Bharkot Airport (VI82) | 2026-06-15 04:07 UTC | 2026-06-15 04:24 UTC | 17m |
| ZKIDU | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-06-15 03:59 UTC | 2026-06-15 04:23 UTC | 23m |
| CWA929 | CWA | Edmonton International Airport (CYEG) | St. Paul Airport (CEW3) | 2026-06-15 03:59 UTC | 2026-06-15 04:20 UTC | 20m |
| RYR8QW | Ryanair | Sigonella Airport (LICZ) | Salerno / Pontecagnano Airport (LIRI) | 2026-06-15 03:49 UTC | 2026-06-15 04:19 UTC | 30m |
| VOZ1690 | Virgin Australia | Gold Coast Airport (YBCG) | Braidwood Airport (YBAO) | 2026-06-15 03:05 UTC | 2026-06-15 04:19 UTC | 1h 14m |
| QLK534D | QLK | Brisbane International Airport (YBBN) | Tara Airport (YTAA) | 2026-06-15 03:51 UTC | 2026-06-15 04:19 UTC | 27m |
| N900EM |  | Barrow County Airport (KWDR) | Chiriaco Summit Airport (KL77) | 2026-06-15 00:00 UTC | 2026-06-15 04:18 UTC | 4h 17m |
| AZU2678 | AZU | Viracopos International Airport (SBKP) | Ouricuri Airport (SNOY) | 2026-06-15 02:08 UTC | 2026-06-15 04:17 UTC | 2h 9m |
| ANA1087 | All Nippon Airways | Tokyo International Airport (RJTT) | Tottori Airport (RJOR) | 2026-06-15 03:26 UTC | 2026-06-15 04:16 UTC | 49m |
| N399MA |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-06-15 03:41 UTC | 2026-06-15 04:14 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
