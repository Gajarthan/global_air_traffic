# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_16:56:25_UTC-green)

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

**Latest saved flight:** 2026-08-10 16:56:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 16:56:25 UTC

- **184,504** saved flights
- **58,708** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **184,504** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,216,482.9 tonnes** estimated CO2 emissions
- **128,491,763 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7322 |
| 2 | SkyWest Airlines | 6701 |
| 3 | EJA | 3641 |
| 4 | IndiGo | 3236 |
| 5 | Southwest Airlines | 2889 |
| 6 | American Airlines | 2876 |
| 7 | ENY | 2299 |
| 8 | Delta Air Lines | 2175 |
| 9 | LATAM Airlines | 1727 |
| 10 | AZU | 1655 |
| 11 | Lufthansa | 1625 |
| 12 | WIF | 1529 |
| 13 | Vueling | 1522 |
| 14 | LXJ | 1453 |
| 15 | easyJet | 1267 |
| 16 | Swiss International | 1265 |
| 17 | AXM | 1235 |
| 18 | EJU | 1138 |
| 19 | QLK | 1135 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1015 |
| 23 | GLO | 986 |
| 24 | AEE | 960 |
| 25 | Air France | 959 |
| 26 | CXK | 956 |
| 27 | Cathay Pacific | 947 |
| 28 | PGT | 943 |
| 29 | United Airlines | 941 |
| 30 | MXY | 916 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 157571 |
| 2 | 🇪🇸 ES | 11861 |
| 3 | 🇧🇷 BR | 10592 |
| 4 | 🇦🇺 AU | 10306 |
| 5 | 🇮🇳 IN | 10138 |
| 6 | 🇨🇦 CA | 10038 |
| 7 | 🇮🇹 IT | 9532 |
| 8 | 🇩🇪 DE | 9130 |
| 9 | 🇬🇧 GB | 8571 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7382 |
| 12 | 🇨🇴 CO | 6919 |
| 13 | 🇬🇷 GR | 5416 |
| 14 | 🇲🇽 MX | 5264 |
| 15 | 🇨🇭 CH | 4939 |
| 16 | 🇹🇷 TR | 4825 |
| 17 | 🇳🇴 NO | 4752 |
| 18 | 🇲🇾 MY | 3219 |
| 19 | 🇿🇦 ZA | 3100 |
| 20 | 🇵🇱 PL | 3085 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2441 |
| 24 | 🇬🇹 GT | 2362 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1865 |
| 27 | 🇭🇷 HR | 1853 |
| 28 | 🇲🇪 ME | 1666 |
| 29 | 🇳🇱 NL | 1654 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3824 |
| 2 | Denver International Airport |  | US | 3043 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2272 |
| 5 | Guaymaral Airport |  | CO | 2253 |
| 6 | Harry Reid International Airport |  | US | 2158 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1980 |
| 8 | Zurich Airport |  | CH | 1975 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1911 |
| 10 | La Aurora Airport |  | GT | 1811 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1677 |
| 12 | El Dorado International Airport |  | CO | 1655 |
| 13 | Salt Lake City International Airport |  | US | 1643 |
| 14 | Chicago O'Hare International Airport |  | US | 1642 |
| 15 | Frankfurt am Main International Airport |  | DE | 1594 |
| 16 | Congonhas Airport |  | BR | 1535 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 19 | Madrid Barajas International Airport |  | ES | 1451 |
| 20 | Capua Airport |  | IT | 1446 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1377 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1320 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1274 |
| 25 | Charles de Gaulle International Airport |  | FR | 1260 |
| 26 | Charlotte/Douglas International Airport |  | US | 1250 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1152 |
| 30 | Ninoy Aquino International Airport |  | PH | 1151 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1130 |
| 32 | Barcelona International Airport |  | ES | 1094 |
| 33 | Viracopos International Airport |  | BR | 1062 |
| 34 | Seattle-Tacoma International Airport |  | US | 1059 |
| 35 | Reno/Tahoe International Airport |  | US | 1054 |
| 36 | Calgary International Airport |  | CA | 1049 |
| 37 | Daniel K Inouye International Airport |  | US | 1048 |
| 38 | Oslo Gardermoen Airport |  | NO | 1028 |
| 39 | Tenerife Norte Airport |  | ES | 1006 |
| 40 | Amsterdam Airport Schiphol |  | NL | 998 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 929 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 676 | 21m | 244 km | 2,846.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 428 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 310 | 27m | 275 km | 1,469.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 275 | 44m | 241 km | 1,142.3 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 269 | 22m | 55 km | 255.7 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 260 | 1h 49m | 1,423 km | 6,380.8 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 260 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 225 | 1h 15m | 961 km | 3,729.5 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 221 | 19m | 144 km | 549.7 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 218 | 24m | 218 km | 821.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N390EA |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-10 16:06 UTC | 2026-08-10 16:56 UTC | 49m |
| N472LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Van Nuys Airport (KVNY) | 2026-08-10 15:42 UTC | 2026-08-10 16:51 UTC | 1h 8m |
| N441MG |  | Aero Country Airport (KT31) | Jones Field (KF00) | 2026-08-10 15:51 UTC | 2026-08-10 16:47 UTC | 56m |
| TIGER03 | TIG | Sandy Creek Airport (73TX) | Dunbar Ranch Airport (0XS8) | 2026-08-10 16:24 UTC | 2026-08-10 16:47 UTC | 22m |
| N613HT |  | Spirit Of St Louis Airport (KSUS) | OK18 (OK18) | 2026-08-10 15:12 UTC | 2026-08-10 16:46 UTC | 1h 34m |
| N734NJ |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-10 16:15 UTC | 2026-08-10 16:43 UTC | 28m |
| 09526656 |  | Dee Jay Airport (8PA1) | Capital City Airport (KCXY) | 2026-08-10 16:13 UTC | 2026-08-10 16:39 UTC | 25m |
| SAMU44 | SAM | Nantes Atlantique Airport (LFRS) | Nantes Atlantique Airport (LFRS) | 2026-08-10 16:33 UTC | 2026-08-10 16:35 UTC | 1m |
| CGNUE | CGN | Brampton Airport (CNC3) | Brampton Airport (CNC3) | 2026-08-10 15:38 UTC | 2026-08-10 16:33 UTC | 55m |
| N566BG |  | Leesburg Executive Airport (KJYO) | Leesburg Executive Airport (KJYO) | 2026-08-10 15:59 UTC | 2026-08-10 16:28 UTC | 29m |
| N4577 |  | Plymouth Municipal Airport (KC65) | Plymouth Municipal Airport (KC65) | 2026-08-10 16:12 UTC | 2026-08-10 16:24 UTC | 12m |
| GSGCB | GSG | Shoreham Airport (EGKA) | Deanland Lewes Airport (EGKL) | 2026-08-10 16:12 UTC | 2026-08-10 16:24 UTC | 11m |
| N892PA |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-08-10 15:54 UTC | 2026-08-10 16:22 UTC | 28m |
| CLOVE1 | CLO | Randolph Afb Airport (KRND) | Lobo Mountain Ranch Airport (TE21) | 2026-08-10 16:10 UTC | 2026-08-10 16:21 UTC | 10m |
| N679W |  | Modesto City-County-Harry Sham Field (KMOD) | Redfield Municipal Airport (K1D8) | 2026-08-10 13:58 UTC | 2026-08-10 16:20 UTC | 2h 22m |
| WIF9HT | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-08-10 16:09 UTC | 2026-08-10 16:20 UTC | 11m |
| N711SR |  | Salt Lake City International Airport (KSLC) | Morgan County Airport (K42U) | 2026-08-10 15:52 UTC | 2026-08-10 16:19 UTC | 26m |
| N18ZD |  | 4Z Ranch Airport (30ID) | Dalhart Municipal Airport (KDHT) | 2026-08-10 14:48 UTC | 2026-08-10 16:17 UTC | 1h 28m |
| N116UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-10 15:18 UTC | 2026-08-10 16:16 UTC | 58m |
| N920CF |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-10 16:12 UTC | 2026-08-10 16:16 UTC | 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
