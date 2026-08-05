# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_04:05:28_UTC-green)

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

**Latest saved flight:** 2026-08-05 04:05:28 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-05 04:05:28 UTC

- **171,701** saved flights
- **55,829** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **171,701** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,069,672.2 tonnes** estimated CO2 emissions
- **119,980,996 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6827 |
| 2 | SkyWest Airlines | 6293 |
| 3 | EJA | 3413 |
| 4 | IndiGo | 3009 |
| 5 | Southwest Airlines | 2708 |
| 6 | American Airlines | 2704 |
| 7 | ENY | 2140 |
| 8 | Delta Air Lines | 2043 |
| 9 | LATAM Airlines | 1590 |
| 10 | Lufthansa | 1564 |
| 11 | AZU | 1513 |
| 12 | WIF | 1433 |
| 13 | Vueling | 1407 |
| 14 | LXJ | 1344 |
| 15 | AXM | 1180 |
| 16 | Swiss International | 1167 |
| 17 | easyJet | 1155 |
| 18 | QLK | 1053 |
| 19 | Alaska Airlines | 1050 |
| 20 | EJU | 1048 |
| 21 | All Nippon Airways | 1039 |
| 22 | VIV | 947 |
| 23 | Cathay Pacific | 928 |
| 24 | CXK | 913 |
| 25 | GLO | 902 |
| 26 | United Airlines | 901 |
| 27 | AEE | 893 |
| 28 | Air France | 880 |
| 29 | MXY | 872 |
| 30 | JetBlue | 861 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 148119 |
| 2 | 🇪🇸 ES | 10980 |
| 3 | 🇧🇷 BR | 9767 |
| 4 | 🇦🇺 AU | 9611 |
| 5 | 🇮🇳 IN | 9435 |
| 6 | 🇨🇦 CA | 9386 |
| 7 | 🇮🇹 IT | 8867 |
| 8 | 🇩🇪 DE | 8514 |
| 9 | 🇬🇧 GB | 7944 |
| 10 | 🇯🇵 JP | 6897 |
| 11 | 🇫🇷 FR | 6795 |
| 12 | 🇨🇴 CO | 6265 |
| 13 | 🇬🇷 GR | 4979 |
| 14 | 🇲🇽 MX | 4921 |
| 15 | 🇨🇭 CH | 4500 |
| 16 | 🇳🇴 NO | 4469 |
| 17 | 🇹🇷 TR | 4194 |
| 18 | 🇲🇾 MY | 3064 |
| 19 | 🇵🇱 PL | 2876 |
| 20 | 🇿🇦 ZA | 2770 |
| 21 | 🇹🇭 TH | 2496 |
| 22 | 🇳🇿 NZ | 2491 |
| 23 | 🇵🇭 PH | 2267 |
| 24 | 🇬🇹 GT | 2200 |
| 25 | 🇰🇷 KR | 2167 |
| 26 | 🇲🇦 MA | 1726 |
| 27 | 🇭🇷 HR | 1651 |
| 28 | 🇲🇪 ME | 1575 |
| 29 | 🇳🇱 NL | 1555 |
| 30 | 🇲🇴 MO | 1478 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3543 |
| 2 | Denver International Airport |  | US | 2849 |
| 3 | Tokyo International Airport |  | JP | 2161 |
| 4 | Guaymaral Airport |  | CO | 2128 |
| 5 | Indira Gandhi International Airport |  | IN | 2095 |
| 6 | Harry Reid International Airport |  | US | 2061 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1868 |
| 8 | Zurich Airport |  | CH | 1810 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1805 |
| 10 | La Aurora Airport |  | GT | 1698 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1589 |
| 12 | Chicago O'Hare International Airport |  | US | 1559 |
| 13 | El Dorado International Airport |  | CO | 1557 |
| 14 | Salt Lake City International Airport |  | US | 1540 |
| 15 | Frankfurt am Main International Airport |  | DE | 1529 |
| 16 | Macau International Airport |  | MO | 1478 |
| 17 | Congonhas Airport |  | BR | 1409 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1406 |
| 19 | Madrid Barajas International Airport |  | ES | 1342 |
| 20 | Capua Airport |  | IT | 1336 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1299 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1211 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1201 |
| 24 | Charlotte/Douglas International Airport |  | US | 1192 |
| 25 | Charles de Gaulle International Airport |  | FR | 1164 |
| 26 | Malpensa International Airport |  | IT | 1156 |
| 27 | Kuala Lumpur International Airport |  | MY | 1154 |
| 28 | Bengaluru International Airport |  | IN | 1122 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1069 |
| 30 | Ninoy Aquino International Airport |  | PH | 1067 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1059 |
| 32 | Barcelona International Airport |  | ES | 1014 |
| 33 | Daniel K Inouye International Airport |  | US | 996 |
| 34 | Seattle-Tacoma International Airport |  | US | 995 |
| 35 | Viracopos International Airport |  | BR | 977 |
| 36 | Calgary International Airport |  | CA | 973 |
| 37 | Reno/Tahoe International Airport |  | US | 968 |
| 38 | Oslo Gardermoen Airport |  | NO | 954 |
| 39 | Tenerife Norte Airport |  | ES | 952 |
| 40 | Scottsdale Airport |  | US | 942 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 881 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 628 | 21m | 244 km | 2,644.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 407 | 24m | 225 km | 1,579.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 405 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 389 | 1h 8m | 770 km | 5,167.6 t |
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
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 206 | 50m | 556 km | 1,974.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 204 | 1h 15m | 961 km | 3,381.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 203 | 19m | 144 km | 505.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 201 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 199 | 31m | 369 km | 1,266.7 t |
| 26 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 199 | 28m | 152 km | 520.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 194 | 1h 38m | 1,156 km | 3,870.2 t |
| 28 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 189 | 8m | - | - |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 188 | 24m | 218 km | 708.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 187 | 1h 1m | 695 km | 2,241.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| WXY | WXY | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-08-05 03:53 UTC | 2026-08-05 04:05 UTC | 11m |
| WPF | WPF | Perth Jandakot Airport (YPJT) | Kalgoorlie-Boulder Airport (YPKG) | 2026-08-05 03:11 UTC | 2026-08-05 04:05 UTC | 53m |
| CJT626 | CJT | John C. Munro Hamilton International Airport (CYHM) | Montréal (Mirabel) Airport (CYMX) | 2026-08-05 03:16 UTC | 2026-08-05 04:04 UTC | 48m |
| ZKSWG | ZKS | Invercargill Airport (NZNV) | Invercargill Airport (NZNV) | 2026-08-05 03:38 UTC | 2026-08-05 03:54 UTC | 16m |
| HKE541 | HKE | Chek Lap Kok International Airport (VHHH) | Macau International Airport (VMMC) | 2026-08-05 00:09 UTC | 2026-08-05 03:53 UTC | 3h 44m |
| XCN81 | XCN | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-08-05 03:34 UTC | 2026-08-05 03:51 UTC | 16m |
| SKW5051 | SkyWest Airlines | Denver International Airport (KDEN) | Steamboat Springs/Bob Adams Field (KSBS) | 2026-08-05 03:27 UTC | 2026-08-05 03:47 UTC | 19m |
| PSQ | PSQ | Hillman Farm Airport (YHLM) | Hillman Farm Airport (YHLM) | 2026-08-05 03:32 UTC | 2026-08-05 03:46 UTC | 14m |
| A7GQE |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-05 02:24 UTC | 2026-08-05 03:41 UTC | 1h 16m |
| N9055F |  | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-08-05 03:20 UTC | 2026-08-05 03:35 UTC | 15m |
| N81LN |  | Valley Point Airport (WV29) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-08-05 03:22 UTC | 2026-08-05 03:30 UTC | 7m |
| N908PA |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-08-05 02:26 UTC | 2026-08-05 03:25 UTC | 59m |
| RXA6174 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bathurst Airport (YBTH) | 2026-08-05 02:58 UTC | 2026-08-05 03:24 UTC | 25m |
| RAX317 | RAX | Jacksonville International Airport (KJAX) | Garden County/King Rhiley Field (KOKS) | 2026-08-05 00:26 UTC | 2026-08-05 03:21 UTC | 2h 54m |
| AM313 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-08-05 02:53 UTC | 2026-08-05 03:19 UTC | 25m |
| SCU5 | SCU | William R Pogue Municipal Airport (KOWP) | Tulsa International Airport (KTUL) | 2026-08-05 03:01 UTC | 2026-08-05 03:18 UTC | 16m |
| FFL1496 | FFL | Central Wisconsin Airport (KCWA) | Guthrie/Edmond Regional Airport (KGOK) | 2026-08-05 01:18 UTC | 2026-08-05 03:18 UTC | 1h 59m |
| 01172065 |  | Laredo International Airport (KLRD) | Quetzalcoatl International Airport (MMNL) | 2026-08-05 02:41 UTC | 2026-08-05 03:17 UTC | 35m |
| GH60 |  | North Island Nas (Halsey Field) Airport (KNZY) | San Clemente Island Nalf Airport (KNUC) | 2026-08-05 01:58 UTC | 2026-08-05 03:17 UTC | 1h 19m |
| FRED09 | FRE | 01PN (01PN) | Dover Afb Airport (KDOV) | 2026-08-05 02:48 UTC | 2026-08-05 03:17 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
