# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_20:17:33_UTC-green)

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

**Latest saved flight:** 2026-08-15 20:17:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 20:17:33 UTC

- **199,808** saved flights
- **62,373** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **199,808** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,387,308.9 tonnes** estimated CO2 emissions
- **138,394,719 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7958 |
| 2 | SkyWest Airlines | 7174 |
| 3 | EJA | 3919 |
| 4 | IndiGo | 3446 |
| 5 | Southwest Airlines | 3093 |
| 6 | American Airlines | 3083 |
| 7 | ENY | 2470 |
| 8 | Delta Air Lines | 2362 |
| 9 | LATAM Airlines | 1881 |
| 10 | AZU | 1818 |
| 11 | Lufthansa | 1708 |
| 12 | Vueling | 1680 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1585 |
| 15 | easyJet | 1378 |
| 16 | Swiss International | 1348 |
| 17 | AXM | 1308 |
| 18 | EJU | 1240 |
| 19 | QLK | 1225 |
| 20 | All Nippon Airways | 1208 |
| 21 | Alaska Airlines | 1174 |
| 22 | VIV | 1105 |
| 23 | GLO | 1086 |
| 24 | Air France | 1062 |
| 25 | PGT | 1054 |
| 26 | AEE | 1030 |
| 27 | United Airlines | 1016 |
| 28 | CXK | 1010 |
| 29 | WMT | 1008 |
| 30 | Wizz Air | 991 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 169339 |
| 2 | 🇪🇸 ES | 12922 |
| 3 | 🇧🇷 BR | 11531 |
| 4 | 🇦🇺 AU | 11150 |
| 5 | 🇨🇦 CA | 10926 |
| 6 | 🇮🇳 IN | 10764 |
| 7 | 🇮🇹 IT | 10498 |
| 8 | 🇩🇪 DE | 9922 |
| 9 | 🇬🇧 GB | 9386 |
| 10 | 🇯🇵 JP | 8160 |
| 11 | 🇫🇷 FR | 7978 |
| 12 | 🇨🇴 CO | 7965 |
| 13 | 🇬🇷 GR | 5901 |
| 14 | 🇲🇽 MX | 5650 |
| 15 | 🇹🇷 TR | 5556 |
| 16 | 🇨🇭 CH | 5411 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3428 |
| 19 | 🇿🇦 ZA | 3370 |
| 20 | 🇵🇱 PL | 3301 |
| 21 | 🇹🇭 TH | 3131 |
| 22 | 🇳🇿 NZ | 2772 |
| 23 | 🇵🇭 PH | 2639 |
| 24 | 🇬🇹 GT | 2549 |
| 25 | 🇰🇷 KR | 2419 |
| 26 | 🇭🇷 HR | 2132 |
| 27 | 🇲🇦 MA | 2027 |
| 28 | 🇳🇱 NL | 1797 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1633 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4165 |
| 2 | Denver International Airport |  | US | 3250 |
| 3 | Tokyo International Airport |  | JP | 2495 |
| 4 | Guaymaral Airport |  | CO | 2471 |
| 5 | Indira Gandhi International Airport |  | IN | 2441 |
| 6 | Harry Reid International Airport |  | US | 2274 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2114 |
| 8 | Zurich Airport |  | CH | 2108 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2066 |
| 10 | La Aurora Airport |  | GT | 1952 |
| 11 | El Dorado International Airport |  | CO | 1841 |
| 12 | Salt Lake City International Airport |  | US | 1777 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1776 |
| 14 | Chicago O'Hare International Airport |  | US | 1755 |
| 15 | Congonhas Airport |  | BR | 1687 |
| 16 | Frankfurt am Main International Airport |  | DE | 1680 |
| 17 | Madrid Barajas International Airport |  | ES | 1577 |
| 18 | Capua Airport |  | IT | 1537 |
| 19 | Macau International Airport |  | MO | 1536 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1513 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1471 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1445 |
| 23 | Malpensa International Airport |  | IT | 1395 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1383 |
| 25 | Charles de Gaulle International Airport |  | FR | 1376 |
| 26 | Charlotte/Douglas International Airport |  | US | 1318 |
| 27 | Kuala Lumpur International Airport |  | MY | 1276 |
| 28 | Bengaluru International Airport |  | IN | 1256 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1248 |
| 30 | Ninoy Aquino International Airport |  | PH | 1248 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1218 |
| 32 | Barcelona International Airport |  | ES | 1204 |
| 33 | Viracopos International Airport |  | BR | 1165 |
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
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 378 | 8m | - | - |
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
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 48m | 1,304 km | 4,859.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MSR688 | EgyptAir | Cairo International Airport (HECA) | HE13 (HE13) | 2026-08-15 14:15 UTC | 2026-08-15 20:17 UTC | 6h 2m |
| JUMP16 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-15 18:48 UTC | 2026-08-15 20:14 UTC | 1h 25m |
| RGA14 | RGA | Zweisimmen Airport (LSTZ) | Reichenbach Air Base (LSGR) | 2026-08-15 19:53 UTC | 2026-08-15 20:12 UTC | 18m |
| MSC304 | MSC | Istanbul Airport (LTFM) | HE12 (HE12) | 2026-08-15 18:29 UTC | 2026-08-15 20:07 UTC | 1h 37m |
| N4287A |  | Santa Fe Regional Airport (KSAF) | K0E8 (K0E8) | 2026-08-15 19:35 UTC | 2026-08-15 20:06 UTC | 30m |
| N16NW |  | Cecil Ranch Airport (37CN) | Independence Airport (K2O7) | 2026-08-15 15:49 UTC | 2026-08-15 20:03 UTC | 4h 13m |
| TKJ8FS | TKJ | Sabiha Gokcen International Airport (LTFJ) | HE42 (HE42) | 2026-08-15 18:28 UTC | 2026-08-15 20:00 UTC | 1h 32m |
| DAL2282 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Alpine Airport (K46U) | 2026-08-15 19:37 UTC | 2026-08-15 19:59 UTC | 22m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-15 19:43 UTC | 2026-08-15 19:58 UTC | 15m |
| C6018 |  | Noatak Airport (PAWN) | Ralph Wien Memorial Airport (PAOT) | 2026-08-15 19:28 UTC | 2026-08-15 19:55 UTC | 27m |
| N2530M |  | Mojave Air & Space Port/Rutan Field (KMHV) | Kern Valley Airport (KL05) | 2026-08-15 19:37 UTC | 2026-08-15 19:54 UTC | 17m |
| OEXYO | OEX | Salzburg Airport (LOWS) | Linz Airport (LOWL) | 2026-08-15 19:15 UTC | 2026-08-15 19:54 UTC | 38m |
| N950RF |  | Provo Municipal Airport (KPVU) | Mineral Canyon Strip (UT75) | 2026-08-15 16:22 UTC | 2026-08-15 19:51 UTC | 3h 28m |
| N777ZA |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-08-15 16:39 UTC | 2026-08-15 19:45 UTC | 3h 6m |
| RYR5BQ | Ryanair | Palermo / Punta Raisi Airport (LICJ) | Malpensa International Airport (LIMC) | 2026-08-15 18:29 UTC | 2026-08-15 19:44 UTC | 1h 15m |
| N71560 |  | Abilene Municipal Airport (KK78) | Abilene Municipal Airport (KK78) | 2026-08-15 19:31 UTC | 2026-08-15 19:44 UTC | 13m |
| NDU661 | NDU | Mesa Gateway Airport (KIWA) | Tombstone Municipal Airport (KP29) | 2026-08-15 18:05 UTC | 2026-08-15 19:39 UTC | 1h 33m |
| N570FG |  | Trenton Mercer Airport (KTTN) | Hammonton Municipal Airport (KN81) | 2026-08-15 18:29 UTC | 2026-08-15 19:38 UTC | 1h 9m |
| IBS1903 | IBS | Madrid Barajas International Airport (LEMD) | HE12 (HE12) | 2026-08-15 15:37 UTC | 2026-08-15 19:37 UTC | 4h 0m |
| CTN385 | CTN | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Otocac Airport (LDRO) | 2026-08-15 16:25 UTC | 2026-08-15 19:36 UTC | 3h 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
