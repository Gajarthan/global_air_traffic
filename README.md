# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_21:38:05_UTC-green)

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

**Latest saved flight:** 2026-07-16 21:38:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-16 21:38:05 UTC

- **142,090** saved flights
- **47,682** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **142,090** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,705,090.4 tonnes** estimated CO2 emissions
- **98,845,819 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5776 |
| 2 | SkyWest Airlines | 5193 |
| 3 | EJA | 2797 |
| 4 | IndiGo | 2595 |
| 5 | American Airlines | 2267 |
| 6 | Southwest Airlines | 2141 |
| 7 | ENY | 1760 |
| 8 | Delta Air Lines | 1682 |
| 9 | Lufthansa | 1434 |
| 10 | LATAM Airlines | 1305 |
| 11 | Vueling | 1221 |
| 12 | AZU | 1219 |
| 13 | WIF | 1216 |
| 14 | LXJ | 1093 |
| 15 | AXM | 1053 |
| 16 | Swiss International | 1011 |
| 17 | easyJet | 923 |
| 18 | All Nippon Airways | 912 |
| 19 | Alaska Airlines | 896 |
| 20 | QLK | 894 |
| 21 | EJU | 876 |
| 22 | VIV | 789 |
| 23 | AEE | 759 |
| 24 | JetBlue | 759 |
| 25 | CXK | 758 |
| 26 | Air France | 755 |
| 27 | United Airlines | 740 |
| 28 | Cathay Pacific | 735 |
| 29 | MXY | 735 |
| 30 | GLO | 728 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 122217 |
| 2 | 🇪🇸 ES | 9266 |
| 3 | 🇦🇺 AU | 8152 |
| 4 | 🇮🇳 IN | 8130 |
| 5 | 🇧🇷 BR | 8013 |
| 6 | 🇨🇦 CA | 7480 |
| 7 | 🇮🇹 IT | 7405 |
| 8 | 🇩🇪 DE | 7373 |
| 9 | 🇬🇧 GB | 6478 |
| 10 | 🇯🇵 JP | 5966 |
| 11 | 🇫🇷 FR | 5644 |
| 12 | 🇨🇴 CO | 4530 |
| 13 | 🇲🇽 MX | 4124 |
| 14 | 🇬🇷 GR | 4042 |
| 15 | 🇳🇴 NO | 3805 |
| 16 | 🇨🇭 CH | 3674 |
| 17 | 🇹🇷 TR | 3359 |
| 18 | 🇲🇾 MY | 2747 |
| 19 | 🇵🇱 PL | 2379 |
| 20 | 🇿🇦 ZA | 2320 |
| 21 | 🇳🇿 NZ | 2182 |
| 22 | 🇹🇭 TH | 2123 |
| 23 | 🇰🇷 KR | 2026 |
| 24 | 🇵🇭 PH | 1924 |
| 25 | 🇬🇹 GT | 1867 |
| 26 | 🇲🇦 MA | 1488 |
| 27 | 🇲🇪 ME | 1407 |
| 28 | 🇳🇱 NL | 1337 |
| 29 | 🇭🇷 HR | 1291 |
| 30 | 🇲🇴 MO | 1191 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2922 |
| 2 | Denver International Airport |  | US | 2377 |
| 3 | Tokyo International Airport |  | JP | 1925 |
| 4 | Indira Gandhi International Airport |  | IN | 1802 |
| 5 | Harry Reid International Airport |  | US | 1785 |
| 6 | Guaymaral Airport |  | CO | 1729 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1628 |
| 8 | Zurich Airport |  | CH | 1579 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1489 |
| 10 | La Aurora Airport |  | GT | 1444 |
| 11 | Frankfurt am Main International Airport |  | DE | 1382 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1349 |
| 13 | Chicago O'Hare International Airport |  | US | 1329 |
| 14 | Salt Lake City International Airport |  | US | 1271 |
| 15 | El Dorado International Airport |  | CO | 1255 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1249 |
| 17 | Macau International Airport |  | MO | 1191 |
| 18 | Capua Airport |  | IT | 1164 |
| 19 | Madrid Barajas International Airport |  | ES | 1144 |
| 20 | Congonhas Airport |  | BR | 1140 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1129 |
| 22 | Kuala Lumpur International Airport |  | MY | 1060 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1034 |
| 24 | Charlotte/Douglas International Airport |  | US | 1028 |
| 25 | Charles de Gaulle International Airport |  | FR | 1000 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 991 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 919 |
| 29 | Ninoy Aquino International Airport |  | PH | 898 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 870 |
| 31 | Daniel K Inouye International Airport |  | US | 868 |
| 32 | Barcelona International Airport |  | ES | 864 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 840 |
| 34 | Tenerife Norte Airport |  | ES | 820 |
| 35 | Calgary International Airport |  | CA | 811 |
| 36 | Seattle-Tacoma International Airport |  | US | 806 |
| 37 | Amsterdam Airport Schiphol |  | NL | 805 |
| 38 | Viracopos International Airport |  | BR | 803 |
| 39 | Scottsdale Airport |  | US | 803 |
| 40 | Vitoria/Foronda Airport |  | ES | 782 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 728 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 518 | 21m | 244 km | 2,181.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 345 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 336 | 1h 9m | 770 km | 4,463.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 208 | 22m | 55 km | 197.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 191 | 1h 46m | 1,423 km | 4,687.4 t |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 189 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 189 | 20m | 99 km | 323.7 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 177 | 28m | 152 km | 462.6 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 172 | 31m | 369 km | 1,094.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 171 | 18m | 144 km | 425.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 167 | 44m | 452 km | 1,301.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 164 | 1h 1m | 695 km | 1,965.9 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 164 | 1h 16m | 961 km | 2,718.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 159 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N139ME |  | Moore County Airport (KSOP) | Reed Mine Airport (5NC3) | 2026-07-16 21:02 UTC | 2026-07-16 21:38 UTC | 35m |
| N447BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-07-16 21:06 UTC | 2026-07-16 21:37 UTC | 31m |
| ZKNZO | ZKN | Queenstown International Airport (NZQN) | Queenstown International Airport (NZQN) | 2026-07-16 21:26 UTC | 2026-07-16 21:36 UTC | 10m |
| N815GY |  | Mc Clellan-Palomar Airport (KCRQ) | Oakland San Francisco Bay Airport (KOAK) | 2026-07-16 20:37 UTC | 2026-07-16 21:35 UTC | 57m |
| N9100H |  | Warren "Bud" Woods Palmer Municipal Airport (PAAQ) | Merrill Field (PAMR) | 2026-07-16 20:50 UTC | 2026-07-16 21:33 UTC | 42m |
| SKW4149 | SkyWest Airlines | Seattle-Tacoma International Airport (KSEA) | Mahlon Sweet Field (KEUG) | 2026-07-16 20:46 UTC | 2026-07-16 21:32 UTC | 45m |
| AAL745 | American Airlines | Copenhagen Kastrup Airport (EKCH) | Philadelphia International Airport (KPHL) | 2026-07-16 13:41 UTC | 2026-07-16 21:27 UTC | 7h 46m |
| N822SA |  | Mc Clellan-Palomar Airport (KCRQ) | Ramona Airport (KRNM) | 2026-07-16 20:39 UTC | 2026-07-16 21:21 UTC | 41m |
| SLH909 | SLH | Lewis University Airport (KLOT) | Lincoln Airport (KLNK) | 2026-07-16 20:10 UTC | 2026-07-16 21:19 UTC | 1h 8m |
| TEXN089 | TEX | Five Oaks Estate Airport (FD03) | South Alabama Regional At Bill Benton Field (K79J) | 2026-07-16 20:46 UTC | 2026-07-16 21:16 UTC | 29m |
| N895CA |  | Hector International Airport (KFAR) | Cold Meadows Usfs Airport (KU81) | 2026-07-16 19:21 UTC | 2026-07-16 21:15 UTC | 1h 54m |
| N3118Y |  | KU77 (KU77) | Nephi Municipal Airport (KU14) | 2026-07-16 20:58 UTC | 2026-07-16 21:15 UTC | 17m |
| CXK382 | CXK | Long Beach (Daugherty Field) Airport (KLGB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-07-16 20:19 UTC | 2026-07-16 21:14 UTC | 54m |
| N7814 |  | Camarillo Airport (KCMA) | SN28 (SN28) | 2026-07-16 18:16 UTC | 2026-07-16 21:13 UTC | 2h 56m |
| SWR8CM | Swiss International | Amsterdam Airport Schiphol (EHAM) | Zurich Airport (LSZH) | 2026-07-16 20:00 UTC | 2026-07-16 21:12 UTC | 1h 11m |
| WSN4 | WSN | Albuquerque International Sunport Airport (KABQ) | Taos Regional Airport (KSKX) | 2026-07-16 20:42 UTC | 2026-07-16 21:12 UTC | 29m |
| N459M |  | Edmonton International Airport (CYEG) | MY13 (MY13) | 2026-07-16 19:23 UTC | 2026-07-16 21:11 UTC | 1h 48m |
| AAL2633 | American Airlines | Sacramento International Airport (KSMF) | Dallas-Fort Worth International Airport (KDFW) | 2026-07-16 18:10 UTC | 2026-07-16 21:10 UTC | 3h 0m |
| JANET27 | JAN | Harry Reid International Airport (KLAS) | NV11 (NV11) | 2026-07-16 20:53 UTC | 2026-07-16 21:10 UTC | 17m |
| SAVER27 | SAV | Liberty Field (7AL5) | Liberty Field (7AL5) | 2026-07-16 20:22 UTC | 2026-07-16 21:09 UTC | 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
