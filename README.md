# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_03:19:52_UTC-green)

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

**Latest saved flight:** 2026-08-07 03:19:52 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 03:19:52 UTC

- **174,489** saved flights
- **56,455** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,489** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,100,246.2 tonnes** estimated CO2 emissions
- **121,753,401 km** total distance flown
- **859 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6910 |
| 2 | SkyWest Airlines | 6390 |
| 3 | EJA | 3458 |
| 4 | IndiGo | 3050 |
| 5 | Southwest Airlines | 2754 |
| 6 | American Airlines | 2733 |
| 7 | ENY | 2173 |
| 8 | Delta Air Lines | 2066 |
| 9 | LATAM Airlines | 1615 |
| 10 | Lufthansa | 1577 |
| 11 | AZU | 1543 |
| 12 | WIF | 1461 |
| 13 | Vueling | 1431 |
| 14 | LXJ | 1368 |
| 15 | AXM | 1190 |
| 16 | Swiss International | 1186 |
| 17 | easyJet | 1183 |
| 18 | QLK | 1067 |
| 19 | EJU | 1064 |
| 20 | All Nippon Airways | 1062 |
| 21 | Alaska Airlines | 1062 |
| 22 | VIV | 961 |
| 23 | Cathay Pacific | 943 |
| 24 | CXK | 926 |
| 25 | GLO | 921 |
| 26 | AEE | 909 |
| 27 | United Airlines | 906 |
| 28 | Air France | 893 |
| 29 | MXY | 882 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150313 |
| 2 | 🇪🇸 ES | 11139 |
| 3 | 🇧🇷 BR | 9943 |
| 4 | 🇦🇺 AU | 9826 |
| 5 | 🇮🇳 IN | 9571 |
| 6 | 🇨🇦 CA | 9559 |
| 7 | 🇮🇹 IT | 8985 |
| 8 | 🇩🇪 DE | 8631 |
| 9 | 🇬🇧 GB | 8066 |
| 10 | 🇯🇵 JP | 7024 |
| 11 | 🇫🇷 FR | 6910 |
| 12 | 🇨🇴 CO | 6422 |
| 13 | 🇬🇷 GR | 5057 |
| 14 | 🇲🇽 MX | 4993 |
| 15 | 🇨🇭 CH | 4600 |
| 16 | 🇳🇴 NO | 4543 |
| 17 | 🇹🇷 TR | 4276 |
| 18 | 🇲🇾 MY | 3095 |
| 19 | 🇵🇱 PL | 2912 |
| 20 | 🇿🇦 ZA | 2808 |
| 21 | 🇹🇭 TH | 2570 |
| 22 | 🇳🇿 NZ | 2540 |
| 23 | 🇵🇭 PH | 2303 |
| 24 | 🇬🇹 GT | 2225 |
| 25 | 🇰🇷 KR | 2194 |
| 26 | 🇲🇦 MA | 1752 |
| 27 | 🇭🇷 HR | 1687 |
| 28 | 🇲🇪 ME | 1593 |
| 29 | 🇳🇱 NL | 1571 |
| 30 | 🇲🇴 MO | 1503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3604 |
| 2 | Denver International Airport |  | US | 2891 |
| 3 | Tokyo International Airport |  | JP | 2193 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2128 |
| 6 | Harry Reid International Airport |  | US | 2087 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1891 |
| 8 | Zurich Airport |  | CH | 1845 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1828 |
| 10 | La Aurora Airport |  | GT | 1713 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1605 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1576 |
| 14 | Salt Lake City International Airport |  | US | 1564 |
| 15 | Frankfurt am Main International Airport |  | DE | 1541 |
| 16 | Macau International Airport |  | MO | 1503 |
| 17 | Congonhas Airport |  | BR | 1439 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1422 |
| 19 | Capua Airport |  | IT | 1358 |
| 20 | Madrid Barajas International Airport |  | ES | 1356 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1306 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1231 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1219 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Charles de Gaulle International Airport |  | FR | 1181 |
| 26 | Malpensa International Airport |  | IT | 1179 |
| 27 | Kuala Lumpur International Airport |  | MY | 1167 |
| 28 | Bengaluru International Airport |  | IN | 1138 |
| 29 | Ninoy Aquino International Airport |  | PH | 1084 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1083 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1078 |
| 32 | Barcelona International Airport |  | ES | 1028 |
| 33 | Seattle-Tacoma International Airport |  | US | 1006 |
| 34 | Daniel K Inouye International Airport |  | US | 1005 |
| 35 | Calgary International Airport |  | CA | 992 |
| 36 | Reno/Tahoe International Airport |  | US | 991 |
| 37 | Viracopos International Airport |  | BR | 990 |
| 38 | Oslo Gardermoen Airport |  | NO | 971 |
| 39 | Tenerife Norte Airport |  | ES | 963 |
| 40 | Scottsdale Airport |  | US | 947 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 637 | 21m | 244 km | 2,682.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 411 | 24m | 225 km | 1,594.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 397 | 1h 8m | 770 km | 5,273.8 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 321 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 262 | 44m | 241 km | 1,088.3 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 239 | 1h 48m | 1,423 km | 5,865.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 225 | 20m | 250 km | 971.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 214 | 20m | 99 km | 366.6 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 207 | 19m | 144 km | 514.9 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 203 | 1h 38m | 1,156 km | 4,049.8 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 195 | 24m | 218 km | 734.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 190 | 43m | 452 km | 1,480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MONDO80 | MON | Liberty Field (7AL5) | Liberty Field (7AL5) | 2026-08-07 01:57 UTC | 2026-08-07 03:19 UTC | 1h 22m |
| N19EV |  | Massey Farm Airport (AZ34) | Lake Havasu City Airport (KHII) | 2026-08-07 02:57 UTC | 2026-08-07 03:12 UTC | 15m |
| EOQ | EOQ | Ballina Byron Gateway Airport (YBNA) | Ballina Byron Gateway Airport (YBNA) | 2026-08-07 02:39 UTC | 2026-08-07 03:12 UTC | 32m |
| SKQ34 | SKQ | Burlington/Alamance Regional Airport (KBUY) | Savannah/Hilton Head International Airport (KSAV) | 2026-08-07 02:01 UTC | 2026-08-07 03:06 UTC | 1h 5m |
| TKR137 | TKR | Boise Air Trml/Gowen Field (KBOI) | Cascade Airport (KU70) | 2026-08-07 02:51 UTC | 2026-08-07 03:01 UTC | 10m |
| YJZ | YJZ | Lyndley Airport (YLYD) | Sunshine Coast Airport (YBMC) | 2026-08-07 02:26 UTC | 2026-08-07 02:57 UTC | 31m |
| BELLS70 | Brussels Airlines | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-08-07 01:29 UTC | 2026-08-07 02:56 UTC | 1h 27m |
| N221LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-08-07 01:19 UTC | 2026-08-07 02:51 UTC | 1h 32m |
| TKR168 | TKR | Boise Air Trml/Gowen Field (KBOI) | High Valley Airport (ID35) | 2026-08-07 02:38 UTC | 2026-08-07 02:49 UTC | 10m |
| N250AL |  | Bay City Regional Airport (KBYY) | Eldon Model Airpark (KH79) | 2026-08-07 01:10 UTC | 2026-08-07 02:47 UTC | 1h 36m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-07 02:36 UTC | 2026-08-07 02:43 UTC | 7m |
| N631JD |  | Miami-Opa Locka Executive Airport (KOPF) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-08-07 00:59 UTC | 2026-08-07 02:40 UTC | 1h 41m |
| N69P |  | San Gabriel Valley Airport (KEMT) | Palm Springs International Airport (KPSP) | 2026-08-07 02:15 UTC | 2026-08-07 02:39 UTC | 23m |
| RS46 |  | CA75 (CA75) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-07 02:08 UTC | 2026-08-07 02:37 UTC | 28m |
| N7SE |  | Van Nuys Airport (KVNY) | Greeley-Weld County Airport (KGXY) | 2026-08-07 00:40 UTC | 2026-08-07 02:35 UTC | 1h 54m |
| N977SC |  | Grand Prairie Municipal Airport (KGPM) | Mid-Way Regional Airport (KJWY) | 2026-08-07 02:16 UTC | 2026-08-07 02:32 UTC | 16m |
| EAF401 | EAF | Burgas Airport (LBBG) | LLBO (LLBO) | 2026-08-07 00:55 UTC | 2026-08-07 02:26 UTC | 1h 30m |
| TKR138 | TKR | Roberts Field/Redmond Municipal Airport (KRDM) | OG12 (OG12) | 2026-08-07 02:16 UTC | 2026-08-07 02:25 UTC | 9m |
| CWA935 | CWA | Edmonton International Airport (CYEG) | Glendon Airport (CFP5) | 2026-08-07 01:59 UTC | 2026-08-07 02:22 UTC | 22m |
| QLK322D | QLK | Brisbane International Airport (YBBN) | Childers Airport (YCDS) | 2026-08-07 01:53 UTC | 2026-08-07 02:22 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
