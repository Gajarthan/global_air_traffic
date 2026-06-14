# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_01:35:32_UTC-green)

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

**Latest saved flight:** 2026-06-14 01:35:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 01:35:32 UTC

- **109,633** saved flights
- **38,298** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,633** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,340,176.6 tonnes** estimated CO2 emissions
- **77,691,399 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4511 |
| 2 | SkyWest Airlines | 4109 |
| 3 | IndiGo | 2161 |
| 4 | EJA | 2107 |
| 5 | American Airlines | 1732 |
| 6 | Southwest Airlines | 1647 |
| 7 | ENY | 1362 |
| 8 | Delta Air Lines | 1294 |
| 9 | Lufthansa | 1239 |
| 10 | Vueling | 1005 |
| 11 | LATAM Airlines | 968 |
| 12 | WIF | 961 |
| 13 | AXM | 931 |
| 14 | AZU | 906 |
| 15 | LXJ | 828 |
| 16 | Swiss International | 794 |
| 17 | All Nippon Airways | 761 |
| 18 | Alaska Airlines | 747 |
| 19 | QLK | 723 |
| 20 | easyJet | 706 |
| 21 | EJU | 697 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 622 |
| 24 | VIV | 619 |
| 25 | Air France | 618 |
| 26 | United Airlines | 606 |
| 27 | MXY | 586 |
| 28 | CXK | 576 |
| 29 | AXB | 541 |
| 30 | Japan Airlines | 538 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92261 |
| 2 | 🇪🇸 ES | 7525 |
| 3 | 🇮🇳 IN | 6816 |
| 4 | 🇦🇺 AU | 6539 |
| 5 | 🇧🇷 BR | 6051 |
| 6 | 🇩🇪 DE | 5869 |
| 7 | 🇮🇹 IT | 5851 |
| 8 | 🇨🇦 CA | 5748 |
| 9 | 🇯🇵 JP | 4983 |
| 10 | 🇬🇧 GB | 4675 |
| 11 | 🇫🇷 FR | 4374 |
| 12 | 🇨🇴 CO | 3759 |
| 13 | 🇲🇽 MX | 3267 |
| 14 | 🇬🇷 GR | 3119 |
| 15 | 🇳🇴 NO | 3025 |
| 16 | 🇨🇭 CH | 2810 |
| 17 | 🇲🇾 MY | 2392 |
| 18 | 🇹🇷 TR | 2149 |
| 19 | 🇿🇦 ZA | 1871 |
| 20 | 🇰🇷 KR | 1834 |
| 21 | 🇹🇭 TH | 1811 |
| 22 | 🇵🇱 PL | 1801 |
| 23 | 🇳🇿 NZ | 1801 |
| 24 | 🇵🇭 PH | 1604 |
| 25 | 🇬🇹 GT | 1570 |
| 26 | 🇲🇦 MA | 1204 |
| 27 | 🇲🇴 MO | 1148 |
| 28 | 🇳🇱 NL | 1074 |
| 29 | 🇲🇪 ME | 1062 |
| 30 | 🇭🇷 HR | 955 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2353 |
| 2 | Denver International Airport |  | US | 1860 |
| 3 | Tokyo International Airport |  | JP | 1651 |
| 4 | Indira Gandhi International Airport |  | IN | 1481 |
| 5 | Guaymaral Airport |  | CO | 1393 |
| 6 | Harry Reid International Airport |  | US | 1388 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1369 |
| 8 | Zurich Airport |  | CH | 1239 |
| 9 | Frankfurt am Main International Airport |  | DE | 1223 |
| 10 | La Aurora Airport |  | GT | 1208 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1171 |
| 12 | Macau International Airport |  | MO | 1148 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1098 |
| 15 | Chicago O'Hare International Airport |  | US | 1088 |
| 16 | Madrid Barajas International Airport |  | ES | 956 |
| 17 | Capua Airport |  | IT | 938 |
| 18 | Kuala Lumpur International Airport |  | MY | 937 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 930 |
| 20 | Salt Lake City International Airport |  | US | 927 |
| 21 | Charlotte/Douglas International Airport |  | US | 845 |
| 22 | Congonhas Airport |  | BR | 838 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 830 |
| 24 | Charles de Gaulle International Airport |  | FR | 825 |
| 25 | Bengaluru International Airport |  | IN | 825 |
| 26 | Malpensa International Airport |  | IT | 801 |
| 27 | Ninoy Aquino International Airport |  | PH | 738 |
| 28 | Daniel K Inouye International Airport |  | US | 733 |
| 29 | General Edward Lawrence Logan International Airport |  | US | 729 |
| 30 | Tenerife Norte Airport |  | ES | 728 |
| 31 | Barcelona International Airport |  | ES | 720 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 713 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 702 |
| 34 | Amsterdam Airport Schiphol |  | NL | 664 |
| 35 | Don Mueang International Airport |  | TH | 659 |
| 36 | Vitoria/Foronda Airport |  | ES | 649 |
| 37 | Calgary International Airport |  | CA | 647 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 629 |
| 39 | Seattle-Tacoma International Airport |  | US | 629 |
| 40 | Viracopos International Airport |  | BR | 620 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 577 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 401 | 21m | 244 km | 1,688.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 293 | 24m | 225 km | 1,136.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 284 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 268 | 1h 25m | 910 km | 4,205.5 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 258 | 1h 10m | 770 km | 3,427.3 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 218 | 26m | 275 km | 1,033.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 163 | 20m | 99 km | 279.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 152 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 143 | 18m | 144 km | 355.7 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 25 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 133 | 44m | 241 km | 552.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 131 | 1h 39m | 1,156 km | 2,613.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 130 | 1h 43m | 1,423 km | 3,190.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 123 | 12m | - | - |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 122 | 1h 2m | 611 km | 1,286.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N801JA |  | Pru Field (K33S) | Pru Field (K33S) | 2026-06-14 01:25 UTC | 2026-06-14 01:35 UTC | 10m |
| CGGZZ | CGG | Sechelt-Gibsons Airport (CAP3) | Vancouver International Airport (CYVR) | 2026-06-14 01:17 UTC | 2026-06-14 01:31 UTC | 13m |
| NVP | NVP | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-06-14 01:13 UTC | 2026-06-14 01:29 UTC | 15m |
| N320KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-06-14 00:52 UTC | 2026-06-14 01:18 UTC | 26m |
| ZEH | ZEH | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-14 00:37 UTC | 2026-06-14 01:15 UTC | 37m |
| KGJ | KGJ | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-06-14 00:27 UTC | 2026-06-14 01:11 UTC | 44m |
| ASTR209 | AST | Redcliffe Airport (YRED) | Brisbane Archerfield Airport (YBAF) | 2026-06-14 00:52 UTC | 2026-06-14 01:09 UTC | 16m |
| N208W |  | Merrill Field (PAMR) | Kenai Municipal Airport (PAEN) | 2026-06-14 00:42 UTC | 2026-06-14 01:06 UTC | 24m |
| ZFW | ZFW | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-06-14 00:31 UTC | 2026-06-14 01:03 UTC | 31m |
| BHA100D | BHA | Tribhuvan International Airport (VNKT) | Langtang Airport (VNLT) | 2026-06-14 00:45 UTC | 2026-06-14 00:55 UTC | 10m |
| AM398 |  | Swan Hill Airport (YSWH) | Prairie Airport (YPRA) | 2026-06-14 00:39 UTC | 2026-06-14 00:53 UTC | 13m |
| N331FZ |  | KU77 (KU77) | K36U (K36U) | 2026-06-14 00:42 UTC | 2026-06-14 00:48 UTC | 6m |
| AXM5301 | AXM | Kota Kinabalu International Airport (WBKK) | Singapore Changi International Airport (WSSS) | 2026-06-13 22:59 UTC | 2026-06-14 00:48 UTC | 1h 49m |
| DAL85 | Delta Air Lines | Charles de Gaulle International Airport (LFPG) | Hartsfield/Jackson Atlanta International Airport (KATL) | 2026-06-13 15:54 UTC | 2026-06-14 00:48 UTC | 8h 53m |
| CGKLD | CGK | Billy Bishop Toronto City Airport (CYTZ) | Billy Bishop Toronto City Airport (CYTZ) | 2026-06-14 00:09 UTC | 2026-06-14 00:47 UTC | 37m |
| TIV723 | TIV | Vancouver International Airport (CYVR) | Boeing Field/King County International Airport (KBFI) | 2026-06-14 00:19 UTC | 2026-06-14 00:46 UTC | 27m |
| JBU2468 | JetBlue | Charleston Afb/International Airport (KCHS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-13 22:54 UTC | 2026-06-14 00:46 UTC | 1h 51m |
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-06-14 00:26 UTC | 2026-06-14 00:42 UTC | 16m |
| QUE10 | QUE | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Grandes-Bergeronnes Airport (CTH3) | 2026-06-14 00:10 UTC | 2026-06-14 00:42 UTC | 32m |
| AIQ3370 | AIQ | Don Mueang International Airport (VTBD) | Surin Airport (VTUJ) | 2026-06-14 00:05 UTC | 2026-06-14 00:41 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
