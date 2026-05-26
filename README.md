# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_23:29:45_UTC-green)

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

**Latest saved flight:** 2026-05-26 23:29:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-26 23:29:45 UTC

- **95,071** saved flights
- **33,513** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **95,071** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,168,976.5 tonnes** estimated CO2 emissions
- **67,766,752 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4008 |
| 2 | SkyWest Airlines | 3529 |
| 3 | IndiGo | 1973 |
| 4 | EJA | 1797 |
| 5 | American Airlines | 1443 |
| 6 | Southwest Airlines | 1380 |
| 7 | ENY | 1176 |
| 8 | Lufthansa | 1142 |
| 9 | Delta Air Lines | 1043 |
| 10 | Vueling | 906 |
| 11 | LATAM Airlines | 855 |
| 12 | AXM | 840 |
| 13 | WIF | 831 |
| 14 | AZU | 762 |
| 15 | LXJ | 720 |
| 16 | Swiss International | 711 |
| 17 | All Nippon Airways | 702 |
| 18 | QLK | 660 |
| 19 | Alaska Airlines | 659 |
| 20 | easyJet | 623 |
| 21 | EJU | 609 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 572 |
| 24 | Air France | 562 |
| 25 | VIV | 562 |
| 26 | CXK | 506 |
| 27 | MXY | 505 |
| 28 | Japan Airlines | 491 |
| 29 | AXB | 480 |
| 30 | AIQ | 457 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78529 |
| 2 | 🇪🇸 ES | 6663 |
| 3 | 🇮🇳 IN | 6223 |
| 4 | 🇦🇺 AU | 5822 |
| 5 | 🇩🇪 DE | 5228 |
| 6 | 🇧🇷 BR | 5218 |
| 7 | 🇮🇹 IT | 5157 |
| 8 | 🇨🇦 CA | 4819 |
| 9 | 🇯🇵 JP | 4551 |
| 10 | 🇬🇧 GB | 4067 |
| 11 | 🇫🇷 FR | 3849 |
| 12 | 🇨🇴 CO | 3284 |
| 13 | 🇲🇽 MX | 2918 |
| 14 | 🇬🇷 GR | 2734 |
| 15 | 🇳🇴 NO | 2648 |
| 16 | 🇨🇭 CH | 2499 |
| 17 | 🇲🇾 MY | 2126 |
| 18 | 🇹🇷 TR | 1761 |
| 19 | 🇿🇦 ZA | 1715 |
| 20 | 🇳🇿 NZ | 1616 |
| 21 | 🇹🇭 TH | 1610 |
| 22 | 🇰🇷 KR | 1561 |
| 23 | 🇵🇱 PL | 1559 |
| 24 | 🇵🇭 PH | 1436 |
| 25 | 🇬🇹 GT | 1425 |
| 26 | 🇲🇦 MA | 1087 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 958 |
| 29 | 🇲🇪 ME | 941 |
| 30 | 🇭🇷 HR | 866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2055 |
| 2 | Denver International Airport |  | US | 1612 |
| 3 | Tokyo International Airport |  | JP | 1510 |
| 4 | Indira Gandhi International Airport |  | IN | 1349 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1255 |
| 6 | Harry Reid International Airport |  | US | 1226 |
| 7 | Frankfurt am Main International Airport |  | DE | 1156 |
| 8 | Guaymaral Airport |  | CO | 1151 |
| 9 | Zurich Airport |  | CH | 1113 |
| 10 | La Aurora Airport |  | GT | 1091 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | El Dorado International Airport |  | CO | 1030 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1029 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 948 |
| 15 | Chicago O'Hare International Airport |  | US | 919 |
| 16 | Madrid Barajas International Airport |  | ES | 844 |
| 17 | Kuala Lumpur International Airport |  | MY | 843 |
| 18 | Salt Lake City International Airport |  | US | 801 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 800 |
| 20 | Capua Airport |  | IT | 788 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 756 |
| 22 | Malpensa International Airport |  | IT | 750 |
| 23 | Bengaluru International Airport |  | IN | 746 |
| 24 | Charles de Gaulle International Airport |  | FR | 743 |
| 25 | Congonhas Airport |  | BR | 724 |
| 26 | Charlotte/Douglas International Airport |  | US | 723 |
| 27 | Daniel K Inouye International Airport |  | US | 679 |
| 28 | Tenerife Norte Airport |  | ES | 675 |
| 29 | Ninoy Aquino International Airport |  | PH | 655 |
| 30 | Barcelona International Airport |  | ES | 641 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 639 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 617 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 611 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 591 |
| 36 | Don Mueang International Airport |  | TH | 589 |
| 37 | Vitoria/Foronda Airport |  | ES | 589 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 563 |
| 40 | O. R. Tambo International Airport |  | ZA | 544 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 472 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 349 | 21m | 244 km | 1,469.5 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 257 | 24m | 225 km | 997.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 253 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 241 | 1h 26m | 910 km | 3,781.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 239 | 28m | 304 km | 1,252.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 218 | 1h 10m | 770 km | 2,896.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 205 | 19m | 165 km | 583.1 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 190 | 26m | 275 km | 900.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 143 | 27m | 215 km | 529.6 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 141 | 14m | 154 km | 373.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 136 | 27m | 152 km | 355.4 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 129 | 20m | 250 km | 557.2 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 124 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 122 | 18m | 144 km | 303.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 119 | 1h 39m | 1,156 km | 2,374.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 52m | 1,304 km | 2,587.2 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 113 | 1h 18m | 961 km | 1,873.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| THA924 | Thai Airways | Suvarnabhumi Airport (VTBS) | Jammu Airport (VIJU) | 2026-05-26 19:31 UTC | 2026-05-26 23:29 UTC | 3h 57m |
| CRDO503 | CRD | Courtenay Airpark (CAH3) | Port Alberni Airport (CBS8) | 2026-05-26 21:17 UTC | 2026-05-26 23:29 UTC | 2h 11m |
| LXJ420 | LXJ | Oakland San Francisco Bay Airport (KOAK) | Scottsdale Airport (KSDL) | 2026-05-26 21:56 UTC | 2026-05-26 23:25 UTC | 1h 28m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-26 23:09 UTC | 2026-05-26 23:24 UTC | 15m |
| FBIR100 | FBI | Hamilton Airport (YHML) | Branxholme Airport (YBXH) | 2026-05-26 23:10 UTC | 2026-05-26 23:24 UTC | 14m |
| URSA20 | URS | Fairbanks International Airport (PAFA) | Ladd Army Air Field (PAFB) | 2026-05-26 22:41 UTC | 2026-05-26 23:21 UTC | 39m |
| N424KT |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-26 22:56 UTC | 2026-05-26 23:21 UTC | 25m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-26 22:57 UTC | 2026-05-26 23:19 UTC | 22m |
| UAL1354 | United Airlines | Pittsburgh International Airport (KPIT) | Denver International Airport (KDEN) | 2026-05-26 20:37 UTC | 2026-05-26 23:18 UTC | 2h 41m |
| N80945 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-26 22:53 UTC | 2026-05-26 23:15 UTC | 21m |
| URSA19 | URS | Gold King Creek Airport (PAAN) | Ladd Army Air Field (PAFB) | 2026-05-26 22:40 UTC | 2026-05-26 23:14 UTC | 33m |
| ZKLTE | ZKL | Alfredton Airport (NZAN) | Alfredton Airport (NZAN) | 2026-05-26 21:29 UTC | 2026-05-26 23:12 UTC | 1h 43m |
| N628SR |  | Livermore Municipal Airport (KLVK) | K4SD (K4SD) | 2026-05-26 22:34 UTC | 2026-05-26 23:11 UTC | 37m |
| N85VR |  | Mexia-Limestone County Airport (KLXY) | Hall-Miller Municipal Airport (KATA) | 2026-05-26 22:40 UTC | 2026-05-26 23:09 UTC | 28m |
| DHK7LK | DHK | East Midlands Airport (EGNX) | Leipzig Halle Airport (EDDP) | 2026-05-26 21:32 UTC | 2026-05-26 23:03 UTC | 1h 31m |
| N938SB |  | Rickenbacker International Airport (KLCK) | GA09 (GA09) | 2026-05-26 21:37 UTC | 2026-05-26 23:03 UTC | 1h 25m |
| N504YH |  | Bellingham International Airport (KBLI) | William R Fairchild International Airport (KCLM) | 2026-05-26 21:58 UTC | 2026-05-26 23:01 UTC | 1h 3m |
| N7288F |  | Mckinney Ntl Airport (KTKI) | Flying Tiger Field (6TA2) | 2026-05-26 22:25 UTC | 2026-05-26 22:59 UTC | 34m |
| XSN25 | XSN | Stone Land Company Airport (36CA) | San Carlos Airport (KSQL) | 2026-05-26 22:12 UTC | 2026-05-26 22:53 UTC | 40m |
| N699SU |  | Aurora State Airport (KUAO) | Western Helicopter Services Airport (OR38) | 2026-05-26 22:45 UTC | 2026-05-26 22:51 UTC | 5m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
