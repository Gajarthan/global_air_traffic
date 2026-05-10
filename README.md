# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_06:06:55_UTC-green)

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

**Latest saved flight:** 2026-05-10 06:06:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-10 06:06:55 UTC

- **76,551** saved flights
- **28,058** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **76,551** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **947,327.0 tonnes** estimated CO2 emissions
- **54,917,508 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3276 |
| 2 | SkyWest Airlines | 2847 |
| 3 | IndiGo | 1701 |
| 4 | EJA | 1410 |
| 5 | American Airlines | 1201 |
| 6 | Southwest Airlines | 1118 |
| 7 | Lufthansa | 995 |
| 8 | ENY | 961 |
| 9 | Delta Air Lines | 789 |
| 10 | Vueling | 734 |
| 11 | AXM | 716 |
| 12 | LATAM Airlines | 708 |
| 13 | WIF | 655 |
| 14 | All Nippon Airways | 619 |
| 15 | AZU | 611 |
| 16 | QLK | 587 |
| 17 | Swiss International | 578 |
| 18 | LXJ | 564 |
| 19 | Alaska Airlines | 540 |
| 20 | easyJet | 503 |
| 21 | Cathay Pacific | 496 |
| 22 | AEE | 493 |
| 23 | EJU | 490 |
| 24 | VIV | 458 |
| 25 | Japan Airlines | 447 |
| 26 | Air France | 443 |
| 27 | AXB | 424 |
| 28 | CXK | 391 |
| 29 | AIQ | 382 |
| 30 | MXY | 376 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 61869 |
| 2 | 🇪🇸 ES | 5465 |
| 3 | 🇮🇳 IN | 5346 |
| 4 | 🇦🇺 AU | 5000 |
| 5 | 🇩🇪 DE | 4297 |
| 6 | 🇧🇷 BR | 4278 |
| 7 | 🇮🇹 IT | 4188 |
| 8 | 🇯🇵 JP | 3983 |
| 9 | 🇨🇦 CA | 3815 |
| 10 | 🇬🇧 GB | 3274 |
| 11 | 🇫🇷 FR | 3022 |
| 12 | 🇨🇴 CO | 2696 |
| 13 | 🇲🇽 MX | 2357 |
| 14 | 🇬🇷 GR | 2251 |
| 15 | 🇳🇴 NO | 2097 |
| 16 | 🇨🇭 CH | 2070 |
| 17 | 🇲🇾 MY | 1782 |
| 18 | 🇿🇦 ZA | 1463 |
| 19 | 🇳🇿 NZ | 1388 |
| 20 | 🇹🇷 TR | 1373 |
| 21 | 🇹🇭 TH | 1365 |
| 22 | 🇵🇱 PL | 1274 |
| 23 | 🇵🇭 PH | 1229 |
| 24 | 🇰🇷 KR | 1200 |
| 25 | 🇬🇹 GT | 1199 |
| 26 | 🇲🇦 MA | 903 |
| 27 | 🇲🇴 MO | 902 |
| 28 | 🇲🇪 ME | 811 |
| 29 | 🇳🇱 NL | 797 |
| 30 | 🇭🇷 HR | 657 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1707 |
| 2 | Tokyo International Airport |  | JP | 1338 |
| 3 | Denver International Airport |  | US | 1287 |
| 4 | Indira Gandhi International Airport |  | IN | 1127 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1104 |
| 6 | Frankfurt am Main International Airport |  | DE | 994 |
| 7 | Harry Reid International Airport |  | US | 951 |
| 8 | Macau International Airport |  | MO | 902 |
| 9 | La Aurora Airport |  | GT | 900 |
| 10 | Zurich Airport |  | CH | 900 |
| 11 | Guaymaral Airport |  | CO | 890 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 768 |
| 14 | Chicago O'Hare International Airport |  | US | 751 |
| 15 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 742 |
| 16 | Kuala Lumpur International Airport |  | MY | 716 |
| 17 | Madrid Barajas International Airport |  | ES | 711 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 681 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 665 |
| 20 | Bengaluru International Airport |  | IN | 663 |
| 21 | Malpensa International Airport |  | IT | 661 |
| 22 | Salt Lake City International Airport |  | US | 628 |
| 23 | Charlotte/Douglas International Airport |  | US | 604 |
| 24 | Congonhas Airport |  | BR | 604 |
| 25 | Charles de Gaulle International Airport |  | FR | 594 |
| 26 | Capua Airport |  | IT | 594 |
| 27 | Tenerife Norte Airport |  | ES | 569 |
| 28 | Daniel K Inouye International Airport |  | US | 559 |
| 29 | Ninoy Aquino International Airport |  | PH | 558 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 547 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 523 |
| 32 | Barcelona International Airport |  | ES | 518 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 517 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 503 |
| 35 | Don Mueang International Airport |  | TH | 483 |
| 36 | Vitoria/Foronda Airport |  | ES | 481 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 480 |
| 38 | Amsterdam Airport Schiphol |  | NL | 479 |
| 39 | O. R. Tambo International Airport |  | ZA | 459 |
| 40 | Calgary International Airport |  | CA | 457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 370 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 274 | 21m | 244 km | 1,153.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 222 | 24m | 225 km | 861.3 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 213 | 28m | 304 km | 1,116.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 207 | 1h 27m | 910 km | 3,248.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 195 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 183 | 19m | 165 km | 520.5 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 181 | 31m | - | - |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 168 | 1h 12m | 770 km | 2,231.7 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 163 | 26m | 275 km | 772.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 139 | 20m | 99 km | 238.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 135 | 44m | 452 km | 1,052.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 122 | 31m | 369 km | 776.6 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 118 | 27m | 152 km | 308.4 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 114 | 27m | 215 km | 422.2 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 114 | 20m | 147 km | 288.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 113 | 20m | 250 km | 488.1 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 109 | 14m | 154 km | 288.8 t |
| 21 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 103 | 1h 2m | 695 km | 1,234.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 102 | 1h 42m | 1,423 km | 2,503.2 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 102 | 57m | 493 km | 867.8 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 100 | 23m | 55 km | 95.0 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 97 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 95 | 1h 19m | 961 km | 1,574.7 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 95 | 52m | 556 km | 910.7 t |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 94 | 18m | 144 km | 233.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AUA96F | Austrian Airlines | Vienna International Airport (LOWW) | Korsor Airport (EKKO) | 2026-05-10 05:18 UTC | 2026-05-10 06:06 UTC | 48m |
| AEE6400 | AEE | Thessaloniki Macedonia International Airport (LGTS) | Ioannina Airport (LGIO) | 2026-05-10 05:42 UTC | 2026-05-10 06:03 UTC | 20m |
| IOV | IOV | YSMB (YSMB) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-10 05:48 UTC | 2026-05-10 06:02 UTC | 13m |
| DLH4YF | Lufthansa | Frankfurt am Main International Airport (EDDF) | Malpensa International Airport (LIMC) | 2026-05-10 05:03 UTC | 2026-05-10 06:01 UTC | 57m |
| AM261 |  | Sydney Kingsford Smith International Airport (YSSY) | Jerilderie Airport (YJER) | 2026-05-10 05:11 UTC | 2026-05-10 05:59 UTC | 47m |
| RYR303F | Ryanair | Berlin Brandenburg Airport (EDDB) | Malpensa International Airport (LIMC) | 2026-05-10 04:10 UTC | 2026-05-10 05:44 UTC | 1h 34m |
| HDSN01 | HDS | Bathurst Airport (YBTH) | RAAF Base Richmond (YSRI) | 2026-05-10 05:15 UTC | 2026-05-10 05:38 UTC | 23m |
| BTN700 | BTN | Hashimara Air Force Station (VE44) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-05-10 04:49 UTC | 2026-05-10 05:38 UTC | 49m |
| QLK225D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-05-10 04:56 UTC | 2026-05-10 05:33 UTC | 36m |
| STA613D | STA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-05-10 05:20 UTC | 2026-05-10 05:25 UTC | 4m |
| HFA601 | HFA | Haifa International Airport (LLHA) | Yotvata Airfield (LLYT) | 2026-05-10 04:38 UTC | 2026-05-10 05:24 UTC | 45m |
| CPA250 | Cathay Pacific | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-05-09 17:31 UTC | 2026-05-10 05:23 UTC | 11h 52m |
| AEE348 | AEE | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-05-10 05:04 UTC | 2026-05-10 05:22 UTC | 18m |
| AIQ2010 | AIQ | Chiang Mai International Airport (VTCC) | Khon Kaen Airport (VTUK) | 2026-05-10 04:40 UTC | 2026-05-10 05:20 UTC | 40m |
| AIQ3209 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-10 04:30 UTC | 2026-05-10 05:20 UTC | 49m |
| THA570 | Thai Airways | Suvarnabhumi Airport (VTBS) | Xieng Khouang Airport (VLXK) | 2026-05-10 04:37 UTC | 2026-05-10 05:19 UTC | 42m |
| ANE72KM | ANE | Palma De Mallorca Airport (LEPA) | Menorca Airport (LEMH) | 2026-05-10 05:03 UTC | 2026-05-10 05:19 UTC | 15m |
| WZZ5AN | Wizz Air | Belgrade Nikola Tesla Airport (LYBE) | Kalmar Airport (ESMQ) | 2026-05-10 03:56 UTC | 2026-05-10 05:18 UTC | 1h 22m |
| ANA295 | All Nippon Airways | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 2026-05-10 04:35 UTC | 2026-05-10 05:18 UTC | 43m |
| JAL2765 | Japan Airlines | Okadama Airport (RJCO) | Tokachi Airport (RJCT) | 2026-05-10 05:01 UTC | 2026-05-10 05:18 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
