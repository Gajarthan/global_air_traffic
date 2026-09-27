# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_10:34:56_UTC-green)

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

**Latest saved flight:** 2026-09-27 10:34:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-27 10:34:56 UTC

- **270,753** saved flights
- **79,287** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **270,753** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,283,936.9 tonnes** estimated CO2 emissions
- **190,373,155 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10657 |
| 2 | SkyWest Airlines | 9426 |
| 3 | EJA | 5286 |
| 4 | IndiGo | 4532 |
| 5 | American Airlines | 4208 |
| 6 | Southwest Airlines | 3986 |
| 7 | Delta Air Lines | 3365 |
| 8 | ENY | 3181 |
| 9 | LATAM Airlines | 2603 |
| 10 | AZU | 2537 |
| 11 | Vueling | 2253 |
| 12 | WIF | 2201 |
| 13 | LXJ | 2128 |
| 14 | Lufthansa | 2056 |
| 15 | easyJet | 1813 |
| 16 | Swiss International | 1774 |
| 17 | QLK | 1743 |
| 18 | EJU | 1695 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1657 |
| 21 | Alaska Airlines | 1599 |
| 22 | All Nippon Airways | 1557 |
| 23 | PGT | 1528 |
| 24 | WMT | 1514 |
| 25 | GLO | 1508 |
| 26 | Air France | 1490 |
| 27 | VIV | 1478 |
| 28 | Wizz Air | 1471 |
| 29 | CXK | 1330 |
| 30 | AEE | 1298 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 225512 |
| 2 | 🇪🇸 ES | 16951 |
| 3 | 🇧🇷 BR | 15824 |
| 4 | 🇦🇺 AU | 15564 |
| 5 | 🇨🇦 CA | 15090 |
| 6 | 🇮🇹 IT | 14644 |
| 7 | 🇮🇳 IN | 14344 |
| 8 | 🇩🇪 DE | 12993 |
| 9 | 🇬🇧 GB | 12523 |
| 10 | 🇨🇴 CO | 12430 |
| 11 | 🇫🇷 FR | 10760 |
| 12 | 🇯🇵 JP | 10400 |
| 13 | 🇹🇷 TR | 8197 |
| 14 | 🇬🇷 GR | 7811 |
| 15 | 🇲🇽 MX | 7473 |
| 16 | 🇨🇭 CH | 7199 |
| 17 | 🇳🇴 NO | 6687 |
| 18 | 🇹🇭 TH | 4841 |
| 19 | 🇲🇾 MY | 4539 |
| 20 | 🇿🇦 ZA | 4518 |
| 21 | 🇵🇱 PL | 4441 |
| 22 | 🇳🇿 NZ | 3800 |
| 23 | 🇵🇭 PH | 3586 |
| 24 | 🇬🇹 GT | 3422 |
| 25 | 🇭🇷 HR | 3090 |
| 26 | 🇰🇷 KR | 3060 |
| 27 | 🇲🇦 MA | 2687 |
| 28 | 🇲🇪 ME | 2541 |
| 29 | 🇳🇱 NL | 2422 |
| 30 | 🇮🇩 ID | 2257 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5512 |
| 2 | Denver International Airport |  | US | 4411 |
| 3 | Indira Gandhi International Airport |  | IN | 3242 |
| 4 | Tokyo International Airport |  | JP | 3113 |
| 5 | El Dorado International Airport |  | CO | 2948 |
| 6 | Harry Reid International Airport |  | US | 2901 |
| 7 | Guaymaral Airport |  | CO | 2821 |
| 8 | Zurich Airport |  | CH | 2807 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2718 |
| 10 | La Aurora Airport |  | GT | 2601 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2601 |
| 12 | Salt Lake City International Airport |  | US | 2392 |
| 13 | Chicago O'Hare International Airport |  | US | 2310 |
| 14 | Congonhas Airport |  | BR | 2307 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2215 |
| 16 | Capua Airport |  | IT | 2094 |
| 17 | Madrid Barajas International Airport |  | ES | 2086 |
| 18 | Frankfurt am Main International Airport |  | DE | 2049 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2044 |
| 20 | Malpensa International Airport |  | IT | 1931 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1925 |
| 22 | Charles de Gaulle International Airport |  | FR | 1925 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1904 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1895 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1824 |
| 26 | Macau International Airport |  | MO | 1788 |
| 27 | Ninoy Aquino International Airport |  | PH | 1760 |
| 28 | Charlotte/Douglas International Airport |  | US | 1696 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1684 |
| 30 | Barcelona International Airport |  | ES | 1682 |
| 31 | Viracopos International Airport |  | BR | 1631 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Seattle-Tacoma International Airport |  | US | 1587 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1585 |
| 35 | Calgary International Airport |  | CA | 1541 |
| 36 | Don Mueang International Airport |  | TH | 1532 |
| 37 | Bengaluru International Airport |  | IN | 1524 |
| 38 | Oslo Gardermoen Airport |  | NO | 1516 |
| 39 | Vancouver International Airport |  | CA | 1514 |
| 40 | Antalya International Airport |  | TR | 1446 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1123 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1016 | 21m | 244 km | 4,278.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 749 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 683 | 1h 6m | 770 km | 9,073.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 678 | 24m | 225 km | 2,630.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 450 | 44m | 555 km | 4,309.0 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 435 | 27m | 275 km | 2,061.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 427 | 1h 50m | 1,423 km | 10,479.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 413 | 44m | 241 km | 1,715.5 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 387 | 24m | 218 km | 1,458.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 378 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 366 | 21m | 250 km | 1,580.9 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 346 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 336 | 26m | 215 km | 1,244.4 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 314 | 19m | 144 km | 781.1 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 306 | 1h 14m | 961 km | 5,072.1 t |
| 24 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 299 | 42m | 535 km | 2,761.5 t |
| 25 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 26 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 295 | 18m | 14 km | 73.8 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 291 | 1h 50m | 1,304 km | 6,546.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LFA684 | LFA | Orlando Sanford International Airport (KSFB) | Orlando Sanford International Airport (KSFB) | 2026-09-27 10:20 UTC | 2026-09-27 10:34 UTC | 14m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Seppe Airport (EHSE) | 2026-09-27 10:17 UTC | 2026-09-27 10:33 UTC | 16m |
| PHBAT | PHB | Seppe Airport (EHSE) | Seppe Airport (EHSE) | 2026-09-27 10:16 UTC | 2026-09-27 10:30 UTC | 14m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-09-27 09:36 UTC | 2026-09-27 10:28 UTC | 51m |
| JST823 | JST | Brisbane International Airport (YBBN) | Sydney Kingsford Smith International Airport (YSSY) | 2026-09-27 08:27 UTC | 2026-09-27 09:59 UTC | 1h 31m |
| PSFGK | PSF | Val de Cans/Julio Cezar Ribeiro International Airport (SBBE) | Maraba Airport (SBMA) | 2026-09-27 09:11 UTC | 2026-09-27 09:57 UTC | 46m |
| TCREG | TCR | Milas Bodrum International Airport (LTFE) | Karain Airport (LTXE) | 2026-09-27 09:23 UTC | 2026-09-27 09:48 UTC | 24m |
| NWK1610 | NWK | Perth International Airport (YPPH) | Westonia Airport (YWSX) | 2026-09-27 09:19 UTC | 2026-09-27 09:44 UTC | 25m |
| CSB1517 | CSB | Cincinnati/Northern Kentucky International Airport (KCVG) | Austin-Bergstrom International Airport (KAUS) | 2026-09-27 07:47 UTC | 2026-09-27 09:43 UTC | 1h 56m |
| WIF1A | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-09-27 08:53 UTC | 2026-09-27 09:43 UTC | 49m |
| RYR280 | Ryanair | Venezia / Tessera -  Marco Polo Airport (LIPZ) | Trapani / Birgi Airport (LICT) | 2026-09-27 08:35 UTC | 2026-09-27 09:41 UTC | 1h 6m |
| DFLLY | DFL | Wrocław-Szymanow Airport (EPWS) | Wrocław-Szymanow Airport (EPWS) | 2026-09-27 08:05 UTC | 2026-09-27 09:41 UTC | 1h 35m |
| QLK1527 | QLK | Canberra International Airport (YSCB) | Melbourne International Airport (YMML) | 2026-09-27 08:46 UTC | 2026-09-27 09:40 UTC | 53m |
| AYT103 | AYT | Hatzor Air Base (LLHS) | Mitzpe Ramon Airfield (LLMR) | 2026-09-27 09:26 UTC | 2026-09-27 09:40 UTC | 13m |
| FGIBV | FGI | Ghisonaccia Alzitone Airport (LFKG) | Ghisonaccia Alzitone Airport (LFKG) | 2026-09-27 09:16 UTC | 2026-09-27 09:40 UTC | 23m |
| 4XDAN |  | Bar Yehuda Airfield (LLMZ) | Bar Yehuda Airfield (LLMZ) | 2026-09-27 09:29 UTC | 2026-09-27 09:37 UTC | 8m |
| AWH84L | AWH | Zurich Airport (LSZH) | Palma De Mallorca Airport (LEPA) | 2026-09-27 07:56 UTC | 2026-09-27 09:36 UTC | 1h 40m |
| AFR68LX | Air France | Charles de Gaulle International Airport (LFPG) | Toulouse-Blagnac Airport (LFBO) | 2026-09-27 08:34 UTC | 2026-09-27 09:35 UTC | 1h 0m |
| EMD305 | EMD | Albuquerque International Sunport Airport (KABQ) | Mystic Bluffs Airport (NM56) | 2026-09-27 09:10 UTC | 2026-09-27 09:33 UTC | 22m |
| GCICK | GCI | Challock Airfield (EGKE) | Lashenden (Headcorn) Airfield (EGKH) | 2026-09-27 09:12 UTC | 2026-09-27 09:32 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
