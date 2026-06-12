# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_23:51:05_UTC-green)

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

**Latest saved flight:** 2026-06-11 23:51:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-11 23:51:05 UTC

- **108,535** saved flights
- **37,995** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **108,535** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,327,338.4 tonnes** estimated CO2 emissions
- **76,947,154 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4468 |
| 2 | SkyWest Airlines | 4067 |
| 3 | IndiGo | 2149 |
| 4 | EJA | 2090 |
| 5 | American Airlines | 1723 |
| 6 | Southwest Airlines | 1630 |
| 7 | ENY | 1355 |
| 8 | Delta Air Lines | 1287 |
| 9 | Lufthansa | 1234 |
| 10 | Vueling | 992 |
| 11 | LATAM Airlines | 962 |
| 12 | WIF | 953 |
| 13 | AXM | 917 |
| 14 | AZU | 891 |
| 15 | LXJ | 821 |
| 16 | Swiss International | 788 |
| 17 | All Nippon Airways | 751 |
| 18 | Alaska Airlines | 741 |
| 19 | QLK | 719 |
| 20 | easyJet | 700 |
| 21 | EJU | 691 |
| 22 | Cathay Pacific | 654 |
| 23 | VIV | 618 |
| 24 | AEE | 617 |
| 25 | Air France | 613 |
| 26 | United Airlines | 597 |
| 27 | MXY | 584 |
| 28 | CXK | 572 |
| 29 | Japan Airlines | 535 |
| 30 | AXB | 532 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 91384 |
| 2 | 🇪🇸 ES | 7442 |
| 3 | 🇮🇳 IN | 6769 |
| 4 | 🇦🇺 AU | 6488 |
| 5 | 🇧🇷 BR | 5988 |
| 6 | 🇩🇪 DE | 5829 |
| 7 | 🇮🇹 IT | 5806 |
| 8 | 🇨🇦 CA | 5700 |
| 9 | 🇯🇵 JP | 4932 |
| 10 | 🇬🇧 GB | 4604 |
| 11 | 🇫🇷 FR | 4323 |
| 12 | 🇨🇴 CO | 3740 |
| 13 | 🇲🇽 MX | 3245 |
| 14 | 🇬🇷 GR | 3075 |
| 15 | 🇳🇴 NO | 3001 |
| 16 | 🇨🇭 CH | 2763 |
| 17 | 🇲🇾 MY | 2353 |
| 18 | 🇹🇷 TR | 2106 |
| 19 | 🇿🇦 ZA | 1849 |
| 20 | 🇰🇷 KR | 1809 |
| 21 | 🇳🇿 NZ | 1794 |
| 22 | 🇹🇭 TH | 1780 |
| 23 | 🇵🇱 PL | 1771 |
| 24 | 🇵🇭 PH | 1592 |
| 25 | 🇬🇹 GT | 1557 |
| 26 | 🇲🇦 MA | 1194 |
| 27 | 🇲🇴 MO | 1142 |
| 28 | 🇳🇱 NL | 1072 |
| 29 | 🇲🇪 ME | 1047 |
| 30 | 🇭🇷 HR | 949 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2340 |
| 2 | Denver International Airport |  | US | 1833 |
| 3 | Tokyo International Airport |  | JP | 1633 |
| 4 | Indira Gandhi International Airport |  | IN | 1473 |
| 5 | Harry Reid International Airport |  | US | 1380 |
| 6 | Guaymaral Airport |  | CO | 1379 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1354 |
| 8 | Zurich Airport |  | CH | 1229 |
| 9 | Frankfurt am Main International Airport |  | DE | 1217 |
| 10 | La Aurora Airport |  | GT | 1199 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1165 |
| 12 | Macau International Airport |  | MO | 1142 |
| 13 | El Dorado International Airport |  | CO | 1132 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1091 |
| 15 | Chicago O'Hare International Airport |  | US | 1077 |
| 16 | Madrid Barajas International Airport |  | ES | 941 |
| 17 | Capua Airport |  | IT | 934 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 923 |
| 19 | Kuala Lumpur International Airport |  | MY | 922 |
| 20 | Salt Lake City International Airport |  | US | 919 |
| 21 | Charlotte/Douglas International Airport |  | US | 841 |
| 22 | Congonhas Airport |  | BR | 827 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 826 |
| 24 | Charles de Gaulle International Airport |  | FR | 819 |
| 25 | Bengaluru International Airport |  | IN | 817 |
| 26 | Malpensa International Airport |  | IT | 800 |
| 27 | Ninoy Aquino International Airport |  | PH | 731 |
| 28 | Daniel K Inouye International Airport |  | US | 729 |
| 29 | Tenerife Norte Airport |  | ES | 726 |
| 30 | General Edward Lawrence Logan International Airport |  | US | 712 |
| 31 | Barcelona International Airport |  | ES | 712 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 706 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 699 |
| 34 | Amsterdam Airport Schiphol |  | NL | 662 |
| 35 | Don Mueang International Airport |  | TH | 651 |
| 36 | Vitoria/Foronda Airport |  | ES | 647 |
| 37 | Calgary International Airport |  | CA | 641 |
| 38 | Seattle-Tacoma International Airport |  | US | 624 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 622 |
| 40 | Viracopos International Airport |  | BR | 614 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 571 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 397 | 21m | 244 km | 1,671.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 291 | 24m | 225 km | 1,128.9 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 282 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 263 | 1h 25m | 910 km | 4,127.1 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 250 | 1h 10m | 770 km | 3,321.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 221 | 19m | 165 km | 628.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 217 | 26m | 275 km | 1,028.3 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 208 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 162 | 20m | 99 km | 277.5 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 159 | 22m | 55 km | 151.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 158 | 27m | 215 km | 585.2 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 152 | 14m | 154 km | 402.7 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 150 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 150 | 27m | 152 km | 392.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 147 | 31m | 369 km | 935.7 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 145 | 44m | 452 km | 1,130.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 140 | 18m | 144 km | 348.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 132 | 1h 1m | 695 km | 1,582.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 26 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 130 | 44m | 241 km | 540.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 128 | 1h 43m | 1,423 km | 3,141.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 123 | 1h 17m | 961 km | 2,038.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 121 | 1h 2m | 611 km | 1,276.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-06-11 23:07 UTC | 2026-06-11 23:51 UTC | 43m |
| N481AE |  | Hunter Army Air Field (KSVN) | Hunter Army Air Field (KSVN) | 2026-06-11 23:29 UTC | 2026-06-11 23:49 UTC | 20m |
| NJL | NJL | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-06-11 23:29 UTC | 2026-06-11 23:46 UTC | 16m |
| MNB478 | MNB | Ordu–Giresun Airport (LTCB) | Macau International Airport (VMMC) | 2026-06-11 12:17 UTC | 2026-06-11 23:43 UTC | 11h 25m |
| N472AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-06-11 22:30 UTC | 2026-06-11 23:39 UTC | 1h 9m |
| N54102 |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-06-11 23:11 UTC | 2026-06-11 23:37 UTC | 25m |
| N1JD |  | Jacksonville Executive At Craig Airport (KCRG) | St Simons Island Airport (KSSI) | 2026-06-11 22:53 UTC | 2026-06-11 23:36 UTC | 42m |
| ATN3398 | ATN | Cincinnati/Northern Kentucky International Airport (KCVG) | Phoenix Sky Harbor International Airport (KPHX) | 2026-06-11 19:50 UTC | 2026-06-11 23:36 UTC | 3h 45m |
| YEL5 | YEL | Portland International Airport (KPDX) | Scottsdale Airport (KSDL) | 2026-06-11 21:25 UTC | 2026-06-11 23:36 UTC | 2h 11m |
| N921AZ |  | Negrito Airstrip (0NM7) | Phoenix Sky Harbor International Airport (KPHX) | 2026-06-11 23:05 UTC | 2026-06-11 23:35 UTC | 30m |
| N562LD |  | Sacramento Executive Airport (KSAC) | Meadows Field (KBFL) | 2026-06-11 22:52 UTC | 2026-06-11 23:35 UTC | 42m |
| UAL1173 | United Airlines | Luis Munoz Marin International Airport (TJSJ) | Newark Liberty International Airport (KEWR) | 2026-06-11 20:06 UTC | 2026-06-11 23:32 UTC | 3h 25m |
| LXJ342 | LXJ | Nashville International Airport (KBNA) | Van Nuys Airport (KVNY) | 2026-06-11 19:16 UTC | 2026-06-11 23:29 UTC | 4h 13m |
| HAWK299 | HAW | Kingsville Nas Airport (KNQI) | Triple B Ranch Airport (42XS) | 2026-06-11 23:05 UTC | 2026-06-11 23:28 UTC | 23m |
| ZKSXL | ZKS | NZTS (NZTS) | NZTS (NZTS) | 2026-06-11 22:40 UTC | 2026-06-11 23:28 UTC | 47m |
| N576DT |  | Princeton Airport (K39N) | Lakewood Airport (KN12) | 2026-06-11 23:14 UTC | 2026-06-11 23:26 UTC | 12m |
| TKR160 | TKR | Albuquerque International Sunport Airport (KABQ) | 83NM (83NM) | 2026-06-11 23:14 UTC | 2026-06-11 23:25 UTC | 10m |
| N72DM |  | John Wayne/Orange County Airport (KSNA) | John Wayne/Orange County Airport (KSNA) | 2026-06-11 23:12 UTC | 2026-06-11 23:21 UTC | 8m |
| TWY281 | TWY | Camarillo Airport (KCMA) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-06-11 22:30 UTC | 2026-06-11 23:19 UTC | 49m |
| THNDR08 | THN | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-06-11 23:16 UTC | 2026-06-11 23:17 UTC | 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
