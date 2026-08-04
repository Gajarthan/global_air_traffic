# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_22:18:38_UTC-green)

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

**Latest saved flight:** 2026-08-04 22:18:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-04 22:18:38 UTC

- **171,354** saved flights
- **55,765** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **171,354** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,065,400.1 tonnes** estimated CO2 emissions
- **119,733,341 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6826 |
| 2 | SkyWest Airlines | 6273 |
| 3 | EJA | 3407 |
| 4 | IndiGo | 3005 |
| 5 | Southwest Airlines | 2704 |
| 6 | American Airlines | 2694 |
| 7 | ENY | 2134 |
| 8 | Delta Air Lines | 2036 |
| 9 | LATAM Airlines | 1585 |
| 10 | Lufthansa | 1564 |
| 11 | AZU | 1509 |
| 12 | WIF | 1433 |
| 13 | Vueling | 1407 |
| 14 | LXJ | 1342 |
| 15 | AXM | 1176 |
| 16 | Swiss International | 1167 |
| 17 | easyJet | 1155 |
| 18 | EJU | 1048 |
| 19 | Alaska Airlines | 1046 |
| 20 | QLK | 1043 |
| 21 | All Nippon Airways | 1036 |
| 22 | VIV | 944 |
| 23 | Cathay Pacific | 922 |
| 24 | CXK | 913 |
| 25 | United Airlines | 901 |
| 26 | GLO | 899 |
| 27 | AEE | 893 |
| 28 | Air France | 880 |
| 29 | MXY | 871 |
| 30 | JetBlue | 858 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 147786 |
| 2 | 🇪🇸 ES | 10980 |
| 3 | 🇧🇷 BR | 9743 |
| 4 | 🇦🇺 AU | 9527 |
| 5 | 🇮🇳 IN | 9414 |
| 6 | 🇨🇦 CA | 9361 |
| 7 | 🇮🇹 IT | 8865 |
| 8 | 🇩🇪 DE | 8508 |
| 9 | 🇬🇧 GB | 7943 |
| 10 | 🇯🇵 JP | 6872 |
| 11 | 🇫🇷 FR | 6793 |
| 12 | 🇨🇴 CO | 6250 |
| 13 | 🇬🇷 GR | 4978 |
| 14 | 🇲🇽 MX | 4906 |
| 15 | 🇨🇭 CH | 4499 |
| 16 | 🇳🇴 NO | 4469 |
| 17 | 🇹🇷 TR | 4183 |
| 18 | 🇲🇾 MY | 3057 |
| 19 | 🇵🇱 PL | 2876 |
| 20 | 🇿🇦 ZA | 2770 |
| 21 | 🇹🇭 TH | 2486 |
| 22 | 🇳🇿 NZ | 2475 |
| 23 | 🇵🇭 PH | 2257 |
| 24 | 🇬🇹 GT | 2200 |
| 25 | 🇰🇷 KR | 2161 |
| 26 | 🇲🇦 MA | 1726 |
| 27 | 🇭🇷 HR | 1650 |
| 28 | 🇲🇪 ME | 1574 |
| 29 | 🇳🇱 NL | 1555 |
| 30 | 🇲🇴 MO | 1468 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3527 |
| 2 | Denver International Airport |  | US | 2840 |
| 3 | Tokyo International Airport |  | JP | 2156 |
| 4 | Guaymaral Airport |  | CO | 2124 |
| 5 | Indira Gandhi International Airport |  | IN | 2088 |
| 6 | Harry Reid International Airport |  | US | 2056 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1868 |
| 8 | Zurich Airport |  | CH | 1809 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1803 |
| 10 | La Aurora Airport |  | GT | 1698 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1580 |
| 12 | Chicago O'Hare International Airport |  | US | 1557 |
| 13 | El Dorado International Airport |  | CO | 1556 |
| 14 | Salt Lake City International Airport |  | US | 1536 |
| 15 | Frankfurt am Main International Airport |  | DE | 1528 |
| 16 | Macau International Airport |  | MO | 1468 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1405 |
| 18 | Congonhas Airport |  | BR | 1403 |
| 19 | Madrid Barajas International Airport |  | ES | 1342 |
| 20 | Capua Airport |  | IT | 1336 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1293 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1209 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1193 |
| 24 | Charlotte/Douglas International Airport |  | US | 1189 |
| 25 | Charles de Gaulle International Airport |  | FR | 1163 |
| 26 | Malpensa International Airport |  | IT | 1155 |
| 27 | Kuala Lumpur International Airport |  | MY | 1151 |
| 28 | Bengaluru International Airport |  | IN | 1120 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1065 |
| 30 | Ninoy Aquino International Airport |  | PH | 1062 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1055 |
| 32 | Barcelona International Airport |  | ES | 1014 |
| 33 | Daniel K Inouye International Airport |  | US | 993 |
| 34 | Seattle-Tacoma International Airport |  | US | 990 |
| 35 | Viracopos International Airport |  | BR | 975 |
| 36 | Calgary International Airport |  | CA | 970 |
| 37 | Reno/Tahoe International Airport |  | US | 966 |
| 38 | Oslo Gardermoen Airport |  | NO | 954 |
| 39 | Tenerife Norte Airport |  | ES | 952 |
| 40 | Scottsdale Airport |  | US | 941 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 880 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 626 | 21m | 244 km | 2,635.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 405 | 24m | 225 km | 1,571.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 405 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 387 | 1h 8m | 770 km | 5,141.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 318 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 292 | 27m | 275 km | 1,383.7 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 256 | 44m | 241 km | 1,063.4 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 255 | 22m | 55 km | 242.4 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 235 | 1h 47m | 1,423 km | 5,767.3 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 222 | 26m | 215 km | 822.2 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 218 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 211 | 20m | 99 km | 361.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 205 | 50m | 556 km | 1,965.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 204 | 1h 15m | 961 km | 3,381.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 201 | 12m | - | - |
| 25 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 197 | 31m | 369 km | 1,254.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 194 | 1h 38m | 1,156 km | 3,870.2 t |
| 28 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 189 | 8m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 188 | 24m | 218 km | 708.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 186 | 1h 1m | 695 km | 2,229.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
|  |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-04 20:22 UTC | 2026-08-04 22:18 UTC | 1h 55m |
| GEC8450 | GEC | Frankfurt am Main International Airport (EDDF) | Macau International Airport (VMMC) | 2026-08-04 11:31 UTC | 2026-08-04 22:18 UTC | 10h 47m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-08-04 15:10 UTC | 2026-08-04 22:16 UTC | 7h 6m |
| JUPITER | JUP | El Dorado International Airport (SKBO) | Velasquez Airport (SKVL) | 2026-08-04 21:38 UTC | 2026-08-04 22:16 UTC | 38m |
| YGA | YGA | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-08-04 21:51 UTC | 2026-08-04 22:12 UTC | 20m |
| CPA234 | Cathay Pacific | Malpensa International Airport (LIMC) | Macau International Airport (VMMC) | 2026-08-04 11:38 UTC | 2026-08-04 22:11 UTC | 10h 33m |
|  |  | Calaveras County/Maury Rasmussen Field (KCPU) | Calaveras County/Maury Rasmussen Field (KCPU) | 2026-08-04 21:56 UTC | 2026-08-04 22:04 UTC | 8m |
| CPA395 | Cathay Pacific | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-08-04 19:25 UTC | 2026-08-04 22:01 UTC | 2h 36m |
| N969YC |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-04 21:26 UTC | 2026-08-04 22:01 UTC | 34m |
| N854AL |  | KFTG (KFTG) | Metrogro Farm Airport (CO25) | 2026-08-04 21:47 UTC | 2026-08-04 21:58 UTC | 11m |
| N249ND |  | Boire Field (KASH) | Dillant/Hopkins Airport (KEEN) | 2026-08-04 21:39 UTC | 2026-08-04 21:57 UTC | 18m |
| TKR183 | TKR | Coeur D'Alene Airport (KCOE) | WA70 (WA70) | 2026-08-04 21:35 UTC | 2026-08-04 21:55 UTC | 20m |
| N229LA |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Bob Hope Airport (KBUR) | 2026-08-04 20:19 UTC | 2026-08-04 21:54 UTC | 1h 35m |
| TKR169 | TKR | Coeur D'Alene Airport (KCOE) | WA70 (WA70) | 2026-08-04 21:33 UTC | 2026-08-04 21:53 UTC | 19m |
| N63PC |  | Long Beach (Daugherty Field) Airport (KLGB) | Robin Airport (59AZ) | 2026-08-04 20:57 UTC | 2026-08-04 21:52 UTC | 55m |
| TKR102 | TKR | Coeur D'Alene Airport (KCOE) | WA70 (WA70) | 2026-08-04 21:34 UTC | 2026-08-04 21:51 UTC | 17m |
| ROUGH81 | ROU | TX09 (TX09) | Richie Rich Airport (8TE1) | 2026-08-04 21:19 UTC | 2026-08-04 21:51 UTC | 31m |
| N388WT |  | Glover Airport (XS70) | Wendover Airport (KENV) | 2026-08-04 18:07 UTC | 2026-08-04 21:51 UTC | 3h 43m |
| CNS719 | CNS | Portsmouth International At Pease Airport (KPSM) | Lancaster Airport (KLNS) | 2026-08-04 20:47 UTC | 2026-08-04 21:50 UTC | 1h 2m |
| N904CF |  | Casper/Natrona County International Airport (KCPR) | Northern Colorado Regional Airport (KFNL) | 2026-08-04 20:26 UTC | 2026-08-04 21:49 UTC | 1h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
