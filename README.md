# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_13:43:55_UTC-green)

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

**Latest saved flight:** 2026-08-22 13:43:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 13:43:55 UTC

- **225,556** saved flights
- **70,182** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,556** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,718,545.1 tonnes** estimated CO2 emissions
- **157,596,819 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9047 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4354 |
| 4 | IndiGo | 3817 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2153 |
| 10 | AZU | 2080 |
| 11 | Vueling | 1907 |
| 12 | Lufthansa | 1852 |
| 13 | WIF | 1794 |
| 14 | LXJ | 1779 |
| 15 | easyJet | 1564 |
| 16 | Swiss International | 1503 |
| 17 | AXM | 1493 |
| 18 | QLK | 1421 |
| 19 | EJU | 1420 |
| 20 | United Airlines | 1418 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1248 |
| 24 | PGT | 1242 |
| 25 | VIV | 1232 |
| 26 | Air France | 1226 |
| 27 | WMT | 1211 |
| 28 | Wizz Air | 1170 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1124 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188806 |
| 2 | 🇪🇸 ES | 14456 |
| 3 | 🇧🇷 BR | 13109 |
| 4 | 🇦🇺 AU | 12776 |
| 5 | 🇨🇦 CA | 12485 |
| 6 | 🇮🇹 IT | 12088 |
| 7 | 🇮🇳 IN | 11903 |
| 8 | 🇩🇪 DE | 11110 |
| 9 | 🇬🇧 GB | 10604 |
| 10 | 🇨🇴 CO | 9267 |
| 11 | 🇯🇵 JP | 9190 |
| 12 | 🇫🇷 FR | 9015 |
| 13 | 🇹🇷 TR | 6610 |
| 14 | 🇬🇷 GR | 6592 |
| 15 | 🇲🇽 MX | 6260 |
| 16 | 🇨🇭 CH | 5965 |
| 17 | 🇳🇴 NO | 5586 |
| 18 | 🇲🇾 MY | 3978 |
| 19 | 🇿🇦 ZA | 3909 |
| 20 | 🇹🇭 TH | 3887 |
| 21 | 🇵🇱 PL | 3749 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3081 |
| 24 | 🇬🇹 GT | 2853 |
| 25 | 🇰🇷 KR | 2676 |
| 26 | 🇭🇷 HR | 2540 |
| 27 | 🇲🇦 MA | 2267 |
| 28 | 🇲🇪 ME | 2028 |
| 29 | 🇳🇱 NL | 2016 |
| 30 | 🇮🇩 ID | 1950 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2747 |
| 4 | Indira Gandhi International Airport |  | IN | 2742 |
| 5 | Guaymaral Airport |  | CO | 2632 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2344 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2282 |
| 10 | La Aurora Airport |  | GT | 2174 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1916 |
| 16 | Frankfurt am Main International Airport |  | DE | 1817 |
| 17 | Madrid Barajas International Airport |  | ES | 1761 |
| 18 | Capua Airport |  | IT | 1738 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1678 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1675 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1594 |
| 23 | Malpensa International Airport |  | IT | 1590 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 25 | Charles de Gaulle International Airport |  | FR | 1561 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1473 |
| 28 | Kuala Lumpur International Airport |  | MY | 1445 |
| 29 | Barcelona International Airport |  | ES | 1399 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1369 |
| 31 | Bengaluru International Airport |  | IN | 1343 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1334 |
| 33 | Seattle-Tacoma International Airport |  | US | 1329 |
| 34 | Viracopos International Airport |  | BR | 1328 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1306 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1275 |
| 38 | Oslo Gardermoen Airport |  | NO | 1258 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1220 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1073 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 816 | 21m | 244 km | 3,436.0 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 563 | 1h 6m | 770 km | 7,479.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 528 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 355 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 340 | 1h 50m | 1,423 km | 8,344.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 329 | 44m | 241 km | 1,366.6 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 292 | 44m | 555 km | 2,796.0 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 288 | 1h 38m | 1,156 km | 5,745.5 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 284 | 24m | 218 km | 1,069.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 258 | 19m | 144 km | 641.8 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N282CH |  | Alliance Airport (23NJ) | Philadelphia International Airport (KPHL) | 2026-08-22 13:31 UTC | 2026-08-22 13:43 UTC | 12m |
| N3039F |  | Bybee Field (97OG) | Emmett Municipal Airport (KS78) | 2026-08-22 12:26 UTC | 2026-08-22 13:40 UTC | 1h 14m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-22 13:06 UTC | 2026-08-22 13:40 UTC | 33m |
| N470RG |  | Provo Municipal Airport (KPVU) | KU77 (KU77) | 2026-08-22 13:25 UTC | 2026-08-22 13:38 UTC | 13m |
| SXHGG | SXH | Eleftherios Venizelos International Airport (LGAV) | Eleftherios Venizelos International Airport (LGAV) | 2026-08-22 13:21 UTC | 2026-08-22 13:38 UTC | 16m |
| N149AH |  | Winter Haven Regional Airport (KGIF) | Orlando Executive Airport (KORL) | 2026-08-22 13:19 UTC | 2026-08-22 13:37 UTC | 18m |
| PRWRC | PRW | Usina Catanduva Airport (SDDV) | Chafei Amsei Airport (SBBT) | 2026-08-22 13:19 UTC | 2026-08-22 13:35 UTC | 16m |
| N842EB |  | Sebastian Municipal Airport (KX26) | Sebastian Municipal Airport (KX26) | 2026-08-22 13:19 UTC | 2026-08-22 13:35 UTC | 16m |
| SEMMK | SEM | Texel Airport (EHTX) | Texel Airport (EHTX) | 2026-08-22 13:02 UTC | 2026-08-22 13:26 UTC | 23m |
| LFA541 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-08-22 12:56 UTC | 2026-08-22 13:24 UTC | 27m |
| PH1693 |  | Terlet Airport (EHTL) | Terlet Airport (EHTL) | 2026-08-22 12:45 UTC | 2026-08-22 13:21 UTC | 36m |
| EIN16C | Aer Lingus | London Heathrow Airport (EGLL) | Dublin Airport (EIDW) | 2026-08-22 12:33 UTC | 2026-08-22 13:18 UTC | 45m |
| N723CD |  | Brandywine Regional Airport (KOQN) | Brandywine Regional Airport (KOQN) | 2026-08-22 12:52 UTC | 2026-08-22 13:14 UTC | 21m |
| N125NG |  | KU77 (KU77) | Wendover Airport (KENV) | 2026-08-22 11:42 UTC | 2026-08-22 13:07 UTC | 1h 24m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 12:55 UTC | 2026-08-22 13:06 UTC | 10m |
| TCMPA | TCM | Antalya International Airport (LTAI) | Belgrade Nikola Tesla Airport (LYBE) | 2026-08-22 10:56 UTC | 2026-08-22 13:05 UTC | 2h 8m |
| GBBMB | GBB | North Weald Airport (EGSX) | Earls Colne Airfield (EGSR) | 2026-08-22 12:55 UTC | 2026-08-22 13:04 UTC | 8m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-22 11:35 UTC | 2026-08-22 13:03 UTC | 1h 28m |
| AIP1408 | AIP | Hector International Airport (KFAR) | Ripplinger Strip (NA33) | 2026-08-22 12:23 UTC | 2026-08-22 13:02 UTC | 38m |
| N8665Y |  | Stevens Point Municipal Airport (KSTE) | Rhinelander/Oneida County Airport (KRHI) | 2026-08-22 12:18 UTC | 2026-08-22 12:51 UTC | 32m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
