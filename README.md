# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_21:37:15_UTC-green)

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

**Latest saved flight:** 2026-07-01 21:37:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-01 21:37:15 UTC

- **125,995** saved flights
- **43,067** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **125,995** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,520,477.6 tonnes** estimated CO2 emissions
- **88,143,632 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5122 |
| 2 | SkyWest Airlines | 4660 |
| 3 | EJA | 2473 |
| 4 | IndiGo | 2390 |
| 5 | American Airlines | 1939 |
| 6 | Southwest Airlines | 1884 |
| 7 | ENY | 1582 |
| 8 | Delta Air Lines | 1503 |
| 9 | Lufthansa | 1347 |
| 10 | LATAM Airlines | 1139 |
| 11 | Vueling | 1119 |
| 12 | WIF | 1112 |
| 13 | AZU | 1062 |
| 14 | AXM | 996 |
| 15 | LXJ | 979 |
| 16 | Swiss International | 879 |
| 17 | All Nippon Airways | 845 |
| 18 | Alaska Airlines | 822 |
| 19 | easyJet | 806 |
| 20 | QLK | 785 |
| 21 | EJU | 781 |
| 22 | Cathay Pacific | 699 |
| 23 | AEE | 694 |
| 24 | VIV | 689 |
| 25 | Air France | 688 |
| 26 | CXK | 675 |
| 27 | United Airlines | 670 |
| 28 | MXY | 655 |
| 29 | JetBlue | 645 |
| 30 | GLO | 634 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 107720 |
| 2 | 🇪🇸 ES | 8422 |
| 3 | 🇮🇳 IN | 7492 |
| 4 | 🇦🇺 AU | 7329 |
| 5 | 🇧🇷 BR | 7022 |
| 6 | 🇩🇪 DE | 6655 |
| 7 | 🇨🇦 CA | 6629 |
| 8 | 🇮🇹 IT | 6628 |
| 9 | 🇬🇧 GB | 5571 |
| 10 | 🇯🇵 JP | 5508 |
| 11 | 🇫🇷 FR | 4979 |
| 12 | 🇨🇴 CO | 4046 |
| 13 | 🇲🇽 MX | 3655 |
| 14 | 🇬🇷 GR | 3594 |
| 15 | 🇳🇴 NO | 3452 |
| 16 | 🇨🇭 CH | 3205 |
| 17 | 🇹🇷 TR | 2656 |
| 18 | 🇲🇾 MY | 2576 |
| 19 | 🇿🇦 ZA | 2080 |
| 20 | 🇵🇱 PL | 2066 |
| 21 | 🇳🇿 NZ | 2029 |
| 22 | 🇹🇭 TH | 1970 |
| 23 | 🇰🇷 KR | 1946 |
| 24 | 🇵🇭 PH | 1778 |
| 25 | 🇬🇹 GT | 1740 |
| 26 | 🇲🇦 MA | 1354 |
| 27 | 🇲🇪 ME | 1250 |
| 28 | 🇳🇱 NL | 1189 |
| 29 | 🇲🇴 MO | 1182 |
| 30 | 🇧🇸 BS | 1091 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2634 |
| 2 | Denver International Airport |  | US | 2125 |
| 3 | Tokyo International Airport |  | JP | 1819 |
| 4 | Indira Gandhi International Airport |  | IN | 1647 |
| 5 | Harry Reid International Airport |  | US | 1573 |
| 6 | Guaymaral Airport |  | CO | 1533 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1506 |
| 8 | Zurich Airport |  | CH | 1392 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1345 |
| 10 | La Aurora Airport |  | GT | 1344 |
| 11 | Frankfurt am Main International Airport |  | DE | 1301 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1233 |
| 13 | Chicago O'Hare International Airport |  | US | 1218 |
| 14 | Macau International Airport |  | MO | 1182 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1111 |
| 17 | Capua Airport |  | IT | 1066 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1046 |
| 19 | Madrid Barajas International Airport |  | ES | 1041 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1026 |
| 21 | Kuala Lumpur International Airport |  | MY | 1003 |
| 22 | Congonhas Airport |  | BR | 985 |
| 23 | Charlotte/Douglas International Airport |  | US | 947 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 920 |
| 25 | Charles de Gaulle International Airport |  | FR | 917 |
| 26 | Bengaluru International Airport |  | IN | 905 |
| 27 | Malpensa International Airport |  | IT | 863 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 838 |
| 29 | Ninoy Aquino International Airport |  | PH | 824 |
| 30 | Daniel K Inouye International Airport |  | US | 804 |
| 31 | Barcelona International Airport |  | ES | 789 |
| 32 | Tenerife Norte Airport |  | ES | 773 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 768 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 739 |
| 35 | Calgary International Airport |  | CA | 738 |
| 36 | Scottsdale Airport |  | US | 731 |
| 37 | Seattle-Tacoma International Airport |  | US | 728 |
| 38 | Vitoria/Foronda Airport |  | ES | 724 |
| 39 | Amsterdam Airport Schiphol |  | NL | 718 |
| 40 | Viracopos International Airport |  | BR | 714 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 639 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 459 | 21m | 244 km | 1,932.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 324 | 24m | 225 km | 1,257.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 317 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 302 | 1h 10m | 770 km | 4,011.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 233 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 174 | 44m | 241 km | 722.8 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 162 | 1h 45m | 1,423 km | 3,975.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 147 | 1h 1m | 695 km | 1,762.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 146 | 1h 17m | 961 km | 2,420.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 144 | 30m | 49 km | 121.7 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N472AT |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-01 20:42 UTC | 2026-07-01 21:37 UTC | 54m |
| CPA640 | Cathay Pacific | Biratnagar Airport (VNVT) | Zhuhai Airport (ZGSD) | 2026-07-01 18:11 UTC | 2026-07-01 21:33 UTC | 3h 22m |
| N509JE |  | NJ64 (NJ64) | Cross Keys Airport (K17N) | 2026-07-01 20:06 UTC | 2026-07-01 21:33 UTC | 1h 26m |
| CLB424 | CLB | Durham Tees Valley Airport (EGNV) | Benbecula Airport (EGPL) | 2026-07-01 19:45 UTC | 2026-07-01 21:30 UTC | 1h 45m |
| N721JD |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-07-01 21:04 UTC | 2026-07-01 21:29 UTC | 25m |
| LEGEND2 | LEG | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-07-01 20:46 UTC | 2026-07-01 21:23 UTC | 36m |
| N669FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-07-01 20:54 UTC | 2026-07-01 21:21 UTC | 26m |
| CGTNX | CGT | Squamish Airport (CYSE) | Vancouver International Airport (CYVR) | 2026-07-01 21:01 UTC | 2026-07-01 21:18 UTC | 17m |
| N54TT |  | Peter O Knight Airport (KTPF) | Orlando Executive Airport (KORL) | 2026-07-01 20:49 UTC | 2026-07-01 21:17 UTC | 27m |
| TKR103 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-01 20:41 UTC | 2026-07-01 21:15 UTC | 34m |
| 080309 |  | Fort Worth Meacham International Airport (KFTW) | Sinton Airport (KT69) | 2026-07-01 20:09 UTC | 2026-07-01 21:15 UTC | 1h 6m |
| BELLS76 | Brussels Airlines | Elk Park Ranch Airport (34CD) | Elk Park Ranch Airport (34CD) | 2026-07-01 20:55 UTC | 2026-07-01 21:06 UTC | 11m |
| N10502 |  | Charlotte/Monroe Executive Airport (KEQY) | Moore County Airport (KSOP) | 2026-07-01 20:39 UTC | 2026-07-01 21:05 UTC | 26m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-07-01 06:07 UTC | 2026-07-01 21:05 UTC | 14h 58m |
| LXJ353 | LXJ | Southwest Florida International Airport (KRSW) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-07-01 19:19 UTC | 2026-07-01 21:03 UTC | 1h 43m |
| N111Y |  | Nashville International Airport (KBNA) | Cherry Capital Airport (KTVC) | 2026-07-01 19:51 UTC | 2026-07-01 21:00 UTC | 1h 9m |
| N797GM |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-07-01 20:24 UTC | 2026-07-01 21:00 UTC | 35m |
| N425AM |  | Bowman Field (KLOU) | Bowman Field (KLOU) | 2026-07-01 20:59 UTC | 2026-07-01 21:00 UTC | 0m |
| EZY93HL | easyJet | Charles de Gaulle International Airport (LFPG) | London Gatwick Airport (EGKK) | 2026-07-01 20:23 UTC | 2026-07-01 21:00 UTC | 36m |
| 00000000 |  | Flying Cloud Airport (KFCM) | Staples Municipal Airport (KSAZ) | 2026-07-01 20:38 UTC | 2026-07-01 21:00 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
