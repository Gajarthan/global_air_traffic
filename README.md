# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_01:23:50_UTC-green)

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

**Latest saved flight:** 2026-09-25 01:23:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-25 01:23:50 UTC

- **268,854** saved flights
- **78,891** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **268,854** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,261,433.2 tonnes** estimated CO2 emissions
- **189,068,590 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10592 |
| 2 | SkyWest Airlines | 9356 |
| 3 | EJA | 5252 |
| 4 | IndiGo | 4499 |
| 5 | American Airlines | 4181 |
| 6 | Southwest Airlines | 3951 |
| 7 | Delta Air Lines | 3345 |
| 8 | ENY | 3159 |
| 9 | LATAM Airlines | 2593 |
| 10 | AZU | 2518 |
| 11 | Vueling | 2243 |
| 12 | WIF | 2186 |
| 13 | LXJ | 2116 |
| 14 | Lufthansa | 2045 |
| 15 | easyJet | 1804 |
| 16 | Swiss International | 1761 |
| 17 | QLK | 1735 |
| 18 | EJU | 1687 |
| 19 | AXM | 1673 |
| 20 | United Airlines | 1648 |
| 21 | Alaska Airlines | 1587 |
| 22 | All Nippon Airways | 1547 |
| 23 | PGT | 1511 |
| 24 | WMT | 1502 |
| 25 | GLO | 1497 |
| 26 | Air France | 1477 |
| 27 | VIV | 1468 |
| 28 | Wizz Air | 1458 |
| 29 | CXK | 1318 |
| 30 | AEE | 1292 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 223846 |
| 2 | 🇪🇸 ES | 16848 |
| 3 | 🇧🇷 BR | 15715 |
| 4 | 🇦🇺 AU | 15475 |
| 5 | 🇨🇦 CA | 15001 |
| 6 | 🇮🇹 IT | 14557 |
| 7 | 🇮🇳 IN | 14232 |
| 8 | 🇩🇪 DE | 12901 |
| 9 | 🇬🇧 GB | 12443 |
| 10 | 🇨🇴 CO | 12309 |
| 11 | 🇫🇷 FR | 10691 |
| 12 | 🇯🇵 JP | 10336 |
| 13 | 🇹🇷 TR | 8136 |
| 14 | 🇬🇷 GR | 7769 |
| 15 | 🇲🇽 MX | 7413 |
| 16 | 🇨🇭 CH | 7144 |
| 17 | 🇳🇴 NO | 6651 |
| 18 | 🇹🇭 TH | 4807 |
| 19 | 🇲🇾 MY | 4518 |
| 20 | 🇿🇦 ZA | 4490 |
| 21 | 🇵🇱 PL | 4402 |
| 22 | 🇳🇿 NZ | 3763 |
| 23 | 🇵🇭 PH | 3560 |
| 24 | 🇬🇹 GT | 3403 |
| 25 | 🇭🇷 HR | 3060 |
| 26 | 🇰🇷 KR | 3041 |
| 27 | 🇲🇦 MA | 2681 |
| 28 | 🇲🇪 ME | 2517 |
| 29 | 🇳🇱 NL | 2405 |
| 30 | 🇮🇩 ID | 2239 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5478 |
| 2 | Denver International Airport |  | US | 4372 |
| 3 | Indira Gandhi International Airport |  | IN | 3219 |
| 4 | Tokyo International Airport |  | JP | 3093 |
| 5 | El Dorado International Airport |  | CO | 2912 |
| 6 | Harry Reid International Airport |  | US | 2881 |
| 7 | Guaymaral Airport |  | CO | 2811 |
| 8 | Zurich Airport |  | CH | 2784 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2704 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2590 |
| 11 | La Aurora Airport |  | GT | 2586 |
| 12 | Salt Lake City International Airport |  | US | 2368 |
| 13 | Chicago O'Hare International Airport |  | US | 2300 |
| 14 | Congonhas Airport |  | BR | 2288 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2202 |
| 16 | Capua Airport |  | IT | 2093 |
| 17 | Madrid Barajas International Airport |  | ES | 2069 |
| 18 | Frankfurt am Main International Airport |  | DE | 2038 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2035 |
| 20 | Malpensa International Airport |  | IT | 1926 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1918 |
| 22 | Charles de Gaulle International Airport |  | FR | 1908 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1883 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1881 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1818 |
| 26 | Macau International Airport |  | MO | 1786 |
| 27 | Ninoy Aquino International Airport |  | PH | 1747 |
| 28 | Charlotte/Douglas International Airport |  | US | 1680 |
| 29 | Barcelona International Airport |  | ES | 1672 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1665 |
| 31 | Viracopos International Airport |  | BR | 1625 |
| 32 | Kuala Lumpur International Airport |  | MY | 1617 |
| 33 | Seattle-Tacoma International Airport |  | US | 1575 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1572 |
| 35 | Calgary International Airport |  | CA | 1532 |
| 36 | Don Mueang International Airport |  | TH | 1523 |
| 37 | Bengaluru International Airport |  | IN | 1514 |
| 38 | Oslo Gardermoen Airport |  | NO | 1509 |
| 39 | Vancouver International Airport |  | CA | 1507 |
| 40 | Antalya International Airport |  | TR | 1431 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1121 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1008 | 21m | 244 km | 4,244.4 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 741 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 677 | 1h 6m | 770 km | 8,993.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 670 | 24m | 225 km | 2,599.3 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 598 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 443 | 44m | 555 km | 4,241.9 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 431 | 27m | 275 km | 2,042.3 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 425 | 1h 50m | 1,423 km | 10,430.2 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 410 | 44m | 241 km | 1,703.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 384 | 24m | 218 km | 1,446.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 376 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 364 | 21m | 250 km | 1,572.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 360 | 23m | 55 km | 342.2 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 343 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 342 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 340 | 1h 6m | 706 km | 4,139.5 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 338 | 19m | 99 km | 579.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 335 | 26m | 215 km | 1,240.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 335 | 1h 39m | 1,156 km | 6,683.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 313 | 19m | 144 km | 778.6 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 304 | 1h 14m | 961 km | 5,039.0 t |
| 24 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 293 | 42m | 535 km | 2,706.0 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 289 | 1h 50m | 1,304 km | 6,501.8 t |
| 27 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 287 | 18m | 14 km | 71.8 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 284 | 28m | 152 km | 742.2 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 272 | 15m | 154 km | 720.7 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1088R |  | Arlington Municipal Airport (KAWO) | Portland-Hillsboro Airport (KHIO) | 2026-09-25 00:43 UTC | 2026-09-25 01:23 UTC | 39m |
| HM5 |  | Melbourne Essendon Airport (YMEN) | Melbourne Essendon Airport (YMEN) | 2026-09-25 00:52 UTC | 2026-09-25 01:23 UTC | 31m |
| NZJ | NZJ | RAAF Williams Point Cook Base (YMPC) | Melbourne Essendon Airport (YMEN) | 2026-09-25 01:02 UTC | 2026-09-25 01:22 UTC | 19m |
| N54983 |  | Merrill Field (PAMR) | Talkeetna Airport (PATK) | 2026-09-25 00:34 UTC | 2026-09-25 01:17 UTC | 42m |
| N124WE |  | Modesto City-County-Harry Sham Field (KMOD) | Sacramento Executive Airport (KSAC) | 2026-09-25 00:38 UTC | 2026-09-25 01:15 UTC | 36m |
| BULETXX | BUL | North Island Nas (Halsey Field) Airport (KNZY) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-09-25 00:53 UTC | 2026-09-25 01:15 UTC | 21m |
| N1154Z |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-09-25 00:51 UTC | 2026-09-25 01:12 UTC | 21m |
| FAC4003 | FAC | Madrid Air Base (SKMA) | Madrid Air Base (SKMA) | 2026-09-25 00:12 UTC | 2026-09-25 01:11 UTC | 59m |
| KRR | KRR | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-09-25 00:51 UTC | 2026-09-25 01:06 UTC | 14m |
| N814SS |  | Trading Bay Production Airport (5AK0) | Nikolai Creek Airport (9AK3) | 2026-09-25 00:57 UTC | 2026-09-25 01:05 UTC | 8m |
| N989PA |  | KU77 (KU77) | Provo Municipal Airport (KPVU) | 2026-09-25 00:49 UTC | 2026-09-25 01:00 UTC | 11m |
| N849AA |  | Antiquers Aerodrome (FD08) | Miami Executive Airport (KTMB) | 2026-09-25 00:04 UTC | 2026-09-25 00:58 UTC | 53m |
| N356BG |  | Wood County Regional Airport (K1G0) | Wood County Regional Airport (K1G0) | 2026-09-25 00:08 UTC | 2026-09-25 00:58 UTC | 50m |
| N230AM |  | Desert Wings Sky Ranch Airport (04CL) | Ramona Airport (KRNM) | 2026-09-25 00:41 UTC | 2026-09-25 00:55 UTC | 13m |
| CGSSC | CGS | Nanaimo Airport (CYCD) | Vancouver International Airport (CYVR) | 2026-09-25 00:33 UTC | 2026-09-25 00:49 UTC | 15m |
| PXT578 | PXT | Oakland San Francisco Bay Airport (KOAK) | Truckee-Tahoe Airport (KTRK) | 2026-09-25 00:24 UTC | 2026-09-25 00:49 UTC | 24m |
| FRG176 | FRG | Trenton Mercer Airport (KTTN) | Lincoln Airport (KLNK) | 2026-09-24 21:31 UTC | 2026-09-25 00:45 UTC | 3h 13m |
| N302TP |  | Tulsa International Airport (KTUL) | Tulsa International Airport (KTUL) | 2026-09-25 00:21 UTC | 2026-09-25 00:43 UTC | 22m |
| PCM7703 | PCM | Visalia Municipal Airport (KVIS) | Oakland San Francisco Bay Airport (KOAK) | 2026-09-24 23:43 UTC | 2026-09-25 00:43 UTC | 59m |
| N434CF |  | Jackpot/Hayden Field (K06U) | KD68 (KD68) | 2026-09-24 23:03 UTC | 2026-09-25 00:41 UTC | 1h 37m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
