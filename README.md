# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_07:38:05_UTC-green)

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

**Latest saved flight:** 2026-10-01 07:38:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-01 07:38:05 UTC

- **273,616** saved flights
- **79,867** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **273,616** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,312,667.3 tonnes** estimated CO2 emissions
- **192,038,682 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10749 |
| 2 | SkyWest Airlines | 9519 |
| 3 | EJA | 5359 |
| 4 | IndiGo | 4565 |
| 5 | American Airlines | 4238 |
| 6 | Southwest Airlines | 4025 |
| 7 | Delta Air Lines | 3395 |
| 8 | ENY | 3206 |
| 9 | LATAM Airlines | 2643 |
| 10 | AZU | 2573 |
| 11 | Vueling | 2273 |
| 12 | WIF | 2225 |
| 13 | LXJ | 2154 |
| 14 | Lufthansa | 2066 |
| 15 | easyJet | 1822 |
| 16 | Swiss International | 1792 |
| 17 | QLK | 1772 |
| 18 | EJU | 1707 |
| 19 | AXM | 1683 |
| 20 | United Airlines | 1671 |
| 21 | Alaska Airlines | 1614 |
| 22 | All Nippon Airways | 1565 |
| 23 | PGT | 1540 |
| 24 | WMT | 1526 |
| 25 | GLO | 1525 |
| 26 | Air France | 1504 |
| 27 | VIV | 1499 |
| 28 | Wizz Air | 1484 |
| 29 | CXK | 1352 |
| 30 | AEE | 1307 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 228109 |
| 2 | 🇪🇸 ES | 17110 |
| 3 | 🇧🇷 BR | 16058 |
| 4 | 🇦🇺 AU | 15817 |
| 5 | 🇨🇦 CA | 15253 |
| 6 | 🇮🇹 IT | 14771 |
| 7 | 🇮🇳 IN | 14445 |
| 8 | 🇩🇪 DE | 13117 |
| 9 | 🇨🇴 CO | 12653 |
| 10 | 🇬🇧 GB | 12611 |
| 11 | 🇫🇷 FR | 10843 |
| 12 | 🇯🇵 JP | 10454 |
| 13 | 🇹🇷 TR | 8281 |
| 14 | 🇬🇷 GR | 7876 |
| 15 | 🇲🇽 MX | 7557 |
| 16 | 🇨🇭 CH | 7262 |
| 17 | 🇳🇴 NO | 6752 |
| 18 | 🇹🇭 TH | 4894 |
| 19 | 🇲🇾 MY | 4559 |
| 20 | 🇿🇦 ZA | 4551 |
| 21 | 🇵🇱 PL | 4473 |
| 22 | 🇳🇿 NZ | 3869 |
| 23 | 🇵🇭 PH | 3610 |
| 24 | 🇬🇹 GT | 3430 |
| 25 | 🇭🇷 HR | 3113 |
| 26 | 🇰🇷 KR | 3084 |
| 27 | 🇲🇦 MA | 2704 |
| 28 | 🇲🇪 ME | 2570 |
| 29 | 🇳🇱 NL | 2450 |
| 30 | 🇮🇩 ID | 2268 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5560 |
| 2 | Denver International Airport |  | US | 4460 |
| 3 | Indira Gandhi International Airport |  | IN | 3266 |
| 4 | Tokyo International Airport |  | JP | 3134 |
| 5 | El Dorado International Airport |  | CO | 3009 |
| 6 | Harry Reid International Airport |  | US | 2944 |
| 7 | Guaymaral Airport |  | CO | 2841 |
| 8 | Zurich Airport |  | CH | 2840 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2737 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2622 |
| 11 | La Aurora Airport |  | GT | 2607 |
| 12 | Salt Lake City International Airport |  | US | 2422 |
| 13 | Congonhas Airport |  | BR | 2336 |
| 14 | Chicago O'Hare International Airport |  | US | 2320 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2241 |
| 16 | Capua Airport |  | IT | 2120 |
| 17 | Madrid Barajas International Airport |  | ES | 2107 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2074 |
| 19 | Frankfurt am Main International Airport |  | DE | 2063 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1945 |
| 21 | Malpensa International Airport |  | IT | 1943 |
| 22 | Hartsfield/Jackson Atlanta International Airport |  | US | 1942 |
| 23 | Charles de Gaulle International Airport |  | FR | 1940 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1928 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1830 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1773 |
| 28 | Charlotte/Douglas International Airport |  | US | 1710 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1699 |
| 30 | Barcelona International Airport |  | ES | 1691 |
| 31 | Viracopos International Airport |  | BR | 1642 |
| 32 | Kuala Lumpur International Airport |  | MY | 1632 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1606 |
| 34 | Seattle-Tacoma International Airport |  | US | 1602 |
| 35 | Calgary International Airport |  | CA | 1554 |
| 36 | Don Mueang International Airport |  | TH | 1545 |
| 37 | Bengaluru International Airport |  | IN | 1533 |
| 38 | Oslo Gardermoen Airport |  | NO | 1532 |
| 39 | Vancouver International Airport |  | CA | 1531 |
| 40 | Reno/Tahoe International Airport |  | US | 1477 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1130 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1030 | 21m | 244 km | 4,337.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 762 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 693 | 1h 6m | 770 km | 9,206.0 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 686 | 24m | 225 km | 2,661.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 603 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 457 | 44m | 555 km | 4,376.0 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 440 | 27m | 275 km | 2,085.0 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 433 | 1h 50m | 1,423 km | 10,626.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 419 | 44m | 241 km | 1,740.4 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 392 | 24m | 218 km | 1,476.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 370 | 23m | 55 km | 351.7 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 370 | 21m | 250 km | 1,598.2 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 350 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 347 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 340 | 26m | 215 km | 1,259.2 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 318 | 19m | 144 km | 791.0 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 310 | 18m | 14 km | 77.5 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 310 | 1h 14m | 961 km | 5,138.4 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 271 | 44m | 431 km | 2,016.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| BH772 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-10-01 07:23 UTC | 2026-10-01 07:38 UTC | 14m |
| BH772 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-10-01 06:58 UTC | 2026-10-01 07:13 UTC | 14m |
| VTJMR | VTJ | Jamnagar Airport (VAJM) | Pune Airport (VAPO) | 2026-10-01 06:22 UTC | 2026-10-01 07:12 UTC | 50m |
| SWT182 | SWT | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 2026-10-01 06:55 UTC | 2026-10-01 07:05 UTC | 10m |
| VLG3229 | Vueling | Santiago de Compostela Airport (LEST) | Tenerife Norte Airport (GCXO) | 2026-10-01 04:32 UTC | 2026-10-01 06:53 UTC | 2h 20m |
| WSK155 | WSK | Perth International Airport (YPPH) | Kondinin Airport (YKDN) | 2026-10-01 06:10 UTC | 2026-10-01 06:51 UTC | 41m |
| TONIC1 | TON | Nordholz-Spieka Airport (EDXN) | Kuhrstedt-Bederkesa Airport (EDXZ) | 2026-10-01 06:26 UTC | 2026-10-01 06:51 UTC | 25m |
| RNA206 | RNA | Indira Gandhi International Airport (VIDP) | Simara Airport (VNSI) | 2026-10-01 05:40 UTC | 2026-10-01 06:50 UTC | 1h 9m |
| IGO239V | IndiGo | Indira Gandhi International Airport (VIDP) | Burnpur Airport (VE23) | 2026-10-01 05:21 UTC | 2026-10-01 06:49 UTC | 1h 28m |
| FRO672 | FRO | Malmo Sturup Airport (ESMS) | Stockholm-Bromma Airport (ESSB) | 2026-10-01 05:49 UTC | 2026-10-01 06:46 UTC | 57m |
| R20176 |  | Ladd Army Air Field (PAFB) | Ladd Army Air Field (PAFB) | 2026-10-01 06:24 UTC | 2026-10-01 06:44 UTC | 20m |
| TVF40JP | TVF | Lyon Saint-Exupery Airport (LFLL) | Santorini Airport (LGSR) | 2026-10-01 04:08 UTC | 2026-10-01 06:40 UTC | 2h 32m |
| AXM6496 | AXM | Kota Kinabalu International Airport (WBKK) | Telupid Airport (WBKE) | 2026-10-01 06:24 UTC | 2026-10-01 06:39 UTC | 14m |
| JAL2737 | Japan Airlines | Okadama Airport (RJCO) | RJCS (RJCS) | 2026-10-01 06:08 UTC | 2026-10-01 06:39 UTC | 30m |
| WID64M | WID | Oslo Gardermoen Airport (ENGM) | Ørsta-Volda Airport Hovden (ENOV) | 2026-10-01 05:51 UTC | 2026-10-01 06:38 UTC | 46m |
| SFJ81 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-10-01 05:26 UTC | 2026-10-01 06:34 UTC | 1h 8m |
| WJF3LP | WJF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-10-01 05:53 UTC | 2026-10-01 06:31 UTC | 38m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Woodville Airport (YWVL) | 2026-10-01 05:50 UTC | 2026-10-01 06:30 UTC | 40m |
| AZU4112 | AZU | Val de Cans/Julio Cezar Ribeiro International Airport (SBBE) | Maraba Airport (SBMA) | 2026-10-01 05:49 UTC | 2026-10-01 06:29 UTC | 40m |
| THA319 | Thai Airways | Suvarnabhumi Airport (VTBS) | Tribhuvan International Airport (VNKT) | 2026-10-01 03:36 UTC | 2026-10-01 06:26 UTC | 2h 50m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
