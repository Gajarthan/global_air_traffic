# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_15:38:18_UTC-green)

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

**Latest saved flight:** 2026-08-17 15:38:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 15:38:18 UTC

- **208,651** saved flights
- **66,391** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **208,651** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,509,314.8 tonnes** estimated CO2 emissions
- **145,467,522 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8263 |
| 2 | SkyWest Airlines | 7481 |
| 3 | EJA | 4057 |
| 4 | IndiGo | 3568 |
| 5 | American Airlines | 3468 |
| 6 | Southwest Airlines | 3352 |
| 7 | Delta Air Lines | 2678 |
| 8 | ENY | 2595 |
| 9 | LATAM Airlines | 1969 |
| 10 | AZU | 1888 |
| 11 | Lufthansa | 1761 |
| 12 | Vueling | 1736 |
| 13 | WIF | 1680 |
| 14 | LXJ | 1647 |
| 15 | easyJet | 1445 |
| 16 | Swiss International | 1391 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1312 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1276 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1147 |
| 24 | GLO | 1127 |
| 25 | Air France | 1120 |
| 26 | PGT | 1119 |
| 27 | JetBlue | 1066 |
| 28 | AEE | 1064 |
| 29 | WMT | 1054 |
| 30 | Wizz Air | 1034 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 176670 |
| 2 | 🇪🇸 ES | 13357 |
| 3 | 🇧🇷 BR | 11970 |
| 4 | 🇦🇺 AU | 11745 |
| 5 | 🇨🇦 CA | 11506 |
| 6 | 🇮🇳 IN | 11132 |
| 7 | 🇮🇹 IT | 10912 |
| 8 | 🇩🇪 DE | 10319 |
| 9 | 🇬🇧 GB | 9752 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8299 |
| 12 | 🇫🇷 FR | 8280 |
| 13 | 🇬🇷 GR | 6147 |
| 14 | 🇹🇷 TR | 5938 |
| 15 | 🇲🇽 MX | 5857 |
| 16 | 🇨🇭 CH | 5557 |
| 17 | 🇳🇴 NO | 5206 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3508 |
| 20 | 🇵🇱 PL | 3450 |
| 21 | 🇹🇭 TH | 3350 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2773 |
| 24 | 🇬🇹 GT | 2683 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2240 |
| 27 | 🇲🇦 MA | 2104 |
| 28 | 🇳🇱 NL | 1862 |
| 29 | 🇲🇪 ME | 1771 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4376 |
| 2 | Denver International Airport |  | US | 3398 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2531 |
| 5 | Guaymaral Airport |  | CO | 2506 |
| 6 | Harry Reid International Airport |  | US | 2350 |
| 7 | Zurich Airport |  | CH | 2173 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2173 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2156 |
| 10 | La Aurora Airport |  | GT | 2041 |
| 11 | Chicago O'Hare International Airport |  | US | 1933 |
| 12 | El Dorado International Airport |  | CO | 1904 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1858 |
| 14 | Salt Lake City International Airport |  | US | 1844 |
| 15 | Congonhas Airport |  | BR | 1741 |
| 16 | Frankfurt am Main International Airport |  | DE | 1717 |
| 17 | Madrid Barajas International Airport |  | ES | 1638 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1584 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1579 |
| 20 | Capua Airport |  | IT | 1576 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1520 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1467 |
| 24 | Malpensa International Airport |  | IT | 1447 |
| 25 | Charles de Gaulle International Airport |  | FR | 1433 |
| 26 | Charlotte/Douglas International Airport |  | US | 1416 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1314 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1288 |
| 30 | Bengaluru International Airport |  | IN | 1287 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1262 |
| 32 | Barcelona International Airport |  | ES | 1251 |
| 33 | Seattle-Tacoma International Airport |  | US | 1239 |
| 34 | Viracopos International Airport |  | BR | 1211 |
| 35 | Calgary International Airport |  | CA | 1179 |
| 36 | Oslo Gardermoen Airport |  | NO | 1156 |
| 37 | Vitoria/Foronda Airport |  | ES | 1149 |
| 38 | Reno/Tahoe International Airport |  | US | 1144 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1124 |
| 40 | Don Mueang International Airport |  | TH | 1112 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1030 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 475 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 407 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 349 | 27m | 275 km | 1,653.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 345 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 305 | 44m | 241 km | 1,266.9 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 304 | 1h 49m | 1,423 km | 7,460.6 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 288 | 22m | 55 km | 273.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 261 | 19m | 99 km | 447.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 255 | 27m | 215 km | 944.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 239 | 19m | 144 km | 594.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 224 | 1h 49m | 1,304 km | 5,039.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N623HA |  | Nobuzzn Airport (8TN5) | Springfield Robertson County Airport (KM91) | 2026-08-17 15:26 UTC | 2026-08-17 15:38 UTC | 12m |
| N356ND |  | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-08-17 14:44 UTC | 2026-08-17 15:35 UTC | 51m |
| PAT837 | PAT | KU42 (KU42) | Telluride Regional Airport (KTEX) | 2026-08-17 14:32 UTC | 2026-08-17 15:34 UTC | 1h 1m |
| N26GP |  | Fayetteville Regional/Grannis Field (KFAY) | Wayne Executive Jetport Airport (KGWW) | 2026-08-17 12:19 UTC | 2026-08-17 15:33 UTC | 3h 14m |
| N199FF |  | Aurora Municipal Airport (KARR) | Chicago Midway International Airport (KMDW) | 2026-08-17 15:09 UTC | 2026-08-17 15:32 UTC | 23m |
| JCY252 | JCY | Renton Municipal Airport (KRNT) | Coeur D'Alene Airport (KCOE) | 2026-08-17 14:52 UTC | 2026-08-17 15:30 UTC | 37m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-08-17 14:58 UTC | 2026-08-17 15:29 UTC | 31m |
| N62PN |  | Rogers Executive - Carter Field (KROG) | Conway Regional Airport (KCXW) | 2026-08-17 15:10 UTC | 2026-08-17 15:28 UTC | 18m |
| AFL2143 | AFL | Antalya International Airport (LTAI) | Sheremetyevo International Airport (UUEE) | 2026-08-17 11:20 UTC | 2026-08-17 15:22 UTC | 4h 2m |
| N10607 |  | Laurel Municipal Airport (K6S8) | Laurel Municipal Airport (K6S8) | 2026-08-17 15:12 UTC | 2026-08-17 15:16 UTC | 4m |
| TOM9LG | TOM | Dionysios Solomos Airport (LGZA) | London Gatwick Airport (EGKK) | 2026-08-17 11:50 UTC | 2026-08-17 15:15 UTC | 3h 25m |
| N673MA |  | Lewis University Airport (KLOT) | K1C2 (K1C2) | 2026-08-17 14:36 UTC | 2026-08-17 15:14 UTC | 37m |
| TGJAC | TGJ | Rancho Guadalupe South Airport (MM51) | Ciudad Acuna New International Airport (MMCC) | 2026-08-17 14:40 UTC | 2026-08-17 15:12 UTC | 32m |
| MIG1 | MIG | Eglin Afb/Destin-Ft Walton Beach Airport (KVPS) | Bird Nest Airport (4MS5) | 2026-08-17 14:59 UTC | 2026-08-17 15:11 UTC | 12m |
| N625PL |  | Hammond Northshore Regional Airport (KHDC) | LA30 (LA30) | 2026-08-17 13:11 UTC | 2026-08-17 15:11 UTC | 1h 59m |
| N104PF |  | Lewis University Airport (KLOT) | K1C2 (K1C2) | 2026-08-17 14:32 UTC | 2026-08-17 15:11 UTC | 38m |
| N723AG |  | Oakland County International Airport (KPTK) | Saginaw County/H W Browne Airport (KHYX) | 2026-08-17 14:47 UTC | 2026-08-17 15:11 UTC | 23m |
| SMASH73 | SMA | Jones Farm Field (OK12) | Ksa Orchards Airport (OK11) | 2026-08-17 14:48 UTC | 2026-08-17 15:10 UTC | 21m |
| N99981 |  | Midway Lake Airport (79FD) | Lakeland Linder International Airport (KLAL) | 2026-08-17 14:39 UTC | 2026-08-17 15:09 UTC | 30m |
| N46CK |  | Tyler Pounds Regional Airport (KTYR) | Skypark Estates Owners Assoc Airport (18FD) | 2026-08-17 13:43 UTC | 2026-08-17 15:09 UTC | 1h 25m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
