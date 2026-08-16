# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_07:53:04_UTC-green)

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

**Latest saved flight:** 2026-08-16 07:53:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 07:53:04 UTC

- **203,904** saved flights
- **65,281** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **203,904** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,450,361.8 tonnes** estimated CO2 emissions
- **142,049,962 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8013 |
| 2 | SkyWest Airlines | 7351 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3476 |
| 5 | American Airlines | 3400 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2611 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1837 |
| 11 | Lufthansa | 1736 |
| 12 | Vueling | 1687 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1397 |
| 16 | Swiss International | 1356 |
| 17 | AXM | 1324 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1259 |
| 21 | EJU | 1247 |
| 22 | All Nippon Airways | 1238 |
| 23 | VIV | 1119 |
| 24 | GLO | 1094 |
| 25 | PGT | 1083 |
| 26 | Air France | 1082 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1039 |
| 29 | WMT | 1015 |
| 30 | CXK | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173782 |
| 2 | 🇪🇸 ES | 13018 |
| 3 | 🇧🇷 BR | 11646 |
| 4 | 🇦🇺 AU | 11462 |
| 5 | 🇨🇦 CA | 11279 |
| 6 | 🇮🇳 IN | 10856 |
| 7 | 🇮🇹 IT | 10555 |
| 8 | 🇩🇪 DE | 10068 |
| 9 | 🇬🇧 GB | 9469 |
| 10 | 🇯🇵 JP | 8384 |
| 11 | 🇫🇷 FR | 8060 |
| 12 | 🇨🇴 CO | 8044 |
| 13 | 🇬🇷 GR | 5981 |
| 14 | 🇲🇽 MX | 5741 |
| 15 | 🇹🇷 TR | 5699 |
| 16 | 🇨🇭 CH | 5447 |
| 17 | 🇳🇴 NO | 5079 |
| 18 | 🇲🇾 MY | 3483 |
| 19 | 🇿🇦 ZA | 3388 |
| 20 | 🇵🇱 PL | 3340 |
| 21 | 🇹🇭 TH | 3207 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2707 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2488 |
| 26 | 🇭🇷 HR | 2147 |
| 27 | 🇲🇦 MA | 2043 |
| 28 | 🇳🇱 NL | 1808 |
| 29 | 🇲🇪 ME | 1694 |
| 30 | 🇮🇩 ID | 1667 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2530 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2467 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2129 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 9 | Zurich Airport |  | CH | 2114 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1903 |
| 12 | El Dorado International Airport |  | CO | 1860 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1826 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1690 |
| 17 | Madrid Barajas International Airport |  | ES | 1592 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Capua Airport |  | IT | 1544 |
| 21 | Macau International Airport |  | MO | 1541 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1435 |
| 24 | Malpensa International Airport |  | IT | 1400 |
| 25 | Charlotte/Douglas International Airport |  | US | 1391 |
| 26 | Charles de Gaulle International Airport |  | FR | 1389 |
| 27 | Kuala Lumpur International Airport |  | MY | 1292 |
| 28 | Ninoy Aquino International Airport |  | PH | 1281 |
| 29 | Bengaluru International Airport |  | IN | 1265 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1232 |
| 32 | Barcelona International Airport |  | ES | 1217 |
| 33 | Seattle-Tacoma International Airport |  | US | 1212 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1121 |
| 38 | Vitoria/Foronda Airport |  | ES | 1120 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Tenerife Norte Airport |  | ES | 1096 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 494 | 1h 7m | 770 km | 6,562.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 475 | 24m | 225 km | 1,842.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 341 | 27m | 275 km | 1,615.9 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 308 | 1h 7m | 706 km | 3,749.9 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 293 | 1h 49m | 1,423 km | 7,190.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 230 | 31m | 369 km | 1,464.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBKNI | HBK | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-08-16 07:15 UTC | 2026-08-16 07:53 UTC | 37m |
| HBKNN | HBK | Locarno Airport (LSZL) | Raron Airport (LSTA) | 2026-08-16 07:19 UTC | 2026-08-16 07:50 UTC | 30m |
| HBZZX | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-16 06:57 UTC | 2026-08-16 07:44 UTC | 47m |
| HBZVQ | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-16 06:56 UTC | 2026-08-16 07:42 UTC | 45m |
| N733AM |  | Whiteman Airport (KWHP) | San Bernardino International Airport (KSBD) | 2026-08-16 06:55 UTC | 2026-08-16 07:39 UTC | 44m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-16 07:24 UTC | 2026-08-16 07:35 UTC | 11m |
| FD645 |  | Bunbury Airport (YBUN) | Perth International Airport (YPPH) | 2026-08-16 06:43 UTC | 2026-08-16 07:31 UTC | 47m |
| BH102 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-08-16 06:31 UTC | 2026-08-16 07:23 UTC | 51m |
| ALE067 | ALE | Palma De Mallorca Airport (LEPA) | Trento / Mattarello Airport (LIDT) | 2026-08-16 04:58 UTC | 2026-08-16 07:19 UTC | 2h 20m |
| AIC8UF | Air India | Indira Gandhi International Airport (VIDP) | Sarsawa Air Force Station (VISP) | 2026-08-16 06:51 UTC | 2026-08-16 07:16 UTC | 25m |
| N8AK |  | Norman Y Mineta San Jose International Airport (KSJC) | Taipei Songshan Airport (RCSS) | 2026-08-15 18:53 UTC | 2026-08-16 07:16 UTC | 12h 22m |
| WJA9532 | WJA | John C. Munro Hamilton International Airport (CYHM) | Odessa / Strawberry Lakes Airstrip (CSL7) | 2026-08-16 04:29 UTC | 2026-08-16 07:14 UTC | 2h 45m |
| HBFXE | HBF | Lugano Airport (LSZA) | Sion Airport (LSGS) | 2026-08-16 06:42 UTC | 2026-08-16 07:14 UTC | 32m |
| AXM6496 | AXM | Kota Kinabalu International Airport (WBKK) | Ranau Airport (WBKR) | 2026-08-16 06:59 UTC | 2026-08-16 07:12 UTC | 12m |
| FD514 |  | Adelaide International Airport (YPAD) | Waikerie Airport (YWKI) | 2026-08-16 06:46 UTC | 2026-08-16 07:11 UTC | 24m |
| EXS6UB | EXS | Birmingham International Airport (EGBB) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-16 05:03 UTC | 2026-08-16 07:11 UTC | 2h 7m |
| BTX3C | BTX | Cannes-Mandelieu Airport (LFMD) | Samedan Airport (LSZS) | 2026-08-16 06:14 UTC | 2026-08-16 07:10 UTC | 55m |
| AIQ3142 | AIQ | Don Mueang International Airport (VTBD) | Kawthoung Airport (VYKT) | 2026-08-16 06:30 UTC | 2026-08-16 07:10 UTC | 40m |
| RGA06 | RGA | Muenster Aero Airport (LSPU) | Lodrino Air Base (LSML) | 2026-08-16 07:01 UTC | 2026-08-16 07:09 UTC | 8m |
| N406LF |  | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-16 07:01 UTC | 2026-08-16 07:09 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
