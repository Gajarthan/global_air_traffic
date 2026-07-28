# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_05:45:15_UTC-green)

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

**Latest saved flight:** 2026-07-28 05:45:15 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-28 05:45:15 UTC

- **155,927** saved flights
- **51,859** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **155,927** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,870,948.1 tonnes** estimated CO2 emissions
- **108,460,761 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6264 |
| 2 | SkyWest Airlines | 5725 |
| 3 | EJA | 3095 |
| 4 | IndiGo | 2759 |
| 5 | American Airlines | 2491 |
| 6 | Southwest Airlines | 2458 |
| 7 | ENY | 1950 |
| 8 | Delta Air Lines | 1859 |
| 9 | Lufthansa | 1501 |
| 10 | LATAM Airlines | 1454 |
| 11 | AZU | 1365 |
| 12 | WIF | 1313 |
| 13 | Vueling | 1303 |
| 14 | LXJ | 1198 |
| 15 | AXM | 1099 |
| 16 | Swiss International | 1083 |
| 17 | easyJet | 1014 |
| 18 | Alaska Airlines | 979 |
| 19 | All Nippon Airways | 971 |
| 20 | QLK | 971 |
| 21 | EJU | 956 |
| 22 | VIV | 858 |
| 23 | United Airlines | 836 |
| 24 | CXK | 826 |
| 25 | GLO | 816 |
| 26 | MXY | 815 |
| 27 | AEE | 814 |
| 28 | JetBlue | 812 |
| 29 | Cathay Pacific | 811 |
| 30 | Air France | 807 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 134788 |
| 2 | 🇪🇸 ES | 10020 |
| 3 | 🇧🇷 BR | 8899 |
| 4 | 🇦🇺 AU | 8823 |
| 5 | 🇮🇳 IN | 8671 |
| 6 | 🇨🇦 CA | 8405 |
| 7 | 🇮🇹 IT | 8032 |
| 8 | 🇩🇪 DE | 7907 |
| 9 | 🇬🇧 GB | 7141 |
| 10 | 🇯🇵 JP | 6395 |
| 11 | 🇫🇷 FR | 6147 |
| 12 | 🇨🇴 CO | 5409 |
| 13 | 🇲🇽 MX | 4479 |
| 14 | 🇬🇷 GR | 4429 |
| 15 | 🇳🇴 NO | 4110 |
| 16 | 🇨🇭 CH | 4060 |
| 17 | 🇹🇷 TR | 3719 |
| 18 | 🇲🇾 MY | 2865 |
| 19 | 🇵🇱 PL | 2650 |
| 20 | 🇿🇦 ZA | 2511 |
| 21 | 🇳🇿 NZ | 2325 |
| 22 | 🇹🇭 TH | 2241 |
| 23 | 🇰🇷 KR | 2089 |
| 24 | 🇵🇭 PH | 2056 |
| 25 | 🇬🇹 GT | 2012 |
| 26 | 🇲🇦 MA | 1587 |
| 27 | 🇲🇪 ME | 1510 |
| 28 | 🇭🇷 HR | 1431 |
| 29 | 🇳🇱 NL | 1424 |
| 30 | 🇲🇴 MO | 1284 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3211 |
| 2 | Denver International Airport |  | US | 2624 |
| 3 | Tokyo International Airport |  | JP | 2027 |
| 4 | Guaymaral Airport |  | CO | 1955 |
| 5 | Indira Gandhi International Airport |  | IN | 1924 |
| 6 | Harry Reid International Airport |  | US | 1917 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1729 |
| 8 | Zurich Airport |  | CH | 1681 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1636 |
| 10 | La Aurora Airport |  | GT | 1559 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1453 |
| 12 | Frankfurt am Main International Airport |  | DE | 1450 |
| 13 | Chicago O'Hare International Airport |  | US | 1422 |
| 14 | Salt Lake City International Airport |  | US | 1409 |
| 15 | El Dorado International Airport |  | CO | 1409 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1320 |
| 17 | Macau International Airport |  | MO | 1284 |
| 18 | Congonhas Airport |  | BR | 1273 |
| 19 | Madrid Barajas International Airport |  | ES | 1235 |
| 20 | Capua Airport |  | IT | 1229 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1200 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1123 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1109 |
| 24 | Charlotte/Douglas International Airport |  | US | 1106 |
| 25 | Kuala Lumpur International Airport |  | MY | 1097 |
| 26 | Charles de Gaulle International Airport |  | FR | 1064 |
| 27 | Bengaluru International Airport |  | IN | 1033 |
| 28 | Malpensa International Airport |  | IT | 1018 |
| 29 | Ninoy Aquino International Airport |  | PH | 964 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 950 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 944 |
| 32 | Barcelona International Airport |  | ES | 924 |
| 33 | Daniel K Inouye International Airport |  | US | 923 |
| 34 | Seattle-Tacoma International Airport |  | US | 911 |
| 35 | Calgary International Airport |  | CA | 894 |
| 36 | Tenerife Norte Airport |  | ES | 891 |
| 37 | Viracopos International Airport |  | BR | 886 |
| 38 | Scottsdale Airport |  | US | 883 |
| 39 | Amsterdam Airport Schiphol |  | NL | 862 |
| 40 | Oslo Gardermoen Airport |  | NO | 854 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 821 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 562 | 21m | 244 km | 2,366.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 376 | 24m | 225 km | 1,458.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 374 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 360 | 1h 9m | 770 km | 4,782.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 287 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 231 | 22m | 55 km | 219.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 214 | 44m | 241 km | 888.9 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 208 | 1h 47m | 1,423 km | 5,104.6 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 204 | 26m | 215 km | 755.5 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 200 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 196 | 20m | 250 km | 846.6 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 188 | 27m | 152 km | 491.3 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 184 | 1h 15m | 961 km | 3,049.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 183 | 18m | 144 km | 455.2 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 182 | 31m | 369 km | 1,158.5 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 181 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 176 | 44m | 452 km | 1,371.7 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 176 | 50m | 556 km | 1,687.1 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 175 | 1h 39m | 1,156 km | 3,491.2 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 173 | 1h 1m | 695 km | 2,073.8 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 50m | 1,304 km | 3,712.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N929TG |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-07-28 05:20 UTC | 2026-07-28 05:45 UTC | 24m |
| DLH899 | Lufthansa | Vilnius International Airport (EYVI) | Frankfurt am Main International Airport (EDDF) | 2026-07-28 03:38 UTC | 2026-07-28 05:25 UTC | 1h 47m |
| DLH885 | Lufthansa | Tallinn Airport (EETN) | Frankfurt am Main International Airport (EDDF) | 2026-07-28 03:18 UTC | 2026-07-28 05:18 UTC | 2h 0m |
| RYR7SN | Ryanair | Riga International Airport (EVRA) | Memmingen Allgau Airport (EDJA) | 2026-07-28 03:16 UTC | 2026-07-28 05:18 UTC | 2h 1m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bombala Airport (YBOM) | 2026-07-28 04:31 UTC | 2026-07-28 05:12 UTC | 41m |
| EJU859L | EJU | Nice-Cote d'Azur Airport (LFMN) | Ecuvillens Airport (LSGE) | 2026-07-28 04:08 UTC | 2026-07-28 05:03 UTC | 54m |
| UN34 |  | Muan International Airport (RKJB) | G 710 Airport (RK6D) | 2026-07-28 04:54 UTC | 2026-07-28 05:02 UTC | 8m |
| UBG143 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-07-28 04:17 UTC | 2026-07-28 04:56 UTC | 38m |
| AXM6490 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-07-28 04:36 UTC | 2026-07-28 04:50 UTC | 14m |
| VAR503 | VAR | Phoenix Goodyear Airport (KGYR) | Western Sky Airpark (0AZ2) | 2026-07-28 04:06 UTC | 2026-07-28 04:50 UTC | 44m |
|  |  | Lanseria Airport (FALA) | Vanderbijlpark Airport (FAVP) | 2026-07-28 04:38 UTC | 2026-07-28 04:49 UTC | 11m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-07-28 04:29 UTC | 2026-07-28 04:49 UTC | 19m |
| A6FHD |  | Al Bateen Executive Airport (OMAD) | Das Island Airport (OMAS) | 2026-07-28 03:39 UTC | 2026-07-28 04:47 UTC | 1h 8m |
| CEB903 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-28 04:23 UTC | 2026-07-28 04:46 UTC | 23m |
| FVS331 | FVS | Al Bateen Executive Airport (OMAD) | Ras Al Khaimah International Airport (OMRK) | 2026-07-28 04:05 UTC | 2026-07-28 04:46 UTC | 41m |
| WIF6PC | WIF | Bodø Airport (ENBO) | Hemavan Airport (ESUT) | 2026-07-28 04:42 UTC | 2026-07-28 04:46 UTC | 4m |
| N248TA |  | KU42 (KU42) | Nephi Municipal Airport (KU14) | 2026-07-28 04:17 UTC | 2026-07-28 04:45 UTC | 27m |
| HGB308 | HGB | Chek Lap Kok International Airport (VHHH) | Iki Airport (RJDB) | 2026-07-28 01:35 UTC | 2026-07-28 04:44 UTC | 3h 8m |
| SEH1CF | SEH | Eleftherios Venizelos International Airport (LGAV) | Aktion National Airport (LGPZ) | 2026-07-28 03:50 UTC | 2026-07-28 04:43 UTC | 52m |
| VLG78PR | Vueling | Alicante International Airport (LEAL) | DAAX (DAAX) | 2026-07-28 04:07 UTC | 2026-07-28 04:41 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
