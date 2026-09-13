# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_04:58:12_UTC-green)

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

**Latest saved flight:** 2026-09-13 04:58:12 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-13 04:58:12 UTC

- **256,963** saved flights
- **76,539** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **256,963** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,107,342.6 tonnes** estimated CO2 emissions
- **180,135,802 km** total distance flown
- **860 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10215 |
| 2 | SkyWest Airlines | 8957 |
| 3 | EJA | 4965 |
| 4 | IndiGo | 4308 |
| 5 | American Airlines | 4064 |
| 6 | Southwest Airlines | 3783 |
| 7 | Delta Air Lines | 3220 |
| 8 | ENY | 3048 |
| 9 | LATAM Airlines | 2470 |
| 10 | AZU | 2394 |
| 11 | Vueling | 2172 |
| 12 | WIF | 2055 |
| 13 | Lufthansa | 2011 |
| 14 | LXJ | 2004 |
| 15 | easyJet | 1756 |
| 16 | Swiss International | 1721 |
| 17 | QLK | 1659 |
| 18 | AXM | 1644 |
| 19 | EJU | 1637 |
| 20 | United Airlines | 1592 |
| 21 | Alaska Airlines | 1527 |
| 22 | All Nippon Airways | 1496 |
| 23 | WMT | 1451 |
| 24 | GLO | 1431 |
| 25 | PGT | 1424 |
| 26 | VIV | 1406 |
| 27 | Air France | 1397 |
| 28 | Wizz Air | 1397 |
| 29 | TKR | 1247 |
| 30 | JetBlue | 1246 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 213349 |
| 2 | 🇪🇸 ES | 16309 |
| 3 | 🇧🇷 BR | 14986 |
| 4 | 🇦🇺 AU | 14654 |
| 5 | 🇨🇦 CA | 14322 |
| 6 | 🇮🇹 IT | 14031 |
| 7 | 🇮🇳 IN | 13505 |
| 8 | 🇩🇪 DE | 12519 |
| 9 | 🇬🇧 GB | 11986 |
| 10 | 🇨🇴 CO | 11504 |
| 11 | 🇫🇷 FR | 10311 |
| 12 | 🇯🇵 JP | 10034 |
| 13 | 🇹🇷 TR | 7726 |
| 14 | 🇬🇷 GR | 7487 |
| 15 | 🇲🇽 MX | 7094 |
| 16 | 🇨🇭 CH | 6894 |
| 17 | 🇳🇴 NO | 6347 |
| 18 | 🇹🇭 TH | 4621 |
| 19 | 🇲🇾 MY | 4418 |
| 20 | 🇿🇦 ZA | 4362 |
| 21 | 🇵🇱 PL | 4257 |
| 22 | 🇳🇿 NZ | 3556 |
| 23 | 🇵🇭 PH | 3458 |
| 24 | 🇬🇹 GT | 3257 |
| 25 | 🇭🇷 HR | 2946 |
| 26 | 🇰🇷 KR | 2943 |
| 27 | 🇲🇦 MA | 2585 |
| 28 | 🇲🇪 ME | 2417 |
| 29 | 🇳🇱 NL | 2315 |
| 30 | 🇮🇩 ID | 2181 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5267 |
| 2 | Denver International Airport |  | US | 4156 |
| 3 | Indira Gandhi International Airport |  | IN | 3109 |
| 4 | Tokyo International Airport |  | JP | 2996 |
| 5 | Guaymaral Airport |  | CO | 2761 |
| 6 | Harry Reid International Airport |  | US | 2723 |
| 7 | Zurich Airport |  | CH | 2691 |
| 8 | El Dorado International Airport |  | CO | 2671 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2593 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2509 |
| 11 | La Aurora Airport |  | GT | 2474 |
| 12 | Salt Lake City International Airport |  | US | 2265 |
| 13 | Chicago O'Hare International Airport |  | US | 2239 |
| 14 | Congonhas Airport |  | BR | 2199 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2098 |
| 16 | Capua Airport |  | IT | 2023 |
| 17 | Madrid Barajas International Airport |  | ES | 2004 |
| 18 | Frankfurt am Main International Airport |  | DE | 1984 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1927 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1857 |
| 21 | Malpensa International Airport |  | IT | 1850 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1808 |
| 23 | Charles de Gaulle International Airport |  | FR | 1804 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1782 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1740 |
| 26 | Macau International Airport |  | MO | 1703 |
| 27 | Ninoy Aquino International Airport |  | PH | 1693 |
| 28 | Barcelona International Airport |  | ES | 1617 |
| 29 | Charlotte/Douglas International Airport |  | US | 1608 |
| 30 | Kuala Lumpur International Airport |  | MY | 1590 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1575 |
| 32 | Viracopos International Airport |  | BR | 1536 |
| 33 | Seattle-Tacoma International Airport |  | US | 1506 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1493 |
| 35 | Don Mueang International Airport |  | TH | 1478 |
| 36 | Calgary International Airport |  | CA | 1471 |
| 37 | Bengaluru International Airport |  | IN | 1458 |
| 38 | Oslo Gardermoen Airport |  | NO | 1449 |
| 39 | Vancouver International Airport |  | CA | 1447 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1388 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1109 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 960 | 21m | 244 km | 4,042.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 691 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 644 | 1h 6m | 770 km | 8,555.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 643 | 24m | 225 km | 2,494.5 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 576 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 418 | 27m | 275 km | 1,980.7 t |
| 8 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 414 | 44m | 555 km | 3,964.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 410 | 1h 50m | 1,423 km | 10,062.0 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 387 | 44m | 241 km | 1,607.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 359 | 24m | 218 km | 1,352.5 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 355 | 21m | 250 km | 1,533.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 343 | 23m | 55 km | 326.0 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 325 | 1h 6m | 706 km | 3,956.9 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 320 | 19m | 99 km | 548.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 316 | 26m | 215 km | 1,170.3 t |
| 19 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 311 | 12m | - | - |
| 21 | Bodø Airport (ENBO) | ENEN (ENEN) | 304 | 13m | - | - |
| 22 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 295 | 1h 14m | 961 km | 4,889.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 295 | 19m | 144 km | 733.8 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 275 | 1h 50m | 1,304 km | 6,186.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 270 | 41m | 535 km | 2,493.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 270 | 28m | 152 km | 705.6 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZKTAW | ZKT | Wellington International Airport (NZWN) | Wellington International Airport (NZWN) | 2026-09-13 04:31 UTC | 2026-09-13 04:58 UTC | 26m |
| ENY3955 | ENY | Chicago O'Hare International Airport (KORD) | Leo's Place Airport (1KS3) | 2026-09-13 03:37 UTC | 2026-09-13 04:55 UTC | 1h 17m |
| CPA821 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-09-12 14:49 UTC | 2026-09-13 04:42 UTC | 13h 53m |
| IGO24V | IndiGo | London Heathrow Airport (EGLL) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-12 19:35 UTC | 2026-09-13 04:39 UTC | 9h 4m |
| N705CA |  | Montgomery-Gibbs Executive Airport (KMYF) | Montgomery-Gibbs Executive Airport (KMYF) | 2026-09-13 04:17 UTC | 2026-09-13 04:37 UTC | 19m |
| CPA841 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-09-12 14:06 UTC | 2026-09-13 04:29 UTC | 14h 23m |
| IGO936J | IndiGo | Cochin International Airport (VOCI) | Pune Airport (VAPO) | 2026-09-13 03:00 UTC | 2026-09-13 04:25 UTC | 1h 25m |
| CRK305 | CRK | Beijing Capital International Airport (ZBAA) | Macau International Airport (VMMC) | 2026-09-13 01:32 UTC | 2026-09-13 04:18 UTC | 2h 45m |
| LIFE45 | LIF | Caloundra Airport (YCDR) | Sunshine Coast Airport (YBMC) | 2026-09-13 04:02 UTC | 2026-09-13 04:15 UTC | 12m |
| OC95 |  | Fukuoka Airport (RJFF) | Kamigoto Airport (RJDK) | 2026-09-13 03:43 UTC | 2026-09-13 04:07 UTC | 23m |
| N911VU |  | Grand Junction Regional Airport (KGJT) | CD82 (CD82) | 2026-09-13 03:35 UTC | 2026-09-13 04:05 UTC | 30m |
| MSR917 | EgyptAir | Abu Dhabi International Airport (OMAA) | Hulwan (HE15) | 2026-09-13 01:02 UTC | 2026-09-13 04:04 UTC | 3h 1m |
| UPG | UPG | Melbourne Moorabbin Airport (YMMB) | Tooradin Airport (YTDN) | 2026-09-13 03:53 UTC | 2026-09-13 04:04 UTC | 10m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-09-13 03:53 UTC | 2026-09-13 03:59 UTC | 5m |
| MSR969 | EgyptAir | Chhatrapati Shivaji International Airport (VABB) | HE13 (HE13) | 2026-09-12 22:43 UTC | 2026-09-13 03:53 UTC | 5h 9m |
| N180B |  | NM87 (NM87) | K54F (K54F) | 2026-09-13 03:12 UTC | 2026-09-13 03:50 UTC | 38m |
| RJA300 | Royal Jordanian | Queen Alia International Airport (OJAI) | LLYO (LLYO) | 2026-09-13 03:25 UTC | 2026-09-13 03:49 UTC | 23m |
|  |  | Tribhuvan International Airport (VNKT) | Thamkharka Airport (VNTH) | 2026-09-13 03:29 UTC | 2026-09-13 03:48 UTC | 19m |
| N5UC |  | Payette Municipal Airport (KS75) | Mountain Home Municipal Airport (KU76) | 2026-09-13 03:26 UTC | 2026-09-13 03:47 UTC | 20m |
| IGO956 | IndiGo | Chennai International Airport (VOMM) | VARK (VARK) | 2026-09-13 00:23 UTC | 2026-09-13 03:47 UTC | 3h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
