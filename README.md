# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_05:27:19_UTC-green)

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

**Latest saved flight:** 2026-09-28 05:27:19 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-28 05:27:19 UTC

- **271,531** saved flights
- **79,452** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **271,531** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,292,457.0 tonnes** estimated CO2 emissions
- **190,867,072 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10682 |
| 2 | SkyWest Airlines | 9460 |
| 3 | EJA | 5317 |
| 4 | IndiGo | 4539 |
| 5 | American Airlines | 4218 |
| 6 | Southwest Airlines | 4002 |
| 7 | Delta Air Lines | 3373 |
| 8 | ENY | 3192 |
| 9 | LATAM Airlines | 2610 |
| 10 | AZU | 2548 |
| 11 | Vueling | 2257 |
| 12 | WIF | 2207 |
| 13 | LXJ | 2141 |
| 14 | Lufthansa | 2059 |
| 15 | easyJet | 1814 |
| 16 | Swiss International | 1778 |
| 17 | QLK | 1752 |
| 18 | EJU | 1698 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1661 |
| 21 | Alaska Airlines | 1604 |
| 22 | All Nippon Airways | 1560 |
| 23 | PGT | 1531 |
| 24 | GLO | 1515 |
| 25 | WMT | 1515 |
| 26 | Air France | 1492 |
| 27 | VIV | 1487 |
| 28 | Wizz Air | 1473 |
| 29 | CXK | 1335 |
| 30 | AEE | 1301 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 226291 |
| 2 | 🇪🇸 ES | 16988 |
| 3 | 🇧🇷 BR | 15896 |
| 4 | 🇦🇺 AU | 15631 |
| 5 | 🇨🇦 CA | 15140 |
| 6 | 🇮🇹 IT | 14669 |
| 7 | 🇮🇳 IN | 14358 |
| 8 | 🇩🇪 DE | 13017 |
| 9 | 🇬🇧 GB | 12550 |
| 10 | 🇨🇴 CO | 12475 |
| 11 | 🇫🇷 FR | 10782 |
| 12 | 🇯🇵 JP | 10410 |
| 13 | 🇹🇷 TR | 8219 |
| 14 | 🇬🇷 GR | 7829 |
| 15 | 🇲🇽 MX | 7494 |
| 16 | 🇨🇭 CH | 7214 |
| 17 | 🇳🇴 NO | 6704 |
| 18 | 🇹🇭 TH | 4855 |
| 19 | 🇲🇾 MY | 4539 |
| 20 | 🇿🇦 ZA | 4524 |
| 21 | 🇵🇱 PL | 4452 |
| 22 | 🇳🇿 NZ | 3820 |
| 23 | 🇵🇭 PH | 3587 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3093 |
| 26 | 🇰🇷 KR | 3068 |
| 27 | 🇲🇦 MA | 2691 |
| 28 | 🇲🇪 ME | 2547 |
| 29 | 🇳🇱 NL | 2439 |
| 30 | 🇮🇩 ID | 2260 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5532 |
| 2 | Denver International Airport |  | US | 4426 |
| 3 | Indira Gandhi International Airport |  | IN | 3244 |
| 4 | Tokyo International Airport |  | JP | 3117 |
| 5 | El Dorado International Airport |  | CO | 2963 |
| 6 | Harry Reid International Airport |  | US | 2918 |
| 7 | Guaymaral Airport |  | CO | 2826 |
| 8 | Zurich Airport |  | CH | 2811 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2721 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2607 |
| 11 | La Aurora Airport |  | GT | 2601 |
| 12 | Salt Lake City International Airport |  | US | 2401 |
| 13 | Chicago O'Hare International Airport |  | US | 2315 |
| 14 | Congonhas Airport |  | BR | 2313 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2223 |
| 16 | Capua Airport |  | IT | 2096 |
| 17 | Madrid Barajas International Airport |  | ES | 2092 |
| 18 | Frankfurt am Main International Airport |  | DE | 2053 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2052 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1931 |
| 21 | Malpensa International Airport |  | IT | 1931 |
| 22 | Charles de Gaulle International Airport |  | FR | 1928 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1910 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1904 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1825 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1761 |
| 28 | Charlotte/Douglas International Airport |  | US | 1697 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1692 |
| 30 | Barcelona International Airport |  | ES | 1683 |
| 31 | Viracopos International Airport |  | BR | 1634 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1596 |
| 34 | Seattle-Tacoma International Airport |  | US | 1591 |
| 35 | Calgary International Airport |  | CA | 1546 |
| 36 | Don Mueang International Airport |  | TH | 1535 |
| 37 | Bengaluru International Airport |  | IN | 1527 |
| 38 | Oslo Gardermoen Airport |  | NO | 1521 |
| 39 | Vancouver International Airport |  | CA | 1520 |
| 40 | Reno/Tahoe International Airport |  | US | 1451 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1125 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1019 | 21m | 244 km | 4,290.7 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 751 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 684 | 1h 6m | 770 km | 9,086.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 678 | 24m | 225 km | 2,630.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 452 | 44m | 555 km | 4,328.1 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 437 | 27m | 275 km | 2,070.8 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 429 | 1h 50m | 1,423 km | 10,528.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 415 | 44m | 241 km | 1,723.8 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 388 | 24m | 218 km | 1,461.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 367 | 21m | 250 km | 1,585.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 347 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 315 | 19m | 144 km | 783.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 307 | 1h 14m | 961 km | 5,088.7 t |
| 24 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 301 | 42m | 535 km | 2,779.9 t |
| 25 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 299 | 18m | 14 km | 74.8 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 294 | 1h 50m | 1,304 km | 6,614.3 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N561SR |  | Fresno Yosemite International Airport (KFAT) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-28 04:58 UTC | 2026-09-28 05:27 UTC | 28m |
| AAL3010 | American Airlines | Miami International Airport (KMIA) | San Diego International Airport (KSAN) | 2026-09-28 00:34 UTC | 2026-09-28 05:23 UTC | 4h 49m |
| UAL1102 | United Airlines | Newark Liberty International Airport (KEWR) | San Diego International Airport (KSAN) | 2026-09-28 00:10 UTC | 2026-09-28 05:12 UTC | 5h 2m |
| WUJ | WUJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-28 04:56 UTC | 2026-09-28 05:10 UTC | 14m |
| CHCK37 | CHC | Mount Hotham Airport (YHOT) | Yarram Airport (YYRM) | 2026-09-28 05:09 UTC | 2026-09-28 05:09 UTC | 0m |
| NPF | NPF | RAAF Williams Point Cook Base (YMPC) | RAAF Williams Point Cook Base (YMPC) | 2026-09-28 04:28 UTC | 2026-09-28 05:09 UTC | 40m |
| VYR19 | VYR | Springdale Municipal Airport (KASG) | Mineta San Jose International Airport (KSJC) | 2026-09-28 01:35 UTC | 2026-09-28 05:07 UTC | 3h 31m |
| AEA27GB | AEA | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 2026-09-28 04:40 UTC | 2026-09-28 05:04 UTC | 24m |
| DERDH | DER | Soest/Bad Sassendorf Airport (EDLZ) | Essen Mulheim Airport (EDLE) | 2026-09-28 04:41 UTC | 2026-09-28 05:02 UTC | 21m |
| JON07 | JON | Kruunupyy Airport (EFKK) | Lulea Airport (ESPA) | 2026-09-28 04:35 UTC | 2026-09-28 04:54 UTC | 18m |
| VOZ1117 | Virgin Australia | Brisbane International Airport (YBBN) | Lakeside Airpark (YLAK) | 2026-09-28 03:40 UTC | 2026-09-28 04:53 UTC | 1h 12m |
| DLH5JV | Lufthansa | Leipzig Halle Airport (EDDP) | Frankfurt am Main International Airport (EDDF) | 2026-09-28 04:17 UTC | 2026-09-28 04:51 UTC | 34m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-09-28 04:28 UTC | 2026-09-28 04:47 UTC | 19m |
| NMU | NMU | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-28 04:32 UTC | 2026-09-28 04:45 UTC | 12m |
| FFT1589 | FFT | Harry Reid International Airport (KLAS) | Mineta San Jose International Airport (KSJC) | 2026-09-28 03:40 UTC | 2026-09-28 04:44 UTC | 1h 3m |
| N1736T |  | Bolinder Field/Tooele Valley Airport (KTVY) | Wendover Airport (KENV) | 2026-09-28 03:54 UTC | 2026-09-28 04:43 UTC | 49m |
| AZU4411 | AZU | Fazenda Saco da Tapera Airport (SSOT) | Benedito Mutran Airport (SIBD) | 2026-09-28 03:11 UTC | 2026-09-28 04:41 UTC | 1h 30m |
| AEE352 | AEE | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 2026-09-28 04:20 UTC | 2026-09-28 04:39 UTC | 19m |
| RYR11EX | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-09-28 04:17 UTC | 2026-09-28 04:35 UTC | 18m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-28 04:21 UTC | 2026-09-28 04:34 UTC | 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
