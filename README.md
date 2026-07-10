# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_15:49:35_UTC-green)

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

**Latest saved flight:** 2026-07-10 15:49:35 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-10 15:49:35 UTC

- **135,752** saved flights
- **45,866** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **135,752** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,632,391.7 tonnes** estimated CO2 emissions
- **94,631,404 km** total distance flown
- **855 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5502 |
| 2 | SkyWest Airlines | 4988 |
| 3 | EJA | 2653 |
| 4 | IndiGo | 2508 |
| 5 | American Airlines | 2134 |
| 6 | Southwest Airlines | 2040 |
| 7 | ENY | 1707 |
| 8 | Delta Air Lines | 1620 |
| 9 | Lufthansa | 1393 |
| 10 | LATAM Airlines | 1245 |
| 11 | Vueling | 1181 |
| 12 | WIF | 1181 |
| 13 | AZU | 1163 |
| 14 | LXJ | 1044 |
| 15 | AXM | 1028 |
| 16 | Swiss International | 967 |
| 17 | All Nippon Airways | 882 |
| 18 | easyJet | 878 |
| 19 | Alaska Airlines | 860 |
| 20 | QLK | 851 |
| 21 | EJU | 834 |
| 22 | VIV | 745 |
| 23 | AEE | 734 |
| 24 | CXK | 729 |
| 25 | Air France | 725 |
| 26 | Cathay Pacific | 725 |
| 27 | United Airlines | 716 |
| 28 | JetBlue | 715 |
| 29 | MXY | 705 |
| 30 | GLO | 694 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 116543 |
| 2 | 🇪🇸 ES | 8967 |
| 3 | 🇮🇳 IN | 7871 |
| 4 | 🇦🇺 AU | 7826 |
| 5 | 🇧🇷 BR | 7655 |
| 6 | 🇨🇦 CA | 7181 |
| 7 | 🇩🇪 DE | 7067 |
| 8 | 🇮🇹 IT | 7032 |
| 9 | 🇬🇧 GB | 6132 |
| 10 | 🇯🇵 JP | 5770 |
| 11 | 🇫🇷 FR | 5385 |
| 12 | 🇨🇴 CO | 4274 |
| 13 | 🇲🇽 MX | 3950 |
| 14 | 🇬🇷 GR | 3859 |
| 15 | 🇳🇴 NO | 3682 |
| 16 | 🇨🇭 CH | 3515 |
| 17 | 🇹🇷 TR | 3107 |
| 18 | 🇲🇾 MY | 2670 |
| 19 | 🇵🇱 PL | 2250 |
| 20 | 🇿🇦 ZA | 2233 |
| 21 | 🇳🇿 NZ | 2117 |
| 22 | 🇹🇭 TH | 2071 |
| 23 | 🇰🇷 KR | 1992 |
| 24 | 🇵🇭 PH | 1861 |
| 25 | 🇬🇹 GT | 1829 |
| 26 | 🇲🇦 MA | 1430 |
| 27 | 🇲🇪 ME | 1347 |
| 28 | 🇳🇱 NL | 1265 |
| 29 | 🇭🇷 HR | 1207 |
| 30 | 🇲🇴 MO | 1186 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2826 |
| 2 | Denver International Airport |  | US | 2280 |
| 3 | Tokyo International Airport |  | JP | 1884 |
| 4 | Indira Gandhi International Airport |  | IN | 1739 |
| 5 | Harry Reid International Airport |  | US | 1697 |
| 6 | Guaymaral Airport |  | CO | 1651 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1582 |
| 8 | Zurich Airport |  | CH | 1512 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1437 |
| 10 | La Aurora Airport |  | GT | 1413 |
| 11 | Frankfurt am Main International Airport |  | DE | 1346 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1305 |
| 13 | Chicago O'Hare International Airport |  | US | 1288 |
| 14 | El Dorado International Airport |  | CO | 1213 |
| 15 | Salt Lake City International Airport |  | US | 1208 |
| 16 | Macau International Airport |  | MO | 1186 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1176 |
| 18 | Madrid Barajas International Airport |  | ES | 1107 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1105 |
| 20 | Capua Airport |  | IT | 1103 |
| 21 | Congonhas Airport |  | BR | 1089 |
| 22 | Kuala Lumpur International Airport |  | MY | 1036 |
| 23 | Charlotte/Douglas International Airport |  | US | 995 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 985 |
| 25 | Charles de Gaulle International Airport |  | FR | 968 |
| 26 | Bengaluru International Airport |  | IN | 946 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 933 |
| 28 | Malpensa International Airport |  | IT | 891 |
| 29 | Ninoy Aquino International Airport |  | PH | 866 |
| 30 | Daniel K Inouye International Airport |  | US | 840 |
| 31 | Barcelona International Airport |  | ES | 831 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 829 |
| 33 | Tenerife Norte Airport |  | ES | 809 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 796 |
| 35 | Calgary International Airport |  | CA | 787 |
| 36 | Scottsdale Airport |  | US | 780 |
| 37 | Seattle-Tacoma International Airport |  | US | 774 |
| 38 | Viracopos International Airport |  | BR | 773 |
| 39 | Vitoria/Foronda Airport |  | ES | 765 |
| 40 | Amsterdam Airport Schiphol |  | NL | 759 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 695 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 491 | 21m | 244 km | 2,067.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 338 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 334 | 24m | 225 km | 1,295.8 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 325 | 1h 10m | 770 km | 4,317.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 291 | 14m | 114 km | 570.7 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 254 | 26m | 275 km | 1,203.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 247 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 199 | 22m | 55 km | 189.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 188 | 26m | 215 km | 696.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 188 | 44m | 241 km | 780.9 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 185 | 20m | 99 km | 316.9 t |
| 17 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 183 | 1h 46m | 1,423 km | 4,491.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 180 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 175 | 27m | 152 km | 457.3 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 166 | 31m | 369 km | 1,056.6 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 166 | 20m | 250 km | 717.0 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 163 | 18m | 144 km | 405.5 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 162 | 30m | 49 km | 136.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 161 | 44m | 452 km | 1,254.8 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 159 | 1h 16m | 961 km | 2,635.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 157 | 1h 1m | 695 km | 1,882.0 t |
| 27 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 155 | 1h 38m | 1,156 km | 3,092.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 149 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N636SJ |  | Spirit Of St Louis Airport (KSUS) | Spirit Of St Louis Airport (KSUS) | 2026-07-10 14:46 UTC | 2026-07-10 15:49 UTC | 1h 3m |
| CAP322 | CAP | Austin-Bergstrom International Airport (KAUS) | Austin-Bergstrom International Airport (KAUS) | 2026-07-10 14:01 UTC | 2026-07-10 15:47 UTC | 1h 45m |
| N802FG |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-07-10 15:24 UTC | 2026-07-10 15:46 UTC | 21m |
| N62770 |  | Orlando Executive Airport (KORL) | Orlando Executive Airport (KORL) | 2026-07-10 14:36 UTC | 2026-07-10 15:42 UTC | 1h 5m |
| N509FG |  | Trenton Mercer Airport (KTTN) | Wings Field (KLOM) | 2026-07-10 15:24 UTC | 2026-07-10 15:40 UTC | 15m |
| BOMR820 | BOM | Corpus Christi Nas (Truax Field) Airport (KNGP) | Mustang Beach Airport (KRAS) | 2026-07-10 14:57 UTC | 2026-07-10 15:33 UTC | 35m |
| N313RJ |  | Boire Field (KASH) | Concord Municipal Airport (KCON) | 2026-07-10 15:06 UTC | 2026-07-10 15:31 UTC | 25m |
| HBIJR | HBI | Zurich Airport (LSZH) | Zurich Airport (LSZH) | 2026-07-10 05:10 UTC | 2026-07-10 15:29 UTC | 10h 19m |
| N571SP |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-07-10 14:41 UTC | 2026-07-10 15:29 UTC | 48m |
| EXS31PY | EXS | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Manchester Airport (EGCC) | 2026-07-10 13:34 UTC | 2026-07-10 15:28 UTC | 1h 53m |
| WIF3P | WIF | Oslo Gardermoen Airport (ENGM) | Leknes Airport (ENLK) | 2026-07-10 13:30 UTC | 2026-07-10 15:27 UTC | 1h 57m |
| TRP3 | TRP | Laura's Landing Airport (22MD) | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | 2026-07-10 15:08 UTC | 2026-07-10 15:27 UTC | 18m |
| N13NW |  | Redding Regional Airport (KRDD) | NV16 (NV16) | 2026-07-10 14:53 UTC | 2026-07-10 15:26 UTC | 33m |
| N150LE |  | Bend Municipal Airport (KBDN) | OG05 (OG05) | 2026-07-10 15:13 UTC | 2026-07-10 15:26 UTC | 12m |
| N8064W |  | Denton Enterprise Airport (KDTO) | Gainesville Municipal Airport (KGLE) | 2026-07-10 15:09 UTC | 2026-07-10 15:26 UTC | 16m |
| ES801 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-07-10 15:05 UTC | 2026-07-10 15:24 UTC | 18m |
| N3517S |  | Rocky Mountain Metro Airport (KBJC) | Greeley-Weld County Airport (KGXY) | 2026-07-10 14:35 UTC | 2026-07-10 15:22 UTC | 46m |
| OEGTX | OEG | Budapest Ferenc Liszt International Airport (LHBP) | Stuttgart Airport (EDDS) | 2026-07-10 14:00 UTC | 2026-07-10 15:18 UTC | 1h 18m |
| N258K |  | K00V (K00V) | Lake Creek Ranch Airport (92CO) | 2026-07-10 14:37 UTC | 2026-07-10 15:17 UTC | 40m |
| N560RE |  | 4AL2 (4AL2) | Auburn University Regional Airport (KAUO) | 2026-07-10 14:40 UTC | 2026-07-10 15:17 UTC | 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
