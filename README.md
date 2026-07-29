# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_21:58:51_UTC-green)

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

**Latest saved flight:** 2026-07-29 21:58:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-29 21:58:51 UTC

- **159,386** saved flights
- **52,766** unique routes
- **136** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **159,386** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,912,897.1 tonnes** estimated CO2 emissions
- **110,892,588 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6400 |
| 2 | SkyWest Airlines | 5825 |
| 3 | EJA | 3171 |
| 4 | IndiGo | 2803 |
| 5 | American Airlines | 2526 |
| 6 | Southwest Airlines | 2502 |
| 7 | ENY | 1985 |
| 8 | Delta Air Lines | 1894 |
| 9 | Lufthansa | 1516 |
| 10 | LATAM Airlines | 1497 |
| 11 | AZU | 1404 |
| 12 | WIF | 1351 |
| 13 | Vueling | 1335 |
| 14 | LXJ | 1230 |
| 15 | AXM | 1113 |
| 16 | Swiss International | 1098 |
| 17 | easyJet | 1042 |
| 18 | Alaska Airlines | 998 |
| 19 | QLK | 986 |
| 20 | All Nippon Airways | 984 |
| 21 | EJU | 976 |
| 22 | VIV | 875 |
| 23 | CXK | 846 |
| 24 | United Airlines | 843 |
| 25 | GLO | 839 |
| 26 | Cathay Pacific | 838 |
| 27 | AEE | 837 |
| 28 | MXY | 830 |
| 29 | Air France | 829 |
| 30 | JetBlue | 818 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 137634 |
| 2 | 🇪🇸 ES | 10238 |
| 3 | 🇧🇷 BR | 9122 |
| 4 | 🇦🇺 AU | 8959 |
| 5 | 🇮🇳 IN | 8816 |
| 6 | 🇨🇦 CA | 8644 |
| 7 | 🇮🇹 IT | 8242 |
| 8 | 🇩🇪 DE | 8064 |
| 9 | 🇬🇧 GB | 7308 |
| 10 | 🇯🇵 JP | 6481 |
| 11 | 🇫🇷 FR | 6303 |
| 12 | 🇨🇴 CO | 5619 |
| 13 | 🇲🇽 MX | 4583 |
| 14 | 🇬🇷 GR | 4571 |
| 15 | 🇳🇴 NO | 4223 |
| 16 | 🇨🇭 CH | 4169 |
| 17 | 🇹🇷 TR | 3800 |
| 18 | 🇲🇾 MY | 2894 |
| 19 | 🇵🇱 PL | 2709 |
| 20 | 🇿🇦 ZA | 2573 |
| 21 | 🇳🇿 NZ | 2349 |
| 22 | 🇹🇭 TH | 2276 |
| 23 | 🇰🇷 KR | 2100 |
| 24 | 🇵🇭 PH | 2091 |
| 25 | 🇬🇹 GT | 2038 |
| 26 | 🇲🇦 MA | 1619 |
| 27 | 🇲🇪 ME | 1524 |
| 28 | 🇭🇷 HR | 1479 |
| 29 | 🇳🇱 NL | 1456 |
| 30 | 🇲🇴 MO | 1320 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3258 |
| 2 | Denver International Airport |  | US | 2654 |
| 3 | Tokyo International Airport |  | JP | 2050 |
| 4 | Guaymaral Airport |  | CO | 2006 |
| 5 | Indira Gandhi International Airport |  | IN | 1964 |
| 6 | Harry Reid International Airport |  | US | 1944 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1767 |
| 8 | Zurich Airport |  | CH | 1705 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1674 |
| 10 | La Aurora Airport |  | GT | 1581 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1488 |
| 12 | Frankfurt am Main International Airport |  | DE | 1464 |
| 13 | El Dorado International Airport |  | CO | 1460 |
| 14 | Chicago O'Hare International Airport |  | US | 1446 |
| 15 | Salt Lake City International Airport |  | US | 1435 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1333 |
| 17 | Congonhas Airport |  | BR | 1322 |
| 18 | Macau International Airport |  | MO | 1320 |
| 19 | Madrid Barajas International Airport |  | ES | 1264 |
| 20 | Capua Airport |  | IT | 1257 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1224 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1138 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1135 |
| 24 | Charlotte/Douglas International Airport |  | US | 1120 |
| 25 | Kuala Lumpur International Airport |  | MY | 1107 |
| 26 | Charles de Gaulle International Airport |  | FR | 1093 |
| 27 | Malpensa International Airport |  | IT | 1053 |
| 28 | Bengaluru International Airport |  | IN | 1050 |
| 29 | Ninoy Aquino International Airport |  | PH | 981 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 973 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 971 |
| 32 | Barcelona International Airport |  | ES | 951 |
| 33 | Daniel K Inouye International Airport |  | US | 940 |
| 34 | Seattle-Tacoma International Airport |  | US | 930 |
| 35 | Calgary International Airport |  | CA | 912 |
| 36 | Viracopos International Airport |  | BR | 911 |
| 37 | Scottsdale Airport |  | US | 902 |
| 38 | Tenerife Norte Airport |  | ES | 897 |
| 39 | Oslo Gardermoen Airport |  | NO | 886 |
| 40 | Amsterdam Airport Schiphol |  | NL | 876 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 842 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 579 | 21m | 244 km | 2,438.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 379 | 24m | 225 km | 1,470.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 379 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 366 | 1h 9m | 770 km | 4,862.0 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 293 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 280 | 27m | 275 km | 1,326.8 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 233 | 22m | 55 km | 221.5 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 226 | 44m | 241 km | 938.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 215 | 1h 47m | 1,423 km | 5,276.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 210 | 26m | 215 km | 777.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 205 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 200 | 20m | 250 km | 863.9 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 191 | 30m | 49 km | 161.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 190 | 1h 15m | 961 km | 3,149.3 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 189 | 27m | 152 km | 493.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 188 | 18m | 144 km | 467.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 186 | 31m | 369 km | 1,183.9 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 181 | 50m | 556 km | 1,735.0 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 179 | 1h 39m | 1,156 km | 3,571.0 t |
| 28 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 176 | 1h 1m | 695 km | 2,109.7 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 170 | 23m | 218 km | 640.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA292 | Cathay Pacific | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Macau International Airport (VMMC) | 2026-07-29 11:43 UTC | 2026-07-29 21:58 UTC | 10h 15m |
| YTX | YTX | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-07-29 21:11 UTC | 2026-07-29 21:56 UTC | 45m |
| N2361L |  | Shannon Flight Strip (2GA8) | Cartersville Airport (KVPC) | 2026-07-29 21:45 UTC | 2026-07-29 21:56 UTC | 11m |
| CXK651 | CXK | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-07-29 20:52 UTC | 2026-07-29 21:54 UTC | 1h 2m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-07-29 17:08 UTC | 2026-07-29 21:53 UTC | 4h 45m |
|  |  | Carr Airport (WV65) | Carr Airport (WV65) | 2026-07-29 21:45 UTC | 2026-07-29 21:47 UTC | 2m |
| CPA216 | Cathay Pacific | Manchester Airport (EGCC) | Macau International Airport (VMMC) | 2026-07-29 10:24 UTC | 2026-07-29 21:46 UTC | 11h 21m |
| N307SH |  | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-07-29 20:36 UTC | 2026-07-29 21:43 UTC | 1h 6m |
| CAI2PW | CAI | Amsterdam Airport Schiphol (EHAM) | Antalya International Airport (LTAI) | 2026-07-29 18:37 UTC | 2026-07-29 21:42 UTC | 3h 5m |
| PXT680 | PXT | Rogers Executive - Carter Field (KROG) | Hayward Executive Airport (KHWD) | 2026-07-29 18:14 UTC | 2026-07-29 21:41 UTC | 3h 26m |
| EJA864 | EJA | Teterboro Airport (KTEB) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-29 16:21 UTC | 2026-07-29 21:39 UTC | 5h 18m |
| N527CH |  | Ted Stevens Anchorage International Airport (PANC) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-29 21:39 UTC | 2026-07-29 21:39 UTC | 0m |
| LS21 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-29 21:37 UTC | 2026-07-29 21:38 UTC | 0m |
| N460AK |  | Mc Clellan Airfield (KMCC) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-29 21:11 UTC | 2026-07-29 21:37 UTC | 26m |
| N527CH |  | Middleton Island Airport (PAMD) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-29 20:33 UTC | 2026-07-29 21:27 UTC | 54m |
| LS21 |  | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-07-29 21:13 UTC | 2026-07-29 21:24 UTC | 11m |
| N56BA |  | Westchester County Airport (KHPN) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-07-29 20:29 UTC | 2026-07-29 21:23 UTC | 54m |
| N137HS |  | Mayhall Airport (5LL3) | IL31 (IL31) | 2026-07-29 21:11 UTC | 2026-07-29 21:23 UTC | 11m |
| N751AP |  | Reading Regional/Carl A Spaatz Field (KRDG) | Lancaster Airport (KLNS) | 2026-07-29 21:11 UTC | 2026-07-29 21:21 UTC | 10m |
| N8436 |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-07-29 20:50 UTC | 2026-07-29 21:18 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
