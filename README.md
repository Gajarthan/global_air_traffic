# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_05:30:36_UTC-green)

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

**Latest saved flight:** 2026-08-08 05:30:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 05:30:36 UTC

- **177,421** saved flights
- **57,116** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,421** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,132,031.9 tonnes** estimated CO2 emissions
- **123,596,053 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7018 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3506 |
| 4 | IndiGo | 3108 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1645 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1581 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1459 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1207 |
| 16 | AXM | 1200 |
| 17 | easyJet | 1200 |
| 18 | QLK | 1088 |
| 19 | EJU | 1082 |
| 20 | Alaska Airlines | 1079 |
| 21 | All Nippon Airways | 1078 |
| 22 | VIV | 978 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 942 |
| 25 | GLO | 937 |
| 26 | AEE | 923 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 896 |
| 30 | JetBlue | 876 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152696 |
| 2 | 🇪🇸 ES | 11328 |
| 3 | 🇧🇷 BR | 10132 |
| 4 | 🇦🇺 AU | 10031 |
| 5 | 🇮🇳 IN | 9742 |
| 6 | 🇨🇦 CA | 9722 |
| 7 | 🇮🇹 IT | 9145 |
| 8 | 🇩🇪 DE | 8742 |
| 9 | 🇬🇧 GB | 8174 |
| 10 | 🇯🇵 JP | 7130 |
| 11 | 🇫🇷 FR | 7026 |
| 12 | 🇨🇴 CO | 6524 |
| 13 | 🇬🇷 GR | 5153 |
| 14 | 🇲🇽 MX | 5093 |
| 15 | 🇨🇭 CH | 4686 |
| 16 | 🇳🇴 NO | 4609 |
| 17 | 🇹🇷 TR | 4403 |
| 18 | 🇲🇾 MY | 3129 |
| 19 | 🇵🇱 PL | 2940 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2641 |
| 22 | 🇳🇿 NZ | 2577 |
| 23 | 🇵🇭 PH | 2338 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2213 |
| 26 | 🇲🇦 MA | 1791 |
| 27 | 🇭🇷 HR | 1742 |
| 28 | 🇲🇪 ME | 1608 |
| 29 | 🇳🇱 NL | 1591 |
| 30 | 🇲🇴 MO | 1508 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2948 |
| 3 | Tokyo International Airport |  | JP | 2223 |
| 4 | Guaymaral Airport |  | CO | 2177 |
| 5 | Indira Gandhi International Airport |  | IN | 2167 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1915 |
| 8 | Zurich Airport |  | CH | 1879 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1589 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1508 |
| 17 | Congonhas Airport |  | BR | 1470 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1384 |
| 20 | Madrid Barajas International Airport |  | ES | 1380 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1253 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1242 |
| 24 | Charlotte/Douglas International Airport |  | US | 1212 |
| 25 | Malpensa International Airport |  | IT | 1211 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1179 |
| 28 | Bengaluru International Airport |  | IN | 1159 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1102 |
| 30 | Ninoy Aquino International Airport |  | PH | 1100 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1052 |
| 33 | Seattle-Tacoma International Airport |  | US | 1025 |
| 34 | Daniel K Inouye International Airport |  | US | 1023 |
| 35 | Viracopos International Airport |  | BR | 1016 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 957 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 653 | 21m | 244 km | 2,749.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 415 | 24m | 225 km | 1,610.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 410 | 1h 8m | 770 km | 5,446.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 297 | 27m | 275 km | 1,407.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 245 | 1h 48m | 1,423 km | 6,012.7 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WWF287 | WWF | Portland International Airport (KPDX) | Cottonwood Creek Ranch Airport (OG50) | 2026-08-08 02:52 UTC | 2026-08-08 05:30 UTC | 2h 37m |
| MXY335B | MXY | Westchester County Airport (KHPN) | Savannah/Hilton Head International Airport (KSAV) | 2026-08-08 02:48 UTC | 2026-08-08 04:36 UTC | 1h 47m |
| AIC9TC | Air India | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-08-08 04:12 UTC | 2026-08-08 04:33 UTC | 21m |
| SWR1845 | Swiss International | Eleftherios Venizelos International Airport (LGAV) | Zurich Airport (LSZH) | 2026-08-08 02:00 UTC | 2026-08-08 04:29 UTC | 2h 29m |
| RYR99PN | Ryanair | Budapest Ferenc Liszt International Airport (LHBP) | Otocac Airport (LDRO) | 2026-08-08 03:50 UTC | 2026-08-08 04:28 UTC | 38m |
| JST836 | JST | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-08-08 03:09 UTC | 2026-08-08 04:24 UTC | 1h 14m |
| RYR824 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Capua Airport (LIAU) | 2026-08-08 03:44 UTC | 2026-08-08 04:24 UTC | 40m |
| ANA859 | All Nippon Airways | Tokyo International Airport (RJTT) | Chek Lap Kok International Airport (VHHH) | 2026-08-08 00:10 UTC | 2026-08-08 04:23 UTC | 4h 13m |
| FAG707 | FAG | La Aurora Airport (MGGT) | Santa Cruz del Quiche Airport (MGQC) | 2026-08-08 04:07 UTC | 2026-08-08 04:23 UTC | 16m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-08-08 02:27 UTC | 2026-08-08 04:22 UTC | 1h 55m |
| RYR4791 | Ryanair | Sofia Airport (LBSF) | Skiathos Island National Airport (LGSK) | 2026-08-08 03:43 UTC | 2026-08-08 04:21 UTC | 37m |
| MSR892 | EgyptAir | Houari Boumediene Airport (DAAG) | HE42 (HE42) | 2026-08-08 01:11 UTC | 2026-08-08 04:16 UTC | 3h 5m |
| CFSUG | CFS | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-08-08 03:45 UTC | 2026-08-08 04:16 UTC | 31m |
| FVS221 | FVS | Futaysi Airport (OMAF) | Khalfan Airport (OE56) | 2026-08-08 04:01 UTC | 2026-08-08 04:13 UTC | 11m |
| N700FJ |  | Wilkes-Barre/Scranton International Airport (KAVP) | General Edward Lawrence Logan International Airport (KBOS) | 2026-08-08 03:31 UTC | 2026-08-08 04:12 UTC | 40m |
| SWA3706 | Southwest Airlines | San Diego International Airport (KSAN) | Sids Airport (MA52) | 2026-08-07 23:05 UTC | 2026-08-08 04:12 UTC | 5h 7m |
| AZU2678 | AZU | Viracopos International Airport (SBKP) | Ouricuri Airport (SNOY) | 2026-08-08 02:04 UTC | 2026-08-08 04:11 UTC | 2h 6m |
| MXY833 | MXY | Ja Field (SC58) | Orlando International Airport (KMCO) | 2026-08-08 02:59 UTC | 2026-08-08 04:07 UTC | 1h 8m |
| HL1271 |  | RKTA (RKTA) | G 710 Airport (RK6D) | 2026-08-08 02:43 UTC | 2026-08-08 04:07 UTC | 1h 24m |
| QLK378D | QLK | Brisbane International Airport (YBBN) | Maryborough Airport (YMYB) | 2026-08-08 03:43 UTC | 2026-08-08 04:07 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
