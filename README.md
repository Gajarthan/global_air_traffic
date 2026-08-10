# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_22:54:03_UTC-green)

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

**Latest saved flight:** 2026-08-10 22:54:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 22:54:03 UTC

- **185,465** saved flights
- **58,947** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **185,465** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,226,638.7 tonnes** estimated CO2 emissions
- **129,080,505 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7353 |
| 2 | SkyWest Airlines | 6767 |
| 3 | EJA | 3672 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2911 |
| 6 | American Airlines | 2894 |
| 7 | ENY | 2311 |
| 8 | Delta Air Lines | 2187 |
| 9 | LATAM Airlines | 1735 |
| 10 | AZU | 1667 |
| 11 | Lufthansa | 1627 |
| 12 | WIF | 1532 |
| 13 | Vueling | 1530 |
| 14 | LXJ | 1457 |
| 15 | easyJet | 1271 |
| 16 | Swiss International | 1268 |
| 17 | AXM | 1235 |
| 18 | EJU | 1146 |
| 19 | QLK | 1136 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1109 |
| 22 | VIV | 1022 |
| 23 | GLO | 995 |
| 24 | AEE | 963 |
| 25 | Air France | 961 |
| 26 | CXK | 960 |
| 27 | United Airlines | 948 |
| 28 | Cathay Pacific | 947 |
| 29 | PGT | 947 |
| 30 | MXY | 921 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 158635 |
| 2 | 🇪🇸 ES | 11907 |
| 3 | 🇧🇷 BR | 10654 |
| 4 | 🇦🇺 AU | 10314 |
| 5 | 🇮🇳 IN | 10141 |
| 6 | 🇨🇦 CA | 10134 |
| 7 | 🇮🇹 IT | 9579 |
| 8 | 🇩🇪 DE | 9151 |
| 9 | 🇬🇧 GB | 8603 |
| 10 | 🇯🇵 JP | 7513 |
| 11 | 🇫🇷 FR | 7404 |
| 12 | 🇨🇴 CO | 7006 |
| 13 | 🇬🇷 GR | 5438 |
| 14 | 🇲🇽 MX | 5293 |
| 15 | 🇨🇭 CH | 4948 |
| 16 | 🇹🇷 TR | 4863 |
| 17 | 🇳🇴 NO | 4762 |
| 18 | 🇲🇾 MY | 3221 |
| 19 | 🇿🇦 ZA | 3110 |
| 20 | 🇵🇱 PL | 3090 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2633 |
| 23 | 🇵🇭 PH | 2445 |
| 24 | 🇬🇹 GT | 2371 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1876 |
| 27 | 🇭🇷 HR | 1864 |
| 28 | 🇲🇪 ME | 1669 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3850 |
| 2 | Denver International Airport |  | US | 3067 |
| 3 | Tokyo International Airport |  | JP | 2330 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2272 |
| 6 | Harry Reid International Airport |  | US | 2170 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1984 |
| 8 | Zurich Airport |  | CH | 1979 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1930 |
| 10 | La Aurora Airport |  | GT | 1819 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1691 |
| 12 | El Dorado International Airport |  | CO | 1664 |
| 13 | Salt Lake City International Airport |  | US | 1656 |
| 14 | Chicago O'Hare International Airport |  | US | 1651 |
| 15 | Frankfurt am Main International Airport |  | DE | 1596 |
| 16 | Congonhas Airport |  | BR | 1550 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1458 |
| 19 | Capua Airport |  | IT | 1455 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1385 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1324 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1279 |
| 25 | Charles de Gaulle International Airport |  | FR | 1264 |
| 26 | Charlotte/Douglas International Airport |  | US | 1254 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1162 |
| 30 | Ninoy Aquino International Airport |  | PH | 1153 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1137 |
| 32 | Barcelona International Airport |  | ES | 1098 |
| 33 | Viracopos International Airport |  | BR | 1068 |
| 34 | Seattle-Tacoma International Airport |  | US | 1067 |
| 35 | Reno/Tahoe International Airport |  | US | 1065 |
| 36 | Calgary International Airport |  | CA | 1057 |
| 37 | Daniel K Inouye International Airport |  | US | 1052 |
| 38 | Oslo Gardermoen Airport |  | NO | 1032 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1005 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 936 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 680 | 21m | 244 km | 2,863.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 445 | 1h 8m | 770 km | 5,911.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 431 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 311 | 27m | 275 km | 1,473.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 277 | 44m | 241 km | 1,150.6 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 268 | 8m | - | - |
| 14 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 232 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 229 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 224 | 50m | 556 km | 2,147.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 219 | 24m | 218 km | 825.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 216 | 31m | 369 km | 1,374.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HYTEK44 | HYT | 3FL8 (3FL8) | North American Farms Airport (56FD) | 2026-08-10 22:24 UTC | 2026-08-10 22:54 UTC | 29m |
| EFY6925 | EFY | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-10 22:34 UTC | 2026-08-10 22:48 UTC | 13m |
| NIT265 | NIT | Heart Of Georgia Regional Airport (KEZM) | Heart Of Georgia Regional Airport (KEZM) | 2026-08-10 22:19 UTC | 2026-08-10 22:48 UTC | 29m |
| N8936P |  | Akron-Canton Regional Airport (KCAK) | OI66 (OI66) | 2026-08-10 21:56 UTC | 2026-08-10 22:48 UTC | 51m |
| AR1 |  | Miami-Opa Locka Executive Airport (KOPF) | Miami-Opa Locka Executive Airport (KOPF) | 2026-08-10 22:35 UTC | 2026-08-10 22:37 UTC | 1m |
| N70727 |  | John Wayne/Orange County Airport (KSNA) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-08-10 22:23 UTC | 2026-08-10 22:37 UTC | 14m |
| EYI | EYI | Sunshine Coast Airport (YBMC) | Sunshine Coast Airport (YBMC) | 2026-08-10 22:25 UTC | 2026-08-10 22:37 UTC | 12m |
| N551MA |  | Montgomery-Gibbs Executive Airport (KMYF) | Borrego Valley Airport (KL08) | 2026-08-10 22:20 UTC | 2026-08-10 22:36 UTC | 15m |
| N610SP |  | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-08-10 22:14 UTC | 2026-08-10 22:36 UTC | 21m |
| N690TW |  | Rocky Mountain Metro Airport (KBJC) | Granby-Grand County Airport (KGNB) | 2026-08-10 22:22 UTC | 2026-08-10 22:33 UTC | 10m |
| DAL2431 | Delta Air Lines | Detroit Metro Wayne County Airport (KDTW) | Orr Field (NE25) | 2026-08-10 20:28 UTC | 2026-08-10 22:31 UTC | 2h 2m |
| N992FG |  | Raleigh-Durham International Airport (KRDU) | Triangle North Executive Airport (KLHZ) | 2026-08-10 22:14 UTC | 2026-08-10 22:30 UTC | 16m |
| N71PM |  | Flying J Airport (86TX) | Camp Bullis Als (Cals) Airport (9TX5) | 2026-08-10 21:18 UTC | 2026-08-10 22:28 UTC | 1h 9m |
| N611AC |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-10 20:32 UTC | 2026-08-10 22:28 UTC | 1h 55m |
| N233S |  | Silver Springs Airport (KSPZ) | Silver Springs Airport (KSPZ) | 2026-08-10 20:53 UTC | 2026-08-10 22:27 UTC | 1h 33m |
| N270TM |  | Sweetwater (Usmc) Airport (NV72) | Silver Springs Airport (KSPZ) | 2026-08-10 21:39 UTC | 2026-08-10 22:22 UTC | 43m |
| N349BG |  | Wood County Regional Airport (K1G0) | 72OI (72OI) | 2026-08-10 21:56 UTC | 2026-08-10 22:21 UTC | 25m |
| UAL15 | United Airlines | London Heathrow Airport (EGLL) | Newark Liberty International Airport (KEWR) | 2026-08-10 14:46 UTC | 2026-08-10 22:20 UTC | 7h 33m |
| TCN717 | TCN | Reno/Tahoe International Airport (KRNO) | 1TE6 (1TE6) | 2026-08-10 20:26 UTC | 2026-08-10 22:19 UTC | 1h 52m |
| ARCAS35 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-08-10 21:59 UTC | 2026-08-10 22:19 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
