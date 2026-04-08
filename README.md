# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_08:33:58_UTC-green)

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

**Latest saved flight:** 2026-04-08 08:33:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-08 08:33:58 UTC

- **22,902** saved flights
- **11,196** unique routes
- **119** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,902** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **283,778.6 tonnes** estimated CO2 emissions
- **16,450,934 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 971 |
| 2 | Ryanair | 944 |
| 3 | IndiGo | 643 |
| 4 | EJA | 422 |
| 5 | American Airlines | 420 |
| 6 | Southwest Airlines | 330 |
| 7 | ENY | 302 |
| 8 | Lufthansa | 288 |
| 9 | Vueling | 238 |
| 10 | AXM | 232 |
| 11 | LATAM Airlines | 230 |
| 12 | QLK | 211 |
| 13 | All Nippon Airways | 209 |
| 14 | Delta Air Lines | 199 |
| 15 | LXJ | 189 |
| 16 | AZU | 181 |
| 17 | Swiss International | 165 |
| 18 | VIV | 162 |
| 19 | Japan Airlines | 159 |
| 20 | Alaska Airlines | 158 |
| 21 | easyJet | 151 |
| 22 | EJU | 148 |
| 23 | United Airlines | 147 |
| 24 | AEE | 143 |
| 25 | WIF | 140 |
| 26 | Avianca | 139 |
| 27 | EDV | 135 |
| 28 | AXB | 129 |
| 29 | Air France | 120 |
| 30 | ANZ | 118 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 18012 |
| 2 | 🇮🇳 IN | 1947 |
| 3 | 🇪🇸 ES | 1758 |
| 4 | 🇦🇺 AU | 1717 |
| 5 | 🇯🇵 JP | 1301 |
| 6 | 🇧🇷 BR | 1285 |
| 7 | 🇨🇴 CO | 1181 |
| 8 | 🇮🇹 IT | 1157 |
| 9 | 🇩🇪 DE | 1138 |
| 10 | 🇨🇦 CA | 1029 |
| 11 | 🇬🇧 GB | 894 |
| 12 | 🇫🇷 FR | 834 |
| 13 | 🇲🇽 MX | 747 |
| 14 | 🇬🇷 GR | 654 |
| 15 | 🇨🇭 CH | 616 |
| 16 | 🇲🇾 MY | 544 |
| 17 | 🇳🇿 NZ | 492 |
| 18 | 🇿🇦 ZA | 492 |
| 19 | 🇳🇴 NO | 481 |
| 20 | 🇬🇹 GT | 467 |
| 21 | 🇹🇷 TR | 437 |
| 22 | 🇵🇭 PH | 436 |
| 23 | 🇰🇷 KR | 412 |
| 24 | 🇹🇭 TH | 362 |
| 25 | 🇵🇱 PL | 327 |
| 26 | 🇲🇦 MA | 274 |
| 27 | 🇧🇸 BS | 243 |
| 28 | 🇮🇩 ID | 242 |
| 29 | 🇲🇪 ME | 232 |
| 30 | 🇳🇱 NL | 226 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 550 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 435 |
| 4 | Denver International Airport |  | US | 407 |
| 5 | Indira Gandhi International Airport |  | IN | 393 |
| 6 | La Aurora Airport |  | GT | 322 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 315 |
| 8 | Harry Reid International Airport |  | US | 308 |
| 9 | Zurich Airport |  | CH | 274 |
| 10 | Frankfurt am Main International Airport |  | DE | 252 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 241 |
| 12 | Hartsfield/Jackson Atlanta International Airport |  | US | 241 |
| 13 | Sydney Kingsford Smith International Airport |  | AU | 240 |
| 14 | Chicago O'Hare International Airport |  | US | 238 |
| 15 | Guaymaral Airport |  | CO | 236 |
| 16 | Bengaluru International Airport |  | IN | 221 |
| 17 | Macau International Airport |  | MO | 218 |
| 18 | Charlotte/Douglas International Airport |  | US | 214 |
| 19 | Madrid Barajas International Airport |  | ES | 204 |
| 20 | Tenerife Norte Airport |  | ES | 202 |
| 21 | Ninoy Aquino International Airport |  | PH | 200 |
| 22 | Kuala Lumpur International Airport |  | MY | 197 |
| 23 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 24 | Congonhas Airport |  | BR | 186 |
| 25 | Malpensa International Airport |  | IT | 182 |
| 26 | Salt Lake City International Airport |  | US | 182 |
| 27 | Daniel K Inouye International Airport |  | US | 177 |
| 28 | Reno/Tahoe International Airport |  | US | 175 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 167 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 156 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | General Edward Lawrence Logan International Airport |  | US | 152 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 152 |
| 36 | Pune Airport |  | IN | 152 |
| 37 | Seattle-Tacoma International Airport |  | US | 149 |
| 38 | Vitoria/Foronda Airport |  | ES | 149 |
| 39 | Barcelona International Airport |  | ES | 147 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 109 | 1h 8m | 706 km | 1,327.1 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 87 | 24m | 225 km | 337.5 t |
| 4 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 87 | 27m | - | - |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 82 | 28m | 304 km | 429.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 69 | 1h 28m | 910 km | 1,082.8 t |
| 7 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 54 | 19m | 165 km | 153.6 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 51 | 55m | 546 km | 480.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 15 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 49 | 27m | 275 km | 232.2 t |
| 16 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 45 | 31m | 369 km | 286.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 43 | 4m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 22 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 41 | 46m | 452 km | 319.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 39 | 1h 43m | 1,423 km | 957.1 t |
| 25 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 33 | 20m | 147 km | 83.5 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AFR188 | Air France | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-07 21:43 UTC | 2026-04-08 08:33 UTC | 10h 50m |
| ROT301V | ROT | Henri Coanda International Airport (LROP) | Mainbullau Airport (EDFU) | 2026-04-08 06:07 UTC | 2026-04-08 08:27 UTC | 2h 20m |
| QTR818 | Qatar Airways | Hamad International Airport (OTHH) | Macau International Airport (VMMC) | 2026-04-08 01:39 UTC | 2026-04-08 08:26 UTC | 6h 46m |
| N131HN |  | Valley Point Airport (WV29) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-04-08 08:14 UTC | 2026-04-08 08:24 UTC | 10m |
| 2611 |  | Chiang Mai International Airport (VTCC) | Mae Hong Son Airport (VTCI) | 2026-04-08 08:08 UTC | 2026-04-08 08:21 UTC | 12m |
| DRAGO64 | DRA | Tarbes-Lourdes-Pyrenees Airport (LFBT) | Tarbes-Lourdes-Pyrenees Airport (LFBT) | 2026-04-08 08:11 UTC | 2026-04-08 08:17 UTC | 5m |
| ZKIDH | ZKI | Dunedin Airport (NZDN) | Taieri Airport (NZTI) | 2026-04-08 08:06 UTC | 2026-04-08 08:17 UTC | 11m |
| SEH2TC | SEH | Larnaca International Airport (LCLK) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-08 06:46 UTC | 2026-04-08 08:12 UTC | 1h 26m |
| R21235 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-08 07:12 UTC | 2026-04-08 08:06 UTC | 54m |
| HBXKF | HBX | Muenster Aero Airport (LSPU) | Kagiswil Airport (LSPG) | 2026-04-08 06:17 UTC | 2026-04-08 08:06 UTC | 1h 48m |
| AAL929 | American Airlines | Miami International Airport (KMIA) | Fazenda Santo Andre Airport (SNRA) | 2026-04-08 01:11 UTC | 2026-04-08 08:05 UTC | 6h 54m |
| YJY | YJY | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-04-08 08:03 UTC | 2026-04-08 08:04 UTC | 0m |
| FHMLR | FHM | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-08 07:43 UTC | 2026-04-08 08:03 UTC | 19m |
| CMA572 | CMA | Charles de Gaulle International Airport (LFPG) | Macau International Airport (VMMC) | 2026-04-07 20:41 UTC | 2026-04-08 08:00 UTC | 11h 19m |
| THY6238 | Turkish Airlines | Tbilisi International Airport (UGTB) | Macau International Airport (VMMC) | 2026-04-07 23:51 UTC | 2026-04-08 07:52 UTC | 8h 0m |
| R21230 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-04-08 07:00 UTC | 2026-04-08 07:50 UTC | 49m |
| CCA162 | Air China | Kansai International Airport (RJBB) | Macau International Airport (VMMC) | 2026-04-08 00:25 UTC | 2026-04-08 07:47 UTC | 7h 21m |
| IGO364F | IndiGo | Bengaluru International Airport (VOBL) | Baglung Airport (VNBL) | 2026-04-08 03:53 UTC | 2026-04-08 07:34 UTC | 3h 41m |
| ICE30R | ICE | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 2026-04-08 07:15 UTC | 2026-04-08 07:33 UTC | 18m |
| PE315 |  | Newcastle Airport (YWLM) | Collector Airport (YCLT) | 2026-04-08 06:41 UTC | 2026-04-08 07:32 UTC | 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
