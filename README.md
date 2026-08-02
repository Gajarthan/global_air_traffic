# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_10:28:45_UTC-green)

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

**Latest saved flight:** 2026-08-02 10:28:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-02 10:28:45 UTC

- **166,233** saved flights
- **54,475** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **166,233** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,001,617.7 tonnes** estimated CO2 emissions
- **116,035,809 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6632 |
| 2 | SkyWest Airlines | 6059 |
| 3 | EJA | 3293 |
| 4 | IndiGo | 2930 |
| 5 | American Airlines | 2623 |
| 6 | Southwest Airlines | 2614 |
| 7 | ENY | 2068 |
| 8 | Delta Air Lines | 1985 |
| 9 | LATAM Airlines | 1547 |
| 10 | Lufthansa | 1539 |
| 11 | AZU | 1455 |
| 12 | WIF | 1389 |
| 13 | Vueling | 1373 |
| 14 | LXJ | 1290 |
| 15 | AXM | 1150 |
| 16 | Swiss International | 1139 |
| 17 | easyJet | 1097 |
| 18 | Alaska Airlines | 1026 |
| 19 | EJU | 1021 |
| 20 | QLK | 1020 |
| 21 | All Nippon Airways | 1015 |
| 22 | VIV | 916 |
| 23 | Cathay Pacific | 886 |
| 24 | CXK | 886 |
| 25 | United Airlines | 877 |
| 26 | AEE | 874 |
| 27 | GLO | 870 |
| 28 | Air France | 859 |
| 29 | MXY | 857 |
| 30 | JetBlue | 840 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 143422 |
| 2 | 🇪🇸 ES | 10625 |
| 3 | 🇧🇷 BR | 9451 |
| 4 | 🇦🇺 AU | 9336 |
| 5 | 🇮🇳 IN | 9186 |
| 6 | 🇨🇦 CA | 9023 |
| 7 | 🇮🇹 IT | 8588 |
| 8 | 🇩🇪 DE | 8303 |
| 9 | 🇬🇧 GB | 7657 |
| 10 | 🇯🇵 JP | 6720 |
| 11 | 🇫🇷 FR | 6588 |
| 12 | 🇨🇴 CO | 5975 |
| 13 | 🇬🇷 GR | 4807 |
| 14 | 🇲🇽 MX | 4760 |
| 15 | 🇨🇭 CH | 4372 |
| 16 | 🇳🇴 NO | 4345 |
| 17 | 🇹🇷 TR | 4008 |
| 18 | 🇲🇾 MY | 2995 |
| 19 | 🇵🇱 PL | 2809 |
| 20 | 🇿🇦 ZA | 2705 |
| 21 | 🇳🇿 NZ | 2430 |
| 22 | 🇹🇭 TH | 2404 |
| 23 | 🇵🇭 PH | 2204 |
| 24 | 🇰🇷 KR | 2143 |
| 25 | 🇬🇹 GT | 2141 |
| 26 | 🇲🇦 MA | 1671 |
| 27 | 🇭🇷 HR | 1579 |
| 28 | 🇲🇪 ME | 1546 |
| 29 | 🇳🇱 NL | 1509 |
| 30 | 🇲🇴 MO | 1420 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3399 |
| 2 | Denver International Airport |  | US | 2766 |
| 3 | Tokyo International Airport |  | JP | 2111 |
| 4 | Guaymaral Airport |  | CO | 2082 |
| 5 | Indira Gandhi International Airport |  | IN | 2038 |
| 6 | Harry Reid International Airport |  | US | 2005 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1828 |
| 8 | Zurich Airport |  | CH | 1767 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1745 |
| 10 | La Aurora Airport |  | GT | 1658 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1539 |
| 12 | El Dorado International Airport |  | CO | 1521 |
| 13 | Frankfurt am Main International Airport |  | DE | 1503 |
| 14 | Chicago O'Hare International Airport |  | US | 1500 |
| 15 | Salt Lake City International Airport |  | US | 1490 |
| 16 | Macau International Airport |  | MO | 1420 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1385 |
| 18 | Congonhas Airport |  | BR | 1370 |
| 19 | Madrid Barajas International Airport |  | ES | 1308 |
| 20 | Capua Airport |  | IT | 1298 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1264 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1175 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1173 |
| 24 | Charlotte/Douglas International Airport |  | US | 1162 |
| 25 | Charles de Gaulle International Airport |  | FR | 1136 |
| 26 | Kuala Lumpur International Airport |  | MY | 1133 |
| 27 | Malpensa International Airport |  | IT | 1111 |
| 28 | Bengaluru International Airport |  | IN | 1085 |
| 29 | Ninoy Aquino International Airport |  | PH | 1035 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1024 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1019 |
| 32 | Barcelona International Airport |  | ES | 981 |
| 33 | Daniel K Inouye International Airport |  | US | 970 |
| 34 | Seattle-Tacoma International Airport |  | US | 965 |
| 35 | Calgary International Airport |  | CA | 944 |
| 36 | Viracopos International Airport |  | BR | 941 |
| 37 | Scottsdale Airport |  | US | 926 |
| 38 | Tenerife Norte Airport |  | ES | 925 |
| 39 | Oslo Gardermoen Airport |  | NO | 920 |
| 40 | Reno/Tahoe International Airport |  | US | 917 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 606 | 21m | 244 km | 2,551.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 400 | 24m | 225 km | 1,551.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 399 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 378 | 1h 9m | 770 km | 5,021.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 313 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 244 | 19m | 165 km | 694.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 229 | 1h 47m | 1,423 km | 5,620.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 218 | 20m | 250 km | 941.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 216 | 26m | 215 km | 800.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 210 | 31m | 49 km | 177.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 196 | 19m | 144 km | 487.5 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 192 | 31m | 369 km | 1,222.1 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 189 | 50m | 556 km | 1,811.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 189 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 182 | 1h 1m | 695 km | 2,181.6 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 179 | 24m | 218 km | 674.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-02 10:17 UTC | 2026-08-02 10:28 UTC | 10m |
| EXS13BP | EXS | London Stansted Airport (EGSS) | Eleftherios Venizelos International Airport (LGAV) | 2026-08-02 07:16 UTC | 2026-08-02 10:21 UTC | 3h 5m |
| MMA712 | MMA | Guangzhou Baiyun International Airport (ZGGG) | Mae Sariang Airport (VTCS) | 2026-08-02 07:48 UTC | 2026-08-02 10:18 UTC | 2h 30m |
| AJO598 | AJO | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-02 09:28 UTC | 2026-08-02 10:13 UTC | 44m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-02 09:56 UTC | 2026-08-02 10:06 UTC | 10m |
| VOZ696 | Virgin Australia | Perth International Airport (YPPH) | Melbourne International Airport (YMML) | 2026-08-02 06:37 UTC | 2026-08-02 10:02 UTC | 3h 24m |
| RYR9HL | Ryanair | Palma De Mallorca Airport (LEPA) | Cologne Bonn Airport (EDDK) | 2026-08-02 07:42 UTC | 2026-08-02 09:44 UTC | 2h 2m |
|  |  | Ataturk International Airport (LTBA) | Istanbul Airport (LTFM) | 2026-08-02 09:00 UTC | 2026-08-02 09:39 UTC | 39m |
| TIE796R | TIE | Václav Havel Airport (LKPR) | Samedan Airport (LSZS) | 2026-08-02 08:50 UTC | 2026-08-02 09:34 UTC | 43m |
| EZY92DA | easyJet | Glasgow International Airport (EGPF) | London Luton Airport (EGGW) | 2026-08-02 08:41 UTC | 2026-08-02 09:32 UTC | 50m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-02 09:01 UTC | 2026-08-02 09:32 UTC | 30m |
| GCMWC | GCM | Damyns Hall Aerodrome (EGML) | Damyns Hall Aerodrome (EGML) | 2026-08-02 09:00 UTC | 2026-08-02 09:31 UTC | 30m |
| IGO4EP | IndiGo | Chennai International Airport (VOMM) | Salem Airport (VOSM) | 2026-08-02 08:53 UTC | 2026-08-02 09:30 UTC | 37m |
| OKHEI | OKH | Letnany Airport (LKLT) | Roudnice Mad Airport (LKRO) | 2026-08-02 08:59 UTC | 2026-08-02 09:29 UTC | 30m |
| NHL06 | NHL | HUDDERSFIELD (Crosland Moor) (EGND) | HUDDERSFIELD (Crosland Moor) (EGND) | 2026-08-02 09:09 UTC | 2026-08-02 09:29 UTC | 20m |
| HBZWE | HBZ | Bern Belp Airport (LSZB) | Raron Airport (LSTA) | 2026-08-02 09:08 UTC | 2026-08-02 09:28 UTC | 20m |
| IGO502F | IndiGo | Indira Gandhi International Airport (VIDP) | Chandigarh Airport (VICG) | 2026-08-02 09:01 UTC | 2026-08-02 09:27 UTC | 26m |
| CYF108 | CYF | Larnaca International Airport (LCLK) | Ben Gurion International Airport (LLBG) | 2026-08-02 08:44 UTC | 2026-08-02 09:27 UTC | 43m |
| FAD512 | FAD | Dubai International Airport (OMDB) | Al Ahsa Airport (OEAH) | 2026-08-01 17:45 UTC | 2026-08-02 09:26 UTC | 15h 40m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Stykkishólmur Airport (BIST) | 2026-08-02 09:03 UTC | 2026-08-02 09:23 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
