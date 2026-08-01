# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_06:05:55_UTC-green)

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

**Latest saved flight:** 2026-08-01 06:05:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 06:05:55 UTC

- **163,925** saved flights
- **53,950** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **163,925** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,967,939.9 tonnes** estimated CO2 emissions
- **114,083,472 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6540 |
| 2 | SkyWest Airlines | 5982 |
| 3 | EJA | 3255 |
| 4 | IndiGo | 2878 |
| 5 | American Airlines | 2590 |
| 6 | Southwest Airlines | 2578 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1958 |
| 9 | LATAM Airlines | 1533 |
| 10 | Lufthansa | 1531 |
| 11 | AZU | 1439 |
| 12 | WIF | 1378 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1133 |
| 16 | Swiss International | 1125 |
| 17 | easyJet | 1072 |
| 18 | Alaska Airlines | 1017 |
| 19 | QLK | 1009 |
| 20 | All Nippon Airways | 1002 |
| 21 | EJU | 1002 |
| 22 | VIV | 906 |
| 23 | CXK | 878 |
| 24 | Cathay Pacific | 870 |
| 25 | United Airlines | 863 |
| 26 | GLO | 858 |
| 27 | AEE | 856 |
| 28 | MXY | 846 |
| 29 | Air France | 844 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141784 |
| 2 | 🇪🇸 ES | 10474 |
| 3 | 🇧🇷 BR | 9352 |
| 4 | 🇦🇺 AU | 9243 |
| 5 | 🇮🇳 IN | 9038 |
| 6 | 🇨🇦 CA | 8936 |
| 7 | 🇮🇹 IT | 8432 |
| 8 | 🇩🇪 DE | 8213 |
| 9 | 🇬🇧 GB | 7514 |
| 10 | 🇯🇵 JP | 6618 |
| 11 | 🇫🇷 FR | 6464 |
| 12 | 🇨🇴 CO | 5865 |
| 13 | 🇲🇽 MX | 4703 |
| 14 | 🇬🇷 GR | 4702 |
| 15 | 🇳🇴 NO | 4308 |
| 16 | 🇨🇭 CH | 4293 |
| 17 | 🇹🇷 TR | 3914 |
| 18 | 🇲🇾 MY | 2946 |
| 19 | 🇵🇱 PL | 2774 |
| 20 | 🇿🇦 ZA | 2655 |
| 21 | 🇳🇿 NZ | 2408 |
| 22 | 🇹🇭 TH | 2330 |
| 23 | 🇵🇭 PH | 2148 |
| 24 | 🇰🇷 KR | 2124 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1651 |
| 27 | 🇭🇷 HR | 1540 |
| 28 | 🇲🇪 ME | 1537 |
| 29 | 🇳🇱 NL | 1487 |
| 30 | 🇲🇴 MO | 1382 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3351 |
| 2 | Denver International Airport |  | US | 2730 |
| 3 | Tokyo International Airport |  | JP | 2083 |
| 4 | Guaymaral Airport |  | CO | 2063 |
| 5 | Indira Gandhi International Airport |  | IN | 2007 |
| 6 | Harry Reid International Airport |  | US | 1990 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1801 |
| 8 | Zurich Airport |  | CH | 1745 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1726 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1523 |
| 12 | El Dorado International Airport |  | CO | 1503 |
| 13 | Frankfurt am Main International Airport |  | DE | 1486 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1477 |
| 16 | Macau International Airport |  | MO | 1382 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1377 |
| 18 | Congonhas Airport |  | BR | 1355 |
| 19 | Madrid Barajas International Airport |  | ES | 1293 |
| 20 | Capua Airport |  | IT | 1283 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1252 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1160 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Kuala Lumpur International Airport |  | MY | 1119 |
| 26 | Charles de Gaulle International Airport |  | FR | 1115 |
| 27 | Malpensa International Airport |  | IT | 1083 |
| 28 | Bengaluru International Airport |  | IN | 1070 |
| 29 | Ninoy Aquino International Airport |  | PH | 1009 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1007 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 32 | Barcelona International Airport |  | ES | 967 |
| 33 | Daniel K Inouye International Airport |  | US | 959 |
| 34 | Seattle-Tacoma International Airport |  | US | 951 |
| 35 | Calgary International Airport |  | CA | 937 |
| 36 | Viracopos International Airport |  | BR | 930 |
| 37 | Scottsdale Airport |  | US | 917 |
| 38 | Tenerife Norte Airport |  | ES | 913 |
| 39 | Oslo Gardermoen Airport |  | NO | 912 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 597 | 21m | 244 km | 2,513.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 392 | 24m | 225 km | 1,520.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 303 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 244 | 22m | 55 km | 231.9 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 225 | 1h 47m | 1,423 km | 5,521.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 209 | 20m | 250 km | 902.8 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 207 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 202 | 31m | 49 km | 170.7 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 192 | 18m | 144 km | 477.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 183 | 1h 39m | 1,156 km | 3,650.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA740 | Cathay Pacific | Gia Lam Air Base (VVGL) | Macau International Airport (VMMC) | 2026-08-01 04:59 UTC | 2026-08-01 06:05 UTC | 1h 6m |
| DAL2585 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Salt Lake City International Airport (KSLC) | 2026-08-01 05:46 UTC | 2026-08-01 06:00 UTC | 13m |
| DLH441 | Lufthansa | George Bush Intcntl/Houston Airport (KIAH) | Frankfurt am Main International Airport (EDDF) | 2026-07-31 20:50 UTC | 2026-08-01 05:59 UTC | 9h 9m |
|  |  | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 2026-08-01 05:39 UTC | 2026-08-01 05:43 UTC | 3m |
| XCN81 | XCN | Boise Air Trml/Gowen Field (KBOI) | Cottonwood Creek Ranch Airport (OG50) | 2026-08-01 05:02 UTC | 2026-08-01 05:43 UTC | 41m |
| HVN592 | HVN | VV01 (VV01) | Zhuhai Airport (ZGSD) | 2026-08-01 04:27 UTC | 2026-08-01 05:35 UTC | 1h 7m |
| CES223 | China Eastern | Incheon International Airport (RKSI) | HE42 (HE42) | 2026-07-31 07:41 UTC | 2026-08-01 05:29 UTC | 21h 47m |
| RYR5914 | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-08-01 04:29 UTC | 2026-08-01 05:22 UTC | 53m |
| N905RT |  | Prineville Airport (KS39) | Six Springs Ranch Airport (OG51) | 2026-08-01 04:27 UTC | 2026-08-01 05:20 UTC | 53m |
| N587L |  | Merced Yosemite Regional Airport (KMCE) | Turlock Municipal Airport (KO15) | 2026-08-01 05:05 UTC | 2026-08-01 05:16 UTC | 10m |
| N1094W |  | Lodi Airport (K1O3) | Castle Airport (KMER) | 2026-08-01 03:46 UTC | 2026-08-01 05:14 UTC | 1h 27m |
| N481LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-08-01 04:00 UTC | 2026-08-01 05:08 UTC | 1h 7m |
| APJ359 | APJ | Narita International Airport (RJAA) | Ashiya Airport (RJFA) | 2026-08-01 03:52 UTC | 2026-08-01 05:05 UTC | 1h 13m |
| IGO573E | IndiGo | Juhu Aerodrome (VAJJ) | Dehradun Airport (VIDN) | 2026-08-01 03:19 UTC | 2026-08-01 05:01 UTC | 1h 42m |
| FDX49 | FDX | Ted Stevens Anchorage International Airport (PANC) | Taiwan Taoyuan International Airport (RCTP) | 2026-07-31 18:29 UTC | 2026-08-01 05:00 UTC | 10h 31m |
| WZZ2511 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Mikonos Airport (LGMK) | 2026-08-01 03:20 UTC | 2026-08-01 05:00 UTC | 1h 39m |
| A7GAC |  | Al Khawr Airport (OTBK) | Persian Gulf International Airport (OIBP) | 2026-08-01 04:27 UTC | 2026-08-01 04:58 UTC | 31m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-08-01 04:36 UTC | 2026-08-01 04:55 UTC | 18m |
| JMA8662 | JMA | Jomo Kenyatta International Airport (HKJK) | Nakuru Airport (HKNK) | 2026-08-01 04:36 UTC | 2026-08-01 04:54 UTC | 17m |
| GLO1468 | GLO | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Santo Antonio do Lerverger Airport (SWLV) | 2026-08-01 03:13 UTC | 2026-08-01 04:53 UTC | 1h 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
