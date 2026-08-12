# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_17:32:29_UTC-green)

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

**Latest saved flight:** 2026-08-12 17:32:29 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-12 17:32:29 UTC

- **190,055** saved flights
- **60,036** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **190,055** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,275,323.4 tonnes** estimated CO2 emissions
- **131,902,804 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7536 |
| 2 | SkyWest Airlines | 6878 |
| 3 | EJA | 3750 |
| 4 | IndiGo | 3309 |
| 5 | Southwest Airlines | 2967 |
| 6 | American Airlines | 2943 |
| 7 | ENY | 2351 |
| 8 | Delta Air Lines | 2229 |
| 9 | LATAM Airlines | 1781 |
| 10 | AZU | 1714 |
| 11 | Lufthansa | 1657 |
| 12 | Vueling | 1578 |
| 13 | WIF | 1578 |
| 14 | LXJ | 1486 |
| 15 | easyJet | 1310 |
| 16 | Swiss International | 1296 |
| 17 | AXM | 1253 |
| 18 | EJU | 1172 |
| 19 | QLK | 1168 |
| 20 | All Nippon Airways | 1155 |
| 21 | Alaska Airlines | 1132 |
| 22 | VIV | 1049 |
| 23 | GLO | 1025 |
| 24 | Air France | 993 |
| 25 | PGT | 981 |
| 26 | AEE | 973 |
| 27 | CXK | 972 |
| 28 | United Airlines | 972 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 945 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 161893 |
| 2 | 🇪🇸 ES | 12259 |
| 3 | 🇧🇷 BR | 10926 |
| 4 | 🇦🇺 AU | 10655 |
| 5 | 🇨🇦 CA | 10407 |
| 6 | 🇮🇳 IN | 10367 |
| 7 | 🇮🇹 IT | 9864 |
| 8 | 🇩🇪 DE | 9400 |
| 9 | 🇬🇧 GB | 8849 |
| 10 | 🇯🇵 JP | 7769 |
| 11 | 🇫🇷 FR | 7608 |
| 12 | 🇨🇴 CO | 7284 |
| 13 | 🇬🇷 GR | 5565 |
| 14 | 🇲🇽 MX | 5393 |
| 15 | 🇨🇭 CH | 5100 |
| 16 | 🇹🇷 TR | 5058 |
| 17 | 🇳🇴 NO | 4898 |
| 18 | 🇲🇾 MY | 3276 |
| 19 | 🇿🇦 ZA | 3209 |
| 20 | 🇵🇱 PL | 3146 |
| 21 | 🇹🇭 TH | 2940 |
| 22 | 🇳🇿 NZ | 2682 |
| 23 | 🇵🇭 PH | 2510 |
| 24 | 🇬🇹 GT | 2404 |
| 25 | 🇰🇷 KR | 2334 |
| 26 | 🇭🇷 HR | 1945 |
| 27 | 🇲🇦 MA | 1926 |
| 28 | 🇳🇱 NL | 1698 |
| 29 | 🇲🇪 ME | 1685 |
| 30 | 🇲🇴 MO | 1526 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3938 |
| 2 | Denver International Airport |  | US | 3123 |
| 3 | Tokyo International Airport |  | JP | 2396 |
| 4 | Guaymaral Airport |  | CO | 2347 |
| 5 | Indira Gandhi International Airport |  | IN | 2335 |
| 6 | Harry Reid International Airport |  | US | 2218 |
| 7 | Zurich Airport |  | CH | 2020 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2013 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1967 |
| 10 | La Aurora Airport |  | GT | 1848 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1717 |
| 12 | El Dorado International Airport |  | CO | 1713 |
| 13 | Salt Lake City International Airport |  | US | 1685 |
| 14 | Chicago O'Hare International Airport |  | US | 1661 |
| 15 | Frankfurt am Main International Airport |  | DE | 1625 |
| 16 | Congonhas Airport |  | BR | 1588 |
| 17 | Macau International Airport |  | MO | 1526 |
| 18 | Madrid Barajas International Airport |  | ES | 1500 |
| 19 | Capua Airport |  | IT | 1474 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1472 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1400 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1363 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1324 |
| 24 | Malpensa International Airport |  | IT | 1312 |
| 25 | Charles de Gaulle International Airport |  | FR | 1302 |
| 26 | Charlotte/Douglas International Airport |  | US | 1273 |
| 27 | Kuala Lumpur International Airport |  | MY | 1226 |
| 28 | Bengaluru International Airport |  | IN | 1224 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1188 |
| 30 | Ninoy Aquino International Airport |  | PH | 1186 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1166 |
| 32 | Barcelona International Airport |  | ES | 1136 |
| 33 | Viracopos International Airport |  | BR | 1102 |
| 34 | Reno/Tahoe International Airport |  | US | 1095 |
| 35 | Seattle-Tacoma International Airport |  | US | 1091 |
| 36 | Calgary International Airport |  | CA | 1083 |
| 37 | Daniel K Inouye International Airport |  | US | 1066 |
| 38 | Oslo Gardermoen Airport |  | NO | 1063 |
| 39 | Tenerife Norte Airport |  | ES | 1043 |
| 40 | Vitoria/Foronda Airport |  | ES | 1031 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 969 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 694 | 21m | 244 km | 2,922.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 461 | 1h 7m | 770 km | 6,124.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 442 | 24m | 225 km | 1,714.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 441 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 333 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 319 | 27m | 275 km | 1,511.6 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 296 | 8m | - | - |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 283 | 44m | 241 km | 1,175.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 275 | 22m | 55 km | 261.4 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 273 | 1h 49m | 1,423 km | 6,699.9 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 255 | 20m | 250 km | 1,101.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 238 | 27m | 215 km | 881.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 238 | 13m | - | - |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 232 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 231 | 1h 15m | 961 km | 3,828.9 t |
| 23 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 231 | 19m | 99 km | 395.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 227 | 19m | 144 km | 564.7 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 226 | 24m | 218 km | 851.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 226 | 1h 38m | 1,156 km | 4,508.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 219 | 31m | 369 km | 1,394.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 207 | 1h 48m | 1,304 km | 4,657.0 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 207 | 28m | 152 km | 541.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N243SD |  | Brookings Regional Airport (KBKX) | Brookings Regional Airport (KBKX) | 2026-08-12 16:47 UTC | 2026-08-12 17:32 UTC | 45m |
| DHXCI | DHX | Straubing Airport (EDMS) | Schmidgaden Airport (EDPQ) | 2026-08-12 17:01 UTC | 2026-08-12 17:20 UTC | 19m |
| N38549 |  | Laconia Municipal Airport (KLCI) | Lebanon Municipal Airport (KLEB) | 2026-08-12 16:37 UTC | 2026-08-12 17:17 UTC | 39m |
| CONGO64 | CON | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-08-12 16:48 UTC | 2026-08-12 17:17 UTC | 28m |
| EXS8T | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-12 16:11 UTC | 2026-08-12 17:17 UTC | 1h 5m |
| MSR848 | EgyptAir | Mohammed V International Airport (GMMN) | HE12 (HE12) | 2026-08-12 12:40 UTC | 2026-08-12 17:13 UTC | 4h 32m |
| BRW16 | BRW | Flying Cloud Airport (KFCM) | Quast Airport (MN62) | 2026-08-12 16:37 UTC | 2026-08-12 17:10 UTC | 32m |
| NDU66 | NDU | Central Valley Aviation Airport (NA81) | Hillsboro Municipal Airport (K3H4) | 2026-08-12 16:46 UTC | 2026-08-12 17:08 UTC | 22m |
| JAG1332 | JAG | Yibal Airport (OOYB) | Buraimi Airport (OOBR) | 2026-08-12 16:44 UTC | 2026-08-12 17:03 UTC | 18m |
| N1967H |  | Modesto City-County-Harry Sham Field (KMOD) | Fall River Mills Airport (KO89) | 2026-08-12 16:19 UTC | 2026-08-12 17:02 UTC | 42m |
| N7231R |  | 00AZ (00AZ) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-12 16:33 UTC | 2026-08-12 17:01 UTC | 27m |
| TORA21 | TOR | 75OK (75OK) | Lariat Ranch Airport (OK42) | 2026-08-12 16:39 UTC | 2026-08-12 16:58 UTC | 19m |
| N739UK |  | Boise Air Trml/Gowen Field (KBOI) | Cascade Airport (KU70) | 2026-08-12 16:25 UTC | 2026-08-12 16:58 UTC | 33m |
| EFC32J | EFC | Al Maktoum International Airport (OMDW) | Al Maktoum International Airport (OMDW) | 2026-08-12 16:45 UTC | 2026-08-12 16:57 UTC | 11m |
| OXF3966 | OXF | Falcon Field (KFFZ) | Four Pillars Airport (AZ21) | 2026-08-12 15:29 UTC | 2026-08-12 16:56 UTC | 1h 26m |
| N528LP |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-08-12 16:14 UTC | 2026-08-12 16:53 UTC | 39m |
| N3070G |  | Charleston Executive Airport (KJZI) | Charleston Afb/International Airport (KCHS) | 2026-08-12 16:11 UTC | 2026-08-12 16:49 UTC | 38m |
| FTO383 | FTO | KHTO (KHTO) | Laguardia Airport (KLGA) | 2026-08-12 16:10 UTC | 2026-08-12 16:48 UTC | 38m |
| HK5463G |  | Madrid Air Base (SKMA) | Guaymaral Airport (SKGY) | 2026-08-12 16:37 UTC | 2026-08-12 16:48 UTC | 11m |
| CXK430 | CXK | Centennial Airport (KAPA) | Morris Airport (CD13) | 2026-08-12 15:30 UTC | 2026-08-12 16:48 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
