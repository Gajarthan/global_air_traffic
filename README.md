# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_06:03:03_UTC-green)

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

**Latest saved flight:** 2026-07-24 06:03:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-24 06:03:03 UTC

- **147,190** saved flights
- **49,191** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **147,190** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,763,232.2 tonnes** estimated CO2 emissions
- **102,216,362 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5948 |
| 2 | SkyWest Airlines | 5402 |
| 3 | EJA | 2914 |
| 4 | IndiGo | 2650 |
| 5 | American Airlines | 2348 |
| 6 | Southwest Airlines | 2229 |
| 7 | ENY | 1833 |
| 8 | Delta Air Lines | 1746 |
| 9 | Lufthansa | 1450 |
| 10 | LATAM Airlines | 1354 |
| 11 | AZU | 1271 |
| 12 | WIF | 1247 |
| 13 | Vueling | 1245 |
| 14 | LXJ | 1134 |
| 15 | AXM | 1068 |
| 16 | Swiss International | 1038 |
| 17 | easyJet | 947 |
| 18 | All Nippon Airways | 935 |
| 19 | Alaska Airlines | 926 |
| 20 | QLK | 918 |
| 21 | EJU | 900 |
| 22 | VIV | 820 |
| 23 | CXK | 788 |
| 24 | AEE | 778 |
| 25 | JetBlue | 773 |
| 26 | Cathay Pacific | 772 |
| 27 | Air France | 770 |
| 28 | MXY | 770 |
| 29 | United Airlines | 765 |
| 30 | GLO | 762 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 127103 |
| 2 | 🇪🇸 ES | 9502 |
| 3 | 🇦🇺 AU | 8413 |
| 4 | 🇧🇷 BR | 8312 |
| 5 | 🇮🇳 IN | 8306 |
| 6 | 🇨🇦 CA | 7884 |
| 7 | 🇮🇹 IT | 7627 |
| 8 | 🇩🇪 DE | 7539 |
| 9 | 🇬🇧 GB | 6687 |
| 10 | 🇯🇵 JP | 6129 |
| 11 | 🇫🇷 FR | 5817 |
| 12 | 🇨🇴 CO | 4879 |
| 13 | 🇲🇽 MX | 4284 |
| 14 | 🇬🇷 GR | 4161 |
| 15 | 🇳🇴 NO | 3912 |
| 16 | 🇨🇭 CH | 3820 |
| 17 | 🇹🇷 TR | 3441 |
| 18 | 🇲🇾 MY | 2784 |
| 19 | 🇵🇱 PL | 2471 |
| 20 | 🇿🇦 ZA | 2372 |
| 21 | 🇳🇿 NZ | 2243 |
| 22 | 🇹🇭 TH | 2147 |
| 23 | 🇰🇷 KR | 2049 |
| 24 | 🇵🇭 PH | 1963 |
| 25 | 🇬🇹 GT | 1908 |
| 26 | 🇲🇦 MA | 1514 |
| 27 | 🇲🇪 ME | 1455 |
| 28 | 🇳🇱 NL | 1364 |
| 29 | 🇭🇷 HR | 1338 |
| 30 | 🇲🇴 MO | 1230 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3035 |
| 2 | Denver International Airport |  | US | 2470 |
| 3 | Tokyo International Airport |  | JP | 1971 |
| 4 | Indira Gandhi International Airport |  | IN | 1845 |
| 5 | Harry Reid International Airport |  | US | 1838 |
| 6 | Guaymaral Airport |  | CO | 1812 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1660 |
| 8 | Zurich Airport |  | CH | 1615 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1551 |
| 10 | La Aurora Airport |  | GT | 1479 |
| 11 | Frankfurt am Main International Airport |  | DE | 1402 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1388 |
| 13 | Chicago O'Hare International Airport |  | US | 1367 |
| 14 | Salt Lake City International Airport |  | US | 1329 |
| 15 | El Dorado International Airport |  | CO | 1320 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1274 |
| 17 | Macau International Airport |  | MO | 1230 |
| 18 | Capua Airport |  | IT | 1193 |
| 19 | Congonhas Airport |  | BR | 1185 |
| 20 | Madrid Barajas International Airport |  | ES | 1169 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1153 |
| 22 | Kuala Lumpur International Airport |  | MY | 1075 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1063 |
| 24 | Charlotte/Douglas International Airport |  | US | 1050 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1031 |
| 26 | Charles de Gaulle International Airport |  | FR | 1016 |
| 27 | Bengaluru International Airport |  | IN | 994 |
| 28 | Malpensa International Airport |  | IT | 947 |
| 29 | Ninoy Aquino International Airport |  | PH | 918 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 903 |
| 31 | Barcelona International Airport |  | ES | 889 |
| 32 | Daniel K Inouye International Airport |  | US | 886 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 884 |
| 34 | Seattle-Tacoma International Airport |  | US | 847 |
| 35 | Tenerife Norte Airport |  | ES | 844 |
| 36 | Calgary International Airport |  | CA | 844 |
| 37 | Viracopos International Airport |  | BR | 833 |
| 38 | Scottsdale Airport |  | US | 833 |
| 39 | Amsterdam Airport Schiphol |  | NL | 824 |
| 40 | Oslo Gardermoen Airport |  | NO | 810 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 764 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 535 | 21m | 244 km | 2,252.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 358 | 24m | 225 km | 1,388.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 356 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 345 | 1h 9m | 770 km | 4,583.1 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 300 | 14m | 114 km | 588.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 264 | 27m | 275 km | 1,251.0 t |
| 10 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 263 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 222 | 22m | 55 km | 211.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 198 | 1h 46m | 1,423 km | 4,859.2 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 197 | 44m | 241 km | 818.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 194 | 26m | 215 km | 718.5 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 194 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 190 | 20m | 99 km | 325.5 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 180 | 20m | 250 km | 777.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 180 | 28m | 152 km | 470.4 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 174 | 31m | 369 km | 1,107.6 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 174 | 18m | 144 km | 432.8 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 172 | 1h 16m | 961 km | 2,851.0 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 171 | 12m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 170 | 44m | 452 km | 1,324.9 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 168 | 1h 1m | 695 km | 2,013.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 166 | 1h 39m | 1,156 km | 3,311.6 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 160 | 55m | 136 km | 375.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EWG4AV | EWG | Dusseldorf International Airport (EDDL) | Tivat Airport (LYTV) | 2026-07-24 04:27 UTC | 2026-07-24 06:03 UTC | 1h 36m |
| VKG616 | VKG | Oslo Gardermoen Airport (ENGM) | Kristianstad Airport (ESMK) | 2026-07-24 05:10 UTC | 2026-07-24 05:48 UTC | 38m |
| ASA1681 | Alaska Airlines | Harry Reid International Airport (KLAS) | Seattle-Tacoma International Airport (KSEA) | 2026-07-24 03:44 UTC | 2026-07-24 05:47 UTC | 2h 3m |
| FSCN200 | FSC | RAAF Base Richmond (YSRI) | Ballina Byron Gateway Airport (YBNA) | 2026-07-24 04:43 UTC | 2026-07-24 05:41 UTC | 57m |
| JA6429 |  | Tokyo International Airport (RJTT) | Tokyo International Airport (RJTT) | 2026-07-24 05:11 UTC | 2026-07-24 05:39 UTC | 27m |
| ABY135 | ABY | Sharjah International Airport (OMSJ) | Sirri Island Airport (OIBS) | 2026-07-24 05:13 UTC | 2026-07-24 05:26 UTC | 12m |
| EWG7QZ | EWG | Václav Havel Airport (LKPR) | Ziemsko Airport (EPDR) | 2026-07-24 04:48 UTC | 2026-07-24 05:25 UTC | 36m |
| N2226N |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-07-24 04:05 UTC | 2026-07-24 05:24 UTC | 1h 19m |
| RXA6133 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Bunyan Airfield (YBUY) | 2026-07-24 04:30 UTC | 2026-07-24 05:14 UTC | 43m |
| UBG143 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-07-24 04:36 UTC | 2026-07-24 05:13 UTC | 37m |
| AXB1496 | AXB | Netaji Subhash Chandra Bose International Airport (VECC) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-07-24 04:50 UTC | 2026-07-24 05:09 UTC | 19m |
|  |  | Langtang Airport (VNLT) | Langtang Airport (VNLT) | 2026-07-24 05:09 UTC | 2026-07-24 05:09 UTC | 0m |
| N7063M |  | Mc Minnville Municipal Airport (KMMV) | Corvallis Municipal Airport (KCVO) | 2026-07-24 04:35 UTC | 2026-07-24 05:01 UTC | 26m |
| AXB1035 | AXB | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 2026-07-24 03:04 UTC | 2026-07-24 05:00 UTC | 1h 55m |
| APG225 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-24 04:33 UTC | 2026-07-24 04:59 UTC | 26m |
| JA6429 |  | Tokyo International Airport (RJTT) | Tokyo International Airport (RJTT) | 2026-07-24 04:17 UTC | 2026-07-24 04:59 UTC | 41m |
| BTK6710 | BTK | Soekarno-Hatta International Airport (WIII) | Banding Agung Airport (WIPD) | 2026-07-24 04:41 UTC | 2026-07-24 04:58 UTC | 16m |
| RYR5914 | Ryanair | Malpensa International Airport (LIMC) | Capua Airport (LIAU) | 2026-07-24 04:04 UTC | 2026-07-24 04:57 UTC | 53m |
| ASA1102 | Alaska Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-07-24 04:35 UTC | 2026-07-24 04:57 UTC | 22m |
| ANZ832L | ANZ | Christchurch International Airport (NZCH) | Hokitika Airfield (NZHK) | 2026-07-24 04:35 UTC | 2026-07-24 04:57 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
