# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_20:31:59_UTC-green)

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

**Latest saved flight:** 2026-07-03 20:31:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 20:31:59 UTC

- **128,162** saved flights
- **43,710** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **128,162** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,545,913.1 tonnes** estimated CO2 emissions
- **89,618,151 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5202 |
| 2 | SkyWest Airlines | 4747 |
| 3 | EJA | 2516 |
| 4 | IndiGo | 2413 |
| 5 | American Airlines | 1975 |
| 6 | Southwest Airlines | 1926 |
| 7 | ENY | 1608 |
| 8 | Delta Air Lines | 1528 |
| 9 | Lufthansa | 1354 |
| 10 | LATAM Airlines | 1165 |
| 11 | Vueling | 1132 |
| 12 | WIF | 1127 |
| 13 | AZU | 1085 |
| 14 | AXM | 1002 |
| 15 | LXJ | 996 |
| 16 | Swiss International | 889 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 829 |
| 19 | easyJet | 816 |
| 20 | QLK | 803 |
| 21 | EJU | 795 |
| 22 | Cathay Pacific | 708 |
| 23 | VIV | 703 |
| 24 | AEE | 701 |
| 25 | Air France | 699 |
| 26 | CXK | 691 |
| 27 | United Airlines | 682 |
| 28 | MXY | 666 |
| 29 | JetBlue | 656 |
| 30 | GLO | 647 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 109750 |
| 2 | 🇪🇸 ES | 8525 |
| 3 | 🇮🇳 IN | 7560 |
| 4 | 🇦🇺 AU | 7449 |
| 5 | 🇧🇷 BR | 7172 |
| 6 | 🇨🇦 CA | 6754 |
| 7 | 🇩🇪 DE | 6745 |
| 8 | 🇮🇹 IT | 6716 |
| 9 | 🇬🇧 GB | 5667 |
| 10 | 🇯🇵 JP | 5567 |
| 11 | 🇫🇷 FR | 5079 |
| 12 | 🇨🇴 CO | 4070 |
| 13 | 🇲🇽 MX | 3734 |
| 14 | 🇬🇷 GR | 3643 |
| 15 | 🇳🇴 NO | 3501 |
| 16 | 🇨🇭 CH | 3256 |
| 17 | 🇹🇷 TR | 2743 |
| 18 | 🇲🇾 MY | 2597 |
| 19 | 🇿🇦 ZA | 2126 |
| 20 | 🇵🇱 PL | 2093 |
| 21 | 🇳🇿 NZ | 2059 |
| 22 | 🇹🇭 TH | 1990 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1755 |
| 26 | 🇲🇦 MA | 1373 |
| 27 | 🇲🇪 ME | 1268 |
| 28 | 🇳🇱 NL | 1206 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇭🇷 HR | 1108 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2677 |
| 2 | Denver International Airport |  | US | 2171 |
| 3 | Tokyo International Airport |  | JP | 1835 |
| 4 | Indira Gandhi International Airport |  | IN | 1664 |
| 5 | Harry Reid International Airport |  | US | 1599 |
| 6 | Guaymaral Airport |  | CO | 1557 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1519 |
| 8 | Zurich Airport |  | CH | 1407 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1366 |
| 10 | La Aurora Airport |  | GT | 1358 |
| 11 | Frankfurt am Main International Airport |  | DE | 1312 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1249 |
| 13 | Chicago O'Hare International Airport |  | US | 1235 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1139 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1058 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1057 |
| 20 | Madrid Barajas International Airport |  | ES | 1047 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 1007 |
| 23 | Charlotte/Douglas International Airport |  | US | 964 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 932 |
| 26 | Bengaluru International Airport |  | IN | 916 |
| 27 | Malpensa International Airport |  | IT | 872 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 860 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 811 |
| 31 | Barcelona International Airport |  | ES | 796 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 780 |
| 33 | Tenerife Norte Airport |  | ES | 780 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 754 |
| 35 | Calgary International Airport |  | CA | 751 |
| 36 | Seattle-Tacoma International Airport |  | US | 741 |
| 37 | Scottsdale Airport |  | US | 741 |
| 38 | Vitoria/Foronda Airport |  | ES | 739 |
| 39 | Viracopos International Airport |  | BR | 732 |
| 40 | Amsterdam Airport Schiphol |  | NL | 727 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 651 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 465 | 21m | 244 km | 1,958.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 323 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 309 | 1h 10m | 770 km | 4,104.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 244 | 26m | 275 km | 1,156.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 181 | 26m | 215 km | 670.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 179 | 44m | 241 km | 743.5 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 166 | 1h 45m | 1,423 km | 4,073.9 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 158 | 18m | 144 km | 393.0 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 157 | 20m | 250 km | 678.1 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 150 | 1h 1m | 695 km | 1,798.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 148 | 1h 17m | 961 km | 2,453.2 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| QTR875 | Qatar Airways | Nanning Wuxu Airport (ZGNN) | Heho Airport (VYHH) | 2026-07-03 19:15 UTC | 2026-07-03 20:31 UTC | 1h 16m |
| BOX728 | BOX | Leipzig Halle Airport (EDDP) | VYNT (VYNT) | 2026-07-03 07:04 UTC | 2026-07-03 20:31 UTC | 13h 27m |
| UAE9832 | Emirates | Al Maktoum International Airport (OMDW) | Lashio Airport (VYLS) | 2026-07-03 15:22 UTC | 2026-07-03 20:31 UTC | 5h 9m |
| AAL3219 | American Airlines | Seattle-Tacoma International Airport (KSEA) | Philadelphia International Airport (KPHL) | 2026-07-03 15:42 UTC | 2026-07-03 20:29 UTC | 4h 46m |
| AIP9936 | AIP | Salt Lake City International Airport (KSLC) | Evanston-Uinta County Burns Field (KEVW) | 2026-07-03 20:08 UTC | 2026-07-03 20:23 UTC | 15m |
| JBU288 | JetBlue | Los Angeles International Airport (KLAX) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-03 15:18 UTC | 2026-07-03 20:23 UTC | 5h 5m |
| FFT3856 | FFT | Orlando International Airport (KMCO) | Philadelphia International Airport (KPHL) | 2026-07-03 18:22 UTC | 2026-07-03 20:23 UTC | 2h 1m |
| ROU1645 | ROU | Miami International Airport (KMIA) | Toronto Pearson International Airport (CYYZ) | 2026-07-03 17:53 UTC | 2026-07-03 20:21 UTC | 2h 27m |
| AAY1776 | AAY | Gerald R Ford International Airport (KGRR) | Philadelphia International Airport (KPHL) | 2026-07-03 18:55 UTC | 2026-07-03 20:17 UTC | 1h 21m |
| N786FA |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-07-03 19:47 UTC | 2026-07-03 20:16 UTC | 29m |
| N733JW |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-07-03 19:26 UTC | 2026-07-03 20:16 UTC | 49m |
| N169BA |  | TE77 (TE77) | Bb Airpark (TE88) | 2026-07-03 20:06 UTC | 2026-07-03 20:14 UTC | 8m |
| AFR1694 | Air France | Charles de Gaulle International Airport (LFPG) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-07-03 18:31 UTC | 2026-07-03 20:13 UTC | 1h 42m |
| TKR910 | TKR | Mesa Gateway Airport (KIWA) | Rimrock Airport (48AZ) | 2026-07-03 19:53 UTC | 2026-07-03 20:09 UTC | 15m |
| N24VF |  | Granbury Regional Airport (KGDJ) | Cleburne Regional Airport (KCPT) | 2026-07-03 19:34 UTC | 2026-07-03 20:07 UTC | 33m |
| N2020 |  | Moore County Airport (KSOP) | Northeast Philadelphia Airport (KPNE) | 2026-07-03 18:59 UTC | 2026-07-03 20:06 UTC | 1h 7m |
| N7263Q |  | Calaveras County/Maury Rasmussen Field (KCPU) | Merced Yosemite Regional Airport (KMCE) | 2026-07-03 19:34 UTC | 2026-07-03 20:05 UTC | 31m |
| N123VV |  | 0TS2 (0TS2) | Benoit Airfield (77AR) | 2026-07-03 19:16 UTC | 2026-07-03 20:05 UTC | 49m |
| N833JB |  | Van Nuys Airport (KVNY) | Rocky Mountain Metro Airport (KBJC) | 2026-07-03 18:25 UTC | 2026-07-03 20:05 UTC | 1h 39m |
| N58GX |  | San Carlos Airport (KSQL) | Truckee-Tahoe Airport (KTRK) | 2026-07-03 19:27 UTC | 2026-07-03 20:04 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
