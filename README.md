# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_09:58:27_UTC-green)

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

**Latest saved flight:** 2026-08-09 09:58:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 09:58:27 UTC

- **180,654** saved flights
- **57,792** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **180,654** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,171,509.3 tonnes** estimated CO2 emissions
- **125,884,595 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7154 |
| 2 | SkyWest Airlines | 6582 |
| 3 | EJA | 3555 |
| 4 | IndiGo | 3165 |
| 5 | Southwest Airlines | 2840 |
| 6 | American Airlines | 2817 |
| 7 | ENY | 2250 |
| 8 | Delta Air Lines | 2142 |
| 9 | LATAM Airlines | 1680 |
| 10 | AZU | 1613 |
| 11 | Lufthansa | 1607 |
| 12 | Vueling | 1495 |
| 13 | WIF | 1494 |
| 14 | LXJ | 1407 |
| 15 | easyJet | 1235 |
| 16 | Swiss International | 1229 |
| 17 | AXM | 1223 |
| 18 | QLK | 1115 |
| 19 | EJU | 1105 |
| 20 | All Nippon Airways | 1102 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 996 |
| 23 | GLO | 965 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 946 |
| 26 | AEE | 944 |
| 27 | Air France | 931 |
| 28 | United Airlines | 929 |
| 29 | MXY | 905 |
| 30 | PGT | 905 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 154731 |
| 2 | 🇪🇸 ES | 11610 |
| 3 | 🇧🇷 BR | 10345 |
| 4 | 🇦🇺 AU | 10187 |
| 5 | 🇮🇳 IN | 9922 |
| 6 | 🇨🇦 CA | 9852 |
| 7 | 🇮🇹 IT | 9336 |
| 8 | 🇩🇪 DE | 8932 |
| 9 | 🇬🇧 GB | 8342 |
| 10 | 🇯🇵 JP | 7327 |
| 11 | 🇫🇷 FR | 7188 |
| 12 | 🇨🇴 CO | 6707 |
| 13 | 🇬🇷 GR | 5284 |
| 14 | 🇲🇽 MX | 5164 |
| 15 | 🇨🇭 CH | 4813 |
| 16 | 🇳🇴 NO | 4650 |
| 17 | 🇹🇷 TR | 4626 |
| 18 | 🇲🇾 MY | 3190 |
| 19 | 🇵🇱 PL | 3021 |
| 20 | 🇿🇦 ZA | 2948 |
| 21 | 🇹🇭 TH | 2769 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2399 |
| 24 | 🇬🇹 GT | 2294 |
| 25 | 🇰🇷 KR | 2258 |
| 26 | 🇲🇦 MA | 1821 |
| 27 | 🇭🇷 HR | 1797 |
| 28 | 🇲🇪 ME | 1641 |
| 29 | 🇳🇱 NL | 1621 |
| 30 | 🇲🇴 MO | 1513 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3732 |
| 2 | Denver International Airport |  | US | 2987 |
| 3 | Tokyo International Airport |  | JP | 2275 |
| 4 | Guaymaral Airport |  | CO | 2223 |
| 5 | Indira Gandhi International Airport |  | IN | 2214 |
| 6 | Harry Reid International Airport |  | US | 2127 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1945 |
| 8 | Zurich Airport |  | CH | 1919 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1878 |
| 10 | La Aurora Airport |  | GT | 1762 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1648 |
| 12 | Chicago O'Hare International Airport |  | US | 1626 |
| 13 | Salt Lake City International Airport |  | US | 1616 |
| 14 | El Dorado International Airport |  | CO | 1611 |
| 15 | Frankfurt am Main International Airport |  | DE | 1568 |
| 16 | Macau International Airport |  | MO | 1513 |
| 17 | Congonhas Airport |  | BR | 1500 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1437 |
| 19 | Madrid Barajas International Airport |  | ES | 1419 |
| 20 | Capua Airport |  | IT | 1414 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1351 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1285 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1247 |
| 25 | Charlotte/Douglas International Airport |  | US | 1224 |
| 26 | Charles de Gaulle International Airport |  | FR | 1223 |
| 27 | Kuala Lumpur International Airport |  | MY | 1199 |
| 28 | Bengaluru International Airport |  | IN | 1179 |
| 29 | Ninoy Aquino International Airport |  | PH | 1130 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1122 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1109 |
| 32 | Barcelona International Airport |  | ES | 1075 |
| 33 | Seattle-Tacoma International Airport |  | US | 1041 |
| 34 | Daniel K Inouye International Airport |  | US | 1040 |
| 35 | Viracopos International Airport |  | BR | 1036 |
| 36 | Reno/Tahoe International Airport |  | US | 1032 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 999 |
| 39 | Tenerife Norte Airport |  | ES | 985 |
| 40 | Amsterdam Airport Schiphol |  | NL | 975 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 918 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 669 | 21m | 244 km | 2,817.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 430 | 1h 8m | 770 km | 5,712.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 303 | 27m | 275 km | 1,435.8 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 253 | 1h 48m | 1,423 km | 6,209.0 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 241 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 237 | 20m | 250 km | 1,023.7 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 218 | 1h 15m | 961 km | 3,613.5 t |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 216 | 19m | 144 km | 537.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 212 | 1h 38m | 1,156 km | 4,229.3 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 210 | 31m | 369 km | 1,336.7 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 207 | 24m | 218 km | 779.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 203 | 28m | 152 km | 530.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FR30 |  | RAF Northolt (EGWU) | Cranfield Airport (EGTC) | 2026-08-09 08:43 UTC | 2026-08-09 09:58 UTC | 1h 14m |
| GSSCR | GSS | Fadmoor Airfield (EG19) | Fadmoor Airfield (EG19) | 2026-08-09 09:45 UTC | 2026-08-09 09:50 UTC | 4m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 09:20 UTC | 2026-08-09 09:50 UTC | 29m |
| AFR1654 | Air France | Charles de Gaulle International Airport (LFPG) | Ain Oussera Airport (DAAQ) | 2026-08-09 08:01 UTC | 2026-08-09 09:49 UTC | 1h 47m |
| FHOLX | FHO | Abbeville-Buigny-Saint-Maclou Airport (LFOI) | Eu Mers Le Treport Airport (LFAE) | 2026-08-09 09:09 UTC | 2026-08-09 09:44 UTC | 34m |
| NHL06 | NHL | Wolverhampton Halfpenny Green Airport (EGBO) | Wolverhampton Halfpenny Green Airport (EGBO) | 2026-08-09 08:52 UTC | 2026-08-09 09:42 UTC | 49m |
| EJU32DZ | EJU | Porto Santo Airport (LPPS) | Aveiro Airport (LPAV) | 2026-08-09 08:04 UTC | 2026-08-09 09:38 UTC | 1h 33m |
| DHXCF | DHX | Lager Hammelburg Airport (EDFJ) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-08-09 09:29 UTC | 2026-08-09 09:37 UTC | 8m |
| SXS7RR | SXS | Zurich Airport (LSZH) | Kaklic Airport (LTFA) | 2026-08-09 07:24 UTC | 2026-08-09 09:35 UTC | 2h 10m |
| A6FTK |  | Al Minhad Air Base (OMDM) | Al Maktoum International Airport (OMDW) | 2026-08-09 08:38 UTC | 2026-08-09 09:27 UTC | 49m |
| AXM464 | AXM | Kuala Lumpur International Airport (WMKK) | Bentayan Airport (WIPY) | 2026-08-09 08:30 UTC | 2026-08-09 09:18 UTC | 48m |
| DMFGD | DMF | Gerstetten Airport (EDPT) | Hoefen Airport (LOIR) | 2026-08-09 08:20 UTC | 2026-08-09 09:16 UTC | 55m |
| RYR49BH | Ryanair | Manchester Airport (EGCC) | Dublin Airport (EIDW) | 2026-08-09 08:35 UTC | 2026-08-09 09:15 UTC | 39m |
| WIF3T | WIF | Bodø Airport (ENBO) | Leknes Airport (ENLK) | 2026-08-09 09:02 UTC | 2026-08-09 09:14 UTC | 12m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-09 08:59 UTC | 2026-08-09 09:09 UTC | 10m |
| DLH8UL | Lufthansa | Frankfurt am Main International Airport (EDDF) | Turweston Airport (EGBT) | 2026-08-09 07:47 UTC | 2026-08-09 09:05 UTC | 1h 18m |
| N402CN |  | Council Bluffs Municipal Airport (KCBF) | Millard Airport (KMLE) | 2026-08-09 08:56 UTC | 2026-08-09 09:04 UTC | 8m |
| AFR74UC | Air France | Charles de Gaulle International Airport (LFPG) | Bergen Airport Flesland (ENBR) | 2026-08-09 07:21 UTC | 2026-08-09 09:02 UTC | 1h 41m |
| ABP721 | ABP | Václav Havel Airport (LKPR) | Samedan Airport (LSZS) | 2026-08-09 08:17 UTC | 2026-08-09 09:02 UTC | 45m |
| DLH63M | Lufthansa | Munich International Airport (EDDM) | Vitoria/Foronda Airport (LEVT) | 2026-08-09 07:15 UTC | 2026-08-09 09:02 UTC | 1h 47m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
