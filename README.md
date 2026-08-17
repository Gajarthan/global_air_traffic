# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_16:47:24_UTC-green)

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

**Latest saved flight:** 2026-08-17 16:47:24 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-17 16:47:24 UTC

- **209,075** saved flights
- **66,624** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **209,075** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,514,404.4 tonnes** estimated CO2 emissions
- **145,762,571 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8280 |
| 2 | SkyWest Airlines | 7501 |
| 3 | EJA | 4064 |
| 4 | IndiGo | 3571 |
| 5 | American Airlines | 3495 |
| 6 | Southwest Airlines | 3364 |
| 7 | Delta Air Lines | 2703 |
| 8 | ENY | 2605 |
| 9 | LATAM Airlines | 1972 |
| 10 | AZU | 1890 |
| 11 | Lufthansa | 1764 |
| 12 | Vueling | 1739 |
| 13 | WIF | 1685 |
| 14 | LXJ | 1650 |
| 15 | easyJet | 1450 |
| 16 | Swiss International | 1398 |
| 17 | AXM | 1363 |
| 18 | United Airlines | 1321 |
| 19 | QLK | 1293 |
| 20 | Alaska Airlines | 1287 |
| 21 | EJU | 1279 |
| 22 | All Nippon Airways | 1265 |
| 23 | VIV | 1147 |
| 24 | GLO | 1130 |
| 25 | Air France | 1127 |
| 26 | PGT | 1119 |
| 27 | JetBlue | 1067 |
| 28 | AEE | 1065 |
| 29 | WMT | 1059 |
| 30 | Wizz Air | 1037 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 177094 |
| 2 | 🇪🇸 ES | 13384 |
| 3 | 🇧🇷 BR | 11988 |
| 4 | 🇦🇺 AU | 11747 |
| 5 | 🇨🇦 CA | 11519 |
| 6 | 🇮🇳 IN | 11145 |
| 7 | 🇮🇹 IT | 10936 |
| 8 | 🇩🇪 DE | 10341 |
| 9 | 🇬🇧 GB | 9771 |
| 10 | 🇯🇵 JP | 8645 |
| 11 | 🇨🇴 CO | 8321 |
| 12 | 🇫🇷 FR | 8311 |
| 13 | 🇬🇷 GR | 6157 |
| 14 | 🇹🇷 TR | 5947 |
| 15 | 🇲🇽 MX | 5862 |
| 16 | 🇨🇭 CH | 5569 |
| 17 | 🇳🇴 NO | 5223 |
| 18 | 🇲🇾 MY | 3594 |
| 19 | 🇿🇦 ZA | 3516 |
| 20 | 🇵🇱 PL | 3455 |
| 21 | 🇹🇭 TH | 3353 |
| 22 | 🇳🇿 NZ | 2893 |
| 23 | 🇵🇭 PH | 2776 |
| 24 | 🇬🇹 GT | 2685 |
| 25 | 🇰🇷 KR | 2545 |
| 26 | 🇭🇷 HR | 2246 |
| 27 | 🇲🇦 MA | 2108 |
| 28 | 🇳🇱 NL | 1870 |
| 29 | 🇲🇪 ME | 1774 |
| 30 | 🇮🇩 ID | 1725 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4388 |
| 2 | Denver International Airport |  | US | 3406 |
| 3 | Tokyo International Airport |  | JP | 2599 |
| 4 | Indira Gandhi International Airport |  | IN | 2535 |
| 5 | Guaymaral Airport |  | CO | 2510 |
| 6 | Harry Reid International Airport |  | US | 2352 |
| 7 | Zurich Airport |  | CH | 2182 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2176 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2165 |
| 10 | La Aurora Airport |  | GT | 2042 |
| 11 | Chicago O'Hare International Airport |  | US | 1938 |
| 12 | El Dorado International Airport |  | CO | 1907 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1862 |
| 14 | Salt Lake City International Airport |  | US | 1846 |
| 15 | Congonhas Airport |  | BR | 1744 |
| 16 | Frankfurt am Main International Airport |  | DE | 1719 |
| 17 | Madrid Barajas International Airport |  | ES | 1640 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1587 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1586 |
| 20 | Capua Airport |  | IT | 1577 |
| 21 | Macau International Airport |  | MO | 1547 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1525 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1468 |
| 24 | Malpensa International Airport |  | IT | 1449 |
| 25 | Charles de Gaulle International Airport |  | FR | 1437 |
| 26 | Charlotte/Douglas International Airport |  | US | 1418 |
| 27 | Kuala Lumpur International Airport |  | MY | 1327 |
| 28 | Ninoy Aquino International Airport |  | PH | 1315 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1291 |
| 30 | Bengaluru International Airport |  | IN | 1289 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1264 |
| 32 | Barcelona International Airport |  | ES | 1253 |
| 33 | Seattle-Tacoma International Airport |  | US | 1240 |
| 34 | Viracopos International Airport |  | BR | 1212 |
| 35 | Calgary International Airport |  | CA | 1179 |
| 36 | Oslo Gardermoen Airport |  | NO | 1158 |
| 37 | Vitoria/Foronda Airport |  | ES | 1150 |
| 38 | Reno/Tahoe International Airport |  | US | 1145 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1131 |
| 40 | Don Mueang International Airport |  | TH | 1113 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1031 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 736 | 21m | 244 km | 3,099.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 514 | 1h 7m | 770 km | 6,828.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 486 | 24m | 225 km | 1,885.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 475 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 410 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 350 | 27m | 275 km | 1,658.5 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 346 | 33m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 306 | 44m | 241 km | 1,271.1 t |
| 12 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 305 | 1h 49m | 1,423 km | 7,485.2 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 288 | 22m | 55 km | 273.7 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 270 | 21m | 250 km | 1,166.2 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 266 | 24m | 218 km | 1,002.1 t |
| 17 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 262 | 19m | 99 km | 448.8 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 257 | 27m | 215 km | 951.8 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 249 | 1h 37m | 1,156 km | 4,967.5 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 248 | 1h 14m | 961 km | 4,110.7 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 246 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 239 | 31m | 369 km | 1,521.3 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 239 | 19m | 144 km | 594.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 27 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 229 | 28m | 152 km | 598.5 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 224 | 1h 49m | 1,304 km | 5,039.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N572JA |  | Aurora Municipal Airport (KARR) | Wade Airport (56LL) | 2026-08-17 16:27 UTC | 2026-08-17 16:47 UTC | 19m |
| PSUCA | PSU | Guarulhos - Governador Andre Franco Montoro International Airport (SBGR) | Campo de Marte Airport (SBMT) | 2026-08-17 16:27 UTC | 2026-08-17 16:44 UTC | 16m |
| N449KC |  | Level Acres Farm Airport (PA84) | Lehigh Valley International Airport (KABE) | 2026-08-17 16:20 UTC | 2026-08-17 16:42 UTC | 21m |
| N5086X |  | Ramona Airport (KRNM) | Billy Joe Airport (37CA) | 2026-08-17 15:23 UTC | 2026-08-17 16:40 UTC | 1h 16m |
| XSN90 | XSN | Truckee-Tahoe Airport (KTRK) | Palo Alto Airport (KPAO) | 2026-08-17 15:52 UTC | 2026-08-17 16:39 UTC | 46m |
| N407TK |  | Crystal Lakes Airport (25CO) | Buckley Space Force Base Airport (KBKF) | 2026-08-17 15:50 UTC | 2026-08-17 16:36 UTC | 45m |
| AAL794 | American Airlines | Austin-Bergstrom International Airport (KAUS) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-17 15:43 UTC | 2026-08-17 16:25 UTC | 42m |
| N4777H |  | Middleton Municipal/Morey Field (KC29) | Middleton Municipal/Morey Field (KC29) | 2026-08-17 16:05 UTC | 2026-08-17 16:24 UTC | 18m |
| LIFELN3 | LIF | Cheyenne Regional/Jerry Olson Field (KCYS) | Buckley Space Force Base Airport (KBKF) | 2026-08-17 15:35 UTC | 2026-08-17 16:20 UTC | 44m |
| NOZ4RM | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Stavanger Airport Sola (ENZV) | 2026-08-17 15:42 UTC | 2026-08-17 16:19 UTC | 36m |
| SCU39 | SCU | Neversweat Airport (1OK0) | Jones Memorial Airport (K3F7) | 2026-08-17 15:51 UTC | 2026-08-17 16:19 UTC | 28m |
| N219CM |  | Mckinney Ntl Airport (KTKI) | Memorial Field (KHOT) | 2026-08-17 15:42 UTC | 2026-08-17 16:19 UTC | 36m |
| N555DP |  | Falcon Field (KFFZ) | Morris Ag Air Sw Airport (56CL) | 2026-08-17 14:44 UTC | 2026-08-17 16:18 UTC | 1h 33m |
| N449BL |  | Johnston Regional Airport (KJNX) | Johnston Regional Airport (KJNX) | 2026-08-17 16:15 UTC | 2026-08-17 16:17 UTC | 1m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | LIVV (LIVV) | 2026-08-17 16:01 UTC | 2026-08-17 16:16 UTC | 14m |
| N127XY |  | Skypark Airport (KBTF) | Nephi Municipal Airport (KU14) | 2026-08-17 15:36 UTC | 2026-08-17 16:15 UTC | 38m |
| CODE21 | COD | 75OK (75OK) | Flying E Ranch Airport (OK16) | 2026-08-17 15:54 UTC | 2026-08-17 16:14 UTC | 20m |
| GTI8138 | GTI | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-08-17 11:41 UTC | 2026-08-17 16:12 UTC | 4h 30m |
| WOLF18 | WOL | Okc Will Rogers International Airport (KOKC) | Shangrila Airport (WS25) | 2026-08-17 13:49 UTC | 2026-08-17 16:11 UTC | 2h 22m |
| AUR214 | AUR | Alderney Airport (EGJA) | Guernsey Airport (EGJB) | 2026-08-17 15:50 UTC | 2026-08-17 16:11 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
