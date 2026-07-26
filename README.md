# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_21:50:50_UTC-green)

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

**Latest saved flight:** 2026-07-26 21:50:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-26 21:50:50 UTC

- **153,321** saved flights
- **50,846** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **153,321** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,834,148.8 tonnes** estimated CO2 emissions
- **106,327,466 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6194 |
| 2 | SkyWest Airlines | 5610 |
| 3 | EJA | 3044 |
| 4 | IndiGo | 2729 |
| 5 | American Airlines | 2430 |
| 6 | Southwest Airlines | 2330 |
| 7 | ENY | 1917 |
| 8 | Delta Air Lines | 1798 |
| 9 | Lufthansa | 1488 |
| 10 | LATAM Airlines | 1423 |
| 11 | AZU | 1332 |
| 12 | WIF | 1290 |
| 13 | Vueling | 1281 |
| 14 | LXJ | 1181 |
| 15 | AXM | 1090 |
| 16 | Swiss International | 1072 |
| 17 | easyJet | 1003 |
| 18 | All Nippon Airways | 960 |
| 19 | Alaska Airlines | 955 |
| 20 | EJU | 942 |
| 21 | QLK | 942 |
| 22 | VIV | 846 |
| 23 | CXK | 818 |
| 24 | MXY | 808 |
| 25 | AEE | 807 |
| 26 | GLO | 799 |
| 27 | Air France | 798 |
| 28 | JetBlue | 794 |
| 29 | United Airlines | 787 |
| 30 | Cathay Pacific | 784 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 132271 |
| 2 | 🇪🇸 ES | 9913 |
| 3 | 🇧🇷 BR | 8707 |
| 4 | 🇦🇺 AU | 8600 |
| 5 | 🇮🇳 IN | 8578 |
| 6 | 🇨🇦 CA | 8204 |
| 7 | 🇮🇹 IT | 7936 |
| 8 | 🇩🇪 DE | 7827 |
| 9 | 🇬🇧 GB | 7034 |
| 10 | 🇯🇵 JP | 6314 |
| 11 | 🇫🇷 FR | 6071 |
| 12 | 🇨🇴 CO | 5262 |
| 13 | 🇲🇽 MX | 4424 |
| 14 | 🇬🇷 GR | 4374 |
| 15 | 🇳🇴 NO | 4051 |
| 16 | 🇨🇭 CH | 4024 |
| 17 | 🇹🇷 TR | 3666 |
| 18 | 🇲🇾 MY | 2838 |
| 19 | 🇵🇱 PL | 2625 |
| 20 | 🇿🇦 ZA | 2483 |
| 21 | 🇳🇿 NZ | 2293 |
| 22 | 🇹🇭 TH | 2221 |
| 23 | 🇰🇷 KR | 2079 |
| 24 | 🇵🇭 PH | 2025 |
| 25 | 🇬🇹 GT | 1998 |
| 26 | 🇲🇦 MA | 1568 |
| 27 | 🇲🇪 ME | 1495 |
| 28 | 🇭🇷 HR | 1409 |
| 29 | 🇳🇱 NL | 1405 |
| 30 | 🇲🇴 MO | 1255 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3160 |
| 2 | Denver International Airport |  | US | 2572 |
| 3 | Tokyo International Airport |  | JP | 2006 |
| 4 | Guaymaral Airport |  | CO | 1927 |
| 5 | Indira Gandhi International Airport |  | IN | 1904 |
| 6 | Harry Reid International Airport |  | US | 1880 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1717 |
| 8 | Zurich Airport |  | CH | 1668 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1603 |
| 10 | La Aurora Airport |  | GT | 1549 |
| 11 | Frankfurt am Main International Airport |  | DE | 1438 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1434 |
| 13 | Chicago O'Hare International Airport |  | US | 1407 |
| 14 | Salt Lake City International Airport |  | US | 1385 |
| 15 | El Dorado International Airport |  | CO | 1383 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1303 |
| 17 | Macau International Airport |  | MO | 1255 |
| 18 | Congonhas Airport |  | BR | 1245 |
| 19 | Madrid Barajas International Airport |  | ES | 1225 |
| 20 | Capua Airport |  | IT | 1215 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1185 |
| 22 | Kuala Lumpur International Airport |  | MY | 1091 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1087 |
| 24 | Charlotte/Douglas International Airport |  | US | 1086 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1085 |
| 26 | Charles de Gaulle International Airport |  | FR | 1052 |
| 27 | Bengaluru International Airport |  | IN | 1025 |
| 28 | Malpensa International Airport |  | IT | 1003 |
| 29 | Ninoy Aquino International Airport |  | PH | 948 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 929 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 924 |
| 32 | Barcelona International Airport |  | ES | 915 |
| 33 | Daniel K Inouye International Airport |  | US | 911 |
| 34 | Tenerife Norte Airport |  | ES | 883 |
| 35 | Seattle-Tacoma International Airport |  | US | 882 |
| 36 | Scottsdale Airport |  | US | 871 |
| 37 | Calgary International Airport |  | CA | 870 |
| 38 | Viracopos International Airport |  | BR | 867 |
| 39 | Amsterdam Airport Schiphol |  | NL | 846 |
| 40 | Oslo Gardermoen Airport |  | NO | 841 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 810 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 555 | 21m | 244 km | 2,337.0 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 373 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 368 | 24m | 225 km | 1,427.7 t |
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
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 187 | 27m | 152 km | 488.7 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 186 | 30m | 49 km | 157.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 182 | 1h 15m | 961 km | 3,016.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 180 | 18m | 144 km | 447.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 179 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 172 | 1h 39m | 1,156 km | 3,431.3 t |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 172 | 51m | 556 km | 1,648.8 t |
| 29 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 171 | 1h 1m | 695 km | 2,049.8 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SD1 |  | Tri-County Aerodrome (48TX) | Tri-County Aerodrome (48TX) | 2026-07-26 20:54 UTC | 2026-07-26 21:50 UTC | 56m |
| N24143 |  | Merrill Field (PAMR) | Sky Harbor Airport (9AK5) | 2026-07-26 21:16 UTC | 2026-07-26 21:47 UTC | 31m |
| N1605M |  | Camarillo Airport (KCMA) | Santa Barbara Municipal Airport (KSBA) | 2026-07-26 21:25 UTC | 2026-07-26 21:43 UTC | 18m |
| N642RG |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-26 20:37 UTC | 2026-07-26 21:41 UTC | 1h 4m |
| PNC0619 | PNC | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-07-26 21:07 UTC | 2026-07-26 21:38 UTC | 31m |
| FDY39 | FDY | Upolu Airport (PHUP) | Ellison Onizuka Kona International At Keahole Airport (PHKO) | 2026-07-26 21:07 UTC | 2026-07-26 21:33 UTC | 26m |
| N10TF |  | Newton Municipal-Earl Johnson Field (KTNU) | Newton Municipal-Earl Johnson Field (KTNU) | 2026-07-26 20:55 UTC | 2026-07-26 21:33 UTC | 37m |
| N435SG |  | Swains Creek Airport (UT00) | Scottsdale Airport (KSDL) | 2026-07-26 20:38 UTC | 2026-07-26 21:32 UTC | 54m |
| N9027C |  | Pine Island Airport (7NC2) | Northeastern Regional Airport (KEDE) | 2026-07-26 20:46 UTC | 2026-07-26 21:30 UTC | 44m |
| N146SM |  | San Luis Obispo County Regional Airport (KSBP) | Shepard Strip (07ID) | 2026-07-26 19:57 UTC | 2026-07-26 21:24 UTC | 1h 27m |
| N997SE |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-26 20:46 UTC | 2026-07-26 21:23 UTC | 37m |
| N737BU |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-26 20:40 UTC | 2026-07-26 21:20 UTC | 39m |
| TEXSIL | TEX | RNZAF Base Ohakea (NZOH) | Wanganui Airport (NZWU) | 2026-07-26 20:52 UTC | 2026-07-26 21:18 UTC | 26m |
| TRF543 | TRF | Addison Airport (KADS) | Addison Airport (KADS) | 2026-07-26 19:46 UTC | 2026-07-26 21:18 UTC | 1h 31m |
| EZY858W | easyJet | Bristol International Airport (EGGD) | Glasgow International Airport (EGPF) | 2026-07-26 20:20 UTC | 2026-07-26 21:18 UTC | 57m |
| SWA4887 | Southwest Airlines | Portland International Airport (KPDX) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-26 19:43 UTC | 2026-07-26 21:17 UTC | 1h 34m |
| ANZ266L | ANZ | Auckland International Airport (NZAA) | Kaikohe Airport (NZKO) | 2026-07-26 20:50 UTC | 2026-07-26 21:16 UTC | 25m |
| N950TT |  | Wheeler Army Air Field (PHHI) | Kawaihapai Airfield (PHDH) | 2026-07-26 21:01 UTC | 2026-07-26 21:15 UTC | 14m |
| N491LG |  | Tall Timber Airport (CD28) | Marshdale Airport (CO52) | 2026-07-26 20:30 UTC | 2026-07-26 21:15 UTC | 45m |
| CWA922 | CWA | Calgary International Airport (CYYC) | Bow Island Airport (CEF3) | 2026-07-26 20:44 UTC | 2026-07-26 21:14 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
