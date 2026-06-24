# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_22:39:24_UTC-green)

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

**Latest saved flight:** 2026-06-24 22:39:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-24 22:39:24 UTC

- **119,458** saved flights
- **41,155** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **119,458** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,445,873.4 tonnes** estimated CO2 emissions
- **83,818,746 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4918 |
| 2 | SkyWest Airlines | 4411 |
| 3 | EJA | 2312 |
| 4 | IndiGo | 2301 |
| 5 | American Airlines | 1859 |
| 6 | Southwest Airlines | 1777 |
| 7 | ENY | 1492 |
| 8 | Delta Air Lines | 1407 |
| 9 | Lufthansa | 1312 |
| 10 | Vueling | 1077 |
| 11 | WIF | 1060 |
| 12 | LATAM Airlines | 1057 |
| 13 | AZU | 995 |
| 14 | AXM | 973 |
| 15 | LXJ | 906 |
| 16 | Swiss International | 839 |
| 17 | All Nippon Airways | 816 |
| 18 | Alaska Airlines | 790 |
| 19 | easyJet | 769 |
| 20 | QLK | 763 |
| 21 | EJU | 749 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 666 |
| 24 | United Airlines | 656 |
| 25 | VIV | 654 |
| 26 | Air France | 652 |
| 27 | CXK | 639 |
| 28 | MXY | 626 |
| 29 | AXB | 593 |
| 30 | GLO | 587 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 101132 |
| 2 | 🇪🇸 ES | 8136 |
| 3 | 🇮🇳 IN | 7226 |
| 4 | 🇦🇺 AU | 7020 |
| 5 | 🇧🇷 BR | 6579 |
| 6 | 🇩🇪 DE | 6384 |
| 7 | 🇮🇹 IT | 6377 |
| 8 | 🇨🇦 CA | 6281 |
| 9 | 🇯🇵 JP | 5320 |
| 10 | 🇬🇧 GB | 5250 |
| 11 | 🇫🇷 FR | 4753 |
| 12 | 🇨🇴 CO | 4012 |
| 13 | 🇲🇽 MX | 3487 |
| 14 | 🇬🇷 GR | 3410 |
| 15 | 🇳🇴 NO | 3290 |
| 16 | 🇨🇭 CH | 3074 |
| 17 | 🇲🇾 MY | 2531 |
| 18 | 🇹🇷 TR | 2453 |
| 19 | 🇿🇦 ZA | 2013 |
| 20 | 🇵🇱 PL | 1965 |
| 21 | 🇳🇿 NZ | 1936 |
| 22 | 🇹🇭 TH | 1909 |
| 23 | 🇰🇷 KR | 1898 |
| 24 | 🇵🇭 PH | 1714 |
| 25 | 🇬🇹 GT | 1673 |
| 26 | 🇲🇦 MA | 1291 |
| 27 | 🇲🇪 ME | 1190 |
| 28 | 🇲🇴 MO | 1172 |
| 29 | 🇳🇱 NL | 1148 |
| 30 | 🇭🇷 HR | 1035 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2513 |
| 2 | Denver International Airport |  | US | 2005 |
| 3 | Tokyo International Airport |  | JP | 1762 |
| 4 | Indira Gandhi International Airport |  | IN | 1588 |
| 5 | Guaymaral Airport |  | CO | 1502 |
| 6 | Harry Reid International Airport |  | US | 1483 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1450 |
| 8 | Zurich Airport |  | CH | 1332 |
| 9 | La Aurora Airport |  | GT | 1291 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1267 |
| 11 | Frankfurt am Main International Airport |  | DE | 1267 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1182 |
| 13 | Macau International Airport |  | MO | 1172 |
| 14 | El Dorado International Airport |  | CO | 1171 |
| 15 | Chicago O'Hare International Airport |  | US | 1169 |
| 16 | Capua Airport |  | IT | 1028 |
| 17 | Salt Lake City International Airport |  | US | 1026 |
| 18 | Madrid Barajas International Airport |  | ES | 1007 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 998 |
| 20 | Kuala Lumpur International Airport |  | MY | 979 |
| 21 | Congonhas Airport |  | BR | 919 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 917 |
| 23 | Charlotte/Douglas International Airport |  | US | 908 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 883 |
| 25 | Charles de Gaulle International Airport |  | FR | 874 |
| 26 | Bengaluru International Airport |  | IN | 873 |
| 27 | Malpensa International Airport |  | IT | 836 |
| 28 | Ninoy Aquino International Airport |  | PH | 793 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 782 |
| 30 | Daniel K Inouye International Airport |  | US | 770 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 757 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 735 |
| 34 | Vitoria/Foronda Airport |  | ES | 699 |
| 35 | Calgary International Airport |  | CA | 698 |
| 36 | Amsterdam Airport Schiphol |  | NL | 694 |
| 37 | Don Mueang International Airport |  | TH | 691 |
| 38 | Seattle-Tacoma International Airport |  | US | 685 |
| 39 | Scottsdale Airport |  | US | 678 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 677 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 625 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 432 | 21m | 244 km | 1,819.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 314 | 24m | 225 km | 1,218.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 306 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 290 | 1h 25m | 910 km | 4,550.8 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 287 | 1h 10m | 770 km | 3,812.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 236 | 26m | 275 km | 1,118.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 221 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 177 | 22m | 55 km | 168.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 171 | 26m | 215 km | 633.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 164 | 44m | 241 km | 681.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 153 | 44m | 452 km | 1,192.4 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 149 | 18m | 144 km | 370.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 140 | 1h 38m | 1,156 km | 2,792.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 135 | 1h 17m | 961 km | 2,237.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N13HC |  | Deck Airport (K9D4) | DE04 (DE04) | 2026-06-24 21:51 UTC | 2026-06-24 22:39 UTC | 48m |
| ICE631 | ICE | Keflavik International Airport (BIKF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-24 17:27 UTC | 2026-06-24 22:35 UTC | 5h 8m |
| N4306B |  | Heritage Field (KPTW) | Northumberland County Airport (KN79) | 2026-06-24 22:02 UTC | 2026-06-24 22:34 UTC | 32m |
| N629D |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Albers Airport (SN13) | 2026-06-24 22:10 UTC | 2026-06-24 22:33 UTC | 23m |
| N3287Q |  | East Kansas City Airport (K3GV) | East Kansas City Airport (K3GV) | 2026-06-24 22:12 UTC | 2026-06-24 22:32 UTC | 20m |
| N62112 |  | John C Tune Airport (KJWN) | Springfield Robertson County Airport (KM91) | 2026-06-24 21:55 UTC | 2026-06-24 22:28 UTC | 33m |
| N4978G |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-06-24 21:34 UTC | 2026-06-24 22:28 UTC | 53m |
| UAV12 | UAV | Sun Hill Ranch Airport (CA70) | Sun Hill Ranch Airport (CA70) | 2026-06-24 21:57 UTC | 2026-06-24 22:27 UTC | 30m |
| N6269Q |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-06-24 21:34 UTC | 2026-06-24 22:23 UTC | 49m |
| N414EP |  | Easton State Airport (KESW) | Auburn Municipal Airport (KS50) | 2026-06-24 22:04 UTC | 2026-06-24 22:21 UTC | 16m |
| YTZ | YTZ | Toowoomba Wellcamp Airport (YBWW) | Sunshine Coast Airport (YBMC) | 2026-06-24 20:56 UTC | 2026-06-24 22:19 UTC | 1h 23m |
| JBU1351 | JetBlue | Nantucket Memorial Airport (KACK) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-24 21:58 UTC | 2026-06-24 22:18 UTC | 20m |
| FRLD64 | FRL | Kanab Municipal Airport (KKNB) | Santa Fe Regional Airport (KSAF) | 2026-06-24 21:04 UTC | 2026-06-24 22:17 UTC | 1h 12m |
| N65716 |  | Central Jersey Regional Airport (K47N) | Central Jersey Regional Airport (K47N) | 2026-06-24 22:05 UTC | 2026-06-24 22:12 UTC | 7m |
| RYR76SW | Ryanair | London Stansted Airport (EGSS) | Cologne Bonn Airport (EDDK) | 2026-06-24 21:11 UTC | 2026-06-24 22:12 UTC | 1h 1m |
| SKW6295 | SkyWest Airlines | Dallas-Fort Worth International Airport (KDFW) | NM76 (NM76) | 2026-06-24 21:06 UTC | 2026-06-24 22:09 UTC | 1h 3m |
| N100DA |  | KU77 (KU77) | K36U (K36U) | 2026-06-24 21:36 UTC | 2026-06-24 22:07 UTC | 30m |
| EJA532 | EJA | Greenville Downtown Airport (KGMU) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-24 20:19 UTC | 2026-06-24 22:07 UTC | 1h 47m |
| STT5026 | STT | Lanai Airport (PHNY) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-06-24 21:38 UTC | 2026-06-24 22:04 UTC | 25m |
|  |  | Wilbur Airport (K2S8) | Pru Field (K33S) | 2026-06-24 21:02 UTC | 2026-06-24 22:03 UTC | 1h 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
