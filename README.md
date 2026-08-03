# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_19:38:54_UTC-green)

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

**Latest saved flight:** 2026-08-03 19:38:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 19:38:54 UTC

- **169,170** saved flights
- **55,222** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **169,170** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,038,819.6 tonnes** estimated CO2 emissions
- **118,192,440 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6752 |
| 2 | SkyWest Airlines | 6179 |
| 3 | EJA | 3363 |
| 4 | IndiGo | 2980 |
| 5 | American Airlines | 2666 |
| 6 | Southwest Airlines | 2661 |
| 7 | ENY | 2105 |
| 8 | Delta Air Lines | 2017 |
| 9 | LATAM Airlines | 1569 |
| 10 | Lufthansa | 1557 |
| 11 | AZU | 1485 |
| 12 | WIF | 1418 |
| 13 | Vueling | 1393 |
| 14 | LXJ | 1326 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1157 |
| 17 | easyJet | 1139 |
| 18 | EJU | 1038 |
| 19 | Alaska Airlines | 1033 |
| 20 | QLK | 1028 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 934 |
| 23 | Cathay Pacific | 902 |
| 24 | CXK | 896 |
| 25 | United Airlines | 891 |
| 26 | AEE | 887 |
| 27 | GLO | 886 |
| 28 | Air France | 871 |
| 29 | MXY | 866 |
| 30 | JetBlue | 852 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145824 |
| 2 | 🇪🇸 ES | 10851 |
| 3 | 🇧🇷 BR | 9617 |
| 4 | 🇦🇺 AU | 9409 |
| 5 | 🇮🇳 IN | 9331 |
| 6 | 🇨🇦 CA | 9163 |
| 7 | 🇮🇹 IT | 8742 |
| 8 | 🇩🇪 DE | 8438 |
| 9 | 🇬🇧 GB | 7870 |
| 10 | 🇯🇵 JP | 6788 |
| 11 | 🇫🇷 FR | 6707 |
| 12 | 🇨🇴 CO | 6119 |
| 13 | 🇬🇷 GR | 4919 |
| 14 | 🇲🇽 MX | 4845 |
| 15 | 🇨🇭 CH | 4460 |
| 16 | 🇳🇴 NO | 4424 |
| 17 | 🇹🇷 TR | 4105 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2854 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇹🇭 TH | 2458 |
| 22 | 🇳🇿 NZ | 2448 |
| 23 | 🇵🇭 PH | 2235 |
| 24 | 🇬🇹 GT | 2189 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1709 |
| 27 | 🇭🇷 HR | 1630 |
| 28 | 🇲🇪 ME | 1565 |
| 29 | 🇳🇱 NL | 1540 |
| 30 | 🇲🇴 MO | 1435 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3474 |
| 2 | Denver International Airport |  | US | 2807 |
| 3 | Tokyo International Airport |  | JP | 2132 |
| 4 | Guaymaral Airport |  | CO | 2105 |
| 5 | Indira Gandhi International Airport |  | IN | 2067 |
| 6 | Harry Reid International Airport |  | US | 2032 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1853 |
| 8 | Zurich Airport |  | CH | 1797 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1780 |
| 10 | La Aurora Airport |  | GT | 1689 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1557 |
| 12 | El Dorado International Airport |  | CO | 1533 |
| 13 | Chicago O'Hare International Airport |  | US | 1533 |
| 14 | Salt Lake City International Airport |  | US | 1518 |
| 15 | Frankfurt am Main International Airport |  | DE | 1516 |
| 16 | Macau International Airport |  | MO | 1435 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1397 |
| 18 | Congonhas Airport |  | BR | 1384 |
| 19 | Madrid Barajas International Airport |  | ES | 1333 |
| 20 | Capua Airport |  | IT | 1318 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1281 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1196 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1180 |
| 25 | Charles de Gaulle International Airport |  | FR | 1150 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1141 |
| 28 | Bengaluru International Airport |  | IN | 1108 |
| 29 | Ninoy Aquino International Airport |  | PH | 1051 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1048 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1044 |
| 32 | Barcelona International Airport |  | ES | 1003 |
| 33 | Daniel K Inouye International Airport |  | US | 983 |
| 34 | Seattle-Tacoma International Airport |  | US | 980 |
| 35 | Viracopos International Airport |  | BR | 962 |
| 36 | Calgary International Airport |  | CA | 956 |
| 37 | Reno/Tahoe International Airport |  | US | 943 |
| 38 | Tenerife Norte Airport |  | ES | 942 |
| 39 | Oslo Gardermoen Airport |  | NO | 940 |
| 40 | Scottsdale Airport |  | US | 934 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 874 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 616 | 21m | 244 km | 2,593.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 403 | 24m | 225 km | 1,563.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 403 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 250 | 44m | 241 km | 1,038.5 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 233 | 1h 47m | 1,423 km | 5,718.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 215 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 201 | 19m | 144 km | 500.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 199 | 1h 15m | 961 km | 3,298.5 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 197 | 50m | 556 km | 1,888.4 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 189 | 1h 38m | 1,156 km | 3,770.5 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SMALL11 | SMA | 2TX3 (2TX3) | Benson Airstrip (2XS8) | 2026-08-03 19:14 UTC | 2026-08-03 19:38 UTC | 24m |
| ERU83 | ERU | Prescott Regional/Ernest A Love Field (KPRC) | 42AZ (42AZ) | 2026-08-03 19:13 UTC | 2026-08-03 19:35 UTC | 22m |
| ENSA47 | ENS | Santa Paula Airport (SISP) | Mirassol Airport (SDMH) | 2026-08-03 19:20 UTC | 2026-08-03 19:32 UTC | 11m |
| AAE123 | AAE | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-08-03 08:10 UTC | 2026-08-03 19:32 UTC | 11h 21m |
| TKR15 | TKR | Hill Afb Airport (KHIF) | K43U (K43U) | 2026-08-03 19:11 UTC | 2026-08-03 19:28 UTC | 16m |
| CGTZB | CGT | Woodstock Airport (CPR5) | Woodstock Airport (CPR5) | 2026-08-03 19:12 UTC | 2026-08-03 19:26 UTC | 14m |
| N760C |  | Dickson Municipal Airport (KM02) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-08-03 18:09 UTC | 2026-08-03 19:23 UTC | 1h 13m |
| N650HF |  | Bob Hope Airport (KBUR) | General Wm J Fox Airfield (KWJF) | 2026-08-03 19:09 UTC | 2026-08-03 19:19 UTC | 10m |
| N80790 |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-08-03 18:41 UTC | 2026-08-03 19:19 UTC | 37m |
| N77ZR |  | Creve Coeur Airport (K1H0) | Blackhawk Airport (6MO0) | 2026-08-03 19:10 UTC | 2026-08-03 19:18 UTC | 8m |
| N115AH |  | CD82 (CD82) | CD82 (CD82) | 2026-08-03 19:04 UTC | 2026-08-03 19:17 UTC | 12m |
| ENSAIO17 | ENS | Professor Urbano Ernesto Stumpf Airport (SBSJ) | Helibras Airport (SIYS) | 2026-08-03 18:45 UTC | 2026-08-03 19:16 UTC | 30m |
| N550SE |  | Montgomery-Gibbs Executive Airport (KMYF) | 51CA (51CA) | 2026-08-03 18:45 UTC | 2026-08-03 19:16 UTC | 31m |
| IGO9023 | IndiGo | Chaudhary Charan Singh International Airport (VILK) | Chaudhary Charan Singh International Airport (VILK) | 2026-08-03 18:46 UTC | 2026-08-03 19:15 UTC | 28m |
| N3956S |  | Kapowsin Field (86WA) | Auburn Municipal Airport (KS50) | 2026-08-03 18:57 UTC | 2026-08-03 19:13 UTC | 15m |
| N548PW |  | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-08-03 18:30 UTC | 2026-08-03 19:13 UTC | 42m |
| N9636V |  | Naper Aero Club Airport (LL10) | Morris Municipal/James R Washburn Field (KC09) | 2026-08-03 18:57 UTC | 2026-08-03 19:12 UTC | 14m |
| VTM627 | VTM | Plan De Guadalupe International Airport (MMIO) | Monclova International Airport (MMMV) | 2026-08-03 18:44 UTC | 2026-08-03 19:11 UTC | 26m |
| SHAHD268 | SHA | King Hussein Air College (OJMF) | Prince Hasan Air Base (OJHF) | 2026-08-03 18:57 UTC | 2026-08-03 19:11 UTC | 13m |
| EDC310E | EDC | Malaga Airport (LEMG) | Farnborough Airport (EGLF) | 2026-08-03 16:53 UTC | 2026-08-03 19:09 UTC | 2h 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
