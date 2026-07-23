# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_20:37:56_UTC-green)

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

**Latest saved flight:** 2026-07-23 20:37:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-23 20:37:56 UTC

- **146,529** saved flights
- **49,005** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **146,529** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,754,253.4 tonnes** estimated CO2 emissions
- **101,695,852 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5939 |
| 2 | SkyWest Airlines | 5367 |
| 3 | EJA | 2896 |
| 4 | IndiGo | 2645 |
| 5 | American Airlines | 2336 |
| 6 | Southwest Airlines | 2215 |
| 7 | ENY | 1822 |
| 8 | Delta Air Lines | 1739 |
| 9 | Lufthansa | 1450 |
| 10 | LATAM Airlines | 1348 |
| 11 | AZU | 1260 |
| 12 | WIF | 1245 |
| 13 | Vueling | 1244 |
| 14 | LXJ | 1130 |
| 15 | AXM | 1066 |
| 16 | Swiss International | 1037 |
| 17 | easyJet | 945 |
| 18 | All Nippon Airways | 932 |
| 19 | Alaska Airlines | 916 |
| 20 | QLK | 913 |
| 21 | EJU | 900 |
| 22 | VIV | 815 |
| 23 | CXK | 787 |
| 24 | AEE | 776 |
| 25 | JetBlue | 771 |
| 26 | Air France | 769 |
| 27 | MXY | 765 |
| 28 | United Airlines | 763 |
| 29 | Cathay Pacific | 758 |
| 30 | GLO | 754 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 126375 |
| 2 | 🇪🇸 ES | 9494 |
| 3 | 🇦🇺 AU | 8344 |
| 4 | 🇮🇳 IN | 8283 |
| 5 | 🇧🇷 BR | 8261 |
| 6 | 🇨🇦 CA | 7812 |
| 7 | 🇮🇹 IT | 7614 |
| 8 | 🇩🇪 DE | 7536 |
| 9 | 🇬🇧 GB | 6677 |
| 10 | 🇯🇵 JP | 6098 |
| 11 | 🇫🇷 FR | 5814 |
| 12 | 🇨🇴 CO | 4848 |
| 13 | 🇲🇽 MX | 4263 |
| 14 | 🇬🇷 GR | 4153 |
| 15 | 🇳🇴 NO | 3908 |
| 16 | 🇨🇭 CH | 3817 |
| 17 | 🇹🇷 TR | 3436 |
| 18 | 🇲🇾 MY | 2781 |
| 19 | 🇵🇱 PL | 2467 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2223 |
| 22 | 🇹🇭 TH | 2141 |
| 23 | 🇰🇷 KR | 2047 |
| 24 | 🇵🇭 PH | 1941 |
| 25 | 🇬🇹 GT | 1904 |
| 26 | 🇲🇦 MA | 1513 |
| 27 | 🇲🇪 ME | 1453 |
| 28 | 🇳🇱 NL | 1362 |
| 29 | 🇭🇷 HR | 1337 |
| 30 | 🇲🇴 MO | 1217 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3021 |
| 2 | Denver International Airport |  | US | 2459 |
| 3 | Tokyo International Airport |  | JP | 1960 |
| 4 | Indira Gandhi International Airport |  | IN | 1839 |
| 5 | Harry Reid International Airport |  | US | 1829 |
| 6 | Guaymaral Airport |  | CO | 1810 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1658 |
| 8 | Zurich Airport |  | CH | 1613 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1539 |
| 10 | La Aurora Airport |  | GT | 1475 |
| 11 | Frankfurt am Main International Airport |  | DE | 1401 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1378 |
| 13 | Chicago O'Hare International Airport |  | US | 1363 |
| 14 | Salt Lake City International Airport |  | US | 1321 |
| 15 | El Dorado International Airport |  | CO | 1313 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1269 |
| 17 | Macau International Airport |  | MO | 1217 |
| 18 | Capua Airport |  | IT | 1190 |
| 19 | Congonhas Airport |  | BR | 1178 |
| 20 | Madrid Barajas International Airport |  | ES | 1169 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1151 |
| 22 | Kuala Lumpur International Airport |  | MY | 1074 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1054 |
| 24 | Charlotte/Douglas International Airport |  | US | 1045 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1022 |
| 26 | Charles de Gaulle International Airport |  | FR | 1013 |
| 27 | Bengaluru International Airport |  | IN | 991 |
| 28 | Malpensa International Airport |  | IT | 945 |
| 29 | Ninoy Aquino International Airport |  | PH | 906 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 894 |
| 31 | Barcelona International Airport |  | ES | 887 |
| 32 | Daniel K Inouye International Airport |  | US | 882 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 878 |
| 34 | Tenerife Norte Airport |  | ES | 842 |
| 35 | Seattle-Tacoma International Airport |  | US | 836 |
| 36 | Calgary International Airport |  | CA | 831 |
| 37 | Scottsdale Airport |  | US | 831 |
| 38 | Viracopos International Airport |  | BR | 830 |
| 39 | Amsterdam Airport Schiphol |  | NL | 822 |
| 40 | Oslo Gardermoen Airport |  | NO | 809 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 763 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 531 | 21m | 244 km | 2,235.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 355 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 352 | 24m | 225 km | 1,365.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 264 | 27m | 275 km | 1,251.0 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 262 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 220 | 22m | 55 km | 209.1 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 197 | 44m | 241 km | 818.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 196 | 1h 46m | 1,423 km | 4,810.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 193 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 170 | 1h 16m | 961 km | 2,817.8 t |
| 25 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 169 | 44m | 452 km | 1,317.1 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 167 | 13m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 166 | 1h 1m | 695 km | 1,989.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N358EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-07-23 17:54 UTC | 2026-07-23 20:37 UTC | 2h 43m |
| N261PJ |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-23 20:11 UTC | 2026-07-23 20:36 UTC | 25m |
| MMA373 | MMA | Suvarnabhumi Airport (VTBS) | Hmawbi Air Base (VYHB) | 2026-07-23 19:42 UTC | 2026-07-23 20:35 UTC | 53m |
| EVA025 | EVA Air | Seattle-Tacoma International Airport (KSEA) | Taiwan Taoyuan International Airport (RCTP) | 2026-07-23 09:14 UTC | 2026-07-23 20:33 UTC | 11h 18m |
| N817FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-07-23 19:29 UTC | 2026-07-23 20:33 UTC | 1h 3m |
| HVN976 | HVN | Indira Gandhi International Airport (VIDP) | Sittwe Airport (VYSW) | 2026-07-23 18:16 UTC | 2026-07-23 20:32 UTC | 2h 15m |
| THY58 | Turkish Airlines | Istanbul Airport (LTFM) | Kyaukpyu Airport (VYKP) | 2026-07-23 13:14 UTC | 2026-07-23 20:32 UTC | 7h 17m |
| EWG19J | EWG | Munich International Airport (EDDM) | Menorca Airport (LEMH) | 2026-07-23 18:36 UTC | 2026-07-23 20:28 UTC | 1h 52m |
| RYR520K | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Palma De Mallorca Airport (LEPA) | 2026-07-23 18:46 UTC | 2026-07-23 20:28 UTC | 1h 41m |
| N742E |  | Cuyahoga County Airport (KCGF) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-23 19:45 UTC | 2026-07-23 20:23 UTC | 38m |
| N74426 |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-07-23 19:52 UTC | 2026-07-23 20:22 UTC | 29m |
| N854FA |  | Hayenga's Cant Find Farms Airport (00IS) | Decatur Airport (KDEC) | 2026-07-23 19:04 UTC | 2026-07-23 20:20 UTC | 1h 16m |
| CAP1820 | CAP | Ennis Aerodrome (2MD4) | Kent Fort Manor Airport (7MD8) | 2026-07-23 19:36 UTC | 2026-07-23 20:19 UTC | 43m |
| N1165W |  | Zamperini Field (KTOA) | Zamperini Field (KTOA) | 2026-07-23 19:43 UTC | 2026-07-23 20:19 UTC | 35m |
| N904RA |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-23 19:46 UTC | 2026-07-23 20:18 UTC | 32m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-23 20:08 UTC | 2026-07-23 20:18 UTC | 10m |
| N54466 |  | Somerset Airport (KSMQ) | Somerset Airport (KSMQ) | 2026-07-23 19:30 UTC | 2026-07-23 20:17 UTC | 47m |
| N2834Q |  | Danbury Municipal Airport (KDXR) | Harford County Airport (K0W3) | 2026-07-23 18:44 UTC | 2026-07-23 20:16 UTC | 1h 32m |
| EXS76SP | EXS | Leeds Bradford Airport (EGNM) | Palma De Mallorca Airport (LEPA) | 2026-07-23 17:47 UTC | 2026-07-23 20:14 UTC | 2h 26m |
| RYR32UX | Ryanair | Francisco de Sá Carneiro Airport (LPPR) | Palma De Mallorca Airport (LEPA) | 2026-07-23 18:39 UTC | 2026-07-23 20:14 UTC | 1h 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
