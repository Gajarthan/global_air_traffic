# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_10:56:20_UTC-green)

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

**Latest saved flight:** 2026-09-10 10:56:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-10 10:56:20 UTC

- **253,465** saved flights
- **75,816** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **253,465** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,055,347.3 tonnes** estimated CO2 emissions
- **177,121,585 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10130 |
| 2 | SkyWest Airlines | 8841 |
| 3 | EJA | 4893 |
| 4 | IndiGo | 4244 |
| 5 | American Airlines | 4031 |
| 6 | Southwest Airlines | 3747 |
| 7 | Delta Air Lines | 3193 |
| 8 | ENY | 3024 |
| 9 | LATAM Airlines | 2439 |
| 10 | AZU | 2356 |
| 11 | Vueling | 2157 |
| 12 | WIF | 2030 |
| 13 | Lufthansa | 1995 |
| 14 | LXJ | 1980 |
| 15 | easyJet | 1732 |
| 16 | Swiss International | 1702 |
| 17 | QLK | 1636 |
| 18 | AXM | 1633 |
| 19 | EJU | 1621 |
| 20 | United Airlines | 1578 |
| 21 | Alaska Airlines | 1511 |
| 22 | All Nippon Airways | 1481 |
| 23 | WMT | 1435 |
| 24 | GLO | 1409 |
| 25 | PGT | 1394 |
| 26 | VIV | 1385 |
| 27 | Air France | 1380 |
| 28 | Wizz Air | 1380 |
| 29 | JetBlue | 1237 |
| 30 | AEE | 1235 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 210351 |
| 2 | 🇪🇸 ES | 16166 |
| 3 | 🇧🇷 BR | 14779 |
| 4 | 🇦🇺 AU | 14467 |
| 5 | 🇨🇦 CA | 14101 |
| 6 | 🇮🇹 IT | 13878 |
| 7 | 🇮🇳 IN | 13285 |
| 8 | 🇩🇪 DE | 12411 |
| 9 | 🇬🇧 GB | 11849 |
| 10 | 🇨🇴 CO | 11215 |
| 11 | 🇫🇷 FR | 10190 |
| 12 | 🇯🇵 JP | 9949 |
| 13 | 🇹🇷 TR | 7587 |
| 14 | 🇬🇷 GR | 7421 |
| 15 | 🇲🇽 MX | 6981 |
| 16 | 🇨🇭 CH | 6820 |
| 17 | 🇳🇴 NO | 6273 |
| 18 | 🇹🇭 TH | 4561 |
| 19 | 🇲🇾 MY | 4394 |
| 20 | 🇿🇦 ZA | 4327 |
| 21 | 🇵🇱 PL | 4216 |
| 22 | 🇳🇿 NZ | 3470 |
| 23 | 🇵🇭 PH | 3430 |
| 24 | 🇬🇹 GT | 3148 |
| 25 | 🇰🇷 KR | 2921 |
| 26 | 🇭🇷 HR | 2910 |
| 27 | 🇲🇦 MA | 2558 |
| 28 | 🇲🇪 ME | 2382 |
| 29 | 🇳🇱 NL | 2283 |
| 30 | 🇮🇩 ID | 2167 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5217 |
| 2 | Denver International Airport |  | US | 4093 |
| 3 | Indira Gandhi International Airport |  | IN | 3075 |
| 4 | Tokyo International Airport |  | JP | 2967 |
| 5 | Guaymaral Airport |  | CO | 2747 |
| 6 | Harry Reid International Airport |  | US | 2690 |
| 7 | Zurich Airport |  | CH | 2652 |
| 8 | El Dorado International Airport |  | CO | 2593 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2565 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2494 |
| 11 | La Aurora Airport |  | GT | 2401 |
| 12 | Salt Lake City International Airport |  | US | 2236 |
| 13 | Chicago O'Hare International Airport |  | US | 2211 |
| 14 | Congonhas Airport |  | BR | 2170 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2078 |
| 16 | Capua Airport |  | IT | 1999 |
| 17 | Madrid Barajas International Airport |  | ES | 1987 |
| 18 | Frankfurt am Main International Airport |  | DE | 1964 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1898 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1841 |
| 21 | Malpensa International Airport |  | IT | 1821 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1781 |
| 23 | Charles de Gaulle International Airport |  | FR | 1776 |
| 24 | General Edward Lawrence Logan International Airport |  | US | 1764 |
| 25 | Enrique Olaya Herrera Airport |  | CO | 1694 |
| 26 | Ninoy Aquino International Airport |  | PH | 1677 |
| 27 | Macau International Airport |  | MO | 1672 |
| 28 | Barcelona International Airport |  | ES | 1596 |
| 29 | Charlotte/Douglas International Airport |  | US | 1593 |
| 30 | Kuala Lumpur International Airport |  | MY | 1583 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1555 |
| 32 | Viracopos International Airport |  | BR | 1512 |
| 33 | Seattle-Tacoma International Airport |  | US | 1493 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1469 |
| 35 | Calgary International Airport |  | CA | 1461 |
| 36 | Don Mueang International Airport |  | TH | 1460 |
| 37 | Bengaluru International Airport |  | IN | 1445 |
| 38 | Oslo Gardermoen Airport |  | NO | 1430 |
| 39 | Vancouver International Airport |  | CA | 1421 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1368 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1105 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 941 | 21m | 244 km | 3,962.3 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 676 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 637 | 1h 6m | 770 km | 8,462.1 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 637 | 24m | 225 km | 2,471.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 566 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 415 | 27m | 275 km | 1,966.5 t |
| 8 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 403 | 1h 50m | 1,423 km | 9,890.3 t |
| 9 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 402 | 44m | 555 km | 3,849.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 380 | 44m | 241 km | 1,578.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 373 | 35m | - | - |
| 12 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 354 | 24m | 218 km | 1,333.7 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 353 | 21m | 250 km | 1,524.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 338 | 23m | 55 km | 321.3 t |
| 15 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 333 | 1h 39m | 1,156 km | 6,643.2 t |
| 16 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 324 | 1h 6m | 706 km | 3,944.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 313 | 26m | 215 km | 1,159.2 t |
| 18 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 307 | 19m | 99 km | 525.9 t |
| 20 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 303 | 12m | - | - |
| 21 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 297 | 13m | - | - |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 290 | 1h 14m | 961 km | 4,806.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 289 | 19m | 144 km | 718.9 t |
| 25 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 274 | 1h 50m | 1,304 km | 6,164.3 t |
| 26 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 269 | 29m | 304 km | 1,410.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 269 | 15m | 154 km | 712.7 t |
| 28 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 263 | 41m | 535 km | 2,429.0 t |
| 29 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 261 | 31m | 369 km | 1,661.3 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 258 | 28m | 152 km | 674.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| VTKJR | VTK | Cochin International Airport (VOCI) | Pune Airport (VAPO) | 2026-09-10 09:26 UTC | 2026-09-10 10:56 UTC | 1h 30m |
| LNTED | LNT | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-09-10 10:00 UTC | 2026-09-10 10:36 UTC | 35m |
| AAN181 | AAN | Ibiza Airport (LEIB) | Stuttgart Airport (EDDS) | 2026-09-10 08:48 UTC | 2026-09-10 10:36 UTC | 1h 47m |
| DEOFF | DEO | Stade Airport (EDHS) | Stade Airport (EDHS) | 2026-09-10 10:23 UTC | 2026-09-10 10:35 UTC | 12m |
| EFC54E | EFC | Al Maktoum International Airport (OMDW) | Al Ain International Airport (OMAL) | 2026-09-10 09:49 UTC | 2026-09-10 10:31 UTC | 42m |
| HBLVC | HBL | Memmingen Allgau Airport (EDJA) | Mengen-Hohentengen Airport (EDTM) | 2026-09-10 10:03 UTC | 2026-09-10 10:27 UTC | 24m |
| EXS1DC | EXS | East Midlands Airport (EGNX) | Son Bonet Airport (LESB) | 2026-09-10 08:29 UTC | 2026-09-10 10:24 UTC | 1h 55m |
| IFJ15C | IFJ | Viseu Airport (LPVZ) | Coimbra Airfield (LPCO) | 2026-09-10 10:00 UTC | 2026-09-10 10:22 UTC | 22m |
| RYR2LC | Ryanair | Barcelona International Airport (LEBL) | Taza Airport (GMFZ) | 2026-09-10 08:44 UTC | 2026-09-10 10:00 UTC | 1h 15m |
| ANE66RP | ANE | Menorca Airport (LEMH) | Palma De Mallorca Airport (LEPA) | 2026-09-10 09:33 UTC | 2026-09-10 09:59 UTC | 25m |
| AFL731 | AFL | Antalya International Airport (LTAI) | Astrakhan Airport (URWA) | 2026-09-10 07:29 UTC | 2026-09-10 09:57 UTC | 2h 27m |
| VOE8YV | VOE | Toulouse-Blagnac Airport (LFBO) | Caen-Carpiquet Airport (LFRK) | 2026-09-10 08:49 UTC | 2026-09-10 09:55 UTC | 1h 5m |
| JST739 | JST | Melbourne International Airport (YMML) | Devonport Airport (YDPO) | 2026-09-10 09:23 UTC | 2026-09-10 09:54 UTC | 30m |
| APJ117 | APJ | Kansai International Airport (RJBB) | New Chitose Airport (RJCC) | 2026-09-10 08:19 UTC | 2026-09-10 09:53 UTC | 1h 33m |
| LCO3604 | LCO | Miami International Airport (KMIA) | Brussels Airport (EBBR) | 2026-09-10 01:13 UTC | 2026-09-10 09:53 UTC | 8h 39m |
| AFR11ZB | Air France | Charles de Gaulle International Airport (LFPG) | Stockholm-Arlanda Airport (ESSA) | 2026-09-10 07:33 UTC | 2026-09-10 09:51 UTC | 2h 18m |
| ANA407 | All Nippon Airways | Tokyo International Airport (RJTT) | Yamagata Airport (RJSC) | 2026-09-10 09:21 UTC | 2026-09-10 09:51 UTC | 29m |
| XUM2597 | XUM | Gimpo International Airport (RKSS) | Sacheon Air Base (RKPS) | 2026-09-10 09:07 UTC | 2026-09-10 09:51 UTC | 43m |
| UBG537 | UBG | VGZR (VGZR) | Shillong Airport (VEBI) | 2026-09-10 09:35 UTC | 2026-09-10 09:49 UTC | 14m |
| SAZ72 | SAZ | Lamezia Terme Airport (LICA) | Taranto / Grottaglie Airport (LIBG) | 2026-09-10 09:25 UTC | 2026-09-10 09:49 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
