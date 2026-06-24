# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_08:22:04_UTC-green)

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

**Latest saved flight:** 2026-06-24 08:22:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-24 08:22:04 UTC

- **118,536** saved flights
- **40,879** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **118,536** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,436,748.6 tonnes** estimated CO2 emissions
- **83,289,773 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4887 |
| 2 | SkyWest Airlines | 4383 |
| 3 | EJA | 2292 |
| 4 | IndiGo | 2285 |
| 5 | American Airlines | 1846 |
| 6 | Southwest Airlines | 1769 |
| 7 | ENY | 1484 |
| 8 | Delta Air Lines | 1398 |
| 9 | Lufthansa | 1302 |
| 10 | Vueling | 1075 |
| 11 | LATAM Airlines | 1049 |
| 12 | WIF | 1048 |
| 13 | AZU | 990 |
| 14 | AXM | 972 |
| 15 | LXJ | 900 |
| 16 | Swiss International | 835 |
| 17 | All Nippon Airways | 812 |
| 18 | Alaska Airlines | 788 |
| 19 | QLK | 763 |
| 20 | easyJet | 762 |
| 21 | EJU | 744 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 662 |
| 24 | VIV | 652 |
| 25 | Air France | 649 |
| 26 | United Airlines | 649 |
| 27 | CXK | 636 |
| 28 | MXY | 623 |
| 29 | AXB | 586 |
| 30 | GLO | 582 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 100240 |
| 2 | 🇪🇸 ES | 8088 |
| 3 | 🇮🇳 IN | 7175 |
| 4 | 🇦🇺 AU | 7007 |
| 5 | 🇧🇷 BR | 6544 |
| 6 | 🇮🇹 IT | 6330 |
| 7 | 🇩🇪 DE | 6320 |
| 8 | 🇨🇦 CA | 6238 |
| 9 | 🇯🇵 JP | 5304 |
| 10 | 🇬🇧 GB | 5196 |
| 11 | 🇫🇷 FR | 4714 |
| 12 | 🇨🇴 CO | 4000 |
| 13 | 🇲🇽 MX | 3479 |
| 14 | 🇬🇷 GR | 3386 |
| 15 | 🇳🇴 NO | 3255 |
| 16 | 🇨🇭 CH | 3042 |
| 17 | 🇲🇾 MY | 2525 |
| 18 | 🇹🇷 TR | 2431 |
| 19 | 🇿🇦 ZA | 1995 |
| 20 | 🇵🇱 PL | 1946 |
| 21 | 🇳🇿 NZ | 1925 |
| 22 | 🇹🇭 TH | 1902 |
| 23 | 🇰🇷 KR | 1896 |
| 24 | 🇵🇭 PH | 1709 |
| 25 | 🇬🇹 GT | 1661 |
| 26 | 🇲🇦 MA | 1284 |
| 27 | 🇲🇪 ME | 1174 |
| 28 | 🇲🇴 MO | 1170 |
| 29 | 🇳🇱 NL | 1138 |
| 30 | 🇭🇷 HR | 1027 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2499 |
| 2 | Denver International Airport |  | US | 1989 |
| 3 | Tokyo International Airport |  | JP | 1757 |
| 4 | Indira Gandhi International Airport |  | IN | 1575 |
| 5 | Guaymaral Airport |  | CO | 1490 |
| 6 | Harry Reid International Airport |  | US | 1473 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1442 |
| 8 | Zurich Airport |  | CH | 1324 |
| 9 | La Aurora Airport |  | GT | 1283 |
| 10 | Frankfurt am Main International Airport |  | DE | 1263 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1258 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1177 |
| 13 | El Dorado International Airport |  | CO | 1171 |
| 14 | Macau International Airport |  | MO | 1170 |
| 15 | Chicago O'Hare International Airport |  | US | 1161 |
| 16 | Capua Airport |  | IT | 1024 |
| 17 | Salt Lake City International Airport |  | US | 1013 |
| 18 | Madrid Barajas International Airport |  | ES | 999 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 993 |
| 20 | Kuala Lumpur International Airport |  | MY | 976 |
| 21 | Congonhas Airport |  | BR | 911 |
| 22 | Charlotte/Douglas International Airport |  | US | 900 |
| 23 | General Edward Lawrence Logan International Airport |  | US | 893 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 882 |
| 25 | Bengaluru International Airport |  | IN | 871 |
| 26 | Charles de Gaulle International Airport |  | FR | 869 |
| 27 | Malpensa International Airport |  | IT | 834 |
| 28 | Ninoy Aquino International Airport |  | PH | 790 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 776 |
| 30 | Daniel K Inouye International Airport |  | US | 768 |
| 31 | Tenerife Norte Airport |  | ES | 760 |
| 32 | Barcelona International Airport |  | ES | 754 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 734 |
| 34 | Vitoria/Foronda Airport |  | ES | 695 |
| 35 | Calgary International Airport |  | CA | 694 |
| 36 | Amsterdam Airport Schiphol |  | NL | 691 |
| 37 | Don Mueang International Airport |  | TH | 688 |
| 38 | Seattle-Tacoma International Airport |  | US | 680 |
| 39 | Viracopos International Airport |  | BR | 673 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 672 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 619 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 430 | 21m | 244 km | 1,810.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 314 | 24m | 225 km | 1,218.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 304 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 289 | 1h 25m | 910 km | 4,535.1 t |
| 6 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 7 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 286 | 1h 10m | 770 km | 3,799.3 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 234 | 26m | 275 km | 1,108.8 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 234 | 19m | 165 km | 665.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 220 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 176 | 22m | 55 km | 167.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 170 | 26m | 215 km | 629.6 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 170 | 20m | 99 km | 291.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 161 | 44m | 241 km | 668.8 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 149 | 20m | 250 km | 643.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 148 | 1h 44m | 1,423 km | 3,632.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 148 | 18m | 144 km | 368.1 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 138 | 1h 39m | 1,156 km | 2,753.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 134 | 1h 17m | 961 km | 2,221.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFROH | DFR | Guidonia Airport (LIRG) | Ciampino Airport (LIRA) | 2026-06-24 07:16 UTC | 2026-06-24 08:22 UTC | 1h 5m |
| CJT570 | CJT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Montréal (Mirabel) Airport (CYMX) | 2026-06-24 06:05 UTC | 2026-06-24 08:16 UTC | 2h 11m |
| M28B |  | Celle Airport (ETHC) | Celle Airport (ETHC) | 2026-06-24 07:11 UTC | 2026-06-24 08:14 UTC | 1h 2m |
| EJU75NR | EJU | Lisbon Portela Airport (LPPT) | Zurich Airport (LSZH) | 2026-06-24 05:38 UTC | 2026-06-24 08:13 UTC | 2h 34m |
| ZAM18 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-24 07:36 UTC | 2026-06-24 08:04 UTC | 28m |
| HSOIC2 | HSO | Husum-Schwesing Airport (EDXJ) | Helgoland-Dune Airport (EDXH) | 2026-06-24 07:30 UTC | 2026-06-24 07:57 UTC | 26m |
| WIF1DK | WIF | Sogndal Airport (ENSG) | Sogndal Airport (ENSG) | 2026-06-24 07:38 UTC | 2026-06-24 07:54 UTC | 15m |
| HBZZZ | HBZ | Wangen-Lachen Airport (LSPV) | Wangen-Lachen Airport (LSPV) | 2026-06-24 07:25 UTC | 2026-06-24 07:46 UTC | 21m |
| HBZVH | HBZ | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-06-24 07:31 UTC | 2026-06-24 07:45 UTC | 14m |
| SERMT | SER | Linkoping SAAB Airport (ESSL) | Linkoping SAAB Airport (ESSL) | 2026-06-24 07:11 UTC | 2026-06-24 07:43 UTC | 31m |
| ABF5 | ABF | Lappeenranta Airport (EFLP) | Lappeenranta Airport (EFLP) | 2026-06-24 07:38 UTC | 2026-06-24 07:43 UTC | 4m |
| MAI336 | MAI | LRPV (LRPV) | LRPV (LRPV) | 2026-06-24 07:32 UTC | 2026-06-24 07:34 UTC | 2m |
| J999KT |  | Gading Wonosari Airport (WI1G) | Gading Wonosari Airport (WI1G) | 2026-06-24 07:29 UTC | 2026-06-24 07:33 UTC | 4m |
| ASA780 | Alaska Airlines | Dallas-Fort Worth International Airport (KDFW) | 2 X 4 Ranch Airport (NM47) | 2026-06-24 06:36 UTC | 2026-06-24 07:32 UTC | 55m |
| ZAM38 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-24 06:57 UTC | 2026-06-24 07:30 UTC | 32m |
| YOP | YOP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-24 06:52 UTC | 2026-06-24 07:29 UTC | 36m |
| AXM431 | AXM | Kuala Lumpur International Airport (WMKK) | Sultan Syarif Kasim Ii (Simpang Tiga) Airport (WIBB) | 2026-06-24 06:58 UTC | 2026-06-24 07:27 UTC | 28m |
| AXM6419 | AXM | Penang International Airport (WMKP) | Batu Pahat Airport (WMAB) | 2026-06-24 06:37 UTC | 2026-06-24 07:23 UTC | 45m |
| KLM27J | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Birmingham International Airport (EGBB) | 2026-06-24 06:37 UTC | 2026-06-24 07:23 UTC | 46m |
| VOZ1350 | Virgin Australia | Darwin International Airport (YPDN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-24 03:40 UTC | 2026-06-24 07:23 UTC | 3h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
