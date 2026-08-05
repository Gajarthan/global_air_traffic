# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_20:29:36_UTC-green)

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

**Latest saved flight:** 2026-08-05 20:29:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 20:29:36 UTC

- **173,095** saved flights
- **56,164** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **173,095** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,085,580.1 tonnes** estimated CO2 emissions
- **120,903,193 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6876 |
| 2 | SkyWest Airlines | 6332 |
| 3 | EJA | 3442 |
| 4 | IndiGo | 3031 |
| 5 | Southwest Airlines | 2729 |
| 6 | American Airlines | 2724 |
| 7 | ENY | 2153 |
| 8 | Delta Air Lines | 2054 |
| 9 | LATAM Airlines | 1599 |
| 10 | Lufthansa | 1574 |
| 11 | AZU | 1527 |
| 12 | WIF | 1448 |
| 13 | Vueling | 1427 |
| 14 | LXJ | 1355 |
| 15 | AXM | 1184 |
| 16 | Swiss International | 1178 |
| 17 | easyJet | 1173 |
| 18 | EJU | 1056 |
| 19 | QLK | 1055 |
| 20 | Alaska Airlines | 1053 |
| 21 | All Nippon Airways | 1045 |
| 22 | VIV | 950 |
| 23 | Cathay Pacific | 934 |
| 24 | CXK | 923 |
| 25 | GLO | 909 |
| 26 | United Airlines | 903 |
| 27 | AEE | 902 |
| 28 | Air France | 888 |
| 29 | MXY | 878 |
| 30 | JetBlue | 864 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 149195 |
| 2 | 🇪🇸 ES | 11084 |
| 3 | 🇧🇷 BR | 9847 |
| 4 | 🇦🇺 AU | 9645 |
| 5 | 🇮🇳 IN | 9507 |
| 6 | 🇨🇦 CA | 9486 |
| 7 | 🇮🇹 IT | 8941 |
| 8 | 🇩🇪 DE | 8583 |
| 9 | 🇬🇧 GB | 8017 |
| 10 | 🇯🇵 JP | 6937 |
| 11 | 🇫🇷 FR | 6862 |
| 12 | 🇨🇴 CO | 6369 |
| 13 | 🇬🇷 GR | 5029 |
| 14 | 🇲🇽 MX | 4954 |
| 15 | 🇨🇭 CH | 4563 |
| 16 | 🇳🇴 NO | 4506 |
| 17 | 🇹🇷 TR | 4246 |
| 18 | 🇲🇾 MY | 3081 |
| 19 | 🇵🇱 PL | 2892 |
| 20 | 🇿🇦 ZA | 2782 |
| 21 | 🇹🇭 TH | 2532 |
| 22 | 🇳🇿 NZ | 2498 |
| 23 | 🇵🇭 PH | 2280 |
| 24 | 🇬🇹 GT | 2213 |
| 25 | 🇰🇷 KR | 2170 |
| 26 | 🇲🇦 MA | 1740 |
| 27 | 🇭🇷 HR | 1671 |
| 28 | 🇲🇪 ME | 1583 |
| 29 | 🇳🇱 NL | 1562 |
| 30 | 🇲🇴 MO | 1493 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3573 |
| 2 | Denver International Airport |  | US | 2862 |
| 3 | Tokyo International Airport |  | JP | 2171 |
| 4 | Guaymaral Airport |  | CO | 2161 |
| 5 | Indira Gandhi International Airport |  | IN | 2118 |
| 6 | Harry Reid International Airport |  | US | 2073 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1882 |
| 8 | Zurich Airport |  | CH | 1831 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1818 |
| 10 | La Aurora Airport |  | GT | 1707 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1598 |
| 12 | El Dorado International Airport |  | CO | 1570 |
| 13 | Chicago O'Hare International Airport |  | US | 1567 |
| 14 | Salt Lake City International Airport |  | US | 1554 |
| 15 | Frankfurt am Main International Airport |  | DE | 1536 |
| 16 | Macau International Airport |  | MO | 1493 |
| 17 | Congonhas Airport |  | BR | 1423 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1414 |
| 19 | Capua Airport |  | IT | 1351 |
| 20 | Madrid Barajas International Airport |  | ES | 1349 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1301 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1216 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1204 |
| 24 | Charlotte/Douglas International Airport |  | US | 1196 |
| 25 | Charles de Gaulle International Airport |  | FR | 1174 |
| 26 | Malpensa International Airport |  | IT | 1172 |
| 27 | Kuala Lumpur International Airport |  | MY | 1162 |
| 28 | Bengaluru International Airport |  | IN | 1128 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1074 |
| 30 | Ninoy Aquino International Airport |  | PH | 1074 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1066 |
| 32 | Barcelona International Airport |  | ES | 1024 |
| 33 | Daniel K Inouye International Airport |  | US | 999 |
| 34 | Seattle-Tacoma International Airport |  | US | 998 |
| 35 | Viracopos International Airport |  | BR | 984 |
| 36 | Calgary International Airport |  | CA | 982 |
| 37 | Reno/Tahoe International Airport |  | US | 980 |
| 38 | Oslo Gardermoen Airport |  | NO | 963 |
| 39 | Tenerife Norte Airport |  | ES | 960 |
| 40 | Scottsdale Airport |  | US | 944 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 894 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 631 | 21m | 244 km | 2,657.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 409 | 24m | 225 km | 1,586.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 392 | 1h 8m | 770 km | 5,207.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 319 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 293 | 27m | 275 km | 1,388.4 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 260 | 44m | 241 km | 1,080.0 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 259 | 22m | 55 km | 246.2 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 238 | 1h 48m | 1,423 km | 5,840.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 224 | 20m | 250 km | 967.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 221 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 208 | 50m | 556 km | 1,993.9 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 205 | 19m | 144 km | 509.9 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 200 | 1h 38m | 1,156 km | 3,989.9 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 200 | 31m | 369 km | 1,273.0 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 28 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 196 | 8m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 193 | 24m | 218 km | 727.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 188 | 1h 1m | 695 km | 2,253.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BRG594 | BRG | Ralph Wien Memorial Airport (PAOT) | Deering Airport (PADE) | 2026-08-05 19:57 UTC | 2026-08-05 20:29 UTC | 31m |
| PNC0619 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-05 19:46 UTC | 2026-08-05 20:22 UTC | 35m |
| MNB280 | MNB | Istanbul Airport (LTFM) | Macau International Airport (VMMC) | 2026-08-05 08:39 UTC | 2026-08-05 20:21 UTC | 11h 41m |
| ROKT11 | ROK | 5MS2 (5MS2) | Dean Griffin Memorial Airport (KM24) | 2026-08-05 20:11 UTC | 2026-08-05 20:19 UTC | 7m |
| N953PT |  | General Mitchell International Airport (KMKE) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-05 19:14 UTC | 2026-08-05 20:18 UTC | 1h 3m |
| MADHAT | MAD | Charleston Executive Airport (KJZI) | Raven's Run Airport (SC65) | 2026-08-05 19:43 UTC | 2026-08-05 20:12 UTC | 28m |
| N265JC |  | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-05 20:02 UTC | 2026-08-05 20:07 UTC | 5m |
| N303HC |  | Gaines County Airport (KGNC) | Central Colorado Regional Airport (KAEJ) | 2026-08-05 18:51 UTC | 2026-08-05 20:06 UTC | 1h 14m |
| MNS551 | MNS | Eleftherios Venizelos International Airport (LGAV) | Mitiga Airport (HLLM) | 2026-08-05 18:22 UTC | 2026-08-05 20:03 UTC | 1h 40m |
| N668PD |  | Los Alamitos Army Air Field (KSLI) | Los Alamitos Army Air Field (KSLI) | 2026-08-05 19:01 UTC | 2026-08-05 20:01 UTC | 1h 0m |
| LRS6718 | LRS | Tobias Bolanos International Airport (MRPV) | Guapiles Airport (MRGP) | 2026-08-05 19:50 UTC | 2026-08-05 20:00 UTC | 10m |
| N812KC |  | Addison Airport (KADS) | Smiley Johnson Municipal/Bass Field (KE34) | 2026-08-05 19:21 UTC | 2026-08-05 19:59 UTC | 38m |
| C6034 |  | Ralph Wien Memorial Airport (PAOT) | Ralph Wien Memorial Airport (PAOT) | 2026-08-05 17:40 UTC | 2026-08-05 19:58 UTC | 2h 18m |
| N74KM |  | Dallas Love Field (KDAL) | Telluride Regional Airport (KTEX) | 2026-08-05 17:59 UTC | 2026-08-05 19:58 UTC | 1h 58m |
| GFD50 | GFD | Boise Air Trml/Gowen Field (KBOI) | Hell Roaring Ranch Airport (ID39) | 2026-08-05 18:38 UTC | 2026-08-05 19:56 UTC | 1h 17m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-08-05 05:50 UTC | 2026-08-05 19:55 UTC | 14h 5m |
| N2454E |  | Grand Prairie Municipal Airport (KGPM) | Mid-Way Regional Airport (KJWY) | 2026-08-05 19:40 UTC | 2026-08-05 19:55 UTC | 14m |
| BOX746 | BOX | Kep Air Base (VVKP) | Zhuhai Airport (ZGSD) | 2026-08-05 18:58 UTC | 2026-08-05 19:52 UTC | 54m |
| RYR62MD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Ifrane Airport (GMFI) | 2026-08-05 17:39 UTC | 2026-08-05 19:52 UTC | 2h 12m |
| TIBBI | TIB | Tobias Bolanos International Airport (MRPV) | Atirro Airport (MRAR) | 2026-08-05 19:34 UTC | 2026-08-05 19:51 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
