# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_22:23:16_UTC-green)

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

**Latest saved flight:** 2026-07-02 22:23:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-02 22:23:16 UTC

- **126,713** saved flights
- **43,272** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **126,713** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,528,825.3 tonnes** estimated CO2 emissions
- **88,627,555 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5137 |
| 2 | SkyWest Airlines | 4680 |
| 3 | EJA | 2497 |
| 4 | IndiGo | 2395 |
| 5 | American Airlines | 1950 |
| 6 | Southwest Airlines | 1899 |
| 7 | ENY | 1591 |
| 8 | Delta Air Lines | 1511 |
| 9 | Lufthansa | 1350 |
| 10 | LATAM Airlines | 1150 |
| 11 | Vueling | 1121 |
| 12 | WIF | 1115 |
| 13 | AZU | 1072 |
| 14 | AXM | 999 |
| 15 | LXJ | 987 |
| 16 | Swiss International | 879 |
| 17 | All Nippon Airways | 850 |
| 18 | Alaska Airlines | 824 |
| 19 | easyJet | 809 |
| 20 | QLK | 797 |
| 21 | EJU | 784 |
| 22 | Cathay Pacific | 704 |
| 23 | AEE | 694 |
| 24 | VIV | 694 |
| 25 | Air France | 692 |
| 26 | CXK | 679 |
| 27 | United Airlines | 674 |
| 28 | MXY | 659 |
| 29 | JetBlue | 649 |
| 30 | GLO | 639 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 108454 |
| 2 | 🇪🇸 ES | 8439 |
| 3 | 🇮🇳 IN | 7516 |
| 4 | 🇦🇺 AU | 7391 |
| 5 | 🇧🇷 BR | 7084 |
| 6 | 🇩🇪 DE | 6682 |
| 7 | 🇨🇦 CA | 6666 |
| 8 | 🇮🇹 IT | 6647 |
| 9 | 🇬🇧 GB | 5587 |
| 10 | 🇯🇵 JP | 5533 |
| 11 | 🇫🇷 FR | 5004 |
| 12 | 🇨🇴 CO | 4046 |
| 13 | 🇲🇽 MX | 3680 |
| 14 | 🇬🇷 GR | 3599 |
| 15 | 🇳🇴 NO | 3461 |
| 16 | 🇨🇭 CH | 3218 |
| 17 | 🇹🇷 TR | 2670 |
| 18 | 🇲🇾 MY | 2588 |
| 19 | 🇿🇦 ZA | 2089 |
| 20 | 🇵🇱 PL | 2071 |
| 21 | 🇳🇿 NZ | 2047 |
| 22 | 🇹🇭 TH | 1977 |
| 23 | 🇰🇷 KR | 1952 |
| 24 | 🇵🇭 PH | 1794 |
| 25 | 🇬🇹 GT | 1743 |
| 26 | 🇲🇦 MA | 1357 |
| 27 | 🇲🇪 ME | 1253 |
| 28 | 🇳🇱 NL | 1193 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1098 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2652 |
| 2 | Denver International Airport |  | US | 2135 |
| 3 | Tokyo International Airport |  | JP | 1826 |
| 4 | Indira Gandhi International Airport |  | IN | 1653 |
| 5 | Harry Reid International Airport |  | US | 1585 |
| 6 | Guaymaral Airport |  | CO | 1533 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1507 |
| 8 | Zurich Airport |  | CH | 1392 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1350 |
| 10 | La Aurora Airport |  | GT | 1347 |
| 11 | Frankfurt am Main International Airport |  | DE | 1304 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1241 |
| 13 | Chicago O'Hare International Airport |  | US | 1224 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1116 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1052 |
| 19 | Madrid Barajas International Airport |  | ES | 1041 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1040 |
| 21 | Kuala Lumpur International Airport |  | MY | 1007 |
| 22 | Congonhas Airport |  | BR | 994 |
| 23 | Charlotte/Douglas International Airport |  | US | 952 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 930 |
| 25 | Charles de Gaulle International Airport |  | FR | 923 |
| 26 | Bengaluru International Airport |  | IN | 909 |
| 27 | Malpensa International Airport |  | IT | 867 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 847 |
| 29 | Ninoy Aquino International Airport |  | PH | 831 |
| 30 | Daniel K Inouye International Airport |  | US | 806 |
| 31 | Barcelona International Airport |  | ES | 790 |
| 32 | Tenerife Norte Airport |  | ES | 776 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 768 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 743 |
| 35 | Calgary International Airport |  | CA | 740 |
| 36 | Seattle-Tacoma International Airport |  | US | 734 |
| 37 | Scottsdale Airport |  | US | 733 |
| 38 | Vitoria/Foronda Airport |  | ES | 725 |
| 39 | Viracopos International Airport |  | BR | 723 |
| 40 | Amsterdam Airport Schiphol |  | NL | 720 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 639 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 461 | 21m | 244 km | 1,941.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 326 | 24m | 225 km | 1,264.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 318 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 304 | 1h 10m | 770 km | 4,038.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 235 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 187 | 22m | 55 km | 177.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 175 | 44m | 241 km | 726.9 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 162 | 1h 45m | 1,423 km | 3,975.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 161 | 31m | 369 km | 1,024.8 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 149 | 30m | 49 km | 125.9 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 147 | 1h 1m | 695 km | 1,762.1 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 147 | 1h 17m | 961 km | 2,436.6 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Zhuhai Airport (ZGSD) | 2026-07-02 10:52 UTC | 2026-07-02 22:23 UTC | 11h 30m |
| N1820Z |  | Merrill Field (PAMR) | Merrill Field (PAMR) | 2026-07-02 22:12 UTC | 2026-07-02 22:23 UTC | 10m |
| N122KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-02 21:41 UTC | 2026-07-02 22:12 UTC | 30m |
| BRW170 | BRW | Flying Cloud Airport (KFCM) | Glencoe Municipal Airport (KGYL) | 2026-07-02 21:18 UTC | 2026-07-02 22:11 UTC | 52m |
| BCS692 | BCS | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-07-02 17:09 UTC | 2026-07-02 22:09 UTC | 4h 59m |
| CPA395 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-07-02 14:08 UTC | 2026-07-02 22:08 UTC | 7h 59m |
| TKR914 | TKR | Mesa Gateway Airport (KIWA) | Rimrock Airport (48AZ) | 2026-07-02 21:50 UTC | 2026-07-02 22:07 UTC | 16m |
| N41TE |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-02 21:38 UTC | 2026-07-02 22:05 UTC | 26m |
| CHRGR9 | CHR | John F Kennedy International Airport (KJFK) | Newark Liberty International Airport (KEWR) | 2026-07-02 21:42 UTC | 2026-07-02 22:05 UTC | 23m |
| CHRGR16 | CHR | John F Kennedy International Airport (KJFK) | Newark Liberty International Airport (KEWR) | 2026-07-02 21:41 UTC | 2026-07-02 22:04 UTC | 22m |
| ZKILT | ZKI | Hamilton International Airport (NZHN) | Hamilton International Airport (NZHN) | 2026-07-02 21:52 UTC | 2026-07-02 22:04 UTC | 11m |
| N280KX |  | Scottsdale Airport (KSDL) | Four Corners Regional Airport (KFMN) | 2026-07-02 21:26 UTC | 2026-07-02 22:01 UTC | 35m |
| N494NJ |  | Hesperia Airport (KL26) | Hemet-Ryan Airport (KHMT) | 2026-07-02 21:15 UTC | 2026-07-02 21:59 UTC | 44m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-02 21:43 UTC | 2026-07-02 21:58 UTC | 15m |
| N4865S |  | Pine Island Airport (7NC2) | College Park Airport (KCGS) | 2026-07-02 20:19 UTC | 2026-07-02 21:57 UTC | 1h 37m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-07-02 11:02 UTC | 2026-07-02 21:56 UTC | 10h 53m |
| N7057Q |  | Council Bluffs Municipal Airport (KCBF) | Eppley Airfield (KOMA) | 2026-07-02 21:34 UTC | 2026-07-02 21:56 UTC | 21m |
| N44996 |  | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-07-02 21:05 UTC | 2026-07-02 21:53 UTC | 47m |
| N608JR |  | Oakland County International Airport (KPTK) | Gaylord Regional Airport (KGLR) | 2026-07-02 21:26 UTC | 2026-07-02 21:52 UTC | 26m |
| N4434R |  | Hicks Airfield (KT67) | Jim Sears Airport (3TA7) | 2026-07-02 21:35 UTC | 2026-07-02 21:51 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
