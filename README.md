# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_03:31:54_UTC-green)

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

**Latest saved flight:** 2026-08-01 03:31:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 03:31:54 UTC

- **163,840** saved flights
- **53,934** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **163,840** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,966,730.9 tonnes** estimated CO2 emissions
- **114,013,388 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6537 |
| 2 | SkyWest Airlines | 5982 |
| 3 | EJA | 3255 |
| 4 | IndiGo | 2871 |
| 5 | American Airlines | 2590 |
| 6 | Southwest Airlines | 2575 |
| 7 | ENY | 2041 |
| 8 | Delta Air Lines | 1956 |
| 9 | LATAM Airlines | 1533 |
| 10 | Lufthansa | 1530 |
| 11 | AZU | 1437 |
| 12 | WIF | 1378 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1133 |
| 16 | Swiss International | 1124 |
| 17 | easyJet | 1072 |
| 18 | Alaska Airlines | 1016 |
| 19 | QLK | 1008 |
| 20 | EJU | 1002 |
| 21 | All Nippon Airways | 1001 |
| 22 | VIV | 905 |
| 23 | CXK | 878 |
| 24 | Cathay Pacific | 869 |
| 25 | United Airlines | 863 |
| 26 | GLO | 857 |
| 27 | AEE | 853 |
| 28 | MXY | 846 |
| 29 | Air France | 844 |
| 30 | JetBlue | 836 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141736 |
| 2 | 🇪🇸 ES | 10474 |
| 3 | 🇧🇷 BR | 9346 |
| 4 | 🇦🇺 AU | 9233 |
| 5 | 🇮🇳 IN | 9027 |
| 6 | 🇨🇦 CA | 8932 |
| 7 | 🇮🇹 IT | 8428 |
| 8 | 🇩🇪 DE | 8211 |
| 9 | 🇬🇧 GB | 7513 |
| 10 | 🇯🇵 JP | 6612 |
| 11 | 🇫🇷 FR | 6464 |
| 12 | 🇨🇴 CO | 5863 |
| 13 | 🇲🇽 MX | 4702 |
| 14 | 🇬🇷 GR | 4691 |
| 15 | 🇳🇴 NO | 4308 |
| 16 | 🇨🇭 CH | 4290 |
| 17 | 🇹🇷 TR | 3911 |
| 18 | 🇲🇾 MY | 2946 |
| 19 | 🇵🇱 PL | 2774 |
| 20 | 🇿🇦 ZA | 2653 |
| 21 | 🇳🇿 NZ | 2402 |
| 22 | 🇹🇭 TH | 2320 |
| 23 | 🇵🇭 PH | 2144 |
| 24 | 🇰🇷 KR | 2123 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1651 |
| 27 | 🇲🇪 ME | 1537 |
| 28 | 🇭🇷 HR | 1537 |
| 29 | 🇳🇱 NL | 1487 |
| 30 | 🇲🇴 MO | 1381 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3351 |
| 2 | Denver International Airport |  | US | 2729 |
| 3 | Tokyo International Airport |  | JP | 2082 |
| 4 | Guaymaral Airport |  | CO | 2062 |
| 5 | Indira Gandhi International Airport |  | IN | 2005 |
| 6 | Harry Reid International Airport |  | US | 1987 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1797 |
| 8 | Zurich Airport |  | CH | 1744 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1726 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1523 |
| 12 | El Dorado International Airport |  | CO | 1502 |
| 13 | Frankfurt am Main International Airport |  | DE | 1485 |
| 14 | Chicago O'Hare International Airport |  | US | 1482 |
| 15 | Salt Lake City International Airport |  | US | 1475 |
| 16 | Macau International Airport |  | MO | 1381 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1377 |
| 18 | Congonhas Airport |  | BR | 1355 |
| 19 | Madrid Barajas International Airport |  | ES | 1293 |
| 20 | Capua Airport |  | IT | 1281 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1251 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1158 |
| 24 | Charlotte/Douglas International Airport |  | US | 1153 |
| 25 | Kuala Lumpur International Airport |  | MY | 1119 |
| 26 | Charles de Gaulle International Airport |  | FR | 1115 |
| 27 | Malpensa International Airport |  | IT | 1082 |
| 28 | Bengaluru International Airport |  | IN | 1070 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1007 |
| 30 | Ninoy Aquino International Airport |  | PH | 1007 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 32 | Barcelona International Airport |  | ES | 967 |
| 33 | Daniel K Inouye International Airport |  | US | 959 |
| 34 | Seattle-Tacoma International Airport |  | US | 951 |
| 35 | Calgary International Airport |  | CA | 936 |
| 36 | Viracopos International Airport |  | BR | 929 |
| 37 | Scottsdale Airport |  | US | 917 |
| 38 | Tenerife Norte Airport |  | ES | 913 |
| 39 | Oslo Gardermoen Airport |  | NO | 912 |
| 40 | Reno/Tahoe International Airport |  | US | 902 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 597 | 21m | 244 km | 2,513.8 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 390 | 24m | 225 km | 1,513.0 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 302 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 243 | 22m | 55 km | 231.0 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 224 | 1h 47m | 1,423 km | 5,497.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 208 | 20m | 250 km | 898.4 t |
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
| AZG246 | AZG | Ras Tanura Airport (OERT) | Macau International Airport (VMMC) | 2026-07-31 19:25 UTC | 2026-08-01 03:31 UTC | 8h 6m |
| A7GQE |  | Al Khawr Airport (OTBK) | Persian Gulf International Airport (OIBP) | 2026-08-01 02:49 UTC | 2026-08-01 03:26 UTC | 37m |
| CPA512 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Iki Airport (RJDB) | 2026-08-01 00:39 UTC | 2026-08-01 03:18 UTC | 2h 38m |
| KAL791 | Korean Air | Incheon International Airport (RKSI) | Iki Airport (RJDB) | 2026-08-01 02:17 UTC | 2026-08-01 03:06 UTC | 49m |
| JJA1471 | JJA | Incheon International Airport (RKSI) | Iki Airport (RJDB) | 2026-08-01 02:20 UTC | 2026-08-01 03:02 UTC | 41m |
| WIS500 | WIS | Anoka County/Blaine (Janes Field) Airport (KANE) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-01 00:08 UTC | 2026-08-01 03:02 UTC | 2h 53m |
| ZKKPH | ZKK | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-08-01 02:46 UTC | 2026-08-01 03:01 UTC | 15m |
| ZKIDH | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-08-01 02:56 UTC | 2026-08-01 03:01 UTC | 4m |
| N408SD |  | Moffett Federal Airfield (KNUQ) | Moffett Federal Airfield (KNUQ) | 2026-08-01 02:00 UTC | 2026-08-01 02:59 UTC | 59m |
| N484BL |  | Johnston Regional Airport (KJNX) | Flying S Ranch Airport (0NC8) | 2026-08-01 01:47 UTC | 2026-08-01 02:54 UTC | 1h 6m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-01 02:18 UTC | 2026-08-01 02:50 UTC | 32m |
| JAL313 | Japan Airlines | Tokyo International Airport (RJTT) | Ashiya Airport (RJFA) | 2026-08-01 01:43 UTC | 2026-08-01 02:49 UTC | 1h 6m |
| CCA101 | Air China | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-08-01 00:14 UTC | 2026-08-01 02:48 UTC | 2h 34m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-01 02:41 UTC | 2026-08-01 02:48 UTC | 6m |
| QLK281 | QLK | Brisbane International Airport (YBBN) | Wellington International Airport (NZWN) | 2026-07-31 23:31 UTC | 2026-08-01 02:42 UTC | 3h 11m |
| N407LP |  | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-08-01 02:36 UTC | 2026-08-01 02:37 UTC | 0m |
| QLK40D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Fairview Airport (YFVW) | 2026-08-01 02:03 UTC | 2026-08-01 02:31 UTC | 28m |
| E82 |  | Tamworth Airport (YSTW) | Gunnedah Airport (YGDH) | 2026-08-01 01:53 UTC | 2026-08-01 02:29 UTC | 35m |
| VTARM | VTA | Indira Gandhi International Airport (VIDP) | Jaipur International Airport (VIJP) | 2026-08-01 02:05 UTC | 2026-08-01 02:27 UTC | 22m |
| LBQ792 | LBQ | Riveredge Airpark (19NK) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-08-01 02:07 UTC | 2026-08-01 02:25 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
