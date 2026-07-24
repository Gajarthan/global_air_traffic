# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_22:17:51_UTC-green)

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

**Latest saved flight:** 2026-07-24 22:17:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 22:17:51 UTC

- **149,000** saved flights
- **49,698** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **149,000** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,781,759.7 tonnes** estimated CO2 emissions
- **103,290,417 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6012 |
| 2 | SkyWest Airlines | 5455 |
| 3 | EJA | 2955 |
| 4 | IndiGo | 2666 |
| 5 | American Airlines | 2373 |
| 6 | Southwest Airlines | 2256 |
| 7 | ENY | 1854 |
| 8 | Delta Air Lines | 1760 |
| 9 | Lufthansa | 1455 |
| 10 | LATAM Airlines | 1372 |
| 11 | AZU | 1288 |
| 12 | WIF | 1268 |
| 13 | Vueling | 1258 |
| 14 | LXJ | 1153 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1052 |
| 17 | easyJet | 962 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 932 |
| 20 | QLK | 922 |
| 21 | EJU | 909 |
| 22 | VIV | 822 |
| 23 | CXK | 799 |
| 24 | AEE | 780 |
| 25 | Air France | 779 |
| 26 | JetBlue | 779 |
| 27 | Cathay Pacific | 777 |
| 28 | MXY | 775 |
| 29 | GLO | 772 |
| 30 | United Airlines | 771 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 128715 |
| 2 | 🇪🇸 ES | 9613 |
| 3 | 🇦🇺 AU | 8461 |
| 4 | 🇧🇷 BR | 8412 |
| 5 | 🇮🇳 IN | 8373 |
| 6 | 🇨🇦 CA | 7993 |
| 7 | 🇮🇹 IT | 7701 |
| 8 | 🇩🇪 DE | 7614 |
| 9 | 🇬🇧 GB | 6808 |
| 10 | 🇯🇵 JP | 6154 |
| 11 | 🇫🇷 FR | 5904 |
| 12 | 🇨🇴 CO | 5024 |
| 13 | 🇲🇽 MX | 4317 |
| 14 | 🇬🇷 GR | 4210 |
| 15 | 🇳🇴 NO | 3974 |
| 16 | 🇨🇭 CH | 3899 |
| 17 | 🇹🇷 TR | 3500 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2509 |
| 20 | 🇿🇦 ZA | 2406 |
| 21 | 🇳🇿 NZ | 2249 |
| 22 | 🇹🇭 TH | 2167 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1979 |
| 25 | 🇬🇹 GT | 1944 |
| 26 | 🇲🇦 MA | 1522 |
| 27 | 🇲🇪 ME | 1470 |
| 28 | 🇳🇱 NL | 1380 |
| 29 | 🇭🇷 HR | 1352 |
| 30 | 🇲🇴 MO | 1238 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3065 |
| 2 | Denver International Airport |  | US | 2501 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Guaymaral Airport |  | CO | 1866 |
| 5 | Indira Gandhi International Airport |  | IN | 1860 |
| 6 | Harry Reid International Airport |  | US | 1849 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1669 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1571 |
| 10 | La Aurora Airport |  | GT | 1506 |
| 11 | Frankfurt am Main International Airport |  | DE | 1404 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1401 |
| 13 | Chicago O'Hare International Airport |  | US | 1382 |
| 14 | Salt Lake City International Airport |  | US | 1342 |
| 15 | El Dorado International Airport |  | CO | 1341 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1281 |
| 17 | Macau International Airport |  | MO | 1238 |
| 18 | Congonhas Airport |  | BR | 1202 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1182 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1158 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1066 |
| 24 | Charlotte/Douglas International Airport |  | US | 1062 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1047 |
| 26 | Charles de Gaulle International Airport |  | FR | 1029 |
| 27 | Bengaluru International Airport |  | IN | 1001 |
| 28 | Malpensa International Airport |  | IT | 963 |
| 29 | Ninoy Aquino International Airport |  | PH | 927 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 907 |
| 31 | Barcelona International Airport |  | ES | 898 |
| 32 | Daniel K Inouye International Airport |  | US | 894 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 893 |
| 34 | Seattle-Tacoma International Airport |  | US | 853 |
| 35 | Tenerife Norte Airport |  | ES | 851 |
| 36 | Calgary International Airport |  | CA | 851 |
| 37 | Scottsdale Airport |  | US | 847 |
| 38 | Viracopos International Airport |  | BR | 840 |
| 39 | Amsterdam Airport Schiphol |  | NL | 830 |
| 40 | Oslo Gardermoen Airport |  | NO | 824 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 787 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 540 | 21m | 244 km | 2,273.8 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 269 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 266 | 27m | 275 km | 1,260.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 203 | 44m | 241 km | 843.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 199 | 1h 46m | 1,423 km | 4,883.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 196 | 20m | 99 km | 335.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 183 | 20m | 250 km | 790.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 176 | 31m | 369 km | 1,120.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 176 | 1h 16m | 961 km | 2,917.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 175 | 18m | 144 km | 435.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N484JB |  | San Gabriel Valley Airport (KEMT) | Whiteman Airport (KWHP) | 2026-07-24 21:37 UTC | 2026-07-24 22:17 UTC | 40m |
| GEC8466 | GEC | Juhu Aerodrome (VAJJ) | Zhuhai Airport (ZGSD) | 2026-07-24 17:08 UTC | 2026-07-24 22:17 UTC | 5h 9m |
| N777ZA |  | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-07-24 21:18 UTC | 2026-07-24 22:16 UTC | 57m |
| N65KD |  | Harvey's Acres Airport (OR28) | Boeing Field/King County International Airport (KBFI) | 2026-07-24 20:43 UTC | 2026-07-24 22:15 UTC | 1h 31m |
| N31BV |  | True Grit South Airport (CO95) | North Fork Valley Airport (K7V2) | 2026-07-24 21:57 UTC | 2026-07-24 22:13 UTC | 16m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-07-24 10:42 UTC | 2026-07-24 22:11 UTC | 11h 28m |
| N261PJ |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-24 21:31 UTC | 2026-07-24 22:05 UTC | 33m |
| VOID01 | VOI | Danaher Airport (7TX0) | Harrison Field Of Knox City Airport (KF75) | 2026-07-24 21:43 UTC | 2026-07-24 22:04 UTC | 21m |
| N608PT |  | Miami Executive Airport (KTMB) | Miami Executive Airport (KTMB) | 2026-07-24 21:50 UTC | 2026-07-24 22:04 UTC | 13m |
| N245PE |  | Rose Field (2NK3) | Manchester Boston Regional Airport (KMHT) | 2026-07-24 21:30 UTC | 2026-07-24 22:01 UTC | 30m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-24 21:42 UTC | 2026-07-24 21:58 UTC | 15m |
| TWY47 | TWY | Indianapolis International Airport (KIND) | Rocky Mountain Metro Airport (KBJC) | 2026-07-24 19:39 UTC | 2026-07-24 21:57 UTC | 2h 18m |
| CPA698 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-07-24 17:31 UTC | 2026-07-24 21:57 UTC | 4h 25m |
| N347T |  | Auburn Municipal Airport (KS50) | Olympia Regional Airport (KOLM) | 2026-07-24 21:18 UTC | 2026-07-24 21:56 UTC | 37m |
| TKR183 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-07-24 21:45 UTC | 2026-07-24 21:55 UTC | 10m |
| ASY822 | ASY | Kelly Field (KSKF) | Flying Eagle Ranch Airport (65TX) | 2026-07-24 20:59 UTC | 2026-07-24 21:53 UTC | 54m |
| RYR8BY | Ryanair | Barcelona International Airport (LEBL) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-07-24 19:31 UTC | 2026-07-24 21:52 UTC | 2h 20m |
| N440BV |  | Fort Worth Meacham International Airport (KFTW) | 4AR6 (4AR6) | 2026-07-24 21:08 UTC | 2026-07-24 21:50 UTC | 42m |
| N821SS |  | Newark Liberty International Airport (KEWR) | Laguardia Airport (KLGA) | 2026-07-24 20:30 UTC | 2026-07-24 21:46 UTC | 1h 15m |
| LXJ601 | LXJ | Mc Clellan-Palomar Airport (KCRQ) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-24 20:48 UTC | 2026-07-24 21:43 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
