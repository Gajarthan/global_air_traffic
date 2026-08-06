# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_15:18:54_UTC-green)

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

**Latest saved flight:** 2026-08-06 15:18:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-06 15:18:54 UTC

- **174,218** saved flights
- **56,405** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **174,218** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,098,391.5 tonnes** estimated CO2 emissions
- **121,645,884 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6908 |
| 2 | SkyWest Airlines | 6371 |
| 3 | EJA | 3456 |
| 4 | IndiGo | 3047 |
| 5 | Southwest Airlines | 2746 |
| 6 | American Airlines | 2732 |
| 7 | ENY | 2167 |
| 8 | Delta Air Lines | 2064 |
| 9 | LATAM Airlines | 1612 |
| 10 | Lufthansa | 1576 |
| 11 | AZU | 1542 |
| 12 | WIF | 1461 |
| 13 | Vueling | 1431 |
| 14 | LXJ | 1365 |
| 15 | AXM | 1190 |
| 16 | Swiss International | 1186 |
| 17 | easyJet | 1183 |
| 18 | EJU | 1064 |
| 19 | QLK | 1063 |
| 20 | Alaska Airlines | 1058 |
| 21 | All Nippon Airways | 1056 |
| 22 | VIV | 958 |
| 23 | Cathay Pacific | 943 |
| 24 | CXK | 925 |
| 25 | GLO | 920 |
| 26 | AEE | 908 |
| 27 | United Airlines | 905 |
| 28 | Air France | 893 |
| 29 | MXY | 881 |
| 30 | JetBlue | 869 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 150029 |
| 2 | 🇪🇸 ES | 11139 |
| 3 | 🇧🇷 BR | 9933 |
| 4 | 🇦🇺 AU | 9767 |
| 5 | 🇮🇳 IN | 9563 |
| 6 | 🇨🇦 CA | 9537 |
| 7 | 🇮🇹 IT | 8985 |
| 8 | 🇩🇪 DE | 8629 |
| 9 | 🇬🇧 GB | 8063 |
| 10 | 🇯🇵 JP | 6995 |
| 11 | 🇫🇷 FR | 6910 |
| 12 | 🇨🇴 CO | 6419 |
| 13 | 🇬🇷 GR | 5056 |
| 14 | 🇲🇽 MX | 4982 |
| 15 | 🇨🇭 CH | 4600 |
| 16 | 🇳🇴 NO | 4542 |
| 17 | 🇹🇷 TR | 4272 |
| 18 | 🇲🇾 MY | 3092 |
| 19 | 🇵🇱 PL | 2912 |
| 20 | 🇿🇦 ZA | 2808 |
| 21 | 🇹🇭 TH | 2562 |
| 22 | 🇳🇿 NZ | 2523 |
| 23 | 🇵🇭 PH | 2296 |
| 24 | 🇬🇹 GT | 2217 |
| 25 | 🇰🇷 KR | 2185 |
| 26 | 🇲🇦 MA | 1752 |
| 27 | 🇭🇷 HR | 1687 |
| 28 | 🇲🇪 ME | 1593 |
| 29 | 🇳🇱 NL | 1571 |
| 30 | 🇲🇴 MO | 1503 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3596 |
| 2 | Denver International Airport |  | US | 2884 |
| 3 | Tokyo International Airport |  | JP | 2185 |
| 4 | Guaymaral Airport |  | CO | 2163 |
| 5 | Indira Gandhi International Airport |  | IN | 2127 |
| 6 | Harry Reid International Airport |  | US | 2085 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1890 |
| 8 | Zurich Airport |  | CH | 1845 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1826 |
| 10 | La Aurora Airport |  | GT | 1709 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1603 |
| 12 | El Dorado International Airport |  | CO | 1581 |
| 13 | Chicago O'Hare International Airport |  | US | 1573 |
| 14 | Salt Lake City International Airport |  | US | 1562 |
| 15 | Frankfurt am Main International Airport |  | DE | 1540 |
| 16 | Macau International Airport |  | MO | 1503 |
| 17 | Congonhas Airport |  | BR | 1436 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1421 |
| 19 | Capua Airport |  | IT | 1358 |
| 20 | Madrid Barajas International Airport |  | ES | 1356 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1305 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1230 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1216 |
| 24 | Charlotte/Douglas International Airport |  | US | 1200 |
| 25 | Charles de Gaulle International Airport |  | FR | 1181 |
| 26 | Malpensa International Airport |  | IT | 1179 |
| 27 | Kuala Lumpur International Airport |  | MY | 1166 |
| 28 | Bengaluru International Airport |  | IN | 1135 |
| 29 | Norman Y Mineta San Jose International Airport |  | US | 1081 |
| 30 | Ninoy Aquino International Airport |  | PH | 1080 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1073 |
| 32 | Barcelona International Airport |  | ES | 1028 |
| 33 | Daniel K Inouye International Airport |  | US | 1003 |
| 34 | Seattle-Tacoma International Airport |  | US | 1003 |
| 35 | Calgary International Airport |  | CA | 990 |
| 36 | Viracopos International Airport |  | BR | 989 |
| 37 | Reno/Tahoe International Airport |  | US | 987 |
| 38 | Oslo Gardermoen Airport |  | NO | 970 |
| 39 | Tenerife Norte Airport |  | ES | 963 |
| 40 | Scottsdale Airport |  | US | 946 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 895 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 635 | 21m | 244 km | 2,673.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 410 | 24m | 225 km | 1,590.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 407 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 395 | 1h 8m | 770 km | 5,247.3 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 321 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 294 | 27m | 275 km | 1,393.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 262 | 22m | 55 km | 249.0 t |
| 13 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 262 | 44m | 241 km | 1,088.3 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 239 | 1h 48m | 1,423 km | 5,865.4 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 225 | 20m | 250 km | 971.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 223 | 26m | 215 km | 825.9 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 223 | 13m | - | - |
| 19 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 217 | 31m | 49 km | 183.4 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 212 | 20m | 99 km | 363.1 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 209 | 50m | 556 km | 2,003.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 207 | 1h 15m | 961 km | 3,431.1 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 207 | 19m | 144 km | 514.9 t |
| 24 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 206 | 8m | - | - |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 202 | 1h 38m | 1,156 km | 4,029.8 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 202 | 31m | 369 km | 1,285.8 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 202 | 12m | - | - |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 200 | 28m | 152 km | 522.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 195 | 24m | 218 km | 734.6 t |
| 30 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 189 | 43m | 452 km | 1,473.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1315E |  | Ohio State University Airport (KOSU) | Mansfield Lahm Regional Airport (KMFD) | 2026-08-06 14:49 UTC | 2026-08-06 15:18 UTC | 29m |
| N407GM |  | Fuller Airport (TS00) | Fuller Airport (TS00) | 2026-08-06 15:00 UTC | 2026-08-06 15:14 UTC | 13m |
| N750AY |  | CARK (CARK) | CARK (CARK) | 2026-08-06 14:54 UTC | 2026-08-06 15:13 UTC | 18m |
| SHADY09 | SHA | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-08-06 14:53 UTC | 2026-08-06 15:11 UTC | 18m |
| N422U |  | Waco Regional Airport (KACT) | Austin-Bergstrom International Airport (KAUS) | 2026-08-06 14:11 UTC | 2026-08-06 15:09 UTC | 58m |
| N1061D |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-08-06 14:17 UTC | 2026-08-06 15:08 UTC | 51m |
| N571JA |  | Aurora Municipal Airport (KARR) | 1IS5 (1IS5) | 2026-08-06 14:38 UTC | 2026-08-06 15:08 UTC | 29m |
| ARCAS31 | ARC | Danaher Airport (7TX0) | TX20 (TX20) | 2026-08-06 14:51 UTC | 2026-08-06 15:06 UTC | 15m |
| N68754 |  | Lehigh Valley International Airport (KABE) | Lehigh Valley International Airport (KABE) | 2026-08-06 14:37 UTC | 2026-08-06 15:05 UTC | 28m |
| N3015D |  | Anoka County/Blaine (Janes Field) Airport (KANE) | Princeton Municipal Airport (KPNM) | 2026-08-06 14:34 UTC | 2026-08-06 15:04 UTC | 29m |
| N84234 |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-08-06 14:46 UTC | 2026-08-06 15:01 UTC | 15m |
| N3356V |  | Cleveland Regional Jetport Airport (KRZR) | Cleveland Regional Jetport Airport (KRZR) | 2026-08-06 14:44 UTC | 2026-08-06 15:01 UTC | 16m |
| HBZVS | HBZ | St Stephan Airport (LSTS) | Courchevel Airport (LFLJ) | 2026-08-06 14:02 UTC | 2026-08-06 14:55 UTC | 52m |
| N559SH |  | Gold King Creek Airport (PAAN) | Healy River Airport (PAHV) | 2026-08-06 14:48 UTC | 2026-08-06 14:54 UTC | 6m |
| N570JA |  | Aurora Municipal Airport (KARR) | Wade Airport (56LL) | 2026-08-06 14:07 UTC | 2026-08-06 14:52 UTC | 45m |
| N7367E |  | Shiprock Airstrip (K5V5) | Blanding Municipal Airport (KBDG) | 2026-08-06 14:28 UTC | 2026-08-06 14:51 UTC | 22m |
| CNS308 | CNS | Portsmouth International At Pease Airport (KPSM) | Concord Municipal Airport (KCON) | 2026-08-06 14:09 UTC | 2026-08-06 14:48 UTC | 39m |
| NDU54 | NDU | Saure Airport (NA02) | 7NA0 (7NA0) | 2026-08-06 14:22 UTC | 2026-08-06 14:47 UTC | 25m |
| N7384S |  | Double Eagle Ii Airport (KAEG) | Santa Fe Regional Airport (KSAF) | 2026-08-06 14:25 UTC | 2026-08-06 14:47 UTC | 22m |
| N784LU |  | Lynchburg Regional/Preston Glenn Field (KLYH) | Skovhus Airport (VA24) | 2026-08-06 14:38 UTC | 2026-08-06 14:47 UTC | 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
