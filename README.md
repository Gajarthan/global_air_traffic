# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_11:22:17_UTC-green)

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

**Latest saved flight:** 2026-08-10 11:22:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 11:22:17 UTC

- **183,735** saved flights
- **58,542** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **183,735** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,208,777.2 tonnes** estimated CO2 emissions
- **128,045,056 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7290 |
| 2 | SkyWest Airlines | 6684 |
| 3 | EJA | 3629 |
| 4 | IndiGo | 3219 |
| 5 | Southwest Airlines | 2882 |
| 6 | American Airlines | 2868 |
| 7 | ENY | 2290 |
| 8 | Delta Air Lines | 2172 |
| 9 | LATAM Airlines | 1716 |
| 10 | AZU | 1646 |
| 11 | Lufthansa | 1622 |
| 12 | WIF | 1521 |
| 13 | Vueling | 1516 |
| 14 | LXJ | 1451 |
| 15 | Swiss International | 1261 |
| 16 | easyJet | 1259 |
| 17 | AXM | 1232 |
| 18 | QLK | 1135 |
| 19 | EJU | 1129 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1104 |
| 22 | VIV | 1012 |
| 23 | GLO | 985 |
| 24 | AEE | 957 |
| 25 | Air France | 953 |
| 26 | CXK | 953 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 940 |
| 29 | PGT | 934 |
| 30 | MXY | 915 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156993 |
| 2 | 🇪🇸 ES | 11802 |
| 3 | 🇧🇷 BR | 10537 |
| 4 | 🇦🇺 AU | 10300 |
| 5 | 🇮🇳 IN | 10085 |
| 6 | 🇨🇦 CA | 9995 |
| 7 | 🇮🇹 IT | 9504 |
| 8 | 🇩🇪 DE | 9094 |
| 9 | 🇬🇧 GB | 8523 |
| 10 | 🇯🇵 JP | 7501 |
| 11 | 🇫🇷 FR | 7325 |
| 12 | 🇨🇴 CO | 6865 |
| 13 | 🇬🇷 GR | 5386 |
| 14 | 🇲🇽 MX | 5248 |
| 15 | 🇨🇭 CH | 4906 |
| 16 | 🇹🇷 TR | 4788 |
| 17 | 🇳🇴 NO | 4728 |
| 18 | 🇲🇾 MY | 3210 |
| 19 | 🇵🇱 PL | 3075 |
| 20 | 🇿🇦 ZA | 3069 |
| 21 | 🇹🇭 TH | 2845 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2435 |
| 24 | 🇬🇹 GT | 2351 |
| 25 | 🇰🇷 KR | 2284 |
| 26 | 🇲🇦 MA | 1856 |
| 27 | 🇭🇷 HR | 1839 |
| 28 | 🇲🇪 ME | 1661 |
| 29 | 🇳🇱 NL | 1648 |
| 30 | 🇲🇴 MO | 1520 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3808 |
| 2 | Denver International Airport |  | US | 3036 |
| 3 | Tokyo International Airport |  | JP | 2326 |
| 4 | Indira Gandhi International Airport |  | IN | 2259 |
| 5 | Guaymaral Airport |  | CO | 2236 |
| 6 | Harry Reid International Airport |  | US | 2150 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1969 |
| 8 | Zurich Airport |  | CH | 1965 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1908 |
| 10 | La Aurora Airport |  | GT | 1804 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1673 |
| 12 | El Dorado International Airport |  | CO | 1646 |
| 13 | Salt Lake City International Airport |  | US | 1639 |
| 14 | Chicago O'Hare International Airport |  | US | 1637 |
| 15 | Frankfurt am Main International Airport |  | DE | 1587 |
| 16 | Congonhas Airport |  | BR | 1529 |
| 17 | Macau International Airport |  | MO | 1520 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1450 |
| 19 | Madrid Barajas International Airport |  | ES | 1442 |
| 20 | Capua Airport |  | IT | 1438 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1373 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1314 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1273 |
| 25 | Charles de Gaulle International Airport |  | FR | 1253 |
| 26 | Charlotte/Douglas International Airport |  | US | 1245 |
| 27 | Kuala Lumpur International Airport |  | MY | 1206 |
| 28 | Bengaluru International Airport |  | IN | 1195 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1148 |
| 30 | Ninoy Aquino International Airport |  | PH | 1148 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1129 |
| 32 | Barcelona International Airport |  | ES | 1086 |
| 33 | Seattle-Tacoma International Airport |  | US | 1057 |
| 34 | Viracopos International Airport |  | BR | 1054 |
| 35 | Reno/Tahoe International Airport |  | US | 1049 |
| 36 | Daniel K Inouye International Airport |  | US | 1046 |
| 37 | Calgary International Airport |  | CA | 1046 |
| 38 | Oslo Gardermoen Airport |  | NO | 1020 |
| 39 | Tenerife Norte Airport |  | ES | 1001 |
| 40 | Amsterdam Airport Schiphol |  | NL | 994 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 922 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 674 | 21m | 244 km | 2,838.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 442 | 1h 8m | 770 km | 5,871.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 427 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 272 | 44m | 241 km | 1,129.8 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 260 | 1h 49m | 1,423 km | 6,380.8 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 255 | 8m | - | - |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 248 | 20m | 250 km | 1,071.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 226 | 19m | 99 km | 387.1 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 224 | 1h 15m | 961 km | 3,712.9 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 220 | 19m | 144 km | 547.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 217 | 1h 38m | 1,156 km | 4,329.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 214 | 31m | 369 km | 1,362.2 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 201 | 1h 1m | 695 km | 2,409.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IOORS | IOO | Napoli / Capodichino International Airport (LIRN) | Gioia Del Colle Airport (LIBV) | 2026-08-10 10:32 UTC | 2026-08-10 11:22 UTC | 49m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Antwerp International Airport (Deurne) (EBAW) | 2026-08-10 10:59 UTC | 2026-08-10 11:21 UTC | 21m |
| UBG316 | UBG | Kuala Lumpur International Airport (WMKK) | Naypyidaw Airport (VYEL) | 2026-08-10 08:52 UTC | 2026-08-10 11:14 UTC | 2h 21m |
| DFHBG | DFH | EDBN (EDBN) | Dortmund Airport (EDLW) | 2026-08-10 10:05 UTC | 2026-08-10 11:11 UTC | 1h 6m |
| TACO01 | TAC | Radom-Sadkow Airport (EPRA) | Kielce-Masłów Airport (EPKA) | 2026-08-10 10:43 UTC | 2026-08-10 11:10 UTC | 27m |
| VIP01 | VIP | Dublin Airport (EIDW) | Farnborough Airport (EGLF) | 2026-08-10 10:19 UTC | 2026-08-10 11:10 UTC | 50m |
| BBC585 | BBC | Singapore Changi International Airport (WSSS) | Naypyidaw Airport (VYEL) | 2026-08-10 08:18 UTC | 2026-08-10 10:55 UTC | 2h 37m |
| N363JH |  | Ted Stevens Anchorage International Airport (PANC) | Unalakleet Airport (PAUN) | 2026-08-10 09:27 UTC | 2026-08-10 10:52 UTC | 1h 24m |
| N725CS |  | Portsmouth International At Pease Airport (KPSM) | Laurence G Hanscom Field (KBED) | 2026-08-10 10:36 UTC | 2026-08-10 10:51 UTC | 14m |
| HDB1 | HDB | Al Minhad Air Base (OMDM) | Al Minhad Air Base (OMDM) | 2026-08-10 10:29 UTC | 2026-08-10 10:39 UTC | 10m |
| BOM1 | BOM | Nice-Cote d'Azur Airport (LFMN) | Samedan Airport (LSZS) | 2026-08-10 09:59 UTC | 2026-08-10 10:34 UTC | 35m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-10 10:20 UTC | 2026-08-10 10:32 UTC | 12m |
| HASJF | HAS | Budaors Glider Airport (LHBS) | Farkashegy Airport (LHFH) | 2026-08-10 10:17 UTC | 2026-08-10 10:32 UTC | 14m |
| VLG3SZ | Vueling | Santiago de Compostela Airport (LEST) | Bilbao Airport (LEBB) | 2026-08-10 09:54 UTC | 2026-08-10 10:30 UTC | 35m |
| OAL092 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiathos Island National Airport (LGSK) | 2026-08-10 10:04 UTC | 2026-08-10 10:29 UTC | 24m |
| THA619 | Thai Airways | Simao Airport (ZPSM) | VTBH (VTBH) | 2026-08-10 09:28 UTC | 2026-08-10 10:28 UTC | 1h 0m |
| DTA130 | DTA | Camembe Airport (FNCB) | Tshimpi Airport (FZAM) | 2026-08-10 09:52 UTC | 2026-08-10 10:24 UTC | 32m |
| EIN1LK | Aer Lingus | London Heathrow Airport (EGLL) | Dublin Airport (EIDW) | 2026-08-10 09:20 UTC | 2026-08-10 10:17 UTC | 56m |
| VOE9XQ | VOE | Marseille Provence Airport (LFML) | Rennes-Saint-Jacques Airport (LFRN) | 2026-08-10 09:04 UTC | 2026-08-10 10:16 UTC | 1h 12m |
| RYR2WH | Ryanair | Toulouse-Blagnac Airport (LFBO) | Ifrane Airport (GMFI) | 2026-08-10 08:40 UTC | 2026-08-10 10:15 UTC | 1h 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
