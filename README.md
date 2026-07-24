# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_21:16:38_UTC-green)

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

**Latest saved flight:** 2026-07-24 21:16:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 21:16:38 UTC

- **148,845** saved flights
- **49,659** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **148,845** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,779,411.3 tonnes** estimated CO2 emissions
- **103,154,280 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6004 |
| 2 | SkyWest Airlines | 5446 |
| 3 | EJA | 2952 |
| 4 | IndiGo | 2666 |
| 5 | American Airlines | 2371 |
| 6 | Southwest Airlines | 2253 |
| 7 | ENY | 1854 |
| 8 | Delta Air Lines | 1758 |
| 9 | Lufthansa | 1455 |
| 10 | LATAM Airlines | 1370 |
| 11 | AZU | 1286 |
| 12 | WIF | 1268 |
| 13 | Vueling | 1258 |
| 14 | LXJ | 1152 |
| 15 | AXM | 1071 |
| 16 | Swiss International | 1052 |
| 17 | easyJet | 962 |
| 18 | All Nippon Airways | 937 |
| 19 | Alaska Airlines | 931 |
| 20 | QLK | 922 |
| 21 | EJU | 909 |
| 22 | VIV | 821 |
| 23 | CXK | 798 |
| 24 | AEE | 780 |
| 25 | Air France | 779 |
| 26 | JetBlue | 779 |
| 27 | MXY | 775 |
| 28 | Cathay Pacific | 773 |
| 29 | GLO | 771 |
| 30 | United Airlines | 770 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 128550 |
| 2 | 🇪🇸 ES | 9606 |
| 3 | 🇦🇺 AU | 8459 |
| 4 | 🇧🇷 BR | 8402 |
| 5 | 🇮🇳 IN | 8371 |
| 6 | 🇨🇦 CA | 7978 |
| 7 | 🇮🇹 IT | 7694 |
| 8 | 🇩🇪 DE | 7614 |
| 9 | 🇬🇧 GB | 6802 |
| 10 | 🇯🇵 JP | 6154 |
| 11 | 🇫🇷 FR | 5902 |
| 12 | 🇨🇴 CO | 5001 |
| 13 | 🇲🇽 MX | 4311 |
| 14 | 🇬🇷 GR | 4208 |
| 15 | 🇳🇴 NO | 3974 |
| 16 | 🇨🇭 CH | 3899 |
| 17 | 🇹🇷 TR | 3498 |
| 18 | 🇲🇾 MY | 2790 |
| 19 | 🇵🇱 PL | 2507 |
| 20 | 🇿🇦 ZA | 2406 |
| 21 | 🇳🇿 NZ | 2245 |
| 22 | 🇹🇭 TH | 2167 |
| 23 | 🇰🇷 KR | 2055 |
| 24 | 🇵🇭 PH | 1977 |
| 25 | 🇬🇹 GT | 1943 |
| 26 | 🇲🇦 MA | 1520 |
| 27 | 🇲🇪 ME | 1469 |
| 28 | 🇳🇱 NL | 1379 |
| 29 | 🇭🇷 HR | 1351 |
| 30 | 🇲🇴 MO | 1236 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3065 |
| 2 | Denver International Airport |  | US | 2495 |
| 3 | Tokyo International Airport |  | JP | 1972 |
| 4 | Guaymaral Airport |  | CO | 1863 |
| 5 | Indira Gandhi International Airport |  | IN | 1859 |
| 6 | Harry Reid International Airport |  | US | 1848 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1668 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1568 |
| 10 | La Aurora Airport |  | GT | 1505 |
| 11 | Frankfurt am Main International Airport |  | DE | 1404 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1401 |
| 13 | Chicago O'Hare International Airport |  | US | 1381 |
| 14 | Salt Lake City International Airport |  | US | 1341 |
| 15 | El Dorado International Airport |  | CO | 1335 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1280 |
| 17 | Macau International Airport |  | MO | 1236 |
| 18 | Congonhas Airport |  | BR | 1200 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1181 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1158 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1066 |
| 24 | Charlotte/Douglas International Airport |  | US | 1062 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1045 |
| 26 | Charles de Gaulle International Airport |  | FR | 1029 |
| 27 | Bengaluru International Airport |  | IN | 1001 |
| 28 | Malpensa International Airport |  | IT | 962 |
| 29 | Ninoy Aquino International Airport |  | PH | 926 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 906 |
| 31 | Barcelona International Airport |  | ES | 896 |
| 32 | Daniel K Inouye International Airport |  | US | 893 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 890 |
| 34 | Seattle-Tacoma International Airport |  | US | 852 |
| 35 | Calgary International Airport |  | CA | 851 |
| 36 | Tenerife Norte Airport |  | ES | 850 |
| 37 | Scottsdale Airport |  | US | 847 |
| 38 | Viracopos International Airport |  | BR | 839 |
| 39 | Amsterdam Airport Schiphol |  | NL | 829 |
| 40 | Oslo Gardermoen Airport |  | NO | 824 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 786 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 539 | 21m | 244 km | 2,269.6 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 360 | 24m | 225 km | 1,396.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 346 | 1h 9m | 770 km | 4,596.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
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
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 175 | 31m | 369 km | 1,113.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 175 | 1h 16m | 961 km | 2,900.7 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 175 | 18m | 144 km | 435.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 174 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N84BL |  | John F Kennedy International Airport (KJFK) | John F Kennedy International Airport (KJFK) | 2026-07-24 20:54 UTC | 2026-07-24 21:16 UTC | 22m |
| QTR254 | Qatar Airways | Tbilisi International Airport (UGTB) | Ras Tanura Airport (OERT) | 2026-07-24 18:01 UTC | 2026-07-24 21:07 UTC | 3h 6m |
| N634GL |  | Okmulgee Regional/Paul And Betty Abbott Field (KOKM) | Tulsa International Airport (KTUL) | 2026-07-24 20:29 UTC | 2026-07-24 21:06 UTC | 37m |
| N7688M |  | Fullerton Municipal Airport (KFUL) | Whiteman Airport (KWHP) | 2026-07-24 20:41 UTC | 2026-07-24 21:04 UTC | 22m |
| KAI82 | KAI | Napa County Airport (KAPC) | Andrews County Airport (KE11) | 2026-07-24 18:28 UTC | 2026-07-24 21:01 UTC | 2h 33m |
| N9531J |  | Mckinney Ntl Airport (KTKI) | Mckinney Ntl Airport (KTKI) | 2026-07-24 20:46 UTC | 2026-07-24 21:00 UTC | 13m |
| N4438U |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-07-24 19:48 UTC | 2026-07-24 20:54 UTC | 1h 6m |
| TKR183 | TKR | Boise Air Trml/Gowen Field (KBOI) | Mountain Home Afb Airport (KMUO) | 2026-07-24 20:43 UTC | 2026-07-24 20:53 UTC | 10m |
| ILU26U | ILU | University Of Illinois/Willard Airport (KCMI) | Triple Creek Airport (1IS2) | 2026-07-24 20:16 UTC | 2026-07-24 20:52 UTC | 36m |
| ATCK103 | ATC | Coeur D'Alene/Pappy Boyington Field (KCOE) | Libby Airport (KS59) | 2026-07-24 19:11 UTC | 2026-07-24 20:50 UTC | 1h 38m |
| N285SD |  | John Glenn Columbus International Airport (KCMH) | Murphy Airport (3II0) | 2026-07-24 20:13 UTC | 2026-07-24 20:49 UTC | 36m |
| C6517 |  | Florence Municipal Airport (K6S2) | Newport Municipal Airport (KONP) | 2026-07-24 20:35 UTC | 2026-07-24 20:49 UTC | 14m |
| N90MC |  | John F Kennedy International Airport (KJFK) | Philadelphia International Airport (KPHL) | 2026-07-24 20:13 UTC | 2026-07-24 20:48 UTC | 34m |
| N894AA |  | St Clair County International Airport (KPHN) | St Clair County International Airport (KPHN) | 2026-07-24 20:39 UTC | 2026-07-24 20:47 UTC | 8m |
| N99DQ |  | Francis S Gabreski Airport (KFOK) | Laguardia Airport (KLGA) | 2026-07-24 20:19 UTC | 2026-07-24 20:47 UTC | 28m |
| N73574 |  | Dupage Airport (KDPA) | 0IL8 (0IL8) | 2026-07-24 20:12 UTC | 2026-07-24 20:45 UTC | 33m |
| CGQHW | CGQ | Saint John Airport (CYSJ) | Saint John Airport (CYSJ) | 2026-07-24 20:23 UTC | 2026-07-24 20:45 UTC | 22m |
| JANET09 | JAN | Trona Airport (KL72) | Edwards Af Aux North Base Airport (K9L2) | 2026-07-24 20:32 UTC | 2026-07-24 20:43 UTC | 11m |
| N3250V |  | Midland International Air And Space Port Airport (KMAF) | Santa Fe Regional Airport (KSAF) | 2026-07-24 19:15 UTC | 2026-07-24 20:38 UTC | 1h 22m |
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-07-24 20:26 UTC | 2026-07-24 20:35 UTC | 9m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
