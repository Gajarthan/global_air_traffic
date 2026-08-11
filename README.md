# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_17:50:11_UTC-green)

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

**Latest saved flight:** 2026-08-11 17:50:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 17:50:11 UTC

- **187,456** saved flights
- **59,415** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **187,456** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,248,240.8 tonnes** estimated CO2 emissions
- **130,332,797 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7448 |
| 2 | SkyWest Airlines | 6806 |
| 3 | EJA | 3688 |
| 4 | IndiGo | 3277 |
| 5 | Southwest Airlines | 2932 |
| 6 | American Airlines | 2909 |
| 7 | ENY | 2327 |
| 8 | Delta Air Lines | 2206 |
| 9 | LATAM Airlines | 1754 |
| 10 | AZU | 1685 |
| 11 | Lufthansa | 1644 |
| 12 | WIF | 1552 |
| 13 | Vueling | 1550 |
| 14 | LXJ | 1463 |
| 15 | easyJet | 1292 |
| 16 | Swiss International | 1281 |
| 17 | AXM | 1247 |
| 18 | EJU | 1159 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1030 |
| 23 | GLO | 1007 |
| 24 | Air France | 976 |
| 25 | AEE | 968 |
| 26 | PGT | 964 |
| 27 | CXK | 962 |
| 28 | United Airlines | 953 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 933 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159828 |
| 2 | 🇪🇸 ES | 12082 |
| 3 | 🇧🇷 BR | 10763 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇮🇳 IN | 10263 |
| 6 | 🇨🇦 CA | 10227 |
| 7 | 🇮🇹 IT | 9718 |
| 8 | 🇩🇪 DE | 9285 |
| 9 | 🇬🇧 GB | 8724 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7507 |
| 12 | 🇨🇴 CO | 7103 |
| 13 | 🇬🇷 GR | 5503 |
| 14 | 🇲🇽 MX | 5332 |
| 15 | 🇨🇭 CH | 5027 |
| 16 | 🇹🇷 TR | 4963 |
| 17 | 🇳🇴 NO | 4827 |
| 18 | 🇲🇾 MY | 3262 |
| 19 | 🇿🇦 ZA | 3154 |
| 20 | 🇵🇱 PL | 3113 |
| 21 | 🇹🇭 TH | 2894 |
| 22 | 🇳🇿 NZ | 2666 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2390 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1906 |
| 27 | 🇭🇷 HR | 1901 |
| 28 | 🇲🇪 ME | 1679 |
| 29 | 🇳🇱 NL | 1676 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3882 |
| 2 | Denver International Airport |  | US | 3078 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2311 |
| 5 | Guaymaral Airport |  | CO | 2300 |
| 6 | Harry Reid International Airport |  | US | 2191 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1998 |
| 8 | Zurich Airport |  | CH | 1997 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1942 |
| 10 | La Aurora Airport |  | GT | 1837 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1699 |
| 12 | El Dorado International Airport |  | CO | 1684 |
| 13 | Salt Lake City International Airport |  | US | 1668 |
| 14 | Chicago O'Hare International Airport |  | US | 1654 |
| 15 | Frankfurt am Main International Airport |  | DE | 1613 |
| 16 | Congonhas Airport |  | BR | 1565 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1480 |
| 19 | Capua Airport |  | IT | 1462 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1456 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1394 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1342 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1290 |
| 25 | Charles de Gaulle International Airport |  | FR | 1282 |
| 26 | Charlotte/Douglas International Airport |  | US | 1260 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1169 |
| 30 | Ninoy Aquino International Airport |  | PH | 1169 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1145 |
| 32 | Barcelona International Airport |  | ES | 1118 |
| 33 | Viracopos International Airport |  | BR | 1078 |
| 34 | Seattle-Tacoma International Airport |  | US | 1077 |
| 35 | Reno/Tahoe International Airport |  | US | 1074 |
| 36 | Calgary International Airport |  | CA | 1063 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1049 |
| 39 | Tenerife Norte Airport |  | ES | 1027 |
| 40 | Vitoria/Foronda Airport |  | ES | 1016 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 948 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 438 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 315 | 27m | 275 km | 1,492.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 304 | 14m | 114 km | 596.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 281 | 44m | 241 km | 1,167.2 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 276 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 268 | 1h 49m | 1,423 km | 6,577.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 229 | 1h 15m | 961 km | 3,795.8 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 225 | 1h 38m | 1,156 km | 4,488.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 221 | 24m | 218 km | 832.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 206 | 28m | 152 km | 538.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N328KT |  | Bend Municipal Airport (KBDN) | Corvallis Municipal Airport (KCVO) | 2026-08-11 16:56 UTC | 2026-08-11 17:50 UTC | 53m |
| WAYLN53 | WAY | California City Municipal Airport (KL71) | Boron Airstrip (57CL) | 2026-08-11 17:32 UTC | 2026-08-11 17:43 UTC | 10m |
| N95RZ |  | OI78 (OI78) | Aerodrome Les Noyers Airport (50OH) | 2026-08-11 17:25 UTC | 2026-08-11 17:42 UTC | 16m |
| BLZR278 | BLZ | Kingsville Nas Airport (KNQI) | Seven C's Ranch Airport (0XA4) | 2026-08-11 17:16 UTC | 2026-08-11 17:38 UTC | 22m |
| N626LM |  | Sussex Airport (KFWN) | Sussex Airport (KFWN) | 2026-08-11 17:18 UTC | 2026-08-11 17:38 UTC | 20m |
| MSR786 | EgyptAir | Frankfurt am Main International Airport (EDDF) | HE12 (HE12) | 2026-08-11 14:15 UTC | 2026-08-11 17:35 UTC | 3h 20m |
| OMART | Oman Air | M. R. Stefanik Airport (LZIB) | LZRY (LZRY) | 2026-08-11 16:34 UTC | 2026-08-11 17:34 UTC | 1h 0m |
| N113UV |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-08-11 16:42 UTC | 2026-08-11 17:28 UTC | 45m |
| N253FD |  | Monmouth Executive Airport (KBLM) | Monmouth Executive Airport (KBLM) | 2026-08-11 15:50 UTC | 2026-08-11 17:28 UTC | 1h 37m |
| BNOB | BNO | Bodø Airport (ENBO) | Svolvær Helle Airport (ENSH) | 2026-08-11 17:09 UTC | 2026-08-11 17:27 UTC | 18m |
| SPR700 | SPR | Charlo Airport (CYCL) | Buctouche Airport (CDT5) | 2026-08-11 16:59 UTC | 2026-08-11 17:25 UTC | 25m |
| PAT180 | PAT | Dallas-Fort Worth International Airport (KDFW) | Austin-Bergstrom International Airport (KAUS) | 2026-08-11 16:38 UTC | 2026-08-11 17:24 UTC | 46m |
| N228JJ |  | Toledo Executive Airport (KTDZ) | Eugene F Kranz Toledo Express Airport (KTOL) | 2026-08-11 16:51 UTC | 2026-08-11 17:23 UTC | 31m |
| RTY705 | RTY | Cheyenne Regional/Jerry Olson Field (KCYS) | Kimball Municipal/Robert E Arraj Field (KIBM) | 2026-08-11 16:56 UTC | 2026-08-11 17:22 UTC | 25m |
| C2701 |  | Mc Clellan Airfield (KMCC) | Truckee-Tahoe Airport (KTRK) | 2026-08-11 16:04 UTC | 2026-08-11 17:20 UTC | 1h 16m |
| N980MR |  | Harry Stern Airport (KBWP) | Milan-Bogard Skyport Airport (MU38) | 2026-08-11 16:01 UTC | 2026-08-11 17:19 UTC | 1h 17m |
| N784LA |  | Flying W Airport (KN14) | Flying W Airport (KN14) | 2026-08-11 17:03 UTC | 2026-08-11 17:18 UTC | 15m |
| N8454H |  | Old Bridge Airport (K3N6) | Monmouth Executive Airport (KBLM) | 2026-08-11 16:53 UTC | 2026-08-11 17:17 UTC | 24m |
| JRT59 | JRT | Mc Ghee Tyson Airport (KTYS) | Austin-Bergstrom International Airport (KAUS) | 2026-08-11 15:15 UTC | 2026-08-11 17:15 UTC | 2h 0m |
| N662JM |  | Scottsdale Airport (KSDL) | Aztec Municipal Airport (KN19) | 2026-08-11 16:24 UTC | 2026-08-11 17:09 UTC | 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
