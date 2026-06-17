# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_06:30:16_UTC-green)

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

**Latest saved flight:** 2026-06-17 06:30:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-17 06:30:16 UTC

- **112,748** saved flights
- **39,221** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **112,748** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,375,541.7 tonnes** estimated CO2 emissions
- **79,741,546 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4638 |
| 2 | SkyWest Airlines | 4204 |
| 3 | IndiGo | 2191 |
| 4 | EJA | 2189 |
| 5 | American Airlines | 1782 |
| 6 | Southwest Airlines | 1682 |
| 7 | ENY | 1409 |
| 8 | Delta Air Lines | 1335 |
| 9 | Lufthansa | 1266 |
| 10 | Vueling | 1030 |
| 11 | LATAM Airlines | 994 |
| 12 | WIF | 993 |
| 13 | AXM | 943 |
| 14 | AZU | 937 |
| 15 | LXJ | 861 |
| 16 | Swiss International | 804 |
| 17 | All Nippon Airways | 783 |
| 18 | Alaska Airlines | 763 |
| 19 | QLK | 739 |
| 20 | easyJet | 726 |
| 21 | EJU | 713 |
| 22 | Cathay Pacific | 665 |
| 23 | AEE | 632 |
| 24 | Air France | 626 |
| 25 | United Airlines | 626 |
| 26 | VIV | 626 |
| 27 | MXY | 598 |
| 28 | CXK | 595 |
| 29 | GLO | 555 |
| 30 | AXB | 553 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 95079 |
| 2 | 🇪🇸 ES | 7713 |
| 3 | 🇮🇳 IN | 6912 |
| 4 | 🇦🇺 AU | 6710 |
| 5 | 🇧🇷 BR | 6237 |
| 6 | 🇮🇹 IT | 6045 |
| 7 | 🇩🇪 DE | 6017 |
| 8 | 🇨🇦 CA | 5927 |
| 9 | 🇯🇵 JP | 5096 |
| 10 | 🇬🇧 GB | 4853 |
| 11 | 🇫🇷 FR | 4486 |
| 12 | 🇨🇴 CO | 3812 |
| 13 | 🇲🇽 MX | 3331 |
| 14 | 🇬🇷 GR | 3199 |
| 15 | 🇳🇴 NO | 3107 |
| 16 | 🇨🇭 CH | 2879 |
| 17 | 🇲🇾 MY | 2438 |
| 18 | 🇹🇷 TR | 2258 |
| 19 | 🇿🇦 ZA | 1915 |
| 20 | 🇰🇷 KR | 1859 |
| 21 | 🇳🇿 NZ | 1856 |
| 22 | 🇹🇭 TH | 1840 |
| 23 | 🇵🇱 PL | 1838 |
| 24 | 🇵🇭 PH | 1643 |
| 25 | 🇬🇹 GT | 1610 |
| 26 | 🇲🇦 MA | 1236 |
| 27 | 🇲🇴 MO | 1161 |
| 28 | 🇲🇪 ME | 1103 |
| 29 | 🇳🇱 NL | 1092 |
| 30 | 🇭🇷 HR | 979 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2407 |
| 2 | Denver International Airport |  | US | 1909 |
| 3 | Tokyo International Airport |  | JP | 1690 |
| 4 | Indira Gandhi International Airport |  | IN | 1504 |
| 5 | Harry Reid International Airport |  | US | 1415 |
| 6 | Guaymaral Airport |  | CO | 1413 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1390 |
| 8 | Zurich Airport |  | CH | 1264 |
| 9 | La Aurora Airport |  | GT | 1240 |
| 10 | Frankfurt am Main International Airport |  | DE | 1235 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1213 |
| 12 | Macau International Airport |  | MO | 1161 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1132 |
| 15 | Chicago O'Hare International Airport |  | US | 1122 |
| 16 | Capua Airport |  | IT | 978 |
| 17 | Madrid Barajas International Airport |  | ES | 976 |
| 18 | Salt Lake City International Airport |  | US | 954 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 947 |
| 20 | Kuala Lumpur International Airport |  | MY | 945 |
| 21 | Charlotte/Douglas International Airport |  | US | 874 |
| 22 | Congonhas Airport |  | BR | 867 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 845 |
| 24 | Charles de Gaulle International Airport |  | FR | 838 |
| 25 | Bengaluru International Airport |  | IN | 837 |
| 26 | Malpensa International Airport |  | IT | 817 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 784 |
| 28 | Ninoy Aquino International Airport |  | PH | 758 |
| 29 | Daniel K Inouye International Airport |  | US | 745 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 740 |
| 31 | Tenerife Norte Airport |  | ES | 738 |
| 32 | Barcelona International Airport |  | ES | 732 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 713 |
| 34 | Amsterdam Airport Schiphol |  | NL | 672 |
| 35 | Don Mueang International Airport |  | TH | 670 |
| 36 | Vitoria/Foronda Airport |  | ES | 668 |
| 37 | Calgary International Airport |  | CA | 666 |
| 38 | Seattle-Tacoma International Airport |  | US | 651 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 648 |
| 40 | Viracopos International Airport |  | BR | 641 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 586 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 411 | 21m | 244 km | 1,730.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 301 | 24m | 225 km | 1,167.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 293 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 276 | 1h 25m | 910 km | 4,331.1 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 268 | 1h 10m | 770 km | 3,560.2 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 226 | 26m | 275 km | 1,070.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 164 | 22m | 55 km | 155.9 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 163 | 27m | 215 km | 603.7 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 154 | 27m | 152 km | 402.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 150 | 44m | 452 km | 1,169.0 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 143 | 44m | 241 km | 594.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 135 | 1h 1m | 695 km | 1,618.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 133 | 1h 43m | 1,423 km | 3,264.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 126 | 24m | 223 km | 484.7 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 126 | 1h 17m | 961 km | 2,088.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EWG6100 | EWG | Dusseldorf International Airport (EDDL) | Leipzig Halle Airport (EDDP) | 2026-06-17 05:45 UTC | 2026-06-17 06:30 UTC | 44m |
| N73262 |  | Banning Municipal Airport (KBNG) | Van Nuys Airport (KVNY) | 2026-06-17 05:05 UTC | 2026-06-17 06:11 UTC | 1h 5m |
|  |  | Akinci Air Base (LTAE) | Akinci Air Base (LTAE) | 2026-06-17 05:53 UTC | 2026-06-17 06:06 UTC | 12m |
| NSZ3194 | NSZ | Copenhagen Kastrup Airport (EKCH) | Stockholm-Arlanda Airport (ESSA) | 2026-06-17 05:07 UTC | 2026-06-17 06:02 UTC | 55m |
| TJT91SZ | TJT | Marseille Provence Airport (LFML) | Malpensa International Airport (LIMC) | 2026-06-17 04:52 UTC | 2026-06-17 06:01 UTC | 1h 8m |
| DLH6VV | Lufthansa | Frankfurt am Main International Airport (EDDF) | Hannover Airport (EDDV) | 2026-06-17 05:18 UTC | 2026-06-17 05:54 UTC | 35m |
| AE921 |  | Sydney Bankstown Airport (YSBK) | Bombala Airport (YBOM) | 2026-06-17 05:12 UTC | 2026-06-17 05:50 UTC | 38m |
| VOE63WX | VOE | Asturias Airport (LEAS) | Requena Airport (LERE) | 2026-06-17 04:48 UTC | 2026-06-17 05:47 UTC | 58m |
| RYR9858 | Ryanair | Malpensa International Airport (LIMC) | Dolna Banya Airport (LBDB) | 2026-06-17 04:11 UTC | 2026-06-17 05:46 UTC | 1h 35m |
| VAR667 | VAR | Montgomery-Gibbs Executive Airport (KMYF) | Phoenix Goodyear Airport (KGYR) | 2026-06-17 03:40 UTC | 2026-06-17 05:46 UTC | 2h 5m |
| DLH9TT | Lufthansa | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-06-17 04:55 UTC | 2026-06-17 05:46 UTC | 50m |
| RYR4PN | Ryanair | Trieste / Ronchi Dei Legionari (LIPQ) | Pantelleria Airport (LICG) | 2026-06-17 04:43 UTC | 2026-06-17 05:45 UTC | 1h 1m |
| QLK225D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-06-17 05:06 UTC | 2026-06-17 05:43 UTC | 37m |
| FIN3AW | Finnair | Helsinki Vantaa Airport (EFHK) | Berlin Brandenburg Airport (EDDB) | 2026-06-17 04:12 UTC | 2026-06-17 05:43 UTC | 1h 30m |
| N793US |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-06-17 04:16 UTC | 2026-06-17 05:39 UTC | 1h 22m |
| CXK174 | CXK | Pueblo Memorial Airport (KPUB) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-06-17 05:03 UTC | 2026-06-17 05:38 UTC | 34m |
| RYR3GD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Capua Airport (LIAU) | 2026-06-17 04:49 UTC | 2026-06-17 05:37 UTC | 48m |
| N353AM |  | Westchester County Airport (KHPN) | Westchester County Airport (KHPN) | 2026-06-17 05:34 UTC | 2026-06-17 05:37 UTC | 2m |
| AMU671 | AMU | Taichung Ching Chuang Kang Airport (RCMQ) | Macau International Airport (VMMC) | 2026-06-17 04:31 UTC | 2026-06-17 05:37 UTC | 1h 5m |
| AM315 |  | Melbourne Essendon Airport (YMEN) | Sale Airport (YSLT) | 2026-06-17 05:10 UTC | 2026-06-17 05:37 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
