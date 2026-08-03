# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_07:20:47_UTC-green)

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

**Latest saved flight:** 2026-08-03 07:20:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 07:20:47 UTC

- **168,278** saved flights
- **54,975** unique routes
- **139** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **168,278** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **2,028,740.9 tonnes** estimated CO2 emissions
- **117,608,168 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6710 |
| 2 | SkyWest Airlines | 6146 |
| 3 | EJA | 3348 |
| 4 | IndiGo | 2965 |
| 5 | American Airlines | 2657 |
| 6 | Southwest Airlines | 2650 |
| 7 | ENY | 2099 |
| 8 | Delta Air Lines | 2009 |
| 9 | LATAM Airlines | 1560 |
| 10 | Lufthansa | 1546 |
| 11 | AZU | 1481 |
| 12 | WIF | 1405 |
| 13 | Vueling | 1386 |
| 14 | LXJ | 1318 |
| 15 | AXM | 1163 |
| 16 | Swiss International | 1152 |
| 17 | easyJet | 1130 |
| 18 | EJU | 1035 |
| 19 | Alaska Airlines | 1031 |
| 20 | QLK | 1027 |
| 21 | All Nippon Airways | 1022 |
| 22 | VIV | 929 |
| 23 | Cathay Pacific | 898 |
| 24 | CXK | 892 |
| 25 | United Airlines | 889 |
| 26 | GLO | 882 |
| 27 | AEE | 881 |
| 28 | Air France | 865 |
| 29 | MXY | 864 |
| 30 | JetBlue | 850 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145128 |
| 2 | 🇪🇸 ES | 10780 |
| 3 | 🇧🇷 BR | 9578 |
| 4 | 🇦🇺 AU | 9400 |
| 5 | 🇮🇳 IN | 9287 |
| 6 | 🇨🇦 CA | 9118 |
| 7 | 🇮🇹 IT | 8688 |
| 8 | 🇩🇪 DE | 8385 |
| 9 | 🇬🇧 GB | 7812 |
| 10 | 🇯🇵 JP | 6781 |
| 11 | 🇫🇷 FR | 6666 |
| 12 | 🇨🇴 CO | 6063 |
| 13 | 🇬🇷 GR | 4885 |
| 14 | 🇲🇽 MX | 4817 |
| 15 | 🇨🇭 CH | 4427 |
| 16 | 🇳🇴 NO | 4395 |
| 17 | 🇹🇷 TR | 4064 |
| 18 | 🇲🇾 MY | 3029 |
| 19 | 🇵🇱 PL | 2835 |
| 20 | 🇿🇦 ZA | 2735 |
| 21 | 🇳🇿 NZ | 2448 |
| 22 | 🇹🇭 TH | 2438 |
| 23 | 🇵🇭 PH | 2227 |
| 24 | 🇬🇹 GT | 2176 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1703 |
| 27 | 🇭🇷 HR | 1611 |
| 28 | 🇲🇪 ME | 1556 |
| 29 | 🇳🇱 NL | 1528 |
| 30 | 🇲🇴 MO | 1429 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3457 |
| 2 | Denver International Airport |  | US | 2799 |
| 3 | Tokyo International Airport |  | JP | 2130 |
| 4 | Guaymaral Airport |  | CO | 2094 |
| 5 | Indira Gandhi International Airport |  | IN | 2056 |
| 6 | Harry Reid International Airport |  | US | 2026 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1843 |
| 8 | Zurich Airport |  | CH | 1788 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1770 |
| 10 | La Aurora Airport |  | GT | 1681 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1554 |
| 12 | Chicago O'Hare International Airport |  | US | 1525 |
| 13 | El Dorado International Airport |  | CO | 1524 |
| 14 | Frankfurt am Main International Airport |  | DE | 1512 |
| 15 | Salt Lake City International Airport |  | US | 1506 |
| 16 | Macau International Airport |  | MO | 1429 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1394 |
| 18 | Congonhas Airport |  | BR | 1380 |
| 19 | Madrid Barajas International Airport |  | ES | 1326 |
| 20 | Capua Airport |  | IT | 1310 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1279 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1187 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1183 |
| 24 | Charlotte/Douglas International Airport |  | US | 1172 |
| 25 | Charles de Gaulle International Airport |  | FR | 1144 |
| 26 | Kuala Lumpur International Airport |  | MY | 1140 |
| 27 | Malpensa International Airport |  | IT | 1132 |
| 28 | Bengaluru International Airport |  | IN | 1102 |
| 29 | Ninoy Aquino International Airport |  | PH | 1047 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1039 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1035 |
| 32 | Barcelona International Airport |  | ES | 993 |
| 33 | Daniel K Inouye International Airport |  | US | 980 |
| 34 | Seattle-Tacoma International Airport |  | US | 978 |
| 35 | Viracopos International Airport |  | BR | 960 |
| 36 | Calgary International Airport |  | CA | 952 |
| 37 | Tenerife Norte Airport |  | ES | 938 |
| 38 | Reno/Tahoe International Airport |  | US | 936 |
| 39 | Oslo Gardermoen Airport |  | NO | 934 |
| 40 | Scottsdale Airport |  | US | 932 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 871 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 613 | 21m | 244 km | 2,581.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 402 | 24m | 225 km | 1,559.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 402 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 381 | 1h 9m | 770 km | 5,061.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 288 | 27m | 275 km | 1,364.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 245 | 44m | 241 km | 1,017.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 231 | 1h 47m | 1,423 km | 5,669.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 222 | 20m | 250 km | 958.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 210 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 199 | 19m | 144 km | 495.0 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 198 | 1h 15m | 961 km | 3,282.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 196 | 31m | 369 km | 1,247.6 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 196 | 50m | 556 km | 1,878.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 189 | 1h 38m | 1,156 km | 3,770.5 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 185 | 24m | 218 km | 697.0 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N739UL |  | Oakland San Francisco Bay Airport (KOAK) | Sacramento Executive Airport (KSAC) | 2026-08-03 05:52 UTC | 2026-08-03 07:20 UTC | 1h 27m |
| CONDR31 | CON | Getafe Air Base (LEGT) | Valladolid Airport (LEVD) | 2026-08-03 06:54 UTC | 2026-08-03 07:15 UTC | 20m |
| VKG1112 | VKG | Copenhagen Kastrup Airport (EKCH) | LZSY (LZSY) | 2026-08-03 06:13 UTC | 2026-08-03 07:10 UTC | 57m |
| NOS24MC | NOS | Malpensa International Airport (LIMC) | Monastir Habib Bourguiba International Airport (DTMB) | 2026-08-03 05:25 UTC | 2026-08-03 07:10 UTC | 1h 44m |
| WIF4X | WIF | Oslo Gardermoen Airport (ENGM) | Gol Airport (ENKL) | 2026-08-03 06:18 UTC | 2026-08-03 06:56 UTC | 37m |
| UZB3218 | UZB | Indira Gandhi International Airport (VIDP) | Bezymyanka Airfield (UWWG) | 2026-08-02 23:05 UTC | 2026-08-03 06:53 UTC | 7h 47m |
|  |  | LICL (LICL) | Comiso Airport Vincenzo Magliocco (LICB) | 2026-08-03 06:17 UTC | 2026-08-03 06:51 UTC | 33m |
| N470LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-08-03 04:11 UTC | 2026-08-03 06:48 UTC | 2h 36m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-08-03 05:49 UTC | 2026-08-03 06:45 UTC | 55m |
| ZSORP | ZSO | Lanseria Airport (FALA) | Rooiberg Airport (FARO) | 2026-08-03 06:20 UTC | 2026-08-03 06:41 UTC | 21m |
| CFG4FD | CFG | Munich International Airport (EDDM) | Chania International Airport (LGSA) | 2026-08-03 04:22 UTC | 2026-08-03 06:36 UTC | 2h 14m |
| PAG02 | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Mccreary Airport (CJR8) | 2026-08-03 06:03 UTC | 2026-08-03 06:36 UTC | 32m |
| REH50 | REH | Redding Regional Airport (KRDD) | Hayfork Airport (KF62) | 2026-08-03 06:15 UTC | 2026-08-03 06:31 UTC | 16m |
| BNOB | BNO | Bodø Airport (ENBO) | Bardufoss Airport (ENDU) | 2026-08-03 05:56 UTC | 2026-08-03 06:31 UTC | 34m |
| N327CH |  | Mayhall Airport (5LL3) | Frasca Field (KC16) | 2026-08-03 06:19 UTC | 2026-08-03 06:30 UTC | 11m |
| N524MT |  | John C Tune Airport (KJWN) | John C Tune Airport (KJWN) | 2026-08-03 06:26 UTC | 2026-08-03 06:29 UTC | 3m |
| EJU18TV | EJU | Malaga Airport (LEMG) | Annemasse Airport (LFLI) | 2026-08-03 04:28 UTC | 2026-08-03 06:25 UTC | 1h 57m |
| KLM27E | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Montricher Airport (LSTR) | 2026-08-03 05:11 UTC | 2026-08-03 06:25 UTC | 1h 14m |
| JFA07J | JFA | Paris-Le Bourget Airport (LFPB) | La Cote Airport (LSGP) | 2026-08-03 05:13 UTC | 2026-08-03 06:25 UTC | 1h 12m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-03 05:46 UTC | 2026-08-03 06:23 UTC | 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
