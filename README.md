# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_04:06:55_UTC-green)

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

**Latest saved flight:** 2026-07-02 04:06:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-02 04:06:55 UTC

- **126,407** saved flights
- **43,178** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **126,407** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,524,309.9 tonnes** estimated CO2 emissions
- **88,365,793 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5124 |
| 2 | SkyWest Airlines | 4674 |
| 3 | EJA | 2488 |
| 4 | IndiGo | 2393 |
| 5 | American Airlines | 1947 |
| 6 | Southwest Airlines | 1894 |
| 7 | ENY | 1589 |
| 8 | Delta Air Lines | 1510 |
| 9 | Lufthansa | 1347 |
| 10 | LATAM Airlines | 1148 |
| 11 | Vueling | 1120 |
| 12 | WIF | 1112 |
| 13 | AZU | 1069 |
| 14 | AXM | 999 |
| 15 | LXJ | 984 |
| 16 | Swiss International | 879 |
| 17 | All Nippon Airways | 849 |
| 18 | Alaska Airlines | 822 |
| 19 | easyJet | 807 |
| 20 | QLK | 794 |
| 21 | EJU | 782 |
| 22 | Cathay Pacific | 699 |
| 23 | AEE | 694 |
| 24 | VIV | 692 |
| 25 | Air France | 688 |
| 26 | CXK | 678 |
| 27 | United Airlines | 671 |
| 28 | MXY | 658 |
| 29 | JetBlue | 649 |
| 30 | GLO | 638 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 108201 |
| 2 | 🇪🇸 ES | 8426 |
| 3 | 🇮🇳 IN | 7505 |
| 4 | 🇦🇺 AU | 7375 |
| 5 | 🇧🇷 BR | 7068 |
| 6 | 🇩🇪 DE | 6659 |
| 7 | 🇨🇦 CA | 6656 |
| 8 | 🇮🇹 IT | 6632 |
| 9 | 🇬🇧 GB | 5575 |
| 10 | 🇯🇵 JP | 5525 |
| 11 | 🇫🇷 FR | 4980 |
| 12 | 🇨🇴 CO | 4046 |
| 13 | 🇲🇽 MX | 3671 |
| 14 | 🇬🇷 GR | 3594 |
| 15 | 🇳🇴 NO | 3453 |
| 16 | 🇨🇭 CH | 3205 |
| 17 | 🇹🇷 TR | 2659 |
| 18 | 🇲🇾 MY | 2584 |
| 19 | 🇿🇦 ZA | 2081 |
| 20 | 🇵🇱 PL | 2068 |
| 21 | 🇳🇿 NZ | 2043 |
| 22 | 🇹🇭 TH | 1974 |
| 23 | 🇰🇷 KR | 1950 |
| 24 | 🇵🇭 PH | 1788 |
| 25 | 🇬🇹 GT | 1740 |
| 26 | 🇲🇦 MA | 1355 |
| 27 | 🇲🇪 ME | 1251 |
| 28 | 🇳🇱 NL | 1189 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1094 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2650 |
| 2 | Denver International Airport |  | US | 2132 |
| 3 | Tokyo International Airport |  | JP | 1826 |
| 4 | Indira Gandhi International Airport |  | IN | 1650 |
| 5 | Harry Reid International Airport |  | US | 1582 |
| 6 | Guaymaral Airport |  | CO | 1533 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1506 |
| 8 | Zurich Airport |  | CH | 1392 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1349 |
| 10 | La Aurora Airport |  | GT | 1344 |
| 11 | Frankfurt am Main International Airport |  | DE | 1302 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1237 |
| 13 | Chicago O'Hare International Airport |  | US | 1221 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1115 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1049 |
| 19 | Madrid Barajas International Airport |  | ES | 1041 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1034 |
| 21 | Kuala Lumpur International Airport |  | MY | 1006 |
| 22 | Congonhas Airport |  | BR | 992 |
| 23 | Charlotte/Douglas International Airport |  | US | 951 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 929 |
| 25 | Charles de Gaulle International Airport |  | FR | 917 |
| 26 | Bengaluru International Airport |  | IN | 906 |
| 27 | Malpensa International Airport |  | IT | 865 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 845 |
| 29 | Ninoy Aquino International Airport |  | PH | 828 |
| 30 | Daniel K Inouye International Airport |  | US | 805 |
| 31 | Barcelona International Airport |  | ES | 790 |
| 32 | Tenerife Norte Airport |  | ES | 774 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 768 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 742 |
| 35 | Calgary International Airport |  | CA | 740 |
| 36 | Seattle-Tacoma International Airport |  | US | 732 |
| 37 | Scottsdale Airport |  | US | 731 |
| 38 | Vitoria/Foronda Airport |  | ES | 724 |
| 39 | Viracopos International Airport |  | BR | 721 |
| 40 | Amsterdam Airport Schiphol |  | NL | 718 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 639 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 460 | 21m | 244 km | 1,936.9 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 326 | 24m | 225 km | 1,264.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 317 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 304 | 1h 10m | 770 km | 4,038.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 234 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 187 | 22m | 55 km | 177.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 174 | 44m | 241 km | 722.8 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 162 | 1h 45m | 1,423 km | 3,975.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 160 | 31m | 369 km | 1,018.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 149 | 30m | 49 km | 125.9 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 147 | 1h 1m | 695 km | 1,762.1 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 146 | 1h 17m | 961 km | 2,420.0 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 140 | 54m | 136 km | 328.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GFA560 | Gulf Air | Al Ahsa Airport (OEAH) | Al Ain International Airport (OMAL) | 2026-07-01 23:08 UTC | 2026-07-02 04:06 UTC | 4h 58m |
| J999KT |  | Adi Sutjipto International Airport (WARJ) | Gading Wonosari Airport (WI1G) | 2026-07-02 03:19 UTC | 2026-07-02 04:05 UTC | 45m |
| YKB | YKB | Cessnock Airport (YCNK) | Tamworth Airport (YSTW) | 2026-07-02 03:02 UTC | 2026-07-02 04:01 UTC | 58m |
| PIKES40 | PIK | Buckley Space Force Base Airport (KBKF) | Buckley Space Force Base Airport (KBKF) | 2026-07-02 03:37 UTC | 2026-07-02 04:01 UTC | 23m |
| N23NP |  | Henderson Executive Airport (KHND) | North Las Vegas Airport (KVGT) | 2026-07-02 03:24 UTC | 2026-07-02 03:59 UTC | 34m |
| FLC94 | FLC | Ted Stevens Anchorage International Airport (PANC) | Elmendorf Afb Airport (PAED) | 2026-07-01 23:56 UTC | 2026-07-02 03:57 UTC | 4h 1m |
| JBU392 | JetBlue | Tampa International Airport (KTPA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-02 01:08 UTC | 2026-07-02 03:49 UTC | 2h 40m |
| DAL2801 | Delta Air Lines | Laguardia Airport (KLGA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-02 03:01 UTC | 2026-07-02 03:45 UTC | 43m |
| N4323F |  | Ocean City Municipal Airport (KOXB) | Harford County Airport (K0W3) | 2026-07-02 02:20 UTC | 2026-07-02 03:43 UTC | 1h 22m |
| OUA38 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Haskell Airport (K2K9) | 2026-07-02 02:59 UTC | 2026-07-02 03:42 UTC | 43m |
| N779AM |  | Mc Clellan-Palomar Airport (KCRQ) | Lake Tahoe Airport (KTVL) | 2026-07-02 02:08 UTC | 2026-07-02 03:40 UTC | 1h 32m |
| N303JD |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-07-02 03:01 UTC | 2026-07-02 03:39 UTC | 37m |
| J932KT |  | Gading Wonosari Airport (WI1G) | Gading Wonosari Airport (WI1G) | 2026-07-02 03:31 UTC | 2026-07-02 03:36 UTC | 4m |
| N500EH |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-07-02 02:14 UTC | 2026-07-02 03:31 UTC | 1h 17m |
| EFC35B | EFC | Al Maktoum International Airport (OMDW) | OM11 (OM11) | 2026-07-02 02:26 UTC | 2026-07-02 03:25 UTC | 59m |
| HRP | HRP | Bathurst Airport (YBTH) | Sydney Bankstown Airport (YSBK) | 2026-07-02 03:02 UTC | 2026-07-02 03:25 UTC | 22m |
| N636KT |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-07-02 02:33 UTC | 2026-07-02 03:25 UTC | 51m |
| N255DP |  | Phoenix Sky Harbor International Airport (KPHX) | Phoenix Goodyear Airport (KGYR) | 2026-07-02 02:13 UTC | 2026-07-02 03:23 UTC | 1h 9m |
| N565TA |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-02 02:34 UTC | 2026-07-02 03:22 UTC | 48m |
| N29LJ |  | Portland International Airport (KPDX) | South Fork Ranch Airport (0ID0) | 2026-07-02 02:32 UTC | 2026-07-02 03:19 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
