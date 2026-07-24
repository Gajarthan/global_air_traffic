# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_18:37:26_UTC-green)

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

**Latest saved flight:** 2026-07-24 18:37:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 18:37:26 UTC

- **148,435** saved flights
- **49,539** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **148,435** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,774,885.4 tonnes** estimated CO2 emissions
- **102,891,907 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5992 |
| 2 | SkyWest Airlines | 5426 |
| 3 | EJA | 2934 |
| 4 | IndiGo | 2665 |
| 5 | American Airlines | 2359 |
| 6 | Southwest Airlines | 2245 |
| 7 | ENY | 1849 |
| 8 | Delta Air Lines | 1751 |
| 9 | Lufthansa | 1454 |
| 10 | LATAM Airlines | 1366 |
| 11 | AZU | 1284 |
| 12 | WIF | 1265 |
| 13 | Vueling | 1256 |
| 14 | LXJ | 1144 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1050 |
| 17 | easyJet | 955 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 929 |
| 20 | QLK | 922 |
| 21 | EJU | 906 |
| 22 | VIV | 820 |
| 23 | CXK | 794 |
| 24 | AEE | 779 |
| 25 | Air France | 779 |
| 26 | JetBlue | 777 |
| 27 | Cathay Pacific | 773 |
| 28 | MXY | 772 |
| 29 | GLO | 770 |
| 30 | United Airlines | 768 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 128054 |
| 2 | 🇪🇸 ES | 9585 |
| 3 | 🇦🇺 AU | 8459 |
| 4 | 🇧🇷 BR | 8387 |
| 5 | 🇮🇳 IN | 8367 |
| 6 | 🇨🇦 CA | 7939 |
| 7 | 🇮🇹 IT | 7679 |
| 8 | 🇩🇪 DE | 7610 |
| 9 | 🇬🇧 GB | 6786 |
| 10 | 🇯🇵 JP | 6154 |
| 11 | 🇫🇷 FR | 5894 |
| 12 | 🇨🇴 CO | 4972 |
| 13 | 🇲🇽 MX | 4299 |
| 14 | 🇬🇷 GR | 4202 |
| 15 | 🇳🇴 NO | 3968 |
| 16 | 🇨🇭 CH | 3897 |
| 17 | 🇹🇷 TR | 3485 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2502 |
| 20 | 🇿🇦 ZA | 2404 |
| 21 | 🇳🇿 NZ | 2243 |
| 22 | 🇹🇭 TH | 2167 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1977 |
| 25 | 🇬🇹 GT | 1927 |
| 26 | 🇲🇦 MA | 1518 |
| 27 | 🇲🇪 ME | 1467 |
| 28 | 🇳🇱 NL | 1379 |
| 29 | 🇭🇷 HR | 1348 |
| 30 | 🇲🇴 MO | 1236 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3054 |
| 2 | Denver International Airport |  | US | 2481 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Indira Gandhi International Airport |  | IN | 1858 |
| 5 | Guaymaral Airport |  | CO | 1852 |
| 6 | Harry Reid International Airport |  | US | 1841 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1667 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1563 |
| 10 | La Aurora Airport |  | GT | 1493 |
| 11 | Frankfurt am Main International Airport |  | DE | 1404 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1395 |
| 13 | Chicago O'Hare International Airport |  | US | 1373 |
| 14 | Salt Lake City International Airport |  | US | 1334 |
| 15 | El Dorado International Airport |  | CO | 1331 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1277 |
| 17 | Macau International Airport |  | MO | 1236 |
| 18 | Congonhas Airport |  | BR | 1198 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1177 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1157 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1066 |
| 24 | Charlotte/Douglas International Airport |  | US | 1058 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1043 |
| 26 | Charles de Gaulle International Airport |  | FR | 1027 |
| 27 | Bengaluru International Airport |  | IN | 1000 |
| 28 | Malpensa International Airport |  | IT | 960 |
| 29 | Ninoy Aquino International Airport |  | PH | 926 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 903 |
| 31 | Barcelona International Airport |  | ES | 895 |
| 32 | Daniel K Inouye International Airport |  | US | 891 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 886 |
| 34 | Seattle-Tacoma International Airport |  | US | 850 |
| 35 | Tenerife Norte Airport |  | ES | 848 |
| 36 | Calgary International Airport |  | CA | 848 |
| 37 | Scottsdale Airport |  | US | 841 |
| 38 | Viracopos International Airport |  | BR | 839 |
| 39 | Amsterdam Airport Schiphol |  | NL | 829 |
| 40 | Oslo Gardermoen Airport |  | NO | 822 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 782 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 538 | 21m | 244 km | 2,265.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 359 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 269 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 265 | 27m | 275 km | 1,255.7 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 202 | 44m | 241 km | 839.1 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 199 | 1h 46m | 1,423 km | 4,883.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 195 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 194 | 20m | 99 km | 332.3 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 182 | 20m | 250 km | 786.1 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 182 | 27m | 152 km | 475.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 175 | 31m | 369 km | 1,113.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 174 | 1h 16m | 961 km | 2,884.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 167 | 1h 39m | 1,156 km | 3,331.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9737V |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-24 17:53 UTC | 2026-07-24 18:37 UTC | 44m |
| N285VN |  | Franklin Regional Airport (KFKN) | Hampton Roads Executive Airport (KPVG) | 2026-07-24 17:39 UTC | 2026-07-24 18:32 UTC | 52m |
| N9666V |  | Carson City Airport (KCXP) | Lake Tahoe Airport (KTVL) | 2026-07-24 18:19 UTC | 2026-07-24 18:31 UTC | 12m |
| N999VP |  | 2LL1 (2LL1) | Walnut Creek Airport (49IL) | 2026-07-24 18:19 UTC | 2026-07-24 18:30 UTC | 10m |
| N1408B |  | Redding Regional Airport (KRDD) | Red Bluff Municipal Airport (KRBL) | 2026-07-24 17:59 UTC | 2026-07-24 18:26 UTC | 27m |
| OHFMZ | OHF | Lahti Vesivehmaa Airport (EFLA) | Lahti Vesivehmaa Airport (EFLA) | 2026-07-24 17:06 UTC | 2026-07-24 18:24 UTC | 1h 18m |
| N36HF |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-07-24 17:56 UTC | 2026-07-24 18:23 UTC | 26m |
| N384ND |  | Woodford Airpark (20VA) | Shannon Airport (KEZF) | 2026-07-24 18:18 UTC | 2026-07-24 18:22 UTC | 3m |
| N9995L |  | Santa Fe Regional Airport (KSAF) | Santa Fe Regional Airport (KSAF) | 2026-07-24 18:07 UTC | 2026-07-24 18:21 UTC | 13m |
| AIC4305 | Air India | Indira Gandhi International Airport (VIDP) | Buraimi Airport (OOBR) | 2026-07-24 15:32 UTC | 2026-07-24 18:20 UTC | 2h 47m |
| N584CC |  | NJ58 (NJ58) | NJ58 (NJ58) | 2026-07-24 18:17 UTC | 2026-07-24 18:20 UTC | 2m |
| JUMP5 | JUM | Eloy Municipal Airport (KE60) | Eloy Municipal Airport (KE60) | 2026-07-24 17:42 UTC | 2026-07-24 18:19 UTC | 37m |
| N532LW |  | Mc Clellan-Palomar Airport (KCRQ) | Lake Tahoe Airport (KTVL) | 2026-07-24 17:13 UTC | 2026-07-24 18:18 UTC | 1h 4m |
| DRACO81 | DRA | 4OK5 (4OK5) | Ramsak Airport (OK67) | 2026-07-24 17:52 UTC | 2026-07-24 18:17 UTC | 25m |
| N661SF |  | Aurora Municipal Airport (KARR) | Ruder Airport (59IL) | 2026-07-24 18:06 UTC | 2026-07-24 18:16 UTC | 10m |
| N48EF |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-07-24 18:00 UTC | 2026-07-24 18:15 UTC | 15m |
| N292VF |  | Brady-Pippin Airport (SN20) | Colonel James Jabara Airport (KAAO) | 2026-07-24 18:09 UTC | 2026-07-24 18:14 UTC | 5m |
| N65KD |  | Mc Minnville Municipal Airport (KMMV) | Portland-Hillsboro Airport (KHIO) | 2026-07-24 17:09 UTC | 2026-07-24 18:13 UTC | 1h 4m |
| CAP408 | CAP | Redding Regional Airport (KRDD) | Scott Valley Airport (KA30) | 2026-07-24 17:47 UTC | 2026-07-24 18:12 UTC | 25m |
| LOST77 | LOS | Los Alamitos Army Air Field (KSLI) | Sedona Airport (KSEZ) | 2026-07-24 16:48 UTC | 2026-07-24 18:12 UTC | 1h 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
