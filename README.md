# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_06:59:17_UTC-green)

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

**Latest saved flight:** 2026-07-21 06:59:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-21 06:59:17 UTC

- **143,126** saved flights
- **47,981** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **143,126** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,716,121.1 tonnes** estimated CO2 emissions
- **99,485,283 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5820 |
| 2 | SkyWest Airlines | 5236 |
| 3 | EJA | 2819 |
| 4 | IndiGo | 2605 |
| 5 | American Airlines | 2295 |
| 6 | Southwest Airlines | 2158 |
| 7 | ENY | 1777 |
| 8 | Delta Air Lines | 1696 |
| 9 | Lufthansa | 1438 |
| 10 | LATAM Airlines | 1319 |
| 11 | Vueling | 1231 |
| 12 | AZU | 1230 |
| 13 | WIF | 1222 |
| 14 | LXJ | 1099 |
| 15 | AXM | 1058 |
| 16 | Swiss International | 1016 |
| 17 | easyJet | 933 |
| 18 | All Nippon Airways | 918 |
| 19 | QLK | 905 |
| 20 | Alaska Airlines | 903 |
| 21 | EJU | 880 |
| 22 | VIV | 797 |
| 23 | CXK | 765 |
| 24 | AEE | 763 |
| 25 | JetBlue | 760 |
| 26 | Air France | 759 |
| 27 | MXY | 744 |
| 28 | United Airlines | 743 |
| 29 | Cathay Pacific | 737 |
| 30 | GLO | 731 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 123161 |
| 2 | 🇪🇸 ES | 9318 |
| 3 | 🇦🇺 AU | 8221 |
| 4 | 🇮🇳 IN | 8156 |
| 5 | 🇧🇷 BR | 8071 |
| 6 | 🇨🇦 CA | 7538 |
| 7 | 🇮🇹 IT | 7455 |
| 8 | 🇩🇪 DE | 7402 |
| 9 | 🇬🇧 GB | 6547 |
| 10 | 🇯🇵 JP | 6013 |
| 11 | 🇫🇷 FR | 5676 |
| 12 | 🇨🇴 CO | 4591 |
| 13 | 🇲🇽 MX | 4159 |
| 14 | 🇬🇷 GR | 4072 |
| 15 | 🇳🇴 NO | 3824 |
| 16 | 🇨🇭 CH | 3699 |
| 17 | 🇹🇷 TR | 3380 |
| 18 | 🇲🇾 MY | 2761 |
| 19 | 🇵🇱 PL | 2406 |
| 20 | 🇿🇦 ZA | 2332 |
| 21 | 🇳🇿 NZ | 2203 |
| 22 | 🇹🇭 TH | 2128 |
| 23 | 🇰🇷 KR | 2033 |
| 24 | 🇵🇭 PH | 1932 |
| 25 | 🇬🇹 GT | 1874 |
| 26 | 🇲🇦 MA | 1494 |
| 27 | 🇲🇪 ME | 1419 |
| 28 | 🇳🇱 NL | 1346 |
| 29 | 🇭🇷 HR | 1303 |
| 30 | 🇲🇴 MO | 1195 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2951 |
| 2 | Denver International Airport |  | US | 2400 |
| 3 | Tokyo International Airport |  | JP | 1936 |
| 4 | Indira Gandhi International Airport |  | IN | 1807 |
| 5 | Harry Reid International Airport |  | US | 1798 |
| 6 | Guaymaral Airport |  | CO | 1738 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1638 |
| 8 | Zurich Airport |  | CH | 1586 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1502 |
| 10 | La Aurora Airport |  | GT | 1450 |
| 11 | Frankfurt am Main International Airport |  | DE | 1387 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1354 |
| 13 | Chicago O'Hare International Airport |  | US | 1337 |
| 14 | Salt Lake City International Airport |  | US | 1282 |
| 15 | El Dorado International Airport |  | CO | 1267 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1257 |
| 17 | Macau International Airport |  | MO | 1195 |
| 18 | Capua Airport |  | IT | 1167 |
| 19 | Madrid Barajas International Airport |  | ES | 1148 |
| 20 | Congonhas Airport |  | BR | 1147 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1132 |
| 22 | Kuala Lumpur International Airport |  | MY | 1066 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1041 |
| 24 | Charlotte/Douglas International Airport |  | US | 1033 |
| 25 | Charles de Gaulle International Airport |  | FR | 1004 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1000 |
| 27 | Bengaluru International Airport |  | IN | 974 |
| 28 | Malpensa International Airport |  | IT | 922 |
| 29 | Ninoy Aquino International Airport |  | PH | 902 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 877 |
| 31 | Daniel K Inouye International Airport |  | US | 871 |
| 32 | Barcelona International Airport |  | ES | 871 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 851 |
| 34 | Tenerife Norte Airport |  | ES | 825 |
| 35 | Calgary International Airport |  | CA | 816 |
| 36 | Seattle-Tacoma International Airport |  | US | 814 |
| 37 | Viracopos International Airport |  | BR | 811 |
| 38 | Amsterdam Airport Schiphol |  | NL | 808 |
| 39 | Scottsdale Airport |  | US | 806 |
| 40 | Vitoria/Foronda Airport |  | ES | 786 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 732 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 521 | 21m | 244 km | 2,193.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 351 | 24m | 225 km | 1,361.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 346 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 339 | 1h 9m | 770 km | 4,503.4 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 212 | 22m | 55 km | 201.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 192 | 26m | 215 km | 711.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 192 | 1h 46m | 1,423 km | 4,712.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 179 | 28m | 152 km | 467.8 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 178 | 20m | 250 km | 768.9 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 168 | 44m | 452 km | 1,309.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 166 | 1h 16m | 961 km | 2,751.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 163 | 13m | - | - |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 159 | 14m | 154 km | 421.3 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MC41 |  | Sydney Bankstown Airport (YSBK) | Brisbane Archerfield Airport (YBAF) | 2026-07-21 05:42 UTC | 2026-07-21 06:59 UTC | 1h 16m |
| IXD | IXD | Nowra Airport (YSNW) | Sydney Bankstown Airport (YSBK) | 2026-07-21 06:19 UTC | 2026-07-21 06:52 UTC | 32m |
| VIPR01 | VIP | RAAF Base Pearce (YPEA) | Catholic Agricultural College Bindoon Airstrip (YBOO) | 2026-07-21 06:36 UTC | 2026-07-21 06:49 UTC | 12m |
| SUCCG | SUC | Port Said Airport (HEPS) | El Arish International Airport (HEAR) | 2026-07-21 06:11 UTC | 2026-07-21 06:43 UTC | 31m |
| YNR | YNR | Adelaide Parafield Airport (YPPF) | Adelaide Parafield Airport (YPPF) | 2026-07-21 05:55 UTC | 2026-07-21 06:32 UTC | 37m |
| EFC995T | EFC | Al Maktoum International Airport (OMDW) | OM11 (OM11) | 2026-07-21 05:52 UTC | 2026-07-21 06:29 UTC | 37m |
| EFC24E | EFC | Al Maktoum International Airport (OMDW) | Al Minhad Air Base (OMDM) | 2026-07-21 06:07 UTC | 2026-07-21 06:27 UTC | 20m |
| BHA553 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-07-21 06:20 UTC | 2026-07-21 06:27 UTC | 6m |
| EFC68H | EFC | Al Maktoum International Airport (OMDW) | Al Ain International Airport (OMAL) | 2026-07-21 06:05 UTC | 2026-07-21 06:26 UTC | 21m |
| BEL8NV | Brussels Airlines | Brussels Airport (EBBR) | Alicante International Airport (LEAL) | 2026-07-21 04:24 UTC | 2026-07-21 06:25 UTC | 2h 1m |
| ETH638 | Ethiopian Airlines | Singapore Changi International Airport (WSSS) | Changi Air Base (WSAC) | 2026-07-19 18:15 UTC | 2026-07-21 06:23 UTC | 36h 8m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-07-21 05:03 UTC | 2026-07-21 06:23 UTC | 1h 20m |
| EFC71M | EFC | Al Maktoum International Airport (OMDW) | Al Minhad Air Base (OMDM) | 2026-07-21 05:50 UTC | 2026-07-21 06:21 UTC | 30m |
| CRK640 | CRK | Chek Lap Kok International Airport (VHHH) | Iki Airport (RJDB) | 2026-07-21 03:34 UTC | 2026-07-21 06:20 UTC | 2h 45m |
| DCS603 | DCS | Copernicus Wrocław Airport (EPWR) | Cluj-Napoca International Airport (LRCL) | 2026-07-21 05:24 UTC | 2026-07-21 06:16 UTC | 51m |
| AA0013 |  | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-21 05:57 UTC | 2026-07-21 06:15 UTC | 18m |
| N112CC |  | San Francisco International Airport (KSFO) | Brown Field Municipal Airport (KSDM) | 2026-07-21 04:59 UTC | 2026-07-21 06:08 UTC | 1h 9m |
| HBZUR | HBZ | Wangen-Lachen Airport (LSPV) | LSMF (LSMF) | 2026-07-21 05:44 UTC | 2026-07-21 06:06 UTC | 21m |
| BAW31 | British Airways | London Heathrow Airport (EGLL) | Macau International Airport (VMMC) | 2026-07-20 18:42 UTC | 2026-07-21 06:06 UTC | 11h 23m |
| WIF3BR | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-07-21 05:38 UTC | 2026-07-21 06:05 UTC | 27m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
