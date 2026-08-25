# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_02:09:16_UTC-green)

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

**Latest saved flight:** 2026-08-25 02:09:16 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 02:09:16 UTC

- **233,977** saved flights
- **71,803** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **233,977** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,818,688.4 tonnes** estimated CO2 emissions
- **163,402,228 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9382 |
| 2 | SkyWest Airlines | 8295 |
| 3 | EJA | 4551 |
| 4 | IndiGo | 3945 |
| 5 | American Airlines | 3815 |
| 6 | Southwest Airlines | 3598 |
| 7 | Delta Air Lines | 2990 |
| 8 | ENY | 2854 |
| 9 | LATAM Airlines | 2251 |
| 10 | AZU | 2183 |
| 11 | Vueling | 1998 |
| 12 | Lufthansa | 1901 |
| 13 | WIF | 1856 |
| 14 | LXJ | 1843 |
| 15 | easyJet | 1632 |
| 16 | Swiss International | 1565 |
| 17 | AXM | 1554 |
| 18 | EJU | 1495 |
| 19 | QLK | 1485 |
| 20 | United Airlines | 1484 |
| 21 | Alaska Airlines | 1410 |
| 22 | All Nippon Airways | 1390 |
| 23 | GLO | 1306 |
| 24 | WMT | 1297 |
| 25 | VIV | 1291 |
| 26 | PGT | 1274 |
| 27 | Air France | 1268 |
| 28 | Wizz Air | 1234 |
| 29 | AEE | 1162 |
| 30 | JetBlue | 1162 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 194966 |
| 2 | 🇪🇸 ES | 15005 |
| 3 | 🇧🇷 BR | 13681 |
| 4 | 🇦🇺 AU | 13226 |
| 5 | 🇨🇦 CA | 12961 |
| 6 | 🇮🇹 IT | 12705 |
| 7 | 🇮🇳 IN | 12285 |
| 8 | 🇩🇪 DE | 11509 |
| 9 | 🇬🇧 GB | 11013 |
| 10 | 🇨🇴 CO | 9832 |
| 11 | 🇯🇵 JP | 9470 |
| 12 | 🇫🇷 FR | 9346 |
| 13 | 🇹🇷 TR | 6925 |
| 14 | 🇬🇷 GR | 6873 |
| 15 | 🇲🇽 MX | 6516 |
| 16 | 🇨🇭 CH | 6225 |
| 17 | 🇳🇴 NO | 5770 |
| 18 | 🇲🇾 MY | 4152 |
| 19 | 🇹🇭 TH | 4113 |
| 20 | 🇿🇦 ZA | 4071 |
| 21 | 🇵🇱 PL | 3892 |
| 22 | 🇳🇿 NZ | 3227 |
| 23 | 🇵🇭 PH | 3197 |
| 24 | 🇬🇹 GT | 2931 |
| 25 | 🇰🇷 KR | 2731 |
| 26 | 🇭🇷 HR | 2686 |
| 27 | 🇲🇦 MA | 2372 |
| 28 | 🇲🇪 ME | 2155 |
| 29 | 🇳🇱 NL | 2092 |
| 30 | 🇮🇩 ID | 2018 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4873 |
| 2 | Denver International Airport |  | US | 3795 |
| 3 | Indira Gandhi International Airport |  | IN | 2845 |
| 4 | Tokyo International Airport |  | JP | 2822 |
| 5 | Guaymaral Airport |  | CO | 2677 |
| 6 | Harry Reid International Airport |  | US | 2514 |
| 7 | Zurich Airport |  | CH | 2442 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2395 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2343 |
| 10 | La Aurora Airport |  | GT | 2234 |
| 11 | El Dorado International Airport |  | CO | 2190 |
| 12 | Chicago O'Hare International Airport |  | US | 2117 |
| 13 | Salt Lake City International Airport |  | US | 2068 |
| 14 | Congonhas Airport |  | BR | 1997 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1969 |
| 16 | Frankfurt am Main International Airport |  | DE | 1863 |
| 17 | Capua Airport |  | IT | 1840 |
| 18 | Madrid Barajas International Airport |  | ES | 1835 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1763 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1732 |
| 21 | Malpensa International Airport |  | IT | 1674 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1664 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1642 |
| 24 | Charles de Gaulle International Airport |  | FR | 1622 |
| 25 | Macau International Airport |  | MO | 1605 |
| 26 | Ninoy Aquino International Airport |  | PH | 1542 |
| 27 | Charlotte/Douglas International Airport |  | US | 1515 |
| 28 | Kuala Lumpur International Airport |  | MY | 1502 |
| 29 | Barcelona International Airport |  | ES | 1475 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1443 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1418 |
| 32 | Viracopos International Airport |  | BR | 1396 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1376 |
| 34 | Seattle-Tacoma International Airport |  | US | 1376 |
| 35 | Bengaluru International Airport |  | IN | 1372 |
| 36 | Calgary International Airport |  | CA | 1342 |
| 37 | Don Mueang International Airport |  | TH | 1341 |
| 38 | Oslo Gardermoen Airport |  | NO | 1307 |
| 39 | Vancouver International Airport |  | CA | 1280 |
| 40 | Vitoria/Foronda Airport |  | ES | 1266 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1085 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 853 | 21m | 244 km | 3,591.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 587 | 1h 6m | 770 km | 7,797.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 584 | 24m | 225 km | 2,265.6 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 584 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 523 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 385 | 27m | 275 km | 1,824.4 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 361 | 1h 50m | 1,423 km | 8,859.5 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 359 | 35m | - | - |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 339 | 44m | 241 km | 1,408.1 t |
| 11 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 327 | 44m | 555 km | 3,131.2 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 310 | 24m | 218 km | 1,167.9 t |
| 16 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 310 | 22m | 55 km | 294.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 306 | 1h 38m | 1,156 km | 6,104.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 289 | 19m | 99 km | 495.0 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 285 | 27m | 215 km | 1,055.5 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 271 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 266 | 19m | 144 km | 661.7 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 252 | 15m | 154 km | 667.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 251 | 1h 50m | 1,304 km | 5,646.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MSR780 | EgyptAir | London Heathrow Airport (EGLL) | HE42 (HE42) | 2026-08-24 22:06 UTC | 2026-08-25 02:09 UTC | 4h 2m |
| ASP858 | ASP | Calgary International Airport (CYYC) | Calgary International Airport (CYYC) | 2026-08-25 01:55 UTC | 2026-08-25 02:08 UTC | 12m |
| N757MS |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-08-25 01:22 UTC | 2026-08-25 02:08 UTC | 46m |
| SITKA22 | SIT | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-08-24 22:38 UTC | 2026-08-25 02:01 UTC | 3h 23m |
| N945PC |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-25 01:40 UTC | 2026-08-25 02:00 UTC | 19m |
| N302TP |  | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-08-25 01:41 UTC | 2026-08-25 01:56 UTC | 15m |
| TKR169 | TKR | Boise Air Trml/Gowen Field (KBOI) | Oasis Airpark (1ID4) | 2026-08-25 01:47 UTC | 2026-08-25 01:55 UTC | 7m |
| N18PY |  | Gwinnett County/Briscoe Field (KLZU) | Dekalb-Peachtree Airport (KPDK) | 2026-08-25 01:34 UTC | 2026-08-25 01:45 UTC | 11m |
| N149TH |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-25 00:52 UTC | 2026-08-25 01:43 UTC | 50m |
| N591SS |  | Napa County Airport (KAPC) | Lake Tahoe Airport (KTVL) | 2026-08-25 01:06 UTC | 2026-08-25 01:39 UTC | 33m |
| EJA895 | EJA | San Diego International Airport (KSAN) | Scottsdale Airport (KSDL) | 2026-08-25 00:46 UTC | 2026-08-25 01:38 UTC | 51m |
| N221FL |  | Trenton Mercer Airport (KTTN) | Ocean City Municipal Airport (KOXB) | 2026-08-25 00:29 UTC | 2026-08-25 01:35 UTC | 1h 5m |
| N465DF |  | Redding Regional Airport (KRDD) | Likely Airport (9CL3) | 2026-08-25 01:08 UTC | 2026-08-25 01:31 UTC | 23m |
| N908FG |  | Trenton Mercer Airport (KTTN) | Trenton Mercer Airport (KTTN) | 2026-08-24 23:57 UTC | 2026-08-25 01:31 UTC | 1h 33m |
| AXM552 | AXM | Kuala Lumpur International Airport (WMKK) | Wattay International Airport (VLVT) | 2026-08-24 23:18 UTC | 2026-08-25 01:31 UTC | 2h 12m |
| TKR168 | TKR | Hill Afb Airport (KHIF) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-08-25 01:14 UTC | 2026-08-25 01:30 UTC | 16m |
| N413DE |  | Napa County Airport (KAPC) | Truckee-Tahoe Airport (KTRK) | 2026-08-25 01:01 UTC | 2026-08-25 01:30 UTC | 28m |
| BDOG200 | BDO | RAAF Base Richmond (YSRI) | Condobolin Airport (YCDO) | 2026-08-25 00:42 UTC | 2026-08-25 01:28 UTC | 46m |
| N745B |  | Chino Airport (KCNO) | Santa Barbara Municipal Airport (KSBA) | 2026-08-25 00:12 UTC | 2026-08-25 01:28 UTC | 1h 15m |
| N550WR |  | William P Hobby Airport (KHOU) | Archer City Municipal Airport (KT39) | 2026-08-25 00:26 UTC | 2026-08-25 01:27 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
