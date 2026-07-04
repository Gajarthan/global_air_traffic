# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_16:25:02_UTC-green)

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

**Latest saved flight:** 2026-07-04 16:25:02 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-04 16:25:02 UTC

- **128,965** saved flights
- **43,911** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **128,965** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,556,293.3 tonnes** estimated CO2 emissions
- **90,219,903 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5244 |
| 2 | SkyWest Airlines | 4779 |
| 3 | EJA | 2525 |
| 4 | IndiGo | 2425 |
| 5 | American Airlines | 1988 |
| 6 | Southwest Airlines | 1940 |
| 7 | ENY | 1617 |
| 8 | Delta Air Lines | 1538 |
| 9 | Lufthansa | 1360 |
| 10 | LATAM Airlines | 1172 |
| 11 | Vueling | 1141 |
| 12 | WIF | 1133 |
| 13 | AZU | 1095 |
| 14 | AXM | 1003 |
| 15 | LXJ | 999 |
| 16 | Swiss International | 898 |
| 17 | All Nippon Airways | 858 |
| 18 | Alaska Airlines | 831 |
| 19 | easyJet | 824 |
| 20 | QLK | 808 |
| 21 | EJU | 798 |
| 22 | Cathay Pacific | 712 |
| 23 | VIV | 712 |
| 24 | AEE | 705 |
| 25 | Air France | 703 |
| 26 | CXK | 694 |
| 27 | United Airlines | 685 |
| 28 | MXY | 673 |
| 29 | JetBlue | 669 |
| 30 | GLO | 654 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110365 |
| 2 | 🇪🇸 ES | 8589 |
| 3 | 🇮🇳 IN | 7606 |
| 4 | 🇦🇺 AU | 7481 |
| 5 | 🇧🇷 BR | 7229 |
| 6 | 🇨🇦 CA | 6789 |
| 7 | 🇩🇪 DE | 6789 |
| 8 | 🇮🇹 IT | 6756 |
| 9 | 🇬🇧 GB | 5722 |
| 10 | 🇯🇵 JP | 5609 |
| 11 | 🇫🇷 FR | 5120 |
| 12 | 🇨🇴 CO | 4076 |
| 13 | 🇲🇽 MX | 3760 |
| 14 | 🇬🇷 GR | 3673 |
| 15 | 🇳🇴 NO | 3518 |
| 16 | 🇨🇭 CH | 3305 |
| 17 | 🇹🇷 TR | 2782 |
| 18 | 🇲🇾 MY | 2603 |
| 19 | 🇿🇦 ZA | 2137 |
| 20 | 🇵🇱 PL | 2120 |
| 21 | 🇳🇿 NZ | 2069 |
| 22 | 🇹🇭 TH | 2001 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1808 |
| 25 | 🇬🇹 GT | 1766 |
| 26 | 🇲🇦 MA | 1381 |
| 27 | 🇲🇪 ME | 1282 |
| 28 | 🇳🇱 NL | 1213 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1125 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2686 |
| 2 | Denver International Airport |  | US | 2187 |
| 3 | Tokyo International Airport |  | JP | 1848 |
| 4 | Indira Gandhi International Airport |  | IN | 1677 |
| 5 | Harry Reid International Airport |  | US | 1607 |
| 6 | Guaymaral Airport |  | CO | 1563 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1528 |
| 8 | Zurich Airport |  | CH | 1419 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1374 |
| 10 | La Aurora Airport |  | GT | 1366 |
| 11 | Frankfurt am Main International Airport |  | DE | 1315 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1257 |
| 13 | Chicago O'Hare International Airport |  | US | 1238 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1147 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1078 |
| 18 | Capua Airport |  | IT | 1067 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1059 |
| 20 | Madrid Barajas International Airport |  | ES | 1057 |
| 21 | Congonhas Airport |  | BR | 1017 |
| 22 | Kuala Lumpur International Airport |  | MY | 1013 |
| 23 | Charlotte/Douglas International Airport |  | US | 969 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 940 |
| 25 | Charles de Gaulle International Airport |  | FR | 937 |
| 26 | Bengaluru International Airport |  | IN | 920 |
| 27 | Malpensa International Airport |  | IT | 876 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 867 |
| 29 | Ninoy Aquino International Airport |  | PH | 838 |
| 30 | Daniel K Inouye International Airport |  | US | 813 |
| 31 | Barcelona International Airport |  | ES | 803 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 789 |
| 33 | Tenerife Norte Airport |  | ES | 783 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 758 |
| 35 | Calgary International Airport |  | CA | 752 |
| 36 | Vitoria/Foronda Airport |  | ES | 746 |
| 37 | Seattle-Tacoma International Airport |  | US | 744 |
| 38 | Scottsdale Airport |  | US | 743 |
| 39 | Viracopos International Airport |  | BR | 738 |
| 40 | Amsterdam Airport Schiphol |  | NL | 730 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 654 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 466 | 21m | 244 km | 1,962.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 325 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 314 | 1h 10m | 770 km | 4,171.2 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 246 | 26m | 275 km | 1,165.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 237 | 31m | - | - |
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
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 158 | 18m | 144 km | 393.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 153 | 1h 1m | 695 km | 1,834.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 149 | 1h 17m | 961 km | 2,469.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 143 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9421F |  | Pennridge Airport (KCKZ) | Pennridge Airport (KCKZ) | 2026-07-04 16:05 UTC | 2026-07-04 16:25 UTC | 19m |
| N682AC |  | Bb Airpark (TE88) | Bb Airpark (TE88) | 2026-07-04 16:11 UTC | 2026-07-04 16:24 UTC | 13m |
| XBPDM | XBP | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-07-04 15:53 UTC | 2026-07-04 16:17 UTC | 24m |
| SXS224 | SXS | Antalya International Airport (LTAI) | HE42 (HE42) | 2026-07-04 15:03 UTC | 2026-07-04 16:13 UTC | 1h 10m |
| N800GY |  | Jim Sears Airport (3TA7) | Bowie Municipal Airport (K0F2) | 2026-07-04 15:56 UTC | 2026-07-04 16:10 UTC | 14m |
| N201UT |  | Watts-Woodland Airport (KO41) | Yolo County Airport (KDWA) | 2026-07-04 15:29 UTC | 2026-07-04 16:07 UTC | 38m |
| N423PW |  | Flying E Airport (OR25) | OR19 (OR19) | 2026-07-04 15:14 UTC | 2026-07-04 16:04 UTC | 49m |
| N3515S |  | Corona Municipal Airport (KAJO) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-07-04 14:59 UTC | 2026-07-04 16:03 UTC | 1h 3m |
| FHUHU | FHU | Hamburg Airport (EDDH) | Uetersen/Heist Airport (EDHE) | 2026-07-04 15:36 UTC | 2026-07-04 15:59 UTC | 23m |
| N355PR |  | Waukesha County Airport (KUES) | Terry's Airport (3IG3) | 2026-07-04 15:11 UTC | 2026-07-04 15:57 UTC | 46m |
| N234GC |  | French Valley Airport (KF70) | French Valley Airport (KF70) | 2026-07-04 15:50 UTC | 2026-07-04 15:54 UTC | 3m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-04 14:55 UTC | 2026-07-04 15:47 UTC | 52m |
| SD1 |  | 52TA (52TA) | 52TA (52TA) | 2026-07-04 13:30 UTC | 2026-07-04 15:43 UTC | 2h 12m |
| N352TS |  | Billings Logan International Airport (KBIL) | Johnson County Airport (KBYG) | 2026-07-04 13:52 UTC | 2026-07-04 15:39 UTC | 1h 47m |
| N747DW |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-07-04 15:08 UTC | 2026-07-04 15:39 UTC | 30m |
| N953AL |  | Felts Field (KSFF) | Felts Field (KSFF) | 2026-07-04 15:34 UTC | 2026-07-04 15:36 UTC | 2m |
| N3802C |  | Tanner Field (CO27) | Tanner Field (CO27) | 2026-07-04 15:29 UTC | 2026-07-04 15:35 UTC | 5m |
| N407WF |  | Pueblo Memorial Airport (KPUB) | Ak Su Airport (CO61) | 2026-07-04 14:56 UTC | 2026-07-04 15:35 UTC | 38m |
| ABY222 | ABY | Nariya Airport (OENR) | Sirri Island Airport (OIBS) | 2026-07-04 14:53 UTC | 2026-07-04 15:34 UTC | 40m |
| FHPCJ | FHP | Marennes Le Bournet Airport (LFJI) | Rochefort-Saint-Agnant (BA 721) Airport (LFDN) | 2026-07-04 14:57 UTC | 2026-07-04 15:34 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
