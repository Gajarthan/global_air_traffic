# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_08:57:31_UTC-green)

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

**Latest saved flight:** 2026-04-10 08:57:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-10 08:57:31 UTC

- **26,485** saved flights
- **12,589** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **26,485** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **325,821.4 tonnes** estimated CO2 emissions
- **18,888,195 km** total distance flown
- **849 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1082 |
| 2 | SkyWest Airlines | 1082 |
| 3 | IndiGo | 713 |
| 4 | EJA | 473 |
| 5 | American Airlines | 471 |
| 6 | Southwest Airlines | 380 |
| 7 | ENY | 350 |
| 8 | Lufthansa | 338 |
| 9 | AXM | 271 |
| 10 | Vueling | 269 |
| 11 | LATAM Airlines | 259 |
| 12 | QLK | 243 |
| 13 | All Nippon Airways | 237 |
| 14 | Delta Air Lines | 220 |
| 15 | LXJ | 212 |
| 16 | AZU | 211 |
| 17 | Swiss International | 184 |
| 18 | Alaska Airlines | 180 |
| 19 | Japan Airlines | 177 |
| 20 | VIV | 176 |
| 21 | easyJet | 173 |
| 22 | EJU | 170 |
| 23 | WIF | 170 |
| 24 | AEE | 167 |
| 25 | United Airlines | 159 |
| 26 | EDV | 155 |
| 27 | Avianca | 150 |
| 28 | AXB | 146 |
| 29 | JetBlue | 140 |
| 30 | ANZ | 137 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 20829 |
| 2 | 🇮🇳 IN | 2190 |
| 3 | 🇦🇺 AU | 1976 |
| 4 | 🇪🇸 ES | 1958 |
| 5 | 🇧🇷 BR | 1484 |
| 6 | 🇯🇵 JP | 1474 |
| 7 | 🇩🇪 DE | 1352 |
| 8 | 🇮🇹 IT | 1344 |
| 9 | 🇨🇴 CO | 1322 |
| 10 | 🇨🇦 CA | 1266 |
| 11 | 🇬🇧 GB | 1062 |
| 12 | 🇫🇷 FR | 987 |
| 13 | 🇲🇽 MX | 851 |
| 14 | 🇬🇷 GR | 751 |
| 15 | 🇨🇭 CH | 723 |
| 16 | 🇲🇾 MY | 652 |
| 17 | 🇳🇿 NZ | 602 |
| 18 | 🇳🇴 NO | 573 |
| 19 | 🇿🇦 ZA | 536 |
| 20 | 🇵🇭 PH | 508 |
| 21 | 🇹🇷 TR | 495 |
| 22 | 🇬🇹 GT | 490 |
| 23 | 🇰🇷 KR | 470 |
| 24 | 🇹🇭 TH | 462 |
| 25 | 🇵🇱 PL | 386 |
| 26 | 🇲🇦 MA | 324 |
| 27 | 🇧🇸 BS | 272 |
| 28 | 🇲🇪 ME | 265 |
| 29 | 🇮🇩 ID | 262 |
| 30 | 🇳🇱 NL | 260 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 623 |
| 2 | Tokyo International Airport |  | JP | 495 |
| 3 | El Dorado International Airport |  | CO | 492 |
| 4 | Indira Gandhi International Airport |  | IN | 449 |
| 5 | Denver International Airport |  | US | 448 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 366 |
| 7 | Harry Reid International Airport |  | US | 345 |
| 8 | La Aurora Airport |  | GT | 340 |
| 9 | Zurich Airport |  | CH | 309 |
| 10 | Frankfurt am Main International Airport |  | DE | 286 |
| 11 | Guaymaral Airport |  | CO | 276 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 275 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 274 |
| 14 | Chicago O'Hare International Airport |  | US | 272 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 269 |
| 16 | Macau International Airport |  | MO | 259 |
| 17 | Bengaluru International Airport |  | IN | 244 |
| 18 | Charlotte/Douglas International Airport |  | US | 242 |
| 19 | Kuala Lumpur International Airport |  | MY | 241 |
| 20 | Ninoy Aquino International Airport |  | PH | 236 |
| 21 | Tenerife Norte Airport |  | ES | 228 |
| 22 | Madrid Barajas International Airport |  | ES | 222 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 209 |
| 24 | Malpensa International Airport |  | IT | 208 |
| 25 | Salt Lake City International Airport |  | US | 206 |
| 26 | Congonhas Airport |  | BR | 205 |
| 27 | Daniel K Inouye International Airport |  | US | 201 |
| 28 | Reno/Tahoe International Airport |  | US | 194 |
| 29 | Charles de Gaulle International Airport |  | FR | 189 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 184 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 183 |
| 32 | Miami International Airport |  | US | 177 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 176 |
| 34 | Barcelona International Airport |  | ES | 171 |
| 35 | O. R. Tambo International Airport |  | ZA | 170 |
| 36 | Seattle-Tacoma International Airport |  | US | 169 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 168 |
| 38 | Vitoria/Foronda Airport |  | ES | 165 |
| 39 | Capua Airport |  | IT | 164 |
| 40 | Pune Airport |  | IN | 160 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 127 | 1h 8m | 706 km | 1,546.2 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 108 | 14m | 114 km | 211.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 104 | 24m | 225 km | 403.5 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 103 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 93 | 28m | 304 km | 487.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 77 | 1h 27m | 910 km | 1,208.3 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 71 | 21m | 99 km | 121.6 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 68 | 27m | 152 km | 177.7 t |
| 9 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 67 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 65 | 19m | 165 km | 184.9 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 60 | 1h 12m | 770 km | 797.1 t |
| 13 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 14 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 57 | 55m | 546 km | 536.7 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 53 | 27m | 275 km | 251.1 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 53 | 31m | 369 km | 337.4 t |
| 17 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 47 | 45m | 452 km | 366.3 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 47 | 52m | 556 km | 450.5 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 47 | 20m | 250 km | 203.0 t |
| 21 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 45 | 4m | - | - |
| 22 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 23 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 45 | 9m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 44 | 1h 42m | 1,423 km | 1,079.8 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 43 | 13m | 99 km | 73.7 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 39 | 1h 1m | 723 km | 486.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 38 | 21m | 147 km | 96.2 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 38 | 12m | 15 km | 10.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 36 | 1h 21m | 961 km | 596.7 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 36 | 15m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GBHWA | GBH | RAF Church Fenton (EGXG) | RAF Church Fenton (EGXG) | 2026-04-10 08:43 UTC | 2026-04-10 08:57 UTC | 14m |
| N860MB |  | Phoenix Sky Harbor International Airport (KPHX) | Mesa Gateway Airport (KIWA) | 2026-04-10 08:31 UTC | 2026-04-10 08:46 UTC | 15m |
| FNA590 | FNA | Reykjavik Airport (BIRK) | Forsaeti Airport (BIFZ) | 2026-04-10 08:26 UTC | 2026-04-10 08:39 UTC | 13m |
| YULSA | YUL | Sofia Airport (LBSF) | Tautii Magheraus Airport (LRBM) | 2026-04-10 07:45 UTC | 2026-04-10 08:38 UTC | 52m |
| BFF20 | BFF | London / Chapeskie Field (CLC2) | Toronto Pearson International Airport (CYYZ) | 2026-04-10 08:21 UTC | 2026-04-10 08:36 UTC | 15m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-04-10 07:42 UTC | 2026-04-10 08:32 UTC | 49m |
| AIQ182 | AIQ | Don Mueang International Airport (VTBD) | Simara Airport (VNSI) | 2026-04-10 05:22 UTC | 2026-04-10 08:21 UTC | 2h 59m |
| SCPTR1 | SCP | RAF Cranwell (EGYD) | Humberside Airport (EGNJ) | 2026-04-10 07:25 UTC | 2026-04-10 08:18 UTC | 52m |
| CHX76 | CHX | Munster Osnabruck Airport (EDDG) | Bonn-Hangelar Airport (EDKB) | 2026-04-10 07:32 UTC | 2026-04-10 08:16 UTC | 44m |
| BGA113G | BGA | Toulouse-Blagnac Airport (LFBO) | Hamburg-Finkenwerder Airport (EDHI) | 2026-04-10 06:00 UTC | 2026-04-10 08:16 UTC | 2h 16m |
| SXN17 | SXN | London City Airport (EGLC) | Guernsey Airport (EGJB) | 2026-04-10 07:03 UTC | 2026-04-10 08:09 UTC | 1h 5m |
|  |  | Moss Airport Rygge (ENRY) | Jarlsberg Airfield (ENJB) | 2026-04-10 07:56 UTC | 2026-04-10 08:08 UTC | 12m |
| EAP53Y | EAP | Valence-Chabeuil Airport (LFLU) | Lyon-Bron Airport (LFLY) | 2026-04-10 07:37 UTC | 2026-04-10 08:06 UTC | 29m |
| CAL1806 | CAL | Taiwan Taoyuan International Airport (RCTP) | Kaohsiung International Airport (RCKH) | 2026-04-10 06:18 UTC | 2026-04-10 08:04 UTC | 1h 45m |
| GPMMC | GPM | Skegness (Ingoldmells) Aerodrome (EGNI) | Norwich International Airport (EGSH) | 2026-04-10 07:41 UTC | 2026-04-10 08:04 UTC | 22m |
| RYR2428 | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Visoko Sport Airfield (LQVI) | 2026-04-10 07:06 UTC | 2026-04-10 08:02 UTC | 56m |
| KLM89Q | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Linate Airport (LIML) | 2026-04-10 06:48 UTC | 2026-04-10 08:01 UTC | 1h 12m |
| VOZ557 | Virgin Australia | Sydney Kingsford Smith International Airport (YSSY) | Perth International Airport (YPPH) | 2026-04-10 03:14 UTC | 2026-04-10 08:00 UTC | 4h 45m |
| VLJ270X | VLJ | Valence-Chabeuil Airport (LFLU) | Raron Airport (LSTA) | 2026-04-10 07:24 UTC | 2026-04-10 07:59 UTC | 35m |
| VLG7KA | Vueling | Sevilla Airport (LEZL) | Vitoria/Foronda Airport (LEVT) | 2026-04-10 07:04 UTC | 2026-04-10 07:58 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
