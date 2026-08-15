# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_19:45:56_UTC-green)

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

**Latest saved flight:** 2026-08-15 19:45:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 19:45:56 UTC

- **199,718** saved flights
- **62,356** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,718** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,386,314.0 tonnes** estimated CO2 emissions
- **138,337,043 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7953 |
| 2 | SkyWest Airlines | 7166 |
| 3 | EJA | 3918 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3091 |
| 6 | American Airlines | 3078 |
| 7 | ENY | 2470 |
| 8 | Delta Air Lines | 2360 |
| 9 | LATAM Airlines | 1881 |
| 10 | AZU | 1816 |
| 11 | Lufthansa | 1708 |
| 12 | Vueling | 1679 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1585 |
| 15 | easyJet | 1374 |
| 16 | Swiss International | 1348 |
| 17 | AXM | 1308 |
| 18 | EJU | 1240 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1105 |
| 23 | GLO | 1085 |
| 24 | Air France | 1062 |
| 25 | PGT | 1053 |
| 26 | AEE | 1029 |
| 27 | United Airlines | 1016 |
| 28 | CXK | 1010 |
| 29 | WMT | 1007 |
| 30 | Wizz Air | 991 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 169254 |
| 2 | 🇪🇸 ES | 12917 |
| 3 | 🇧🇷 BR | 11525 |
| 4 | 🇦🇺 AU | 11148 |
| 5 | 🇨🇦 CA | 10926 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10488 |
| 8 | 🇩🇪 DE | 9922 |
| 9 | 🇬🇧 GB | 9382 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7972 |
| 12 | 🇨🇴 CO | 7951 |
| 13 | 🇬🇷 GR | 5897 |
| 14 | 🇲🇽 MX | 5650 |
| 15 | 🇹🇷 TR | 5548 |
| 16 | 🇨🇭 CH | 5408 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3300 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2549 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2128 |
| 27 | 🇲🇦 MA | 2024 |
| 28 | 🇳🇱 NL | 1796 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4160 |
| 2 | Denver International Airport |  | US | 3249 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2469 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2274 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2113 |
| 8 | Zurich Airport |  | CH | 2108 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2064 |
| 10 | La Aurora Airport |  | GT | 1952 |
| 11 | El Dorado International Airport |  | CO | 1840 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1775 |
| 13 | Salt Lake City International Airport |  | US | 1774 |
| 14 | Chicago O'Hare International Airport |  | US | 1754 |
| 15 | Congonhas Airport |  | BR | 1687 |
| 16 | Frankfurt am Main International Airport |  | DE | 1680 |
| 17 | Madrid Barajas International Airport |  | ES | 1575 |
| 18 | Macau International Airport |  | MO | 1536 |
| 19 | Capua Airport |  | IT | 1533 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1513 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1470 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1443 |
| 23 | Malpensa International Airport |  | IT | 1394 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1382 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1318 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1248 |
| 30 | Ninoy Aquino International Airport |  | PH | 1248 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1217 |
| 32 | Barcelona International Airport |  | ES | 1203 |
| 33 | Viracopos International Airport |  | BR | 1165 |
| 34 | Seattle-Tacoma International Airport |  | US | 1143 |
| 35 | Calgary International Airport |  | CA | 1136 |
| 36 | Reno/Tahoe International Airport |  | US | 1124 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1115 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1095 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1017 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 376 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 339 | 27m | 275 km | 1,606.4 t |
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
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 48m | 1,304 km | 4,859.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-15 16:39 UTC | 2026-08-15 19:45 UTC | 3h 6m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Hammonton Municipal Airport (KN81) | 2026-08-15 18:29 UTC | 2026-08-15 19:38 UTC | 1h 9m |
| IBS1903 | IBS | Madrid Barajas International Airport (LEMD) | HE12 (HE12) | 2026-08-15 15:37 UTC | 2026-08-15 19:37 UTC | 4h 0m |
| XSN40 | XSN | 6CL6 (6CL6) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-15 19:02 UTC | 2026-08-15 19:34 UTC | 32m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-08-15 18:58 UTC | 2026-08-15 19:33 UTC | 34m |
| N100JF |  | Plantation Airpark (KJYL) | Plantation Airpark (KJYL) | 2026-08-15 19:09 UTC | 2026-08-15 19:31 UTC | 21m |
| N708GC |  | Morgan County Airport (K42U) | Malad City Airport (KMLD) | 2026-08-15 19:01 UTC | 2026-08-15 19:27 UTC | 26m |
| N28UK |  | Ayresouth Airport (0GA3) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-08-15 19:20 UTC | 2026-08-15 19:27 UTC | 7m |
| N510PR |  | Mc Kinley Country Airport (81AK) | Helio Airport (2AK7) | 2026-08-15 18:46 UTC | 2026-08-15 19:15 UTC | 28m |
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

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
