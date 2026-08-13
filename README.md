# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_19:03:23_UTC-green)

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

**Latest saved flight:** 2026-08-13 19:03:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-13 19:03:23 UTC

- **193,251** saved flights
- **60,821** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **193,251** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,310,100.8 tonnes** estimated CO2 emissions
- **133,918,889 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7685 |
| 2 | SkyWest Airlines | 6970 |
| 3 | EJA | 3809 |
| 4 | IndiGo | 3343 |
| 5 | Southwest Airlines | 3008 |
| 6 | American Airlines | 2988 |
| 7 | ENY | 2394 |
| 8 | Delta Air Lines | 2279 |
| 9 | LATAM Airlines | 1812 |
| 10 | AZU | 1744 |
| 11 | Lufthansa | 1672 |
| 12 | Vueling | 1609 |
| 13 | WIF | 1601 |
| 14 | LXJ | 1527 |
| 15 | easyJet | 1334 |
| 16 | Swiss International | 1315 |
| 17 | AXM | 1258 |
| 18 | EJU | 1191 |
| 19 | QLK | 1186 |
| 20 | All Nippon Airways | 1168 |
| 21 | Alaska Airlines | 1146 |
| 22 | VIV | 1064 |
| 23 | GLO | 1040 |
| 24 | Air France | 1011 |
| 25 | PGT | 1002 |
| 26 | AEE | 990 |
| 27 | CXK | 989 |
| 28 | United Airlines | 983 |
| 29 | WMT | 961 |
| 30 | Wizz Air | 960 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 164493 |
| 2 | 🇪🇸 ES | 12481 |
| 3 | 🇧🇷 BR | 11105 |
| 4 | 🇦🇺 AU | 10810 |
| 5 | 🇨🇦 CA | 10575 |
| 6 | 🇮🇳 IN | 10467 |
| 7 | 🇮🇹 IT | 10048 |
| 8 | 🇩🇪 DE | 9578 |
| 9 | 🇬🇧 GB | 9048 |
| 10 | 🇯🇵 JP | 7884 |
| 11 | 🇫🇷 FR | 7726 |
| 12 | 🇨🇴 CO | 7497 |
| 13 | 🇬🇷 GR | 5654 |
| 14 | 🇲🇽 MX | 5466 |
| 15 | 🇨🇭 CH | 5204 |
| 16 | 🇹🇷 TR | 5203 |
| 17 | 🇳🇴 NO | 4959 |
| 18 | 🇲🇾 MY | 3297 |
| 19 | 🇿🇦 ZA | 3264 |
| 20 | 🇵🇱 PL | 3182 |
| 21 | 🇹🇭 TH | 2991 |
| 22 | 🇳🇿 NZ | 2710 |
| 23 | 🇵🇭 PH | 2536 |
| 24 | 🇬🇹 GT | 2462 |
| 25 | 🇰🇷 KR | 2349 |
| 26 | 🇭🇷 HR | 2005 |
| 27 | 🇲🇦 MA | 1961 |
| 28 | 🇳🇱 NL | 1739 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1556 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4010 |
| 2 | Denver International Airport |  | US | 3163 |
| 3 | Tokyo International Airport |  | JP | 2424 |
| 4 | Guaymaral Airport |  | CO | 2405 |
| 5 | Indira Gandhi International Airport |  | IN | 2358 |
| 6 | Harry Reid International Airport |  | US | 2242 |
| 7 | Zurich Airport |  | CH | 2051 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2040 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1996 |
| 10 | La Aurora Airport |  | GT | 1893 |
| 11 | El Dorado International Airport |  | CO | 1754 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1736 |
| 13 | Salt Lake City International Airport |  | US | 1717 |
| 14 | Chicago O'Hare International Airport |  | US | 1691 |
| 15 | Frankfurt am Main International Airport |  | DE | 1638 |
| 16 | Congonhas Airport |  | BR | 1616 |
| 17 | Macau International Airport |  | MO | 1528 |
| 18 | Madrid Barajas International Airport |  | ES | 1526 |
| 19 | Capua Airport |  | IT | 1488 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1487 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1426 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1386 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1342 |
| 24 | Malpensa International Airport |  | IT | 1335 |
| 25 | Charles de Gaulle International Airport |  | FR | 1327 |
| 26 | Charlotte/Douglas International Airport |  | US | 1287 |
| 27 | Bengaluru International Airport |  | IN | 1236 |
| 28 | Kuala Lumpur International Airport |  | MY | 1231 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1206 |
| 30 | Ninoy Aquino International Airport |  | PH | 1199 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1180 |
| 32 | Barcelona International Airport |  | ES | 1156 |
| 33 | Viracopos International Airport |  | BR | 1123 |
| 34 | Seattle-Tacoma International Airport |  | US | 1106 |
| 35 | Calgary International Airport |  | CA | 1105 |
| 36 | Reno/Tahoe International Airport |  | US | 1102 |
| 37 | Oslo Gardermoen Airport |  | NO | 1086 |
| 38 | Daniel K Inouye International Airport |  | US | 1082 |
| 39 | Tenerife Norte Airport |  | ES | 1061 |
| 40 | Vitoria/Foronda Airport |  | ES | 1058 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 994 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 710 | 21m | 244 km | 2,989.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 469 | 1h 7m | 770 km | 6,230.3 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 454 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 445 | 24m | 225 km | 1,726.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 326 | 27m | 275 km | 1,544.8 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 314 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 309 | 14m | 114 km | 606.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 288 | 44m | 241 km | 1,196.3 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 278 | 1h 49m | 1,423 km | 6,822.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 276 | 22m | 55 km | 262.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 259 | 20m | 250 km | 1,118.7 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 242 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 241 | 27m | 215 km | 892.6 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 235 | 24m | 218 km | 885.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 235 | 1h 15m | 961 km | 3,895.2 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 235 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 228 | 19m | 144 km | 567.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 227 | 1h 38m | 1,156 km | 4,528.6 t |
| 27 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 220 | 31m | 369 km | 1,400.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 211 | 28m | 152 km | 551.4 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 209 | 1h 48m | 1,304 km | 4,702.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4640B |  | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | Raleigh Executive Jetport At Sanford-Lee County Airport (KTTA) | 2026-08-13 17:50 UTC | 2026-08-13 19:03 UTC | 1h 12m |
| CXK191 | CXK | Brackett Field (KPOC) | Riverside Airport (KRAL) | 2026-08-13 18:33 UTC | 2026-08-13 19:01 UTC | 27m |
| N757LE |  | Lake Elmo Airport (K21D) | St Paul Downtown Holman Field (KSTP) | 2026-08-13 18:30 UTC | 2026-08-13 18:59 UTC | 28m |
| N92DV |  | Vance Brand Airport (KLMO) | Erie Municipal Airport (KEIK) | 2026-08-13 18:41 UTC | 2026-08-13 18:59 UTC | 17m |
| LXJ429 | LXJ | Tampa International Airport (KTPA) | Addison Airport (KADS) | 2026-08-13 16:52 UTC | 2026-08-13 18:55 UTC | 2h 2m |
| N948HC |  | T W Spear Memorial Airport (4AL9) | West Georgia Regional/O V Gray Field (KCTJ) | 2026-08-13 18:01 UTC | 2026-08-13 18:51 UTC | 50m |
| N8351L |  | Sahoma Lake Airport (03OK) | William R Pogue Municipal Airport (KOWP) | 2026-08-13 18:34 UTC | 2026-08-13 18:51 UTC | 16m |
| N70378 |  | Destin Executive Airport (KDTS) | Dugger Field (0FD3) | 2026-08-13 18:40 UTC | 2026-08-13 18:47 UTC | 6m |
| THY1DY | Turkish Airlines | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-08-13 16:35 UTC | 2026-08-13 18:46 UTC | 2h 11m |
| N5102D |  | Wadsworth Municipal Airport (K3G3) | Wayne County Airport (KBJJ) | 2026-08-13 18:22 UTC | 2026-08-13 18:46 UTC | 24m |
| TRP4 | TRP | Bunting's Field (4MD1) | Ocean City Municipal Airport (KOXB) | 2026-08-13 18:40 UTC | 2026-08-13 18:45 UTC | 4m |
| ADY431 | ADY | Abu Dhabi International Airport (OMAA) | Hulwan (HE15) | 2026-08-13 15:52 UTC | 2026-08-13 18:45 UTC | 2h 52m |
| HK5271G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-08-13 18:34 UTC | 2026-08-13 18:45 UTC | 10m |
| N574ND |  | Ormond Beach Municipal Airport (KOMN) | Kissimmee Gateway Airport (KISM) | 2026-08-13 17:59 UTC | 2026-08-13 18:44 UTC | 44m |
| N76SJ |  | Dayton Valley Airpark (KA34) | Silver Springs Airport (KSPZ) | 2026-08-13 18:02 UTC | 2026-08-13 18:43 UTC | 41m |
| GFY1124 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-13 17:53 UTC | 2026-08-13 18:43 UTC | 49m |
| N704MD |  | Mule Creek Airport (CBS4) | Airkat Airpark (9AA9) | 2026-08-13 18:25 UTC | 2026-08-13 18:42 UTC | 17m |
| MUSL | MUS | Joint Base Andrews Airport (KADW) | Ty-Ti-To Airport (MD83) | 2026-08-13 18:30 UTC | 2026-08-13 18:41 UTC | 11m |
| MSR888 | EgyptAir | Cairo International Airport (HECA) | HE30 (HE30) | 2026-08-13 08:24 UTC | 2026-08-13 18:36 UTC | 10h 11m |
| WIF1DJ | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-13 18:18 UTC | 2026-08-13 18:34 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
