# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_16:19:55_UTC-green)

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

**Latest saved flight:** 2026-07-25 16:19:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 16:19:55 UTC

- **150,393** saved flights
- **50,042** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **150,393** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,799,453.0 tonnes** estimated CO2 emissions
- **104,316,117 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6067 |
| 2 | SkyWest Airlines | 5489 |
| 3 | EJA | 2975 |
| 4 | IndiGo | 2689 |
| 5 | American Airlines | 2386 |
| 6 | Southwest Airlines | 2277 |
| 7 | ENY | 1870 |
| 8 | Delta Air Lines | 1769 |
| 9 | Lufthansa | 1473 |
| 10 | LATAM Airlines | 1387 |
| 11 | AZU | 1302 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1268 |
| 14 | LXJ | 1158 |
| 15 | AXM | 1081 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 975 |
| 18 | All Nippon Airways | 952 |
| 19 | Alaska Airlines | 936 |
| 20 | QLK | 931 |
| 21 | EJU | 918 |
| 22 | VIV | 831 |
| 23 | CXK | 808 |
| 24 | AEE | 794 |
| 25 | MXY | 787 |
| 26 | Air France | 784 |
| 27 | JetBlue | 783 |
| 28 | Cathay Pacific | 781 |
| 29 | GLO | 781 |
| 30 | United Airlines | 772 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129582 |
| 2 | 🇪🇸 ES | 9723 |
| 3 | 🇧🇷 BR | 8505 |
| 4 | 🇦🇺 AU | 8505 |
| 5 | 🇮🇳 IN | 8466 |
| 6 | 🇨🇦 CA | 8040 |
| 7 | 🇮🇹 IT | 7777 |
| 8 | 🇩🇪 DE | 7719 |
| 9 | 🇬🇧 GB | 6889 |
| 10 | 🇯🇵 JP | 6249 |
| 11 | 🇫🇷 FR | 5961 |
| 12 | 🇨🇴 CO | 5089 |
| 13 | 🇲🇽 MX | 4345 |
| 14 | 🇬🇷 GR | 4280 |
| 15 | 🇳🇴 NO | 3998 |
| 16 | 🇨🇭 CH | 3965 |
| 17 | 🇹🇷 TR | 3557 |
| 18 | 🇲🇾 MY | 2817 |
| 19 | 🇵🇱 PL | 2558 |
| 20 | 🇿🇦 ZA | 2454 |
| 21 | 🇳🇿 NZ | 2265 |
| 22 | 🇹🇭 TH | 2192 |
| 23 | 🇰🇷 KR | 2065 |
| 24 | 🇵🇭 PH | 2005 |
| 25 | 🇬🇹 GT | 1965 |
| 26 | 🇲🇦 MA | 1531 |
| 27 | 🇲🇪 ME | 1479 |
| 28 | 🇳🇱 NL | 1388 |
| 29 | 🇭🇷 HR | 1371 |
| 30 | 🇲🇴 MO | 1248 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3090 |
| 2 | Denver International Airport |  | US | 2519 |
| 3 | Tokyo International Airport |  | JP | 1993 |
| 4 | Guaymaral Airport |  | CO | 1884 |
| 5 | Indira Gandhi International Airport |  | IN | 1876 |
| 6 | Harry Reid International Airport |  | US | 1859 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1693 |
| 8 | Zurich Airport |  | CH | 1644 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1577 |
| 10 | La Aurora Airport |  | GT | 1521 |
| 11 | Frankfurt am Main International Airport |  | DE | 1422 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1407 |
| 13 | Chicago O'Hare International Airport |  | US | 1385 |
| 14 | El Dorado International Airport |  | CO | 1350 |
| 15 | Salt Lake City International Airport |  | US | 1349 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1288 |
| 17 | Macau International Airport |  | MO | 1248 |
| 18 | Congonhas Airport |  | BR | 1217 |
| 19 | Madrid Barajas International Airport |  | ES | 1197 |
| 20 | Capua Airport |  | IT | 1196 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1164 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1076 |
| 24 | Charlotte/Douglas International Airport |  | US | 1069 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1057 |
| 26 | Charles de Gaulle International Airport |  | FR | 1034 |
| 27 | Bengaluru International Airport |  | IN | 1010 |
| 28 | Malpensa International Airport |  | IT | 982 |
| 29 | Ninoy Aquino International Airport |  | PH | 939 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 912 |
| 31 | Barcelona International Airport |  | ES | 903 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 899 |
| 33 | Daniel K Inouye International Airport |  | US | 898 |
| 34 | Tenerife Norte Airport |  | ES | 863 |
| 35 | Seattle-Tacoma International Airport |  | US | 861 |
| 36 | Calgary International Airport |  | CA | 855 |
| 37 | Viracopos International Airport |  | BR | 851 |
| 38 | Scottsdale Airport |  | US | 851 |
| 39 | Amsterdam Airport Schiphol |  | NL | 834 |
| 40 | Oslo Gardermoen Airport |  | NO | 828 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 795 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 544 | 21m | 244 km | 2,290.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 366 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 364 | 24m | 225 km | 1,412.1 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 269 | 27m | 275 km | 1,274.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 224 | 22m | 55 km | 212.9 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 201 | 1h 47m | 1,423 km | 4,932.9 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 188 | 20m | 250 km | 812.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 177 | 1h 16m | 961 km | 2,933.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 177 | 18m | 144 km | 440.3 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 173 | 44m | 452 km | 1,348.3 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 169 | 1h 39m | 1,156 km | 3,371.5 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6937T |  | Four Pillars Airport (AZ21) | Benson Airport (31AZ) | 2026-07-25 16:04 UTC | 2026-07-25 16:19 UTC | 15m |
| N199SP |  | Chicago Executive Airport (KPWK) | Lake In The Hills Airport (K3CK) | 2026-07-25 15:53 UTC | 2026-07-25 16:18 UTC | 24m |
| RVP953 | RVP | Cascais Airport (LPCS) | Portimão Airport (LPPM) | 2026-07-25 15:37 UTC | 2026-07-25 16:13 UTC | 35m |
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-07-25 15:52 UTC | 2026-07-25 16:10 UTC | 17m |
| N890MP |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-25 15:34 UTC | 2026-07-25 16:10 UTC | 35m |
| LHX076 | LHX | Frankfurt am Main International Airport (EDDF) | Werdohl-Kuntrop Airport (EDKW) | 2026-07-25 15:27 UTC | 2026-07-25 16:03 UTC | 35m |
| N567JW |  | City Of Colorado Springs Municipal Airport (KCOS) | Limon Municipal Airport (KLIC) | 2026-07-25 15:35 UTC | 2026-07-25 16:03 UTC | 28m |
| N52789 |  | Oakland San Francisco Bay Airport (KOAK) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-25 15:42 UTC | 2026-07-25 16:02 UTC | 19m |
| N6393E |  | Northern Colorado Regional Airport (KFNL) | Laramie Regional Airport (KLAR) | 2026-07-25 15:16 UTC | 2026-07-25 16:02 UTC | 45m |
| JZA365 | JZA | Vancouver International Airport (CYVR) | Dawson Creek (Flying L Ranch) Airport (CDC3) | 2026-07-25 14:44 UTC | 2026-07-25 16:01 UTC | 1h 17m |
| OAR5IS | OAR | La Axarquia-Leoni Benabu Airport (LEAX) | La Axarquia-Leoni Benabu Airport (LEAX) | 2026-07-25 15:40 UTC | 2026-07-25 15:59 UTC | 18m |
| ICG35 | ICG | Sandskeid Airport (BISS) | Reykjavik Airport (BIRK) | 2026-07-25 15:51 UTC | 2026-07-25 15:58 UTC | 7m |
| HBZEA | HBZ | Locarno Airport (LSZL) | Lodrino Air Base (LSML) | 2026-07-25 15:54 UTC | 2026-07-25 15:58 UTC | 4m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-07-25 15:38 UTC | 2026-07-25 15:57 UTC | 18m |
| ERU16 | ERU | Robin Airport (59AZ) | Pilots Rest Airport (AZ57) | 2026-07-25 15:34 UTC | 2026-07-25 15:55 UTC | 20m |
| N611MV |  | Mc Clellan Airfield (KMCC) | Lee Vining Airport (KO24) | 2026-07-25 15:23 UTC | 2026-07-25 15:54 UTC | 30m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-25 15:20 UTC | 2026-07-25 15:53 UTC | 33m |
| WLDLD28 | WLD | Centennial Airport (KAPA) | 6CO0 (6CO0) | 2026-07-25 14:29 UTC | 2026-07-25 15:53 UTC | 1h 24m |
| CAP3074 | CAP | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-07-25 14:55 UTC | 2026-07-25 15:52 UTC | 57m |
| N667LF |  | Boise Air Trml/Gowen Field (KBOI) | 83OR (83OR) | 2026-07-25 15:11 UTC | 2026-07-25 15:51 UTC | 40m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
