# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_15:50:16_UTC-green)

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

**Latest saved flight:** 2026-06-14 15:50:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 15:50:16 UTC

- **110,112** saved flights
- **38,421** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **110,112** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,345,939.5 tonnes** estimated CO2 emissions
- **78,025,476 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4547 |
| 2 | SkyWest Airlines | 4111 |
| 3 | IndiGo | 2172 |
| 4 | EJA | 2110 |
| 5 | American Airlines | 1736 |
| 6 | Southwest Airlines | 1647 |
| 7 | ENY | 1367 |
| 8 | Delta Air Lines | 1299 |
| 9 | Lufthansa | 1251 |
| 10 | Vueling | 1009 |
| 11 | LATAM Airlines | 973 |
| 12 | WIF | 971 |
| 13 | AXM | 933 |
| 14 | AZU | 908 |
| 15 | LXJ | 831 |
| 16 | Swiss International | 795 |
| 17 | All Nippon Airways | 769 |
| 18 | Alaska Airlines | 750 |
| 19 | QLK | 726 |
| 20 | easyJet | 709 |
| 21 | EJU | 702 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 624 |
| 24 | VIV | 619 |
| 25 | Air France | 618 |
| 26 | United Airlines | 607 |
| 27 | MXY | 586 |
| 28 | CXK | 577 |
| 29 | AXB | 544 |
| 30 | Japan Airlines | 542 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92450 |
| 2 | 🇪🇸 ES | 7570 |
| 3 | 🇮🇳 IN | 6847 |
| 4 | 🇦🇺 AU | 6567 |
| 5 | 🇧🇷 BR | 6067 |
| 6 | 🇮🇹 IT | 5925 |
| 7 | 🇩🇪 DE | 5911 |
| 8 | 🇨🇦 CA | 5758 |
| 9 | 🇯🇵 JP | 5015 |
| 10 | 🇬🇧 GB | 4717 |
| 11 | 🇫🇷 FR | 4413 |
| 12 | 🇨🇴 CO | 3761 |
| 13 | 🇲🇽 MX | 3269 |
| 14 | 🇬🇷 GR | 3141 |
| 15 | 🇳🇴 NO | 3053 |
| 16 | 🇨🇭 CH | 2828 |
| 17 | 🇲🇾 MY | 2409 |
| 18 | 🇹🇷 TR | 2170 |
| 19 | 🇿🇦 ZA | 1885 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1826 |
| 22 | 🇵🇱 PL | 1812 |
| 23 | 🇳🇿 NZ | 1807 |
| 24 | 🇵🇭 PH | 1611 |
| 25 | 🇬🇹 GT | 1572 |
| 26 | 🇲🇦 MA | 1213 |
| 27 | 🇲🇴 MO | 1149 |
| 28 | 🇳🇱 NL | 1083 |
| 29 | 🇲🇪 ME | 1077 |
| 30 | 🇭🇷 HR | 960 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2354 |
| 2 | Denver International Airport |  | US | 1861 |
| 3 | Tokyo International Airport |  | JP | 1661 |
| 4 | Indira Gandhi International Airport |  | IN | 1488 |
| 5 | Guaymaral Airport |  | CO | 1395 |
| 6 | Harry Reid International Airport |  | US | 1389 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1375 |
| 8 | Zurich Airport |  | CH | 1243 |
| 9 | Frankfurt am Main International Airport |  | DE | 1226 |
| 10 | La Aurora Airport |  | GT | 1209 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1175 |
| 12 | Macau International Airport |  | MO | 1149 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1098 |
| 15 | Chicago O'Hare International Airport |  | US | 1089 |
| 16 | Madrid Barajas International Airport |  | ES | 964 |
| 17 | Capua Airport |  | IT | 951 |
| 18 | Kuala Lumpur International Airport |  | MY | 940 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 931 |
| 20 | Salt Lake City International Airport |  | US | 928 |
| 21 | Charlotte/Douglas International Airport |  | US | 846 |
| 22 | Congonhas Airport |  | BR | 842 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Bengaluru International Airport |  | IN | 828 |
| 25 | Charles de Gaulle International Airport |  | FR | 827 |
| 26 | Malpensa International Airport |  | IT | 803 |
| 27 | Ninoy Aquino International Airport |  | PH | 742 |
| 28 | General Edward Lawrence Logan International Airport |  | US | 737 |
| 29 | Daniel K Inouye International Airport |  | US | 735 |
| 30 | Tenerife Norte Airport |  | ES | 730 |
| 31 | Barcelona International Airport |  | ES | 721 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 716 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 702 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 652 |
| 37 | Calgary International Airport |  | CA | 649 |
| 38 | Seattle-Tacoma International Airport |  | US | 631 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 630 |
| 40 | Viracopos International Airport |  | BR | 621 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 578 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 403 | 21m | 244 km | 1,696.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 284 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 220 | 26m | 275 km | 1,042.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 163 | 20m | 99 km | 279.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 159 | 27m | 215 km | 588.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 156 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 144 | 18m | 144 km | 358.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 137 | 44m | 241 km | 569.1 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 131 | 1h 43m | 1,423 km | 3,214.9 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 123 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 122 | 24m | 223 km | 469.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N602JH |  | Sunrise Dusters Airport (CA18) | Sunrise Dusters Airport (CA18) | 2026-06-14 15:07 UTC | 2026-06-14 15:50 UTC | 43m |
| N7DW |  | Ocean City Municipal Airport (KOXB) | Ocean City Municipal Airport (KOXB) | 2026-06-14 15:41 UTC | 2026-06-14 15:48 UTC | 6m |
| ELY383 | ELY | Ben Gurion International Airport (LLBG) | Queen Alia International Airport (OJAI) | 2026-06-14 15:35 UTC | 2026-06-14 15:46 UTC | 11m |
| N321DZ |  | Arthur Dunn Air Park (KX21) | Arthur Dunn Air Park (KX21) | 2026-06-14 14:40 UTC | 2026-06-14 15:46 UTC | 1h 5m |
| N76JK |  | Harvey's Acres Airport (OR28) | Portland-Hillsboro Airport (KHIO) | 2026-06-14 15:36 UTC | 2026-06-14 15:46 UTC | 10m |
| UAE110 | Emirates | Luqa Airport (LMML) | Queen Alia International Airport (OJAI) | 2026-06-14 13:54 UTC | 2026-06-14 15:44 UTC | 1h 49m |
| N724GT |  | Treasure Coast International Airport (KFPR) | Orlando Executive Airport (KORL) | 2026-06-14 15:14 UTC | 2026-06-14 15:39 UTC | 25m |
| N531SJ |  | City Of Colorado Springs Municipal Airport (KCOS) | Rocky Mountain Metro Airport (KBJC) | 2026-06-14 15:00 UTC | 2026-06-14 15:37 UTC | 37m |
| ELY222 | ELY | Charles de Gaulle International Airport (LFPG) | Queen Alia International Airport (OJAI) | 2026-06-14 12:13 UTC | 2026-06-14 15:37 UTC | 3h 24m |
| MEA253 | Middle East Airlines | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-06-14 15:17 UTC | 2026-06-14 15:32 UTC | 15m |
| FXC33 | FXC | North Canaan Aviation Facilities Inc Airport (CT24) | Francis S Gabreski Airport (KFOK) | 2026-06-14 14:57 UTC | 2026-06-14 15:31 UTC | 34m |
| N300KT |  | Nephi Municipal Airport (KU14) | Nephi Municipal Airport (KU14) | 2026-06-14 15:14 UTC | 2026-06-14 15:28 UTC | 13m |
| AAL1416 | American Airlines | Philadelphia International Airport (KPHL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-14 14:32 UTC | 2026-06-14 15:26 UTC | 53m |
|  |  | Lamezia Terme Airport (LICA) | Trapani / Birgi Airport (LICT) | 2026-06-14 14:20 UTC | 2026-06-14 15:25 UTC | 1h 4m |
| IAW109 | IAW | Queen Alia International Airport (OJAI) | Queen Alia International Airport (OJAI) | 2026-06-14 15:07 UTC | 2026-06-14 15:24 UTC | 17m |
| FENIX71 | FEN | KWSD (KWSD) | Holloman Afb Airport (KHMN) | 2026-06-14 15:05 UTC | 2026-06-14 15:23 UTC | 18m |
| N723AJ |  | KU42 (KU42) | Logan-Cache Airport (KLGU) | 2026-06-14 14:27 UTC | 2026-06-14 15:21 UTC | 53m |
| N475RC |  | Rimrock Airport (48AZ) | Payson Airport (KPAN) | 2026-06-14 15:01 UTC | 2026-06-14 15:20 UTC | 19m |
| N292VF |  | Mono Aircraft Airport (0KS7) | Mono Aircraft Airport (0KS7) | 2026-06-14 15:09 UTC | 2026-06-14 15:19 UTC | 10m |
| LNX06AR | LNX | Genova / Sestri Cristoforo Colombo Airport (LIMJ) | Birmingham International Airport (EGBB) | 2026-06-14 13:20 UTC | 2026-06-14 15:18 UTC | 1h 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
