# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_22:42:34_UTC-green)

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

**Latest saved flight:** 2026-07-31 22:42:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-31 22:42:34 UTC

- **163,604** saved flights
- **53,888** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **163,604** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,963,822.7 tonnes** estimated CO2 emissions
- **113,844,793 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6534 |
| 2 | SkyWest Airlines | 5974 |
| 3 | EJA | 3252 |
| 4 | IndiGo | 2860 |
| 5 | American Airlines | 2585 |
| 6 | Southwest Airlines | 2562 |
| 7 | ENY | 2036 |
| 8 | Delta Air Lines | 1951 |
| 9 | Lufthansa | 1530 |
| 10 | LATAM Airlines | 1530 |
| 11 | AZU | 1434 |
| 12 | WIF | 1378 |
| 13 | Vueling | 1352 |
| 14 | LXJ | 1274 |
| 15 | AXM | 1131 |
| 16 | Swiss International | 1124 |
| 17 | easyJet | 1071 |
| 18 | Alaska Airlines | 1013 |
| 19 | QLK | 1003 |
| 20 | EJU | 1001 |
| 21 | All Nippon Airways | 999 |
| 22 | VIV | 902 |
| 23 | CXK | 878 |
| 24 | Cathay Pacific | 867 |
| 25 | United Airlines | 860 |
| 26 | GLO | 856 |
| 27 | AEE | 852 |
| 28 | MXY | 846 |
| 29 | Air France | 844 |
| 30 | JetBlue | 835 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 141501 |
| 2 | 🇪🇸 ES | 10473 |
| 3 | 🇧🇷 BR | 9334 |
| 4 | 🇦🇺 AU | 9202 |
| 5 | 🇮🇳 IN | 8991 |
| 6 | 🇨🇦 CA | 8917 |
| 7 | 🇮🇹 IT | 8420 |
| 8 | 🇩🇪 DE | 8209 |
| 9 | 🇬🇧 GB | 7511 |
| 10 | 🇯🇵 JP | 6587 |
| 11 | 🇫🇷 FR | 6463 |
| 12 | 🇨🇴 CO | 5861 |
| 13 | 🇲🇽 MX | 4694 |
| 14 | 🇬🇷 GR | 4689 |
| 15 | 🇳🇴 NO | 4308 |
| 16 | 🇨🇭 CH | 4290 |
| 17 | 🇹🇷 TR | 3909 |
| 18 | 🇲🇾 MY | 2938 |
| 19 | 🇵🇱 PL | 2773 |
| 20 | 🇿🇦 ZA | 2653 |
| 21 | 🇳🇿 NZ | 2389 |
| 22 | 🇹🇭 TH | 2316 |
| 23 | 🇵🇭 PH | 2134 |
| 24 | 🇰🇷 KR | 2119 |
| 25 | 🇬🇹 GT | 2115 |
| 26 | 🇲🇦 MA | 1651 |
| 27 | 🇲🇪 ME | 1537 |
| 28 | 🇭🇷 HR | 1537 |
| 29 | 🇳🇱 NL | 1487 |
| 30 | 🇲🇴 MO | 1378 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3342 |
| 2 | Denver International Airport |  | US | 2727 |
| 3 | Tokyo International Airport |  | JP | 2076 |
| 4 | Guaymaral Airport |  | CO | 2061 |
| 5 | Indira Gandhi International Airport |  | IN | 1998 |
| 6 | Harry Reid International Airport |  | US | 1983 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1797 |
| 8 | Zurich Airport |  | CH | 1744 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1722 |
| 10 | La Aurora Airport |  | GT | 1638 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1519 |
| 12 | El Dorado International Airport |  | CO | 1502 |
| 13 | Frankfurt am Main International Airport |  | DE | 1485 |
| 14 | Chicago O'Hare International Airport |  | US | 1481 |
| 15 | Salt Lake City International Airport |  | US | 1472 |
| 16 | Macau International Airport |  | MO | 1378 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1374 |
| 18 | Congonhas Airport |  | BR | 1352 |
| 19 | Madrid Barajas International Airport |  | ES | 1292 |
| 20 | Capua Airport |  | IT | 1281 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1249 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1157 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1157 |
| 24 | Charlotte/Douglas International Airport |  | US | 1151 |
| 25 | Kuala Lumpur International Airport |  | MY | 1118 |
| 26 | Charles de Gaulle International Airport |  | FR | 1115 |
| 27 | Malpensa International Airport |  | IT | 1080 |
| 28 | Bengaluru International Airport |  | IN | 1065 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1005 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1002 |
| 31 | Ninoy Aquino International Airport |  | PH | 1002 |
| 32 | Barcelona International Airport |  | ES | 967 |
| 33 | Daniel K Inouye International Airport |  | US | 958 |
| 34 | Seattle-Tacoma International Airport |  | US | 948 |
| 35 | Calgary International Airport |  | CA | 934 |
| 36 | Viracopos International Airport |  | BR | 927 |
| 37 | Scottsdale Airport |  | US | 916 |
| 38 | Tenerife Norte Airport |  | ES | 913 |
| 39 | Oslo Gardermoen Airport |  | NO | 912 |
| 40 | Reno/Tahoe International Airport |  | US | 899 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 862 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 596 | 21m | 244 km | 2,509.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 391 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 387 | 24m | 225 km | 1,501.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 373 | 1h 9m | 770 km | 4,955.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 302 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 284 | 27m | 275 km | 1,345.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 243 | 22m | 55 km | 231.0 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 240 | 19m | 165 km | 682.7 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 238 | 44m | 241 km | 988.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 224 | 1h 47m | 1,423 km | 5,497.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 213 | 26m | 215 km | 788.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 209 | 20m | 99 km | 358.0 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 208 | 20m | 250 km | 898.4 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 207 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 201 | 31m | 49 km | 169.9 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 195 | 1h 15m | 961 km | 3,232.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 192 | 18m | 144 km | 477.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 190 | 31m | 369 km | 1,209.4 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 187 | 50m | 556 km | 1,792.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 182 | 1h 39m | 1,156 km | 3,630.8 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 179 | 44m | 452 km | 1,395.0 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THY6201 | Turkish Airlines | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-07-31 08:27 UTC | 2026-07-31 22:42 UTC | 14h 15m |
| CPA696 | Cathay Pacific | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-07-31 17:35 UTC | 2026-07-31 22:35 UTC | 4h 59m |
| RPA4773 | Republic Airways | Laguardia Airport (KLGA) | Forest Hill Airport (MD31) | 2026-07-31 21:37 UTC | 2026-07-31 22:28 UTC | 51m |
| SWA1053 | Southwest Airlines | General Edward Lawrence Logan International Airport (KBOS) | Ewing Airport (MD28) | 2026-07-31 21:09 UTC | 2026-07-31 22:28 UTC | 1h 19m |
| N882KB |  | Charles M Schulz/Sonoma County Airport (KSTS) | Lake Tahoe Airport (KTVL) | 2026-07-31 22:07 UTC | 2026-07-31 22:27 UTC | 20m |
| VTE5424 | VTE | Charlotte/Douglas International Airport (KCLT) | Mercer County Airport (KBLF) | 2026-07-31 21:59 UTC | 2026-07-31 22:23 UTC | 23m |
| LXJ342 | LXJ | Van Nuys Airport (KVNY) | North Las Vegas Airport (KVGT) | 2026-07-31 21:36 UTC | 2026-07-31 22:22 UTC | 46m |
| GEC8466 | GEC | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-07-31 17:21 UTC | 2026-07-31 22:19 UTC | 4h 57m |
| TOM38K | TOM | Gran Canaria Airport (GCLP) | London Gatwick Airport (EGKK) | 2026-07-31 18:35 UTC | 2026-07-31 22:16 UTC | 3h 40m |
| TKR838 | TKR | Animas Air Park (K00C) | True Grit South Airport (CO95) | 2026-07-31 22:00 UTC | 2026-07-31 22:15 UTC | 15m |
| T868 |  | Animas Air Park (K00C) | True Grit South Airport (CO95) | 2026-07-31 22:00 UTC | 2026-07-31 22:15 UTC | 15m |
| AAL3263 | American Airlines | Charlotte/Douglas International Airport (KCLT) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-07-31 21:04 UTC | 2026-07-31 22:15 UTC | 1h 11m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-07-31 10:35 UTC | 2026-07-31 22:12 UTC | 11h 37m |
| N1377M |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-07-31 22:00 UTC | 2026-07-31 22:12 UTC | 11m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Zhuhai Airport (ZGSD) | 2026-07-31 11:13 UTC | 2026-07-31 22:09 UTC | 10h 56m |
| N748RE |  | Waukegan Ntl Airport (KUGN) | Rhinelander/Oneida County Airport (KRHI) | 2026-07-31 21:38 UTC | 2026-07-31 22:09 UTC | 30m |
| N578JZ |  | Sacramento Mather Airport (KMHR) | CA38 (CA38) | 2026-07-31 21:40 UTC | 2026-07-31 22:09 UTC | 28m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-07-31 07:38 UTC | 2026-07-31 22:06 UTC | 14h 28m |
| AWH92V | AWH | Husum-Schwesing Airport (EDXJ) | Stuttgart Airport (EDDS) | 2026-07-31 20:22 UTC | 2026-07-31 22:05 UTC | 1h 43m |
| N80945 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-31 21:16 UTC | 2026-07-31 22:02 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
