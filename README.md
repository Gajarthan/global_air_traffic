# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_09:10:05_UTC-green)

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

**Latest saved flight:** 2026-09-22 09:10:05 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-22 09:10:05 UTC

- **266,137** saved flights
- **78,323** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **266,137** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,226,963.2 tonnes** estimated CO2 emissions
- **187,070,328 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10525 |
| 2 | SkyWest Airlines | 9259 |
| 3 | EJA | 5171 |
| 4 | IndiGo | 4470 |
| 5 | American Airlines | 4151 |
| 6 | Southwest Airlines | 3919 |
| 7 | Delta Air Lines | 3310 |
| 8 | ENY | 3130 |
| 9 | LATAM Airlines | 2563 |
| 10 | AZU | 2502 |
| 11 | Vueling | 2234 |
| 12 | WIF | 2154 |
| 13 | LXJ | 2089 |
| 14 | Lufthansa | 2039 |
| 15 | easyJet | 1790 |
| 16 | Swiss International | 1756 |
| 17 | QLK | 1721 |
| 18 | EJU | 1679 |
| 19 | AXM | 1667 |
| 20 | United Airlines | 1633 |
| 21 | Alaska Airlines | 1574 |
| 22 | All Nippon Airways | 1536 |
| 23 | PGT | 1498 |
| 24 | WMT | 1495 |
| 25 | GLO | 1483 |
| 26 | Air France | 1464 |
| 27 | VIV | 1456 |
| 28 | Wizz Air | 1447 |
| 29 | CXK | 1291 |
| 30 | AEE | 1285 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 221164 |
| 2 | 🇪🇸 ES | 16728 |
| 3 | 🇧🇷 BR | 15562 |
| 4 | 🇦🇺 AU | 15264 |
| 5 | 🇨🇦 CA | 14819 |
| 6 | 🇮🇹 IT | 14477 |
| 7 | 🇮🇳 IN | 14140 |
| 8 | 🇩🇪 DE | 12818 |
| 9 | 🇬🇧 GB | 12345 |
| 10 | 🇨🇴 CO | 12130 |
| 11 | 🇫🇷 FR | 10620 |
| 12 | 🇯🇵 JP | 10270 |
| 13 | 🇹🇷 TR | 8059 |
| 14 | 🇬🇷 GR | 7709 |
| 15 | 🇲🇽 MX | 7335 |
| 16 | 🇨🇭 CH | 7105 |
| 17 | 🇳🇴 NO | 6583 |
| 18 | 🇹🇭 TH | 4776 |
| 19 | 🇲🇾 MY | 4494 |
| 20 | 🇿🇦 ZA | 4468 |
| 21 | 🇵🇱 PL | 4373 |
| 22 | 🇳🇿 NZ | 3701 |
| 23 | 🇵🇭 PH | 3537 |
| 24 | 🇬🇹 GT | 3378 |
| 25 | 🇭🇷 HR | 3033 |
| 26 | 🇰🇷 KR | 3020 |
| 27 | 🇲🇦 MA | 2659 |
| 28 | 🇲🇪 ME | 2495 |
| 29 | 🇳🇱 NL | 2383 |
| 30 | 🇮🇩 ID | 2225 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5422 |
| 2 | Denver International Airport |  | US | 4320 |
| 3 | Indira Gandhi International Airport |  | IN | 3196 |
| 4 | Tokyo International Airport |  | JP | 3070 |
| 5 | El Dorado International Airport |  | CO | 2853 |
| 6 | Harry Reid International Airport |  | US | 2845 |
| 7 | Guaymaral Airport |  | CO | 2793 |
| 8 | Zurich Airport |  | CH | 2768 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2671 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2567 |
| 11 | La Aurora Airport |  | GT | 2566 |
| 12 | Salt Lake City International Airport |  | US | 2350 |
| 13 | Chicago O'Hare International Airport |  | US | 2285 |
| 14 | Congonhas Airport |  | BR | 2267 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2175 |
| 16 | Capua Airport |  | IT | 2083 |
| 17 | Madrid Barajas International Airport |  | ES | 2050 |
| 18 | Frankfurt am Main International Airport |  | DE | 2025 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2012 |
| 20 | Malpensa International Airport |  | IT | 1921 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1900 |
| 22 | Charles de Gaulle International Airport |  | FR | 1887 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1872 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1863 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1810 |
| 26 | Macau International Airport |  | MO | 1770 |
| 27 | Ninoy Aquino International Airport |  | PH | 1735 |
| 28 | Barcelona International Airport |  | ES | 1662 |
| 29 | Charlotte/Douglas International Airport |  | US | 1660 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1643 |
| 31 | Viracopos International Airport |  | BR | 1614 |
| 32 | Kuala Lumpur International Airport |  | MY | 1610 |
| 33 | Seattle-Tacoma International Airport |  | US | 1560 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1554 |
| 35 | Calgary International Airport |  | CA | 1519 |
| 36 | Don Mueang International Airport |  | TH | 1514 |
| 37 | Bengaluru International Airport |  | IN | 1507 |
| 38 | Oslo Gardermoen Airport |  | NO | 1499 |
| 39 | Vancouver International Airport |  | CA | 1488 |
| 40 | Antalya International Airport |  | TR | 1425 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1115 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 996 | 21m | 244 km | 4,193.9 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 735 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 669 | 1h 6m | 770 km | 8,887.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 663 | 24m | 225 km | 2,572.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 592 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 439 | 44m | 555 km | 4,203.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 426 | 27m | 275 km | 2,018.6 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 422 | 1h 50m | 1,423 km | 10,356.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 405 | 44m | 241 km | 1,682.3 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 381 | 24m | 218 km | 1,435.4 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 362 | 21m | 250 km | 1,563.6 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 352 | 23m | 55 km | 334.6 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 340 | 12m | - | - |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 336 | 1h 6m | 706 km | 4,090.8 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 336 | 19m | 99 km | 575.5 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 332 | 13m | - | - |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 330 | 26m | 215 km | 1,222.2 t |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 310 | 19m | 144 km | 771.1 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 303 | 1h 14m | 961 km | 5,022.4 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 289 | 42m | 535 km | 2,669.1 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 283 | 28m | 152 km | 739.6 t |
| 28 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 278 | 18m | 14 km | 69.5 t |
| 29 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA254 | Cathay Pacific | Chek Lap Kok International Airport (VHHH) | Zhuhai Airport (ZGSD) | 2026-09-21 05:37 UTC | 2026-09-22 09:10 UTC | 27h 32m |
|  |  | Ravenna Airport (LIDR) | Ravenna Airport (LIDR) | 2026-09-22 08:38 UTC | 2026-09-22 09:08 UTC | 29m |
| THY6218 | Turkish Airlines | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-09-22 01:39 UTC | 2026-09-22 08:57 UTC | 7h 18m |
| SRB502 | SRB | Cenej Airport (LYNS) | Batajnica Air Base (LYBT) | 2026-09-22 08:39 UTC | 2026-09-22 08:55 UTC | 16m |
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-09-21 21:49 UTC | 2026-09-22 08:52 UTC | 11h 3m |
| HBPES | HBP | Schaerding-Suben Airport (LOLS) | Schaerding-Suben Airport (LOLS) | 2026-09-22 08:37 UTC | 2026-09-22 08:50 UTC | 13m |
| STH03 | STH | Gap - Tallard Airport (LFNA) | Gap - Tallard Airport (LFNA) | 2026-09-22 08:29 UTC | 2026-09-22 08:48 UTC | 19m |
| DUKE20 | DUK | Wiesbaden Army Airfield (ETOU) | Ingolstadt Manching Airport (ETSI) | 2026-09-22 06:59 UTC | 2026-09-22 08:46 UTC | 1h 46m |
| N307KH |  | Double Eagle Ii Airport (KAEG) | Los Alamos Airport (KLAM) | 2026-09-22 08:22 UTC | 2026-09-22 08:41 UTC | 18m |
| AFR188 | Air France | Suvarnabhumi Airport (VTBS) | Zhuhai Airport (ZGSD) | 2026-09-21 04:46 UTC | 2026-09-22 08:34 UTC | 27h 48m |
| DHAID | DHA | Aerodrom dels Pirineus-Alt Urgell Airport (LESU) | La Cerdanya Airport (LECD) | 2026-09-22 08:29 UTC | 2026-09-22 08:34 UTC | 4m |
|  |  | Wangen-Lachen Airport (LSPV) | Speck-Fehraltorf Airport (LSZK) | 2026-09-22 08:24 UTC | 2026-09-22 08:28 UTC | 4m |
| CAL1806 | CAL | Taiwan Taoyuan International Airport (RCTP) | Kaohsiung International Airport (RCKH) | 2026-09-22 06:36 UTC | 2026-09-22 08:28 UTC | 1h 51m |
| JST465 | JST | Ballina Byron Gateway Airport (YBNA) | Melbourne International Airport (YMML) | 2026-09-22 06:16 UTC | 2026-09-22 08:26 UTC | 2h 10m |
| LEA153R | LEA | Sofia Airport (LBSF) | Cardak Airport (LTAY) | 2026-09-22 07:24 UTC | 2026-09-22 08:26 UTC | 1h 2m |
| HBZVU | HBZ | Meiringen Airport (LSMM) | Raron Airport (LSTA) | 2026-09-22 08:12 UTC | 2026-09-22 08:23 UTC | 10m |
| DRDNT36 | DRD | RAF Lossiemouth (EGQS) | RAF Waddington (EGXW) | 2026-09-22 07:28 UTC | 2026-09-22 08:21 UTC | 52m |
| AFR36YL | Air France | Charles de Gaulle International Airport (LFPG) | Hamburg Airport (EDDH) | 2026-09-22 07:06 UTC | 2026-09-22 08:20 UTC | 1h 13m |
| IGO43PY | IndiGo | Bengaluru International Airport (VOBL) | Giridih Airport (VE41) | 2026-09-22 06:17 UTC | 2026-09-22 08:17 UTC | 1h 59m |
| SEH3JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-09-22 07:58 UTC | 2026-09-22 08:17 UTC | 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
