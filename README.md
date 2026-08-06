# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_11:13:51_UTC-green)

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

**Latest saved flight:** 2026-08-06 11:13:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-06 11:13:51 UTC

- **173,911** saved flights
- **56,338** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,911** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,094,878.0 tonnes** estimated CO2 emissions
- **121,442,202 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6897 |
| 2 | SkyWest Airlines | 6370 |
| 3 | EJA | 3451 |
| 4 | IndiGo | 3043 |
| 5 | Southwest Airlines | 2742 |
| 6 | American Airlines | 2732 |
| 7 | ENY | 2166 |
| 8 | Delta Air Lines | 2062 |
| 9 | LATAM Airlines | 1606 |
| 10 | Lufthansa | 1575 |
| 11 | AZU | 1537 |
| 12 | WIF | 1454 |
| 13 | Vueling | 1431 |
| 14 | LXJ | 1362 |
| 15 | AXM | 1190 |
| 16 | Swiss International | 1183 |
| 17 | easyJet | 1181 |
| 18 | QLK | 1063 |
| 19 | EJU | 1062 |
| 20 | Alaska Airlines | 1058 |
| 21 | All Nippon Airways | 1056 |
| 22 | VIV | 956 |
| 23 | Cathay Pacific | 940 |
| 24 | CXK | 924 |
| 25 | GLO | 915 |
| 26 | AEE | 907 |
| 27 | United Airlines | 904 |
| 28 | Air France | 893 |
| 29 | MXY | 880 |
| 30 | JetBlue | 868 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149812 |
| 2 | 🇪🇸 ES | 11124 |
| 3 | 🇧🇷 BR | 9894 |
| 4 | 🇦🇺 AU | 9763 |
| 5 | 🇮🇳 IN | 9548 |
| 6 | 🇨🇦 CA | 9522 |
| 7 | 🇮🇹 IT | 8973 |
| 8 | 🇩🇪 DE | 8611 |
| 9 | 🇬🇧 GB | 8047 |
| 10 | 🇯🇵 JP | 6990 |
| 11 | 🇫🇷 FR | 6897 |
| 12 | 🇨🇴 CO | 6403 |
| 13 | 🇬🇷 GR | 5045 |
| 14 | 🇲🇽 MX | 4976 |
| 15 | 🇨🇭 CH | 4585 |
| 16 | 🇳🇴 NO | 4524 |
| 17 | 🇹🇷 TR | 4265 |
| 18 | 🇲🇾 MY | 3090 |
| 19 | 🇵🇱 PL | 2906 |
| 20 | 🇿🇦 ZA | 2796 |
| 21 | 🇹🇭 TH | 2553 |
| 22 | 🇳🇿 NZ | 2523 |
| 23 | 🇵🇭 PH | 2296 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2180 |
| 26 | 🇲🇦 MA | 1748 |
| 27 | 🇭🇷 HR | 1680 |
| 28 | 🇲🇪 ME | 1593 |
| 29 | 🇳🇱 NL | 1566 |
| 30 | 🇲🇴 MO | 1503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3595 |
| 2 | Denver International Airport |  | US | 2882 |
| 3 | Tokyo International Airport |  | JP | 2184 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2125 |
| 6 | Harry Reid International Airport |  | US | 2082 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1886 |
| 8 | Zurich Airport |  | CH | 1839 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1824 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1602 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1572 |
| 14 | Salt Lake City International Airport |  | US | 1562 |
| 15 | Frankfurt am Main International Airport |  | DE | 1537 |
| 16 | Macau International Airport |  | MO | 1503 |
| 17 | Congonhas Airport |  | BR | 1432 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1420 |
| 19 | Capua Airport |  | IT | 1355 |
| 20 | Madrid Barajas International Airport |  | ES | 1354 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1305 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1223 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1215 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Charles de Gaulle International Airport |  | FR | 1181 |
| 26 | Malpensa International Airport |  | IT | 1178 |
| 27 | Kuala Lumpur International Airport |  | MY | 1165 |
| 28 | Bengaluru International Airport |  | IN | 1132 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1080 |
| 30 | Ninoy Aquino International Airport |  | PH | 1080 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1072 |
| 32 | Barcelona International Airport |  | ES | 1026 |
| 33 | Daniel K Inouye International Airport |  | US | 1003 |
| 34 | Seattle-Tacoma International Airport |  | US | 1003 |
| 35 | Calgary International Airport |  | CA | 989 |
| 36 | Reno/Tahoe International Airport |  | US | 987 |
| 37 | Viracopos International Airport |  | BR | 986 |
| 38 | Oslo Gardermoen Airport |  | NO | 966 |
| 39 | Tenerife Norte Airport |  | ES | 962 |
| 40 | Scottsdale Airport |  | US | 946 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 635 | 21m | 244 km | 2,673.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 410 | 24m | 225 km | 1,590.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 394 | 1h 8m | 770 km | 5,234.0 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 321 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 239 | 1h 48m | 1,423 km | 5,865.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 222 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 206 | 19m | 144 km | 512.4 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 201 | 1h 38m | 1,156 km | 4,009.9 t |
| 27 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 200 | 8m | - | - |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 189 | 43m | 452 km | 1,473.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N3300D |  | Crisp County-Cordele Airport (KCKF) | Sylvester Airport (KSYV) | 2026-08-06 10:42 UTC | 2026-08-06 11:13 UTC | 31m |
| AWH91B | AWH | Munster Osnabruck Airport (EDDG) | Stuttgart Airport (EDDS) | 2026-08-06 10:09 UTC | 2026-08-06 11:12 UTC | 1h 3m |
| QTR69X | Qatar Airways | Hamad International Airport (OTHH) | Bezymyanka Airfield (UWWG) | 2026-08-06 06:37 UTC | 2026-08-06 11:10 UTC | 4h 32m |
| HYD164 | HYD | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Rouyn-Noranda Airport (CYUY) | 2026-08-06 10:11 UTC | 2026-08-06 11:00 UTC | 48m |
| MRA603 | MRA | 92MI (92MI) | Twin Lakes Airport (MI55) | 2026-08-06 10:43 UTC | 2026-08-06 10:59 UTC | 15m |
| RSQ116 | RSQ | Powerscourt Airfield (EIPT) | Dublin Airport (EIDW) | 2026-08-06 10:45 UTC | 2026-08-06 10:56 UTC | 10m |
| BPO260 | BPO | Elsenthal Grafe Airport (EDNF) | Elsenthal Grafe Airport (EDNF) | 2026-08-06 10:43 UTC | 2026-08-06 10:53 UTC | 9m |
| ZEH | ZEH | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-08-06 10:21 UTC | 2026-08-06 10:49 UTC | 28m |
| CU22 |  | Gimhae International Airport (RKPK) | G 710 Airport (RK6D) | 2026-08-06 10:29 UTC | 2026-08-06 10:48 UTC | 18m |
| BNO93J | BNO | Haugesund Airport (ENHD) | Kristiansand Airport (ENCN) | 2026-08-06 10:21 UTC | 2026-08-06 10:47 UTC | 25m |
| DHK238 | DHK | Leipzig Halle Airport (EDDP) | Macau International Airport (VMMC) | 2026-08-06 00:07 UTC | 2026-08-06 10:46 UTC | 10h 39m |
| LBQ870 | LBQ | Roanoke/Blacksburg Regional (Woodrum Field) Airport (KROA) | Washington Manassas/Harry P Davis Field (KHEF) | 2026-08-06 10:06 UTC | 2026-08-06 10:42 UTC | 36m |
| AM341 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-08-06 10:21 UTC | 2026-08-06 10:42 UTC | 21m |
| VOE4ER | VOE | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-06 10:00 UTC | 2026-08-06 10:41 UTC | 41m |
| AOJ69Y | AOJ | Verona / Villafranca Airport (LIPX) | Graz Airport (LOWG) | 2026-08-06 10:06 UTC | 2026-08-06 10:40 UTC | 34m |
| ZSSFT | ZSS | Wonderboom Airport (FAWB) | Thabazimbi Airport (FATI) | 2026-08-06 09:53 UTC | 2026-08-06 10:39 UTC | 46m |
| LYBRI | LYB | Paluknys Airport (EYVP) | Paluknys Airport (EYVP) | 2026-08-06 10:19 UTC | 2026-08-06 10:35 UTC | 16m |
| HBYAK | HBY | St Stephan Airport (LSTS) | St Stephan Airport (LSTS) | 2026-08-06 10:30 UTC | 2026-08-06 10:34 UTC | 3m |
| THY6802 | Turkish Airlines | Balikesir Korfez Airport (LTFD) | Balikesir Korfez Airport (LTFD) | 2026-08-06 09:47 UTC | 2026-08-06 10:33 UTC | 45m |
| JST531 | JST | Sydney Kingsford Smith International Airport (YSSY) | Melbourne International Airport (YMML) | 2026-08-06 09:07 UTC | 2026-08-06 10:28 UTC | 1h 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
