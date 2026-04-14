# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_07:03:33_UTC-green)

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

**Latest saved flight:** 2026-04-14 07:03:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-14 07:03:33 UTC

- **33,551** saved flights
- **14,949** unique routes
- **120** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **33,551** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **412,588.6 tonnes** estimated CO2 emissions
- **23,918,179 km** total distance flown
- **850 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1421 |
| 2 | SkyWest Airlines | 1354 |
| 3 | IndiGo | 844 |
| 4 | American Airlines | 585 |
| 5 | EJA | 577 |
| 6 | Southwest Airlines | 487 |
| 7 | ENY | 449 |
| 8 | Lufthansa | 377 |
| 9 | AXM | 353 |
| 10 | Vueling | 341 |
| 11 | LATAM Airlines | 337 |
| 12 | All Nippon Airways | 306 |
| 13 | AZU | 297 |
| 14 | QLK | 287 |
| 15 | Delta Air Lines | 285 |
| 16 | LXJ | 271 |
| 17 | Swiss International | 253 |
| 18 | WIF | 231 |
| 19 | Alaska Airlines | 228 |
| 20 | easyJet | 222 |
| 21 | EJU | 221 |
| 22 | AEE | 218 |
| 23 | VIV | 218 |
| 24 | Japan Airlines | 212 |
| 25 | EDV | 195 |
| 26 | United Airlines | 193 |
| 27 | GLO | 183 |
| 28 | Avianca | 181 |
| 29 | JetBlue | 180 |
| 30 | Air France | 178 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 26428 |
| 2 | 🇮🇳 IN | 2585 |
| 3 | 🇪🇸 ES | 2506 |
| 4 | 🇦🇺 AU | 2375 |
| 5 | 🇧🇷 BR | 1973 |
| 6 | 🇯🇵 JP | 1843 |
| 7 | 🇮🇹 IT | 1783 |
| 8 | 🇩🇪 DE | 1676 |
| 9 | 🇨🇴 CO | 1675 |
| 10 | 🇨🇦 CA | 1646 |
| 11 | 🇬🇧 GB | 1360 |
| 12 | 🇫🇷 FR | 1226 |
| 13 | 🇲🇽 MX | 1075 |
| 14 | 🇬🇷 GR | 972 |
| 15 | 🇨🇭 CH | 923 |
| 16 | 🇲🇾 MY | 851 |
| 17 | 🇳🇴 NO | 760 |
| 18 | 🇳🇿 NZ | 722 |
| 19 | 🇿🇦 ZA | 688 |
| 20 | 🇵🇭 PH | 642 |
| 21 | 🇹🇷 TR | 623 |
| 22 | 🇹🇭 TH | 607 |
| 23 | 🇬🇹 GT | 601 |
| 24 | 🇰🇷 KR | 575 |
| 25 | 🇵🇱 PL | 519 |
| 26 | 🇲🇦 MA | 426 |
| 27 | 🇧🇸 BS | 340 |
| 28 | 🇲🇪 ME | 331 |
| 29 | 🇳🇱 NL | 321 |
| 30 | 🇮🇩 ID | 321 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 803 |
| 2 | Tokyo International Airport |  | JP | 626 |
| 3 | El Dorado International Airport |  | CO | 599 |
| 4 | Denver International Airport |  | US | 570 |
| 5 | Indira Gandhi International Airport |  | IN | 550 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 475 |
| 7 | Harry Reid International Airport |  | US | 442 |
| 8 | La Aurora Airport |  | GT | 438 |
| 9 | Zurich Airport |  | CH | 414 |
| 10 | Guaymaral Airport |  | CO | 406 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 343 |
| 12 | Chicago O'Hare International Airport |  | US | 343 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 340 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 328 |
| 15 | Frankfurt am Main International Airport |  | DE | 327 |
| 16 | Kuala Lumpur International Airport |  | MY | 327 |
| 17 | Macau International Airport |  | MO | 317 |
| 18 | Charlotte/Douglas International Airport |  | US | 306 |
| 19 | Madrid Barajas International Airport |  | ES | 305 |
| 20 | Bengaluru International Airport |  | IN | 300 |
| 21 | Ninoy Aquino International Airport |  | PH | 296 |
| 22 | Tenerife Norte Airport |  | ES | 294 |
| 23 | Congonhas Airport |  | BR | 293 |
| 24 | Malpensa International Airport |  | IT | 273 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 258 |
| 26 | Daniel K Inouye International Airport |  | US | 258 |
| 27 | Salt Lake City International Airport |  | US | 255 |
| 28 | Reno/Tahoe International Airport |  | US | 243 |
| 29 | Charles de Gaulle International Airport |  | FR | 241 |
| 30 | Capua Airport |  | IT | 239 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 237 |
| 32 | John Paul II International Airport Kraków-Balice Airport |  | PL | 228 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 228 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 228 |
| 35 | O. R. Tambo International Airport |  | ZA | 224 |
| 36 | Vitoria/Foronda Airport |  | ES | 223 |
| 37 | Barcelona International Airport |  | ES | 215 |
| 38 | Miami International Airport |  | US | 214 |
| 39 | Seattle-Tacoma International Airport |  | US | 211 |
| 40 | Viracopos International Airport |  | BR | 206 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 157 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 156 | 1h 8m | 706 km | 1,899.3 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 139 | 14m | 114 km | 272.6 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 125 | 24m | 225 km | 484.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 110 | 28m | 304 km | 576.7 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 97 | 1h 27m | 910 km | 1,522.2 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 86 | 19m | 165 km | 244.6 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 82 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 81 | 9m | - | - |
| 10 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 77 | 54m | 546 km | 725.0 t |
| 11 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 12 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 76 | 21m | 244 km | 320.0 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 73 | 27m | 275 km | 345.9 t |
| 14 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 15 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 71 | 1h 11m | 770 km | 943.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 65 | 31m | 369 km | 413.7 t |
| 18 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 62 | 45m | 452 km | 483.2 t |
| 19 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 20 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 57 | 20m | 250 km | 246.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 53 | 20m | 147 km | 134.1 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 52 | 1h 41m | 1,423 km | 1,276.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 52 | 13m | 99 km | 89.2 t |
| 25 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 49 | 16m | 162 km | 137.4 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 48 | 23m | 252 km | 208.4 t |
| 27 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 48 | 12m | 15 km | 12.7 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 47 | 1h 20m | 961 km | 779.0 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 47 | 1h 53m | 1,304 km | 1,057.4 t |
| 30 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 46 | 14m | 154 km | 121.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XHT | XHT | Rugby Airport (YRUG) | Canberra International Airport (YSCB) | 2026-04-14 06:37 UTC | 2026-04-14 07:03 UTC | 26m |
| DKADV | DKA | Juist Airport (EDWJ) | Juist Airport (EDWJ) | 2026-04-14 06:17 UTC | 2026-04-14 06:41 UTC | 23m |
| WIF64M | WIF | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 2026-04-14 05:52 UTC | 2026-04-14 06:37 UTC | 45m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-14 06:31 UTC | 2026-04-14 06:37 UTC | 6m |
| KRR | KRR | Melbourne Moorabbin Airport (YMMB) | Melbourne Moorabbin Airport (YMMB) | 2026-04-14 05:52 UTC | 2026-04-14 06:37 UTC | 44m |
| CHOP21 | CHO | Newcastle Airport (YWLM) | Newcastle Airport (YWLM) | 2026-04-14 06:18 UTC | 2026-04-14 06:29 UTC | 11m |
| ZSDVT | ZSD | Wonderboom Airport (FAWB) | Dunnottar Airport (FADR) | 2026-04-14 06:09 UTC | 2026-04-14 06:24 UTC | 15m |
| WLBY46 | WLB | RAAF Base Amberley (YAMB) | Dalby Airport (YDAY) | 2026-04-14 06:07 UTC | 2026-04-14 06:24 UTC | 17m |
| TJT31DR | TJT | Toulouse-Blagnac Airport (LFBO) | Rennes-Saint-Jacques Airport (LFRN) | 2026-04-14 05:08 UTC | 2026-04-14 06:24 UTC | 1h 15m |
| RXA6673 | RXA | Sydney Kingsford Smith International Airport (YSSY) | Tumut Airport (YTMU) | 2026-04-14 05:32 UTC | 2026-04-14 06:21 UTC | 48m |
| RYR306H | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Niederrhein Airport (EDLV) | 2026-04-14 05:10 UTC | 2026-04-14 06:20 UTC | 1h 10m |
| WIF3BR | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-04-14 05:49 UTC | 2026-04-14 06:19 UTC | 30m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-04-14 05:38 UTC | 2026-04-14 06:16 UTC | 38m |
| RYR68NZ | Ryanair | Niederrhein Airport (EDLV) | Ampuriabrava Airport (LEAP) | 2026-04-14 04:45 UTC | 2026-04-14 06:14 UTC | 1h 28m |
| QLK1580 | QLK | Sydney Kingsford Smith International Airport (YSSY) | Sunshine Coast Airport (YBMC) | 2026-04-14 04:55 UTC | 2026-04-14 06:13 UTC | 1h 18m |
| IGO5025 | IndiGo | Indira Gandhi International Airport (VIDP) | VIBN (VIBN) | 2026-04-14 05:25 UTC | 2026-04-14 06:11 UTC | 46m |
| DHYAL | DHY | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-04-14 06:04 UTC | 2026-04-14 06:11 UTC | 7m |
| QLK164D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Port Macquarie Airport (YPMQ) | 2026-04-14 05:27 UTC | 2026-04-14 06:11 UTC | 43m |
| VOE3544 | VOE | Asturias Airport (LEAS) | Federico Garcia Lorca Airport (LEGR) | 2026-04-14 05:08 UTC | 2026-04-14 06:10 UTC | 1h 2m |
| CGWRS | CGW | Edmonton International Airport (CYEG) | Viking (South) Airport (CVS2) | 2026-04-14 05:52 UTC | 2026-04-14 06:08 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
