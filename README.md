# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_19:04:49_UTC-green)

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

**Latest saved flight:** 2026-08-07 19:04:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-07 19:04:49 UTC

- **176,289** saved flights
- **56,869** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **176,289** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,119,850.6 tonnes** estimated CO2 emissions
- **122,889,888 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6990 |
| 2 | SkyWest Airlines | 6429 |
| 3 | EJA | 3480 |
| 4 | IndiGo | 3092 |
| 5 | Southwest Airlines | 2775 |
| 6 | American Airlines | 2752 |
| 7 | ENY | 2193 |
| 8 | Delta Air Lines | 2081 |
| 9 | LATAM Airlines | 1630 |
| 10 | Lufthansa | 1584 |
| 11 | AZU | 1565 |
| 12 | WIF | 1480 |
| 13 | Vueling | 1455 |
| 14 | LXJ | 1386 |
| 15 | Swiss International | 1204 |
| 16 | AXM | 1196 |
| 17 | easyJet | 1194 |
| 18 | QLK | 1082 |
| 19 | EJU | 1081 |
| 20 | All Nippon Airways | 1069 |
| 21 | Alaska Airlines | 1067 |
| 22 | VIV | 968 |
| 23 | Cathay Pacific | 944 |
| 24 | CXK | 936 |
| 25 | GLO | 926 |
| 26 | AEE | 919 |
| 27 | Air France | 911 |
| 28 | United Airlines | 910 |
| 29 | MXY | 888 |
| 30 | JetBlue | 872 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 151516 |
| 2 | 🇪🇸 ES | 11301 |
| 3 | 🇧🇷 BR | 10036 |
| 4 | 🇦🇺 AU | 9951 |
| 5 | 🇮🇳 IN | 9690 |
| 6 | 🇨🇦 CA | 9641 |
| 7 | 🇮🇹 IT | 9111 |
| 8 | 🇩🇪 DE | 8737 |
| 9 | 🇬🇧 GB | 8156 |
| 10 | 🇯🇵 JP | 7076 |
| 11 | 🇫🇷 FR | 7014 |
| 12 | 🇨🇴 CO | 6474 |
| 13 | 🇬🇷 GR | 5136 |
| 14 | 🇲🇽 MX | 5034 |
| 15 | 🇨🇭 CH | 4680 |
| 16 | 🇳🇴 NO | 4599 |
| 17 | 🇹🇷 TR | 4375 |
| 18 | 🇲🇾 MY | 3120 |
| 19 | 🇵🇱 PL | 2934 |
| 20 | 🇿🇦 ZA | 2878 |
| 21 | 🇹🇭 TH | 2623 |
| 22 | 🇳🇿 NZ | 2555 |
| 23 | 🇵🇭 PH | 2326 |
| 24 | 🇬🇹 GT | 2246 |
| 25 | 🇰🇷 KR | 2203 |
| 26 | 🇲🇦 MA | 1782 |
| 27 | 🇭🇷 HR | 1727 |
| 28 | 🇲🇪 ME | 1606 |
| 29 | 🇳🇱 NL | 1589 |
| 30 | 🇲🇴 MO | 1507 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3640 |
| 2 | Denver International Airport |  | US | 2905 |
| 3 | Tokyo International Airport |  | JP | 2208 |
| 4 | Guaymaral Airport |  | CO | 2166 |
| 5 | Indira Gandhi International Airport |  | IN | 2154 |
| 6 | Harry Reid International Airport |  | US | 2101 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1910 |
| 8 | Zurich Airport |  | CH | 1874 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1842 |
| 10 | La Aurora Airport |  | GT | 1728 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1615 |
| 12 | Chicago O'Hare International Airport |  | US | 1586 |
| 13 | El Dorado International Airport |  | CO | 1581 |
| 14 | Salt Lake City International Airport |  | US | 1571 |
| 15 | Frankfurt am Main International Airport |  | DE | 1550 |
| 16 | Macau International Airport |  | MO | 1507 |
| 17 | Congonhas Airport |  | BR | 1454 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1424 |
| 19 | Capua Airport |  | IT | 1378 |
| 20 | Madrid Barajas International Airport |  | ES | 1373 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1312 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1239 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1235 |
| 24 | Charlotte/Douglas International Airport |  | US | 1205 |
| 25 | Charles de Gaulle International Airport |  | FR | 1202 |
| 26 | Malpensa International Airport |  | IT | 1201 |
| 27 | Kuala Lumpur International Airport |  | MY | 1175 |
| 28 | Bengaluru International Airport |  | IN | 1152 |
| 29 | Ninoy Aquino International Airport |  | PH | 1094 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1091 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1088 |
| 32 | Barcelona International Airport |  | ES | 1048 |
| 33 | Seattle-Tacoma International Airport |  | US | 1013 |
| 34 | Daniel K Inouye International Airport |  | US | 1012 |
| 35 | Viracopos International Airport |  | BR | 1003 |
| 36 | Reno/Tahoe International Airport |  | US | 1002 |
| 37 | Calgary International Airport |  | CA | 997 |
| 38 | Oslo Gardermoen Airport |  | NO | 984 |
| 39 | Tenerife Norte Airport |  | ES | 970 |
| 40 | Amsterdam Airport Schiphol |  | NL | 955 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 643 | 21m | 244 km | 2,707.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 414 | 24m | 225 km | 1,606.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 411 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 406 | 1h 8m | 770 km | 5,393.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 325 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 296 | 27m | 275 km | 1,402.6 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 244 | 1h 48m | 1,423 km | 5,988.1 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 226 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 217 | 20m | 99 km | 371.7 t |
| 21 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 216 | 8m | - | - |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 212 | 51m | 556 km | 2,032.2 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 210 | 1h 15m | 961 km | 3,480.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 210 | 19m | 144 km | 522.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 205 | 1h 38m | 1,156 km | 4,089.7 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 205 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 203 | 31m | 369 km | 1,292.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 200 | 24m | 218 km | 753.5 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 192 | 1h 2m | 695 km | 2,301.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N968DK |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-08-07 18:52 UTC | 2026-08-07 19:04 UTC | 12m |
| N5618Y |  | Johnson County Airport (KBYG) | Johnson County Airport (KBYG) | 2026-08-07 18:47 UTC | 2026-08-07 18:59 UTC | 12m |
| N978FA |  | Greenwood Lake Airport (K4N1) | Greenwood Lake Airport (K4N1) | 2026-08-07 18:44 UTC | 2026-08-07 18:59 UTC | 14m |
| CXK535 | CXK | Smyrna Airport (KMQY) | Smyrna Airport (KMQY) | 2026-08-07 18:27 UTC | 2026-08-07 18:55 UTC | 27m |
| N864MB |  | Denton Enterprise Airport (KDTO) | Jbj Ranch Airport (XA98) | 2026-08-07 18:27 UTC | 2026-08-07 18:55 UTC | 27m |
| TKR132 | TKR | Albuquerque International Sunport Airport (KABQ) | Santa Fe Regional Airport (KSAF) | 2026-08-07 18:39 UTC | 2026-08-07 18:53 UTC | 13m |
| RAM983 | Royal Air Maroc | Lisbon Portela Airport (LPPT) | Tit Mellil Airport (GMMT) | 2026-08-07 18:02 UTC | 2026-08-07 18:51 UTC | 48m |
| 00000000 |  | Tyler Pounds Regional Airport (KTYR) | Dallas Love Field (KDAL) | 2026-08-07 18:22 UTC | 2026-08-07 18:47 UTC | 24m |
| CFNQN | CFN | Radisson Airport (CJL9) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-08-07 17:54 UTC | 2026-08-07 18:46 UTC | 51m |
| PERRIS2 | PER | Perris Valley Airport (KL65) | Perris Valley Airport (KL65) | 2026-08-07 18:27 UTC | 2026-08-07 18:45 UTC | 17m |
| N172EL |  | Palo Alto Airport (KPAO) | Buchanan Field (KCCR) | 2026-08-07 18:05 UTC | 2026-08-07 18:43 UTC | 38m |
| N15CT |  | Grand Haven Memorial Airpark (K3GM) | Grand Haven Memorial Airpark (K3GM) | 2026-08-07 18:23 UTC | 2026-08-07 18:38 UTC | 14m |
| N24BQ |  | Dupage Airport (KDPA) | Willadae Farms Airport (4LL7) | 2026-08-07 18:00 UTC | 2026-08-07 18:38 UTC | 37m |
| MSR760 | EgyptAir | HE12 (HE12) | HE42 (HE42) | 2026-08-07 09:28 UTC | 2026-08-07 18:37 UTC | 9h 9m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-07 18:13 UTC | 2026-08-07 18:35 UTC | 21m |
| WIF1DJ | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-07 18:20 UTC | 2026-08-07 18:34 UTC | 14m |
| N633GE |  | Gaines County Airport (KGNC) | Williams Field (TX99) | 2026-08-07 18:01 UTC | 2026-08-07 18:33 UTC | 31m |
| N135RF |  | Lee Vining Airport (KO24) | Groveland/Yosemite Airport (KE45) | 2026-08-07 18:18 UTC | 2026-08-07 18:29 UTC | 11m |
| N457TS |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-08-07 18:24 UTC | 2026-08-07 18:29 UTC | 5m |
| JUMP17 | JUM | MT88 (MT88) | Carson Field (MT53) | 2026-08-07 18:18 UTC | 2026-08-07 18:28 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
