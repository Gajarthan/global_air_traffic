# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_10:09:11_UTC-green)

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

**Latest saved flight:** 2026-09-18 10:09:11 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-18 10:09:11 UTC

- **262,102** saved flights
- **77,563** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **262,102** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,175,733.6 tonnes** estimated CO2 emissions
- **184,100,499 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10371 |
| 2 | SkyWest Airlines | 9126 |
| 3 | EJA | 5081 |
| 4 | IndiGo | 4400 |
| 5 | American Airlines | 4113 |
| 6 | Southwest Airlines | 3847 |
| 7 | Delta Air Lines | 3275 |
| 8 | ENY | 3094 |
| 9 | LATAM Airlines | 2524 |
| 10 | AZU | 2457 |
| 11 | Vueling | 2205 |
| 12 | WIF | 2115 |
| 13 | LXJ | 2050 |
| 14 | Lufthansa | 2029 |
| 15 | easyJet | 1773 |
| 16 | Swiss International | 1735 |
| 17 | QLK | 1698 |
| 18 | AXM | 1655 |
| 19 | EJU | 1650 |
| 20 | United Airlines | 1609 |
| 21 | Alaska Airlines | 1555 |
| 22 | All Nippon Airways | 1518 |
| 23 | WMT | 1478 |
| 24 | PGT | 1468 |
| 25 | GLO | 1463 |
| 26 | Air France | 1435 |
| 27 | VIV | 1431 |
| 28 | Wizz Air | 1423 |
| 29 | TKR | 1275 |
| 30 | AEE | 1271 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 217680 |
| 2 | 🇪🇸 ES | 16542 |
| 3 | 🇧🇷 BR | 15333 |
| 4 | 🇦🇺 AU | 15066 |
| 5 | 🇨🇦 CA | 14589 |
| 6 | 🇮🇹 IT | 14257 |
| 7 | 🇮🇳 IN | 13887 |
| 8 | 🇩🇪 DE | 12680 |
| 9 | 🇬🇧 GB | 12181 |
| 10 | 🇨🇴 CO | 11825 |
| 11 | 🇫🇷 FR | 10478 |
| 12 | 🇯🇵 JP | 10179 |
| 13 | 🇹🇷 TR | 7920 |
| 14 | 🇬🇷 GR | 7610 |
| 15 | 🇲🇽 MX | 7215 |
| 16 | 🇨🇭 CH | 7004 |
| 17 | 🇳🇴 NO | 6474 |
| 18 | 🇹🇭 TH | 4699 |
| 19 | 🇲🇾 MY | 4462 |
| 20 | 🇿🇦 ZA | 4424 |
| 21 | 🇵🇱 PL | 4323 |
| 22 | 🇳🇿 NZ | 3639 |
| 23 | 🇵🇭 PH | 3499 |
| 24 | 🇬🇹 GT | 3340 |
| 25 | 🇭🇷 HR | 2992 |
| 26 | 🇰🇷 KR | 2987 |
| 27 | 🇲🇦 MA | 2618 |
| 28 | 🇲🇪 ME | 2462 |
| 29 | 🇳🇱 NL | 2338 |
| 30 | 🇮🇩 ID | 2213 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5363 |
| 2 | Denver International Airport |  | US | 4240 |
| 3 | Indira Gandhi International Airport |  | IN | 3154 |
| 4 | Tokyo International Airport |  | JP | 3038 |
| 5 | Harry Reid International Airport |  | US | 2787 |
| 6 | Guaymaral Airport |  | CO | 2777 |
| 7 | El Dorado International Airport |  | CO | 2760 |
| 8 | Zurich Airport |  | CH | 2733 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2638 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2545 |
| 11 | La Aurora Airport |  | GT | 2537 |
| 12 | Salt Lake City International Airport |  | US | 2314 |
| 13 | Chicago O'Hare International Airport |  | US | 2263 |
| 14 | Congonhas Airport |  | BR | 2238 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2140 |
| 16 | Capua Airport |  | IT | 2047 |
| 17 | Madrid Barajas International Airport |  | ES | 2027 |
| 18 | Frankfurt am Main International Airport |  | DE | 2000 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1978 |
| 20 | Malpensa International Airport |  | IT | 1887 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1880 |
| 22 | Charles de Gaulle International Airport |  | FR | 1851 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1850 |
| 24 | Enrique Olaya Herrera Airport |  | CO | 1798 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1797 |
| 26 | Macau International Airport |  | MO | 1742 |
| 27 | Ninoy Aquino International Airport |  | PH | 1716 |
| 28 | Barcelona International Airport |  | ES | 1635 |
| 29 | Charlotte/Douglas International Airport |  | US | 1632 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1613 |
| 31 | Kuala Lumpur International Airport |  | MY | 1601 |
| 32 | Viracopos International Airport |  | BR | 1585 |
| 33 | Seattle-Tacoma International Airport |  | US | 1540 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1525 |
| 35 | Don Mueang International Airport |  | TH | 1497 |
| 36 | Calgary International Airport |  | CA | 1496 |
| 37 | Bengaluru International Airport |  | IN | 1488 |
| 38 | Oslo Gardermoen Airport |  | NO | 1474 |
| 39 | Vancouver International Airport |  | CA | 1467 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1403 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1112 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 978 | 21m | 244 km | 4,118.1 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 711 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 659 | 1h 6m | 770 km | 8,754.3 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 655 | 24m | 225 km | 2,541.1 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 588 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 425 | 44m | 555 km | 4,069.6 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 424 | 27m | 275 km | 2,009.2 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 414 | 1h 50m | 1,423 km | 10,160.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 399 | 44m | 241 km | 1,657.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 375 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 369 | 24m | 218 km | 1,390.2 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 359 | 21m | 250 km | 1,550.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 349 | 23m | 55 km | 331.7 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 334 | 1h 39m | 1,156 km | 6,663.2 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 332 | 19m | 99 km | 568.7 t |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 330 | 1h 6m | 706 km | 4,017.8 t |
| 18 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 327 | 12m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 324 | 26m | 215 km | 1,200.0 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 323 | 13m | - | - |
| 21 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 303 | 19m | 144 km | 753.7 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 302 | 1h 14m | 961 km | 5,005.8 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 283 | 1h 50m | 1,304 km | 6,366.8 t |
| 26 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 278 | 42m | 535 km | 2,567.5 t |
| 27 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 278 | 28m | 152 km | 726.5 t |
| 28 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 30 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-09-18 10:01 UTC | 2026-09-18 10:09 UTC | 7m |
| UAE9846 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-09-18 03:05 UTC | 2026-09-18 10:04 UTC | 6h 59m |
| MFX7482 | MFX | Mollis Airport (LSZM) | Macau International Airport (VMMC) | 2026-09-17 11:31 UTC | 2026-09-18 09:58 UTC | 22h 27m |
| SPMOC | SPM | Pobiednik Wielki Airport (EPKP) | Pobiednik Wielki Airport (EPKP) | 2026-09-18 08:57 UTC | 2026-09-18 09:57 UTC | 1h 0m |
| CHX1 | CHX | Munich International Airport (EDDM) | Oberschleisheim Airfield (EDNX) | 2026-09-18 09:44 UTC | 2026-09-18 09:54 UTC | 9m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-09-18 08:44 UTC | 2026-09-18 09:53 UTC | 1h 8m |
| IGO1452 | IndiGo | Dubai International Airport (OMDB) | Pune Airport (VAPO) | 2026-09-18 07:20 UTC | 2026-09-18 09:48 UTC | 2h 28m |
| OKLIO | OKL | Salzburg Airport (LOWS) | Hradec Kralove Airport (LKHK) | 2026-09-18 07:40 UTC | 2026-09-18 09:46 UTC | 2h 6m |
| HBLMB | HBL | Buochs Airport (LSZC) | Raron Airport (LSTA) | 2026-09-18 09:15 UTC | 2026-09-18 09:44 UTC | 29m |
| AOJ53L | AOJ | Sofia Airport (LBSF) | Kastoria National Airport (LGKA) | 2026-09-18 09:14 UTC | 2026-09-18 09:42 UTC | 28m |
| AIC2356 | Air India | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-09-18 08:53 UTC | 2026-09-18 09:41 UTC | 48m |
| OKDUN77 | OKD | Mikulovice Airport (LKMI) | Krnov Airport (LKKR) | 2026-09-18 09:04 UTC | 2026-09-18 09:39 UTC | 34m |
| AUA707X | Austrian Airlines | Vienna International Airport (LOWW) | Sibiu International Airport (LRSB) | 2026-09-18 08:48 UTC | 2026-09-18 09:37 UTC | 49m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-09-18 09:25 UTC | 2026-09-18 09:37 UTC | 12m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-09-18 09:12 UTC | 2026-09-18 09:34 UTC | 22m |
| IGO1854 | IndiGo | Jomo Kenyatta International Airport (HKJK) | Chhatrapati Shivaji International Airport (VABB) | 2026-09-18 03:44 UTC | 2026-09-18 09:33 UTC | 5h 49m |
| IGO273W | IndiGo | Netaji Subhash Chandra Bose International Airport (VECC) | Lengpui Airport (VELP) | 2026-09-18 08:52 UTC | 2026-09-18 09:27 UTC | 35m |
| AW274 |  | Casement Air Base (EIME) | Casement Air Base (EIME) | 2026-09-18 09:12 UTC | 2026-09-18 09:26 UTC | 14m |
| QTR58N | Qatar Airways | Hamad International Airport (OTHH) | Queen Alia International Airport (OJAI) | 2026-09-18 07:11 UTC | 2026-09-18 09:25 UTC | 2h 14m |
| BTK7041 | BTK | Soekarno-Hatta International Airport (WIII) | Adi Sumarmo Wiryokusumo Airport (WARQ) | 2026-09-18 08:44 UTC | 2026-09-18 09:25 UTC | 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
