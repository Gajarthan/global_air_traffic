# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_17:44:26_UTC-green)

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

**Latest saved flight:** 2026-05-29 17:44:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-29 17:44:26 UTC

- **96,761** saved flights
- **34,014** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **96,761** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,184,285.1 tonnes** estimated CO2 emissions
- **68,654,211 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4061 |
| 2 | SkyWest Airlines | 3594 |
| 3 | IndiGo | 1998 |
| 4 | EJA | 1829 |
| 5 | American Airlines | 1462 |
| 6 | Southwest Airlines | 1405 |
| 7 | ENY | 1190 |
| 8 | Lufthansa | 1155 |
| 9 | Delta Air Lines | 1056 |
| 10 | Vueling | 914 |
| 11 | LATAM Airlines | 865 |
| 12 | WIF | 859 |
| 13 | AXM | 854 |
| 14 | AZU | 782 |
| 15 | LXJ | 738 |
| 16 | Swiss International | 719 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 673 |
| 19 | QLK | 669 |
| 20 | easyJet | 632 |
| 21 | EJU | 614 |
| 22 | Cathay Pacific | 584 |
| 23 | AEE | 582 |
| 24 | VIV | 571 |
| 25 | Air France | 569 |
| 26 | CXK | 519 |
| 27 | MXY | 512 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 488 |
| 30 | AIQ | 465 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 79997 |
| 2 | 🇪🇸 ES | 6753 |
| 3 | 🇮🇳 IN | 6310 |
| 4 | 🇦🇺 AU | 5922 |
| 5 | 🇧🇷 BR | 5322 |
| 6 | 🇩🇪 DE | 5309 |
| 7 | 🇮🇹 IT | 5226 |
| 8 | 🇨🇦 CA | 4923 |
| 9 | 🇯🇵 JP | 4599 |
| 10 | 🇬🇧 GB | 4146 |
| 11 | 🇫🇷 FR | 3929 |
| 12 | 🇨🇴 CO | 3355 |
| 13 | 🇲🇽 MX | 2968 |
| 14 | 🇬🇷 GR | 2796 |
| 15 | 🇳🇴 NO | 2724 |
| 16 | 🇨🇭 CH | 2544 |
| 17 | 🇲🇾 MY | 2170 |
| 18 | 🇹🇷 TR | 1803 |
| 19 | 🇿🇦 ZA | 1731 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1639 |
| 22 | 🇰🇷 KR | 1589 |
| 23 | 🇵🇱 PL | 1580 |
| 24 | 🇵🇭 PH | 1455 |
| 25 | 🇬🇹 GT | 1448 |
| 26 | 🇲🇦 MA | 1093 |
| 27 | 🇲🇴 MO | 1041 |
| 28 | 🇳🇱 NL | 972 |
| 29 | 🇲🇪 ME | 949 |
| 30 | 🇭🇷 HR | 876 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2093 |
| 2 | Denver International Airport |  | US | 1633 |
| 3 | Tokyo International Airport |  | JP | 1524 |
| 4 | Indira Gandhi International Airport |  | IN | 1367 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1280 |
| 6 | Harry Reid International Airport |  | US | 1242 |
| 7 | Guaymaral Airport |  | CO | 1194 |
| 8 | Frankfurt am Main International Airport |  | DE | 1166 |
| 9 | Zurich Airport |  | CH | 1131 |
| 10 | La Aurora Airport |  | GT | 1110 |
| 11 | El Dorado International Airport |  | CO | 1042 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1041 |
| 13 | Macau International Airport |  | MO | 1041 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 968 |
| 15 | Chicago O'Hare International Airport |  | US | 927 |
| 16 | Kuala Lumpur International Airport |  | MY | 858 |
| 17 | Madrid Barajas International Airport |  | ES | 854 |
| 18 | Salt Lake City International Airport |  | US | 814 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 810 |
| 20 | Capua Airport |  | IT | 801 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Bengaluru International Airport |  | IN | 755 |
| 23 | Malpensa International Airport |  | IT | 754 |
| 24 | Charles de Gaulle International Airport |  | FR | 751 |
| 25 | Congonhas Airport |  | BR | 737 |
| 26 | Charlotte/Douglas International Airport |  | US | 735 |
| 27 | Daniel K Inouye International Airport |  | US | 687 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 646 |
| 31 | Barcelona International Airport |  | ES | 646 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 623 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 617 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 35 | Don Mueang International Airport |  | TH | 600 |
| 36 | Amsterdam Airport Schiphol |  | NL | 599 |
| 37 | Vitoria/Foronda Airport |  | ES | 596 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 571 |
| 39 | Calgary International Airport |  | CA | 570 |
| 40 | O. R. Tambo International Airport |  | ZA | 551 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 492 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 357 | 21m | 244 km | 1,503.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 258 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 246 | 14m | 114 km | 482.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 192 | 26m | 275 km | 909.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 140 | 22m | 55 km | 133.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 139 | 27m | 152 km | 363.3 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 132 | 20m | 250 km | 570.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 127 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 124 | 18m | 144 km | 308.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 123 | 1h 39m | 1,156 km | 2,453.8 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 28 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N520MD |  | Savannah/Hilton Head International Airport (KSAV) | Savannah/Hilton Head International Airport (KSAV) | 2026-05-29 17:33 UTC | 2026-05-29 17:44 UTC | 10m |
| N3717R |  | CL36 (CL36) | CL36 (CL36) | 2026-05-29 17:25 UTC | 2026-05-29 17:42 UTC | 17m |
| N642PF |  | Brandywine Regional Airport (KOQN) | Princeton Airport (K39N) | 2026-05-29 17:08 UTC | 2026-05-29 17:41 UTC | 32m |
| HK4412 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-29 17:27 UTC | 2026-05-29 17:38 UTC | 10m |
| N133PS |  | Waukesha County Airport (KUES) | Sss Aerodrome (WI62) | 2026-05-29 17:17 UTC | 2026-05-29 17:32 UTC | 15m |
| N338XA |  | Mesa Gateway Airport (KIWA) | Payson Airport (KPAN) | 2026-05-29 16:58 UTC | 2026-05-29 17:31 UTC | 32m |
| N636CM |  | Chicago Executive Airport (KPWK) | Campbell Airport (KC81) | 2026-05-29 16:54 UTC | 2026-05-29 17:24 UTC | 30m |
| N1882S |  | Van Nuys Airport (KVNY) | San Bernardino International Airport (KSBD) | 2026-05-29 16:47 UTC | 2026-05-29 17:23 UTC | 36m |
| N993FG |  | Raleigh-Durham International Airport (KRDU) | Triangle North Executive Airport (KLHZ) | 2026-05-29 16:44 UTC | 2026-05-29 17:21 UTC | 37m |
| C2703 |  | Mc Clellan Airfield (KMCC) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-05-29 16:05 UTC | 2026-05-29 17:13 UTC | 1h 7m |
| N477UV |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-05-29 16:45 UTC | 2026-05-29 17:12 UTC | 26m |
| N481MR |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-05-29 16:29 UTC | 2026-05-29 17:12 UTC | 42m |
| N22182 |  | Rimrock Airport (48AZ) | Phoenix Deer Valley Airport (KDVT) | 2026-05-29 16:42 UTC | 2026-05-29 17:10 UTC | 27m |
| OEFEG | OEF | Catania / Fontanarossa Airport (LICC) | Crotone Airport (LIBC) | 2026-05-29 16:45 UTC | 2026-05-29 17:08 UTC | 23m |
| AATK309 | AAT | AZ86 (AZ86) | Payson Airport (KPAN) | 2026-05-29 16:54 UTC | 2026-05-29 17:08 UTC | 14m |
| N600XT |  | Dayton/Wright Brothers Airport (KMGY) | Roscommon County/Blodgett Memorial Airport (KHTL) | 2026-05-29 16:05 UTC | 2026-05-29 17:07 UTC | 1h 1m |
| N510PR |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-29 16:26 UTC | 2026-05-29 17:05 UTC | 39m |
| N814SS |  | Beluga Airport (PABG) | Nikolai Creek Airport (9AK3) | 2026-05-29 16:55 UTC | 2026-05-29 17:05 UTC | 9m |
| N9531J |  | Mckinney Ntl Airport (KTKI) | Grove Hill Airport (5TX2) | 2026-05-29 16:20 UTC | 2026-05-29 17:03 UTC | 42m |
| AEZ2627 | AEZ | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-05-29 16:23 UTC | 2026-05-29 17:02 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
