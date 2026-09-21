# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_05:09:03_UTC-green)

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

**Latest saved flight:** 2026-09-21 05:09:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-21 05:09:03 UTC

- **265,252** saved flights
- **78,181** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **265,252** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,214,643.9 tonnes** estimated CO2 emissions
- **186,356,171 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10496 |
| 2 | SkyWest Airlines | 9229 |
| 3 | EJA | 5156 |
| 4 | IndiGo | 4453 |
| 5 | American Airlines | 4144 |
| 6 | Southwest Airlines | 3907 |
| 7 | Delta Air Lines | 3303 |
| 8 | ENY | 3125 |
| 9 | LATAM Airlines | 2557 |
| 10 | AZU | 2497 |
| 11 | Vueling | 2226 |
| 12 | WIF | 2143 |
| 13 | LXJ | 2082 |
| 14 | Lufthansa | 2037 |
| 15 | easyJet | 1785 |
| 16 | Swiss International | 1745 |
| 17 | QLK | 1714 |
| 18 | EJU | 1674 |
| 19 | AXM | 1662 |
| 20 | United Airlines | 1624 |
| 21 | Alaska Airlines | 1571 |
| 22 | All Nippon Airways | 1529 |
| 23 | PGT | 1489 |
| 24 | WMT | 1489 |
| 25 | GLO | 1478 |
| 26 | Air France | 1451 |
| 27 | VIV | 1450 |
| 28 | Wizz Air | 1440 |
| 29 | CXK | 1284 |
| 30 | AEE | 1282 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 220494 |
| 2 | 🇪🇸 ES | 16680 |
| 3 | 🇧🇷 BR | 15526 |
| 4 | 🇦🇺 AU | 15196 |
| 5 | 🇨🇦 CA | 14764 |
| 6 | 🇮🇹 IT | 14450 |
| 7 | 🇮🇳 IN | 14081 |
| 8 | 🇩🇪 DE | 12784 |
| 9 | 🇬🇧 GB | 12290 |
| 10 | 🇨🇴 CO | 12065 |
| 11 | 🇫🇷 FR | 10579 |
| 12 | 🇯🇵 JP | 10238 |
| 13 | 🇹🇷 TR | 8028 |
| 14 | 🇬🇷 GR | 7680 |
| 15 | 🇲🇽 MX | 7301 |
| 16 | 🇨🇭 CH | 7066 |
| 17 | 🇳🇴 NO | 6550 |
| 18 | 🇹🇭 TH | 4758 |
| 19 | 🇲🇾 MY | 4481 |
| 20 | 🇿🇦 ZA | 4452 |
| 21 | 🇵🇱 PL | 4364 |
| 22 | 🇳🇿 NZ | 3687 |
| 23 | 🇵🇭 PH | 3529 |
| 24 | 🇬🇹 GT | 3377 |
| 25 | 🇭🇷 HR | 3026 |
| 26 | 🇰🇷 KR | 3008 |
| 27 | 🇲🇦 MA | 2653 |
| 28 | 🇲🇪 ME | 2482 |
| 29 | 🇳🇱 NL | 2377 |
| 30 | 🇮🇩 ID | 2222 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5411 |
| 2 | Denver International Airport |  | US | 4297 |
| 3 | Indira Gandhi International Airport |  | IN | 3186 |
| 4 | Tokyo International Airport |  | JP | 3060 |
| 5 | Harry Reid International Airport |  | US | 2832 |
| 6 | El Dorado International Airport |  | CO | 2831 |
| 7 | Guaymaral Airport |  | CO | 2788 |
| 8 | Zurich Airport |  | CH | 2754 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2661 |
| 10 | La Aurora Airport |  | GT | 2565 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2563 |
| 12 | Salt Lake City International Airport |  | US | 2346 |
| 13 | Chicago O'Hare International Airport |  | US | 2278 |
| 14 | Congonhas Airport |  | BR | 2262 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2172 |
| 16 | Capua Airport |  | IT | 2078 |
| 17 | Madrid Barajas International Airport |  | ES | 2046 |
| 18 | Frankfurt am Main International Airport |  | DE | 2022 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2004 |
| 20 | Malpensa International Airport |  | IT | 1918 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1897 |
| 22 | Charles de Gaulle International Airport |  | FR | 1872 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1867 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1850 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1807 |
| 26 | Macau International Airport |  | MO | 1766 |
| 27 | Ninoy Aquino International Airport |  | PH | 1733 |
| 28 | Charlotte/Douglas International Airport |  | US | 1656 |
| 29 | Barcelona International Airport |  | ES | 1656 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1636 |
| 31 | Viracopos International Airport |  | BR | 1609 |
| 32 | Kuala Lumpur International Airport |  | MY | 1606 |
| 33 | Seattle-Tacoma International Airport |  | US | 1558 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1548 |
| 35 | Calgary International Airport |  | CA | 1515 |
| 36 | Don Mueang International Airport |  | TH | 1510 |
| 37 | Bengaluru International Airport |  | IN | 1501 |
| 38 | Oslo Gardermoen Airport |  | NO | 1492 |
| 39 | Vancouver International Airport |  | CA | 1484 |
| 40 | Antalya International Airport |  | TR | 1421 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1114 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 992 | 21m | 244 km | 4,177.0 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 730 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 667 | 1h 6m | 770 km | 8,860.6 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 661 | 24m | 225 km | 2,564.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 435 | 44m | 555 km | 4,165.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 420 | 1h 50m | 1,423 km | 10,307.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 404 | 44m | 241 km | 1,678.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 380 | 24m | 218 km | 1,431.6 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 361 | 21m | 250 km | 1,559.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 350 | 23m | 55 km | 332.7 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 339 | 12m | - | - |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 18 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 334 | 1h 6m | 706 km | 4,066.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 330 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 329 | 26m | 215 km | 1,218.5 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 308 | 19m | 144 km | 766.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 288 | 1h 50m | 1,304 km | 6,479.3 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 287 | 42m | 535 km | 2,650.6 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 272 | 18m | 14 km | 68.0 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| IGO427P | IndiGo | Indira Gandhi International Airport (VIDP) | Netaji Subhash Chandra Bose International Airport (VECC) | 2026-09-21 03:11 UTC | 2026-09-21 05:09 UTC | 1h 57m |
| JUST | JUS | Holsworthy (Military) Airport (YSHW) | Holsworthy (Military) Airport (YSHW) | 2026-09-21 03:53 UTC | 2026-09-21 05:02 UTC | 1h 8m |
| BH772 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-09-21 04:48 UTC | 2026-09-21 04:48 UTC | 0m |
| N82TX |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Hayward Executive Airport (KHWD) | 2026-09-21 02:32 UTC | 2026-09-21 04:48 UTC | 2h 16m |
| N501KT |  | K3A1 (K3A1) | Auburn University Regional Airport (KAUO) | 2026-09-21 04:09 UTC | 2026-09-21 04:33 UTC | 24m |
| WIF7GT | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-09-21 04:11 UTC | 2026-09-21 04:27 UTC | 16m |
| BH772 |  | Tejgaon Airport (VGTJ) | Tejgaon Airport (VGTJ) | 2026-09-21 03:23 UTC | 2026-09-21 04:25 UTC | 1h 1m |
| QLK386D | QLK | Brisbane International Airport (YBBN) | Grenfell Airport (YGNF) | 2026-09-21 02:41 UTC | 2026-09-21 04:20 UTC | 1h 39m |
| BHA133 | BHA | Tribhuvan International Airport (VNKT) | Rukumkot Airport (VNRK) | 2026-09-21 03:30 UTC | 2026-09-21 04:15 UTC | 44m |
| 8BE |  | Sunshine Coast Airport (YBMC) | Bamawm Airport (YBMM) | 2026-09-21 01:23 UTC | 2026-09-21 04:14 UTC | 2h 50m |
| N157MW |  | Lakefront Airport (KNEW) | Denton Enterprise Airport (KDTO) | 2026-09-21 02:51 UTC | 2026-09-21 04:12 UTC | 1h 21m |
| JES3146 | JES | Ministro Pistarini International Airport (SAEZ) | Bernardo De Irigoyen Airport (SATI) | 2026-09-21 02:51 UTC | 2026-09-21 04:10 UTC | 1h 19m |
| NYT927 | NYT | Langtang Airport (VNLT) | Bhojpur Airport (VNBJ) | 2026-09-21 03:43 UTC | 2026-09-21 04:07 UTC | 23m |
| OXV | OXV | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-09-21 03:53 UTC | 2026-09-21 04:05 UTC | 11m |
| N1118Q |  | Skypark Airport (KBTF) | Nephi Municipal Airport (KU14) | 2026-09-21 03:14 UTC | 2026-09-21 04:02 UTC | 47m |
| N31 |  | Tampere-Pirkkala Airport (EFTP) | EFML (EFML) | 2026-09-21 02:58 UTC | 2026-09-21 04:00 UTC | 1h 2m |
| N423SP |  | KU42 (KU42) | Wendover Airport (KENV) | 2026-09-21 03:13 UTC | 2026-09-21 03:59 UTC | 46m |
|  |  | Tribhuvan International Airport (VNKT) | Rukumkot Airport (VNRK) | 2026-09-21 03:27 UTC | 2026-09-21 03:59 UTC | 31m |
| VOZ9203 | Virgin Australia | Perth International Airport (YPPH) | Turkey Creek Airport (YTKY) | 2026-09-21 01:24 UTC | 2026-09-21 03:58 UTC | 2h 34m |
| PGT1861 | PGT | Ercan International Airport (LCEN) | Selcuk Efes Airport (LTFB) | 2026-09-21 03:02 UTC | 2026-09-21 03:56 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
