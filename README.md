# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_17:13:27_UTC-green)

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

**Latest saved flight:** 2026-08-07 17:13:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 17:13:27 UTC

- **175,901** saved flights
- **56,770** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **175,901** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,115,334.7 tonnes** estimated CO2 emissions
- **122,628,098 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6977 |
| 2 | SkyWest Airlines | 6406 |
| 3 | EJA | 3471 |
| 4 | IndiGo | 3090 |
| 5 | Southwest Airlines | 2763 |
| 6 | American Airlines | 2741 |
| 7 | ENY | 2184 |
| 8 | Delta Air Lines | 2080 |
| 9 | LATAM Airlines | 1628 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1558 |
| 12 | WIF | 1477 |
| 13 | Vueling | 1451 |
| 14 | LXJ | 1380 |
| 15 | Swiss International | 1200 |
| 16 | AXM | 1196 |
| 17 | easyJet | 1193 |
| 18 | QLK | 1082 |
| 19 | EJU | 1078 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1065 |
| 22 | VIV | 964 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 934 |
| 25 | GLO | 923 |
| 26 | AEE | 916 |
| 27 | Air France | 909 |
| 28 | United Airlines | 909 |
| 29 | MXY | 884 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 151101 |
| 2 | 🇪🇸 ES | 11269 |
| 3 | 🇧🇷 BR | 10010 |
| 4 | 🇦🇺 AU | 9951 |
| 5 | 🇮🇳 IN | 9685 |
| 6 | 🇨🇦 CA | 9614 |
| 7 | 🇮🇹 IT | 9094 |
| 8 | 🇩🇪 DE | 8727 |
| 9 | 🇬🇧 GB | 8152 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 6998 |
| 12 | 🇨🇴 CO | 6457 |
| 13 | 🇬🇷 GR | 5123 |
| 14 | 🇲🇽 MX | 5023 |
| 15 | 🇨🇭 CH | 4670 |
| 16 | 🇳🇴 NO | 4591 |
| 17 | 🇹🇷 TR | 4346 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2931 |
| 20 | 🇿🇦 ZA | 2872 |
| 21 | 🇹🇭 TH | 2623 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2241 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1776 |
| 27 | 🇭🇷 HR | 1722 |
| 28 | 🇲🇪 ME | 1605 |
| 29 | 🇳🇱 NL | 1588 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3626 |
| 2 | Denver International Airport |  | US | 2899 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2164 |
| 5 | Indira Gandhi International Airport |  | IN | 2150 |
| 6 | Harry Reid International Airport |  | US | 2096 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1908 |
| 8 | Zurich Airport |  | CH | 1868 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1837 |
| 10 | La Aurora Airport |  | GT | 1723 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1608 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1580 |
| 14 | Salt Lake City International Airport |  | US | 1566 |
| 15 | Frankfurt am Main International Airport |  | DE | 1550 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1447 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1424 |
| 19 | Capua Airport |  | IT | 1374 |
| 20 | Madrid Barajas International Airport |  | ES | 1371 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1310 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1238 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1203 |
| 25 | Malpensa International Airport |  | IT | 1198 |
| 26 | Charles de Gaulle International Airport |  | FR | 1198 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1152 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1087 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1086 |
| 32 | Barcelona International Airport |  | ES | 1042 |
| 33 | Daniel K Inouye International Airport |  | US | 1010 |
| 34 | Seattle-Tacoma International Airport |  | US | 1010 |
| 35 | Viracopos International Airport |  | BR | 1000 |
| 36 | Reno/Tahoe International Airport |  | US | 997 |
| 37 | Calgary International Airport |  | CA | 995 |
| 38 | Oslo Gardermoen Airport |  | NO | 982 |
| 39 | Tenerife Norte Airport |  | ES | 968 |
| 40 | Amsterdam Airport Schiphol |  | NL | 955 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 641 | 21m | 244 km | 2,699.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 409 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 296 | 27m | 275 km | 1,402.6 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 268 | 44m | 241 km | 1,113.2 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 242 | 1h 48m | 1,423 km | 5,939.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 230 | 20m | 250 km | 993.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 224 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 217 | 20m | 99 km | 371.7 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 21 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 212 | 8m | - | - |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 212 | 51m | 556 km | 2,032.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 210 | 19m | 144 km | 522.4 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 209 | 1h 15m | 961 km | 3,464.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 204 | 1h 38m | 1,156 km | 4,069.7 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 200 | 24m | 218 km | 753.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 191 | 1h 2m | 695 km | 2,289.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N5000Y |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-08-07 17:01 UTC | 2026-08-07 17:13 UTC | 11m |
| N445B |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-08-07 16:32 UTC | 2026-08-07 17:09 UTC | 37m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-08-07 16:21 UTC | 2026-08-07 17:07 UTC | 46m |
| N332PH |  | Hilltop Ranch Airport (9TA1) | Kelly Field (KSKF) | 2026-08-07 16:53 UTC | 2026-08-07 17:06 UTC | 13m |
| JUMP17 | JUM | Carson Field (MT53) | Carson Field (MT53) | 2026-08-07 16:53 UTC | 2026-08-07 17:04 UTC | 11m |
| N944KC |  | North Palm Beach County General Aviation Airport (KF45) | North Palm Beach County General Aviation Airport (KF45) | 2026-08-07 16:42 UTC | 2026-08-07 16:59 UTC | 16m |
| PROOQ | PRO | SBEC (SBEC) | SBMM (SBMM) | 2026-08-07 16:49 UTC | 2026-08-07 16:58 UTC | 9m |
| N1RD |  | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-08-07 16:30 UTC | 2026-08-07 16:53 UTC | 23m |
| N121MF |  | Bend Municipal Airport (KBDN) | Rogue Valley International/Medford Airport (KMFR) | 2026-08-07 16:13 UTC | 2026-08-07 16:53 UTC | 39m |
| GXTST24 | GXT | Wichita Dwight D Eisenhower Ntl Airport (KICT) | 1KS5 (1KS5) | 2026-08-07 15:54 UTC | 2026-08-07 16:50 UTC | 55m |
| N900DG |  | Chino Airport (KCNO) | Lake Tahoe Airport (KTVL) | 2026-08-07 15:34 UTC | 2026-08-07 16:49 UTC | 1h 14m |
| TWY281 | TWY | Truckee-Tahoe Airport (KTRK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-07 16:06 UTC | 2026-08-07 16:47 UTC | 40m |
| OEANN | OEA | Hohenems-Dornbirn Airport (LOIH) | Konstanz Airport (EDTZ) | 2026-08-07 15:25 UTC | 2026-08-07 16:42 UTC | 1h 17m |
| N737CH |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-08-07 16:41 UTC | 2026-08-07 16:41 UTC | 0m |
| N90JF |  | Antonio/Nery/Juarbe Pol Airport (TJAB) | Antonio/Nery/Juarbe Pol Airport (TJAB) | 2026-08-07 16:28 UTC | 2026-08-07 16:41 UTC | 12m |
| VAR491 | VAR | Phoenix Goodyear Airport (KGYR) | Prescott Regional/Ernest A Love Field (KPRC) | 2026-08-07 15:57 UTC | 2026-08-07 16:40 UTC | 43m |
| DRAGO741 | DRA | Geneva Cointrin International Airport (LSGG) | Geneva Cointrin International Airport (LSGG) | 2026-08-07 16:34 UTC | 2026-08-07 16:40 UTC | 5m |
| FTO501 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-07 16:06 UTC | 2026-08-07 16:38 UTC | 32m |
| N61606 |  | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-08-07 16:32 UTC | 2026-08-07 16:37 UTC | 5m |
| N5158J |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Vowers Ranch Airport (WY29) | 2026-08-07 16:15 UTC | 2026-08-07 16:37 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
