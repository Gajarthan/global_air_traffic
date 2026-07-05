# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_04:11:07_UTC-green)

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

**Latest saved flight:** 2026-07-05 04:11:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 04:11:07 UTC

- **129,302** saved flights
- **43,989** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **129,302** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,561,575.4 tonnes** estimated CO2 emissions
- **90,526,108 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5253 |
| 2 | SkyWest Airlines | 4796 |
| 3 | EJA | 2529 |
| 4 | IndiGo | 2428 |
| 5 | American Airlines | 1997 |
| 6 | Southwest Airlines | 1948 |
| 7 | ENY | 1623 |
| 8 | Delta Air Lines | 1546 |
| 9 | Lufthansa | 1360 |
| 10 | LATAM Airlines | 1176 |
| 11 | Vueling | 1147 |
| 12 | WIF | 1133 |
| 13 | AZU | 1098 |
| 14 | AXM | 1005 |
| 15 | LXJ | 999 |
| 16 | Swiss International | 899 |
| 17 | All Nippon Airways | 859 |
| 18 | Alaska Airlines | 834 |
| 19 | easyJet | 828 |
| 20 | QLK | 810 |
| 21 | EJU | 801 |
| 22 | VIV | 715 |
| 23 | Cathay Pacific | 713 |
| 24 | AEE | 706 |
| 25 | Air France | 703 |
| 26 | CXK | 694 |
| 27 | United Airlines | 690 |
| 28 | MXY | 677 |
| 29 | JetBlue | 673 |
| 30 | GLO | 657 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110675 |
| 2 | 🇪🇸 ES | 8616 |
| 3 | 🇮🇳 IN | 7614 |
| 4 | 🇦🇺 AU | 7495 |
| 5 | 🇧🇷 BR | 7254 |
| 6 | 🇨🇦 CA | 6813 |
| 7 | 🇩🇪 DE | 6794 |
| 8 | 🇮🇹 IT | 6767 |
| 9 | 🇬🇧 GB | 5736 |
| 10 | 🇯🇵 JP | 5617 |
| 11 | 🇫🇷 FR | 5127 |
| 12 | 🇨🇴 CO | 4086 |
| 13 | 🇲🇽 MX | 3773 |
| 14 | 🇬🇷 GR | 3684 |
| 15 | 🇳🇴 NO | 3522 |
| 16 | 🇨🇭 CH | 3308 |
| 17 | 🇹🇷 TR | 2815 |
| 18 | 🇲🇾 MY | 2607 |
| 19 | 🇿🇦 ZA | 2137 |
| 20 | 🇵🇱 PL | 2122 |
| 21 | 🇳🇿 NZ | 2078 |
| 22 | 🇹🇭 TH | 2003 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1813 |
| 25 | 🇬🇹 GT | 1766 |
| 26 | 🇲🇦 MA | 1385 |
| 27 | 🇲🇪 ME | 1285 |
| 28 | 🇳🇱 NL | 1214 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1130 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2698 |
| 2 | Denver International Airport |  | US | 2201 |
| 3 | Tokyo International Airport |  | JP | 1848 |
| 4 | Indira Gandhi International Airport |  | IN | 1680 |
| 5 | Harry Reid International Airport |  | US | 1612 |
| 6 | Guaymaral Airport |  | CO | 1573 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1531 |
| 8 | Zurich Airport |  | CH | 1421 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1376 |
| 10 | La Aurora Airport |  | GT | 1366 |
| 11 | Frankfurt am Main International Airport |  | DE | 1316 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1259 |
| 13 | Chicago O'Hare International Airport |  | US | 1241 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1151 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1085 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1062 |
| 20 | Madrid Barajas International Airport |  | ES | 1060 |
| 21 | Congonhas Airport |  | BR | 1021 |
| 22 | Kuala Lumpur International Airport |  | MY | 1014 |
| 23 | Charlotte/Douglas International Airport |  | US | 969 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 945 |
| 25 | Charles de Gaulle International Airport |  | FR | 939 |
| 26 | Bengaluru International Airport |  | IN | 920 |
| 27 | Malpensa International Airport |  | IT | 878 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 873 |
| 29 | Ninoy Aquino International Airport |  | PH | 841 |
| 30 | Daniel K Inouye International Airport |  | US | 815 |
| 31 | Barcelona International Airport |  | ES | 804 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 790 |
| 33 | Tenerife Norte Airport |  | ES | 784 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 760 |
| 35 | Calgary International Airport |  | CA | 753 |
| 36 | Vitoria/Foronda Airport |  | ES | 748 |
| 37 | Seattle-Tacoma International Airport |  | US | 747 |
| 38 | Scottsdale Airport |  | US | 744 |
| 39 | Viracopos International Airport |  | BR | 739 |
| 40 | Amsterdam Airport Schiphol |  | NL | 731 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 659 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 468 | 21m | 244 km | 1,970.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 325 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 314 | 1h 10m | 770 km | 4,171.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 238 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 180 | 44m | 241 km | 747.7 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 173 | 27m | 152 km | 452.1 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 168 | 1h 45m | 1,423 km | 4,123.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 159 | 18m | 144 km | 395.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 153 | 1h 1m | 695 km | 1,834.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 148 | 54m | 136 km | 347.0 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6016B |  | Logan-Cache Airport (KLGU) | Logan-Cache Airport (KLGU) | 2026-07-05 03:52 UTC | 2026-07-05 04:11 UTC | 18m |
| OC95 |  | Fukuoka Airport (RJFF) | Fukue Airport (RJFE) | 2026-07-05 03:33 UTC | 2026-07-05 04:02 UTC | 28m |
| EJA354 | EJA | Sierraville Dearwater Airport (KO79) | San Francisco International Airport (KSFO) | 2026-07-05 03:12 UTC | 2026-07-05 03:55 UTC | 43m |
| ITY | ITY | Beechworth Airport (YBCH) | Albury Airport (YMAY) | 2026-07-05 03:20 UTC | 2026-07-05 03:32 UTC | 12m |
| N365MT |  | Savannah/Hilton Head International Airport (KSAV) | Hunter Army Air Field (KSVN) | 2026-07-05 03:15 UTC | 2026-07-05 03:23 UTC | 7m |
| VOI3316 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | General Jose Maria Yanez International Airport (MMGM) | 2026-07-05 02:14 UTC | 2026-07-05 03:14 UTC | 1h 0m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-07-05 02:56 UTC | 2026-07-05 03:08 UTC | 12m |
| RZN866 | RZN | 0TS2 (0TS2) | Philadelphia International Airport (KPHL) | 2026-07-05 00:14 UTC | 2026-07-05 03:05 UTC | 2h 51m |
| GAP2018 | GAP | Ninoy Aquino International Airport (RPLL) | Loakan Airport (RPUB) | 2026-07-05 02:40 UTC | 2026-07-05 03:02 UTC | 22m |
| ASA1092 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-07-05 02:40 UTC | 2026-07-05 03:01 UTC | 21m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-07-05 02:24 UTC | 2026-07-05 03:00 UTC | 36m |
| N129NB |  | Talaheim Airport (1AK8) | Flyway Farm Airstrip (36AK) | 2026-07-05 02:37 UTC | 2026-07-05 02:57 UTC | 20m |
| IGO164W | IndiGo | Indira Gandhi International Airport (VIDP) | Tezpur Airport (VETZ) | 2026-07-05 00:51 UTC | 2026-07-05 02:57 UTC | 2h 5m |
| N167Z |  | Roberts Field (KRDM) | Sunriver Airport (KS21) | 2026-07-05 02:43 UTC | 2026-07-05 02:57 UTC | 13m |
| CEB506 | CEB | Ninoy Aquino International Airport (RPLL) | RP14 (RP14) | 2026-07-05 02:34 UTC | 2026-07-05 02:56 UTC | 22m |
| JBU638 | JetBlue | Austin-Bergstrom International Airport (KAUS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-04 23:19 UTC | 2026-07-05 02:55 UTC | 3h 36m |
| MXD322 | MXD | Simpang Airport (WMKF) | Parapat Airport (WIMP) | 2026-07-05 02:25 UTC | 2026-07-05 02:54 UTC | 29m |
| SNJ102 | SNJ | Futenma Marine Corps Air Station (ROTM) | Iki Airport (RJDB) | 2026-07-05 01:49 UTC | 2026-07-05 02:53 UTC | 1h 4m |
| MDA303 | MDA | Kaohsiung International Airport (RCKH) | Wang-an Airport (RCWA) | 2026-07-05 02:29 UTC | 2026-07-05 02:52 UTC | 22m |
| CEB897 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-05 02:28 UTC | 2026-07-05 02:51 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
