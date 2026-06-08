# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_06:19:01_UTC-green)

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

**Latest saved flight:** 2026-06-08 06:19:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-08 06:19:01 UTC

- **105,759** saved flights
- **37,201** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,759** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,294,162.8 tonnes** estimated CO2 emissions
- **75,023,933 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4361 |
| 2 | SkyWest Airlines | 3979 |
| 3 | IndiGo | 2102 |
| 4 | EJA | 2023 |
| 5 | American Airlines | 1696 |
| 6 | Southwest Airlines | 1597 |
| 7 | ENY | 1327 |
| 8 | Delta Air Lines | 1255 |
| 9 | Lufthansa | 1212 |
| 10 | Vueling | 971 |
| 11 | LATAM Airlines | 934 |
| 12 | WIF | 927 |
| 13 | AXM | 908 |
| 14 | AZU | 852 |
| 15 | LXJ | 798 |
| 16 | Swiss International | 765 |
| 17 | All Nippon Airways | 739 |
| 18 | Alaska Airlines | 732 |
| 19 | QLK | 710 |
| 20 | easyJet | 686 |
| 21 | EJU | 670 |
| 22 | Cathay Pacific | 633 |
| 23 | AEE | 610 |
| 24 | VIV | 605 |
| 25 | Air France | 603 |
| 26 | United Airlines | 586 |
| 27 | MXY | 578 |
| 28 | CXK | 557 |
| 29 | Japan Airlines | 526 |
| 30 | AXB | 516 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88930 |
| 2 | 🇪🇸 ES | 7273 |
| 3 | 🇮🇳 IN | 6629 |
| 4 | 🇦🇺 AU | 6381 |
| 5 | 🇧🇷 BR | 5782 |
| 6 | 🇩🇪 DE | 5682 |
| 7 | 🇮🇹 IT | 5654 |
| 8 | 🇨🇦 CA | 5504 |
| 9 | 🇯🇵 JP | 4860 |
| 10 | 🇬🇧 GB | 4462 |
| 11 | 🇫🇷 FR | 4197 |
| 12 | 🇨🇴 CO | 3645 |
| 13 | 🇲🇽 MX | 3161 |
| 14 | 🇬🇷 GR | 3009 |
| 15 | 🇳🇴 NO | 2930 |
| 16 | 🇨🇭 CH | 2703 |
| 17 | 🇲🇾 MY | 2331 |
| 18 | 🇹🇷 TR | 2036 |
| 19 | 🇿🇦 ZA | 1826 |
| 20 | 🇳🇿 NZ | 1766 |
| 21 | 🇰🇷 KR | 1763 |
| 22 | 🇹🇭 TH | 1755 |
| 23 | 🇵🇱 PL | 1721 |
| 24 | 🇵🇭 PH | 1561 |
| 25 | 🇬🇹 GT | 1529 |
| 26 | 🇲🇦 MA | 1169 |
| 27 | 🇲🇴 MO | 1107 |
| 28 | 🇳🇱 NL | 1036 |
| 29 | 🇲🇪 ME | 1014 |
| 30 | 🇭🇷 HR | 923 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2296 |
| 2 | Denver International Airport |  | US | 1810 |
| 3 | Tokyo International Airport |  | JP | 1610 |
| 4 | Indira Gandhi International Airport |  | IN | 1441 |
| 5 | Harry Reid International Airport |  | US | 1354 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1336 |
| 7 | Guaymaral Airport |  | CO | 1327 |
| 8 | Frankfurt am Main International Airport |  | DE | 1202 |
| 9 | Zurich Airport |  | CH | 1196 |
| 10 | La Aurora Airport |  | GT | 1177 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1140 |
| 12 | El Dorado International Airport |  | CO | 1112 |
| 13 | Macau International Airport |  | MO | 1107 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1066 |
| 15 | Chicago O'Hare International Airport |  | US | 1063 |
| 16 | Madrid Barajas International Airport |  | ES | 925 |
| 17 | Kuala Lumpur International Airport |  | MY | 914 |
| 18 | Salt Lake City International Airport |  | US | 905 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 905 |
| 20 | Capua Airport |  | IT | 894 |
| 21 | Charlotte/Douglas International Airport |  | US | 822 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 813 |
| 23 | Charles de Gaulle International Airport |  | FR | 802 |
| 24 | Congonhas Airport |  | BR | 801 |
| 25 | Malpensa International Airport |  | IT | 792 |
| 26 | Bengaluru International Airport |  | IN | 792 |
| 27 | Daniel K Inouye International Airport |  | US | 721 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 715 |
| 30 | Barcelona International Airport |  | ES | 692 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 683 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 682 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 680 |
| 34 | Amsterdam Airport Schiphol |  | NL | 642 |
| 35 | Don Mueang International Airport |  | TH | 641 |
| 36 | Vitoria/Foronda Airport |  | ES | 633 |
| 37 | Calgary International Airport |  | CA | 625 |
| 38 | Seattle-Tacoma International Airport |  | US | 616 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 606 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 605 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 548 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 389 | 21m | 244 km | 1,638.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 284 | 24m | 225 km | 1,101.8 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 267 | 14m | 114 km | 523.7 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 260 | 1h 25m | 910 km | 4,080.0 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 244 | 1h 10m | 770 km | 3,241.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 211 | 26m | 275 km | 999.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 146 | 31m | 369 km | 929.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 146 | 27m | 152 km | 381.6 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 142 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 139 | 18m | 144 km | 345.8 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 130 | 1h 1m | 695 km | 1,558.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 123 | 1h 43m | 1,423 km | 3,018.6 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 122 | 44m | 241 km | 506.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBZJB | HBZ | LSMF (LSMF) | Meiringen Airport (LSMM) | 2026-06-08 05:49 UTC | 2026-06-08 06:19 UTC | 29m |
| DLH9TT | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-06-08 04:56 UTC | 2026-06-08 05:45 UTC | 48m |
| N357EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-08 04:51 UTC | 2026-06-08 05:43 UTC | 52m |
| THA132 | Thai Airways | Suvarnabhumi Airport (VTBS) | Phayao Ban Chiang Kham Airport (VTCB) | 2026-06-08 04:47 UTC | 2026-06-08 05:40 UTC | 53m |
| WVU | WVU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-06-08 05:26 UTC | 2026-06-08 05:39 UTC | 12m |
| CATS00 | CAT | Osan Air Base (RKSO) | G 417 Airport (RK34) | 2026-06-08 05:07 UTC | 2026-06-08 05:37 UTC | 29m |
| UBG533 | UBG | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-06-08 05:12 UTC | 2026-06-08 05:36 UTC | 24m |
| BTI13F | BTI | Riga International Airport (EVRA) | Copenhagen Kastrup Airport (EKCH) | 2026-06-08 04:28 UTC | 2026-06-08 05:34 UTC | 1h 5m |
| LNK621M | LNK | Cape Town International Airport (FACT) | Hendrik Swellengrebel Airport (FASX) | 2026-06-08 05:16 UTC | 2026-06-08 05:33 UTC | 16m |
| SAA030 | SAA | O. R. Tambo International Airport (FAOR) | Dwaalboom Airport (FADB) | 2026-06-08 05:10 UTC | 2026-06-08 05:31 UTC | 21m |
| N61NG |  | Oakland San Francisco Bay Airport (KOAK) | Sierraville Dearwater Airport (KO79) | 2026-06-08 04:50 UTC | 2026-06-08 05:28 UTC | 38m |
| ANA283 | All Nippon Airways | Tokyo International Airport (RJTT) | Takamatsu Airport (RJOT) | 2026-06-08 04:44 UTC | 2026-06-08 05:27 UTC | 43m |
| N58AZ |  | Bagdad Airport (KE51) | Outback Ranch Airstrip (AZ01) | 2026-06-08 05:12 UTC | 2026-06-08 05:25 UTC | 13m |
| SFJ13 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-06-08 04:11 UTC | 2026-06-08 05:24 UTC | 1h 12m |
| RYR5914 | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-06-08 04:33 UTC | 2026-06-08 05:23 UTC | 50m |
| N734ST |  | Bend Municipal Airport (KBDN) | Ochs Private Airport (72OR) | 2026-06-08 04:54 UTC | 2026-06-08 05:23 UTC | 29m |
| KHV | KHV | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-08 04:47 UTC | 2026-06-08 05:23 UTC | 35m |
| AAAAAAA | AAA | Suwon Airport (RKSW) | RKTS (RKTS) | 2026-06-08 05:03 UTC | 2026-06-08 05:22 UTC | 19m |
| UIA8985 | UIA | Tainan Airport (RCNN) | Makung Airport (RCQC) | 2026-06-08 05:01 UTC | 2026-06-08 05:21 UTC | 20m |
| QFA618 | Qantas | Melbourne International Airport (YMML) | Brisbane International Airport (YBBN) | 2026-06-08 03:23 UTC | 2026-06-08 05:20 UTC | 1h 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
