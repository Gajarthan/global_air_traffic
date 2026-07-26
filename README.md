# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_18:30:07_UTC-green)

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

**Latest saved flight:** 2026-07-26 18:30:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 18:30:07 UTC

- **152,795** saved flights
- **50,676** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **152,795** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,828,120.6 tonnes** estimated CO2 emissions
- **105,978,008 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6173 |
| 2 | SkyWest Airlines | 5582 |
| 3 | EJA | 3024 |
| 4 | IndiGo | 2729 |
| 5 | American Airlines | 2422 |
| 6 | Southwest Airlines | 2323 |
| 7 | ENY | 1907 |
| 8 | Delta Air Lines | 1788 |
| 9 | Lufthansa | 1487 |
| 10 | LATAM Airlines | 1416 |
| 11 | AZU | 1329 |
| 12 | WIF | 1288 |
| 13 | Vueling | 1278 |
| 14 | LXJ | 1176 |
| 15 | AXM | 1090 |
| 16 | Swiss International | 1072 |
| 17 | easyJet | 997 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 950 |
| 20 | QLK | 941 |
| 21 | EJU | 940 |
| 22 | VIV | 843 |
| 23 | CXK | 816 |
| 24 | AEE | 805 |
| 25 | MXY | 804 |
| 26 | Air France | 797 |
| 27 | GLO | 796 |
| 28 | JetBlue | 793 |
| 29 | Cathay Pacific | 784 |
| 30 | United Airlines | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 131651 |
| 2 | 🇪🇸 ES | 9892 |
| 3 | 🇧🇷 BR | 8677 |
| 4 | 🇦🇺 AU | 8597 |
| 5 | 🇮🇳 IN | 8577 |
| 6 | 🇨🇦 CA | 8146 |
| 7 | 🇮🇹 IT | 7916 |
| 8 | 🇩🇪 DE | 7818 |
| 9 | 🇬🇧 GB | 7008 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6060 |
| 12 | 🇨🇴 CO | 5223 |
| 13 | 🇲🇽 MX | 4407 |
| 14 | 🇬🇷 GR | 4359 |
| 15 | 🇳🇴 NO | 4044 |
| 16 | 🇨🇭 CH | 4020 |
| 17 | 🇹🇷 TR | 3654 |
| 18 | 🇲🇾 MY | 2838 |
| 19 | 🇵🇱 PL | 2621 |
| 20 | 🇿🇦 ZA | 2483 |
| 21 | 🇳🇿 NZ | 2289 |
| 22 | 🇹🇭 TH | 2221 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2025 |
| 25 | 🇬🇹 GT | 1989 |
| 26 | 🇲🇦 MA | 1557 |
| 27 | 🇲🇪 ME | 1492 |
| 28 | 🇭🇷 HR | 1406 |
| 29 | 🇳🇱 NL | 1403 |
| 30 | 🇲🇴 MO | 1254 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3150 |
| 2 | Denver International Airport |  | US | 2557 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1922 |
| 5 | Indira Gandhi International Airport |  | IN | 1904 |
| 6 | Harry Reid International Airport |  | US | 1877 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1713 |
| 8 | Zurich Airport |  | CH | 1667 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1595 |
| 10 | La Aurora Airport |  | GT | 1541 |
| 11 | Frankfurt am Main International Airport |  | DE | 1437 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1426 |
| 13 | Chicago O'Hare International Airport |  | US | 1400 |
| 14 | El Dorado International Airport |  | CO | 1376 |
| 15 | Salt Lake City International Airport |  | US | 1374 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1299 |
| 17 | Macau International Airport |  | MO | 1254 |
| 18 | Congonhas Airport |  | BR | 1240 |
| 19 | Madrid Barajas International Airport |  | ES | 1220 |
| 20 | Capua Airport |  | IT | 1212 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1182 |
| 22 | Kuala Lumpur International Airport |  | MY | 1091 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1084 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1079 |
| 26 | Charles de Gaulle International Airport |  | FR | 1050 |
| 27 | Bengaluru International Airport |  | IN | 1025 |
| 28 | Malpensa International Airport |  | IT | 1001 |
| 29 | Ninoy Aquino International Airport |  | PH | 948 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 925 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 914 |
| 32 | Barcelona International Airport |  | ES | 910 |
| 33 | Daniel K Inouye International Airport |  | US | 909 |
| 34 | Tenerife Norte Airport |  | ES | 883 |
| 35 | Seattle-Tacoma International Airport |  | US | 879 |
| 36 | Viracopos International Airport |  | BR | 865 |
| 37 | Calgary International Airport |  | CA | 865 |
| 38 | Scottsdale Airport |  | US | 864 |
| 39 | Amsterdam Airport Schiphol |  | NL | 846 |
| 40 | Oslo Gardermoen Airport |  | NO | 839 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 809 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 553 | 21m | 244 km | 2,328.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 370 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 368 | 24m | 225 km | 1,427.7 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 356 | 1h 9m | 770 km | 4,729.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 280 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 274 | 27m | 275 km | 1,298.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 207 | 44m | 241 km | 859.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 202 | 26m | 215 km | 748.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 199 | 20m | 99 km | 340.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 197 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 186 | 27m | 152 km | 486.1 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 185 | 30m | 49 km | 156.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 181 | 1h 15m | 961 km | 3,000.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 179 | 18m | 144 km | 445.3 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 171 | 1h 1m | 695 km | 2,049.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 170 | 51m | 556 km | 1,629.6 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N80616 |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-26 18:13 UTC | 2026-07-26 18:30 UTC | 16m |
| N947AF |  | Addison Airport (KADS) | Gainesville Municipal Airport (KGLE) | 2026-07-26 17:55 UTC | 2026-07-26 18:29 UTC | 34m |
| GFY1894 | GFY | Tacoma Narrows Airport (KTIW) | Tacoma Narrows Airport (KTIW) | 2026-07-26 17:44 UTC | 2026-07-26 18:28 UTC | 43m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-26 17:43 UTC | 2026-07-26 18:28 UTC | 45m |
| N87RM |  | Skydive New England Airport (ME64) | Skydive New England Airport (ME64) | 2026-07-26 18:15 UTC | 2026-07-26 18:27 UTC | 12m |
| AAL2317 | American Airlines | Los Angeles International Airport (KLAX) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-26 15:47 UTC | 2026-07-26 18:27 UTC | 2h 39m |
| N530JL |  | North Las Vegas Airport (KVGT) | Jean Airport (K0L7) | 2026-07-26 18:07 UTC | 2026-07-26 18:26 UTC | 19m |
| N468DC |  | Mc Clellan Airfield (KMCC) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-07-26 17:32 UTC | 2026-07-26 18:14 UTC | 42m |
| CAP2796 | CAP | Redding Regional Airport (KRDD) | Scott Valley Airport (KA30) | 2026-07-26 17:44 UTC | 2026-07-26 18:14 UTC | 29m |
| N102UC |  | Palo Alto Airport (KPAO) | Palo Alto Airport (KPAO) | 2026-07-26 17:23 UTC | 2026-07-26 18:12 UTC | 49m |
| CXK651 | CXK | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-26 17:07 UTC | 2026-07-26 18:11 UTC | 1h 4m |
| N44653 |  | Schenectady County Airport (KSCH) | Johnson Airport (NY50) | 2026-07-26 18:01 UTC | 2026-07-26 18:11 UTC | 9m |
| QXE2325 | QXE | Southfork Airport (23ID) | Seattle-Tacoma International Airport (KSEA) | 2026-07-26 16:54 UTC | 2026-07-26 18:05 UTC | 1h 11m |
| N5366X |  | Helio Airport (2AK7) | Castle Mountain Airstrip (48AK) | 2026-07-26 17:12 UTC | 2026-07-26 18:05 UTC | 52m |
| RFS716 | RFS | Auburn Municipal Airport (KS50) | Renton Municipal Airport (KRNT) | 2026-07-26 17:45 UTC | 2026-07-26 18:02 UTC | 17m |
| TWY652 | TWY | Nice-Cote d'Azur Airport (LFMN) | Bangor International Airport (KBGR) | 2026-07-26 10:24 UTC | 2026-07-26 18:01 UTC | 7h 37m |
| N73924 |  | Mc Ghee Tyson Airport (KTYS) | Riverside Airport (22GA) | 2026-07-26 16:31 UTC | 2026-07-26 18:00 UTC | 1h 28m |
| N614LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-26 17:38 UTC | 2026-07-26 18:00 UTC | 21m |
| CXK374 | CXK | Jim Sears Airport (3TA7) | Jim Sears Airport (3TA7) | 2026-07-26 17:59 UTC | 2026-07-26 17:59 UTC | 0m |
| WIF1VR | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-07-26 17:12 UTC | 2026-07-26 17:56 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
