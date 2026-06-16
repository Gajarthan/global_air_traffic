# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_23:52:53_UTC-green)

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

**Latest saved flight:** 2026-06-15 23:52:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-15 23:52:53 UTC

- **111,681** saved flights
- **38,930** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **111,681** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,364,981.2 tonnes** estimated CO2 emissions
- **79,129,346 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4602 |
| 2 | SkyWest Airlines | 4185 |
| 3 | IndiGo | 2180 |
| 4 | EJA | 2167 |
| 5 | American Airlines | 1764 |
| 6 | Southwest Airlines | 1671 |
| 7 | ENY | 1395 |
| 8 | Delta Air Lines | 1325 |
| 9 | Lufthansa | 1258 |
| 10 | Vueling | 1023 |
| 11 | LATAM Airlines | 985 |
| 12 | WIF | 985 |
| 13 | AXM | 937 |
| 14 | AZU | 928 |
| 15 | LXJ | 853 |
| 16 | Swiss International | 800 |
| 17 | All Nippon Airways | 776 |
| 18 | Alaska Airlines | 757 |
| 19 | QLK | 732 |
| 20 | easyJet | 720 |
| 21 | EJU | 708 |
| 22 | Cathay Pacific | 662 |
| 23 | AEE | 630 |
| 24 | VIV | 624 |
| 25 | United Airlines | 623 |
| 26 | Air France | 622 |
| 27 | MXY | 596 |
| 28 | CXK | 586 |
| 29 | AXB | 547 |
| 30 | GLO | 547 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 94142 |
| 2 | 🇪🇸 ES | 7650 |
| 3 | 🇮🇳 IN | 6873 |
| 4 | 🇦🇺 AU | 6630 |
| 5 | 🇧🇷 BR | 6173 |
| 6 | 🇮🇹 IT | 6004 |
| 7 | 🇩🇪 DE | 5961 |
| 8 | 🇨🇦 CA | 5877 |
| 9 | 🇯🇵 JP | 5041 |
| 10 | 🇬🇧 GB | 4794 |
| 11 | 🇫🇷 FR | 4447 |
| 12 | 🇨🇴 CO | 3793 |
| 13 | 🇲🇽 MX | 3309 |
| 14 | 🇬🇷 GR | 3172 |
| 15 | 🇳🇴 NO | 3081 |
| 16 | 🇨🇭 CH | 2853 |
| 17 | 🇲🇾 MY | 2420 |
| 18 | 🇹🇷 TR | 2221 |
| 19 | 🇿🇦 ZA | 1895 |
| 20 | 🇰🇷 KR | 1848 |
| 21 | 🇹🇭 TH | 1836 |
| 22 | 🇳🇿 NZ | 1830 |
| 23 | 🇵🇱 PL | 1827 |
| 24 | 🇵🇭 PH | 1627 |
| 25 | 🇬🇹 GT | 1594 |
| 26 | 🇲🇦 MA | 1228 |
| 27 | 🇲🇴 MO | 1154 |
| 28 | 🇲🇪 ME | 1092 |
| 29 | 🇳🇱 NL | 1084 |
| 30 | 🇭🇷 HR | 970 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2385 |
| 2 | Denver International Airport |  | US | 1897 |
| 3 | Tokyo International Airport |  | JP | 1671 |
| 4 | Indira Gandhi International Airport |  | IN | 1494 |
| 5 | Guaymaral Airport |  | CO | 1407 |
| 6 | Harry Reid International Airport |  | US | 1406 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1383 |
| 8 | Zurich Airport |  | CH | 1253 |
| 9 | Frankfurt am Main International Airport |  | DE | 1231 |
| 10 | La Aurora Airport |  | GT | 1226 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1201 |
| 12 | Macau International Airport |  | MO | 1154 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1120 |
| 15 | Chicago O'Hare International Airport |  | US | 1114 |
| 16 | Madrid Barajas International Airport |  | ES | 973 |
| 17 | Capua Airport |  | IT | 968 |
| 18 | Salt Lake City International Airport |  | US | 949 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 942 |
| 20 | Kuala Lumpur International Airport |  | MY | 941 |
| 21 | Charlotte/Douglas International Airport |  | US | 860 |
| 22 | Congonhas Airport |  | BR | 860 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 837 |
| 24 | Charles de Gaulle International Airport |  | FR | 834 |
| 25 | Bengaluru International Airport |  | IN | 829 |
| 26 | Malpensa International Airport |  | IT | 812 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 762 |
| 28 | Ninoy Aquino International Airport |  | PH | 751 |
| 29 | Daniel K Inouye International Airport |  | US | 739 |
| 30 | Tenerife Norte Airport |  | ES | 734 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 729 |
| 32 | Barcelona International Airport |  | ES | 728 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 711 |
| 34 | Don Mueang International Airport |  | TH | 669 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 662 |
| 37 | Calgary International Airport |  | CA | 659 |
| 38 | Norman Y Mineta San Jose International Airport |  | US | 644 |
| 39 | Seattle-Tacoma International Airport |  | US | 643 |
| 40 | Viracopos International Airport |  | BR | 635 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 407 | 21m | 244 km | 1,713.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 297 | 24m | 225 km | 1,152.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 288 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 262 | 1h 10m | 770 km | 3,480.5 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 224 | 26m | 275 km | 1,061.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 162 | 27m | 215 km | 600.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 160 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 151 | 31m | 369 km | 961.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 148 | 44m | 452 km | 1,153.4 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 143 | 20m | 250 km | 617.7 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 142 | 44m | 241 km | 589.8 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 134 | 1h 1m | 695 km | 1,606.3 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 125 | 1h 17m | 961 km | 2,071.9 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DRAGO06 | DRA | A 511 Airport (RKSG) | RKRS (RKRS) | 2026-06-15 23:27 UTC | 2026-06-15 23:52 UTC | 25m |
| SWR52 | Swiss International | Zurich Airport (LSZH) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-15 16:08 UTC | 2026-06-15 23:52 UTC | 7h 44m |
| N945G |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-06-15 23:14 UTC | 2026-06-15 23:52 UTC | 38m |
| CXK416 | CXK | Ogden-Hinckley Airport (KOGD) | Wendover Airport (KENV) | 2026-06-15 22:41 UTC | 2026-06-15 23:48 UTC | 1h 6m |
| N360ES |  | Centennial Airport (KAPA) | Bijou Bottom Strip (9CO8) | 2026-06-15 23:17 UTC | 2026-06-15 23:46 UTC | 29m |
| DLH420 | Lufthansa | Frankfurt am Main International Airport (EDDF) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-15 15:58 UTC | 2026-06-15 23:41 UTC | 7h 43m |
| N229HT |  | Bear Valley Airport (73CA) | Bear Valley Airport (73CA) | 2026-06-15 23:29 UTC | 2026-06-15 23:40 UTC | 11m |
| N322VR |  | Abraham Lincoln Capital Airport (KSPI) | Abraham Lincoln Capital Airport (KSPI) | 2026-06-15 23:26 UTC | 2026-06-15 23:40 UTC | 13m |
| TKR107 | TKR | Roberts Field (KRDM) | Wasco State Airport (K35S) | 2026-06-15 23:22 UTC | 2026-06-15 23:38 UTC | 16m |
| N32101 |  | Warren County/John Lane Field (KI68) | Warren County/John Lane Field (KI68) | 2026-06-15 23:23 UTC | 2026-06-15 23:34 UTC | 11m |
| TKR184 | TKR | Crystal Airport (46CN) | San Bernardino International Airport (KSBD) | 2026-06-15 23:09 UTC | 2026-06-15 23:32 UTC | 22m |
| EJA866 | EJA | Teterboro Airport (KTEB) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-15 22:53 UTC | 2026-06-15 23:30 UTC | 37m |
| TKR136 | TKR | Roberts Field (KRDM) | Mac Field (1OR5) | 2026-06-15 23:06 UTC | 2026-06-15 23:29 UTC | 22m |
| N13AL |  | Whittier Airport (PAWR) | Valdez Pioneer Field (PAVD) | 2026-06-15 23:05 UTC | 2026-06-15 23:28 UTC | 23m |
| N757MK |  | Oakland County International Airport (KPTK) | Prices Airport (K9G2) | 2026-06-15 22:52 UTC | 2026-06-15 23:26 UTC | 34m |
| N862DP |  | John C Tune Airport (KJWN) | Springfield Robertson County Airport (KM91) | 2026-06-15 23:02 UTC | 2026-06-15 23:25 UTC | 23m |
| PNC0995 | PNC | El Dorado International Airport (SKBO) | El Dorado International Airport (SKBO) | 2026-06-15 22:53 UTC | 2026-06-15 23:25 UTC | 32m |
| ES806 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-06-15 22:39 UTC | 2026-06-15 23:24 UTC | 45m |
| CAP4274 | CAP | KWSD (KWSD) | KWSD (KWSD) | 2026-06-15 22:34 UTC | 2026-06-15 23:20 UTC | 45m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-06-15 22:38 UTC | 2026-06-15 23:19 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
