# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_20:58:32_UTC-green)

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

**Latest saved flight:** 2026-08-20 20:58:32 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-20 20:58:32 UTC

- **220,376** saved flights
- **69,149** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **220,376** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,653,480.2 tonnes** estimated CO2 emissions
- **153,824,937 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8832 |
| 2 | SkyWest Airlines | 7850 |
| 3 | EJA | 4275 |
| 4 | IndiGo | 3732 |
| 5 | American Airlines | 3655 |
| 6 | Southwest Airlines | 3483 |
| 7 | Delta Air Lines | 2841 |
| 8 | ENY | 2714 |
| 9 | LATAM Airlines | 2092 |
| 10 | AZU | 2017 |
| 11 | Vueling | 1856 |
| 12 | Lufthansa | 1830 |
| 13 | WIF | 1763 |
| 14 | LXJ | 1742 |
| 15 | easyJet | 1528 |
| 16 | Swiss International | 1466 |
| 17 | AXM | 1445 |
| 18 | United Airlines | 1387 |
| 19 | QLK | 1375 |
| 20 | EJU | 1374 |
| 21 | Alaska Airlines | 1342 |
| 22 | All Nippon Airways | 1319 |
| 23 | GLO | 1204 |
| 24 | VIV | 1202 |
| 25 | Air France | 1196 |
| 26 | PGT | 1194 |
| 27 | WMT | 1162 |
| 28 | Wizz Air | 1124 |
| 29 | JetBlue | 1116 |
| 30 | AEE | 1104 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 185494 |
| 2 | 🇪🇸 ES | 14129 |
| 3 | 🇧🇷 BR | 12722 |
| 4 | 🇦🇺 AU | 12419 |
| 5 | 🇨🇦 CA | 12163 |
| 6 | 🇮🇹 IT | 11733 |
| 7 | 🇮🇳 IN | 11635 |
| 8 | 🇩🇪 DE | 10889 |
| 9 | 🇬🇧 GB | 10353 |
| 10 | 🇨🇴 CO | 9047 |
| 11 | 🇯🇵 JP | 8963 |
| 12 | 🇫🇷 FR | 8781 |
| 13 | 🇬🇷 GR | 6432 |
| 14 | 🇹🇷 TR | 6342 |
| 15 | 🇲🇽 MX | 6120 |
| 16 | 🇨🇭 CH | 5829 |
| 17 | 🇳🇴 NO | 5481 |
| 18 | 🇲🇾 MY | 3820 |
| 19 | 🇿🇦 ZA | 3763 |
| 20 | 🇵🇱 PL | 3656 |
| 21 | 🇹🇭 TH | 3655 |
| 22 | 🇳🇿 NZ | 3041 |
| 23 | 🇵🇭 PH | 2961 |
| 24 | 🇬🇹 GT | 2785 |
| 25 | 🇰🇷 KR | 2635 |
| 26 | 🇭🇷 HR | 2446 |
| 27 | 🇲🇦 MA | 2218 |
| 28 | 🇳🇱 NL | 1959 |
| 29 | 🇲🇪 ME | 1949 |
| 30 | 🇮🇩 ID | 1866 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4623 |
| 2 | Denver International Airport |  | US | 3596 |
| 3 | Tokyo International Airport |  | JP | 2689 |
| 4 | Indira Gandhi International Airport |  | IN | 2668 |
| 5 | Guaymaral Airport |  | CO | 2604 |
| 6 | Harry Reid International Airport |  | US | 2422 |
| 7 | Zurich Airport |  | CH | 2288 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2266 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2239 |
| 10 | La Aurora Airport |  | GT | 2122 |
| 11 | El Dorado International Airport |  | CO | 2060 |
| 12 | Chicago O'Hare International Airport |  | US | 2018 |
| 13 | Salt Lake City International Airport |  | US | 1942 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1906 |
| 15 | Congonhas Airport |  | BR | 1863 |
| 16 | Frankfurt am Main International Airport |  | DE | 1797 |
| 17 | Madrid Barajas International Airport |  | ES | 1731 |
| 18 | Capua Airport |  | IT | 1684 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1654 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1624 |
| 21 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1619 |
| 22 | Macau International Airport |  | MO | 1582 |
| 23 | Malpensa International Airport |  | IT | 1548 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1542 |
| 25 | Charles de Gaulle International Airport |  | FR | 1518 |
| 26 | Charlotte/Douglas International Airport |  | US | 1466 |
| 27 | Ninoy Aquino International Airport |  | PH | 1408 |
| 28 | Kuala Lumpur International Airport |  | MY | 1403 |
| 29 | Barcelona International Airport |  | ES | 1352 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1337 |
| 31 | Bengaluru International Airport |  | IN | 1325 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1310 |
| 33 | Seattle-Tacoma International Airport |  | US | 1301 |
| 34 | Viracopos International Airport |  | BR | 1290 |
| 35 | Calgary International Airport |  | CA | 1243 |
| 36 | Enrique Olaya Herrera Airport |  | CO | 1225 |
| 37 | Oslo Gardermoen Airport |  | NO | 1224 |
| 38 | Vitoria/Foronda Airport |  | ES | 1224 |
| 39 | Don Mueang International Airport |  | TH | 1202 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1183 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1063 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 790 | 21m | 244 km | 3,326.5 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 543 | 1h 7m | 770 km | 7,213.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 521 | 24m | 225 km | 2,021.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 498 | 12m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 495 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 371 | 27m | 275 km | 1,758.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 350 | 33m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 325 | 1h 50m | 1,423 km | 7,976.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 324 | 44m | 241 km | 1,345.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 297 | 22m | 55 km | 282.3 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 292 | 21m | 250 km | 1,261.3 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 274 | 1h 38m | 1,156 km | 5,466.2 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 273 | 24m | 218 km | 1,028.5 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 272 | 27m | 215 km | 1,007.4 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 272 | 19m | 99 km | 465.9 t |
| 20 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 259 | 1h 14m | 961 km | 4,293.1 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 25 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 251 | 44m | 555 km | 2,403.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 251 | 19m | 144 km | 624.3 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 247 | 12m | - | - |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 237 | 1h 49m | 1,304 km | 5,331.9 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 232 | 28m | 152 km | 606.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BULETXX | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-08-20 20:02 UTC | 2026-08-20 20:58 UTC | 55m |
| QTR8394 | Qatar Airways | Hamad International Airport (OTHH) | Zhuhai Airport (ZGSD) | 2026-08-20 13:18 UTC | 2026-08-20 20:56 UTC | 7h 38m |
| N5679U |  | Flying Frog Field (91GA) | Ashland/Lineville Airport (K26A) | 2026-08-20 20:21 UTC | 2026-08-20 20:49 UTC | 28m |
| NIT265 | NIT | Atlanta Regional Falcon Field (KFFC) | W H 'Bud' Barron Airport (KDBN) | 2026-08-20 19:43 UTC | 2026-08-20 20:47 UTC | 1h 4m |
| BOX712 | BOX | Dubai International Airport (OMDB) | Macau International Airport (VMMC) | 2026-08-20 13:41 UTC | 2026-08-20 20:46 UTC | 7h 5m |
|  |  | Battle Creek Executive At Kellogg Field (KBTL) | Battle Creek Executive At Kellogg Field (KBTL) | 2026-08-20 20:41 UTC | 2026-08-20 20:41 UTC | 0m |
| CPA843 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-08-20 06:13 UTC | 2026-08-20 20:40 UTC | 14h 27m |
| TAP93ZS | TAP Air Portugal | Zurich Airport (LSZH) | Lisbon Portela Airport (LPPT) | 2026-08-20 17:29 UTC | 2026-08-20 20:39 UTC | 3h 10m |
| CXK490 | CXK | Sacramento Executive Airport (KSAC) | Yolo County Airport (KDWA) | 2026-08-20 19:40 UTC | 2026-08-20 20:36 UTC | 55m |
| N677TX |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-08-20 19:58 UTC | 2026-08-20 20:33 UTC | 35m |
| EVA316 | EVA Air | Brisbane International Airport (YBBN) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-20 12:30 UTC | 2026-08-20 20:32 UTC | 8h 2m |
| N840SW |  | Witham Field (KSUA) | Witham Field (KSUA) | 2026-08-20 20:27 UTC | 2026-08-20 20:32 UTC | 4m |
| N248PA |  | Lanai Airport (PHNY) | Kawaihapai Airfield (PHDH) | 2026-08-20 20:16 UTC | 2026-08-20 20:28 UTC | 11m |
| N101PG |  | Livermore Municipal Airport (KLVK) | Reno/Tahoe International Airport (KRNO) | 2026-08-20 19:51 UTC | 2026-08-20 20:25 UTC | 33m |
| N150YD |  | Hector International Airport (KFAR) | Crookston Municipal/Kirkwood Field (KCKN) | 2026-08-20 20:09 UTC | 2026-08-20 20:24 UTC | 15m |
| N149GT |  | Rochester International Airport (KRST) | Breezy Point Airport (8MN3) | 2026-08-20 19:35 UTC | 2026-08-20 20:24 UTC | 48m |
| N6152B |  | Music Mountain Air Ranch Airport (68AZ) | Grand Canyon West Airport (K1G4) | 2026-08-20 20:02 UTC | 2026-08-20 20:24 UTC | 21m |
| N89653 |  | Portland-Hillsboro Airport (KHIO) | Venell Airport (OR52) | 2026-08-20 19:34 UTC | 2026-08-20 20:22 UTC | 47m |
| TIBLV | TIB | Juan Santamaria International Airport (MROC) | Portalon Airport (MRPL) | 2026-08-20 20:08 UTC | 2026-08-20 20:22 UTC | 14m |
| N3BU |  | Trenton Mercer Airport (KTTN) | Teterboro Airport (KTEB) | 2026-08-20 19:47 UTC | 2026-08-20 20:21 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
