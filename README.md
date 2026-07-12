# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_14:01:42_UTC-green)

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

**Latest saved flight:** 2026-07-12 14:01:42 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-12 14:01:42 UTC

- **138,686** saved flights
- **46,723** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **138,686** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,666,490.2 tonnes** estimated CO2 emissions
- **96,608,129 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5657 |
| 2 | SkyWest Airlines | 5076 |
| 3 | EJA | 2714 |
| 4 | IndiGo | 2556 |
| 5 | American Airlines | 2186 |
| 6 | Southwest Airlines | 2088 |
| 7 | ENY | 1736 |
| 8 | Delta Air Lines | 1646 |
| 9 | Lufthansa | 1416 |
| 10 | LATAM Airlines | 1276 |
| 11 | Vueling | 1199 |
| 12 | WIF | 1195 |
| 13 | AZU | 1189 |
| 14 | LXJ | 1061 |
| 15 | AXM | 1041 |
| 16 | Swiss International | 987 |
| 17 | easyJet | 901 |
| 18 | All Nippon Airways | 892 |
| 19 | Alaska Airlines | 874 |
| 20 | QLK | 865 |
| 21 | EJU | 858 |
| 22 | VIV | 761 |
| 23 | AEE | 747 |
| 24 | Air France | 744 |
| 25 | CXK | 743 |
| 26 | United Airlines | 729 |
| 27 | Cathay Pacific | 727 |
| 28 | JetBlue | 727 |
| 29 | MXY | 722 |
| 30 | GLO | 709 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 118972 |
| 2 | 🇪🇸 ES | 9122 |
| 3 | 🇮🇳 IN | 8011 |
| 4 | 🇦🇺 AU | 7924 |
| 5 | 🇧🇷 BR | 7818 |
| 6 | 🇨🇦 CA | 7286 |
| 7 | 🇮🇹 IT | 7258 |
| 8 | 🇩🇪 DE | 7249 |
| 9 | 🇬🇧 GB | 6302 |
| 10 | 🇯🇵 JP | 5844 |
| 11 | 🇫🇷 FR | 5540 |
| 12 | 🇨🇴 CO | 4385 |
| 13 | 🇲🇽 MX | 4015 |
| 14 | 🇬🇷 GR | 3957 |
| 15 | 🇳🇴 NO | 3740 |
| 16 | 🇨🇭 CH | 3605 |
| 17 | 🇹🇷 TR | 3252 |
| 18 | 🇲🇾 MY | 2702 |
| 19 | 🇵🇱 PL | 2330 |
| 20 | 🇿🇦 ZA | 2278 |
| 21 | 🇳🇿 NZ | 2134 |
| 22 | 🇹🇭 TH | 2105 |
| 23 | 🇰🇷 KR | 2005 |
| 24 | 🇵🇭 PH | 1891 |
| 25 | 🇬🇹 GT | 1841 |
| 26 | 🇲🇦 MA | 1462 |
| 27 | 🇲🇪 ME | 1380 |
| 28 | 🇳🇱 NL | 1301 |
| 29 | 🇭🇷 HR | 1258 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2871 |
| 2 | Denver International Airport |  | US | 2321 |
| 3 | Tokyo International Airport |  | JP | 1900 |
| 4 | Indira Gandhi International Airport |  | IN | 1770 |
| 5 | Harry Reid International Airport |  | US | 1729 |
| 6 | Guaymaral Airport |  | CO | 1690 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1604 |
| 8 | Zurich Airport |  | CH | 1544 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1458 |
| 10 | La Aurora Airport |  | GT | 1422 |
| 11 | Frankfurt am Main International Airport |  | DE | 1369 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1326 |
| 13 | Chicago O'Hare International Airport |  | US | 1306 |
| 14 | El Dorado International Airport |  | CO | 1233 |
| 15 | Salt Lake City International Airport |  | US | 1229 |
| 16 | Macau International Airport |  | MO | 1188 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1187 |
| 18 | Capua Airport |  | IT | 1143 |
| 19 | Madrid Barajas International Airport |  | ES | 1129 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1118 |
| 21 | Congonhas Airport |  | BR | 1115 |
| 22 | Kuala Lumpur International Airport |  | MY | 1048 |
| 23 | Charlotte/Douglas International Airport |  | US | 1014 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 999 |
| 25 | Charles de Gaulle International Airport |  | FR | 987 |
| 26 | Bengaluru International Airport |  | IN | 960 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 957 |
| 28 | Malpensa International Airport |  | IT | 904 |
| 29 | Ninoy Aquino International Airport |  | PH | 880 |
| 30 | Daniel K Inouye International Airport |  | US | 852 |
| 31 | Barcelona International Airport |  | ES | 845 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 843 |
| 33 | Tenerife Norte Airport |  | ES | 813 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 811 |
| 35 | Calgary International Airport |  | CA | 802 |
| 36 | Viracopos International Airport |  | BR | 792 |
| 37 | Scottsdale Airport |  | US | 791 |
| 38 | Seattle-Tacoma International Airport |  | US | 789 |
| 39 | Amsterdam Airport Schiphol |  | NL | 779 |
| 40 | Vitoria/Foronda Airport |  | ES | 776 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 712 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 502 | 21m | 244 km | 2,113.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 341 | 24m | 225 km | 1,322.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 340 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 253 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 189 | 26m | 215 km | 700.0 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 183 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 167 | 18m | 144 km | 415.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 161 | 1h 16m | 961 km | 2,668.7 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 160 | 1h 1m | 695 km | 1,917.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 157 | 1h 38m | 1,156 km | 3,132.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 155 | 14m | 154 km | 410.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 152 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HKW842 | HKW | Mason County Airport (KLDM) | Frankfort Dow Memorial Field (KFKS) | 2026-07-12 13:38 UTC | 2026-07-12 14:01 UTC | 23m |
| CXK403 | CXK | Spirit Of St Louis Airport (KSUS) | KMO6 (KMO6) | 2026-07-12 13:34 UTC | 2026-07-12 14:00 UTC | 26m |
| N115GK |  | Martha's Vineyard Airport (KMVY) | Laguardia Airport (KLGA) | 2026-07-12 12:53 UTC | 2026-07-12 14:00 UTC | 1h 6m |
| HKW221 | HKW | Mason County Airport (KLDM) | Frankfort Dow Memorial Field (KFKS) | 2026-07-12 13:34 UTC | 2026-07-12 13:59 UTC | 25m |
| N36HF |  | Newark Liberty International Airport (KEWR) | KHTO (KHTO) | 2026-07-12 13:20 UTC | 2026-07-12 13:58 UTC | 38m |
| RYR2AD | Ryanair | Kaunas International Airport (EYKA) | Khrabrovo Airport (UMKK) | 2026-07-12 13:19 UTC | 2026-07-12 13:52 UTC | 33m |
| N139TJ |  | Reading Regional/Carl A Spaatz Field (KRDG) | Wings Field (KLOM) | 2026-07-12 13:33 UTC | 2026-07-12 13:51 UTC | 17m |
| OM1010 |  | Sisteron - Theze Airport (LFNS) | Aosta Airport (LIMW) | 2026-07-12 10:51 UTC | 2026-07-12 13:48 UTC | 2h 57m |
| JIA5074 | JIA | Eppley Airfield (KOMA) | Philadelphia International Airport (KPHL) | 2026-07-12 11:19 UTC | 2026-07-12 13:47 UTC | 2h 27m |
| N5309J |  | Ellison Airport (35IN) | Crawfordsville Regional Airport (KCFJ) | 2026-07-12 13:00 UTC | 2026-07-12 13:45 UTC | 45m |
| N999GX |  | Morgan County Airport (K42U) | Flying R Airport (11UT) | 2026-07-12 13:35 UTC | 2026-07-12 13:43 UTC | 8m |
| N13NS |  | Skypark Airport (KBTF) | Logan-Cache Airport (KLGU) | 2026-07-12 13:08 UTC | 2026-07-12 13:42 UTC | 34m |
| N8352T |  | Rocky Mountain Metro Airport (KBJC) | Vance Brand Airport (KLMO) | 2026-07-12 13:27 UTC | 2026-07-12 13:40 UTC | 13m |
| N707DJ |  | North Perry Airport (KHWO) | North Perry Airport (KHWO) | 2026-07-12 12:18 UTC | 2026-07-12 13:38 UTC | 1h 20m |
| N562JL |  | Richmond International Airport (KRIC) | Norfolk International Airport (KORF) | 2026-07-12 13:17 UTC | 2026-07-12 13:38 UTC | 21m |
| N75138 |  | Quast Airport (MN62) | Hutchinson Municipal/Butler Field (KHCD) | 2026-07-12 13:20 UTC | 2026-07-12 13:37 UTC | 17m |
| CXK279 | CXK | Northeast Philadelphia Airport (KPNE) | Northeast Philadelphia Airport (KPNE) | 2026-07-12 13:09 UTC | 2026-07-12 13:35 UTC | 26m |
| N2448H |  | New Garden Airport (KN57) | New Castle Airport (KILG) | 2026-07-12 13:20 UTC | 2026-07-12 13:33 UTC | 13m |
| N652CR |  | Leesburg Executive Airport (KJYO) | Ocean City Municipal Airport (KOXB) | 2026-07-12 12:47 UTC | 2026-07-12 13:32 UTC | 45m |
| FGIBV | FGI | Chambery-Challes-les-Eaux Airport (LFLE) | Chambery-Savoie Airport (LFLB) | 2026-07-12 12:08 UTC | 2026-07-12 13:32 UTC | 1h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
