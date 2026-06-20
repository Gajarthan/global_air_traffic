# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_01:36:58_UTC-green)

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

**Latest saved flight:** 2026-06-20 01:36:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-20 01:36:58 UTC

- **115,248** saved flights
- **39,953** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **115,248** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,401,474.8 tonnes** estimated CO2 emissions
- **81,244,917 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4748 |
| 2 | SkyWest Airlines | 4295 |
| 3 | EJA | 2237 |
| 4 | IndiGo | 2218 |
| 5 | American Airlines | 1804 |
| 6 | Southwest Airlines | 1715 |
| 7 | ENY | 1435 |
| 8 | Delta Air Lines | 1361 |
| 9 | Lufthansa | 1280 |
| 10 | Vueling | 1040 |
| 11 | WIF | 1022 |
| 12 | LATAM Airlines | 1014 |
| 13 | AZU | 963 |
| 14 | AXM | 952 |
| 15 | LXJ | 876 |
| 16 | Swiss International | 813 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 775 |
| 19 | QLK | 749 |
| 20 | easyJet | 740 |
| 21 | EJU | 723 |
| 22 | Cathay Pacific | 671 |
| 23 | AEE | 646 |
| 24 | United Airlines | 639 |
| 25 | VIV | 635 |
| 26 | Air France | 633 |
| 27 | CXK | 615 |
| 28 | MXY | 611 |
| 29 | AXB | 563 |
| 30 | GLO | 562 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97381 |
| 2 | 🇪🇸 ES | 7857 |
| 3 | 🇮🇳 IN | 7000 |
| 4 | 🇦🇺 AU | 6843 |
| 5 | 🇧🇷 BR | 6354 |
| 6 | 🇮🇹 IT | 6163 |
| 7 | 🇩🇪 DE | 6148 |
| 8 | 🇨🇦 CA | 6069 |
| 9 | 🇯🇵 JP | 5167 |
| 10 | 🇬🇧 GB | 4995 |
| 11 | 🇫🇷 FR | 4572 |
| 12 | 🇨🇴 CO | 3972 |
| 13 | 🇲🇽 MX | 3392 |
| 14 | 🇬🇷 GR | 3280 |
| 15 | 🇳🇴 NO | 3179 |
| 16 | 🇨🇭 CH | 2929 |
| 17 | 🇲🇾 MY | 2464 |
| 18 | 🇹🇷 TR | 2328 |
| 19 | 🇿🇦 ZA | 1945 |
| 20 | 🇳🇿 NZ | 1895 |
| 21 | 🇵🇱 PL | 1886 |
| 22 | 🇰🇷 KR | 1880 |
| 23 | 🇹🇭 TH | 1875 |
| 24 | 🇵🇭 PH | 1671 |
| 25 | 🇬🇹 GT | 1633 |
| 26 | 🇲🇦 MA | 1254 |
| 27 | 🇲🇴 MO | 1168 |
| 28 | 🇲🇪 ME | 1132 |
| 29 | 🇳🇱 NL | 1114 |
| 30 | 🇭🇷 HR | 1000 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2440 |
| 2 | Denver International Airport |  | US | 1951 |
| 3 | Tokyo International Airport |  | JP | 1713 |
| 4 | Indira Gandhi International Airport |  | IN | 1531 |
| 5 | Guaymaral Airport |  | CO | 1470 |
| 6 | Harry Reid International Airport |  | US | 1448 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1413 |
| 8 | Zurich Airport |  | CH | 1284 |
| 9 | La Aurora Airport |  | GT | 1260 |
| 10 | Frankfurt am Main International Airport |  | DE | 1250 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1236 |
| 12 | El Dorado International Airport |  | CO | 1170 |
| 13 | Macau International Airport |  | MO | 1168 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1152 |
| 15 | Chicago O'Hare International Airport |  | US | 1134 |
| 16 | Capua Airport |  | IT | 1001 |
| 17 | Salt Lake City International Airport |  | US | 989 |
| 18 | Madrid Barajas International Airport |  | ES | 984 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 965 |
| 20 | Kuala Lumpur International Airport |  | MY | 954 |
| 21 | Charlotte/Douglas International Airport |  | US | 883 |
| 22 | Congonhas Airport |  | BR | 881 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 859 |
| 24 | Bengaluru International Airport |  | IN | 847 |
| 25 | Charles de Gaulle International Airport |  | FR | 846 |
| 26 | General Edward Lawrence Logan International Airport |  | US | 842 |
| 27 | Malpensa International Airport |  | IT | 823 |
| 28 | Ninoy Aquino International Airport |  | PH | 770 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 755 |
| 30 | Daniel K Inouye International Airport |  | US | 750 |
| 31 | Tenerife Norte Airport |  | ES | 750 |
| 32 | Barcelona International Airport |  | ES | 737 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 723 |
| 34 | Don Mueang International Airport |  | TH | 680 |
| 35 | Calgary International Airport |  | CA | 678 |
| 36 | Vitoria/Foronda Airport |  | ES | 678 |
| 37 | Amsterdam Airport Schiphol |  | NL | 678 |
| 38 | Seattle-Tacoma International Airport |  | US | 665 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Viracopos International Airport |  | BR | 657 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 610 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 416 | 21m | 244 km | 1,751.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 308 | 24m | 225 km | 1,194.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 298 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 285 | 1h 7m | 706 km | 3,469.9 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 282 | 1h 25m | 910 km | 4,425.2 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 275 | 1h 10m | 770 km | 3,653.2 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 230 | 26m | 275 km | 1,089.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 213 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 173 | 22m | 55 km | 164.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 153 | 31m | 369 km | 973.9 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 151 | 44m | 241 km | 627.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 137 | 1h 1m | 695 km | 1,642.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 135 | 1h 43m | 1,423 km | 3,313.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 134 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 130 | 1h 17m | 961 km | 2,154.8 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 128 | 12m | 99 km | 219.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N81BV |  | Mefford Field (KTLR) | Meadows Field (KBFL) | 2026-06-20 00:54 UTC | 2026-06-20 01:36 UTC | 41m |
| AAL2875 | American Airlines | Kansas City International Airport (KMCI) | Brokenstraw Airport (PA55) | 2026-06-19 23:16 UTC | 2026-06-20 01:21 UTC | 2h 4m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-20 01:04 UTC | 2026-06-20 01:20 UTC | 16m |
| TKR140 | TKR | AZ86 (AZ86) | Cottonwood Airport (KP52) | 2026-06-20 01:14 UTC | 2026-06-20 01:14 UTC | 0m |
| YGP | YGP | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-20 00:41 UTC | 2026-06-20 01:10 UTC | 28m |
| IGO541H | IndiGo | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-06-19 23:21 UTC | 2026-06-20 01:08 UTC | 1h 47m |
| NMN | NMN | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-06-19 23:48 UTC | 2026-06-20 01:03 UTC | 1h 14m |
| 8ZY |  | Sydney Bankstown Airport (YSBK) | YSMB (YSMB) | 2026-06-20 00:44 UTC | 2026-06-20 01:00 UTC | 16m |
| N144AL |  | Mineral Wells Regional Airport (KMWL) | Valley Vista Airport (6CA5) | 2026-06-19 22:17 UTC | 2026-06-20 00:59 UTC | 2h 41m |
| N294JY |  | Long Beach (Daugherty Field) Airport (KLGB) | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | 2026-06-20 00:10 UTC | 2026-06-20 00:58 UTC | 47m |
| N805AL |  | Santa Barbara Municipal Airport (KSBA) | San Francisco International Airport (KSFO) | 2026-06-20 00:12 UTC | 2026-06-20 00:57 UTC | 44m |
| KAL1807 | Korean Air | Gimpo International Airport (RKSS) | Gimhae International Airport (RKPK) | 2026-06-20 00:06 UTC | 2026-06-20 00:55 UTC | 49m |
| PFT605 | PFT | Provo Municipal Airport (KPVU) | Scottsdale Airport (KSDL) | 2026-06-19 23:47 UTC | 2026-06-20 00:55 UTC | 1h 7m |
| N315NG |  | Cortez Municipal Airport (KCEZ) | 39AZ (39AZ) | 2026-06-20 00:34 UTC | 2026-06-20 00:53 UTC | 19m |
| N705MJ |  | Hayward Executive Airport (KHWD) | Truckee-Tahoe Airport (KTRK) | 2026-06-20 00:23 UTC | 2026-06-20 00:51 UTC | 28m |
| ERU90 | ERU | Robin Airport (59AZ) | Pilots Rest Airport (AZ57) | 2026-06-20 00:30 UTC | 2026-06-20 00:48 UTC | 17m |
| JBU1152 | JetBlue | General Edward Lawrence Logan International Airport (KBOS) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-20 00:46 UTC | 2026-06-20 00:46 UTC | 0m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-20 00:31 UTC | 2026-06-20 00:45 UTC | 13m |
| N289RT |  | Petaluma Municipal Airport (KO69) | Truckee-Tahoe Airport (KTRK) | 2026-06-20 00:20 UTC | 2026-06-20 00:45 UTC | 24m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-06-19 23:59 UTC | 2026-06-20 00:44 UTC | 45m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
