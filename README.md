# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_18:36:54_UTC-green)

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

**Latest saved flight:** 2026-09-19 18:36:54 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 18:36:54 UTC

- **263,759** saved flights
- **77,885** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **263,759** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,194,882.4 tonnes** estimated CO2 emissions
- **185,210,574 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10434 |
| 2 | SkyWest Airlines | 9167 |
| 3 | EJA | 5124 |
| 4 | IndiGo | 4436 |
| 5 | American Airlines | 4129 |
| 6 | Southwest Airlines | 3880 |
| 7 | Delta Air Lines | 3288 |
| 8 | ENY | 3110 |
| 9 | LATAM Airlines | 2541 |
| 10 | AZU | 2480 |
| 11 | Vueling | 2215 |
| 12 | WIF | 2128 |
| 13 | LXJ | 2066 |
| 14 | Lufthansa | 2033 |
| 15 | easyJet | 1783 |
| 16 | Swiss International | 1742 |
| 17 | QLK | 1701 |
| 18 | EJU | 1665 |
| 19 | AXM | 1660 |
| 20 | United Airlines | 1618 |
| 21 | Alaska Airlines | 1562 |
| 22 | All Nippon Airways | 1522 |
| 23 | PGT | 1484 |
| 24 | WMT | 1483 |
| 25 | GLO | 1470 |
| 26 | Air France | 1445 |
| 27 | VIV | 1441 |
| 28 | Wizz Air | 1430 |
| 29 | CXK | 1278 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 219119 |
| 2 | 🇪🇸 ES | 16626 |
| 3 | 🇧🇷 BR | 15430 |
| 4 | 🇦🇺 AU | 15106 |
| 5 | 🇨🇦 CA | 14678 |
| 6 | 🇮🇹 IT | 14341 |
| 7 | 🇮🇳 IN | 14016 |
| 8 | 🇩🇪 DE | 12748 |
| 9 | 🇬🇧 GB | 12245 |
| 10 | 🇨🇴 CO | 11959 |
| 11 | 🇫🇷 FR | 10546 |
| 12 | 🇯🇵 JP | 10206 |
| 13 | 🇹🇷 TR | 7992 |
| 14 | 🇬🇷 GR | 7652 |
| 15 | 🇲🇽 MX | 7257 |
| 16 | 🇨🇭 CH | 7047 |
| 17 | 🇳🇴 NO | 6513 |
| 18 | 🇹🇭 TH | 4732 |
| 19 | 🇲🇾 MY | 4472 |
| 20 | 🇿🇦 ZA | 4442 |
| 21 | 🇵🇱 PL | 4349 |
| 22 | 🇳🇿 NZ | 3652 |
| 23 | 🇵🇭 PH | 3508 |
| 24 | 🇬🇹 GT | 3364 |
| 25 | 🇭🇷 HR | 3009 |
| 26 | 🇰🇷 KR | 2992 |
| 27 | 🇲🇦 MA | 2641 |
| 28 | 🇲🇪 ME | 2473 |
| 29 | 🇳🇱 NL | 2365 |
| 30 | 🇮🇩 ID | 2216 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5392 |
| 2 | Denver International Airport |  | US | 4264 |
| 3 | Indira Gandhi International Airport |  | IN | 3167 |
| 4 | Tokyo International Airport |  | JP | 3047 |
| 5 | Harry Reid International Airport |  | US | 2804 |
| 6 | El Dorado International Airport |  | CO | 2802 |
| 7 | Guaymaral Airport |  | CO | 2782 |
| 8 | Zurich Airport |  | CH | 2746 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2651 |
| 10 | La Aurora Airport |  | GT | 2556 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2554 |
| 12 | Salt Lake City International Airport |  | US | 2326 |
| 13 | Chicago O'Hare International Airport |  | US | 2267 |
| 14 | Congonhas Airport |  | BR | 2253 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2154 |
| 16 | Capua Airport |  | IT | 2064 |
| 17 | Madrid Barajas International Airport |  | ES | 2037 |
| 18 | Frankfurt am Main International Airport |  | DE | 2014 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1988 |
| 20 | Malpensa International Airport |  | IT | 1901 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1890 |
| 22 | Charles de Gaulle International Airport |  | FR | 1863 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1856 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1830 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1801 |
| 26 | Macau International Airport |  | MO | 1752 |
| 27 | Ninoy Aquino International Airport |  | PH | 1722 |
| 28 | Barcelona International Airport |  | ES | 1647 |
| 29 | Charlotte/Douglas International Airport |  | US | 1645 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1623 |
| 31 | Kuala Lumpur International Airport |  | MY | 1603 |
| 32 | Viracopos International Airport |  | BR | 1601 |
| 33 | Seattle-Tacoma International Airport |  | US | 1546 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1535 |
| 35 | Calgary International Airport |  | CA | 1503 |
| 36 | Don Mueang International Airport |  | TH | 1502 |
| 37 | Bengaluru International Airport |  | IN | 1498 |
| 38 | Oslo Gardermoen Airport |  | NO | 1485 |
| 39 | Vancouver International Airport |  | CA | 1476 |
| 40 | Antalya International Airport |  | TR | 1411 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1113 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 987 | 21m | 244 km | 4,156.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 724 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 662 | 1h 6m | 770 km | 8,794.2 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 657 | 24m | 225 km | 2,548.8 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 591 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 429 | 44m | 555 km | 4,107.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 425 | 27m | 275 km | 2,013.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 417 | 1h 50m | 1,423 km | 10,233.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 402 | 44m | 241 km | 1,669.8 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 376 | 24m | 218 km | 1,416.5 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 333 | 1h 6m | 706 km | 4,054.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 333 | 19m | 99 km | 570.4 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 333 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 283 | 42m | 535 km | 2,613.7 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 282 | 28m | 152 km | 737.0 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 262 | 18m | 14 km | 65.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N113RF |  | Lewiston/Nez Perce County Airport (KLWS) | Rugg Ranches Airport (45OG) | 2026-09-19 16:26 UTC | 2026-09-19 18:36 UTC | 2h 10m |
| N240TS |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-09-19 18:20 UTC | 2026-09-19 18:34 UTC | 13m |
| JUMP13 | JUM | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-09-19 17:44 UTC | 2026-09-19 18:32 UTC | 47m |
| FTT10 | FTT | Punta Gorda Airport (KPGD) | Venice Municipal Airport (KVNC) | 2026-09-19 17:45 UTC | 2026-09-19 18:31 UTC | 46m |
| N384CA |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-09-19 17:49 UTC | 2026-09-19 18:29 UTC | 40m |
| NDU732 | NDU | Mesa Gateway Airport (KIWA) | Pinal Airpark (KMZJ) | 2026-09-19 17:47 UTC | 2026-09-19 18:27 UTC | 40m |
| N24VF |  | TX23 (TX23) | Lampasas Airport (KLZZ) | 2026-09-19 17:51 UTC | 2026-09-19 18:21 UTC | 30m |
| N8ZW |  | CT51 (CT51) | Whelan Farms Airport (CT01) | 2026-09-19 18:05 UTC | 2026-09-19 18:20 UTC | 14m |
| N5833J |  | Fayette Airport (WV59) | West Virginia International Yeager Airport (KCRW) | 2026-09-19 17:36 UTC | 2026-09-19 18:12 UTC | 35m |
| N97398 |  | NV13 (NV13) | Dayton Valley Airpark (KA34) | 2026-09-19 17:59 UTC | 2026-09-19 18:09 UTC | 10m |
| BRG641 | BRG | Buckland Airport (PABL) | Deering Airport (PADE) | 2026-09-19 17:52 UTC | 2026-09-19 18:09 UTC | 17m |
| N259UR |  | Peeler Airpark (TS47) | Jim Sears Airport (3TA7) | 2026-09-19 17:54 UTC | 2026-09-19 18:08 UTC | 14m |
| N510JK |  | Fremont County Airport (K1V6) | Fordyce Municipal Airport (K5M4) | 2026-09-19 15:56 UTC | 2026-09-19 18:07 UTC | 2h 11m |
| N3040F |  | Greeneville Municipal Airport (KGCY) | 75TN (75TN) | 2026-09-19 17:55 UTC | 2026-09-19 18:07 UTC | 12m |
| N8417P |  | OI34 (OI34) | OI34 (OI34) | 2026-09-19 17:39 UTC | 2026-09-19 18:00 UTC | 20m |
| EJA814 | EJA | Los Angeles International Airport (KLAX) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-19 17:07 UTC | 2026-09-19 17:59 UTC | 52m |
| N226JM |  | Boeing Field/King County International Airport (KBFI) | King Salmon Airport (PAKN) | 2026-09-19 14:03 UTC | 2026-09-19 17:59 UTC | 3h 55m |
| N611MV |  | 11CA (11CA) | Hemet-Ryan Airport (KHMT) | 2026-09-19 17:00 UTC | 2026-09-19 17:58 UTC | 57m |
| N53TP |  | Delaware Coastal Airport (KGED) | Flying H Ranch Airport (68NM) | 2026-09-19 13:49 UTC | 2026-09-19 17:56 UTC | 4h 7m |
| N613GA |  | Mammoth Yosemite Airport (KMMH) | Yerington Municipal Airport (KO43) | 2026-09-19 17:24 UTC | 2026-09-19 17:54 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
