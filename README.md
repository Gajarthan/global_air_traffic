# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_02:11:45_UTC-green)

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

**Latest saved flight:** 2026-08-08 02:11:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 02:11:45 UTC

- **177,228** saved flights
- **57,089** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,228** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,129,956.7 tonnes** estimated CO2 emissions
- **123,475,750 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7015 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3505 |
| 4 | IndiGo | 3096 |
| 5 | Southwest Airlines | 2799 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2099 |
| 9 | LATAM Airlines | 1644 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1580 |
| 12 | WIF | 1481 |
| 13 | Vueling | 1459 |
| 14 | LXJ | 1394 |
| 15 | Swiss International | 1206 |
| 16 | easyJet | 1200 |
| 17 | AXM | 1196 |
| 18 | QLK | 1084 |
| 19 | EJU | 1082 |
| 20 | Alaska Airlines | 1075 |
| 21 | All Nippon Airways | 1072 |
| 22 | VIV | 975 |
| 23 | Cathay Pacific | 945 |
| 24 | CXK | 941 |
| 25 | GLO | 937 |
| 26 | AEE | 923 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 893 |
| 30 | JetBlue | 876 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152577 |
| 2 | 🇪🇸 ES | 11328 |
| 3 | 🇧🇷 BR | 10129 |
| 4 | 🇦🇺 AU | 9993 |
| 5 | 🇨🇦 CA | 9716 |
| 6 | 🇮🇳 IN | 9706 |
| 7 | 🇮🇹 IT | 9143 |
| 8 | 🇩🇪 DE | 8741 |
| 9 | 🇬🇧 GB | 8174 |
| 10 | 🇯🇵 JP | 7099 |
| 11 | 🇫🇷 FR | 7026 |
| 12 | 🇨🇴 CO | 6524 |
| 13 | 🇬🇷 GR | 5150 |
| 14 | 🇲🇽 MX | 5075 |
| 15 | 🇨🇭 CH | 4685 |
| 16 | 🇳🇴 NO | 4609 |
| 17 | 🇹🇷 TR | 4398 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2939 |
| 20 | 🇿🇦 ZA | 2880 |
| 21 | 🇹🇭 TH | 2626 |
| 22 | 🇳🇿 NZ | 2567 |
| 23 | 🇵🇭 PH | 2336 |
| 24 | 🇬🇹 GT | 2266 |
| 25 | 🇰🇷 KR | 2210 |
| 26 | 🇲🇦 MA | 1791 |
| 27 | 🇭🇷 HR | 1741 |
| 28 | 🇲🇪 ME | 1608 |
| 29 | 🇳🇱 NL | 1591 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2947 |
| 3 | Tokyo International Airport |  | JP | 2214 |
| 4 | Guaymaral Airport |  | CO | 2177 |
| 5 | Indira Gandhi International Airport |  | IN | 2157 |
| 6 | Harry Reid International Airport |  | US | 2110 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1914 |
| 8 | Zurich Airport |  | CH | 1878 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1853 |
| 10 | La Aurora Airport |  | GT | 1743 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1626 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1588 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1551 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1470 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1427 |
| 19 | Capua Airport |  | IT | 1383 |
| 20 | Madrid Barajas International Airport |  | ES | 1380 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1252 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1238 |
| 24 | Charlotte/Douglas International Airport |  | US | 1212 |
| 25 | Malpensa International Airport |  | IT | 1211 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1153 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1099 |
| 30 | Ninoy Aquino International Airport |  | PH | 1099 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1096 |
| 32 | Barcelona International Airport |  | ES | 1052 |
| 33 | Seattle-Tacoma International Airport |  | US | 1025 |
| 34 | Daniel K Inouye International Airport |  | US | 1019 |
| 35 | Viracopos International Airport |  | BR | 1015 |
| 36 | Reno/Tahoe International Airport |  | US | 1010 |
| 37 | Calgary International Airport |  | CA | 1009 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 957 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 649 | 21m | 244 km | 2,732.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 415 | 24m | 225 km | 1,610.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 408 | 1h 8m | 770 km | 5,420.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 297 | 27m | 275 km | 1,407.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 244 | 1h 48m | 1,423 km | 5,988.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 219 | 20m | 99 km | 375.1 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 214 | 51m | 556 km | 2,051.4 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 207 | 1h 38m | 1,156 km | 4,129.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 193 | 1h 2m | 695 km | 2,313.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AIRTAC67 | AIR | Roberts Field/Redmond Municipal Airport (KRDM) | OG12 (OG12) | 2026-08-08 01:59 UTC | 2026-08-08 02:11 UTC | 12m |
| ZKTTS | ZKT | Taupo Airport (NZAP) | Taupo Airport (NZAP) | 2026-08-08 01:57 UTC | 2026-08-08 02:09 UTC | 11m |
| N1260K |  | Colonel James Jabara Airport (KAAO) | Colonel James Jabara Airport (KAAO) | 2026-08-08 01:28 UTC | 2026-08-08 02:08 UTC | 40m |
| RAQ | RAQ | Redcliffe Airport (YRED) | Caloundra Airport (YCDR) | 2026-08-08 01:12 UTC | 2026-08-08 02:04 UTC | 51m |
| N885M |  | Bonaventure Airport (CYVB) | Laurence G Hanscom Field (KBED) | 2026-08-08 00:47 UTC | 2026-08-08 01:57 UTC | 1h 9m |
| BRG644 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-08-08 01:41 UTC | 2026-08-08 01:56 UTC | 14m |
| CFDYL | CFD | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-08-08 01:23 UTC | 2026-08-08 01:52 UTC | 28m |
| N2714F |  | Homer Airport (PAHO) | Ted Stevens Anchorage International Airport (PANC) | 2026-08-08 01:00 UTC | 2026-08-08 01:50 UTC | 50m |
| TKR169 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-08 01:41 UTC | 2026-08-08 01:46 UTC | 5m |
| N561AU |  | North Las Vegas Airport (KVGT) | Cottonwood Airport (KP52) | 2026-08-08 00:28 UTC | 2026-08-08 01:43 UTC | 1h 14m |
| N515RA |  | Space Coast Regional Airport (KTIX) | San Francisco International Airport (KSFO) | 2026-08-07 20:38 UTC | 2026-08-08 01:42 UTC | 5h 3m |
| LSXX | LSX | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-08 00:04 UTC | 2026-08-08 01:29 UTC | 1h 25m |
| WFN3404 | WFN | Edmonton International Airport (CYEG) | Moose Jaw Municipal Airport (CJS4) | 2026-08-08 00:24 UTC | 2026-08-08 01:26 UTC | 1h 2m |
| N121MF |  | Rogue Valley International/Medford Airport (KMFR) | Siskiyou County Airport (KSIY) | 2026-08-08 00:37 UTC | 2026-08-08 01:23 UTC | 46m |
| UNN | UNN | Sydney Bankstown Airport (YSBK) | Sydney Bankstown Airport (YSBK) | 2026-08-08 00:47 UTC | 2026-08-08 01:22 UTC | 35m |
| JST834 | JST | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-08-08 00:08 UTC | 2026-08-08 01:20 UTC | 1h 12m |
| MONDO54 | MON | Cairns Army Air Field (Fort Rucker) Airport (KOZR) | Striplin Airfield (AL62) | 2026-08-08 01:04 UTC | 2026-08-08 01:20 UTC | 15m |
| IGO7646 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-08-08 00:52 UTC | 2026-08-08 01:19 UTC | 26m |
| N957JW |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-08-07 23:52 UTC | 2026-08-08 01:19 UTC | 1h 27m |
| N667LF |  | Felts Field (KSFF) | 3OR2 (3OR2) | 2026-08-08 00:35 UTC | 2026-08-08 01:14 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
