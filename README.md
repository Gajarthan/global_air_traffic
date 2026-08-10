# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_15:45:21_UTC-green)

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

**Latest saved flight:** 2026-08-10 15:45:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 15:45:21 UTC

- **184,312** saved flights
- **58,666** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **184,312** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,214,350.8 tonnes** estimated CO2 emissions
- **128,368,164 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7318 |
| 2 | SkyWest Airlines | 6689 |
| 3 | EJA | 3633 |
| 4 | IndiGo | 3232 |
| 5 | Southwest Airlines | 2886 |
| 6 | American Airlines | 2870 |
| 7 | ENY | 2295 |
| 8 | Delta Air Lines | 2174 |
| 9 | LATAM Airlines | 1726 |
| 10 | AZU | 1653 |
| 11 | Lufthansa | 1625 |
| 12 | WIF | 1526 |
| 13 | Vueling | 1522 |
| 14 | LXJ | 1452 |
| 15 | easyJet | 1265 |
| 16 | Swiss International | 1265 |
| 17 | AXM | 1235 |
| 18 | QLK | 1135 |
| 19 | EJU | 1134 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1015 |
| 23 | GLO | 985 |
| 24 | AEE | 958 |
| 25 | Air France | 956 |
| 26 | CXK | 956 |
| 27 | Cathay Pacific | 947 |
| 28 | PGT | 941 |
| 29 | United Airlines | 941 |
| 30 | MXY | 916 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 157376 |
| 2 | 🇪🇸 ES | 11847 |
| 3 | 🇧🇷 BR | 10584 |
| 4 | 🇦🇺 AU | 10306 |
| 5 | 🇮🇳 IN | 10124 |
| 6 | 🇨🇦 CA | 10030 |
| 7 | 🇮🇹 IT | 9525 |
| 8 | 🇩🇪 DE | 9123 |
| 9 | 🇬🇧 GB | 8559 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7372 |
| 12 | 🇨🇴 CO | 6904 |
| 13 | 🇬🇷 GR | 5409 |
| 14 | 🇲🇽 MX | 5259 |
| 15 | 🇨🇭 CH | 4935 |
| 16 | 🇹🇷 TR | 4817 |
| 17 | 🇳🇴 NO | 4746 |
| 18 | 🇲🇾 MY | 3219 |
| 19 | 🇿🇦 ZA | 3094 |
| 20 | 🇵🇱 PL | 3084 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2439 |
| 24 | 🇬🇹 GT | 2360 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1863 |
| 27 | 🇭🇷 HR | 1849 |
| 28 | 🇲🇪 ME | 1665 |
| 29 | 🇳🇱 NL | 1653 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3815 |
| 2 | Denver International Airport |  | US | 3037 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2268 |
| 5 | Guaymaral Airport |  | CO | 2246 |
| 6 | Harry Reid International Airport |  | US | 2156 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1977 |
| 8 | Zurich Airport |  | CH | 1975 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1911 |
| 10 | La Aurora Airport |  | GT | 1810 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1675 |
| 12 | El Dorado International Airport |  | CO | 1653 |
| 13 | Salt Lake City International Airport |  | US | 1640 |
| 14 | Chicago O'Hare International Airport |  | US | 1640 |
| 15 | Frankfurt am Main International Airport |  | DE | 1592 |
| 16 | Congonhas Airport |  | BR | 1533 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 19 | Madrid Barajas International Airport |  | ES | 1448 |
| 20 | Capua Airport |  | IT | 1445 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1320 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1273 |
| 25 | Charles de Gaulle International Airport |  | FR | 1257 |
| 26 | Charlotte/Douglas International Airport |  | US | 1247 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1151 |
| 30 | Ninoy Aquino International Airport |  | PH | 1150 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1093 |
| 33 | Viracopos International Airport |  | BR | 1060 |
| 34 | Seattle-Tacoma International Airport |  | US | 1057 |
| 35 | Reno/Tahoe International Airport |  | US | 1051 |
| 36 | Calgary International Airport |  | CA | 1049 |
| 37 | Daniel K Inouye International Airport |  | US | 1047 |
| 38 | Oslo Gardermoen Airport |  | NO | 1027 |
| 39 | Tenerife Norte Airport |  | ES | 1005 |
| 40 | Amsterdam Airport Schiphol |  | NL | 997 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 926 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 675 | 21m | 244 km | 2,842.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 428 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 310 | 27m | 275 km | 1,469.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 274 | 44m | 241 km | 1,138.1 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 269 | 22m | 55 km | 255.7 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 260 | 1h 49m | 1,423 km | 6,380.8 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 259 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 221 | 19m | 144 km | 549.7 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 218 | 1h 38m | 1,156 km | 4,349.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 217 | 24m | 218 km | 817.5 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FFAB123 | FFA | Felker Army Air Field (KFAF) | Norfolk Ns (Chambers Field) Airport (KNGU) | 2026-08-10 15:18 UTC | 2026-08-10 15:45 UTC | 26m |
| N550RS |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-08-10 15:22 UTC | 2026-08-10 15:44 UTC | 22m |
| N5128N |  | Sunrise Dusters Airport (CA18) | Sunrise Dusters Airport (CA18) | 2026-08-10 13:28 UTC | 2026-08-10 15:41 UTC | 2h 13m |
| EPI257 | EPI | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-10 13:41 UTC | 2026-08-10 15:38 UTC | 1h 56m |
| N624Y |  | Falcon Field (KFFZ) | Chapman Ranch Airstrip (58AZ) | 2026-08-10 15:21 UTC | 2026-08-10 15:36 UTC | 15m |
| ENSAIO73 | ENS | Santa Paula Airport (SISP) | Mirassol Airport (SDMH) | 2026-08-10 15:22 UTC | 2026-08-10 15:34 UTC | 12m |
| N464RB |  | Centennial Airport (KAPA) | High Plains Airport Airport (CD15) | 2026-08-10 15:16 UTC | 2026-08-10 15:32 UTC | 16m |
| N81LN |  | Garrett County Airport (K2G4) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-08-10 15:17 UTC | 2026-08-10 15:32 UTC | 15m |
| CAP546 | CAP | Centennial Airport (KAPA) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-10 15:01 UTC | 2026-08-10 15:30 UTC | 29m |
| N3641R |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-08-10 14:57 UTC | 2026-08-10 15:29 UTC | 32m |
| N744TX |  | Goode Field (TX43) | Tyler Pounds Regional Airport (KTYR) | 2026-08-10 15:10 UTC | 2026-08-10 15:28 UTC | 18m |
| NDU794 | NDU | Mesa Gateway Airport (KIWA) | Tombstone Municipal Airport (KP29) | 2026-08-10 14:20 UTC | 2026-08-10 15:27 UTC | 1h 7m |
| DELPL | DEL | Marl Loemuhle Airport (EDLM) | Dortmund Airport (EDLW) | 2026-08-10 14:43 UTC | 2026-08-10 15:27 UTC | 44m |
| FAC4004 | FAC | El Dorado International Airport (SKBO) | El Dorado International Airport (SKBO) | 2026-08-10 15:09 UTC | 2026-08-10 15:27 UTC | 18m |
| N744DA |  | Fairbanks International Airport (PAFA) | Edward G Pitka Sr Airport (PAGA) | 2026-08-10 14:17 UTC | 2026-08-10 15:23 UTC | 1h 5m |
| N870B |  | Toledo Suburban Airport (KDUH) | Lakes Of The North Airport (K4Y4) | 2026-08-10 14:37 UTC | 2026-08-10 15:20 UTC | 42m |
| N106UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-08-10 14:10 UTC | 2026-08-10 15:19 UTC | 1h 9m |
| N61GE |  | Telluride Regional Airport (KTEX) | Four Corners Regional Airport (KFMN) | 2026-08-10 14:46 UTC | 2026-08-10 15:18 UTC | 31m |
| SHADY09 | SHA | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-08-10 15:04 UTC | 2026-08-10 15:17 UTC | 13m |
| N263TH |  | Frankfurt am Main International Airport (EDDF) | Rzeszów Airport (EPRJ) | 2026-08-10 13:59 UTC | 2026-08-10 15:16 UTC | 1h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
