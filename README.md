# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_10:24:39_UTC-green)

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

**Latest saved flight:** 2026-08-13 10:24:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 10:24:39 UTC

- **191,820** saved flights
- **60,453** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **191,820** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,294,762.8 tonnes** estimated CO2 emissions
- **133,029,727 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7611 |
| 2 | SkyWest Airlines | 6935 |
| 3 | EJA | 3785 |
| 4 | IndiGo | 3324 |
| 5 | Southwest Airlines | 2994 |
| 6 | American Airlines | 2974 |
| 7 | ENY | 2375 |
| 8 | Delta Air Lines | 2256 |
| 9 | LATAM Airlines | 1796 |
| 10 | AZU | 1730 |
| 11 | Lufthansa | 1667 |
| 12 | Vueling | 1595 |
| 13 | WIF | 1589 |
| 14 | LXJ | 1505 |
| 15 | easyJet | 1321 |
| 16 | Swiss International | 1303 |
| 17 | AXM | 1258 |
| 18 | QLK | 1186 |
| 19 | EJU | 1185 |
| 20 | All Nippon Airways | 1164 |
| 21 | Alaska Airlines | 1144 |
| 22 | VIV | 1057 |
| 23 | GLO | 1033 |
| 24 | Air France | 1000 |
| 25 | PGT | 991 |
| 26 | CXK | 983 |
| 27 | AEE | 981 |
| 28 | United Airlines | 977 |
| 29 | Wizz Air | 952 |
| 30 | WMT | 951 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 163381 |
| 2 | 🇪🇸 ES | 12343 |
| 3 | 🇧🇷 BR | 11014 |
| 4 | 🇦🇺 AU | 10802 |
| 5 | 🇨🇦 CA | 10510 |
| 6 | 🇮🇳 IN | 10412 |
| 7 | 🇮🇹 IT | 9977 |
| 8 | 🇩🇪 DE | 9486 |
| 9 | 🇬🇧 GB | 8950 |
| 10 | 🇯🇵 JP | 7864 |
| 11 | 🇫🇷 FR | 7661 |
| 12 | 🇨🇴 CO | 7385 |
| 13 | 🇬🇷 GR | 5601 |
| 14 | 🇲🇽 MX | 5426 |
| 15 | 🇨🇭 CH | 5146 |
| 16 | 🇹🇷 TR | 5140 |
| 17 | 🇳🇴 NO | 4930 |
| 18 | 🇲🇾 MY | 3294 |
| 19 | 🇿🇦 ZA | 3234 |
| 20 | 🇵🇱 PL | 3164 |
| 21 | 🇹🇭 TH | 2972 |
| 22 | 🇳🇿 NZ | 2706 |
| 23 | 🇵🇭 PH | 2534 |
| 24 | 🇬🇹 GT | 2424 |
| 25 | 🇰🇷 KR | 2345 |
| 26 | 🇭🇷 HR | 1975 |
| 27 | 🇲🇦 MA | 1941 |
| 28 | 🇳🇱 NL | 1716 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1547 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3983 |
| 2 | Denver International Airport |  | US | 3143 |
| 3 | Tokyo International Airport |  | JP | 2419 |
| 4 | Guaymaral Airport |  | CO | 2365 |
| 5 | Indira Gandhi International Airport |  | IN | 2345 |
| 6 | Harry Reid International Airport |  | US | 2229 |
| 7 | Zurich Airport |  | CH | 2034 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2028 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1982 |
| 10 | La Aurora Airport |  | GT | 1862 |
| 11 | El Dorado International Airport |  | CO | 1733 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1731 |
| 13 | Salt Lake City International Airport |  | US | 1710 |
| 14 | Chicago O'Hare International Airport |  | US | 1680 |
| 15 | Frankfurt am Main International Airport |  | DE | 1629 |
| 16 | Congonhas Airport |  | BR | 1602 |
| 17 | Macau International Airport |  | MO | 1527 |
| 18 | Madrid Barajas International Airport |  | ES | 1509 |
| 19 | Capua Airport |  | IT | 1484 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1483 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1416 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1375 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1324 |
| 25 | Charles de Gaulle International Airport |  | FR | 1313 |
| 26 | Charlotte/Douglas International Airport |  | US | 1278 |
| 27 | Bengaluru International Airport |  | IN | 1231 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1198 |
| 30 | Ninoy Aquino International Airport |  | PH | 1198 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1177 |
| 32 | Barcelona International Airport |  | ES | 1146 |
| 33 | Viracopos International Airport |  | BR | 1113 |
| 34 | Seattle-Tacoma International Airport |  | US | 1104 |
| 35 | Reno/Tahoe International Airport |  | US | 1097 |
| 36 | Calgary International Airport |  | CA | 1097 |
| 37 | Daniel K Inouye International Airport |  | US | 1078 |
| 38 | Oslo Gardermoen Airport |  | NO | 1076 |
| 39 | Tenerife Norte Airport |  | ES | 1052 |
| 40 | Vitoria/Foronda Airport |  | ES | 1041 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 976 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 706 | 21m | 244 km | 2,972.8 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 468 | 1h 7m | 770 km | 6,217.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 445 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 334 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 322 | 27m | 275 km | 1,525.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 306 | 8m | - | - |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 285 | 44m | 241 km | 1,183.8 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 275 | 1h 49m | 1,423 km | 6,748.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 257 | 20m | 250 km | 1,110.1 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 240 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 239 | 27m | 215 km | 885.2 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 234 | 19m | 99 km | 400.8 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 234 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 233 | 1h 15m | 961 km | 3,862.1 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 231 | 24m | 218 km | 870.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 208 | 1h 48m | 1,304 km | 4,679.5 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TUTOR983 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-13 09:57 UTC | 2026-08-13 10:24 UTC | 27m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | Sollieres Sardieres Airport (LFKD) | 2026-08-13 10:10 UTC | 2026-08-13 10:21 UTC | 11m |
| TUTOR862 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-13 09:53 UTC | 2026-08-13 10:19 UTC | 25m |
| UFX63 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-08-13 09:33 UTC | 2026-08-13 10:13 UTC | 40m |
| ULR91N | ULR | Fair Isle Airport (EGEF) | Aberdeen Dyce Airport (EGPD) | 2026-08-13 09:52 UTC | 2026-08-13 10:04 UTC | 12m |
| DEFFY | DEF | Baneasa International Airport (LRBS) | Baneasa International Airport (LRBS) | 2026-08-13 09:24 UTC | 2026-08-13 10:01 UTC | 36m |
| HKS51 | HKS | Humberside Airport (EGNJ) | EGYO (EGYO) | 2026-08-13 09:32 UTC | 2026-08-13 09:52 UTC | 19m |
| ITY759 | ITY | Suvarnabhumi Airport (VTBS) | Alama Iqbal International Airport (OPLA) | 2026-08-13 05:54 UTC | 2026-08-13 09:51 UTC | 3h 57m |
| GSRXX | GSR | London Biggin Hill Airport (EGKB) | Lydd Airport (EGMD) | 2026-08-13 09:17 UTC | 2026-08-13 09:50 UTC | 32m |
| VCG2LE | VCG | Guernsey Airport (EGJB) | Newquay Cornwall Airport (EGHQ) | 2026-08-13 09:20 UTC | 2026-08-13 09:47 UTC | 26m |
| N113VG |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-08-13 09:17 UTC | 2026-08-13 09:45 UTC | 27m |
| EWG86C | EWG | Palma De Mallorca Airport (LEPA) | Saarbrucken Airport (EDDR) | 2026-08-13 08:00 UTC | 2026-08-13 09:40 UTC | 1h 40m |
| TUTOR983 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-13 09:13 UTC | 2026-08-13 09:39 UTC | 25m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-13 09:30 UTC | 2026-08-13 09:38 UTC | 8m |
| NOZ7TE | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Bardufoss Airport (ENDU) | 2026-08-13 08:10 UTC | 2026-08-13 09:35 UTC | 1h 25m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-08-13 09:07 UTC | 2026-08-13 09:33 UTC | 25m |
| TUTOR862 | TUT | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-13 09:09 UTC | 2026-08-13 09:33 UTC | 23m |
| IGO273W | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Lengpui Airport (VELP) | 2026-08-13 08:57 UTC | 2026-08-13 09:32 UTC | 34m |
| EAI17W | EAI | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-13 08:30 UTC | 2026-08-13 09:31 UTC | 1h 0m |
| QLK1296 | QLK | Georgetown (Tas) Airport (YGTO) | Melbourne International Airport (YMML) | 2026-08-13 08:37 UTC | 2026-08-13 09:23 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
