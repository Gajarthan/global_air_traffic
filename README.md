# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_01:41:23_UTC-green)

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

**Latest saved flight:** 2026-05-27 01:41:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-27 01:41:23 UTC

- **95,181** saved flights
- **33,537** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **95,181** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,169,732.3 tonnes** estimated CO2 emissions
- **67,810,569 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4008 |
| 2 | SkyWest Airlines | 3538 |
| 3 | IndiGo | 1974 |
| 4 | EJA | 1797 |
| 5 | American Airlines | 1444 |
| 6 | Southwest Airlines | 1387 |
| 7 | ENY | 1176 |
| 8 | Lufthansa | 1142 |
| 9 | Delta Air Lines | 1044 |
| 10 | Vueling | 906 |
| 11 | LATAM Airlines | 857 |
| 12 | AXM | 844 |
| 13 | WIF | 831 |
| 14 | AZU | 762 |
| 15 | LXJ | 721 |
| 16 | Swiss International | 711 |
| 17 | All Nippon Airways | 705 |
| 18 | QLK | 662 |
| 19 | Alaska Airlines | 661 |
| 20 | easyJet | 623 |
| 21 | EJU | 609 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 572 |
| 24 | VIV | 564 |
| 25 | Air France | 562 |
| 26 | CXK | 507 |
| 27 | MXY | 505 |
| 28 | Japan Airlines | 493 |
| 29 | AXB | 480 |
| 30 | AIQ | 459 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 78631 |
| 2 | 🇪🇸 ES | 6663 |
| 3 | 🇮🇳 IN | 6225 |
| 4 | 🇦🇺 AU | 5848 |
| 5 | 🇩🇪 DE | 5228 |
| 6 | 🇧🇷 BR | 5222 |
| 7 | 🇮🇹 IT | 5157 |
| 8 | 🇨🇦 CA | 4823 |
| 9 | 🇯🇵 JP | 4568 |
| 10 | 🇬🇧 GB | 4067 |
| 11 | 🇫🇷 FR | 3849 |
| 12 | 🇨🇴 CO | 3286 |
| 13 | 🇲🇽 MX | 2926 |
| 14 | 🇬🇷 GR | 2734 |
| 15 | 🇳🇴 NO | 2648 |
| 16 | 🇨🇭 CH | 2499 |
| 17 | 🇲🇾 MY | 2136 |
| 18 | 🇹🇷 TR | 1761 |
| 19 | 🇿🇦 ZA | 1715 |
| 20 | 🇳🇿 NZ | 1622 |
| 21 | 🇹🇭 TH | 1614 |
| 22 | 🇰🇷 KR | 1568 |
| 23 | 🇵🇱 PL | 1559 |
| 24 | 🇵🇭 PH | 1438 |
| 25 | 🇬🇹 GT | 1425 |
| 26 | 🇲🇦 MA | 1087 |
| 27 | 🇲🇴 MO | 1038 |
| 28 | 🇳🇱 NL | 958 |
| 29 | 🇲🇪 ME | 941 |
| 30 | 🇭🇷 HR | 866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2057 |
| 2 | Denver International Airport |  | US | 1614 |
| 3 | Tokyo International Airport |  | JP | 1517 |
| 4 | Indira Gandhi International Airport |  | IN | 1349 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1255 |
| 6 | Harry Reid International Airport |  | US | 1228 |
| 7 | Frankfurt am Main International Airport |  | DE | 1156 |
| 8 | Guaymaral Airport |  | CO | 1153 |
| 9 | Zurich Airport |  | CH | 1113 |
| 10 | La Aurora Airport |  | GT | 1091 |
| 11 | Macau International Airport |  | MO | 1038 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1031 |
| 13 | El Dorado International Airport |  | CO | 1030 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 952 |
| 15 | Chicago O'Hare International Airport |  | US | 919 |
| 16 | Kuala Lumpur International Airport |  | MY | 847 |
| 17 | Madrid Barajas International Airport |  | ES | 844 |
| 18 | Salt Lake City International Airport |  | US | 802 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 801 |
| 20 | Capua Airport |  | IT | 788 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 759 |
| 22 | Malpensa International Airport |  | IT | 750 |
| 23 | Bengaluru International Airport |  | IN | 746 |
| 24 | Charles de Gaulle International Airport |  | FR | 743 |
| 25 | Congonhas Airport |  | BR | 726 |
| 26 | Charlotte/Douglas International Airport |  | US | 723 |
| 27 | Daniel K Inouye International Airport |  | US | 681 |
| 28 | Tenerife Norte Airport |  | ES | 675 |
| 29 | Ninoy Aquino International Airport |  | PH | 656 |
| 30 | Barcelona International Airport |  | ES | 641 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 640 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 618 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 611 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Don Mueang International Airport |  | TH | 591 |
| 36 | Amsterdam Airport Schiphol |  | NL | 591 |
| 37 | Vitoria/Foronda Airport |  | ES | 589 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 568 |
| 39 | Calgary International Airport |  | CA | 563 |
| 40 | O. R. Tambo International Airport |  | ZA | 544 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 473 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 351 | 21m | 244 km | 1,478.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 258 | 24m | 225 km | 1,000.9 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 253 | 9m | - | - |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 242 | 1h 26m | 910 km | 3,797.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 242 | 14m | 114 km | 474.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 239 | 28m | 304 km | 1,252.9 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 221 | 1h 10m | 770 km | 2,935.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 190 | 26m | 275 km | 900.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 152 | 21m | 99 km | 260.4 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 143 | 27m | 215 km | 529.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 142 | 14m | 154 km | 376.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 141 | 44m | 452 km | 1,098.9 t |
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
| CHH491 | CHH | Beijing Capital International Airport (ZBAA) | Trufanovo Airfield (XLWT) | 2026-05-26 19:15 UTC | 2026-05-27 01:41 UTC | 6h 25m |
| N472KK |  | South Jersey Regional Airport (KVAY) | Lehigh Valley International Airport (KABE) | 2026-05-27 00:50 UTC | 2026-05-27 01:33 UTC | 42m |
| NGH24 | NGH | Burke Lakefront Airport (KBKL) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-26 23:29 UTC | 2026-05-27 01:28 UTC | 1h 58m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-27 01:03 UTC | 2026-05-27 01:24 UTC | 20m |
| N859JG |  | Princeton Airport (K39N) | Lancaster Airport (KLNS) | 2026-05-27 00:43 UTC | 2026-05-27 01:22 UTC | 39m |
| N394P |  | NM74 (NM74) | Los Alamos Airport (KLAM) | 2026-05-27 00:26 UTC | 2026-05-27 01:07 UTC | 41m |
| N80945 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-27 00:45 UTC | 2026-05-27 01:06 UTC | 20m |
| KSQ | KSQ | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-05-27 00:44 UTC | 2026-05-27 01:05 UTC | 20m |
| N320KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-27 00:09 UTC | 2026-05-27 01:03 UTC | 53m |
| AXM6051 | AXM | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 2026-05-27 00:44 UTC | 2026-05-27 01:03 UTC | 18m |
| ZKLTE | ZKL | Alfredton Airport (NZAN) | Alfredton Airport (NZAN) | 2026-05-26 23:26 UTC | 2026-05-27 01:01 UTC | 1h 35m |
| TIV425 | TIV | Spokane International Airport (KGEG) | Silverton Municipal Airport (79XS) | 2026-05-26 22:13 UTC | 2026-05-27 01:01 UTC | 2h 47m |
| N246SF |  | Dupage Airport (KDPA) | De Kalb Taylor Municipal Airport (KDKB) | 2026-05-27 00:25 UTC | 2026-05-27 00:55 UTC | 30m |
| IY25 |  | Seoul Air Base (RKSM) | G 417 Airport (RK34) | 2026-05-27 00:32 UTC | 2026-05-27 00:54 UTC | 21m |
| GFY164 | GFY | Scappoose Airport (KSPB) | 52OR (52OR) | 2026-05-27 00:10 UTC | 2026-05-27 00:53 UTC | 43m |
| AXM5301 | AXM | Kota Kinabalu International Airport (WBKK) | Seletar Airport (WSSL) | 2026-05-26 23:02 UTC | 2026-05-27 00:52 UTC | 1h 49m |
| N781JH |  | Kansas City/Lee's Summit Regional Airport (KLXT) | Dubuque Regional Airport (KDBQ) | 2026-05-27 00:04 UTC | 2026-05-27 00:50 UTC | 45m |
| SWA2184 | Southwest Airlines | Harry Reid International Airport (KLAS) | NV13 (NV13) | 2026-05-26 23:57 UTC | 2026-05-27 00:49 UTC | 51m |
| SWA1769 | Southwest Airlines | Phoenix Sky Harbor International Airport (KPHX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-05-26 23:11 UTC | 2026-05-27 00:49 UTC | 1h 37m |
| CXK685 | CXK | Sugar Land Regional Airport (KSGR) | Sugar Land Regional Airport (KSGR) | 2026-05-27 00:21 UTC | 2026-05-27 00:48 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
