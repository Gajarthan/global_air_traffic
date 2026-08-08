# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_11:26:58_UTC-green)

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

**Latest saved flight:** 2026-08-08 11:26:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 11:26:58 UTC

- **178,025** saved flights
- **57,221** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,025** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,139,828.6 tonnes** estimated CO2 emissions
- **124,048,037 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7056 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3507 |
| 4 | IndiGo | 3132 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1646 |
| 10 | Lufthansa | 1594 |
| 11 | AZU | 1581 |
| 12 | WIF | 1490 |
| 13 | Vueling | 1467 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1214 |
| 16 | AXM | 1209 |
| 17 | easyJet | 1207 |
| 18 | QLK | 1093 |
| 19 | All Nippon Airways | 1088 |
| 20 | EJU | 1084 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 979 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 943 |
| 25 | GLO | 939 |
| 26 | AEE | 927 |
| 27 | Air France | 918 |
| 28 | United Airlines | 918 |
| 29 | MXY | 896 |
| 30 | PGT | 881 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152744 |
| 2 | 🇪🇸 ES | 11402 |
| 3 | 🇧🇷 BR | 10138 |
| 4 | 🇦🇺 AU | 10066 |
| 5 | 🇮🇳 IN | 9817 |
| 6 | 🇨🇦 CA | 9729 |
| 7 | 🇮🇹 IT | 9206 |
| 8 | 🇩🇪 DE | 8806 |
| 9 | 🇬🇧 GB | 8215 |
| 10 | 🇯🇵 JP | 7223 |
| 11 | 🇫🇷 FR | 7075 |
| 12 | 🇨🇴 CO | 6526 |
| 13 | 🇬🇷 GR | 5194 |
| 14 | 🇲🇽 MX | 5097 |
| 15 | 🇨🇭 CH | 4732 |
| 16 | 🇳🇴 NO | 4628 |
| 17 | 🇹🇷 TR | 4460 |
| 18 | 🇲🇾 MY | 3156 |
| 19 | 🇵🇱 PL | 2966 |
| 20 | 🇿🇦 ZA | 2902 |
| 21 | 🇹🇭 TH | 2690 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2236 |
| 26 | 🇲🇦 MA | 1798 |
| 27 | 🇭🇷 HR | 1760 |
| 28 | 🇲🇪 ME | 1621 |
| 29 | 🇳🇱 NL | 1604 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2949 |
| 3 | Tokyo International Airport |  | JP | 2243 |
| 4 | Indira Gandhi International Airport |  | IN | 2183 |
| 5 | Guaymaral Airport |  | CO | 2177 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1923 |
| 8 | Zurich Airport |  | CH | 1890 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1591 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1556 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1471 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1394 |
| 20 | Madrid Barajas International Airport |  | ES | 1389 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1255 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1220 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1209 |
| 27 | Kuala Lumpur International Airport |  | MY | 1189 |
| 28 | Bengaluru International Airport |  | IN | 1169 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1103 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1057 |
| 33 | Daniel K Inouye International Airport |  | US | 1025 |
| 34 | Seattle-Tacoma International Airport |  | US | 1025 |
| 35 | Viracopos International Airport |  | BR | 1016 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 992 |
| 39 | Tenerife Norte Airport |  | ES | 975 |
| 40 | Amsterdam Airport Schiphol |  | NL | 963 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 655 | 21m | 244 km | 2,758.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 419 | 1h 8m | 770 km | 5,566.1 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 299 | 27m | 275 km | 1,416.8 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 248 | 1h 48m | 1,423 km | 6,086.3 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 226 | 26m | 215 km | 837.0 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 212 | 19m | 144 km | 527.3 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 203 | 24m | 218 km | 764.8 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N75200 |  | Pompano Beach Airpark (KPMP) | Palm Beach County Park Airport (KLNA) | 2026-08-08 10:52 UTC | 2026-08-08 11:26 UTC | 34m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 11:12 UTC | 2026-08-08 11:24 UTC | 11m |
| WIF7JE | WIF | Oslo Gardermoen Airport (ENGM) | Bringeland Airport (ENBL) | 2026-08-08 10:19 UTC | 2026-08-08 11:17 UTC | 58m |
| HBZWE | HBZ | Courchevel Airport (LFLJ) | Bex Airport (LSGB) | 2026-08-08 10:51 UTC | 2026-08-08 11:17 UTC | 25m |
| DKKCN | DKK | Lauf-Lillinghof Airport (EDQI) | Lauf-Lillinghof Airport (EDQI) | 2026-08-08 11:04 UTC | 2026-08-08 11:11 UTC | 6m |
|  |  | Debrecen International Airport (LHDC) | Debrecen International Airport (LHDC) | 2026-08-08 11:06 UTC | 2026-08-08 11:07 UTC | 1m |
| RYR582Z | Ryanair | Helsinki Vantaa Airport (EFHK) | Rojunai Airport (EYRO) | 2026-08-08 10:10 UTC | 2026-08-08 11:01 UTC | 50m |
| WOODVALE | WOO | RAF Woodvale (EGOW) | RAF Woodvale (EGOW) | 2026-08-08 10:52 UTC | 2026-08-08 10:55 UTC | 2m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-08-08 10:31 UTC | 2026-08-08 10:51 UTC | 19m |
| WZZ5107 | Wizz Air | Swidnik Lotnisko Airport (EPSW) | Otocac Airport (LDRO) | 2026-08-08 09:35 UTC | 2026-08-08 10:47 UTC | 1h 12m |
| EIN9CX | Aer Lingus | Denver International Airport (KDEN) | Dublin Airport (EIDW) | 2026-08-08 02:53 UTC | 2026-08-08 10:47 UTC | 7h 54m |
| EWG2XZ | EWG | Stockholm-Arlanda Airport (ESSA) | Stuttgart Airport (EDDS) | 2026-08-08 08:47 UTC | 2026-08-08 10:45 UTC | 1h 57m |
| ANE61HB | ANE | Madrid Barajas International Airport (LEMD) | Jayena Airport (LE84) | 2026-08-08 10:12 UTC | 2026-08-08 10:45 UTC | 32m |
| VLZ75X | VLZ | Farnborough Airport (EGLF) | Nice-Cote d'Azur Airport (LFMN) | 2026-08-08 09:13 UTC | 2026-08-08 10:43 UTC | 1h 29m |
| WIF51N | WIF | Bergen Airport Flesland (ENBR) | Leknes Airport (ENLK) | 2026-08-08 08:32 UTC | 2026-08-08 10:43 UTC | 2h 10m |
| IGO7642 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-08-08 10:14 UTC | 2026-08-08 10:42 UTC | 27m |
| SFR693 | SFR | Cape Town International Airport (FACT) | Rand Airport (FAGM) | 2026-08-08 09:04 UTC | 2026-08-08 10:41 UTC | 1h 36m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Chania International Airport (LGSA) | 2026-08-08 10:14 UTC | 2026-08-08 10:40 UTC | 25m |
| BEL1KZ | Brussels Airlines | Brussels Airport (EBBR) | Otocac Airport (LDRO) | 2026-08-08 09:22 UTC | 2026-08-08 10:40 UTC | 1h 18m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 10:28 UTC | 2026-08-08 10:39 UTC | 11m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
