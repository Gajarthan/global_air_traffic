# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_17:52:59_UTC-green)

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

**Latest saved flight:** 2026-07-31 17:52:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 17:52:59 UTC

- **162,915** saved flights
- **53,685** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **162,915** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,954,077.9 tonnes** estimated CO2 emissions
- **113,279,880 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6503 |
| 2 | SkyWest Airlines | 5928 |
| 3 | EJA | 3227 |
| 4 | IndiGo | 2859 |
| 5 | American Airlines | 2565 |
| 6 | Southwest Airlines | 2548 |
| 7 | ENY | 2025 |
| 8 | Delta Air Lines | 1938 |
| 9 | Lufthansa | 1529 |
| 10 | LATAM Airlines | 1528 |
| 11 | AZU | 1429 |
| 12 | WIF | 1373 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1266 |
| 15 | AXM | 1131 |
| 16 | Swiss International | 1122 |
| 17 | easyJet | 1071 |
| 18 | Alaska Airlines | 1008 |
| 19 | QLK | 1003 |
| 20 | EJU | 1000 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 897 |
| 23 | CXK | 872 |
| 24 | Cathay Pacific | 857 |
| 25 | United Airlines | 857 |
| 26 | GLO | 854 |
| 27 | AEE | 851 |
| 28 | Air France | 844 |
| 29 | MXY | 841 |
| 30 | JetBlue | 829 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 140670 |
| 2 | 🇪🇸 ES | 10438 |
| 3 | 🇧🇷 BR | 9298 |
| 4 | 🇦🇺 AU | 9202 |
| 5 | 🇮🇳 IN | 8985 |
| 6 | 🇨🇦 CA | 8856 |
| 7 | 🇮🇹 IT | 8387 |
| 8 | 🇩🇪 DE | 8200 |
| 9 | 🇬🇧 GB | 7493 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6450 |
| 12 | 🇨🇴 CO | 5811 |
| 13 | 🇬🇷 GR | 4677 |
| 14 | 🇲🇽 MX | 4671 |
| 15 | 🇳🇴 NO | 4297 |
| 16 | 🇨🇭 CH | 4284 |
| 17 | 🇹🇷 TR | 3894 |
| 18 | 🇲🇾 MY | 2938 |
| 19 | 🇵🇱 PL | 2769 |
| 20 | 🇿🇦 ZA | 2653 |
| 21 | 🇳🇿 NZ | 2383 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2100 |
| 26 | 🇲🇦 MA | 1641 |
| 27 | 🇲🇪 ME | 1534 |
| 28 | 🇭🇷 HR | 1530 |
| 29 | 🇳🇱 NL | 1486 |
| 30 | 🇲🇴 MO | 1363 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3321 |
| 2 | Denver International Airport |  | US | 2703 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2053 |
| 5 | Indira Gandhi International Airport |  | IN | 1996 |
| 6 | Harry Reid International Airport |  | US | 1971 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1793 |
| 8 | Zurich Airport |  | CH | 1742 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1712 |
| 10 | La Aurora Airport |  | GT | 1628 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1511 |
| 12 | El Dorado International Airport |  | CO | 1487 |
| 13 | Frankfurt am Main International Airport |  | DE | 1484 |
| 14 | Chicago O'Hare International Airport |  | US | 1472 |
| 15 | Salt Lake City International Airport |  | US | 1462 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1366 |
| 17 | Macau International Airport |  | MO | 1363 |
| 18 | Congonhas Airport |  | BR | 1350 |
| 19 | Madrid Barajas International Airport |  | ES | 1284 |
| 20 | Capua Airport |  | IT | 1278 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1243 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1154 |
| 24 | Charlotte/Douglas International Airport |  | US | 1142 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1112 |
| 27 | Malpensa International Airport |  | IT | 1075 |
| 28 | Bengaluru International Airport |  | IN | 1065 |
| 29 | Ninoy Aquino International Airport |  | PH | 1002 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 998 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 988 |
| 32 | Barcelona International Airport |  | ES | 964 |
| 33 | Daniel K Inouye International Airport |  | US | 955 |
| 34 | Seattle-Tacoma International Airport |  | US | 943 |
| 35 | Calgary International Airport |  | CA | 928 |
| 36 | Viracopos International Airport |  | BR | 926 |
| 37 | Tenerife Norte Airport |  | ES | 912 |
| 38 | Scottsdale Airport |  | US | 912 |
| 39 | Oslo Gardermoen Airport |  | NO | 909 |
| 40 | Reno/Tahoe International Airport |  | US | 892 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 860 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 593 | 21m | 244 km | 2,497.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 389 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 302 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 241 | 22m | 55 km | 229.1 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 236 | 44m | 241 km | 980.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 224 | 1h 47m | 1,423 km | 5,497.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 208 | 20m | 250 km | 898.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 206 | 20m | 99 km | 352.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 199 | 31m | 49 km | 168.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 195 | 28m | 152 km | 509.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 194 | 1h 15m | 961 km | 3,215.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 192 | 18m | 144 km | 477.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 174 | 1h 49m | 1,304 km | 3,914.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N124JW |  | Cobb County International/Mccollum Field (KRYY) | Paulding Northwest Atlanta Airport (KPUJ) | 2026-07-31 16:49 UTC | 2026-07-31 17:52 UTC | 1h 3m |
| TIGER42 | TIG | 2TX3 (2TX3) | Laughlin Afb Aux Nr 1 Airport (KT70) | 2026-07-31 17:38 UTC | 2026-07-31 17:49 UTC | 11m |
| N705CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-07-31 17:24 UTC | 2026-07-31 17:44 UTC | 20m |
| N268Z |  | Palo Alto Airport (KPAO) | Hayward Executive Airport (KHWD) | 2026-07-31 17:20 UTC | 2026-07-31 17:40 UTC | 19m |
| SGA2561 | SGA | Al Maktoum International Airport (OMDW) | Macau International Airport (VMMC) | 2026-07-31 09:44 UTC | 2026-07-31 17:40 UTC | 7h 55m |
| CXK490 | CXK | Sacramento Executive Airport (KSAC) | Sacramento Mather Airport (KMHR) | 2026-07-31 17:25 UTC | 2026-07-31 17:38 UTC | 13m |
| N4000K |  | Gerald R Ford International Airport (KGRR) | Iowa City Municipal Airport (KIOW) | 2026-07-31 16:42 UTC | 2026-07-31 17:36 UTC | 53m |
| N749DS |  | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-07-31 17:12 UTC | 2026-07-31 17:32 UTC | 19m |
| LTA443 | LTA | Columbia Metro Airport (KCAE) | The Farm Airport (24SC) | 2026-07-31 16:25 UTC | 2026-07-31 17:27 UTC | 1h 1m |
| TGLOP | TGL | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-07-31 17:04 UTC | 2026-07-31 17:27 UTC | 23m |
| BOE467 | BOE | Boeing Field/King County International Airport (KBFI) | Franz Ranch Airport (33WA) | 2026-07-31 16:03 UTC | 2026-07-31 17:26 UTC | 1h 22m |
| NASA520 | NAS | Boise Air Trml/Gowen Field (KBOI) | Juntura Airport (OR14) | 2026-07-31 16:54 UTC | 2026-07-31 17:25 UTC | 31m |
| N225N |  | Boeing Field/King County International Airport (KBFI) | Eck Field (SN64) | 2026-07-31 14:30 UTC | 2026-07-31 17:24 UTC | 2h 53m |
| BRG621 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-07-31 16:40 UTC | 2026-07-31 17:24 UTC | 43m |
| N759XT |  | Oakland County International Airport (KPTK) | Rainbow Airport (WI37) | 2026-07-31 15:55 UTC | 2026-07-31 17:24 UTC | 1h 28m |
| N303JD |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-07-31 16:45 UTC | 2026-07-31 17:23 UTC | 38m |
| HK3544G |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-07-31 16:58 UTC | 2026-07-31 17:23 UTC | 25m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-31 16:26 UTC | 2026-07-31 17:22 UTC | 55m |
| NWX333 | NWX | Aero Valley Airport (K52F) | Bridgeport Municipal Airport (KXBP) | 2026-07-31 16:42 UTC | 2026-07-31 17:22 UTC | 39m |
| CXK654 | CXK | Montgomery-Gibbs Executive Airport (KMYF) | Riverside Airport (KRAL) | 2026-07-31 16:33 UTC | 2026-07-31 17:21 UTC | 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
