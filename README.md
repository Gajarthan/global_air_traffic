# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_23:03:33_UTC-green)

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

**Latest saved flight:** 2026-07-05 23:03:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 23:03:33 UTC

- **130,562** saved flights
- **44,406** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **130,562** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,575,376.4 tonnes** estimated CO2 emissions
- **91,326,168 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5310 |
| 2 | SkyWest Airlines | 4840 |
| 3 | EJA | 2560 |
| 4 | IndiGo | 2443 |
| 5 | American Airlines | 2025 |
| 6 | Southwest Airlines | 1969 |
| 7 | ENY | 1644 |
| 8 | Delta Air Lines | 1568 |
| 9 | Lufthansa | 1368 |
| 10 | LATAM Airlines | 1196 |
| 11 | Vueling | 1154 |
| 12 | WIF | 1138 |
| 13 | AZU | 1111 |
| 14 | LXJ | 1010 |
| 15 | AXM | 1009 |
| 16 | Swiss International | 910 |
| 17 | All Nippon Airways | 860 |
| 18 | Alaska Airlines | 837 |
| 19 | easyJet | 837 |
| 20 | QLK | 817 |
| 21 | EJU | 805 |
| 22 | VIV | 723 |
| 23 | Cathay Pacific | 713 |
| 24 | Air France | 709 |
| 25 | AEE | 708 |
| 26 | CXK | 697 |
| 27 | United Airlines | 695 |
| 28 | JetBlue | 684 |
| 29 | MXY | 682 |
| 30 | GLO | 670 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 111906 |
| 2 | 🇪🇸 ES | 8695 |
| 3 | 🇮🇳 IN | 7654 |
| 4 | 🇦🇺 AU | 7527 |
| 5 | 🇧🇷 BR | 7358 |
| 6 | 🇨🇦 CA | 6896 |
| 7 | 🇩🇪 DE | 6847 |
| 8 | 🇮🇹 IT | 6820 |
| 9 | 🇬🇧 GB | 5802 |
| 10 | 🇯🇵 JP | 5624 |
| 11 | 🇫🇷 FR | 5187 |
| 12 | 🇨🇴 CO | 4102 |
| 13 | 🇲🇽 MX | 3816 |
| 14 | 🇬🇷 GR | 3722 |
| 15 | 🇳🇴 NO | 3538 |
| 16 | 🇨🇭 CH | 3350 |
| 17 | 🇹🇷 TR | 2883 |
| 18 | 🇲🇾 MY | 2616 |
| 19 | 🇿🇦 ZA | 2159 |
| 20 | 🇵🇱 PL | 2144 |
| 21 | 🇳🇿 NZ | 2080 |
| 22 | 🇹🇭 TH | 2014 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1815 |
| 25 | 🇬🇹 GT | 1779 |
| 26 | 🇲🇦 MA | 1394 |
| 27 | 🇲🇪 ME | 1295 |
| 28 | 🇳🇱 NL | 1226 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1144 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2731 |
| 2 | Denver International Airport |  | US | 2216 |
| 3 | Tokyo International Airport |  | JP | 1851 |
| 4 | Indira Gandhi International Airport |  | IN | 1690 |
| 5 | Harry Reid International Airport |  | US | 1627 |
| 6 | Guaymaral Airport |  | CO | 1587 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1539 |
| 8 | Zurich Airport |  | CH | 1438 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1393 |
| 10 | La Aurora Airport |  | GT | 1376 |
| 11 | Frankfurt am Main International Airport |  | DE | 1324 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1265 |
| 13 | Chicago O'Hare International Airport |  | US | 1256 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1162 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1111 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1073 |
| 19 | Madrid Barajas International Airport |  | ES | 1070 |
| 20 | Capua Airport |  | IT | 1069 |
| 21 | Congonhas Airport |  | BR | 1039 |
| 22 | Kuala Lumpur International Airport |  | MY | 1015 |
| 23 | Charlotte/Douglas International Airport |  | US | 974 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 950 |
| 25 | Charles de Gaulle International Airport |  | FR | 945 |
| 26 | Bengaluru International Airport |  | IN | 926 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 888 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 842 |
| 30 | Daniel K Inouye International Airport |  | US | 820 |
| 31 | Barcelona International Airport |  | ES | 809 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 795 |
| 33 | Tenerife Norte Airport |  | ES | 792 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 769 |
| 35 | Calgary International Airport |  | CA | 764 |
| 36 | Seattle-Tacoma International Airport |  | US | 754 |
| 37 | Vitoria/Foronda Airport |  | ES | 750 |
| 38 | Viracopos International Airport |  | BR | 749 |
| 39 | Scottsdale Airport |  | US | 747 |
| 40 | Amsterdam Airport Schiphol |  | NL | 742 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 666 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 473 | 21m | 244 km | 1,991.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 328 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 315 | 1h 10m | 770 km | 4,184.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 240 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 190 | 22m | 55 km | 180.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 183 | 44m | 241 km | 760.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 174 | 27m | 152 km | 454.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 169 | 1h 45m | 1,423 km | 4,147.5 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 164 | 31m | 369 km | 1,043.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 160 | 20m | 250 km | 691.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 160 | 18m | 144 km | 398.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 157 | 30m | 49 km | 132.7 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 154 | 1h 16m | 961 km | 2,552.6 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 150 | 54m | 136 km | 351.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 146 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N52654 |  | Merrill Field (PAMR) | Birchwood Airport (PABV) | 2026-07-05 22:31 UTC | 2026-07-05 23:03 UTC | 31m |
| AAL204 | American Airlines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-05 22:44 UTC | 2026-07-05 22:54 UTC | 9m |
| N742GJ |  | Buchanan Field (KCCR) | Truckee-Tahoe Airport (KTRK) | 2026-07-05 22:05 UTC | 2026-07-05 22:52 UTC | 47m |
| AAL1100 | American Airlines | Dallas-Fort Worth International Airport (KDFW) | Philadelphia International Airport (KPHL) | 2026-07-05 20:06 UTC | 2026-07-05 22:51 UTC | 2h 45m |
| N915TT |  | Lake Elmo Airport (K21D) | Lake Elmo Airport (K21D) | 2026-07-05 22:25 UTC | 2026-07-05 22:51 UTC | 25m |
| TRP1 | TRP | Martin State Airport (KMTN) | Claremont Airport (K58M) | 2026-07-05 22:29 UTC | 2026-07-05 22:44 UTC | 15m |
| N55029 |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-05 22:23 UTC | 2026-07-05 22:41 UTC | 18m |
| TKR137 | TKR | Grant County International Airport (KMWH) | Carr Airport (6WA6) | 2026-07-05 22:30 UTC | 2026-07-05 22:41 UTC | 10m |
| FFT7048 | FFT | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-05 20:33 UTC | 2026-07-05 22:34 UTC | 2h 1m |
| N975SC |  | Scribner State Airport (KSCB) | Lincoln Airport (KLNK) | 2026-07-05 22:08 UTC | 2026-07-05 22:33 UTC | 24m |
| LXJ600 | LXJ | Norman Y Mineta San Jose International Airport (KSJC) | Van Nuys Airport (KVNY) | 2026-07-05 21:45 UTC | 2026-07-05 22:32 UTC | 47m |
| AAL1776 | American Airlines | Philadelphia International Airport (KPHL) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-05 21:45 UTC | 2026-07-05 22:29 UTC | 43m |
| N3413X |  | Scotts Airport (0AK0) | Blair Lake Airport (2AK1) | 2026-07-05 22:13 UTC | 2026-07-05 22:28 UTC | 14m |
| AAL2722 | American Airlines | San Francisco International Airport (KSFO) | Philadelphia International Airport (KPHL) | 2026-07-05 17:20 UTC | 2026-07-05 22:21 UTC | 5h 0m |
| N508SF |  | Smith Field (KSLG) | Morrilton Airport (07AR) | 2026-07-05 22:04 UTC | 2026-07-05 22:21 UTC | 16m |
| N435HC |  | John Wayne/Orange County Airport (KSNA) | Sequoia Field (KD86) | 2026-07-05 21:47 UTC | 2026-07-05 22:20 UTC | 32m |
| N50GP |  | Redding Regional Airport (KRDD) | Pine Hollow Airport (32OR) | 2026-07-05 21:37 UTC | 2026-07-05 22:17 UTC | 40m |
| N456PF |  | Miami Executive Airport (KTMB) | South Bimini Airport (MYBS) | 2026-07-05 21:57 UTC | 2026-07-05 22:16 UTC | 19m |
| N61696 |  | Petaluma Municipal Airport (KO69) | Petaluma Municipal Airport (KO69) | 2026-07-05 21:44 UTC | 2026-07-05 22:14 UTC | 29m |
| N704MF |  | Van Nuys Airport (KVNY) | Truckee-Tahoe Airport (KTRK) | 2026-07-05 21:29 UTC | 2026-07-05 22:11 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
