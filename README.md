# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_07:30:53_UTC-green)

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

**Latest saved flight:** 2026-07-05 07:30:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 07:30:53 UTC

- **129,395** saved flights
- **44,018** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **129,395** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,563,036.2 tonnes** estimated CO2 emissions
- **90,610,794 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5261 |
| 2 | SkyWest Airlines | 4796 |
| 3 | EJA | 2529 |
| 4 | IndiGo | 2434 |
| 5 | American Airlines | 1997 |
| 6 | Southwest Airlines | 1948 |
| 7 | ENY | 1623 |
| 8 | Delta Air Lines | 1546 |
| 9 | Lufthansa | 1361 |
| 10 | LATAM Airlines | 1176 |
| 11 | Vueling | 1151 |
| 12 | WIF | 1133 |
| 13 | AZU | 1098 |
| 14 | AXM | 1008 |
| 15 | LXJ | 999 |
| 16 | Swiss International | 901 |
| 17 | All Nippon Airways | 860 |
| 18 | Alaska Airlines | 835 |
| 19 | easyJet | 828 |
| 20 | QLK | 816 |
| 21 | EJU | 801 |
| 22 | VIV | 715 |
| 23 | Cathay Pacific | 713 |
| 24 | AEE | 706 |
| 25 | Air France | 703 |
| 26 | CXK | 694 |
| 27 | United Airlines | 690 |
| 28 | MXY | 677 |
| 29 | JetBlue | 673 |
| 30 | GLO | 657 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110685 |
| 2 | 🇪🇸 ES | 8636 |
| 3 | 🇮🇳 IN | 7630 |
| 4 | 🇦🇺 AU | 7515 |
| 5 | 🇧🇷 BR | 7255 |
| 6 | 🇨🇦 CA | 6815 |
| 7 | 🇩🇪 DE | 6803 |
| 8 | 🇮🇹 IT | 6769 |
| 9 | 🇬🇧 GB | 5741 |
| 10 | 🇯🇵 JP | 5624 |
| 11 | 🇫🇷 FR | 5132 |
| 12 | 🇨🇴 CO | 4086 |
| 13 | 🇲🇽 MX | 3773 |
| 14 | 🇬🇷 GR | 3686 |
| 15 | 🇳🇴 NO | 3522 |
| 16 | 🇨🇭 CH | 3312 |
| 17 | 🇹🇷 TR | 2826 |
| 18 | 🇲🇾 MY | 2614 |
| 19 | 🇿🇦 ZA | 2147 |
| 20 | 🇵🇱 PL | 2124 |
| 21 | 🇳🇿 NZ | 2080 |
| 22 | 🇹🇭 TH | 2009 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1813 |
| 25 | 🇬🇹 GT | 1766 |
| 26 | 🇲🇦 MA | 1386 |
| 27 | 🇲🇪 ME | 1286 |
| 28 | 🇳🇱 NL | 1216 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1131 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2698 |
| 2 | Denver International Airport |  | US | 2201 |
| 3 | Tokyo International Airport |  | JP | 1851 |
| 4 | Indira Gandhi International Airport |  | IN | 1684 |
| 5 | Harry Reid International Airport |  | US | 1612 |
| 6 | Guaymaral Airport |  | CO | 1573 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1531 |
| 8 | Zurich Airport |  | CH | 1424 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1376 |
| 10 | La Aurora Airport |  | GT | 1366 |
| 11 | Frankfurt am Main International Airport |  | DE | 1317 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1259 |
| 13 | Chicago O'Hare International Airport |  | US | 1241 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1151 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1085 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Madrid Barajas International Airport |  | ES | 1063 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1062 |
| 21 | Congonhas Airport |  | BR | 1021 |
| 22 | Kuala Lumpur International Airport |  | MY | 1015 |
| 23 | Charlotte/Douglas International Airport |  | US | 969 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 950 |
| 25 | Charles de Gaulle International Airport |  | FR | 939 |
| 26 | Bengaluru International Airport |  | IN | 923 |
| 27 | Malpensa International Airport |  | IT | 878 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 874 |
| 29 | Ninoy Aquino International Airport |  | PH | 841 |
| 30 | Daniel K Inouye International Airport |  | US | 816 |
| 31 | Barcelona International Airport |  | ES | 805 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 790 |
| 33 | Tenerife Norte Airport |  | ES | 784 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 760 |
| 35 | Calgary International Airport |  | CA | 753 |
| 36 | Vitoria/Foronda Airport |  | ES | 749 |
| 37 | Seattle-Tacoma International Airport |  | US | 747 |
| 38 | Scottsdale Airport |  | US | 744 |
| 39 | Viracopos International Airport |  | BR | 739 |
| 40 | Amsterdam Airport Schiphol |  | NL | 733 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 659 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 469 | 21m | 244 km | 1,974.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 325 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 315 | 1h 10m | 770 km | 4,184.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 238 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 180 | 44m | 241 km | 747.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 173 | 27m | 152 km | 452.1 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 168 | 1h 45m | 1,423 km | 4,123.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 159 | 18m | 144 km | 395.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 153 | 1h 1m | 695 km | 1,834.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 148 | 54m | 136 km | 347.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JKY143 | JKY | Coventry Airport (EGBE) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-07-05 07:16 UTC | 2026-07-05 07:30 UTC | 14m |
| YR5752 |  | Transilvania Targu Mures International Airport (LRTM) | Transilvania Targu Mures International Airport (LRTM) | 2026-07-05 06:52 UTC | 2026-07-05 07:24 UTC | 32m |
| TCAHB | TCA | Istanbul Hezarfen Airfield (LTBW) | Istanbul Hezarfen Airfield (LTBW) | 2026-07-05 06:50 UTC | 2026-07-05 07:10 UTC | 19m |
| ETH644 | Ethiopian Airlines | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Zhuhai Airport (ZGSD) | 2026-07-04 05:00 UTC | 2026-07-05 07:07 UTC | 26h 7m |
| QLK6D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Tamworth Airport (YSTW) | 2026-07-05 06:17 UTC | 2026-07-05 06:59 UTC | 42m |
| YYYY0000 | YYY | Meiktila Air Base (VYML) | Heho Airport (VYHH) | 2026-07-05 06:37 UTC | 2026-07-05 06:50 UTC | 13m |
| RYR18PG | Ryanair | Karlsruhe Baden-Baden Airport (EDSB) | Saiss Airport (GMFF) | 2026-07-05 04:20 UTC | 2026-07-05 06:48 UTC | 2h 28m |
| HDB1 | HDB | Dubai International Airport (OMDB) | Dubai International Airport (OMDB) | 2026-07-05 06:11 UTC | 2026-07-05 06:40 UTC | 28m |
| CWA929 | CWA | Edmonton International Airport (CYEG) | High Prairie Airport (CZHP) | 2026-07-05 05:58 UTC | 2026-07-05 06:39 UTC | 40m |
| ANE30KP | ANE | Madrid Barajas International Airport (LEMD) | Federico Garcia Lorca Airport (LEGR) | 2026-07-05 06:02 UTC | 2026-07-05 06:38 UTC | 36m |
| ASA1112 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-07-05 06:16 UTC | 2026-07-05 06:36 UTC | 20m |
| N264MC |  | Valence-Chabeuil Airport (LFLU) | Moulins-Montbeugny Airport (LFHY) | 2026-07-05 05:43 UTC | 2026-07-05 06:34 UTC | 51m |
| RYR3VU | Ryanair | Sevilla Airport (LEZL) | Valencia Airport (LEVC) | 2026-07-05 05:41 UTC | 2026-07-05 06:34 UTC | 52m |
| ZSARN | ZSA | Rand Airport (FAGM) | Reitz Airport (FARZ) | 2026-07-05 05:51 UTC | 2026-07-05 06:33 UTC | 42m |
| VLG7KA | Vueling | Sevilla Airport (LEZL) | Vitoria/Foronda Airport (LEVT) | 2026-07-05 05:34 UTC | 2026-07-05 06:32 UTC | 57m |
| SWR273M | Swiss International | Geneva Cointrin International Airport (LSGG) | Faro Airport (LPFR) | 2026-07-05 04:17 UTC | 2026-07-05 06:32 UTC | 2h 14m |
| SWR47W | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-07-05 05:25 UTC | 2026-07-05 06:30 UTC | 1h 4m |
| TRA65T | TRA | Amsterdam Airport Schiphol (EHAM) | Dingolfing Airport (EDPD) | 2026-07-05 05:22 UTC | 2026-07-05 06:27 UTC | 1h 5m |
| VLG5QN | Vueling | Palma De Mallorca Airport (LEPA) | Bilbao Airport (LEBB) | 2026-07-05 05:35 UTC | 2026-07-05 06:26 UTC | 50m |
| VOZ1715 | Virgin Australia | Brisbane International Airport (YBBN) | Monduran Airport (YMUA) | 2026-07-05 05:50 UTC | 2026-07-05 06:25 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
