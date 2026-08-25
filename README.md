# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_17:32:38_UTC-green)

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

**Latest saved flight:** 2026-08-25 17:32:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-25 17:32:38 UTC

- **235,899** saved flights
- **72,104** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **235,899** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,840,766.0 tonnes** estimated CO2 emissions
- **164,682,088 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9458 |
| 2 | SkyWest Airlines | 8318 |
| 3 | EJA | 4574 |
| 4 | IndiGo | 3983 |
| 5 | American Airlines | 3826 |
| 6 | Southwest Airlines | 3600 |
| 7 | Delta Air Lines | 3000 |
| 8 | ENY | 2861 |
| 9 | LATAM Airlines | 2263 |
| 10 | AZU | 2197 |
| 11 | Vueling | 2020 |
| 12 | Lufthansa | 1918 |
| 13 | WIF | 1878 |
| 14 | LXJ | 1847 |
| 15 | easyJet | 1646 |
| 16 | Swiss International | 1585 |
| 17 | AXM | 1575 |
| 18 | EJU | 1513 |
| 19 | QLK | 1497 |
| 20 | United Airlines | 1489 |
| 21 | Alaska Airlines | 1417 |
| 22 | All Nippon Airways | 1401 |
| 23 | WMT | 1318 |
| 24 | GLO | 1314 |
| 25 | VIV | 1301 |
| 26 | PGT | 1287 |
| 27 | Air France | 1282 |
| 28 | Wizz Air | 1261 |
| 29 | AEE | 1172 |
| 30 | JetBlue | 1168 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 195883 |
| 2 | 🇪🇸 ES | 15162 |
| 3 | 🇧🇷 BR | 13767 |
| 4 | 🇦🇺 AU | 13340 |
| 5 | 🇨🇦 CA | 13035 |
| 6 | 🇮🇹 IT | 12867 |
| 7 | 🇮🇳 IN | 12410 |
| 8 | 🇩🇪 DE | 11639 |
| 9 | 🇬🇧 GB | 11133 |
| 10 | 🇨🇴 CO | 9981 |
| 11 | 🇯🇵 JP | 9545 |
| 12 | 🇫🇷 FR | 9481 |
| 13 | 🇹🇷 TR | 7005 |
| 14 | 🇬🇷 GR | 6955 |
| 15 | 🇲🇽 MX | 6548 |
| 16 | 🇨🇭 CH | 6310 |
| 17 | 🇳🇴 NO | 5851 |
| 18 | 🇲🇾 MY | 4224 |
| 19 | 🇹🇭 TH | 4218 |
| 20 | 🇿🇦 ZA | 4141 |
| 21 | 🇵🇱 PL | 3936 |
| 22 | 🇳🇿 NZ | 3249 |
| 23 | 🇵🇭 PH | 3241 |
| 24 | 🇬🇹 GT | 2951 |
| 25 | 🇰🇷 KR | 2757 |
| 26 | 🇭🇷 HR | 2714 |
| 27 | 🇲🇦 MA | 2390 |
| 28 | 🇲🇪 ME | 2194 |
| 29 | 🇳🇱 NL | 2121 |
| 30 | 🇮🇩 ID | 2057 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4892 |
| 2 | Denver International Airport |  | US | 3810 |
| 3 | Indira Gandhi International Airport |  | IN | 2879 |
| 4 | Tokyo International Airport |  | JP | 2842 |
| 5 | Guaymaral Airport |  | CO | 2685 |
| 6 | Harry Reid International Airport |  | US | 2524 |
| 7 | Zurich Airport |  | CH | 2473 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2408 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2363 |
| 10 | La Aurora Airport |  | GT | 2250 |
| 11 | El Dorado International Airport |  | CO | 2237 |
| 12 | Chicago O'Hare International Airport |  | US | 2124 |
| 13 | Salt Lake City International Airport |  | US | 2075 |
| 14 | Congonhas Airport |  | BR | 2009 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1975 |
| 16 | Frankfurt am Main International Airport |  | DE | 1877 |
| 17 | Madrid Barajas International Airport |  | ES | 1854 |
| 18 | Capua Airport |  | IT | 1852 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1773 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1738 |
| 21 | Malpensa International Airport |  | IT | 1689 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1672 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1649 |
| 24 | Charles de Gaulle International Airport |  | FR | 1644 |
| 25 | Macau International Airport |  | MO | 1613 |
| 26 | Ninoy Aquino International Airport |  | PH | 1567 |
| 27 | Kuala Lumpur International Airport |  | MY | 1526 |
| 28 | Charlotte/Douglas International Airport |  | US | 1520 |
| 29 | Barcelona International Airport |  | ES | 1490 |
| 30 | Enrique Olaya Herrera Airport |  | CO | 1468 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1427 |
| 32 | Viracopos International Airport |  | BR | 1406 |
| 33 | Bengaluru International Airport |  | IN | 1384 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1381 |
| 35 | Seattle-Tacoma International Airport |  | US | 1381 |
| 36 | Don Mueang International Airport |  | TH | 1368 |
| 37 | Calgary International Airport |  | CA | 1346 |
| 38 | Oslo Gardermoen Airport |  | NO | 1324 |
| 39 | O. R. Tambo International Airport |  | ZA | 1286 |
| 40 | Vancouver International Airport |  | CA | 1285 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1088 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 864 | 21m | 244 km | 3,638.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 598 | 1h 6m | 770 km | 7,944.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 595 | 24m | 225 km | 2,308.3 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 595 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 528 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 390 | 27m | 275 km | 1,848.0 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 365 | 1h 50m | 1,423 km | 8,957.7 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 362 | 35m | - | - |
| 10 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 343 | 44m | 555 km | 3,284.4 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 341 | 44m | 241 km | 1,416.4 t |
| 12 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 333 | 21m | 250 km | 1,438.4 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 317 | 1h 7m | 706 km | 3,859.5 t |
| 14 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 316 | 24m | 218 km | 1,190.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 312 | 1h 40m | 1,156 km | 6,224.3 t |
| 16 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 311 | 22m | 55 km | 295.6 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 292 | 19m | 99 km | 500.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 290 | 27m | 215 km | 1,074.0 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 276 | 12m | - | - |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 273 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 272 | 1h 14m | 961 km | 4,508.5 t |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 267 | 29m | 304 km | 1,399.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 267 | 19m | 144 km | 664.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 262 | 15m | 154 km | 694.2 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 252 | 1h 50m | 1,304 km | 5,669.4 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 246 | 28m | 152 km | 642.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LVS028 | LVS | Islas Malvinas Airport (SAAR) | Islas Malvinas Airport (SAAR) | 2026-08-25 17:22 UTC | 2026-08-25 17:32 UTC | 10m |
| N106JL |  | John C Tune Airport (KJWN) | Dickson Municipal Airport (KM02) | 2026-08-25 16:36 UTC | 2026-08-25 17:28 UTC | 51m |
| N4787E |  | Caldwell Executive Airport (KEUL) | Lanham Field (04ID) | 2026-08-25 16:54 UTC | 2026-08-25 17:25 UTC | 30m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-25 16:30 UTC | 2026-08-25 17:20 UTC | 50m |
| PDU53 | PDU | Purdue University Airport (KLAF) | De Ford Airport (4II0) | 2026-08-25 17:08 UTC | 2026-08-25 17:20 UTC | 11m |
| N8024Q |  | Trenton Mercer Airport (KTTN) | Northeast Philadelphia Airport (KPNE) | 2026-08-25 16:46 UTC | 2026-08-25 17:19 UTC | 33m |
| N981HC |  | Salt Lake City International Airport (KSLC) | Flying R Airport (11UT) | 2026-08-25 17:01 UTC | 2026-08-25 17:17 UTC | 15m |
| BRU990 | BRU | Pulkovo Airport (ULLI) | Gomel Airport (UMGG) | 2026-08-25 15:33 UTC | 2026-08-25 17:13 UTC | 1h 40m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-08-25 16:56 UTC | 2026-08-25 17:13 UTC | 16m |
| SCU19 | SCU | Sahoma Lake Airport (03OK) | Neversweat Airport (1OK0) | 2026-08-25 16:33 UTC | 2026-08-25 17:12 UTC | 38m |
| CXK335 | CXK | Hartford-Brainard Airport (KHFD) | Hartford-Brainard Airport (KHFD) | 2026-08-25 16:14 UTC | 2026-08-25 17:12 UTC | 57m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-08-25 16:59 UTC | 2026-08-25 17:11 UTC | 12m |
| N780U |  | Ohio University Airport (KUNI) | Ohio University Airport (KUNI) | 2026-08-25 17:06 UTC | 2026-08-25 17:10 UTC | 3m |
| N2122M |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-08-25 16:44 UTC | 2026-08-25 17:08 UTC | 24m |
| N6812W |  | Abbotsford Airport (CYXX) | Merritt Airport (CAD5) | 2026-08-25 16:38 UTC | 2026-08-25 17:08 UTC | 30m |
| EXS2 | EXS | Newquay Cornwall Airport (EGHQ) | Newquay Cornwall Airport (EGHQ) | 2026-08-25 16:37 UTC | 2026-08-25 17:07 UTC | 30m |
| N4950U |  | Albuquerque International Sunport Airport (KABQ) | Albuquerque International Sunport Airport (KABQ) | 2026-08-25 15:52 UTC | 2026-08-25 17:07 UTC | 1h 15m |
| N9451T |  | Georgetown Executive Airport (KGTU) | 8TE7 (8TE7) | 2026-08-25 16:25 UTC | 2026-08-25 17:07 UTC | 41m |
| N9863Q |  | Kodiak Municipal Airport (PAKD) | Kodiak Municipal Airport (PAKD) | 2026-08-25 17:01 UTC | 2026-08-25 17:05 UTC | 4m |
| TOPCT25 | TOP | Offutt Afb Airport (KOFF) | 0SD0 (0SD0) | 2026-08-25 15:16 UTC | 2026-08-25 17:04 UTC | 1h 48m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
