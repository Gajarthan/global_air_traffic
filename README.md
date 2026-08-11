# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_16:53:25_UTC-green)

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

**Latest saved flight:** 2026-08-11 16:53:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-11 16:53:25 UTC

- **187,260** saved flights
- **59,359** unique routes
- **142** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **187,260** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,245,984.6 tonnes** estimated CO2 emissions
- **130,202,007 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7439 |
| 2 | SkyWest Airlines | 6797 |
| 3 | EJA | 3684 |
| 4 | IndiGo | 3273 |
| 5 | Southwest Airlines | 2931 |
| 6 | American Airlines | 2909 |
| 7 | ENY | 2324 |
| 8 | Delta Air Lines | 2204 |
| 9 | LATAM Airlines | 1753 |
| 10 | AZU | 1684 |
| 11 | Lufthansa | 1643 |
| 12 | WIF | 1552 |
| 13 | Vueling | 1549 |
| 14 | LXJ | 1463 |
| 15 | easyJet | 1289 |
| 16 | Swiss International | 1279 |
| 17 | AXM | 1247 |
| 18 | EJU | 1156 |
| 19 | QLK | 1154 |
| 20 | All Nippon Airways | 1142 |
| 21 | Alaska Airlines | 1117 |
| 22 | VIV | 1029 |
| 23 | GLO | 1004 |
| 24 | Air France | 973 |
| 25 | AEE | 968 |
| 26 | CXK | 962 |
| 27 | PGT | 962 |
| 28 | United Airlines | 953 |
| 29 | Cathay Pacific | 947 |
| 30 | WMT | 931 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 159653 |
| 2 | 🇪🇸 ES | 12067 |
| 3 | 🇧🇷 BR | 10753 |
| 4 | 🇦🇺 AU | 10482 |
| 5 | 🇮🇳 IN | 10253 |
| 6 | 🇨🇦 CA | 10217 |
| 7 | 🇮🇹 IT | 9707 |
| 8 | 🇩🇪 DE | 9278 |
| 9 | 🇬🇧 GB | 8713 |
| 10 | 🇯🇵 JP | 7644 |
| 11 | 🇫🇷 FR | 7500 |
| 12 | 🇨🇴 CO | 7088 |
| 13 | 🇬🇷 GR | 5497 |
| 14 | 🇲🇽 MX | 5327 |
| 15 | 🇨🇭 CH | 5024 |
| 16 | 🇹🇷 TR | 4944 |
| 17 | 🇳🇴 NO | 4823 |
| 18 | 🇲🇾 MY | 3262 |
| 19 | 🇿🇦 ZA | 3152 |
| 20 | 🇵🇱 PL | 3110 |
| 21 | 🇹🇭 TH | 2892 |
| 22 | 🇳🇿 NZ | 2666 |
| 23 | 🇵🇭 PH | 2477 |
| 24 | 🇬🇹 GT | 2387 |
| 25 | 🇰🇷 KR | 2313 |
| 26 | 🇲🇦 MA | 1906 |
| 27 | 🇭🇷 HR | 1900 |
| 28 | 🇲🇪 ME | 1679 |
| 29 | 🇳🇱 NL | 1675 |
| 30 | 🇲🇴 MO | 1523 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3879 |
| 2 | Denver International Airport |  | US | 3077 |
| 3 | Tokyo International Airport |  | JP | 2364 |
| 4 | Indira Gandhi International Airport |  | IN | 2307 |
| 5 | Guaymaral Airport |  | CO | 2294 |
| 6 | Harry Reid International Airport |  | US | 2188 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1997 |
| 8 | Zurich Airport |  | CH | 1994 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1940 |
| 10 | La Aurora Airport |  | GT | 1834 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1697 |
| 12 | El Dorado International Airport |  | CO | 1684 |
| 13 | Salt Lake City International Airport |  | US | 1665 |
| 14 | Chicago O'Hare International Airport |  | US | 1654 |
| 15 | Frankfurt am Main International Airport |  | DE | 1612 |
| 16 | Congonhas Airport |  | BR | 1563 |
| 17 | Macau International Airport |  | MO | 1523 |
| 18 | Madrid Barajas International Airport |  | ES | 1479 |
| 19 | Capua Airport |  | IT | 1460 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1456 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1393 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1342 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1307 |
| 24 | Malpensa International Airport |  | IT | 1290 |
| 25 | Charles de Gaulle International Airport |  | FR | 1280 |
| 26 | Charlotte/Douglas International Airport |  | US | 1258 |
| 27 | Kuala Lumpur International Airport |  | MY | 1221 |
| 28 | Bengaluru International Airport |  | IN | 1210 |
| 29 | Ninoy Aquino International Airport |  | PH | 1169 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1168 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1145 |
| 32 | Barcelona International Airport |  | ES | 1117 |
| 33 | Viracopos International Airport |  | BR | 1078 |
| 34 | Seattle-Tacoma International Airport |  | US | 1076 |
| 35 | Reno/Tahoe International Airport |  | US | 1073 |
| 36 | Calgary International Airport |  | CA | 1063 |
| 37 | Daniel K Inouye International Airport |  | US | 1057 |
| 38 | Oslo Gardermoen Airport |  | NO | 1048 |
| 39 | Tenerife Norte Airport |  | ES | 1025 |
| 40 | Vitoria/Foronda Airport |  | ES | 1016 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 945 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 685 | 21m | 244 km | 2,884.3 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 454 | 1h 7m | 770 km | 6,031.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 438 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 436 | 24m | 225 km | 1,691.5 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 330 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 315 | 27m | 275 km | 1,492.7 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 304 | 14m | 114 km | 596.2 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 303 | 1h 7m | 706 km | 3,689.0 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 281 | 44m | 241 km | 1,167.2 t |
| 12 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 272 | 8m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 266 | 1h 49m | 1,423 km | 6,528.1 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 251 | 20m | 250 km | 1,084.2 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 235 | 27m | 215 km | 870.3 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 233 | 13m | - | - |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 230 | 12m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 229 | 19m | 99 km | 392.3 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 228 | 1h 15m | 961 km | 3,779.2 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 228 | 50m | 556 km | 2,185.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 224 | 1h 38m | 1,156 km | 4,468.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 223 | 19m | 144 km | 554.7 t |
| 26 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 221 | 24m | 218 km | 832.6 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 218 | 31m | 369 km | 1,387.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TFHNH | TFH | Keflavik International Airport (BIKF) | Reykjavik Airport (BIRK) | 2026-08-11 16:34 UTC | 2026-08-11 16:53 UTC | 18m |
| SVX41 | SVX | Fairbanks International Airport (PAFA) | Ralph Wien Memorial Airport (PAOT) | 2026-08-11 15:13 UTC | 2026-08-11 16:48 UTC | 1h 34m |
| N460LE |  | Bend Municipal Airport (KBDN) | Bend Municipal Airport (KBDN) | 2026-08-11 16:08 UTC | 2026-08-11 16:45 UTC | 37m |
| N3403 |  | Orlando Apopka Airport (KX04) | Orlando North Airpark (FA83) | 2026-08-11 16:38 UTC | 2026-08-11 16:40 UTC | 1m |
| SPGAA | SPG | Jastarnia Airport (EPJA) | Jastarnia Airport (EPJA) | 2026-08-11 16:07 UTC | 2026-08-11 16:39 UTC | 31m |
| N2129J |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-08-11 15:45 UTC | 2026-08-11 16:36 UTC | 50m |
| N200FK |  | Lorain County Regional Airport (KLPR) | Burke Lakefront Airport (KBKL) | 2026-08-11 16:21 UTC | 2026-08-11 16:34 UTC | 13m |
| N1570C |  | Greenwood County Airport (KGRD) | Mustang Field (0GA1) | 2026-08-11 16:21 UTC | 2026-08-11 16:34 UTC | 13m |
| OKEUI15 | OKE | Letnany Airport (LKLT) | Letnany Airport (LKLT) | 2026-08-11 15:45 UTC | 2026-08-11 16:33 UTC | 47m |
| LN877PA |  | Valdosta Regional Airport (KVLD) | Dekalb-Peachtree Airport (KPDK) | 2026-08-11 15:26 UTC | 2026-08-11 16:21 UTC | 55m |
| N6704D |  | Mountain Valley Airport (KL94) | Meadows Field (KBFL) | 2026-08-11 15:20 UTC | 2026-08-11 16:21 UTC | 1h 1m |
| N228JJ |  | Toledo Suburban Airport (KDUH) | Toledo Executive Airport (KTDZ) | 2026-08-11 15:35 UTC | 2026-08-11 16:21 UTC | 45m |
| N36GV |  | Diamond A Ranch Airport (NM64) | Diamond A Ranch Airport (NM64) | 2026-08-11 16:03 UTC | 2026-08-11 16:16 UTC | 13m |
| EZY47UJ | easyJet | Belfast International Airport (EGAA) | Manchester Airport (EGCC) | 2026-08-11 15:33 UTC | 2026-08-11 16:11 UTC | 37m |
| N866US |  | Brigham City Regional Airport (KBMC) | Malad City Airport (KMLD) | 2026-08-11 15:50 UTC | 2026-08-11 16:10 UTC | 19m |
| PSFUN | PSF | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-08-11 15:54 UTC | 2026-08-11 16:08 UTC | 14m |
| N7444W |  | Carson City Airport (KCXP) | Carson City Airport (KCXP) | 2026-08-11 15:57 UTC | 2026-08-11 16:08 UTC | 10m |
| CXK131 | CXK | Provo Municipal Airport (KPVU) | Provo Municipal Airport (KPVU) | 2026-08-11 15:48 UTC | 2026-08-11 16:06 UTC | 18m |
| N825US |  | North Las Vegas Airport (KVGT) | Sky Ranch Airport (K3L2) | 2026-08-11 15:20 UTC | 2026-08-11 16:06 UTC | 46m |
| N6338F |  | Princeton Airport (K39N) | Northeast Philadelphia Airport (KPNE) | 2026-08-11 15:17 UTC | 2026-08-11 16:06 UTC | 49m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
