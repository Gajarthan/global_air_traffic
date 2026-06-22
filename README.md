# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_05:06:05_UTC-green)

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

**Latest saved flight:** 2026-06-22 05:06:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-22 05:06:05 UTC

- **117,031** saved flights
- **40,459** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **117,031** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,421,568.2 tonnes** estimated CO2 emissions
- **82,409,751 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4832 |
| 2 | SkyWest Airlines | 4342 |
| 3 | EJA | 2269 |
| 4 | IndiGo | 2264 |
| 5 | American Airlines | 1825 |
| 6 | Southwest Airlines | 1747 |
| 7 | ENY | 1460 |
| 8 | Delta Air Lines | 1381 |
| 9 | Lufthansa | 1294 |
| 10 | Vueling | 1051 |
| 11 | LATAM Airlines | 1033 |
| 12 | WIF | 1032 |
| 13 | AZU | 973 |
| 14 | AXM | 963 |
| 15 | LXJ | 891 |
| 16 | Swiss International | 827 |
| 17 | All Nippon Airways | 805 |
| 18 | Alaska Airlines | 780 |
| 19 | QLK | 754 |
| 20 | easyJet | 749 |
| 21 | EJU | 732 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 658 |
| 24 | VIV | 647 |
| 25 | United Airlines | 644 |
| 26 | Air France | 643 |
| 27 | CXK | 626 |
| 28 | MXY | 620 |
| 29 | AXB | 579 |
| 30 | GLO | 574 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 98876 |
| 2 | 🇪🇸 ES | 7972 |
| 3 | 🇮🇳 IN | 7120 |
| 4 | 🇦🇺 AU | 6925 |
| 5 | 🇧🇷 BR | 6455 |
| 6 | 🇮🇹 IT | 6255 |
| 7 | 🇩🇪 DE | 6232 |
| 8 | 🇨🇦 CA | 6131 |
| 9 | 🇯🇵 JP | 5256 |
| 10 | 🇬🇧 GB | 5111 |
| 11 | 🇫🇷 FR | 4661 |
| 12 | 🇨🇴 CO | 3992 |
| 13 | 🇲🇽 MX | 3442 |
| 14 | 🇬🇷 GR | 3349 |
| 15 | 🇳🇴 NO | 3207 |
| 16 | 🇨🇭 CH | 3002 |
| 17 | 🇲🇾 MY | 2500 |
| 18 | 🇹🇷 TR | 2384 |
| 19 | 🇿🇦 ZA | 1974 |
| 20 | 🇵🇱 PL | 1922 |
| 21 | 🇳🇿 NZ | 1918 |
| 22 | 🇹🇭 TH | 1895 |
| 23 | 🇰🇷 KR | 1892 |
| 24 | 🇵🇭 PH | 1698 |
| 25 | 🇬🇹 GT | 1652 |
| 26 | 🇲🇦 MA | 1272 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1150 |
| 29 | 🇳🇱 NL | 1126 |
| 30 | 🇭🇷 HR | 1019 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2469 |
| 2 | Denver International Airport |  | US | 1970 |
| 3 | Tokyo International Airport |  | JP | 1742 |
| 4 | Indira Gandhi International Airport |  | IN | 1563 |
| 5 | Guaymaral Airport |  | CO | 1482 |
| 6 | Harry Reid International Airport |  | US | 1460 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1429 |
| 8 | Zurich Airport |  | CH | 1308 |
| 9 | La Aurora Airport |  | GT | 1275 |
| 10 | Frankfurt am Main International Airport |  | DE | 1260 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1244 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1162 |
| 15 | Chicago O'Hare International Airport |  | US | 1150 |
| 16 | Capua Airport |  | IT | 1016 |
| 17 | Salt Lake City International Airport |  | US | 1002 |
| 18 | Madrid Barajas International Airport |  | ES | 989 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 978 |
| 20 | Kuala Lumpur International Airport |  | MY | 965 |
| 21 | Congonhas Airport |  | BR | 899 |
| 22 | Charlotte/Douglas International Airport |  | US | 891 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 871 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 869 |
| 25 | Charles de Gaulle International Airport |  | FR | 861 |
| 26 | Bengaluru International Airport |  | IN | 861 |
| 27 | Malpensa International Airport |  | IT | 829 |
| 28 | Ninoy Aquino International Airport |  | PH | 784 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 764 |
| 30 | Daniel K Inouye International Airport |  | US | 761 |
| 31 | Tenerife Norte Airport |  | ES | 758 |
| 32 | Barcelona International Airport |  | ES | 742 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Don Mueang International Airport |  | TH | 686 |
| 35 | Calgary International Airport |  | CA | 686 |
| 36 | Vitoria/Foronda Airport |  | ES | 685 |
| 37 | Amsterdam Airport Schiphol |  | NL | 683 |
| 38 | Seattle-Tacoma International Airport |  | US | 673 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 670 |
| 40 | Viracopos International Airport |  | BR | 664 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 615 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 425 | 21m | 244 km | 1,789.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 313 | 24m | 225 km | 1,214.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 301 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 286 | 1h 25m | 910 km | 4,488.0 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 282 | 1h 10m | 770 km | 3,746.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 231 | 19m | 165 km | 657.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 217 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 168 | 26m | 215 km | 622.2 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 159 | 27m | 152 km | 415.5 t |
| 18 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 155 | 44m | 241 km | 643.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 148 | 20m | 250 km | 639.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 146 | 1h 44m | 1,423 km | 3,583.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 136 | 1h 39m | 1,156 km | 2,713.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 133 | 1h 17m | 961 km | 2,204.5 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKIMC | OKI | Mlada Boleslav Airport (LKMB) | Kolin Airport (LKKO) | 2026-06-22 04:53 UTC | 2026-06-22 05:06 UTC | 12m |
| GNS105 | GNS | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-22 04:46 UTC | 2026-06-22 05:03 UTC | 16m |
| VOZ524 | Virgin Australia | Gold Coast Airport (YBCG) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-22 03:49 UTC | 2026-06-22 04:55 UTC | 1h 5m |
| N95S |  | Las Cruces International Airport (KLRU) | NM71 (NM71) | 2026-06-22 02:21 UTC | 2026-06-22 04:49 UTC | 2h 28m |
| TRP4 | TRP | Ocean City Municipal Airport (KOXB) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-06-22 04:01 UTC | 2026-06-22 04:44 UTC | 43m |
| N887WP |  | Dallas-Fort Worth International Airport (KDFW) | Raleigh-Durham International Airport (KRDU) | 2026-06-22 02:18 UTC | 2026-06-22 04:34 UTC | 2h 16m |
| WIF7GT | WIF | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-06-22 04:18 UTC | 2026-06-22 04:33 UTC | 15m |
| VAR502 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-06-22 03:45 UTC | 2026-06-22 04:32 UTC | 46m |
| RYR64TK | Ryanair | Malaga Airport (LEMG) | Kenitra Airport (GMMY) | 2026-06-22 04:02 UTC | 2026-06-22 04:30 UTC | 28m |
| ZEH | ZEH | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-22 03:49 UTC | 2026-06-22 04:23 UTC | 33m |
| JTE504 | JTE | Brisbane International Airport (YBBN) | Bundarra Airport (YBUA) | 2026-06-22 01:41 UTC | 2026-06-22 04:22 UTC | 2h 40m |
| IGO5215 | IndiGo | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-06-22 02:30 UTC | 2026-06-22 04:19 UTC | 1h 49m |
| VOZ1117 | Virgin Australia | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-06-22 03:01 UTC | 2026-06-22 04:18 UTC | 1h 17m |
| QLK861D | QLK | Brisbane International Airport (YBBN) | Bunyan Airfield (YBUY) | 2026-06-22 02:28 UTC | 2026-06-22 04:18 UTC | 1h 49m |
| RYR8QW | Ryanair | Comiso Airport Vincenzo Magliocco (LICB) | Salerno / Pontecagnano Airport (LIRI) | 2026-06-22 03:47 UTC | 2026-06-22 04:16 UTC | 29m |
| IGO531P | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 2026-06-22 03:32 UTC | 2026-06-22 04:13 UTC | 40m |
| AEE3KN | AEE | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-06-22 03:48 UTC | 2026-06-22 04:13 UTC | 24m |
| JST293 | JST | Auckland International Airport (NZAA) | Omarama Glider Airport (NZOA) | 2026-06-22 02:59 UTC | 2026-06-22 04:11 UTC | 1h 12m |
| AM210 |  | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-06-22 03:26 UTC | 2026-06-22 04:11 UTC | 44m |
| AIZ801 | AIZ | Ben Gurion International Airport (LLBG) | Ein Yahav Airfield (LLEY) | 2026-06-22 03:49 UTC | 2026-06-22 04:10 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
