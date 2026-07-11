# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_23:56:25_UTC-green)

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

**Latest saved flight:** 2026-07-10 23:56:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-10 23:56:25 UTC

- **136,350** saved flights
- **46,051** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **136,350** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,638,666.4 tonnes** estimated CO2 emissions
- **94,995,155 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5516 |
| 2 | SkyWest Airlines | 5013 |
| 3 | EJA | 2679 |
| 4 | IndiGo | 2510 |
| 5 | American Airlines | 2147 |
| 6 | Southwest Airlines | 2060 |
| 7 | ENY | 1715 |
| 8 | Delta Air Lines | 1628 |
| 9 | Lufthansa | 1398 |
| 10 | LATAM Airlines | 1252 |
| 11 | Vueling | 1183 |
| 12 | WIF | 1181 |
| 13 | AZU | 1171 |
| 14 | LXJ | 1051 |
| 15 | AXM | 1028 |
| 16 | Swiss International | 967 |
| 17 | All Nippon Airways | 885 |
| 18 | easyJet | 880 |
| 19 | Alaska Airlines | 862 |
| 20 | QLK | 853 |
| 21 | EJU | 834 |
| 22 | VIV | 747 |
| 23 | AEE | 736 |
| 24 | CXK | 729 |
| 25 | Air France | 727 |
| 26 | Cathay Pacific | 726 |
| 27 | United Airlines | 718 |
| 28 | JetBlue | 717 |
| 29 | MXY | 709 |
| 30 | GLO | 696 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 117297 |
| 2 | 🇪🇸 ES | 8986 |
| 3 | 🇮🇳 IN | 7875 |
| 4 | 🇦🇺 AU | 7841 |
| 5 | 🇧🇷 BR | 7694 |
| 6 | 🇨🇦 CA | 7213 |
| 7 | 🇩🇪 DE | 7089 |
| 8 | 🇮🇹 IT | 7052 |
| 9 | 🇬🇧 GB | 6156 |
| 10 | 🇯🇵 JP | 5780 |
| 11 | 🇫🇷 FR | 5398 |
| 12 | 🇨🇴 CO | 4284 |
| 13 | 🇲🇽 MX | 3962 |
| 14 | 🇬🇷 GR | 3868 |
| 15 | 🇳🇴 NO | 3683 |
| 16 | 🇨🇭 CH | 3519 |
| 17 | 🇹🇷 TR | 3125 |
| 18 | 🇲🇾 MY | 2670 |
| 19 | 🇵🇱 PL | 2254 |
| 20 | 🇿🇦 ZA | 2241 |
| 21 | 🇳🇿 NZ | 2119 |
| 22 | 🇹🇭 TH | 2071 |
| 23 | 🇰🇷 KR | 1993 |
| 24 | 🇵🇭 PH | 1869 |
| 25 | 🇬🇹 GT | 1834 |
| 26 | 🇲🇦 MA | 1432 |
| 27 | 🇲🇪 ME | 1350 |
| 28 | 🇳🇱 NL | 1266 |
| 29 | 🇭🇷 HR | 1214 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2843 |
| 2 | Denver International Airport |  | US | 2288 |
| 3 | Tokyo International Airport |  | JP | 1888 |
| 4 | Indira Gandhi International Airport |  | IN | 1740 |
| 5 | Harry Reid International Airport |  | US | 1711 |
| 6 | Guaymaral Airport |  | CO | 1654 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1584 |
| 8 | Zurich Airport |  | CH | 1512 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1446 |
| 10 | La Aurora Airport |  | GT | 1417 |
| 11 | Frankfurt am Main International Airport |  | DE | 1352 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1311 |
| 13 | Chicago O'Hare International Airport |  | US | 1293 |
| 14 | El Dorado International Airport |  | CO | 1214 |
| 15 | Salt Lake City International Airport |  | US | 1212 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1179 |
| 18 | Madrid Barajas International Airport |  | ES | 1109 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1107 |
| 20 | Capua Airport |  | IT | 1105 |
| 21 | Congonhas Airport |  | BR | 1093 |
| 22 | Kuala Lumpur International Airport |  | MY | 1036 |
| 23 | Charlotte/Douglas International Airport |  | US | 1000 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 986 |
| 25 | Charles de Gaulle International Airport |  | FR | 970 |
| 26 | Bengaluru International Airport |  | IN | 946 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 939 |
| 28 | Malpensa International Airport |  | IT | 893 |
| 29 | Ninoy Aquino International Airport |  | PH | 870 |
| 30 | Daniel K Inouye International Airport |  | US | 841 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 832 |
| 32 | Barcelona International Airport |  | ES | 832 |
| 33 | Tenerife Norte Airport |  | ES | 811 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 806 |
| 35 | Calgary International Airport |  | CA | 797 |
| 36 | Scottsdale Airport |  | US | 784 |
| 37 | Viracopos International Airport |  | BR | 780 |
| 38 | Seattle-Tacoma International Airport |  | US | 780 |
| 39 | Vitoria/Foronda Airport |  | ES | 770 |
| 40 | Amsterdam Airport Schiphol |  | NL | 759 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 696 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 492 | 21m | 244 km | 2,071.7 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 339 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 335 | 24m | 225 km | 1,299.6 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 326 | 1h 10m | 770 km | 4,330.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 292 | 14m | 114 km | 572.7 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 255 | 26m | 275 km | 1,208.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 247 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 201 | 22m | 55 km | 191.0 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 188 | 26m | 215 km | 696.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 183 | 1h 46m | 1,423 km | 4,491.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 168 | 31m | 369 km | 1,069.4 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 167 | 20m | 250 km | 721.3 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 164 | 30m | 49 km | 138.6 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 162 | 44m | 452 km | 1,262.6 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 156 | 1h 38m | 1,156 km | 3,112.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N230AM |  | French Valley Airport (KF70) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-07-10 23:31 UTC | 2026-07-10 23:56 UTC | 24m |
| N3824S |  | Roppair Airport (OR22) | Roppair Airport (OR22) | 2026-07-10 23:15 UTC | 2026-07-10 23:55 UTC | 39m |
| HLE60 | HLE | Redhill Aerodrome (EGKR) | Redhill Aerodrome (EGKR) | 2026-07-10 23:44 UTC | 2026-07-10 23:54 UTC | 10m |
| N955PT |  | Miami Executive Airport (KTMB) | Mjd Airport (FL31) | 2026-07-10 23:30 UTC | 2026-07-10 23:52 UTC | 22m |
| WMU81 | WMU | MI56 (MI56) | MI56 (MI56) | 2026-07-10 23:27 UTC | 2026-07-10 23:50 UTC | 23m |
| WJA645 | WJA | Toronto Pearson International Airport (CYYZ) | Calgary International Airport (CYYC) | 2026-07-10 20:07 UTC | 2026-07-10 23:50 UTC | 3h 43m |
| AAL2076 | American Airlines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-10 02:49 UTC | 2026-07-10 23:50 UTC | 21h 1m |
| N82BH |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-10 22:32 UTC | 2026-07-10 23:49 UTC | 1h 17m |
| FFT2970 | FFT | Dallas-Fort Worth International Airport (KDFW) | Philadelphia International Airport (KPHL) | 2026-07-10 20:58 UTC | 2026-07-10 23:48 UTC | 2h 50m |
| BRG622 | BRG | Ralph Wien Memorial Airport (PAOT) | Ambler Airport (PAFM) | 2026-07-10 23:02 UTC | 2026-07-10 23:47 UTC | 44m |
| N628SR |  | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-07-10 23:07 UTC | 2026-07-10 23:47 UTC | 39m |
| CFTWC | CFT | Calgary / Springbank Airport (CYBW) | Banff Airport (CYBA) | 2026-07-10 23:15 UTC | 2026-07-10 23:45 UTC | 30m |
| N77NG |  | Montgomery-Gibbs Executive Airport (KMYF) | 8CL0 (8CL0) | 2026-07-10 23:05 UTC | 2026-07-10 23:37 UTC | 31m |
| N205FG |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-07-10 23:24 UTC | 2026-07-10 23:35 UTC | 11m |
| N28PK |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-07-10 23:14 UTC | 2026-07-10 23:33 UTC | 19m |
| TIGER11 | TIG | Kaneohe Bay Mcas (Marion E Carl Field) Airport (PHNG) | Kaneohe Bay Mcas (Marion E Carl Field) Airport (PHNG) | 2026-07-10 22:54 UTC | 2026-07-10 23:28 UTC | 34m |
| RPA4685 | Republic Airways | Laguardia Airport (KLGA) | Philadelphia International Airport (KPHL) | 2026-07-10 21:31 UTC | 2026-07-10 23:26 UTC | 1h 54m |
| TKR104 | TKR | San Bernardino International Airport (KSBD) | San Bernardino International Airport (KSBD) | 2026-07-10 22:57 UTC | 2026-07-10 23:24 UTC | 27m |
| TKR107 | TKR | Animas Air Park (K00C) | Animas Air Park (K00C) | 2026-07-10 22:55 UTC | 2026-07-10 23:21 UTC | 26m |
| LRS6794 | LRS | Juan Santamaria International Airport (MROC) | Atirro Airport (MRAR) | 2026-07-10 23:04 UTC | 2026-07-10 23:17 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
