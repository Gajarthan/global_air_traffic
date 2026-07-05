# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_15:35:51_UTC-green)

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

**Latest saved flight:** 2026-07-05 15:35:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 15:35:51 UTC

- **129,772** saved flights
- **44,132** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **129,772** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,566,186.3 tonnes** estimated CO2 emissions
- **90,793,407 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5285 |
| 2 | SkyWest Airlines | 4801 |
| 3 | EJA | 2537 |
| 4 | IndiGo | 2438 |
| 5 | American Airlines | 2000 |
| 6 | Southwest Airlines | 1949 |
| 7 | ENY | 1629 |
| 8 | Delta Air Lines | 1554 |
| 9 | Lufthansa | 1365 |
| 10 | LATAM Airlines | 1183 |
| 11 | Vueling | 1152 |
| 12 | WIF | 1137 |
| 13 | AZU | 1104 |
| 14 | AXM | 1009 |
| 15 | LXJ | 1001 |
| 16 | Swiss International | 908 |
| 17 | All Nippon Airways | 860 |
| 18 | Alaska Airlines | 835 |
| 19 | easyJet | 829 |
| 20 | QLK | 816 |
| 21 | EJU | 803 |
| 22 | VIV | 719 |
| 23 | Cathay Pacific | 713 |
| 24 | AEE | 707 |
| 25 | Air France | 705 |
| 26 | CXK | 696 |
| 27 | United Airlines | 691 |
| 28 | JetBlue | 677 |
| 29 | MXY | 677 |
| 30 | GLO | 662 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 110958 |
| 2 | 🇪🇸 ES | 8660 |
| 3 | 🇮🇳 IN | 7641 |
| 4 | 🇦🇺 AU | 7519 |
| 5 | 🇧🇷 BR | 7295 |
| 6 | 🇨🇦 CA | 6842 |
| 7 | 🇩🇪 DE | 6821 |
| 8 | 🇮🇹 IT | 6792 |
| 9 | 🇬🇧 GB | 5769 |
| 10 | 🇯🇵 JP | 5624 |
| 11 | 🇫🇷 FR | 5169 |
| 12 | 🇨🇴 CO | 4092 |
| 13 | 🇲🇽 MX | 3788 |
| 14 | 🇬🇷 GR | 3704 |
| 15 | 🇳🇴 NO | 3531 |
| 16 | 🇨🇭 CH | 3338 |
| 17 | 🇹🇷 TR | 2847 |
| 18 | 🇲🇾 MY | 2616 |
| 19 | 🇿🇦 ZA | 2153 |
| 20 | 🇵🇱 PL | 2135 |
| 21 | 🇳🇿 NZ | 2080 |
| 22 | 🇹🇭 TH | 2014 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1813 |
| 25 | 🇬🇹 GT | 1768 |
| 26 | 🇲🇦 MA | 1389 |
| 27 | 🇲🇪 ME | 1288 |
| 28 | 🇳🇱 NL | 1219 |
| 29 | 🇲🇴 MO | 1185 |
| 30 | 🇭🇷 HR | 1137 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2704 |
| 2 | Denver International Airport |  | US | 2201 |
| 3 | Tokyo International Airport |  | JP | 1851 |
| 4 | Indira Gandhi International Airport |  | IN | 1687 |
| 5 | Harry Reid International Airport |  | US | 1612 |
| 6 | Guaymaral Airport |  | CO | 1579 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1537 |
| 8 | Zurich Airport |  | CH | 1431 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1379 |
| 10 | La Aurora Airport |  | GT | 1368 |
| 11 | Frankfurt am Main International Airport |  | DE | 1321 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1259 |
| 13 | Chicago O'Hare International Airport |  | US | 1243 |
| 14 | Macau International Airport |  | MO | 1185 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1153 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1092 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1067 |
| 19 | Capua Airport |  | IT | 1067 |
| 20 | Madrid Barajas International Airport |  | ES | 1066 |
| 21 | Congonhas Airport |  | BR | 1029 |
| 22 | Kuala Lumpur International Airport |  | MY | 1015 |
| 23 | Charlotte/Douglas International Airport |  | US | 969 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 950 |
| 25 | Charles de Gaulle International Airport |  | FR | 941 |
| 26 | Bengaluru International Airport |  | IN | 924 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 879 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 841 |
| 30 | Daniel K Inouye International Airport |  | US | 816 |
| 31 | Barcelona International Airport |  | ES | 806 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 793 |
| 33 | Tenerife Norte Airport |  | ES | 786 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 760 |
| 35 | Calgary International Airport |  | CA | 754 |
| 36 | Vitoria/Foronda Airport |  | ES | 749 |
| 37 | Seattle-Tacoma International Airport |  | US | 747 |
| 38 | Viracopos International Airport |  | BR | 744 |
| 39 | Scottsdale Airport |  | US | 744 |
| 40 | Amsterdam Airport Schiphol |  | NL | 736 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 662 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 469 | 21m | 244 km | 1,974.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 326 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 315 | 1h 10m | 770 km | 4,184.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 240 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 182 | 44m | 241 km | 756.0 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 173 | 27m | 152 km | 452.1 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 168 | 1h 45m | 1,423 km | 4,123.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 159 | 20m | 250 km | 686.8 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 159 | 18m | 144 km | 395.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 150 | 1h 16m | 961 km | 2,486.3 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 150 | 54m | 136 km | 351.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VAR850 | VAR | Phoenix Goodyear Airport (KGYR) | Bishop Airfield (1AZ0) | 2026-07-05 15:18 UTC | 2026-07-05 15:35 UTC | 17m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-07-05 15:19 UTC | 2026-07-05 15:31 UTC | 11m |
|  |  | Blairstown Airport (K1N7) | Blairstown Airport (K1N7) | 2026-07-05 15:18 UTC | 2026-07-05 15:28 UTC | 10m |
| N806JA |  | Port Colborne Airport (CPE5) | Port Colborne Airport (CPE5) | 2026-07-05 14:08 UTC | 2026-07-05 15:27 UTC | 1h 18m |
| 00000000 |  | Salt Lake City International Airport (KSLC) | Telluride Regional Airport (KTEX) | 2026-07-05 14:35 UTC | 2026-07-05 15:23 UTC | 48m |
| OKPMP | OKP | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Mauterndorf Airport (LOSM) | 2026-07-05 14:15 UTC | 2026-07-05 15:22 UTC | 1h 6m |
| N625DW |  | Northeast Philadelphia Airport (KPNE) | Millville Municipal Airport (KMIV) | 2026-07-05 14:50 UTC | 2026-07-05 15:22 UTC | 31m |
| CXK181 | CXK | Martin State Airport (KMTN) | Martin State Airport (KMTN) | 2026-07-05 15:11 UTC | 2026-07-05 15:22 UTC | 11m |
| N250EX |  | Dekalb-Peachtree Airport (KPDK) | Villa Char Mar Airport (1FA9) | 2026-07-05 14:11 UTC | 2026-07-05 15:17 UTC | 1h 5m |
| N487LP |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-05 14:16 UTC | 2026-07-05 15:14 UTC | 57m |
| ERU64 | ERU | Parsons Field (4AZ6) | Lake Havasu City Airport (KHII) | 2026-07-05 14:43 UTC | 2026-07-05 15:13 UTC | 30m |
| N32004 |  | Flying Cloud Airport (KFCM) | Flying Cloud Airport (KFCM) | 2026-07-05 15:00 UTC | 2026-07-05 15:13 UTC | 13m |
| OXF4756 | OXF | Falcon Field (KFFZ) | Rancho San Marcos Airport (74AZ) | 2026-07-05 13:42 UTC | 2026-07-05 15:12 UTC | 1h 29m |
| SWR15Y | Swiss International | Melsbroek Air Base (EBMB) | Zurich Airport (LSZH) | 2026-07-05 14:18 UTC | 2026-07-05 15:11 UTC | 53m |
| N253EA |  | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 2026-07-05 14:12 UTC | 2026-07-05 15:08 UTC | 56m |
| N722UE |  | North Las Vegas Airport (KVGT) | Caas Airport (NV98) | 2026-07-05 14:51 UTC | 2026-07-05 15:08 UTC | 16m |
| N846AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-07-05 14:55 UTC | 2026-07-05 15:08 UTC | 12m |
| N80866 |  | Albuquerque International Sunport Airport (KABQ) | Skywagon Farm Airport (NM88) | 2026-07-05 14:38 UTC | 2026-07-05 15:08 UTC | 29m |
| ASI96 | ASI | Phoenix Deer Valley Airport (KDVT) | Gila Bend Municipal Airport (KE63) | 2026-07-05 14:17 UTC | 2026-07-05 15:06 UTC | 49m |
| JKY039 | JKY | Oxford (Kidlington) Airport (EGTK) | Turweston Airport (EGBT) | 2026-07-05 14:44 UTC | 2026-07-05 15:06 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
