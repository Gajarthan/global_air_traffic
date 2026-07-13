# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_00:44:51_UTC-green)

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

**Latest saved flight:** 2026-07-13 00:44:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-13 00:44:51 UTC

- **139,569** saved flights
- **47,023** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **139,569** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,676,241.0 tonnes** estimated CO2 emissions
- **97,173,394 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5686 |
| 2 | SkyWest Airlines | 5119 |
| 3 | EJA | 2754 |
| 4 | IndiGo | 2560 |
| 5 | American Airlines | 2210 |
| 6 | Southwest Airlines | 2101 |
| 7 | ENY | 1743 |
| 8 | Delta Air Lines | 1655 |
| 9 | Lufthansa | 1423 |
| 10 | LATAM Airlines | 1283 |
| 11 | Vueling | 1206 |
| 12 | AZU | 1200 |
| 13 | WIF | 1200 |
| 14 | LXJ | 1072 |
| 15 | AXM | 1043 |
| 16 | Swiss International | 993 |
| 17 | easyJet | 907 |
| 18 | All Nippon Airways | 896 |
| 19 | Alaska Airlines | 878 |
| 20 | QLK | 870 |
| 21 | EJU | 861 |
| 22 | VIV | 769 |
| 23 | AEE | 751 |
| 24 | CXK | 749 |
| 25 | Air France | 748 |
| 26 | JetBlue | 734 |
| 27 | United Airlines | 731 |
| 28 | Cathay Pacific | 728 |
| 29 | MXY | 726 |
| 30 | GLO | 715 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 119986 |
| 2 | 🇪🇸 ES | 9164 |
| 3 | 🇮🇳 IN | 8018 |
| 4 | 🇦🇺 AU | 7958 |
| 5 | 🇧🇷 BR | 7880 |
| 6 | 🇨🇦 CA | 7328 |
| 7 | 🇮🇹 IT | 7292 |
| 8 | 🇩🇪 DE | 7280 |
| 9 | 🇬🇧 GB | 6335 |
| 10 | 🇯🇵 JP | 5857 |
| 11 | 🇫🇷 FR | 5559 |
| 12 | 🇨🇴 CO | 4414 |
| 13 | 🇲🇽 MX | 4052 |
| 14 | 🇬🇷 GR | 3979 |
| 15 | 🇳🇴 NO | 3754 |
| 16 | 🇨🇭 CH | 3620 |
| 17 | 🇹🇷 TR | 3277 |
| 18 | 🇲🇾 MY | 2709 |
| 19 | 🇵🇱 PL | 2336 |
| 20 | 🇿🇦 ZA | 2284 |
| 21 | 🇳🇿 NZ | 2136 |
| 22 | 🇹🇭 TH | 2105 |
| 23 | 🇰🇷 KR | 2007 |
| 24 | 🇵🇭 PH | 1891 |
| 25 | 🇬🇹 GT | 1848 |
| 26 | 🇲🇦 MA | 1465 |
| 27 | 🇲🇪 ME | 1386 |
| 28 | 🇳🇱 NL | 1309 |
| 29 | 🇭🇷 HR | 1262 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2886 |
| 2 | Denver International Airport |  | US | 2341 |
| 3 | Tokyo International Airport |  | JP | 1903 |
| 4 | Indira Gandhi International Airport |  | IN | 1772 |
| 5 | Harry Reid International Airport |  | US | 1743 |
| 6 | Guaymaral Airport |  | CO | 1701 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1611 |
| 8 | Zurich Airport |  | CH | 1553 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1466 |
| 10 | La Aurora Airport |  | GT | 1428 |
| 11 | Frankfurt am Main International Airport |  | DE | 1373 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1335 |
| 13 | Chicago O'Hare International Airport |  | US | 1313 |
| 14 | Salt Lake City International Airport |  | US | 1243 |
| 15 | El Dorado International Airport |  | CO | 1239 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1198 |
| 17 | Macau International Airport |  | MO | 1188 |
| 18 | Capua Airport |  | IT | 1147 |
| 19 | Madrid Barajas International Airport |  | ES | 1137 |
| 20 | Congonhas Airport |  | BR | 1122 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1120 |
| 22 | Kuala Lumpur International Airport |  | MY | 1051 |
| 23 | Charlotte/Douglas International Airport |  | US | 1022 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1003 |
| 25 | Charles de Gaulle International Airport |  | FR | 991 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 967 |
| 27 | Bengaluru International Airport |  | IN | 961 |
| 28 | Malpensa International Airport |  | IT | 906 |
| 29 | Ninoy Aquino International Airport |  | PH | 880 |
| 30 | Daniel K Inouye International Airport |  | US | 855 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 854 |
| 32 | Barcelona International Airport |  | ES | 851 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 820 |
| 34 | Tenerife Norte Airport |  | ES | 816 |
| 35 | Calgary International Airport |  | CA | 804 |
| 36 | Viracopos International Airport |  | BR | 797 |
| 37 | Seattle-Tacoma International Airport |  | US | 795 |
| 38 | Scottsdale Airport |  | US | 792 |
| 39 | Amsterdam Airport Schiphol |  | NL | 783 |
| 40 | Vitoria/Foronda Airport |  | ES | 776 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 717 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 505 | 21m | 244 km | 2,126.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 342 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 341 | 24m | 225 km | 1,322.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 190 | 26m | 215 km | 703.7 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 184 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 164 | 44m | 452 km | 1,278.1 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 161 | 1h 1m | 695 km | 1,929.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 157 | 1h 38m | 1,156 km | 3,132.1 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 154 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JZR1539 | JZR | John Paul II International Airport Kraków-Balice Airport (EPKK) | Simara Airport (VNSI) | 2026-07-12 12:46 UTC | 2026-07-13 00:44 UTC | 11h 58m |
| THY726 | Turkish Airlines | Istanbul Airport (LTFM) | Simara Airport (VNSI) | 2026-07-12 18:18 UTC | 2026-07-13 00:42 UTC | 6h 24m |
| RPA5665 | Republic Airways | Richmond International Airport (KRIC) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-12 23:30 UTC | 2026-07-13 00:41 UTC | 1h 10m |
| YHT | YHT | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-13 00:04 UTC | 2026-07-13 00:38 UTC | 34m |
| N989R |  | Canyon Airport (ID04) | Nephi Municipal Airport (KU14) | 2026-07-12 22:50 UTC | 2026-07-13 00:36 UTC | 1h 45m |
| N491SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-07-13 00:27 UTC | 2026-07-13 00:29 UTC | 1m |
| N24AS |  | Camarillo Airport (KCMA) | Lake Tahoe Airport (KTVL) | 2026-07-12 22:41 UTC | 2026-07-13 00:28 UTC | 1h 47m |
| AAL3090 | American Airlines | Portland International Airport (KPDX) | Philadelphia International Airport (KPHL) | 2026-07-12 19:39 UTC | 2026-07-13 00:24 UTC | 4h 45m |
| N818PR |  | San Carlos Airport (KSQL) | Sacramento Mather Airport (KMHR) | 2026-07-12 23:33 UTC | 2026-07-13 00:24 UTC | 50m |
| SVK | SVK | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-07-12 23:38 UTC | 2026-07-13 00:16 UTC | 38m |
| PE993 |  | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-07-12 23:26 UTC | 2026-07-13 00:15 UTC | 49m |
| LFA313 | LFA | Orlando Sanford International Airport (KSFB) | Leesburg International Airport (KLEE) | 2026-07-12 22:58 UTC | 2026-07-13 00:15 UTC | 1h 16m |
| SKW577P | SkyWest Airlines | Denver International Airport (KDEN) | Kimball Municipal/Robert E Arraj Field (KIBM) | 2026-07-12 23:51 UTC | 2026-07-13 00:11 UTC | 20m |
| CXK676 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-13 00:04 UTC | 2026-07-13 00:10 UTC | 6m |
| AAL2157 | American Airlines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Philadelphia International Airport (KPHL) | 2026-07-12 21:46 UTC | 2026-07-13 00:10 UTC | 2h 23m |
| N12JS |  | Harry Reid International Airport (KLAS) | Mc Neill Ranch Airport (6TE7) | 2026-07-12 22:01 UTC | 2026-07-13 00:10 UTC | 2h 8m |
| N493LG |  | CO54 (CO54) | Perry Park Airport (CO93) | 2026-07-13 00:01 UTC | 2026-07-13 00:10 UTC | 9m |
| CGBLQ | CGB | Peterborough Airport (CYPQ) | CME2 (CME2) | 2026-07-12 23:42 UTC | 2026-07-13 00:09 UTC | 26m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-12 23:27 UTC | 2026-07-13 00:08 UTC | 40m |
| N945FG |  | Trenton Mercer Airport (KTTN) | Trenton Mercer Airport (KTTN) | 2026-07-12 22:56 UTC | 2026-07-13 00:08 UTC | 1h 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
