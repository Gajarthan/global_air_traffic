# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_19:34:07_UTC-green)

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

**Latest saved flight:** 2026-08-01 19:34:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 19:34:07 UTC

- **165,393** saved flights
- **54,297** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **165,393** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,988,780.1 tonnes** estimated CO2 emissions
- **115,291,597 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6603 |
| 2 | SkyWest Airlines | 6023 |
| 3 | EJA | 3287 |
| 4 | IndiGo | 2912 |
| 5 | American Airlines | 2604 |
| 6 | Southwest Airlines | 2597 |
| 7 | ENY | 2055 |
| 8 | Delta Air Lines | 1973 |
| 9 | LATAM Airlines | 1541 |
| 10 | Lufthansa | 1537 |
| 11 | AZU | 1450 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1366 |
| 14 | LXJ | 1285 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1133 |
| 17 | easyJet | 1089 |
| 18 | Alaska Airlines | 1019 |
| 19 | EJU | 1013 |
| 20 | QLK | 1011 |
| 21 | All Nippon Airways | 1009 |
| 22 | VIV | 911 |
| 23 | CXK | 885 |
| 24 | Cathay Pacific | 879 |
| 25 | United Airlines | 871 |
| 26 | AEE | 870 |
| 27 | GLO | 866 |
| 28 | Air France | 854 |
| 29 | MXY | 853 |
| 30 | JetBlue | 839 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 142808 |
| 2 | 🇪🇸 ES | 10581 |
| 3 | 🇧🇷 BR | 9421 |
| 4 | 🇦🇺 AU | 9259 |
| 5 | 🇮🇳 IN | 9136 |
| 6 | 🇨🇦 CA | 8986 |
| 7 | 🇮🇹 IT | 8546 |
| 8 | 🇩🇪 DE | 8283 |
| 9 | 🇬🇧 GB | 7610 |
| 10 | 🇯🇵 JP | 6660 |
| 11 | 🇫🇷 FR | 6558 |
| 12 | 🇨🇴 CO | 5952 |
| 13 | 🇬🇷 GR | 4775 |
| 14 | 🇲🇽 MX | 4734 |
| 15 | 🇨🇭 CH | 4352 |
| 16 | 🇳🇴 NO | 4342 |
| 17 | 🇹🇷 TR | 3975 |
| 18 | 🇲🇾 MY | 2968 |
| 19 | 🇵🇱 PL | 2802 |
| 20 | 🇿🇦 ZA | 2695 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2369 |
| 23 | 🇵🇭 PH | 2173 |
| 24 | 🇬🇹 GT | 2139 |
| 25 | 🇰🇷 KR | 2133 |
| 26 | 🇲🇦 MA | 1666 |
| 27 | 🇭🇷 HR | 1568 |
| 28 | 🇲🇪 ME | 1544 |
| 29 | 🇳🇱 NL | 1501 |
| 30 | 🇲🇴 MO | 1403 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3375 |
| 2 | Denver International Airport |  | US | 2743 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2079 |
| 5 | Indira Gandhi International Airport |  | IN | 2025 |
| 6 | Harry Reid International Airport |  | US | 2001 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1817 |
| 8 | Zurich Airport |  | CH | 1759 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1736 |
| 10 | La Aurora Airport |  | GT | 1656 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1534 |
| 12 | El Dorado International Airport |  | CO | 1518 |
| 13 | Frankfurt am Main International Airport |  | DE | 1497 |
| 14 | Chicago O'Hare International Airport |  | US | 1492 |
| 15 | Salt Lake City International Airport |  | US | 1486 |
| 16 | Macau International Airport |  | MO | 1403 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1384 |
| 18 | Congonhas Airport |  | BR | 1366 |
| 19 | Madrid Barajas International Airport |  | ES | 1303 |
| 20 | Capua Airport |  | IT | 1295 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1259 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1168 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 24 | Charlotte/Douglas International Airport |  | US | 1158 |
| 25 | Charles de Gaulle International Airport |  | FR | 1130 |
| 26 | Kuala Lumpur International Airport |  | MY | 1124 |
| 27 | Malpensa International Airport |  | IT | 1103 |
| 28 | Bengaluru International Airport |  | IN | 1081 |
| 29 | Ninoy Aquino International Airport |  | PH | 1022 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1014 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1012 |
| 32 | Barcelona International Airport |  | ES | 978 |
| 33 | Daniel K Inouye International Airport |  | US | 965 |
| 34 | Seattle-Tacoma International Airport |  | US | 956 |
| 35 | Calgary International Airport |  | CA | 941 |
| 36 | Viracopos International Airport |  | BR | 937 |
| 37 | Scottsdale Airport |  | US | 924 |
| 38 | Tenerife Norte Airport |  | ES | 922 |
| 39 | Oslo Gardermoen Airport |  | NO | 919 |
| 40 | Reno/Tahoe International Airport |  | US | 910 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 603 | 21m | 244 km | 2,539.1 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 398 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 308 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 228 | 1h 47m | 1,423 km | 5,595.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 217 | 20m | 250 km | 937.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 204 | 31m | 49 km | 172.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 197 | 1h 15m | 961 km | 3,265.4 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 194 | 19m | 144 km | 482.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 188 | 50m | 556 km | 1,802.1 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 187 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 186 | 1h 38m | 1,156 km | 3,710.6 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 177 | 24m | 218 km | 666.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N806J |  | Monterey Regional Airport (KMRY) | Meadows Field (KBFL) | 2026-08-01 18:56 UTC | 2026-08-01 19:34 UTC | 37m |
| RNGR743 | RNG | Corpus Christi Nas (Truax Field) Airport (KNGP) | XS10 (XS10) | 2026-08-01 19:07 UTC | 2026-08-01 19:33 UTC | 25m |
| CHX7 | CHX | Korbach Airport (EDGK) | Kassel-Calden Airport (EDVK) | 2026-08-01 19:17 UTC | 2026-08-01 19:31 UTC | 13m |
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-08-01 14:51 UTC | 2026-08-01 19:30 UTC | 4h 38m |
| IBS1903 | IBS | Madrid Barajas International Airport (LEMD) | HE42 (HE42) | 2026-08-01 15:20 UTC | 2026-08-01 19:23 UTC | 4h 2m |
| N3289Q |  | Easton/Newnam Field (KESN) | Easton/Newnam Field (KESN) | 2026-08-01 18:41 UTC | 2026-08-01 19:15 UTC | 33m |
| RYR4YT | Ryanair | Vienna International Airport (LOWW) | Malpensa International Airport (LIMC) | 2026-08-01 18:04 UTC | 2026-08-01 19:15 UTC | 1h 11m |
| CAP409 | CAP | Riverside Airport (KRAL) | Adelanto Airport (52CL) | 2026-08-01 18:14 UTC | 2026-08-01 19:14 UTC | 59m |
| MSR794 | EgyptAir | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | HE42 (HE42) | 2026-08-01 16:37 UTC | 2026-08-01 19:12 UTC | 2h 35m |
| N500XX |  | Visalia Municipal Airport (KVIS) | San Francisco International Airport (KSFO) | 2026-08-01 18:38 UTC | 2026-08-01 19:10 UTC | 31m |
| N6094E |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-01 18:32 UTC | 2026-08-01 19:09 UTC | 37m |
| N198AE |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-01 17:03 UTC | 2026-08-01 19:09 UTC | 2h 6m |
| N2670M |  | Dewitt Field/Old Town Municipal Airport (KOLD) | Dewitt Field/Old Town Municipal Airport (KOLD) | 2026-08-01 18:57 UTC | 2026-08-01 19:09 UTC | 11m |
| ACA540 | Air Canada | Seattle-Tacoma International Airport (KSEA) | Toronto Pearson International Airport (CYYZ) | 2026-08-01 15:09 UTC | 2026-08-01 19:08 UTC | 3h 59m |
| TKR02 | TKR | Hill Afb Airport (KHIF) | KU77 (KU77) | 2026-08-01 18:49 UTC | 2026-08-01 19:04 UTC | 15m |
| LRS1092 | LRS | Juan Santamaria International Airport (MROC) | Atirro Airport (MRAR) | 2026-08-01 18:48 UTC | 2026-08-01 19:04 UTC | 16m |
| N9922T |  | Reid-Hillview Of Santa Clara County Airport (KRHV) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-08-01 17:49 UTC | 2026-08-01 19:04 UTC | 1h 14m |
| N64087 |  | Hayward Executive Airport (KHWD) | Sacramento Executive Airport (KSAC) | 2026-08-01 18:15 UTC | 2026-08-01 19:03 UTC | 48m |
| N739BZ |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Pine Bluffs Municipal Airport (K82V) | 2026-08-01 18:42 UTC | 2026-08-01 19:03 UTC | 20m |
| MXY618 | MXY | Harry Reid International Airport (KLAS) | Lincoln Airport (KLNK) | 2026-08-01 16:40 UTC | 2026-08-01 18:58 UTC | 2h 17m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
