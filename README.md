# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_23:04:57_UTC-green)

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

**Latest saved flight:** 2026-08-16 23:04:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 23:04:57 UTC

- **206,565** saved flights
- **65,863** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,565** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,484,453.0 tonnes** estimated CO2 emissions
- **144,026,258 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8147 |
| 2 | SkyWest Airlines | 7443 |
| 3 | EJA | 4026 |
| 4 | IndiGo | 3522 |
| 5 | American Airlines | 3448 |
| 6 | Southwest Airlines | 3319 |
| 7 | Delta Air Lines | 2658 |
| 8 | ENY | 2580 |
| 9 | LATAM Airlines | 1943 |
| 10 | AZU | 1870 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1709 |
| 13 | WIF | 1657 |
| 14 | LXJ | 1636 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1376 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1303 |
| 19 | Alaska Airlines | 1279 |
| 20 | QLK | 1265 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1136 |
| 24 | GLO | 1119 |
| 25 | Air France | 1103 |
| 26 | PGT | 1102 |
| 27 | JetBlue | 1059 |
| 28 | AEE | 1052 |
| 29 | WMT | 1040 |
| 30 | CXK | 1018 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175671 |
| 2 | 🇪🇸 ES | 13186 |
| 3 | 🇧🇷 BR | 11847 |
| 4 | 🇦🇺 AU | 11505 |
| 5 | 🇨🇦 CA | 11419 |
| 6 | 🇮🇳 IN | 10993 |
| 7 | 🇮🇹 IT | 10767 |
| 8 | 🇩🇪 DE | 10208 |
| 9 | 🇬🇧 GB | 9628 |
| 10 | 🇯🇵 JP | 8455 |
| 11 | 🇨🇴 CO | 8227 |
| 12 | 🇫🇷 FR | 8167 |
| 13 | 🇬🇷 GR | 6069 |
| 14 | 🇹🇷 TR | 5854 |
| 15 | 🇲🇽 MX | 5813 |
| 16 | 🇨🇭 CH | 5513 |
| 17 | 🇳🇴 NO | 5138 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3403 |
| 21 | 🇹🇭 TH | 3247 |
| 22 | 🇳🇿 NZ | 2847 |
| 23 | 🇵🇭 PH | 2733 |
| 24 | 🇬🇹 GT | 2640 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2209 |
| 27 | 🇲🇦 MA | 2081 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1742 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4358 |
| 2 | Denver International Airport |  | US | 3383 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Guaymaral Airport |  | CO | 2494 |
| 5 | Indira Gandhi International Airport |  | IN | 2494 |
| 6 | Harry Reid International Airport |  | US | 2336 |
| 7 | Zurich Airport |  | CH | 2154 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2151 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2147 |
| 10 | La Aurora Airport |  | GT | 2010 |
| 11 | Chicago O'Hare International Airport |  | US | 1913 |
| 12 | El Dorado International Airport |  | CO | 1890 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1846 |
| 14 | Salt Lake City International Airport |  | US | 1829 |
| 15 | Congonhas Airport |  | BR | 1726 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1618 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1576 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1572 |
| 20 | Capua Airport |  | IT | 1568 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1499 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1437 |
| 24 | Malpensa International Airport |  | IT | 1425 |
| 25 | Charles de Gaulle International Airport |  | FR | 1413 |
| 26 | Charlotte/Douglas International Airport |  | US | 1412 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1295 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1280 |
| 30 | Bengaluru International Airport |  | IN | 1276 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1250 |
| 32 | Seattle-Tacoma International Airport |  | US | 1229 |
| 33 | Barcelona International Airport |  | ES | 1229 |
| 34 | Viracopos International Airport |  | BR | 1198 |
| 35 | Calgary International Airport |  | CA | 1171 |
| 36 | Reno/Tahoe International Airport |  | US | 1142 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1107 |
| 40 | Tenerife Norte Airport |  | ES | 1105 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 470 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 403 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 256 | 19m | 99 km | 438.5 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 244 | 1h 37m | 1,156 km | 4,867.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 235 | 31m | 369 km | 1,495.8 t |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 225 | 28m | 152 km | 588.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 222 | 1h 49m | 1,304 km | 4,994.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N20AW |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-16 22:34 UTC | 2026-08-16 23:04 UTC | 30m |
| CXK556 | CXK | Riverside Airport (KRAL) | Whiteman Airport (KWHP) | 2026-08-16 22:03 UTC | 2026-08-16 22:49 UTC | 45m |
| N805FA |  | Truckee-Tahoe Airport (KTRK) | Santa Monica Municipal Airport (KSMO) | 2026-08-16 21:22 UTC | 2026-08-16 22:48 UTC | 1h 26m |
| N36HF |  | KHTO (KHTO) | Teterboro Airport (KTEB) | 2026-08-16 22:03 UTC | 2026-08-16 22:45 UTC | 42m |
| PAT825 | PAT | K4SD (K4SD) | Sacramento Mather Airport (KMHR) | 2026-08-16 21:10 UTC | 2026-08-16 22:42 UTC | 1h 31m |
| UPS5768 | UPS | Louisville Muhammad Ali International Airport (KSDF) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-16 20:55 UTC | 2026-08-16 22:35 UTC | 1h 39m |
| XBNLT | XBN | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-16 21:38 UTC | 2026-08-16 22:31 UTC | 53m |
| N622TP |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-08-16 21:58 UTC | 2026-08-16 22:31 UTC | 32m |
| N809GG |  | Miami-Opa Locka Executive Airport (KOPF) | San Andros Airport (MYAN) | 2026-08-16 22:03 UTC | 2026-08-16 22:29 UTC | 26m |
| N182KQ |  | Thompson Airport (WA61) | Boeing Field/King County International Airport (KBFI) | 2026-08-16 22:19 UTC | 2026-08-16 22:28 UTC | 8m |
| N999VP |  | IS95 (IS95) | 7IL8 (7IL8) | 2026-08-16 22:16 UTC | 2026-08-16 22:27 UTC | 11m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-16 22:08 UTC | 2026-08-16 22:24 UTC | 16m |
| GFY1124 | GFY | Portland-Hillsboro Airport (KHIO) | Portland-Hillsboro Airport (KHIO) | 2026-08-16 21:39 UTC | 2026-08-16 22:22 UTC | 43m |
| N821TN |  | Kansas City Downtown/Wheeler Field (KMKC) | Marshall Memorial Municipal Airport (KMHL) | 2026-08-16 22:08 UTC | 2026-08-16 22:20 UTC | 11m |
| N820KE |  | Orcas Island Airport (KORS) | Anacortes Airport (K74S) | 2026-08-16 22:12 UTC | 2026-08-16 22:19 UTC | 7m |
| AAL2655 | American Airlines | Portland International Airport (KPDX) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-16 19:07 UTC | 2026-08-16 22:18 UTC | 3h 11m |
| N330V |  | Kintail Farm Airport (GA00) | Kintail Farm Airport (GA00) | 2026-08-16 22:05 UTC | 2026-08-16 22:18 UTC | 12m |
| N309AG |  | Henderson Executive Airport (KHND) | Converse Farm Airport (SN47) | 2026-08-16 19:57 UTC | 2026-08-16 22:17 UTC | 2h 20m |
| VOE83UD | VOE | Pisa / San Giusto - Galileo Galilei International Airport (LIRP) | Corte Airport (LFKT) | 2026-08-16 21:50 UTC | 2026-08-16 22:16 UTC | 25m |
| CXK685 | CXK | Conroe/North Houston Regional Airport (KCXO) | Conroe/North Houston Regional Airport (KCXO) | 2026-08-16 21:12 UTC | 2026-08-16 22:15 UTC | 1h 3m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
