# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_10:05:09_UTC-green)

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

**Latest saved flight:** 2026-07-25 10:05:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 10:05:09 UTC

- **149,663** saved flights
- **49,858** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **149,663** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,791,289.0 tonnes** estimated CO2 emissions
- **103,842,840 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6038 |
| 2 | SkyWest Airlines | 5479 |
| 3 | EJA | 2966 |
| 4 | IndiGo | 2675 |
| 5 | American Airlines | 2380 |
| 6 | Southwest Airlines | 2272 |
| 7 | ENY | 1863 |
| 8 | Delta Air Lines | 1764 |
| 9 | Lufthansa | 1462 |
| 10 | LATAM Airlines | 1377 |
| 11 | AZU | 1292 |
| 12 | WIF | 1271 |
| 13 | Vueling | 1262 |
| 14 | LXJ | 1153 |
| 15 | AXM | 1079 |
| 16 | Swiss International | 1054 |
| 17 | easyJet | 969 |
| 18 | All Nippon Airways | 950 |
| 19 | Alaska Airlines | 936 |
| 20 | QLK | 931 |
| 21 | EJU | 913 |
| 22 | VIV | 825 |
| 23 | CXK | 799 |
| 24 | AEE | 787 |
| 25 | Cathay Pacific | 781 |
| 26 | JetBlue | 781 |
| 27 | Air France | 780 |
| 28 | MXY | 779 |
| 29 | GLO | 773 |
| 30 | United Airlines | 771 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129165 |
| 2 | 🇪🇸 ES | 9653 |
| 3 | 🇦🇺 AU | 8503 |
| 4 | 🇧🇷 BR | 8431 |
| 5 | 🇮🇳 IN | 8423 |
| 6 | 🇨🇦 CA | 8025 |
| 7 | 🇮🇹 IT | 7725 |
| 8 | 🇩🇪 DE | 7644 |
| 9 | 🇬🇧 GB | 6844 |
| 10 | 🇯🇵 JP | 6227 |
| 11 | 🇫🇷 FR | 5918 |
| 12 | 🇨🇴 CO | 5039 |
| 13 | 🇲🇽 MX | 4332 |
| 14 | 🇬🇷 GR | 4238 |
| 15 | 🇳🇴 NO | 3982 |
| 16 | 🇨🇭 CH | 3926 |
| 17 | 🇹🇷 TR | 3529 |
| 18 | 🇲🇾 MY | 2807 |
| 19 | 🇵🇱 PL | 2526 |
| 20 | 🇿🇦 ZA | 2430 |
| 21 | 🇳🇿 NZ | 2261 |
| 22 | 🇹🇭 TH | 2186 |
| 23 | 🇰🇷 KR | 2063 |
| 24 | 🇵🇭 PH | 2001 |
| 25 | 🇬🇹 GT | 1949 |
| 26 | 🇲🇦 MA | 1524 |
| 27 | 🇲🇪 ME | 1473 |
| 28 | 🇳🇱 NL | 1381 |
| 29 | 🇭🇷 HR | 1357 |
| 30 | 🇲🇴 MO | 1246 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3080 |
| 2 | Denver International Airport |  | US | 2514 |
| 3 | Tokyo International Airport |  | JP | 1986 |
| 4 | Indira Gandhi International Airport |  | IN | 1869 |
| 5 | Guaymaral Airport |  | CO | 1866 |
| 6 | Harry Reid International Airport |  | US | 1857 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1678 |
| 8 | Zurich Airport |  | CH | 1633 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1573 |
| 10 | La Aurora Airport |  | GT | 1509 |
| 11 | Frankfurt am Main International Airport |  | DE | 1411 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1405 |
| 13 | Chicago O'Hare International Airport |  | US | 1383 |
| 14 | Salt Lake City International Airport |  | US | 1348 |
| 15 | El Dorado International Airport |  | CO | 1343 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1285 |
| 17 | Macau International Airport |  | MO | 1246 |
| 18 | Congonhas Airport |  | BR | 1205 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1187 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1162 |
| 22 | Kuala Lumpur International Airport |  | MY | 1081 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1066 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1050 |
| 26 | Charles de Gaulle International Airport |  | FR | 1030 |
| 27 | Bengaluru International Airport |  | IN | 1007 |
| 28 | Malpensa International Airport |  | IT | 974 |
| 29 | Ninoy Aquino International Airport |  | PH | 937 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 909 |
| 31 | Barcelona International Airport |  | ES | 900 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 898 |
| 33 | Daniel K Inouye International Airport |  | US | 897 |
| 34 | Seattle-Tacoma International Airport |  | US | 861 |
| 35 | Tenerife Norte Airport |  | ES | 855 |
| 36 | Calgary International Airport |  | CA | 854 |
| 37 | Scottsdale Airport |  | US | 849 |
| 38 | Viracopos International Airport |  | BR | 844 |
| 39 | Amsterdam Airport Schiphol |  | NL | 831 |
| 40 | Oslo Gardermoen Airport |  | NO | 827 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 787 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 543 | 21m | 244 km | 2,286.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 349 | 1h 9m | 770 km | 4,636.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 272 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 267 | 27m | 275 km | 1,265.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 204 | 44m | 241 km | 847.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 200 | 1h 47m | 1,423 km | 4,908.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 184 | 20m | 250 km | 794.8 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 176 | 1h 16m | 961 km | 2,917.3 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 176 | 18m | 144 km | 437.8 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 169 | 1h 1m | 695 km | 2,025.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WMT8JT | WMT | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Francisco de Sá Carneiro Airport (LPPR) | 2026-07-25 07:22 UTC | 2026-07-25 10:05 UTC | 2h 42m |
| N106AN |  | Lashenden (Headcorn) Airfield (EGKH) | Lashenden (Headcorn) Airfield (EGKH) | 2026-07-25 09:34 UTC | 2026-07-25 10:01 UTC | 26m |
| DFLIP | DFL | Roudnice Mad Airport (LKRO) | Roudnice Mad Airport (LKRO) | 2026-07-25 09:40 UTC | 2026-07-25 09:59 UTC | 18m |
| EAI23C | EAI | Southampton Airport (EGHI) | Dublin Airport (EIDW) | 2026-07-25 08:34 UTC | 2026-07-25 09:56 UTC | 1h 21m |
| IBX65 | IBX | Matsumoto Airport (RJAF) | Hiroshima Airport (RJOA) | 2026-07-25 09:02 UTC | 2026-07-25 09:42 UTC | 40m |
| HST2356 | HST | Antalya International Airport (LTAI) | Kedainiai Air Base (EYKD) | 2026-07-25 07:05 UTC | 2026-07-25 09:42 UTC | 2h 37m |
| CONDR31 | CON | Getafe Air Base (LEGT) | La Morgal Airport (LEMR) | 2026-07-25 08:58 UTC | 2026-07-25 09:40 UTC | 41m |
| HBKBT | HBK | Langenthal Airport (LSPL) | Langenthal Airport (LSPL) | 2026-07-25 09:16 UTC | 2026-07-25 09:37 UTC | 21m |
| RSC83XR | RSC | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-07-25 09:26 UTC | 2026-07-25 09:37 UTC | 11m |
| DITFC | DIT | Stuttgart Airport (EDDS) | Samedan Airport (LSZS) | 2026-07-25 08:57 UTC | 2026-07-25 09:37 UTC | 39m |
| RYR9GA | Ryanair | London Stansted Airport (EGSS) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-25 07:36 UTC | 2026-07-25 09:35 UTC | 1h 58m |
| CPA254 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-07-24 21:39 UTC | 2026-07-25 09:35 UTC | 11h 55m |
| ASA1543 | Alaska Airlines | Ted Stevens Anchorage International Airport (PANC) | Fort St. John Airport (CYXJ) | 2026-07-25 07:25 UTC | 2026-07-25 09:34 UTC | 2h 9m |
| RGA17 | RGA | Reichenbach Air Base (LSGR) | Reichenbach Air Base (LSGR) | 2026-07-25 09:03 UTC | 2026-07-25 09:30 UTC | 26m |
| SKV111 | SKV | Toulon-Hyeres Airport (LFTH) | Otocac Airport (LDRO) | 2026-07-25 08:36 UTC | 2026-07-25 09:29 UTC | 53m |
| PGC69P | PGC | Wevelgem Airport (EBKT) | Raron Airport (LSTA) | 2026-07-25 07:48 UTC | 2026-07-25 09:29 UTC | 1h 41m |
| RYR3BU | Ryanair | Leeds Bradford Airport (EGNM) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-25 07:13 UTC | 2026-07-25 09:27 UTC | 2h 14m |
| LOT3HB | LOT Polish Airlines | Warsaw Chopin Airport (EPWA) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-25 08:50 UTC | 2026-07-25 09:27 UTC | 36m |
| RNA409 | RNA | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-07-25 05:31 UTC | 2026-07-25 09:25 UTC | 3h 54m |
| RYR91SK | Ryanair | Leeds Bradford Airport (EGNM) | Le Blanc Airport (LFEL) | 2026-07-25 08:10 UTC | 2026-07-25 09:25 UTC | 1h 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
