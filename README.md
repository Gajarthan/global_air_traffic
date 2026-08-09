# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_05:49:42_UTC-green)

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

**Latest saved flight:** 2026-08-09 05:49:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 05:49:42 UTC

- **180,271** saved flights
- **57,738** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,271** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,166,390.2 tonnes** estimated CO2 emissions
- **125,587,840 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7126 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3156 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2817 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1680 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1600 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1487 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1229 |
| 16 | Swiss International | 1226 |
| 17 | AXM | 1216 |
| 18 | QLK | 1106 |
| 19 | Alaska Airlines | 1095 |
| 20 | EJU | 1095 |
| 21 | All Nippon Airways | 1094 |
| 22 | VIV | 996 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 939 |
| 27 | United Airlines | 929 |
| 28 | Air France | 924 |
| 29 | MXY | 905 |
| 30 | PGT | 900 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154705 |
| 2 | 🇪🇸 ES | 11554 |
| 3 | 🇧🇷 BR | 10344 |
| 4 | 🇦🇺 AU | 10149 |
| 5 | 🇮🇳 IN | 9890 |
| 6 | 🇨🇦 CA | 9848 |
| 7 | 🇮🇹 IT | 9288 |
| 8 | 🇩🇪 DE | 8897 |
| 9 | 🇬🇧 GB | 8309 |
| 10 | 🇯🇵 JP | 7278 |
| 11 | 🇫🇷 FR | 7154 |
| 12 | 🇨🇴 CO | 6707 |
| 13 | 🇬🇷 GR | 5253 |
| 14 | 🇲🇽 MX | 5163 |
| 15 | 🇨🇭 CH | 4791 |
| 16 | 🇳🇴 NO | 4646 |
| 17 | 🇹🇷 TR | 4594 |
| 18 | 🇲🇾 MY | 3173 |
| 19 | 🇵🇱 PL | 2999 |
| 20 | 🇿🇦 ZA | 2924 |
| 21 | 🇹🇭 TH | 2741 |
| 22 | 🇳🇿 NZ | 2602 |
| 23 | 🇵🇭 PH | 2386 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2253 |
| 26 | 🇲🇦 MA | 1817 |
| 27 | 🇭🇷 HR | 1793 |
| 28 | 🇲🇪 ME | 1635 |
| 29 | 🇳🇱 NL | 1617 |
| 30 | 🇲🇴 MO | 1511 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3732 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2260 |
| 4 | Guaymaral Airport |  | CO | 2223 |
| 5 | Indira Gandhi International Airport |  | IN | 2205 |
| 6 | Harry Reid International Airport |  | US | 2126 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1938 |
| 8 | Zurich Airport |  | CH | 1910 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1615 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1564 |
| 16 | Macau International Airport |  | MO | 1511 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1436 |
| 19 | Madrid Barajas International Airport |  | ES | 1409 |
| 20 | Capua Airport |  | IT | 1401 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1350 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1284 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1265 |
| 24 | Malpensa International Airport |  | IT | 1241 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1216 |
| 27 | Kuala Lumpur International Airport |  | MY | 1195 |
| 28 | Bengaluru International Airport |  | IN | 1178 |
| 29 | Ninoy Aquino International Airport |  | PH | 1123 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1121 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1073 |
| 33 | Seattle-Tacoma International Airport |  | US | 1041 |
| 34 | Daniel K Inouye International Airport |  | US | 1038 |
| 35 | Viracopos International Airport |  | BR | 1036 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1029 |
| 38 | Oslo Gardermoen Airport |  | NO | 998 |
| 39 | Tenerife Norte Airport |  | ES | 983 |
| 40 | Amsterdam Airport Schiphol |  | NL | 974 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 667 | 21m | 244 km | 2,808.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 425 | 24m | 225 km | 1,648.8 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 424 | 1h 8m | 770 km | 5,632.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 301 | 27m | 275 km | 1,426.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 297 | 1h 7m | 706 km | 3,616.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 253 | 1h 48m | 1,423 km | 6,209.0 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 215 | 19m | 144 km | 534.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 211 | 1h 38m | 1,156 km | 4,209.4 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 209 | 31m | 369 km | 1,330.3 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 205 | 24m | 218 km | 772.3 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 05:39 UTC | 2026-08-09 05:49 UTC | 10m |
| AWH95W | AWH | Nice-Cote d'Azur Airport (LFMN) | Bern Belp Airport (LSZB) | 2026-08-09 05:01 UTC | 2026-08-09 05:41 UTC | 40m |
| YTB | YTB | Wondai Airport (YWND) | Sunshine Coast Airport (YBMC) | 2026-08-09 04:55 UTC | 2026-08-09 05:26 UTC | 31m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 04:54 UTC | 2026-08-09 05:25 UTC | 31m |
| QLK35D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Ballina Byron Gateway Airport (YBNA) | 2026-08-09 04:17 UTC | 2026-08-09 05:25 UTC | 1h 7m |
| YTG | YTG | Watts Bridge Airport (YWSG) | Sunshine Coast Airport (YBMC) | 2026-08-09 04:51 UTC | 2026-08-09 05:16 UTC | 24m |
| N886LF |  | Richland Airport (KRLD) | Cottonwood Municipal Airport (KS84) | 2026-08-09 04:43 UTC | 2026-08-09 05:15 UTC | 32m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-08-09 04:31 UTC | 2026-08-09 05:11 UTC | 40m |
| KLM1708 | KLM Royal Dutch | Luxembourg-Findel International Airport (ELLX) | Amsterdam Airport Schiphol (EHAM) | 2026-08-09 04:12 UTC | 2026-08-09 05:09 UTC | 56m |
| IVW | IVW | Redcliffe Airport (YRED) | Sunshine Coast Airport (YBMC) | 2026-08-09 02:54 UTC | 2026-08-09 05:07 UTC | 2h 13m |
| JST631 | JST | Gold Coast Airport (YBCG) | Avalon Airport (YMAV) | 2026-08-09 03:05 UTC | 2026-08-09 05:04 UTC | 1h 59m |
| RXA2125 | RXA | Perth International Airport (YPPH) | Frankland Airport (YFRK) | 2026-08-09 04:16 UTC | 2026-08-09 05:02 UTC | 46m |
| XCN81 | XCN | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-08-09 04:37 UTC | 2026-08-09 04:57 UTC | 19m |
| ANZ270L | ANZ | Auckland International Airport (NZAA) | Kerikeri Airport (NZKK) | 2026-08-09 04:21 UTC | 2026-08-09 04:52 UTC | 30m |
| JST836 | JST | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-08-09 03:36 UTC | 2026-08-09 04:48 UTC | 1h 11m |
| RAM956 | Royal Air Maroc | Mohammed V International Airport (GMMN) | Malpensa International Airport (LIMC) | 2026-08-09 02:13 UTC | 2026-08-09 04:47 UTC | 2h 33m |
| ZSOEE | ZSO | O. R. Tambo International Airport (FAOR) | New Largo Airport (FANL) | 2026-08-09 04:32 UTC | 2026-08-09 04:44 UTC | 12m |
| JAL665 | Japan Airlines | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-08-09 03:37 UTC | 2026-08-09 04:36 UTC | 59m |
| AEE352 | AEE | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-08-09 04:15 UTC | 2026-08-09 04:34 UTC | 19m |
| FD608 |  | Perth Jandakot Airport (YPJT) | Kellerberrin Airport (YKEB) | 2026-08-09 04:04 UTC | 2026-08-09 04:32 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
