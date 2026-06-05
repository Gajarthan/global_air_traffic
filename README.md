# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_09:49:21_UTC-green)

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

**Latest saved flight:** 2026-06-05 09:49:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-05 09:49:21 UTC

- **102,750** saved flights
- **36,370** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **102,750** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,254,009.6 tonnes** estimated CO2 emissions
- **72,696,206 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4222 |
| 2 | SkyWest Airlines | 3859 |
| 3 | IndiGo | 2054 |
| 4 | EJA | 1969 |
| 5 | American Airlines | 1659 |
| 6 | Southwest Airlines | 1553 |
| 7 | ENY | 1275 |
| 8 | Delta Air Lines | 1208 |
| 9 | Lufthansa | 1190 |
| 10 | Vueling | 948 |
| 11 | LATAM Airlines | 909 |
| 12 | WIF | 903 |
| 13 | AXM | 885 |
| 14 | AZU | 828 |
| 15 | LXJ | 773 |
| 16 | Swiss International | 741 |
| 17 | All Nippon Airways | 726 |
| 18 | Alaska Airlines | 719 |
| 19 | QLK | 692 |
| 20 | easyJet | 667 |
| 21 | EJU | 643 |
| 22 | Cathay Pacific | 616 |
| 23 | AEE | 598 |
| 24 | VIV | 590 |
| 25 | Air France | 589 |
| 26 | United Airlines | 571 |
| 27 | MXY | 558 |
| 28 | CXK | 552 |
| 29 | Japan Airlines | 511 |
| 30 | AXB | 505 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 86398 |
| 2 | 🇪🇸 ES | 7077 |
| 3 | 🇮🇳 IN | 6492 |
| 4 | 🇦🇺 AU | 6263 |
| 5 | 🇧🇷 BR | 5625 |
| 6 | 🇩🇪 DE | 5520 |
| 7 | 🇮🇹 IT | 5458 |
| 8 | 🇨🇦 CA | 5345 |
| 9 | 🇯🇵 JP | 4744 |
| 10 | 🇬🇧 GB | 4339 |
| 11 | 🇫🇷 FR | 4075 |
| 12 | 🇨🇴 CO | 3538 |
| 13 | 🇲🇽 MX | 3093 |
| 14 | 🇬🇷 GR | 2917 |
| 15 | 🇳🇴 NO | 2858 |
| 16 | 🇨🇭 CH | 2633 |
| 17 | 🇲🇾 MY | 2256 |
| 18 | 🇹🇷 TR | 1946 |
| 19 | 🇿🇦 ZA | 1782 |
| 20 | 🇳🇿 NZ | 1727 |
| 21 | 🇹🇭 TH | 1700 |
| 22 | 🇰🇷 KR | 1675 |
| 23 | 🇵🇱 PL | 1640 |
| 24 | 🇬🇹 GT | 1506 |
| 25 | 🇵🇭 PH | 1502 |
| 26 | 🇲🇦 MA | 1136 |
| 27 | 🇲🇴 MO | 1076 |
| 28 | 🇳🇱 NL | 1016 |
| 29 | 🇲🇪 ME | 968 |
| 30 | 🇭🇷 HR | 902 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2228 |
| 2 | Denver International Airport |  | US | 1759 |
| 3 | Tokyo International Airport |  | JP | 1573 |
| 4 | Indira Gandhi International Airport |  | IN | 1410 |
| 5 | Harry Reid International Airport |  | US | 1318 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1309 |
| 7 | Guaymaral Airport |  | CO | 1284 |
| 8 | Frankfurt am Main International Airport |  | DE | 1190 |
| 9 | Zurich Airport |  | CH | 1169 |
| 10 | La Aurora Airport |  | GT | 1159 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1110 |
| 12 | El Dorado International Airport |  | CO | 1082 |
| 13 | Macau International Airport |  | MO | 1076 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1041 |
| 15 | Chicago O'Hare International Airport |  | US | 1027 |
| 16 | Madrid Barajas International Airport |  | ES | 899 |
| 17 | Kuala Lumpur International Airport |  | MY | 890 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 882 |
| 19 | Salt Lake City International Airport |  | US | 866 |
| 20 | Capua Airport |  | IT | 855 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 799 |
| 22 | Charlotte/Douglas International Airport |  | US | 798 |
| 23 | Charles de Gaulle International Airport |  | FR | 783 |
| 24 | Congonhas Airport |  | BR | 781 |
| 25 | Bengaluru International Airport |  | IN | 777 |
| 26 | Malpensa International Airport |  | IT | 772 |
| 27 | Daniel K Inouye International Airport |  | US | 709 |
| 28 | Tenerife Norte Airport |  | ES | 703 |
| 29 | Ninoy Aquino International Airport |  | PH | 686 |
| 30 | Barcelona International Airport |  | ES | 673 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 666 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 664 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 656 |
| 34 | Amsterdam Airport Schiphol |  | NL | 628 |
| 35 | Don Mueang International Airport |  | TH | 623 |
| 36 | Vitoria/Foronda Airport |  | ES | 621 |
| 37 | Calgary International Airport |  | CA | 607 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 594 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 581 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 530 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 377 | 21m | 244 km | 1,587.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 270 | 24m | 225 km | 1,047.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 250 | 1h 26m | 910 km | 3,923.1 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 248 | 28m | 304 km | 1,300.1 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 236 | 1h 10m | 770 km | 3,135.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 143 | 27m | 152 km | 373.7 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 136 | 20m | 250 km | 587.4 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 133 | 18m | 144 km | 330.8 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 129 | 1h 39m | 1,156 km | 2,573.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 116 | 44m | 241 km | 481.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| 4XCCM |  | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-06-05 09:30 UTC | 2026-06-05 09:49 UTC | 18m |
| PHCBV | PHC | Geneva Cointrin International Airport (LSGG) | Ibiza Airport (LEIB) | 2026-06-05 08:18 UTC | 2026-06-05 09:42 UTC | 1h 23m |
| AEE4319 | AEE | Kuopio Airport (EFKU) | Seduva Airport (EYSE) | 2026-06-05 08:19 UTC | 2026-06-05 09:29 UTC | 1h 9m |
| CAL101 | CAL | Narita International Airport (RJAA) | Hsinchu Air Base (RCPO) | 2026-06-05 06:13 UTC | 2026-06-05 09:21 UTC | 3h 8m |
| N481LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-06-05 08:16 UTC | 2026-06-05 09:19 UTC | 1h 2m |
| RY100T |  | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-06-05 08:30 UTC | 2026-06-05 09:16 UTC | 45m |
| N966JM |  | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Napoli / Capodichino International Airport (LIRN) | 2026-06-05 08:21 UTC | 2026-06-05 09:13 UTC | 51m |
| FD229 |  | Melbourne Essendon Airport (YMEN) | Benalla Airport (YBLA) | 2026-06-05 08:49 UTC | 2026-06-05 09:11 UTC | 21m |
| VLG1AE | Vueling | Menorca Airport (LEMH) | Vitoria/Foronda Airport (LEVT) | 2026-06-05 07:53 UTC | 2026-06-05 09:05 UTC | 1h 12m |
| AEE5C | AEE | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-06-05 08:45 UTC | 2026-06-05 09:05 UTC | 20m |
| WIF824 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-05 08:54 UTC | 2026-06-05 09:04 UTC | 9m |
| EZY48YV | easyJet | Manchester Airport (EGCC) | Madeira Airport (LPMA) | 2026-06-05 05:36 UTC | 2026-06-05 09:02 UTC | 3h 25m |
| HBXCL | HBX | Courchevel Airport (LFLJ) | Courchevel Airport (LFLJ) | 2026-06-05 08:51 UTC | 2026-06-05 09:02 UTC | 11m |
| CHX45 | CHX | St Gallen Altenrhein Airport (LSZR) | Erbach Airport (EDNE) | 2026-06-05 08:35 UTC | 2026-06-05 09:02 UTC | 26m |
| JAL2825 | Japan Airlines | Okadama Airport (RJCO) | Odate Noshiro Airport (RJSR) | 2026-06-05 08:10 UTC | 2026-06-05 09:01 UTC | 50m |
| NOZ2FH | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Sørkjosen Airport (ENSR) | 2026-06-05 07:33 UTC | 2026-06-05 09:01 UTC | 1h 27m |
| WZZ3EA | Wizz Air | Berlin Brandenburg Airport (EDDB) | Stenkovec Brazda Airport (LW75) | 2026-06-05 07:12 UTC | 2026-06-05 09:00 UTC | 1h 47m |
| FDX1426 | FDX | Frederick W Smith International Airport (KMEM) | Austin-Bergstrom International Airport (KAUS) | 2026-06-05 07:36 UTC | 2026-06-05 08:59 UTC | 1h 23m |
| TVS2637 | TVS | Antalya International Airport (LTAI) | Václav Havel Airport (LKPR) | 2026-06-05 06:13 UTC | 2026-06-05 08:58 UTC | 2h 44m |
| WIF6F | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-05 08:43 UTC | 2026-06-05 08:56 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
