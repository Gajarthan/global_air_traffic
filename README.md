# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_20:26:17_UTC-green)

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

**Latest saved flight:** 2026-08-15 20:26:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 20:26:17 UTC

- **199,860** saved flights
- **62,389** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,860** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,388,033.7 tonnes** estimated CO2 emissions
- **138,436,734 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7963 |
| 2 | SkyWest Airlines | 7175 |
| 3 | EJA | 3921 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3093 |
| 6 | American Airlines | 3084 |
| 7 | ENY | 2471 |
| 8 | Delta Air Lines | 2364 |
| 9 | LATAM Airlines | 1881 |
| 10 | AZU | 1819 |
| 11 | Lufthansa | 1708 |
| 12 | Vueling | 1680 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1587 |
| 15 | easyJet | 1378 |
| 16 | Swiss International | 1349 |
| 17 | AXM | 1308 |
| 18 | EJU | 1240 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1107 |
| 23 | GLO | 1086 |
| 24 | Air France | 1063 |
| 25 | PGT | 1056 |
| 26 | AEE | 1030 |
| 27 | United Airlines | 1016 |
| 28 | CXK | 1010 |
| 29 | WMT | 1009 |
| 30 | Wizz Air | 991 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 169381 |
| 2 | 🇪🇸 ES | 12923 |
| 3 | 🇧🇷 BR | 11533 |
| 4 | 🇦🇺 AU | 11150 |
| 5 | 🇨🇦 CA | 10930 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10502 |
| 8 | 🇩🇪 DE | 9923 |
| 9 | 🇬🇧 GB | 9389 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7982 |
| 12 | 🇨🇴 CO | 7975 |
| 13 | 🇬🇷 GR | 5901 |
| 14 | 🇲🇽 MX | 5653 |
| 15 | 🇹🇷 TR | 5561 |
| 16 | 🇨🇭 CH | 5412 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3304 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2549 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2132 |
| 27 | 🇲🇦 MA | 2029 |
| 28 | 🇳🇱 NL | 1798 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4168 |
| 2 | Denver International Airport |  | US | 3250 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2471 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2275 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2114 |
| 8 | Zurich Airport |  | CH | 2108 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2066 |
| 10 | La Aurora Airport |  | GT | 1952 |
| 11 | El Dorado International Airport |  | CO | 1845 |
| 12 | Salt Lake City International Airport |  | US | 1777 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1776 |
| 14 | Chicago O'Hare International Airport |  | US | 1756 |
| 15 | Congonhas Airport |  | BR | 1687 |
| 16 | Frankfurt am Main International Airport |  | DE | 1680 |
| 17 | Madrid Barajas International Airport |  | ES | 1577 |
| 18 | Capua Airport |  | IT | 1539 |
| 19 | Macau International Airport |  | MO | 1536 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1514 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1471 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1445 |
| 23 | Malpensa International Airport |  | IT | 1396 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1383 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1318 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1249 |
| 30 | Ninoy Aquino International Airport |  | PH | 1248 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1219 |
| 32 | Barcelona International Airport |  | ES | 1204 |
| 33 | Viracopos International Airport |  | BR | 1166 |
| 34 | Seattle-Tacoma International Airport |  | US | 1143 |
| 35 | Calgary International Airport |  | CA | 1136 |
| 36 | Reno/Tahoe International Airport |  | US | 1124 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1116 |
| 39 | Daniel K Inouye International Airport |  | US | 1102 |
| 40 | Tenerife Norte Airport |  | ES | 1095 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1018 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 488 | 1h 7m | 770 km | 6,482.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 465 | 24m | 225 km | 1,804.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 465 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 379 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 341 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 292 | 1h 49m | 1,423 km | 7,166.1 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 286 | 22m | 55 km | 271.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 250 | 24m | 218 km | 941.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 244 | 1h 14m | 961 km | 4,044.4 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 244 | 19m | 99 km | 418.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 238 | 1h 37m | 1,156 km | 4,748.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 217 | 1h 48m | 1,304 km | 4,881.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N38EE |  | Minden-Tahoe Airport (KMEV) | Sweetwater (Usmc) Airport (NV72) | 2026-08-15 19:28 UTC | 2026-08-15 20:26 UTC | 58m |
| MSR688 | EgyptAir | Cairo International Airport (HECA) | HE13 (HE13) | 2026-08-15 14:15 UTC | 2026-08-15 20:17 UTC | 6h 2m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-15 18:48 UTC | 2026-08-15 20:14 UTC | 1h 25m |
| RGA14 | RGA | Zweisimmen Airport (LSTZ) | Reichenbach Air Base (LSGR) | 2026-08-15 19:53 UTC | 2026-08-15 20:12 UTC | 18m |
| N539LC |  | Elkhart Municipal Airport (KEKM) | Cherry Capital Airport (KTVC) | 2026-08-15 19:41 UTC | 2026-08-15 20:11 UTC | 30m |
| N21ME |  | Wichita Dwight D Eisenhower Ntl Airport (KICT) | Eglin Aux Field 6 Airport (FL34) | 2026-08-15 18:24 UTC | 2026-08-15 20:09 UTC | 1h 45m |
| MSC304 | MSC | Istanbul Airport (LTFM) | HE12 (HE12) | 2026-08-15 18:29 UTC | 2026-08-15 20:07 UTC | 1h 37m |
| N4287A |  | Santa Fe Regional Airport (KSAF) | K0E8 (K0E8) | 2026-08-15 19:35 UTC | 2026-08-15 20:06 UTC | 30m |
| SWR9H | Swiss International | Geneva Cointrin International Airport (LSGG) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-15 19:23 UTC | 2026-08-15 20:04 UTC | 41m |
| JTZ807 | JTZ | Stennis International Airport (KHSA) | Copiah County Airport (KM11) | 2026-08-15 19:47 UTC | 2026-08-15 20:04 UTC | 17m |
| N16NW |  | Cecil Ranch Airport (37CN) | Independence Airport (K2O7) | 2026-08-15 15:49 UTC | 2026-08-15 20:03 UTC | 4h 13m |
| TKJ8FS | TKJ | Sabiha Gokcen International Airport (LTFJ) | HE42 (HE42) | 2026-08-15 18:28 UTC | 2026-08-15 20:00 UTC | 1h 32m |
| DAL2282 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Alpine Airport (K46U) | 2026-08-15 19:37 UTC | 2026-08-15 19:59 UTC | 22m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-15 19:43 UTC | 2026-08-15 19:58 UTC | 15m |
| EFY7836 | EFY | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-08-15 19:30 UTC | 2026-08-15 19:58 UTC | 28m |
| RYR7GU | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Paris Beauvais Tille Airport (LFOB) | 2026-08-15 18:06 UTC | 2026-08-15 19:57 UTC | 1h 51m |
| NSE8690 | NSE | El Dorado International Airport (SKBO) | SKSR (SKSR) | 2026-08-15 18:47 UTC | 2026-08-15 19:56 UTC | 1h 8m |
| C6018 |  | Noatak Airport (PAWN) | Ralph Wien Memorial Airport (PAOT) | 2026-08-15 19:28 UTC | 2026-08-15 19:55 UTC | 27m |
| EJA690 | EJA | Laconia Municipal Airport (KLCI) | Matzie Airport (30MO) | 2026-08-15 17:19 UTC | 2026-08-15 19:55 UTC | 2h 36m |
| N920FC |  | Table Mountain Field (5CL9) | Baker & Hall Airport (77CL) | 2026-08-15 19:48 UTC | 2026-08-15 19:54 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
