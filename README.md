# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_23:28:21_UTC-green)

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

**Latest saved flight:** 2026-04-07 23:28:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-07 23:28:21 UTC

- **22,424** saved flights
- **11,044** unique routes
- **118** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **22,424** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **277,582.2 tonnes** estimated CO2 emissions
- **16,091,720 km** total distance flown
- **851 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | SkyWest Airlines | 964 |
| 2 | Ryanair | 929 |
| 3 | IndiGo | 624 |
| 4 | EJA | 421 |
| 5 | American Airlines | 418 |
| 6 | Southwest Airlines | 327 |
| 7 | ENY | 301 |
| 8 | Lufthansa | 281 |
| 9 | Vueling | 233 |
| 10 | LATAM Airlines | 229 |
| 11 | AXM | 214 |
| 12 | Delta Air Lines | 197 |
| 13 | All Nippon Airways | 193 |
| 14 | LXJ | 189 |
| 15 | QLK | 187 |
| 16 | AZU | 178 |
| 17 | Swiss International | 162 |
| 18 | VIV | 159 |
| 19 | Alaska Airlines | 154 |
| 20 | easyJet | 149 |
| 21 | Japan Airlines | 148 |
| 22 | United Airlines | 146 |
| 23 | EJU | 143 |
| 24 | Avianca | 139 |
| 25 | AEE | 138 |
| 26 | EDV | 134 |
| 27 | WIF | 134 |
| 28 | AXB | 126 |
| 29 | Air France | 119 |
| 30 | JetBlue | 115 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 17802 |
| 2 | 🇮🇳 IN | 1903 |
| 3 | 🇪🇸 ES | 1739 |
| 4 | 🇦🇺 AU | 1582 |
| 5 | 🇧🇷 BR | 1274 |
| 6 | 🇯🇵 JP | 1216 |
| 7 | 🇨🇴 CO | 1179 |
| 8 | 🇮🇹 IT | 1128 |
| 9 | 🇩🇪 DE | 1109 |
| 10 | 🇨🇦 CA | 1008 |
| 11 | 🇬🇧 GB | 882 |
| 12 | 🇫🇷 FR | 816 |
| 13 | 🇲🇽 MX | 737 |
| 14 | 🇬🇷 GR | 630 |
| 15 | 🇨🇭 CH | 604 |
| 16 | 🇲🇾 MY | 501 |
| 17 | 🇿🇦 ZA | 492 |
| 18 | 🇳🇴 NO | 467 |
| 19 | 🇬🇹 GT | 467 |
| 20 | 🇳🇿 NZ | 455 |
| 21 | 🇹🇷 TR | 429 |
| 22 | 🇵🇭 PH | 421 |
| 23 | 🇰🇷 KR | 391 |
| 24 | 🇹🇭 TH | 349 |
| 25 | 🇵🇱 PL | 321 |
| 26 | 🇲🇦 MA | 269 |
| 27 | 🇧🇸 BS | 243 |
| 28 | 🇮🇩 ID | 231 |
| 29 | 🇲🇪 ME | 231 |
| 30 | 🇳🇱 NL | 221 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 549 |
| 2 | El Dorado International Airport |  | CO | 442 |
| 3 | Tokyo International Airport |  | JP | 411 |
| 4 | Denver International Airport |  | US | 404 |
| 5 | Indira Gandhi International Airport |  | IN | 383 |
| 6 | La Aurora Airport |  | GT | 322 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 302 |
| 8 | Harry Reid International Airport |  | US | 300 |
| 9 | Zurich Airport |  | CH | 269 |
| 10 | Frankfurt am Main International Airport |  | DE | 248 |
| 11 | Hartsfield/Jackson Atlanta International Airport |  | US | 240 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 237 |
| 13 | Chicago O'Hare International Airport |  | US | 237 |
| 14 | Guaymaral Airport |  | CO | 234 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 220 |
| 16 | Charlotte/Douglas International Airport |  | US | 214 |
| 17 | Bengaluru International Airport |  | IN | 214 |
| 18 | Macau International Airport |  | MO | 204 |
| 19 | Tenerife Norte Airport |  | ES | 202 |
| 20 | Madrid Barajas International Airport |  | ES | 200 |
| 21 | Ninoy Aquino International Airport |  | PH | 193 |
| 22 | Atizapan De Zaragoza Airport |  | MX | 192 |
| 23 | Congonhas Airport |  | BR | 184 |
| 24 | Salt Lake City International Airport |  | US | 180 |
| 25 | Kuala Lumpur International Airport |  | MY | 178 |
| 26 | Malpensa International Airport |  | IT | 174 |
| 27 | Reno/Tahoe International Airport |  | US | 174 |
| 28 | Daniel K Inouye International Airport |  | US | 173 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 170 |
| 30 | Charles de Gaulle International Airport |  | FR | 164 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 162 |
| 32 | Miami International Airport |  | US | 154 |
| 33 | O. R. Tambo International Airport |  | ZA | 153 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 151 |
| 35 | Pune Airport |  | IN | 151 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 150 |
| 37 | Vitoria/Foronda Airport |  | ES | 147 |
| 38 | Seattle-Tacoma International Airport |  | US | 146 |
| 39 | Barcelona International Airport |  | ES | 145 |
| 40 | George Bush Intcntl/Houston Airport |  | US | 140 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 104 | 1h 8m | 706 km | 1,266.2 t |
| 2 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 95 | 14m | 114 km | 186.3 t |
| 3 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 86 | 27m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 84 | 24m | 225 km | 325.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 77 | 28m | 304 km | 403.7 t |
| 6 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 68 | 22m | 99 km | 116.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 66 | 1h 28m | 910 km | 1,035.7 t |
| 8 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 66 | 27m | 152 km | 172.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 63 | 31m | - | - |
| 10 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 62 | 1h 42m | 1,156 km | 1,236.9 t |
| 11 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 57 | 16m | 206 km | 202.6 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 51 | 19m | 165 km | 145.1 t |
| 13 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 50 | 1h 13m | 770 km | 664.2 t |
| 14 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 48 | 27m | 275 km | 227.5 t |
| 15 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 47 | 23m | 252 km | 204.1 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 46 | 55m | 546 km | 433.1 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 45 | 31m | 369 km | 286.4 t |
| 18 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 45 | 52m | 556 km | 431.4 t |
| 19 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 45 | 1h 53m | 1,304 km | 1,012.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 42 | 20m | 250 km | 181.4 t |
| 21 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 42 | 9m | - | - |
| 22 | Bodø Airport (ENBO) | Bodø Airport (ENBO) | 41 | 4m | - | - |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 39 | 46m | 452 km | 303.9 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 39 | 13m | 99 km | 66.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 38 | 1h 43m | 1,423 km | 932.6 t |
| 26 | Bengaluru International Airport (VOBL) | Pune Airport (VAPO) | 38 | 1h 1m | 723 km | 473.7 t |
| 27 | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 36 | 30m | 114 km | 70.9 t |
| 28 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 34 | 12m | 15 km | 9.0 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Ulu Bernam Airport (WMBF) | 33 | 11m | 127 km | 72.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 33 | 1h 22m | 961 km | 547.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CXK1135 | CXK | Livermore Municipal Airport (KLVK) | Livermore Municipal Airport (KLVK) | 2026-04-07 22:33 UTC | 2026-04-07 23:28 UTC | 54m |
| N40FC |  | 1TS3 (1TS3) | Lakefront Airport (KNEW) | 2026-04-07 22:43 UTC | 2026-04-07 23:28 UTC | 44m |
| CCA737 | Air China | Beijing Capital International Airport (ZBAA) | Sharypovo Airport (UNKO) | 2026-04-07 20:01 UTC | 2026-04-07 23:26 UTC | 3h 25m |
| PAT594 | PAT | Falcon Field (KFFZ) | Lake Havasu City Airport (KHII) | 2026-04-07 22:25 UTC | 2026-04-07 23:26 UTC | 1h 1m |
| N5344G |  | Tacoma Narrows Airport (KTIW) | Boeing Field/King County International Airport (KBFI) | 2026-04-07 22:14 UTC | 2026-04-07 23:15 UTC | 1h 1m |
| N936EA |  | NY73 (NY73) | Laurence G Hanscom Field (KBED) | 2026-04-07 22:36 UTC | 2026-04-07 23:09 UTC | 33m |
| BYF21 | BYF | San Carlos Airport (KSQL) | San Carlos Airport (KSQL) | 2026-04-07 22:09 UTC | 2026-04-07 23:09 UTC | 1h 0m |
| KING70 | KIN | Francis S Gabreski Airport (KFOK) | Francis S Gabreski Airport (KFOK) | 2026-04-07 22:48 UTC | 2026-04-07 23:09 UTC | 20m |
| N789FA |  | Montgomery-Gibbs Executive Airport (KMYF) | Bob Maxwell Memorial Airfield (KOKB) | 2026-04-07 22:35 UTC | 2026-04-07 23:03 UTC | 28m |
| N5386J |  | Capital City Airport (KCXY) | Schuylkill County/Joe Zerbey Airport (KZER) | 2026-04-07 22:30 UTC | 2026-04-07 23:02 UTC | 31m |
| N512HW |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-04-07 22:05 UTC | 2026-04-07 23:00 UTC | 55m |
| RDHK723 | RDH | Norfolk Ns (Chambers Field) Airport (KNGU) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-04-07 22:23 UTC | 2026-04-07 22:58 UTC | 35m |
| WAH | WAH | Kenai Municipal Airport (PAEN) | Nikolai Creek Airport (9AK3) | 2026-04-07 22:27 UTC | 2026-04-07 22:57 UTC | 30m |
| CGCFS | CGC | Fort Langley Airport (CBQ2) | Pitt Meadows Airport (CYPK) | 2026-04-07 22:46 UTC | 2026-04-07 22:55 UTC | 8m |
| N12VP |  | Owen Field (4XA3) | Mid-Way Regional Airport (KJWY) | 2026-04-07 22:21 UTC | 2026-04-07 22:53 UTC | 31m |
| 00000000 |  | Cecil Ranch Airport (37CN) | Louis Armstrong New Orleans International Airport (KMSY) | 2026-04-07 19:22 UTC | 2026-04-07 22:50 UTC | 3h 28m |
| FFAB123 | FFA | North Island Nas (Halsey Field) Airport (KNZY) | Imperial Beach Nolf (Ream Field) Airport (KNRS) | 2026-04-07 22:27 UTC | 2026-04-07 22:50 UTC | 23m |
| UTY6520 | UTY | Perth International Airport (YPPH) | Leonora Airport (YLEO) | 2026-04-07 22:02 UTC | 2026-04-07 22:50 UTC | 47m |
| DAL928 | Delta Air Lines | Seattle-Tacoma International Airport (KSEA) | Ted Stevens Anchorage International Airport (PANC) | 2026-04-07 19:21 UTC | 2026-04-07 22:47 UTC | 3h 25m |
| UGLY73 | UGL | Short Creek Airport (8TN7) | Campbell Army Air Field (Fort Campbell) Airport (KHOP) | 2026-04-07 22:07 UTC | 2026-04-07 22:44 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
