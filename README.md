# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_04:48:43_UTC-green)

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

**Latest saved flight:** 2026-09-19 04:48:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-19 04:48:43 UTC

- **263,123** saved flights
- **77,772** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **263,123** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,187,553.6 tonnes** estimated CO2 emissions
- **184,785,714 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10406 |
| 2 | SkyWest Airlines | 9157 |
| 3 | EJA | 5107 |
| 4 | IndiGo | 4418 |
| 5 | American Airlines | 4127 |
| 6 | Southwest Airlines | 3868 |
| 7 | Delta Air Lines | 3286 |
| 8 | ENY | 3103 |
| 9 | LATAM Airlines | 2535 |
| 10 | AZU | 2472 |
| 11 | Vueling | 2212 |
| 12 | WIF | 2125 |
| 13 | LXJ | 2063 |
| 14 | Lufthansa | 2030 |
| 15 | easyJet | 1777 |
| 16 | Swiss International | 1736 |
| 17 | QLK | 1701 |
| 18 | AXM | 1658 |
| 19 | EJU | 1656 |
| 20 | United Airlines | 1614 |
| 21 | Alaska Airlines | 1561 |
| 22 | All Nippon Airways | 1520 |
| 23 | WMT | 1479 |
| 24 | PGT | 1478 |
| 25 | GLO | 1469 |
| 26 | Air France | 1442 |
| 27 | VIV | 1438 |
| 28 | Wizz Air | 1428 |
| 29 | CXK | 1275 |
| 30 | TKR | 1275 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 218699 |
| 2 | 🇪🇸 ES | 16585 |
| 3 | 🇧🇷 BR | 15398 |
| 4 | 🇦🇺 AU | 15102 |
| 5 | 🇨🇦 CA | 14655 |
| 6 | 🇮🇹 IT | 14287 |
| 7 | 🇮🇳 IN | 13963 |
| 8 | 🇩🇪 DE | 12707 |
| 9 | 🇬🇧 GB | 12216 |
| 10 | 🇨🇴 CO | 11916 |
| 11 | 🇫🇷 FR | 10511 |
| 12 | 🇯🇵 JP | 10187 |
| 13 | 🇹🇷 TR | 7961 |
| 14 | 🇬🇷 GR | 7630 |
| 15 | 🇲🇽 MX | 7239 |
| 16 | 🇨🇭 CH | 7016 |
| 17 | 🇳🇴 NO | 6500 |
| 18 | 🇹🇭 TH | 4713 |
| 19 | 🇲🇾 MY | 4468 |
| 20 | 🇿🇦 ZA | 4432 |
| 21 | 🇵🇱 PL | 4335 |
| 22 | 🇳🇿 NZ | 3646 |
| 23 | 🇵🇭 PH | 3504 |
| 24 | 🇬🇹 GT | 3352 |
| 25 | 🇭🇷 HR | 3000 |
| 26 | 🇰🇷 KR | 2989 |
| 27 | 🇲🇦 MA | 2631 |
| 28 | 🇲🇪 ME | 2467 |
| 29 | 🇳🇱 NL | 2349 |
| 30 | 🇮🇩 ID | 2214 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5380 |
| 2 | Denver International Airport |  | US | 4257 |
| 3 | Indira Gandhi International Airport |  | IN | 3160 |
| 4 | Tokyo International Airport |  | JP | 3041 |
| 5 | Harry Reid International Airport |  | US | 2800 |
| 6 | El Dorado International Airport |  | CO | 2787 |
| 7 | Guaymaral Airport |  | CO | 2779 |
| 8 | Zurich Airport |  | CH | 2738 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2646 |
| 10 | La Aurora Airport |  | GT | 2548 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2548 |
| 12 | Salt Lake City International Airport |  | US | 2325 |
| 13 | Chicago O'Hare International Airport |  | US | 2265 |
| 14 | Congonhas Airport |  | BR | 2248 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2151 |
| 16 | Capua Airport |  | IT | 2052 |
| 17 | Madrid Barajas International Airport |  | ES | 2033 |
| 18 | Frankfurt am Main International Airport |  | DE | 2004 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1985 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1889 |
| 21 | Malpensa International Airport |  | IT | 1889 |
| 22 | Charles de Gaulle International Airport |  | FR | 1859 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1856 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1820 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1799 |
| 26 | Macau International Airport |  | MO | 1750 |
| 27 | Ninoy Aquino International Airport |  | PH | 1720 |
| 28 | Barcelona International Airport |  | ES | 1643 |
| 29 | Charlotte/Douglas International Airport |  | US | 1642 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1619 |
| 31 | Kuala Lumpur International Airport |  | MY | 1603 |
| 32 | Viracopos International Airport |  | BR | 1596 |
| 33 | Seattle-Tacoma International Airport |  | US | 1546 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1533 |
| 35 | Calgary International Airport |  | CA | 1502 |
| 36 | Don Mueang International Airport |  | TH | 1500 |
| 37 | Bengaluru International Airport |  | IN | 1494 |
| 38 | Oslo Gardermoen Airport |  | NO | 1481 |
| 39 | Vancouver International Airport |  | CA | 1472 |
| 40 | Antalya International Airport |  | TR | 1408 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 984 | 21m | 244 km | 4,143.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 720 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 660 | 1h 6m | 770 km | 8,767.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 656 | 24m | 225 km | 2,545.0 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 590 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 428 | 44m | 555 km | 4,098.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 415 | 1h 50m | 1,423 km | 10,184.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 401 | 44m | 241 km | 1,665.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 371 | 24m | 218 km | 1,397.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 360 | 21m | 250 km | 1,555.0 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 333 | 12m | - | - |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 331 | 1h 6m | 706 km | 4,029.9 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 326 | 26m | 215 km | 1,207.4 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 326 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 307 | 19m | 144 km | 763.6 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 284 | 1h 50m | 1,304 km | 6,389.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 281 | 42m | 535 km | 2,595.2 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 281 | 28m | 152 km | 734.4 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| JST223 | JST | Sydney Kingsford Smith International Airport (YSSY) | Queenstown International Airport (NZQN) | 2026-09-19 02:22 UTC | 2026-09-19 04:48 UTC | 2h 26m |
| FFT2107 | FFT | Joe Foss Field (KFSD) | Denver International Airport (KDEN) | 2026-09-19 03:10 UTC | 2026-09-19 04:44 UTC | 1h 34m |
| HL1269 |  | RKTA (RKTA) | Daegu Airport (RKTN) | 2026-09-19 03:09 UTC | 2026-09-19 04:35 UTC | 1h 25m |
| JAL6777 | Japan Airlines | Narita International Airport (RJAA) | Tianjin Binhai International Airport (ZBTJ) | 2026-09-19 01:19 UTC | 2026-09-19 04:26 UTC | 3h 6m |
| CWA927 | CWA | Calgary International Airport (CYYC) | Ross International Airport (CEP4) | 2026-09-19 03:55 UTC | 2026-09-19 04:23 UTC | 28m |
| VOZ147 | Virgin Australia | Melbourne International Airport (YMML) | Queenstown International Airport (NZQN) | 2026-09-19 01:55 UTC | 2026-09-19 04:23 UTC | 2h 27m |
| CGHCV | CGH | Regina International Airport (CYQR) | Calgary / Springbank Airport (CYBW) | 2026-09-19 03:08 UTC | 2026-09-19 04:17 UTC | 1h 9m |
| JRE824 | JRE | Blue Grass Airport (KLEX) | Addison-Henley Field (0MS7) | 2026-09-19 03:07 UTC | 2026-09-19 04:04 UTC | 56m |
| NTR823 | NTR | Faa'a International Airport (NTAA) | Niau Airport (NTKN) | 2026-09-19 03:10 UTC | 2026-09-19 04:01 UTC | 51m |
| JMA8660 | JMA | Jomo Kenyatta International Airport (HKJK) | Nakuru Airport (HKNK) | 2026-09-19 03:34 UTC | 2026-09-19 03:53 UTC | 19m |
| N933SB |  | Shelby County Airport (KEET) | Okolona Municipal/Richard Stovall Field (K5A4) | 2026-09-19 03:29 UTC | 2026-09-19 03:52 UTC | 22m |
| AIC8TB | Air India | Bhuj Airport (VABJ) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-19 02:55 UTC | 2026-09-19 03:51 UTC | 56m |
| SFJ77 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-09-19 02:51 UTC | 2026-09-19 03:51 UTC | 59m |
| N548CB |  | Hector International Airport (KFAR) | Z P Field (64ND) | 2026-09-19 03:05 UTC | 2026-09-19 03:50 UTC | 45m |
| NOK542 | NOK | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 2026-09-19 03:05 UTC | 2026-09-19 03:49 UTC | 44m |
| UAL519 | United Airlines | San Diego International Airport (KSAN) | Denver International Airport (KDEN) | 2026-09-19 02:00 UTC | 2026-09-19 03:48 UTC | 1h 48m |
| ANA793 | All Nippon Airways | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 2026-09-19 02:49 UTC | 2026-09-19 03:47 UTC | 57m |
| N585AW |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-09-19 03:09 UTC | 2026-09-19 03:46 UTC | 37m |
| N616ML |  | Logan-Cache Airport (KLGU) | Preston Airport (KU10) | 2026-09-19 03:06 UTC | 2026-09-19 03:44 UTC | 38m |
| SWA1844 | Southwest Airlines | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 2026-09-19 03:24 UTC | 2026-09-19 03:44 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
