# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_00:06:04_UTC-green)

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

**Latest saved flight:** 2026-07-02 00:06:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-02 00:06:04 UTC

- **126,313** saved flights
- **43,163** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **126,313** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,523,617.1 tonnes** estimated CO2 emissions
- **88,325,628 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5124 |
| 2 | SkyWest Airlines | 4674 |
| 3 | EJA | 2488 |
| 4 | IndiGo | 2390 |
| 5 | American Airlines | 1947 |
| 6 | Southwest Airlines | 1893 |
| 7 | ENY | 1589 |
| 8 | Delta Air Lines | 1509 |
| 9 | Lufthansa | 1347 |
| 10 | LATAM Airlines | 1148 |
| 11 | Vueling | 1120 |
| 12 | WIF | 1112 |
| 13 | AZU | 1069 |
| 14 | AXM | 996 |
| 15 | LXJ | 984 |
| 16 | Swiss International | 879 |
| 17 | All Nippon Airways | 847 |
| 18 | Alaska Airlines | 822 |
| 19 | easyJet | 807 |
| 20 | QLK | 789 |
| 21 | EJU | 782 |
| 22 | Cathay Pacific | 699 |
| 23 | AEE | 694 |
| 24 | VIV | 692 |
| 25 | Air France | 688 |
| 26 | CXK | 678 |
| 27 | United Airlines | 671 |
| 28 | MXY | 658 |
| 29 | JetBlue | 648 |
| 30 | GLO | 638 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 108141 |
| 2 | 🇪🇸 ES | 8426 |
| 3 | 🇮🇳 IN | 7492 |
| 4 | 🇦🇺 AU | 7345 |
| 5 | 🇧🇷 BR | 7068 |
| 6 | 🇩🇪 DE | 6658 |
| 7 | 🇨🇦 CA | 6648 |
| 8 | 🇮🇹 IT | 6632 |
| 9 | 🇬🇧 GB | 5575 |
| 10 | 🇯🇵 JP | 5516 |
| 11 | 🇫🇷 FR | 4979 |
| 12 | 🇨🇴 CO | 4046 |
| 13 | 🇲🇽 MX | 3669 |
| 14 | 🇬🇷 GR | 3594 |
| 15 | 🇳🇴 NO | 3453 |
| 16 | 🇨🇭 CH | 3205 |
| 17 | 🇹🇷 TR | 2659 |
| 18 | 🇲🇾 MY | 2577 |
| 19 | 🇿🇦 ZA | 2080 |
| 20 | 🇵🇱 PL | 2068 |
| 21 | 🇳🇿 NZ | 2037 |
| 22 | 🇹🇭 TH | 1970 |
| 23 | 🇰🇷 KR | 1947 |
| 24 | 🇵🇭 PH | 1784 |
| 25 | 🇬🇹 GT | 1740 |
| 26 | 🇲🇦 MA | 1355 |
| 27 | 🇲🇪 ME | 1251 |
| 28 | 🇳🇱 NL | 1189 |
| 29 | 🇲🇴 MO | 1182 |
| 30 | 🇧🇸 BS | 1094 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2650 |
| 2 | Denver International Airport |  | US | 2132 |
| 3 | Tokyo International Airport |  | JP | 1823 |
| 4 | Indira Gandhi International Airport |  | IN | 1647 |
| 5 | Harry Reid International Airport |  | US | 1581 |
| 6 | Guaymaral Airport |  | CO | 1533 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1506 |
| 8 | Zurich Airport |  | CH | 1392 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1349 |
| 10 | La Aurora Airport |  | GT | 1344 |
| 11 | Frankfurt am Main International Airport |  | DE | 1302 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1236 |
| 13 | Chicago O'Hare International Airport |  | US | 1221 |
| 14 | Macau International Airport |  | MO | 1182 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1115 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1049 |
| 19 | Madrid Barajas International Airport |  | ES | 1041 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1032 |
| 21 | Kuala Lumpur International Airport |  | MY | 1003 |
| 22 | Congonhas Airport |  | BR | 992 |
| 23 | Charlotte/Douglas International Airport |  | US | 951 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 924 |
| 25 | Charles de Gaulle International Airport |  | FR | 917 |
| 26 | Bengaluru International Airport |  | IN | 905 |
| 27 | Malpensa International Airport |  | IT | 865 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 845 |
| 29 | Ninoy Aquino International Airport |  | PH | 827 |
| 30 | Daniel K Inouye International Airport |  | US | 804 |
| 31 | Barcelona International Airport |  | ES | 790 |
| 32 | Tenerife Norte Airport |  | ES | 774 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 768 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 742 |
| 35 | Calgary International Airport |  | CA | 739 |
| 36 | Seattle-Tacoma International Airport |  | US | 732 |
| 37 | Scottsdale Airport |  | US | 731 |
| 38 | Vitoria/Foronda Airport |  | ES | 724 |
| 39 | Viracopos International Airport |  | BR | 721 |
| 40 | Amsterdam Airport Schiphol |  | NL | 718 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 639 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 459 | 21m | 244 km | 1,932.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 325 | 24m | 225 km | 1,260.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 317 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 303 | 1h 10m | 770 km | 4,025.1 t |
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
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 160 | 31m | 369 km | 1,018.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 147 | 1h 1m | 695 km | 1,762.1 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 147 | 30m | 49 km | 124.3 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 146 | 1h 17m | 961 km | 2,420.0 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFBLU | CFB | John C. Munro Hamilton International Airport (CYHM) | CPC2 (CPC2) | 2026-07-01 23:16 UTC | 2026-07-02 00:06 UTC | 49m |
| N572CW |  | Livingston County/Spencer J Hardy Airport (KOZW) | Livingston County/Spencer J Hardy Airport (KOZW) | 2026-07-01 23:07 UTC | 2026-07-02 00:05 UTC | 58m |
| DAL411 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Doig Airport (CFX3) | 2026-07-01 21:19 UTC | 2026-07-02 00:05 UTC | 2h 46m |
| N56488 |  | Pensacola International Airport (KPNS) | Mc Kinnon Airpark (48FL) | 2026-07-01 23:37 UTC | 2026-07-01 23:57 UTC | 19m |
| ZKTAS | ZKT | Ardmore Airport (NZAR) | Mercer1 PDZ Airport (NZME) | 2026-07-01 23:42 UTC | 2026-07-01 23:56 UTC | 14m |
| VILLN51 | VIL | Hill Afb Airport (KHIF) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-07-01 23:23 UTC | 2026-07-01 23:55 UTC | 32m |
| PGT1574 | PGT | Antalya International Airport (LTAI) | EPMX (EPMX) | 2026-07-01 21:33 UTC | 2026-07-01 23:54 UTC | 2h 21m |
| N500KB |  | Frederick Municipal Airport (KFDK) | Ocean City Municipal Airport (KOXB) | 2026-07-01 23:13 UTC | 2026-07-01 23:54 UTC | 40m |
| TKR105 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-07-01 23:16 UTC | 2026-07-01 23:51 UTC | 35m |
| RJA612N | Royal Jordanian | Queen Alia International Airport (OJAI) | Dubai International Airport (OMDB) | 2026-07-01 21:18 UTC | 2026-07-01 23:46 UTC | 2h 28m |
| N48LF |  | Newton Municipal-Earl Johnson Field (KTNU) | Newton Municipal-Earl Johnson Field (KTNU) | 2026-07-01 23:27 UTC | 2026-07-01 23:44 UTC | 16m |
| QLK203D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Albury Airport (YMAY) | 2026-07-01 22:44 UTC | 2026-07-01 23:43 UTC | 58m |
| N99253 |  | Crow Island Airport (8MA4) | Sids Airport (MA52) | 2026-07-01 23:27 UTC | 2026-07-01 23:39 UTC | 12m |
| JBU400 | JetBlue | Louis Armstrong New Orleans International Airport (KMSY) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-01 20:31 UTC | 2026-07-01 23:39 UTC | 3h 7m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-07-01 23:06 UTC | 2026-07-01 23:37 UTC | 30m |
| PREY21 | PRE | Randolph Afb Airport (KRND) | Bailey Airport (2TS8) | 2026-07-01 23:10 UTC | 2026-07-01 23:36 UTC | 25m |
| N345P |  | Ames Municipal Airport (KAMW) | OMU9 (OMU9) | 2026-07-01 22:39 UTC | 2026-07-01 23:31 UTC | 51m |
| N9740W |  | Yates Airport (IL29) | Mussman Airport (7IL0) | 2026-07-01 23:27 UTC | 2026-07-01 23:28 UTC | 1m |
| CXK153 | CXK | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-07-01 23:22 UTC | 2026-07-01 23:26 UTC | 4m |
| N812VA |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Reed Mine Airport (5NC3) | 2026-07-01 22:27 UTC | 2026-07-01 23:25 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
