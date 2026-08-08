# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_15:25:30_UTC-green)

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

**Latest saved flight:** 2026-08-08 15:25:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 15:25:30 UTC

- **178,518** saved flights
- **57,337** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,518** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,145,393.1 tonnes** estimated CO2 emissions
- **124,370,617 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7086 |
| 2 | SkyWest Airlines | 6500 |
| 3 | EJA | 3510 |
| 4 | IndiGo | 3139 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2774 |
| 7 | ENY | 2216 |
| 8 | Delta Air Lines | 2105 |
| 9 | LATAM Airlines | 1657 |
| 10 | Lufthansa | 1597 |
| 11 | AZU | 1593 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1474 |
| 14 | LXJ | 1398 |
| 15 | Swiss International | 1221 |
| 16 | easyJet | 1212 |
| 17 | AXM | 1210 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1088 |
| 20 | EJU | 1086 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 981 |
| 23 | Cathay Pacific | 946 |
| 24 | GLO | 946 |
| 25 | CXK | 943 |
| 26 | AEE | 929 |
| 27 | Air France | 920 |
| 28 | United Airlines | 919 |
| 29 | MXY | 897 |
| 30 | PGT | 883 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152984 |
| 2 | 🇪🇸 ES | 11445 |
| 3 | 🇧🇷 BR | 10207 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9841 |
| 6 | 🇨🇦 CA | 9747 |
| 7 | 🇮🇹 IT | 9238 |
| 8 | 🇩🇪 DE | 8850 |
| 9 | 🇬🇧 GB | 8255 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7113 |
| 12 | 🇨🇴 CO | 6564 |
| 13 | 🇬🇷 GR | 5211 |
| 14 | 🇲🇽 MX | 5105 |
| 15 | 🇨🇭 CH | 4767 |
| 16 | 🇳🇴 NO | 4637 |
| 17 | 🇹🇷 TR | 4498 |
| 18 | 🇲🇾 MY | 3159 |
| 19 | 🇵🇱 PL | 2976 |
| 20 | 🇿🇦 ZA | 2916 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2281 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1806 |
| 27 | 🇭🇷 HR | 1770 |
| 28 | 🇲🇪 ME | 1627 |
| 29 | 🇳🇱 NL | 1608 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3677 |
| 2 | Denver International Airport |  | US | 2949 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Indira Gandhi International Airport |  | IN | 2189 |
| 5 | Guaymaral Airport |  | CO | 2182 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1928 |
| 8 | Zurich Airport |  | CH | 1900 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1856 |
| 10 | La Aurora Airport |  | GT | 1752 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1601 |
| 13 | Salt Lake City International Airport |  | US | 1592 |
| 14 | El Dorado International Airport |  | CO | 1589 |
| 15 | Frankfurt am Main International Airport |  | DE | 1561 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1481 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1431 |
| 19 | Capua Airport |  | IT | 1398 |
| 20 | Madrid Barajas International Airport |  | ES | 1395 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1324 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1265 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1226 |
| 25 | Charlotte/Douglas International Airport |  | US | 1215 |
| 26 | Charles de Gaulle International Airport |  | FR | 1212 |
| 27 | Kuala Lumpur International Airport |  | MY | 1190 |
| 28 | Bengaluru International Airport |  | IN | 1174 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1105 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1061 |
| 33 | Daniel K Inouye International Airport |  | US | 1026 |
| 34 | Viracopos International Airport |  | BR | 1025 |
| 35 | Seattle-Tacoma International Airport |  | US | 1025 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 993 |
| 39 | Tenerife Norte Airport |  | ES | 975 |
| 40 | Amsterdam Airport Schiphol |  | NL | 966 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 901 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 656 | 21m | 244 km | 2,762.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 415 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 299 | 27m | 275 km | 1,416.8 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 249 | 1h 48m | 1,423 km | 6,110.9 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 17 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 229 | 8m | - | - |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 214 | 1h 15m | 961 km | 3,547.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 204 | 24m | 218 km | 768.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N996TA |  | Auburn Municipal Airport (KS50) | Auburn Municipal Airport (KS50) | 2026-08-08 15:01 UTC | 2026-08-08 15:25 UTC | 24m |
| N94505 |  | 54OK (54OK) | Eagle Creek Airport (51OK) | 2026-08-08 15:03 UTC | 2026-08-08 15:21 UTC | 18m |
| N595DD |  | Scottsdale Airport (KSDL) | Montezuma Airport (19AZ) | 2026-08-08 14:56 UTC | 2026-08-08 15:19 UTC | 22m |
| UZB3234 | UZB | Karlovy Vary International Airport (LKKV) | Bezymyanka Airfield (UWWG) | 2026-08-08 12:22 UTC | 2026-08-08 15:17 UTC | 2h 54m |
| CAP2682 | CAP | Millard Airport (KMLE) | Scribner State Airport (KSCB) | 2026-08-08 14:42 UTC | 2026-08-08 15:11 UTC | 29m |
| N61622 |  | Blue Grass Airport (KLEX) | Lebanon Springfield/George Hoerter Field (K6I2) | 2026-08-08 14:15 UTC | 2026-08-08 15:10 UTC | 54m |
| N665KA |  | Henderson Executive Airport (KHND) | Santa Barbara Municipal Airport (KSBA) | 2026-08-08 13:28 UTC | 2026-08-08 15:09 UTC | 1h 41m |
| N204EH |  | Zephyrhills Municipal Airport (KZPH) | Zephyrhills Municipal Airport (KZPH) | 2026-08-08 14:47 UTC | 2026-08-08 15:08 UTC | 21m |
| N4588L |  | Moore County Airport (KSOP) | Moore County Airport (KSOP) | 2026-08-08 14:56 UTC | 2026-08-08 15:08 UTC | 12m |
| JAS21 | JAS | Washington Dulles International Airport (KIAD) | KNHZ (KNHZ) | 2026-08-08 13:51 UTC | 2026-08-08 15:07 UTC | 1h 15m |
| LID641 | LID | LICL (LICL) | LICL (LICL) | 2026-08-08 14:54 UTC | 2026-08-08 15:06 UTC | 12m |
| N55066 |  | General Dick Stout Field (K1L8) | General Dick Stout Field (K1L8) | 2026-08-08 13:10 UTC | 2026-08-08 15:04 UTC | 1h 54m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 14:53 UTC | 2026-08-08 15:04 UTC | 11m |
| HB2420 |  | Ambri Airport (LSPM) | St Stephan Airport (LSTS) | 2026-08-08 13:58 UTC | 2026-08-08 15:02 UTC | 1h 3m |
| WMU2 | WMU | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-08-08 14:46 UTC | 2026-08-08 15:02 UTC | 16m |
| OKAPT | OKA | Otrokovice Zlin Airport (LKOT) | Kunovice Airport (LKKU) | 2026-08-08 14:41 UTC | 2026-08-08 15:00 UTC | 19m |
| N71F |  | Washington Manassas/Harry P Davis Field (KHEF) | Kurt's Field (27WV) | 2026-08-08 14:20 UTC | 2026-08-08 15:00 UTC | 39m |
| N17NA |  | Westfield-Barnes Regional Airport (KBAF) | Northampton Airport (K7B2) | 2026-08-08 14:45 UTC | 2026-08-08 14:59 UTC | 14m |
| N252BM |  | North Fork Valley Airport (K7V2) | North Fork Valley Airport (K7V2) | 2026-08-08 14:48 UTC | 2026-08-08 14:59 UTC | 10m |
| N7954N |  | Stillwater Regional Airport (KSWO) | Bartlesville Municipal Airport (KBVO) | 2026-08-08 14:21 UTC | 2026-08-08 14:51 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
