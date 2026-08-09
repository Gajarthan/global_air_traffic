# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_18:01:33_UTC-green)

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

**Latest saved flight:** 2026-08-09 18:01:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 18:01:33 UTC

- **181,996** saved flights
- **58,105** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,996** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,187,215.5 tonnes** estimated CO2 emissions
- **126,795,099 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7219 |
| 2 | SkyWest Airlines | 6609 |
| 3 | EJA | 3581 |
| 4 | IndiGo | 3193 |
| 5 | Southwest Airlines | 2853 |
| 6 | American Airlines | 2831 |
| 7 | ENY | 2265 |
| 8 | Delta Air Lines | 2151 |
| 9 | LATAM Airlines | 1699 |
| 10 | AZU | 1630 |
| 11 | Lufthansa | 1617 |
| 12 | Vueling | 1506 |
| 13 | WIF | 1506 |
| 14 | LXJ | 1423 |
| 15 | Swiss International | 1249 |
| 16 | easyJet | 1245 |
| 17 | AXM | 1226 |
| 18 | EJU | 1119 |
| 19 | QLK | 1116 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 1001 |
| 23 | GLO | 975 |
| 24 | CXK | 951 |
| 25 | AEE | 949 |
| 26 | Cathay Pacific | 947 |
| 27 | Air France | 946 |
| 28 | United Airlines | 931 |
| 29 | PGT | 921 |
| 30 | MXY | 910 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 155585 |
| 2 | 🇪🇸 ES | 11723 |
| 3 | 🇧🇷 BR | 10447 |
| 4 | 🇦🇺 AU | 10203 |
| 5 | 🇮🇳 IN | 10005 |
| 6 | 🇨🇦 CA | 9894 |
| 7 | 🇮🇹 IT | 9434 |
| 8 | 🇩🇪 DE | 9028 |
| 9 | 🇬🇧 GB | 8421 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7272 |
| 12 | 🇨🇴 CO | 6767 |
| 13 | 🇬🇷 GR | 5338 |
| 14 | 🇲🇽 MX | 5191 |
| 15 | 🇨🇭 CH | 4865 |
| 16 | 🇹🇷 TR | 4715 |
| 17 | 🇳🇴 NO | 4686 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3059 |
| 20 | 🇿🇦 ZA | 3025 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2318 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1841 |
| 27 | 🇭🇷 HR | 1814 |
| 28 | 🇲🇪 ME | 1648 |
| 29 | 🇳🇱 NL | 1636 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3759 |
| 2 | Denver International Airport |  | US | 3001 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2236 |
| 5 | Guaymaral Airport |  | CO | 2231 |
| 6 | Harry Reid International Airport |  | US | 2132 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1958 |
| 8 | Zurich Airport |  | CH | 1944 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1888 |
| 10 | La Aurora Airport |  | GT | 1779 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1654 |
| 12 | Chicago O'Hare International Airport |  | US | 1632 |
| 13 | El Dorado International Airport |  | CO | 1624 |
| 14 | Salt Lake City International Airport |  | US | 1621 |
| 15 | Frankfurt am Main International Airport |  | DE | 1584 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1516 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1442 |
| 19 | Madrid Barajas International Airport |  | ES | 1433 |
| 20 | Capua Airport |  | IT | 1426 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1359 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1299 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1259 |
| 25 | Charles de Gaulle International Airport |  | FR | 1244 |
| 26 | Charlotte/Douglas International Airport |  | US | 1230 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1129 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1110 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1046 |
| 34 | Seattle-Tacoma International Airport |  | US | 1044 |
| 35 | Daniel K Inouye International Airport |  | US | 1042 |
| 36 | Reno/Tahoe International Airport |  | US | 1039 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1009 |
| 39 | Tenerife Norte Airport |  | ES | 996 |
| 40 | Vitoria/Foronda Airport |  | ES | 988 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 920 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 420 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 248 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 244 | 20m | 250 km | 1,053.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 221 | 1h 15m | 961 km | 3,663.2 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 218 | 19m | 144 km | 542.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 215 | 1h 38m | 1,156 km | 4,289.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 213 | 24m | 218 km | 802.5 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 204 | 28m | 152 km | 533.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3341R |  | Fullerton Municipal Airport (KFUL) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-08-09 16:24 UTC | 2026-08-09 18:01 UTC | 1h 37m |
| N726MM |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-09 17:48 UTC | 2026-08-09 17:59 UTC | 11m |
| N7693Y |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-08-09 17:32 UTC | 2026-08-09 17:58 UTC | 26m |
| N75727 |  | Caldwell Executive Airport (KEUL) | Emmett Municipal Airport (KS78) | 2026-08-09 17:44 UTC | 2026-08-09 17:58 UTC | 13m |
| N803DB |  | NV13 (NV13) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-08-09 16:21 UTC | 2026-08-09 17:56 UTC | 1h 34m |
| TKR132 | TKR | Parowan Airport (K1L9) | NV54 (NV54) | 2026-08-09 17:28 UTC | 2026-08-09 17:55 UTC | 26m |
| EJA138 | EJA | John Wayne/Orange County Airport (KSNA) | Ziggy's Airport (0ID1) | 2026-08-09 16:34 UTC | 2026-08-09 17:52 UTC | 1h 17m |
| N3546T |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Reid-Hillview Of Santa Clara County Airport (KRHV) | 2026-08-09 16:24 UTC | 2026-08-09 17:48 UTC | 1h 24m |
| N219BH |  | Stout Airport (FD83) | Stout Airport (FD83) | 2026-08-09 17:13 UTC | 2026-08-09 17:46 UTC | 33m |
| N64962 |  | Montgomery County Airpark (KGAI) | Montgomery County Airpark (KGAI) | 2026-08-09 17:27 UTC | 2026-08-09 17:45 UTC | 17m |
| N76091 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-09 17:34 UTC | 2026-08-09 17:45 UTC | 10m |
| OKFBA | OKF | Jaromer Airport (LKJA) | Nove Mesto Airport (LKNM) | 2026-08-09 17:31 UTC | 2026-08-09 17:43 UTC | 11m |
| TKR41 | TKR | Citabriair Airport (UT43) | Creech Afb Airport (KINS) | 2026-08-09 17:18 UTC | 2026-08-09 17:42 UTC | 24m |
| LXJ481 | LXJ | San Francisco International Airport (KSFO) | Truckee-Tahoe Airport (KTRK) | 2026-08-09 17:11 UTC | 2026-08-09 17:39 UTC | 27m |
| N12704 |  | Frederick Municipal Airport (KFDK) | Frederick Municipal Airport (KFDK) | 2026-08-09 16:43 UTC | 2026-08-09 17:39 UTC | 55m |
| N727KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-09 16:47 UTC | 2026-08-09 17:36 UTC | 49m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-08-09 14:10 UTC | 2026-08-09 17:36 UTC | 3h 25m |
| EFY9156 | EFY | Enrique Olaya Herrera Airport (SKMD) | SKAN (SKAN) | 2026-08-09 15:52 UTC | 2026-08-09 17:31 UTC | 1h 39m |
| N638CT |  | San Marcos Regional Airport (KHYI) | San Marcos Regional Airport (KHYI) | 2026-08-09 17:28 UTC | 2026-08-09 17:31 UTC | 3m |
| N929KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-09 16:41 UTC | 2026-08-09 17:31 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
