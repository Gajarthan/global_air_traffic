# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_17:53:11_UTC-green)

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

**Latest saved flight:** 2026-08-03 17:53:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-03 17:53:11 UTC

- **168,949** saved flights
- **55,160** unique routes
- **140** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **168,949** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,036,467.8 tonnes** estimated CO2 emissions
- **118,056,106 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6746 |
| 2 | SkyWest Airlines | 6160 |
| 3 | EJA | 3357 |
| 4 | IndiGo | 2979 |
| 5 | American Airlines | 2662 |
| 6 | Southwest Airlines | 2660 |
| 7 | ENY | 2105 |
| 8 | Delta Air Lines | 2011 |
| 9 | LATAM Airlines | 1567 |
| 10 | Lufthansa | 1556 |
| 11 | AZU | 1484 |
| 12 | WIF | 1415 |
| 13 | Vueling | 1392 |
| 14 | LXJ | 1324 |
| 15 | AXM | 1166 |
| 16 | Swiss International | 1157 |
| 17 | easyJet | 1138 |
| 18 | EJU | 1036 |
| 19 | Alaska Airlines | 1032 |
| 20 | QLK | 1028 |
| 21 | All Nippon Airways | 1023 |
| 22 | VIV | 930 |
| 23 | Cathay Pacific | 902 |
| 24 | CXK | 895 |
| 25 | United Airlines | 889 |
| 26 | GLO | 886 |
| 27 | AEE | 884 |
| 28 | Air France | 871 |
| 29 | MXY | 865 |
| 30 | JetBlue | 851 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 145584 |
| 2 | 🇪🇸 ES | 10834 |
| 3 | 🇧🇷 BR | 9606 |
| 4 | 🇦🇺 AU | 9409 |
| 5 | 🇮🇳 IN | 9328 |
| 6 | 🇨🇦 CA | 9153 |
| 7 | 🇮🇹 IT | 8728 |
| 8 | 🇩🇪 DE | 8435 |
| 9 | 🇬🇧 GB | 7863 |
| 10 | 🇯🇵 JP | 6788 |
| 11 | 🇫🇷 FR | 6705 |
| 12 | 🇨🇴 CO | 6107 |
| 13 | 🇬🇷 GR | 4913 |
| 14 | 🇲🇽 MX | 4829 |
| 15 | 🇨🇭 CH | 4457 |
| 16 | 🇳🇴 NO | 4419 |
| 17 | 🇹🇷 TR | 4101 |
| 18 | 🇲🇾 MY | 3035 |
| 19 | 🇵🇱 PL | 2853 |
| 20 | 🇿🇦 ZA | 2743 |
| 21 | 🇹🇭 TH | 2458 |
| 22 | 🇳🇿 NZ | 2448 |
| 23 | 🇵🇭 PH | 2235 |
| 24 | 🇬🇹 GT | 2187 |
| 25 | 🇰🇷 KR | 2151 |
| 26 | 🇲🇦 MA | 1708 |
| 27 | 🇭🇷 HR | 1629 |
| 28 | 🇲🇪 ME | 1565 |
| 29 | 🇳🇱 NL | 1540 |
| 30 | 🇲🇴 MO | 1435 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3470 |
| 2 | Denver International Airport |  | US | 2801 |
| 3 | Tokyo International Airport |  | JP | 2132 |
| 4 | Guaymaral Airport |  | CO | 2104 |
| 5 | Indira Gandhi International Airport |  | IN | 2067 |
| 6 | Harry Reid International Airport |  | US | 2031 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1851 |
| 8 | Zurich Airport |  | CH | 1796 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1777 |
| 10 | La Aurora Airport |  | GT | 1687 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1555 |
| 12 | El Dorado International Airport |  | CO | 1531 |
| 13 | Chicago O'Hare International Airport |  | US | 1529 |
| 14 | Frankfurt am Main International Airport |  | DE | 1516 |
| 15 | Salt Lake City International Airport |  | US | 1510 |
| 16 | Macau International Airport |  | MO | 1435 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1396 |
| 18 | Congonhas Airport |  | BR | 1384 |
| 19 | Madrid Barajas International Airport |  | ES | 1332 |
| 20 | Capua Airport |  | IT | 1316 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1280 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1194 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1184 |
| 24 | Charlotte/Douglas International Airport |  | US | 1178 |
| 25 | Charles de Gaulle International Airport |  | FR | 1150 |
| 26 | Kuala Lumpur International Airport |  | MY | 1144 |
| 27 | Malpensa International Airport |  | IT | 1139 |
| 28 | Bengaluru International Airport |  | IN | 1108 |
| 29 | Ninoy Aquino International Airport |  | PH | 1051 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1046 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1037 |
| 32 | Barcelona International Airport |  | ES | 1002 |
| 33 | Daniel K Inouye International Airport |  | US | 982 |
| 34 | Seattle-Tacoma International Airport |  | US | 979 |
| 35 | Viracopos International Airport |  | BR | 962 |
| 36 | Calgary International Airport |  | CA | 954 |
| 37 | Tenerife Norte Airport |  | ES | 940 |
| 38 | Oslo Gardermoen Airport |  | NO | 939 |
| 39 | Reno/Tahoe International Airport |  | US | 938 |
| 40 | Scottsdale Airport |  | US | 934 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 874 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 615 | 21m | 244 km | 2,589.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 403 | 24m | 225 km | 1,563.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 402 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 382 | 1h 9m | 770 km | 5,074.6 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 317 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 289 | 27m | 275 km | 1,369.4 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 249 | 44m | 241 km | 1,034.3 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 246 | 19m | 165 km | 699.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 233 | 1h 47m | 1,423 km | 5,718.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 223 | 20m | 250 km | 963.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 219 | 26m | 215 km | 811.1 t |
| 18 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 212 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 201 | 19m | 144 km | 500.0 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 199 | 1h 15m | 961 km | 3,298.5 t |
| 23 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 197 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 196 | 50m | 556 km | 1,878.8 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 189 | 1h 38m | 1,156 km | 3,770.5 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 187 | 24m | 218 km | 704.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 185 | 1h 1m | 695 km | 2,217.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 182 | 44m | 452 km | 1,418.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3048E |  | Long Beach (Daugherty Field) Airport (KLGB) | Brown Field Municipal Airport (KSDM) | 2026-08-03 16:45 UTC | 2026-08-03 17:53 UTC | 1h 7m |
| N798ND |  | Punta Gorda Airport (KPGD) | Arcadia Municipal Airport (KX06) | 2026-08-03 17:11 UTC | 2026-08-03 17:51 UTC | 40m |
| TVF20HQ | TVF | Mikonos Airport (LGMK) | Paris-Orly Airport (LFPO) | 2026-08-03 14:46 UTC | 2026-08-03 17:49 UTC | 3h 2m |
| N334WB |  | Pegasus Airpark (5AZ3) | Phoenix Goodyear Airport (KGYR) | 2026-08-03 16:40 UTC | 2026-08-03 17:47 UTC | 1h 7m |
| MILAN80 | MIL | Cannes-Mandelieu Airport (LFMD) | Valence-Chabeuil Airport (LFLU) | 2026-08-03 15:56 UTC | 2026-08-03 17:47 UTC | 1h 51m |
| BOX544 | BOX | Moron Airport (ZMMN) | Macau International Airport (VMMC) | 2026-08-03 04:22 UTC | 2026-08-03 17:47 UTC | 13h 25m |
| TKR02 | TKR | Hill Afb Airport (KHIF) | K43U (K43U) | 2026-08-03 17:30 UTC | 2026-08-03 17:47 UTC | 16m |
| PAIN71 | PAI | 2TX3 (2TX3) | Anacacho Ranch Airport (0XS7) | 2026-08-03 17:30 UTC | 2026-08-03 17:45 UTC | 14m |
| RA02748 |  | Milas Bodrum International Airport (LTFE) | Sheremetyevo International Airport (UUEE) | 2026-08-03 13:07 UTC | 2026-08-03 17:43 UTC | 4h 36m |
| N238PT |  | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-08-03 17:17 UTC | 2026-08-03 17:39 UTC | 22m |
| N307SH |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-08-03 17:22 UTC | 2026-08-03 17:37 UTC | 15m |
| N4183N |  | Miami-Opa Locka Executive Airport (KOPF) | Miami-Opa Locka Executive Airport (KOPF) | 2026-08-03 16:40 UTC | 2026-08-03 17:31 UTC | 51m |
| N20BQ |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-08-03 16:46 UTC | 2026-08-03 17:31 UTC | 45m |
| N3744Y |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-03 17:08 UTC | 2026-08-03 17:25 UTC | 17m |
| N283MK |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-03 16:34 UTC | 2026-08-03 17:23 UTC | 48m |
| KING41 | KIN | Macdill Afb Aux Field (KAGR) | Patrick Space Force Base Airport (KCOF) | 2026-08-03 17:04 UTC | 2026-08-03 17:22 UTC | 17m |
| N220BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-03 17:21 UTC | 2026-08-03 17:22 UTC | 0m |
| CFOCI | CFO | MA72 (MA72) | Laurence G Hanscom Field (KBED) | 2026-08-03 16:50 UTC | 2026-08-03 17:20 UTC | 30m |
| N500WD |  | KI12 (KI12) | Antrim County Airport (KACB) | 2026-08-03 16:28 UTC | 2026-08-03 17:19 UTC | 51m |
| BNOB | BNO | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-03 17:05 UTC | 2026-08-03 17:19 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
