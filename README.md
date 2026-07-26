# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_17:32:39_UTC-green)

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

**Latest saved flight:** 2026-07-26 17:32:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 17:32:39 UTC

- **152,600** saved flights
- **50,628** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **152,600** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,825,682.3 tonnes** estimated CO2 emissions
- **105,836,656 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6166 |
| 2 | SkyWest Airlines | 5574 |
| 3 | EJA | 3017 |
| 4 | IndiGo | 2727 |
| 5 | American Airlines | 2416 |
| 6 | Southwest Airlines | 2320 |
| 7 | ENY | 1903 |
| 8 | Delta Air Lines | 1784 |
| 9 | Lufthansa | 1487 |
| 10 | LATAM Airlines | 1413 |
| 11 | AZU | 1326 |
| 12 | WIF | 1287 |
| 13 | Vueling | 1276 |
| 14 | LXJ | 1174 |
| 15 | AXM | 1090 |
| 16 | Swiss International | 1071 |
| 17 | easyJet | 996 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 950 |
| 20 | QLK | 941 |
| 21 | EJU | 939 |
| 22 | VIV | 842 |
| 23 | CXK | 813 |
| 24 | AEE | 804 |
| 25 | MXY | 802 |
| 26 | Air France | 796 |
| 27 | GLO | 795 |
| 28 | JetBlue | 790 |
| 29 | Cathay Pacific | 784 |
| 30 | United Airlines | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 131443 |
| 2 | 🇪🇸 ES | 9881 |
| 3 | 🇧🇷 BR | 8664 |
| 4 | 🇦🇺 AU | 8597 |
| 5 | 🇮🇳 IN | 8572 |
| 6 | 🇨🇦 CA | 8125 |
| 7 | 🇮🇹 IT | 7909 |
| 8 | 🇩🇪 DE | 7815 |
| 9 | 🇬🇧 GB | 7002 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6052 |
| 12 | 🇨🇴 CO | 5209 |
| 13 | 🇲🇽 MX | 4399 |
| 14 | 🇬🇷 GR | 4355 |
| 15 | 🇳🇴 NO | 4041 |
| 16 | 🇨🇭 CH | 4015 |
| 17 | 🇹🇷 TR | 3646 |
| 18 | 🇲🇾 MY | 2838 |
| 19 | 🇵🇱 PL | 2620 |
| 20 | 🇿🇦 ZA | 2483 |
| 21 | 🇳🇿 NZ | 2289 |
| 22 | 🇹🇭 TH | 2220 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2025 |
| 25 | 🇬🇹 GT | 1986 |
| 26 | 🇲🇦 MA | 1552 |
| 27 | 🇲🇪 ME | 1490 |
| 28 | 🇭🇷 HR | 1405 |
| 29 | 🇳🇱 NL | 1402 |
| 30 | 🇲🇴 MO | 1254 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3144 |
| 2 | Denver International Airport |  | US | 2556 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1919 |
| 5 | Indira Gandhi International Airport |  | IN | 1902 |
| 6 | Harry Reid International Airport |  | US | 1875 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1712 |
| 8 | Zurich Airport |  | CH | 1663 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1590 |
| 10 | La Aurora Airport |  | GT | 1538 |
| 11 | Frankfurt am Main International Airport |  | DE | 1437 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1422 |
| 13 | Chicago O'Hare International Airport |  | US | 1400 |
| 14 | El Dorado International Airport |  | CO | 1373 |
| 15 | Salt Lake City International Airport |  | US | 1371 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1297 |
| 17 | Macau International Airport |  | MO | 1254 |
| 18 | Congonhas Airport |  | BR | 1239 |
| 19 | Madrid Barajas International Airport |  | ES | 1219 |
| 20 | Capua Airport |  | IT | 1211 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1180 |
| 22 | Kuala Lumpur International Airport |  | MY | 1091 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1084 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1075 |
| 26 | Charles de Gaulle International Airport |  | FR | 1049 |
| 27 | Bengaluru International Airport |  | IN | 1025 |
| 28 | Malpensa International Airport |  | IT | 1001 |
| 29 | Ninoy Aquino International Airport |  | PH | 948 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 924 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 912 |
| 32 | Barcelona International Airport |  | ES | 910 |
| 33 | Daniel K Inouye International Airport |  | US | 909 |
| 34 | Tenerife Norte Airport |  | ES | 879 |
| 35 | Seattle-Tacoma International Airport |  | US | 877 |
| 36 | Viracopos International Airport |  | BR | 864 |
| 37 | Calgary International Airport |  | CA | 863 |
| 38 | Scottsdale Airport |  | US | 863 |
| 39 | Amsterdam Airport Schiphol |  | NL | 845 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 839 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 808 | 24m | - | - |
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
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 207 | 44m | 241 km | 859.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 206 | 1h 47m | 1,423 km | 5,055.6 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 202 | 26m | 215 km | 748.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 199 | 20m | 99 km | 340.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 197 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 185 | 30m | 49 km | 156.4 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 185 | 27m | 152 km | 483.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 179 | 18m | 144 km | 445.3 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 171 | 1h 1m | 695 km | 2,049.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 169 | 51m | 556 km | 1,620.0 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JIA5080 | JIA | Parker Field (AL18) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-07-26 15:56 UTC | 2026-07-26 17:32 UTC | 1h 36m |
| BBG701 | BBG | Eleftherios Venizelos International Airport (LGAV) | Ben Gurion International Airport (LLBG) | 2026-07-26 15:44 UTC | 2026-07-26 17:27 UTC | 1h 42m |
| N897CH |  | Orlando Sanford International Airport (KSFB) | Sylvester Airport (KSYV) | 2026-07-26 16:32 UTC | 2026-07-26 17:26 UTC | 53m |
| N5585 |  | General Mitchell International Airport (KMKE) | Smith County Airport (MS39) | 2026-07-26 15:52 UTC | 2026-07-26 17:18 UTC | 1h 26m |
| BNO91J | BNO | Oslo Gardermoen Airport (ENGM) | Kristiansand Airport (ENCN) | 2026-07-26 16:45 UTC | 2026-07-26 17:16 UTC | 30m |
| OKFUG03 | OKF | Liberec Airport (LKLB) | Liberec Airport (LKLB) | 2026-07-26 17:04 UTC | 2026-07-26 17:15 UTC | 11m |
| N234GC |  | French Valley Airport (KF70) | 8CA5 (8CA5) | 2026-07-26 16:46 UTC | 2026-07-26 17:10 UTC | 24m |
| N582BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-07-26 16:56 UTC | 2026-07-26 17:02 UTC | 6m |
| EJA917 | EJA | Indianapolis Executive Airport (KTYQ) | Dubuque Regional Airport (KDBQ) | 2026-07-26 16:08 UTC | 2026-07-26 17:02 UTC | 54m |
| N714JB |  | Queen Beatrix International Airport (TNCA) | Pilots Ridge Airport (03NC) | 2026-07-26 13:46 UTC | 2026-07-26 17:00 UTC | 3h 14m |
| CNS422 | CNS | Cape Cod Gateway Airport (KHYA) | Millinocket Municipal Airport (KMLT) | 2026-07-26 16:14 UTC | 2026-07-26 16:59 UTC | 45m |
| N27WA |  | John F Kennedy International Airport (KJFK) | Laguardia Airport (KLGA) | 2026-07-26 16:16 UTC | 2026-07-26 16:58 UTC | 42m |
| N3859V |  | 89LL (89LL) | Mussman Airport (7IL0) | 2026-07-26 16:19 UTC | 2026-07-26 16:57 UTC | 37m |
| AAL1618 | American Airlines | Ronald Reagan Washington Ntl Airport (KDCA) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-26 14:23 UTC | 2026-07-26 16:54 UTC | 2h 31m |
| N619AG |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-07-26 16:11 UTC | 2026-07-26 16:54 UTC | 42m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-26 16:31 UTC | 2026-07-26 16:51 UTC | 19m |
| N100BW |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-26 16:20 UTC | 2026-07-26 16:51 UTC | 30m |
| EJA882 | EJA | Chicago Executive Airport (KPWK) | Anderson Field (KS97) | 2026-07-26 13:18 UTC | 2026-07-26 16:50 UTC | 3h 32m |
| N972FB |  | Scottsdale Airport (KSDL) | Kanab Municipal Airport (KKNB) | 2026-07-26 16:15 UTC | 2026-07-26 16:50 UTC | 34m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-26 16:13 UTC | 2026-07-26 16:48 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
