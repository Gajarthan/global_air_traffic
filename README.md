# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_21:17:45_UTC-green)

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

**Latest saved flight:** 2026-07-20 21:17:45 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-20 21:17:45 UTC

- **142,710** saved flights
- **47,869** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **142,710** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,711,811.6 tonnes** estimated CO2 emissions
- **99,235,454 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5812 |
| 2 | SkyWest Airlines | 5214 |
| 3 | EJA | 2815 |
| 4 | IndiGo | 2599 |
| 5 | American Airlines | 2281 |
| 6 | Southwest Airlines | 2149 |
| 7 | ENY | 1770 |
| 8 | Delta Air Lines | 1690 |
| 9 | Lufthansa | 1435 |
| 10 | LATAM Airlines | 1315 |
| 11 | AZU | 1227 |
| 12 | Vueling | 1227 |
| 13 | WIF | 1220 |
| 14 | LXJ | 1097 |
| 15 | AXM | 1055 |
| 16 | Swiss International | 1014 |
| 17 | easyJet | 932 |
| 18 | All Nippon Airways | 913 |
| 19 | Alaska Airlines | 900 |
| 20 | QLK | 894 |
| 21 | EJU | 879 |
| 22 | VIV | 791 |
| 23 | AEE | 763 |
| 24 | CXK | 762 |
| 25 | JetBlue | 760 |
| 26 | Air France | 759 |
| 27 | United Airlines | 743 |
| 28 | MXY | 741 |
| 29 | Cathay Pacific | 736 |
| 30 | GLO | 730 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 122764 |
| 2 | 🇪🇸 ES | 9308 |
| 3 | 🇦🇺 AU | 8162 |
| 4 | 🇮🇳 IN | 8141 |
| 5 | 🇧🇷 BR | 8055 |
| 6 | 🇨🇦 CA | 7519 |
| 7 | 🇮🇹 IT | 7438 |
| 8 | 🇩🇪 DE | 7389 |
| 9 | 🇬🇧 GB | 6539 |
| 10 | 🇯🇵 JP | 5974 |
| 11 | 🇫🇷 FR | 5672 |
| 12 | 🇨🇴 CO | 4570 |
| 13 | 🇲🇽 MX | 4142 |
| 14 | 🇬🇷 GR | 4068 |
| 15 | 🇳🇴 NO | 3820 |
| 16 | 🇨🇭 CH | 3690 |
| 17 | 🇹🇷 TR | 3375 |
| 18 | 🇲🇾 MY | 2751 |
| 19 | 🇵🇱 PL | 2402 |
| 20 | 🇿🇦 ZA | 2326 |
| 21 | 🇳🇿 NZ | 2186 |
| 22 | 🇹🇭 TH | 2127 |
| 23 | 🇰🇷 KR | 2027 |
| 24 | 🇵🇭 PH | 1928 |
| 25 | 🇬🇹 GT | 1873 |
| 26 | 🇲🇦 MA | 1491 |
| 27 | 🇲🇪 ME | 1413 |
| 28 | 🇳🇱 NL | 1345 |
| 29 | 🇭🇷 HR | 1301 |
| 30 | 🇲🇴 MO | 1193 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2939 |
| 2 | Denver International Airport |  | US | 2387 |
| 3 | Tokyo International Airport |  | JP | 1928 |
| 4 | Indira Gandhi International Airport |  | IN | 1804 |
| 5 | Harry Reid International Airport |  | US | 1791 |
| 6 | Guaymaral Airport |  | CO | 1738 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1637 |
| 8 | Zurich Airport |  | CH | 1585 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1498 |
| 10 | La Aurora Airport |  | GT | 1449 |
| 11 | Frankfurt am Main International Airport |  | DE | 1385 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1351 |
| 13 | Chicago O'Hare International Airport |  | US | 1333 |
| 14 | Salt Lake City International Airport |  | US | 1277 |
| 15 | El Dorado International Airport |  | CO | 1261 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1256 |
| 17 | Macau International Airport |  | MO | 1193 |
| 18 | Capua Airport |  | IT | 1166 |
| 19 | Madrid Barajas International Airport |  | ES | 1147 |
| 20 | Congonhas Airport |  | BR | 1144 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1131 |
| 22 | Kuala Lumpur International Airport |  | MY | 1062 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1034 |
| 24 | Charlotte/Douglas International Airport |  | US | 1030 |
| 25 | Charles de Gaulle International Airport |  | FR | 1004 |
| 26 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 997 |
| 27 | Bengaluru International Airport |  | IN | 972 |
| 28 | Malpensa International Airport |  | IT | 921 |
| 29 | Ninoy Aquino International Airport |  | PH | 900 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 874 |
| 31 | Daniel K Inouye International Airport |  | US | 869 |
| 32 | Barcelona International Airport |  | ES | 869 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 846 |
| 34 | Tenerife Norte Airport |  | ES | 825 |
| 35 | Calgary International Airport |  | CA | 814 |
| 36 | Seattle-Tacoma International Airport |  | US | 813 |
| 37 | Viracopos International Airport |  | BR | 809 |
| 38 | Amsterdam Airport Schiphol |  | NL | 808 |
| 39 | Scottsdale Airport |  | US | 804 |
| 40 | Vitoria/Foronda Airport |  | ES | 786 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 732 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 519 | 21m | 244 km | 2,185.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 349 | 24m | 225 km | 1,354.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 346 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 338 | 1h 9m | 770 km | 4,490.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 259 | 26m | 275 km | 1,227.3 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 210 | 22m | 55 km | 199.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 192 | 1h 46m | 1,423 km | 4,712.0 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 191 | 26m | 215 km | 707.4 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 190 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 190 | 44m | 241 km | 789.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 178 | 28m | 152 km | 465.2 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 177 | 20m | 250 km | 764.5 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 173 | 31m | 369 km | 1,101.2 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 172 | 18m | 144 km | 427.8 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 167 | 44m | 452 km | 1,301.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 165 | 1h 1m | 695 km | 1,977.9 t |
| 26 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 165 | 1h 16m | 961 km | 2,735.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 163 | 1h 38m | 1,156 km | 3,251.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 163 | 13m | - | - |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 157 | 54m | 136 km | 368.1 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 156 | 14m | 154 km | 413.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N7614Y |  | Lenawee County Airport (KADG) | Lenawee County Airport (KADG) | 2026-07-20 20:53 UTC | 2026-07-20 21:17 UTC | 24m |
| TKR910 | TKR | Rogue Valley International/Medford Airport (KMFR) | Fall River Mills Airport (KO89) | 2026-07-20 20:42 UTC | 2026-07-20 21:04 UTC | 21m |
| N234WL |  | Tweed/New Haven Airport (KHVN) | Laguardia Airport (KLGA) | 2026-07-20 20:34 UTC | 2026-07-20 21:01 UTC | 26m |
| TIBKY | TIB | Juan Santamaria International Airport (MROC) | Portalon Airport (MRPL) | 2026-07-20 20:45 UTC | 2026-07-20 21:00 UTC | 15m |
| N1675B |  | Ambler Airport (PAFM) | Ambler Airport (PAFM) | 2026-07-20 20:37 UTC | 2026-07-20 20:56 UTC | 18m |
| ITY247 | ITY | Mulhouse-Habsheim Airport (LFGB) | Muenster Aero Airport (LSPU) | 2026-07-20 20:30 UTC | 2026-07-20 20:56 UTC | 26m |
| N77YA |  | Northeast Philadelphia Airport (KPNE) | Lee Airport (KANP) | 2026-07-20 20:09 UTC | 2026-07-20 20:56 UTC | 46m |
| N245CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Gillespie Field (KSEE) | 2026-07-20 20:26 UTC | 2026-07-20 20:55 UTC | 29m |
| LRS6715 | LRS | Carrizal Airport (MRCZ) | Juan Santamaria International Airport (MROC) | 2026-07-20 20:43 UTC | 2026-07-20 20:54 UTC | 10m |
| N630HR |  | Decatur Municipal Airport (KLUD) | Decatur Municipal Airport (KLUD) | 2026-07-20 20:36 UTC | 2026-07-20 20:52 UTC | 15m |
| WIF1H | WIF | Bodø Airport (ENBO) | Leknes Airport (ENLK) | 2026-07-20 20:38 UTC | 2026-07-20 20:51 UTC | 13m |
|  |  | Whidbey Island Nas (Ault Field) Airport (KNUW) | Fairchild Afb Airport (KSKA) | 2026-07-20 19:05 UTC | 2026-07-20 20:50 UTC | 1h 44m |
| N353MM |  | Monmouth Executive Airport (KBLM) | Blairstown Airport (K1N7) | 2026-07-20 20:03 UTC | 2026-07-20 20:49 UTC | 45m |
| EJA864 | EJA | Dallas Love Field (KDAL) | Austin-Bergstrom International Airport (KAUS) | 2026-07-20 20:17 UTC | 2026-07-20 20:49 UTC | 32m |
| SPFPB | SPF | Siljansnas Airport (ESVS) | Skinnlanda Airport (ESVM) | 2026-07-20 20:22 UTC | 2026-07-20 20:49 UTC | 26m |
| LXJ438 | LXJ | Norman Y Mineta San Jose International Airport (KSJC) | Van Nuys Airport (KVNY) | 2026-07-20 19:59 UTC | 2026-07-20 20:48 UTC | 49m |
| TKR133 | TKR | Mc Clellan Airfield (KMCC) | Milhous Ranch Airport (79CL) | 2026-07-20 20:23 UTC | 2026-07-20 20:47 UTC | 24m |
| N4035S |  | Fremont County Airport (K1V6) | 14CO (14CO) | 2026-07-20 20:24 UTC | 2026-07-20 20:44 UTC | 20m |
| N412MH |  | Boise Air Trml/Gowen Field (KBOI) | Hidden Lakes Airport (ID44) | 2026-07-20 20:36 UTC | 2026-07-20 20:44 UTC | 8m |
| RYR7801 | Ryanair | Palma De Mallorca Airport (LEPA) | Mirandela Airport (LPMI) | 2026-07-20 18:57 UTC | 2026-07-20 20:43 UTC | 1h 46m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
