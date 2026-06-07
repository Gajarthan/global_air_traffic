# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_10:04:57_UTC-green)

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

**Latest saved flight:** 2026-06-07 10:04:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-07 10:04:57 UTC

- **105,152** saved flights
- **37,011** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,152** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,286,404.5 tonnes** estimated CO2 emissions
- **74,574,174 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4325 |
| 2 | SkyWest Airlines | 3961 |
| 3 | IndiGo | 2093 |
| 4 | EJA | 2009 |
| 5 | American Airlines | 1691 |
| 6 | Southwest Airlines | 1591 |
| 7 | ENY | 1320 |
| 8 | Delta Air Lines | 1244 |
| 9 | Lufthansa | 1208 |
| 10 | Vueling | 968 |
| 11 | LATAM Airlines | 929 |
| 12 | WIF | 917 |
| 13 | AXM | 902 |
| 14 | AZU | 841 |
| 15 | LXJ | 792 |
| 16 | Swiss International | 761 |
| 17 | All Nippon Airways | 735 |
| 18 | Alaska Airlines | 730 |
| 19 | QLK | 708 |
| 20 | easyJet | 684 |
| 21 | EJU | 663 |
| 22 | Cathay Pacific | 628 |
| 23 | AEE | 608 |
| 24 | Air France | 603 |
| 25 | VIV | 603 |
| 26 | United Airlines | 585 |
| 27 | MXY | 571 |
| 28 | CXK | 554 |
| 29 | Japan Airlines | 524 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88457 |
| 2 | 🇪🇸 ES | 7238 |
| 3 | 🇮🇳 IN | 6604 |
| 4 | 🇦🇺 AU | 6349 |
| 5 | 🇧🇷 BR | 5725 |
| 6 | 🇩🇪 DE | 5653 |
| 7 | 🇮🇹 IT | 5596 |
| 8 | 🇨🇦 CA | 5470 |
| 9 | 🇯🇵 JP | 4841 |
| 10 | 🇬🇧 GB | 4441 |
| 11 | 🇫🇷 FR | 4174 |
| 12 | 🇨🇴 CO | 3634 |
| 13 | 🇲🇽 MX | 3147 |
| 14 | 🇬🇷 GR | 2998 |
| 15 | 🇳🇴 NO | 2910 |
| 16 | 🇨🇭 CH | 2686 |
| 17 | 🇲🇾 MY | 2308 |
| 18 | 🇹🇷 TR | 2018 |
| 19 | 🇿🇦 ZA | 1812 |
| 20 | 🇳🇿 NZ | 1758 |
| 21 | 🇰🇷 KR | 1748 |
| 22 | 🇹🇭 TH | 1739 |
| 23 | 🇵🇱 PL | 1707 |
| 24 | 🇵🇭 PH | 1555 |
| 25 | 🇬🇹 GT | 1526 |
| 26 | 🇲🇦 MA | 1163 |
| 27 | 🇲🇴 MO | 1103 |
| 28 | 🇳🇱 NL | 1032 |
| 29 | 🇲🇪 ME | 1004 |
| 30 | 🇭🇷 HR | 917 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2285 |
| 2 | Denver International Airport |  | US | 1801 |
| 3 | Tokyo International Airport |  | JP | 1602 |
| 4 | Indira Gandhi International Airport |  | IN | 1436 |
| 5 | Harry Reid International Airport |  | US | 1346 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1333 |
| 7 | Guaymaral Airport |  | CO | 1323 |
| 8 | Frankfurt am Main International Airport |  | DE | 1200 |
| 9 | Zurich Airport |  | CH | 1191 |
| 10 | La Aurora Airport |  | GT | 1174 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1133 |
| 12 | El Dorado International Airport |  | CO | 1108 |
| 13 | Macau International Airport |  | MO | 1103 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1065 |
| 15 | Chicago O'Hare International Airport |  | US | 1058 |
| 16 | Madrid Barajas International Airport |  | ES | 919 |
| 17 | Kuala Lumpur International Airport |  | MY | 903 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 899 |
| 19 | Salt Lake City International Airport |  | US | 898 |
| 20 | Capua Airport |  | IT | 888 |
| 21 | Charlotte/Douglas International Airport |  | US | 816 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 809 |
| 23 | Charles de Gaulle International Airport |  | FR | 801 |
| 24 | Congonhas Airport |  | BR | 795 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 786 |
| 27 | Daniel K Inouye International Airport |  | US | 719 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 712 |
| 30 | Barcelona International Airport |  | ES | 690 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 682 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 678 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 674 |
| 34 | Amsterdam Airport Schiphol |  | NL | 640 |
| 35 | Don Mueang International Airport |  | TH | 636 |
| 36 | Vitoria/Foronda Airport |  | ES | 632 |
| 37 | Calgary International Airport |  | CA | 621 |
| 38 | Seattle-Tacoma International Airport |  | US | 612 |
| 39 | Netaji Subhash Chandra Bose International Airport |  | IN | 604 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 601 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 546 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 387 | 21m | 244 km | 1,629.6 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 282 | 24m | 225 km | 1,094.0 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 266 | 14m | 114 km | 521.7 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 258 | 1h 25m | 910 km | 4,048.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 242 | 1h 10m | 770 km | 3,214.8 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 210 | 26m | 275 km | 995.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 153 | 27m | 215 km | 566.6 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 146 | 31m | 369 km | 929.3 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 140 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 137 | 18m | 144 km | 340.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 119 | 44m | 241 km | 494.3 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO301P | IndiGo | Indira Gandhi International Airport (VIDP) | Agartala Airport (VEAT) | 2026-06-07 08:12 UTC | 2026-06-07 10:04 UTC | 1h 52m |
| AWH91A | AWH | Hannover Airport (EDDV) | Friedrichshafen Airport (EDNY) | 2026-06-07 08:47 UTC | 2026-06-07 10:04 UTC | 1h 17m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-06-07 09:51 UTC | 2026-06-07 10:03 UTC | 12m |
| JJA1406 | JJA | Fukuoka Airport (RJFF) | Incheon International Airport (RKSI) | 2026-06-07 08:57 UTC | 2026-06-07 09:54 UTC | 56m |
| AEZ2629 | AEZ | Linate Airport (LIML) | Olbia / Costa Smeralda Airport (LIEO) | 2026-06-07 09:05 UTC | 2026-06-07 09:47 UTC | 42m |
| DLH2MM | Lufthansa | Bologna / Borgo Panigale Airport (LIPE) | Frankfurt am Main International Airport (EDDF) | 2026-06-07 08:29 UTC | 2026-06-07 09:39 UTC | 1h 10m |
| OAL099 | OAL | Ikaria Airport (LGIK) | Limnos Airport (LGLM) | 2026-06-07 09:00 UTC | 2026-06-07 09:38 UTC | 38m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-06-07 09:09 UTC | 2026-06-07 09:34 UTC | 25m |
| FGNEP | FGN | Sallanches Airport (LFHZ) | Megeve Airport (LFHM) | 2026-06-07 09:08 UTC | 2026-06-07 09:34 UTC | 26m |
| AFR53PG | Air France | Charles de Gaulle International Airport (LFPG) | EGNP (EGNP) | 2026-06-07 08:13 UTC | 2026-06-07 09:33 UTC | 1h 19m |
| AAR372 | AAR | Shenzhen Bao'an International Airport (ZGSZ) | Incheon International Airport (RKSI) | 2026-06-07 06:44 UTC | 2026-06-07 09:30 UTC | 2h 46m |
| SWR9MH | Swiss International | Stuttgart Airport (EDDS) | Zurich Airport (LSZH) | 2026-06-07 09:01 UTC | 2026-06-07 09:30 UTC | 29m |
| IELKO | IEL | LIVD (LIVD) | Bolzano Airport (LIPB) | 2026-06-07 08:04 UTC | 2026-06-07 09:30 UTC | 1h 26m |
| SWR8HG | Swiss International | London Heathrow Airport (EGLL) | Zurich Airport (LSZH) | 2026-06-07 08:15 UTC | 2026-06-07 09:30 UTC | 1h 15m |
| LAV924P | LAV | Valencia Airport (LEVC) | Logrono-Agoncillo Airport (LELO) | 2026-06-07 08:51 UTC | 2026-06-07 09:29 UTC | 38m |
| FHZSL | FHZ | La Mole Airport (LFTZ) | La Mole Airport (LFTZ) | 2026-06-07 08:31 UTC | 2026-06-07 09:24 UTC | 53m |
| WIF47H | WIF | Bergen Airport Flesland (ENBR) | Trondheim Airport Vaernes (ENVA) | 2026-06-07 08:35 UTC | 2026-06-07 09:24 UTC | 48m |
|  |  | Trollhattan-Vanersborg Airport (ESGT) | Trollhattan-Vanersborg Airport (ESGT) | 2026-06-07 09:22 UTC | 2026-06-07 09:24 UTC | 2m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Reykholar Airport (BIRE) | 2026-06-07 09:04 UTC | 2026-06-07 09:23 UTC | 18m |
| QLK1581 | QLK | Sunshine Coast Airport (YBMC) | Sydney Kingsford Smith International Airport (YSSY) | 2026-06-07 07:39 UTC | 2026-06-07 09:23 UTC | 1h 44m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
