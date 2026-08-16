# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_14:02:05_UTC-green)

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

**Latest saved flight:** 2026-08-16 14:02:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 14:02:05 UTC

- **204,667** saved flights
- **65,400** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **204,667** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,460,834.3 tonnes** estimated CO2 emissions
- **142,657,060 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8064 |
| 2 | SkyWest Airlines | 7352 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3504 |
| 5 | American Airlines | 3403 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2615 |
| 8 | ENY | 2549 |
| 9 | LATAM Airlines | 1917 |
| 10 | AZU | 1846 |
| 11 | Lufthansa | 1742 |
| 12 | Vueling | 1697 |
| 13 | WIF | 1647 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1415 |
| 16 | Swiss International | 1364 |
| 17 | AXM | 1338 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1276 |
| 20 | QLK | 1261 |
| 21 | EJU | 1253 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1122 |
| 24 | GLO | 1095 |
| 25 | Air France | 1092 |
| 26 | PGT | 1091 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1046 |
| 29 | WMT | 1023 |
| 30 | CXK | 1012 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173879 |
| 2 | 🇪🇸 ES | 13094 |
| 3 | 🇧🇷 BR | 11686 |
| 4 | 🇦🇺 AU | 11482 |
| 5 | 🇨🇦 CA | 11286 |
| 6 | 🇮🇳 IN | 10942 |
| 7 | 🇮🇹 IT | 10641 |
| 8 | 🇩🇪 DE | 10128 |
| 9 | 🇬🇧 GB | 9557 |
| 10 | 🇯🇵 JP | 8452 |
| 11 | 🇫🇷 FR | 8110 |
| 12 | 🇨🇴 CO | 8063 |
| 13 | 🇬🇷 GR | 6026 |
| 14 | 🇹🇷 TR | 5776 |
| 15 | 🇲🇽 MX | 5747 |
| 16 | 🇨🇭 CH | 5485 |
| 17 | 🇳🇴 NO | 5101 |
| 18 | 🇲🇾 MY | 3526 |
| 19 | 🇿🇦 ZA | 3438 |
| 20 | 🇵🇱 PL | 3371 |
| 21 | 🇹🇭 TH | 3242 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2560 |
| 25 | 🇰🇷 KR | 2503 |
| 26 | 🇭🇷 HR | 2182 |
| 27 | 🇲🇦 MA | 2061 |
| 28 | 🇳🇱 NL | 1827 |
| 29 | 🇲🇪 ME | 1711 |
| 30 | 🇮🇩 ID | 1682 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4290 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2549 |
| 4 | Indira Gandhi International Airport |  | IN | 2483 |
| 5 | Guaymaral Airport |  | CO | 2478 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2141 |
| 8 | Zurich Airport |  | CH | 2135 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2119 |
| 10 | La Aurora Airport |  | GT | 1961 |
| 11 | Chicago O'Hare International Airport |  | US | 1904 |
| 12 | El Dorado International Airport |  | CO | 1865 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1827 |
| 14 | Salt Lake City International Airport |  | US | 1809 |
| 15 | Congonhas Airport |  | BR | 1700 |
| 16 | Frankfurt am Main International Airport |  | DE | 1697 |
| 17 | Madrid Barajas International Airport |  | ES | 1602 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1552 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1477 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1407 |
| 25 | Charles de Gaulle International Airport |  | FR | 1400 |
| 26 | Charlotte/Douglas International Airport |  | US | 1392 |
| 27 | Kuala Lumpur International Airport |  | MY | 1307 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1271 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1259 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1222 |
| 33 | Seattle-Tacoma International Airport |  | US | 1215 |
| 34 | Viracopos International Airport |  | BR | 1185 |
| 35 | Calgary International Airport |  | CA | 1158 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Vitoria/Foronda Airport |  | ES | 1130 |
| 38 | Oslo Gardermoen Airport |  | NO | 1127 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Tenerife Norte Airport |  | ES | 1102 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1020 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 343 | 27m | 275 km | 1,625.3 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 300 | 44m | 241 km | 1,246.1 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 296 | 1h 49m | 1,423 km | 7,264.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 254 | 24m | 218 km | 956.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 249 | 26m | 215 km | 922.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 246 | 19m | 99 km | 421.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 240 | 1h 37m | 1,156 km | 4,787.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 236 | 19m | 144 km | 587.0 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 217 | 28m | 152 km | 567.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N342US |  | Pompano Beach Airpark (KPMP) | Sebring Regional Airport (KSEF) | 2026-08-16 13:16 UTC | 2026-08-16 14:02 UTC | 45m |
| N4460L |  | Albert Whitted Airport (KSPG) | Albert Whitted Airport (KSPG) | 2026-08-16 12:42 UTC | 2026-08-16 14:00 UTC | 1h 17m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-16 13:43 UTC | 2026-08-16 13:58 UTC | 14m |
| OST6 | OST | Stillwater Regional Airport (KSWO) | 19OK (19OK) | 2026-08-16 13:29 UTC | 2026-08-16 13:57 UTC | 28m |
| AAL882 | American Airlines | Buffalo Niagara International Airport (KBUF) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-16 11:12 UTC | 2026-08-16 13:48 UTC | 2h 36m |
| AUA80 | Austrian Airlines | Ben Gurion International Airport (LLBG) | OS64 (OS64) | 2026-08-16 13:21 UTC | 2026-08-16 13:46 UTC | 25m |
| N39954 |  | Falcon Field (KFFZ) | Falcon Field (KFFZ) | 2026-08-16 13:23 UTC | 2026-08-16 13:45 UTC | 21m |
| PHGLD | PHG | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-08-16 12:26 UTC | 2026-08-16 13:40 UTC | 1h 13m |
| N145SH |  | Michael J Smith Field (KMRH) | Michael J Smith Field (KMRH) | 2026-08-16 13:24 UTC | 2026-08-16 13:32 UTC | 8m |
| FBPKH | FBP | Saint-Cyr-l'Ecole Airport (LFPZ) | Dreux Vernouillet Airport (LFON) | 2026-08-16 13:07 UTC | 2026-08-16 13:32 UTC | 25m |
| N911LS |  | Moundridge Municipal Airport (K47K) | Cessna Acft Field (KCEA) | 2026-08-16 13:12 UTC | 2026-08-16 13:28 UTC | 15m |
| IGO6069 | IndiGo | Agartala Airport (VEAT) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-08-16 13:01 UTC | 2026-08-16 13:27 UTC | 26m |
| LVJUQ | LVJ | RAF Akrotiri (LCRA) | RAF Akrotiri (LCRA) | 2026-08-16 12:11 UTC | 2026-08-16 13:26 UTC | 1h 14m |
| AZU4530 | AZU | Viracopos International Airport (SBKP) | Bariri Airport (SDBY) | 2026-08-16 12:54 UTC | 2026-08-16 13:24 UTC | 30m |
| N61633 |  | Danbury Municipal Airport (KDXR) | Waterbury-Oxford Airport (KOXC) | 2026-08-16 12:46 UTC | 2026-08-16 13:24 UTC | 38m |
| N1759F |  | Sandridge Airpark Inc Airport (OK94) | Sandridge Airpark Inc Airport (OK94) | 2026-08-16 13:23 UTC | 2026-08-16 13:23 UTC | 0m |
| OMBHA | OMB | RAF Akrotiri (LCRA) | RAF Akrotiri (LCRA) | 2026-08-16 13:06 UTC | 2026-08-16 13:18 UTC | 11m |
| N274CW |  | Aero Country Airport (KT31) | Jones Field (KF00) | 2026-08-16 12:58 UTC | 2026-08-16 13:17 UTC | 19m |
| RJA132 | Royal Jordanian | Eleftherios Venizelos International Airport (LGAV) | Queen Alia International Airport (OJAI) | 2026-08-16 11:39 UTC | 2026-08-16 13:15 UTC | 1h 36m |
| CXK607 | CXK | Ellington Airport (KEFD) | Jack Brooks Regional Airport (KBPT) | 2026-08-16 11:17 UTC | 2026-08-16 13:15 UTC | 1h 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
