# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_15:37:49_UTC-green)

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

**Latest saved flight:** 2026-06-04 15:37:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-04 15:37:49 UTC

- **102,112** saved flights
- **36,165** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **102,112** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,247,629.0 tonnes** estimated CO2 emissions
- **72,326,318 km** total distance flown
- **862 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4206 |
| 2 | SkyWest Airlines | 3828 |
| 3 | IndiGo | 2045 |
| 4 | EJA | 1949 |
| 5 | American Airlines | 1646 |
| 6 | Southwest Airlines | 1545 |
| 7 | ENY | 1269 |
| 8 | Delta Air Lines | 1199 |
| 9 | Lufthansa | 1189 |
| 10 | Vueling | 947 |
| 11 | LATAM Airlines | 905 |
| 12 | WIF | 896 |
| 13 | AXM | 881 |
| 14 | AZU | 824 |
| 15 | LXJ | 768 |
| 16 | Swiss International | 741 |
| 17 | All Nippon Airways | 720 |
| 18 | Alaska Airlines | 714 |
| 19 | QLK | 685 |
| 20 | easyJet | 666 |
| 21 | EJU | 642 |
| 22 | Cathay Pacific | 615 |
| 23 | AEE | 592 |
| 24 | VIV | 588 |
| 25 | Air France | 587 |
| 26 | United Airlines | 568 |
| 27 | MXY | 549 |
| 28 | CXK | 548 |
| 29 | Japan Airlines | 509 |
| 30 | AXB | 505 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 85709 |
| 2 | 🇪🇸 ES | 7055 |
| 3 | 🇮🇳 IN | 6472 |
| 4 | 🇦🇺 AU | 6201 |
| 5 | 🇧🇷 BR | 5602 |
| 6 | 🇩🇪 DE | 5502 |
| 7 | 🇮🇹 IT | 5427 |
| 8 | 🇨🇦 CA | 5303 |
| 9 | 🇯🇵 JP | 4709 |
| 10 | 🇬🇧 GB | 4325 |
| 11 | 🇫🇷 FR | 4059 |
| 12 | 🇨🇴 CO | 3534 |
| 13 | 🇲🇽 MX | 3083 |
| 14 | 🇬🇷 GR | 2905 |
| 15 | 🇳🇴 NO | 2843 |
| 16 | 🇨🇭 CH | 2629 |
| 17 | 🇲🇾 MY | 2246 |
| 18 | 🇹🇷 TR | 1934 |
| 19 | 🇿🇦 ZA | 1775 |
| 20 | 🇳🇿 NZ | 1717 |
| 21 | 🇹🇭 TH | 1695 |
| 22 | 🇰🇷 KR | 1658 |
| 23 | 🇵🇱 PL | 1636 |
| 24 | 🇬🇹 GT | 1504 |
| 25 | 🇵🇭 PH | 1497 |
| 26 | 🇲🇦 MA | 1135 |
| 27 | 🇲🇴 MO | 1074 |
| 28 | 🇳🇱 NL | 1013 |
| 29 | 🇲🇪 ME | 966 |
| 30 | 🇭🇷 HR | 901 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2216 |
| 2 | Denver International Airport |  | US | 1744 |
| 3 | Tokyo International Airport |  | JP | 1560 |
| 4 | Indira Gandhi International Airport |  | IN | 1408 |
| 5 | Harry Reid International Airport |  | US | 1308 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1304 |
| 7 | Guaymaral Airport |  | CO | 1282 |
| 8 | Frankfurt am Main International Airport |  | DE | 1189 |
| 9 | Zurich Airport |  | CH | 1169 |
| 10 | La Aurora Airport |  | GT | 1157 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1101 |
| 12 | El Dorado International Airport |  | CO | 1081 |
| 13 | Macau International Airport |  | MO | 1074 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1035 |
| 15 | Chicago O'Hare International Airport |  | US | 1020 |
| 16 | Madrid Barajas International Airport |  | ES | 894 |
| 17 | Kuala Lumpur International Airport |  | MY | 887 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 876 |
| 19 | Salt Lake City International Airport |  | US | 861 |
| 20 | Capua Airport |  | IT | 851 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 794 |
| 22 | Charlotte/Douglas International Airport |  | US | 791 |
| 23 | Charles de Gaulle International Airport |  | FR | 780 |
| 24 | Congonhas Airport |  | BR | 778 |
| 25 | Bengaluru International Airport |  | IN | 773 |
| 26 | Malpensa International Airport |  | IT | 772 |
| 27 | Daniel K Inouye International Airport |  | US | 706 |
| 28 | Tenerife Norte Airport |  | ES | 701 |
| 29 | Ninoy Aquino International Airport |  | PH | 684 |
| 30 | Barcelona International Airport |  | ES | 673 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 665 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 663 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 653 |
| 34 | Amsterdam Airport Schiphol |  | NL | 625 |
| 35 | Don Mueang International Airport |  | TH | 620 |
| 36 | Vitoria/Foronda Airport |  | ES | 620 |
| 37 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 38 | Calgary International Airport |  | CA | 601 |
| 39 | Seattle-Tacoma International Airport |  | US | 590 |
| 40 | John Paul II International Airport Kraków-Balice Airport |  | PL | 575 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 529 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 374 | 21m | 244 km | 1,574.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 269 | 24m | 225 km | 1,043.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 249 | 1h 26m | 910 km | 3,907.4 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 247 | 28m | 304 km | 1,294.8 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 233 | 1h 10m | 770 km | 3,095.2 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 215 | 19m | 165 km | 611.6 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 153 | 22m | 55 km | 145.4 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 143 | 44m | 452 km | 1,114.5 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 142 | 27m | 152 km | 371.1 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 136 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 135 | 20m | 250 km | 583.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 132 | 18m | 144 km | 328.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 131 | 20m | 147 km | 331.5 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 128 | 1h 39m | 1,156 km | 2,553.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 127 | 1h 1m | 695 km | 1,522.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 117 | 12m | - | - |
| 30 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N304PT |  | Ted Stevens Anchorage International Airport (PANC) | Beluga Airport (PABG) | 2026-06-04 15:27 UTC | 2026-06-04 15:37 UTC | 10m |
| WJA613 | WJA | Ottawa / Macdonald-Cartier International Airport (CYOW) | Calgary International Airport (CYYC) | 2026-06-04 11:28 UTC | 2026-06-04 15:37 UTC | 4h 8m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-06-04 15:00 UTC | 2026-06-04 15:33 UTC | 33m |
| DICMD | DIC | Geneva Cointrin International Airport (LSGG) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-04 14:44 UTC | 2026-06-04 15:33 UTC | 48m |
| TCYRZ | TCY | London Biggin Hill Airport (EGKB) | Nice-Cote d'Azur Airport (LFMN) | 2026-06-04 13:51 UTC | 2026-06-04 15:28 UTC | 1h 37m |
| N615JS |  | Warren County/John Lane Field (KI68) | Warren County/John Lane Field (KI68) | 2026-06-04 15:15 UTC | 2026-06-04 15:27 UTC | 12m |
| N684JA |  | Lima Allen County Airport (KAOH) | Fayette County Airport (KI23) | 2026-06-04 14:47 UTC | 2026-06-04 15:27 UTC | 39m |
| SHERPA6 | SHE | Marana Regional Airport (KAVQ) | Marana Regional Airport (KAVQ) | 2026-06-04 15:05 UTC | 2026-06-04 15:27 UTC | 21m |
| HJ437 |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-06-04 14:40 UTC | 2026-06-04 15:26 UTC | 45m |
| N2851G |  | Columbus Airport (KCSG) | Columbus Airport (KCSG) | 2026-06-04 15:15 UTC | 2026-06-04 15:25 UTC | 10m |
| LYRE71 | LYR | Randolph Afb Airport (KRND) | Burris Ranch Airport (2TE6) | 2026-06-04 14:46 UTC | 2026-06-04 15:25 UTC | 39m |
| BURNY01 | BUR | Kickapoo Downtown Airport (KCWC) | Panhandle-Carson County Airport (KT45) | 2026-06-04 14:57 UTC | 2026-06-04 15:24 UTC | 27m |
| N474AK |  | Usaf Academy Davis Airfield (KAFF) | Usaf Academy Davis Airfield (KAFF) | 2026-06-04 15:07 UTC | 2026-06-04 15:21 UTC | 13m |
| N780LA |  | Northeast Philadelphia Airport (KPNE) | Heritage Field (KPTW) | 2026-06-04 14:54 UTC | 2026-06-04 15:18 UTC | 24m |
| N27AF |  | Tulsa International Airport (KTUL) | Lincoln Airport (KLNK) | 2026-06-04 14:23 UTC | 2026-06-04 15:13 UTC | 50m |
| SCA75 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-06-04 15:06 UTC | 2026-06-04 15:12 UTC | 5m |
| FAB3702 | FAB | Fazenda Santa Helena Airport (SDZH) | Fazenda Maristela Airport (SDMA) | 2026-06-04 13:42 UTC | 2026-06-04 15:11 UTC | 1h 28m |
| N737EE |  | Casper/Natrona County International Airport (KCPR) | American Falconry Airport (45WY) | 2026-06-04 14:43 UTC | 2026-06-04 15:09 UTC | 26m |
| N81519 |  | Fuller Airport (TS00) | Fuller Airport (TS00) | 2026-06-04 14:55 UTC | 2026-06-04 15:08 UTC | 13m |
| GECKO77 | GEC | Buie Field (9NR8) | Buie Field (9NR8) | 2026-06-04 14:16 UTC | 2026-06-04 15:08 UTC | 51m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
