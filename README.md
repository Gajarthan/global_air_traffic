# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_19:13:15_UTC-green)

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

**Latest saved flight:** 2026-08-15 19:13:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 19:13:15 UTC

- **199,598** saved flights
- **62,324** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,598** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,384,509.0 tonnes** estimated CO2 emissions
- **138,232,408 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7951 |
| 2 | SkyWest Airlines | 7159 |
| 3 | EJA | 3917 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3088 |
| 6 | American Airlines | 3073 |
| 7 | ENY | 2465 |
| 8 | Delta Air Lines | 2357 |
| 9 | LATAM Airlines | 1880 |
| 10 | AZU | 1816 |
| 11 | Lufthansa | 1707 |
| 12 | Vueling | 1679 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1584 |
| 15 | easyJet | 1370 |
| 16 | Swiss International | 1346 |
| 17 | AXM | 1308 |
| 18 | EJU | 1237 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1104 |
| 23 | GLO | 1085 |
| 24 | Air France | 1062 |
| 25 | PGT | 1051 |
| 26 | AEE | 1028 |
| 27 | United Airlines | 1012 |
| 28 | CXK | 1010 |
| 29 | WMT | 1007 |
| 30 | Wizz Air | 989 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 169134 |
| 2 | 🇪🇸 ES | 12909 |
| 3 | 🇧🇷 BR | 11521 |
| 4 | 🇦🇺 AU | 11148 |
| 5 | 🇨🇦 CA | 10911 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10482 |
| 8 | 🇩🇪 DE | 9916 |
| 9 | 🇬🇧 GB | 9375 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7971 |
| 12 | 🇨🇴 CO | 7944 |
| 13 | 🇬🇷 GR | 5892 |
| 14 | 🇲🇽 MX | 5646 |
| 15 | 🇹🇷 TR | 5535 |
| 16 | 🇨🇭 CH | 5405 |
| 17 | 🇳🇴 NO | 5075 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3299 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2547 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2124 |
| 27 | 🇲🇦 MA | 2023 |
| 28 | 🇳🇱 NL | 1795 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4155 |
| 2 | Denver International Airport |  | US | 3242 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2466 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2273 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2111 |
| 8 | Zurich Airport |  | CH | 2107 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2062 |
| 10 | La Aurora Airport |  | GT | 1951 |
| 11 | El Dorado International Airport |  | CO | 1839 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1773 |
| 13 | Salt Lake City International Airport |  | US | 1772 |
| 14 | Chicago O'Hare International Airport |  | US | 1752 |
| 15 | Congonhas Airport |  | BR | 1687 |
| 16 | Frankfurt am Main International Airport |  | DE | 1679 |
| 17 | Madrid Barajas International Airport |  | ES | 1572 |
| 18 | Macau International Airport |  | MO | 1536 |
| 19 | Capua Airport |  | IT | 1533 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1513 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1467 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1442 |
| 23 | Malpensa International Airport |  | IT | 1393 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1382 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1317 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Ninoy Aquino International Airport |  | PH | 1248 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1247 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1216 |
| 32 | Barcelona International Airport |  | ES | 1203 |
| 33 | Viracopos International Airport |  | BR | 1165 |
| 34 | Seattle-Tacoma International Airport |  | US | 1142 |
| 35 | Calgary International Airport |  | CA | 1134 |
| 36 | Reno/Tahoe International Airport |  | US | 1123 |
| 37 | Oslo Gardermoen Airport |  | NO | 1119 |
| 38 | Vitoria/Foronda Airport |  | ES | 1113 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1095 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1016 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 375 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 337 | 27m | 275 km | 1,596.9 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 286 | 22m | 55 km | 271.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 249 | 24m | 218 km | 938.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 244 | 1h 14m | 961 km | 4,044.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 233 | 19m | 144 km | 579.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 216 | 28m | 152 km | 564.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AFR19LP | Air France | Eleftherios Venizelos International Airport (LGAV) | Troyes-Barberey Airport (LFQB) | 2026-08-15 16:05 UTC | 2026-08-15 19:13 UTC | 3h 7m |
| AFR44SZ | Air France | Charles de Gaulle International Airport (LFPG) | Tournus Cuisery Airport (LFFX) | 2026-08-15 18:13 UTC | 2026-08-15 19:13 UTC | 59m |
| AFR69ZL | Air France | Verona / Villafranca Airport (LIPX) | Chatillon Sur Seine Airport (LFQH) | 2026-08-15 17:58 UTC | 2026-08-15 19:13 UTC | 1h 14m |
| AFR87LF | Air France | Nice-Cote d'Azur Airport (LFMN) | Chatillon Sur Seine Airport (LFQH) | 2026-08-15 18:00 UTC | 2026-08-15 19:13 UTC | 1h 12m |
| EFW89WH | EFW | London Gatwick Airport (EGKK) | Puimoisson Airport (LFTP) | 2026-08-15 17:32 UTC | 2026-08-15 19:13 UTC | 1h 41m |
| ENT7LX | ENT | Warsaw Chopin Airport (EPWA) | Ruoms Airport (LFHF) | 2026-08-15 16:49 UTC | 2026-08-15 19:13 UTC | 2h 24m |
| EWG20H | EWG | Palma De Mallorca Airport (LEPA) | Reims-Prunay Airport (LFQA) | 2026-08-15 17:17 UTC | 2026-08-15 19:13 UTC | 1h 55m |
| EZS51CE | EZS | Cagliari / Elmas Airport (LIEE) | Ecuvillens Airport (LSGE) | 2026-08-15 17:40 UTC | 2026-08-15 19:13 UTC | 1h 32m |
| RYR19FE | Ryanair | Francisco de Sá Carneiro Airport (LPPR) | Torino / Caselle International Airport (LIMF) | 2026-08-15 16:57 UTC | 2026-08-15 19:13 UTC | 2h 16m |
| RYR65CN | Ryanair | Manchester Airport (EGCC) | Mulhouse-Habsheim Airport (LFGB) | 2026-08-15 17:34 UTC | 2026-08-15 19:13 UTC | 1h 38m |
| RYR970Y | Ryanair | Stockholm-Arlanda Airport (ESSA) | Avignon-Caumont Airport (LFMV) | 2026-08-15 16:01 UTC | 2026-08-15 19:13 UTC | 3h 11m |
| RYR9N | Ryanair | Brussels South Charleroi Airport (EBCI) | Grenoble-Isere Airport (LFLS) | 2026-08-15 17:51 UTC | 2026-08-15 19:13 UTC | 1h 22m |
| SAMU26 | SAM | Saint-Rambert-d'Albon Airport (LFLR) | Lyon Corbas Airport (LFHJ) | 2026-08-15 18:58 UTC | 2026-08-15 19:13 UTC | 14m |
| VOE4KJ | VOE | Bastia-Poretta Airport (LFKB) | Saint-Jean-en-Royans Airport (LFKE) | 2026-08-15 18:11 UTC | 2026-08-15 19:13 UTC | 1h 1m |
| N49TT |  | North Las Vegas Airport (KVGT) | Creech Afb Airport (KINS) | 2026-08-15 18:54 UTC | 2026-08-15 19:12 UTC | 17m |
| QTR61G | Qatar Airways | Hamad International Airport (OTHH) | Hulwan (HE15) | 2026-08-15 16:37 UTC | 2026-08-15 19:11 UTC | 2h 33m |
| N574SA |  | Livermore Municipal Airport (KLVK) | Merced Yosemite Regional Airport (KMCE) | 2026-08-15 18:31 UTC | 2026-08-15 19:06 UTC | 35m |
| N6409E |  | Chehalis-Centralia Airport (KCLS) | 20WA (20WA) | 2026-08-15 17:43 UTC | 2026-08-15 18:59 UTC | 1h 16m |
| ABY597 | ABY | Sharjah International Airport (OMSJ) | Hulwan (HE15) | 2026-08-15 15:59 UTC | 2026-08-15 18:56 UTC | 2h 57m |
| N113RF |  | Longbell Ranch Airport (2CL3) | Longbell Ranch Airport (2CL3) | 2026-08-15 18:24 UTC | 2026-08-15 18:55 UTC | 31m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
