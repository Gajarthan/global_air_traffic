# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_00:00:53_UTC-green)

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

**Latest saved flight:** 2026-07-27 00:00:53 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-27 00:00:53 UTC

- **153,605** saved flights
- **50,964** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **153,605** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,837,586.5 tonnes** estimated CO2 emissions
- **106,526,752 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6197 |
| 2 | SkyWest Airlines | 5627 |
| 3 | EJA | 3052 |
| 4 | IndiGo | 2729 |
| 5 | American Airlines | 2438 |
| 6 | Southwest Airlines | 2339 |
| 7 | ENY | 1926 |
| 8 | Delta Air Lines | 1803 |
| 9 | Lufthansa | 1488 |
| 10 | LATAM Airlines | 1429 |
| 11 | AZU | 1340 |
| 12 | WIF | 1290 |
| 13 | Vueling | 1282 |
| 14 | LXJ | 1189 |
| 15 | AXM | 1090 |
| 16 | Swiss International | 1072 |
| 17 | easyJet | 1003 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 957 |
| 20 | QLK | 944 |
| 21 | EJU | 943 |
| 22 | VIV | 847 |
| 23 | CXK | 820 |
| 24 | MXY | 809 |
| 25 | AEE | 807 |
| 26 | GLO | 801 |
| 27 | Air France | 798 |
| 28 | JetBlue | 797 |
| 29 | United Airlines | 788 |
| 30 | Cathay Pacific | 785 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 132604 |
| 2 | 🇪🇸 ES | 9916 |
| 3 | 🇧🇷 BR | 8741 |
| 4 | 🇦🇺 AU | 8631 |
| 5 | 🇮🇳 IN | 8579 |
| 6 | 🇨🇦 CA | 8233 |
| 7 | 🇮🇹 IT | 7944 |
| 8 | 🇩🇪 DE | 7828 |
| 9 | 🇬🇧 GB | 7037 |
| 10 | 🇯🇵 JP | 6320 |
| 11 | 🇫🇷 FR | 6074 |
| 12 | 🇨🇴 CO | 5272 |
| 13 | 🇲🇽 MX | 4430 |
| 14 | 🇬🇷 GR | 4378 |
| 15 | 🇳🇴 NO | 4051 |
| 16 | 🇨🇭 CH | 4024 |
| 17 | 🇹🇷 TR | 3670 |
| 18 | 🇲🇾 MY | 2838 |
| 19 | 🇵🇱 PL | 2626 |
| 20 | 🇿🇦 ZA | 2483 |
| 21 | 🇳🇿 NZ | 2301 |
| 22 | 🇹🇭 TH | 2222 |
| 23 | 🇰🇷 KR | 2080 |
| 24 | 🇵🇭 PH | 2029 |
| 25 | 🇬🇹 GT | 1999 |
| 26 | 🇲🇦 MA | 1569 |
| 27 | 🇲🇪 ME | 1496 |
| 28 | 🇭🇷 HR | 1409 |
| 29 | 🇳🇱 NL | 1405 |
| 30 | 🇲🇴 MO | 1255 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3173 |
| 2 | Denver International Airport |  | US | 2580 |
| 3 | Tokyo International Airport |  | JP | 2007 |
| 4 | Guaymaral Airport |  | CO | 1928 |
| 5 | Indira Gandhi International Airport |  | IN | 1904 |
| 6 | Harry Reid International Airport |  | US | 1884 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1717 |
| 8 | Zurich Airport |  | CH | 1668 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1612 |
| 10 | La Aurora Airport |  | GT | 1550 |
| 11 | Frankfurt am Main International Airport |  | DE | 1438 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1437 |
| 13 | Chicago O'Hare International Airport |  | US | 1412 |
| 14 | Salt Lake City International Airport |  | US | 1388 |
| 15 | El Dorado International Airport |  | CO | 1387 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1307 |
| 17 | Macau International Airport |  | MO | 1255 |
| 18 | Congonhas Airport |  | BR | 1250 |
| 19 | Madrid Barajas International Airport |  | ES | 1225 |
| 20 | Capua Airport |  | IT | 1215 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1186 |
| 22 | Charlotte/Douglas International Airport |  | US | 1093 |
| 23 | Kuala Lumpur International Airport |  | MY | 1091 |
| 24 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1090 |
| 25 | Sydney Kingsford Smith International Airport |  | AU | 1089 |
| 26 | Charles de Gaulle International Airport |  | FR | 1053 |
| 27 | Bengaluru International Airport |  | IN | 1025 |
| 28 | Malpensa International Airport |  | IT | 1004 |
| 29 | Ninoy Aquino International Airport |  | PH | 950 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 930 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 929 |
| 32 | Barcelona International Airport |  | ES | 916 |
| 33 | Daniel K Inouye International Airport |  | US | 911 |
| 34 | Seattle-Tacoma International Airport |  | US | 888 |
| 35 | Tenerife Norte Airport |  | ES | 883 |
| 36 | Calgary International Airport |  | CA | 875 |
| 37 | Scottsdale Airport |  | US | 873 |
| 38 | Viracopos International Airport |  | BR | 872 |
| 39 | Amsterdam Airport Schiphol |  | NL | 846 |
| 40 | Oslo Gardermoen Airport |  | NO | 841 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 810 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 555 | 21m | 244 km | 2,337.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 373 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 369 | 24m | 225 km | 1,431.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 356 | 1h 9m | 770 km | 4,729.2 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 280 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 275 | 27m | 275 km | 1,303.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 208 | 44m | 241 km | 864.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 207 | 1h 47m | 1,423 km | 5,080.1 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 202 | 26m | 215 km | 748.1 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 200 | 20m | 99 km | 342.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 198 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 187 | 30m | 49 km | 158.1 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 180 | 18m | 144 km | 447.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 180 | 13m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 179 | 31m | 369 km | 1,139.4 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 172 | 1h 1m | 695 km | 2,061.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 172 | 51m | 556 km | 1,648.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N121CD |  | North Las Vegas Airport (KVGT) | Pinewood Airport (0GE0) | 2026-07-26 13:15 UTC | 2026-07-27 00:00 UTC | 10h 45m |
| FDX9746 | FDX | Kep Air Base (VVKP) | Sendai Airport (RJSS) | 2026-07-26 18:57 UTC | 2026-07-26 23:57 UTC | 4h 59m |
| SWA1390 | Southwest Airlines | Hangar Haciendas Airport (AZ90) | Mesa Gateway Airport (KIWA) | 2026-07-26 23:42 UTC | 2026-07-26 23:56 UTC | 14m |
| N491LG |  | Tall Timber Airport (CD28) | Buckley Space Force Base Airport (KBKF) | 2026-07-26 23:22 UTC | 2026-07-26 23:54 UTC | 31m |
| AMX493 | Aeromexico | Seattle-Tacoma International Airport (KSEA) | Grand Canyon Ntl Park Airport (KGCN) | 2026-07-26 21:36 UTC | 2026-07-26 23:53 UTC | 2h 16m |
| AUA907 | Austrian Airlines | Vienna International Airport (LOWW) | Mukhrani Airport (UGMM) | 2026-07-26 20:53 UTC | 2026-07-26 23:52 UTC | 2h 58m |
| VOZ920 | Virgin Australia | Brisbane International Airport (YBBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-07-26 21:56 UTC | 2026-07-26 23:52 UTC | 1h 55m |
| UPS494 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Trenton / Mountain View Airport (CPZ3) | 2026-07-26 21:45 UTC | 2026-07-26 23:50 UTC | 2h 5m |
| AAR224 | AAR | Incheon International Airport (RKSI) | Langton Airstrip (MT60) | 2026-07-26 13:23 UTC | 2026-07-26 23:50 UTC | 10h 27m |
| ASA571 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Hesperia Airport (KL26) | 2026-07-26 21:07 UTC | 2026-07-26 23:48 UTC | 2h 40m |
| N205TA |  | CO98 (CO98) | CO98 (CO98) | 2026-07-26 22:17 UTC | 2026-07-26 23:47 UTC | 1h 30m |
| RYR8593 | Ryanair | Reggio Calabria Airport (LICR) | Modena / Marzaglia Airport (LIPM) | 2026-07-26 21:54 UTC | 2026-07-26 23:47 UTC | 1h 52m |
| N1876S |  | Fremont Municipal Airport (KFET) | 97CO (97CO) | 2026-07-26 19:37 UTC | 2026-07-26 23:46 UTC | 4h 9m |
| LXJ437 | LXJ | Scottsdale Airport (KSDL) | San Francisco International Airport (KSFO) | 2026-07-26 21:29 UTC | 2026-07-26 23:45 UTC | 2h 16m |
| N720EA |  | Pioneer Airport (WS17) | 17LL (17LL) | 2026-07-26 21:58 UTC | 2026-07-26 23:45 UTC | 1h 46m |
| JTZ724 | JTZ | City Of Colorado Springs Municipal Airport (KCOS) | Moore County Airport (KDUX) | 2026-07-26 22:57 UTC | 2026-07-26 23:42 UTC | 44m |
| N21EQ |  | State Technical College Of Missouri Airport (K1H3) | Waldemer Flying W Ranch Airport (MO58) | 2026-07-26 22:44 UTC | 2026-07-26 23:42 UTC | 58m |
| T7MEL |  | Bob Hope Airport (KBUR) | Fire Island Airport (6AK5) | 2026-07-26 18:52 UTC | 2026-07-26 23:42 UTC | 4h 49m |
| QFA760 | Qantas | Perth International Airport (YPPH) | Newdegate Airport (YNDG) | 2026-07-26 22:57 UTC | 2026-07-26 23:42 UTC | 44m |
| AAY1334 | AAY | Orlando Sanford International Airport (KSFB) | Cherokee County Regional Airport (KCKP) | 2026-07-26 20:19 UTC | 2026-07-26 23:42 UTC | 3h 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
