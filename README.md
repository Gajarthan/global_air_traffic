# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_08:47:33_UTC-green)

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

**Latest saved flight:** 2026-04-17 08:47:33 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-17 08:47:33 UTC

- **38,657** saved flights
- **16,633** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **38,657** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **467,101.7 tonnes** estimated CO2 emissions
- **27,078,362 km** total distance flown
- **840 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1618 |
| 2 | SkyWest Airlines | 1511 |
| 3 | IndiGo | 953 |
| 4 | EJA | 667 |
| 5 | American Airlines | 646 |
| 6 | Southwest Airlines | 534 |
| 7 | ENY | 500 |
| 8 | AXM | 408 |
| 9 | Vueling | 390 |
| 10 | LATAM Airlines | 386 |
| 11 | Lufthansa | 385 |
| 12 | All Nippon Airways | 344 |
| 13 | AZU | 343 |
| 14 | Delta Air Lines | 326 |
| 15 | QLK | 326 |
| 16 | LXJ | 309 |
| 17 | WIF | 294 |
| 18 | Swiss International | 290 |
| 19 | Alaska Airlines | 258 |
| 20 | AEE | 257 |
| 21 | easyJet | 251 |
| 22 | EJU | 250 |
| 23 | VIV | 245 |
| 24 | Japan Airlines | 235 |
| 25 | Air France | 215 |
| 26 | EDV | 212 |
| 27 | United Airlines | 211 |
| 28 | AIQ | 200 |
| 29 | GLO | 200 |
| 30 | JetBlue | 199 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 30447 |
| 2 | 🇮🇳 IN | 2919 |
| 3 | 🇪🇸 ES | 2868 |
| 4 | 🇦🇺 AU | 2773 |
| 5 | 🇧🇷 BR | 2263 |
| 6 | 🇯🇵 JP | 2098 |
| 7 | 🇮🇹 IT | 2026 |
| 8 | 🇩🇪 DE | 1960 |
| 9 | 🇨🇦 CA | 1902 |
| 10 | 🇨🇴 CO | 1899 |
| 11 | 🇬🇧 GB | 1581 |
| 12 | 🇫🇷 FR | 1454 |
| 13 | 🇲🇽 MX | 1216 |
| 14 | 🇬🇷 GR | 1161 |
| 15 | 🇨🇭 CH | 1053 |
| 16 | 🇲🇾 MY | 985 |
| 17 | 🇳🇴 NO | 940 |
| 18 | 🇳🇿 NZ | 809 |
| 19 | 🇿🇦 ZA | 799 |
| 20 | 🇵🇭 PH | 718 |
| 21 | 🇹🇭 TH | 710 |
| 22 | 🇹🇷 TR | 688 |
| 23 | 🇬🇹 GT | 654 |
| 24 | 🇰🇷 KR | 636 |
| 25 | 🇵🇱 PL | 601 |
| 26 | 🇲🇦 MA | 480 |
| 27 | 🇳🇱 NL | 389 |
| 28 | 🇲🇪 ME | 381 |
| 29 | 🇧🇸 BS | 373 |
| 30 | 🇮🇩 ID | 361 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 902 |
| 2 | Tokyo International Airport |  | JP | 715 |
| 3 | El Dorado International Airport |  | CO | 670 |
| 4 | Denver International Airport |  | US | 648 |
| 5 | Indira Gandhi International Airport |  | IN | 631 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 574 |
| 7 | Harry Reid International Airport |  | US | 507 |
| 8 | Guaymaral Airport |  | CO | 494 |
| 9 | La Aurora Airport |  | GT | 481 |
| 10 | Zurich Airport |  | CH | 466 |
| 11 | Kuala Lumpur International Airport |  | MY | 386 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 383 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 380 |
| 14 | Sydney Kingsford Smith International Airport |  | AU | 378 |
| 15 | Chicago O'Hare International Airport |  | US | 373 |
| 16 | Macau International Airport |  | MO | 355 |
| 17 | Madrid Barajas International Airport |  | ES | 352 |
| 18 | Frankfurt am Main International Airport |  | DE | 347 |
| 19 | Charlotte/Douglas International Airport |  | US | 343 |
| 20 | Tenerife Norte Airport |  | ES | 343 |
| 21 | Bengaluru International Airport |  | IN | 338 |
| 22 | Congonhas Airport |  | BR | 334 |
| 23 | Ninoy Aquino International Airport |  | PH | 333 |
| 24 | Malpensa International Airport |  | IT | 312 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 301 |
| 26 | Salt Lake City International Airport |  | US | 293 |
| 27 | Daniel K Inouye International Airport |  | US | 287 |
| 28 | Charles de Gaulle International Airport |  | FR | 282 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 277 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 271 |
| 31 | Vitoria/Foronda Airport |  | ES | 264 |
| 32 | Capua Airport |  | IT | 262 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 258 |
| 34 | Reno/Tahoe International Airport |  | US | 257 |
| 35 | O. R. Tambo International Airport |  | ZA | 256 |
| 36 | General Edward Lawrence Logan International Airport |  | US | 252 |
| 37 | Barcelona International Airport |  | ES | 250 |
| 38 | Don Mueang International Airport |  | TH | 238 |
| 39 | Viracopos International Airport |  | BR | 236 |
| 40 | Seattle-Tacoma International Airport |  | US | 233 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 197 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 180 | 1h 8m | 706 km | 2,191.5 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 157 | 14m | 114 km | 307.9 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 141 | 24m | 225 km | 547.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 111 | 1h 27m | 910 km | 1,741.8 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 102 | 19m | 165 km | 290.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 98 | 31m | - | - |
| 9 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 97 | 21m | 244 km | 408.4 t |
| 10 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 95 | 9m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 89 | 26m | 275 km | 421.7 t |
| 12 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 86 | 54m | 546 km | 809.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 82 | 21m | 99 km | 140.5 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 78 | 1h 11m | 770 km | 1,036.2 t |
| 15 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 75 | 45m | 452 km | 584.5 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 71 | 31m | 369 km | 451.9 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 62 | 20m | 147 km | 156.9 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 61 | 52m | 556 km | 584.7 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 61 | 20m | 250 km | 263.5 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 59 | 1h 41m | 1,423 km | 1,448.0 t |
| 23 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 59 | 13m | 99 km | 101.2 t |
| 24 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 25 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 57 | 26m | 215 km | 211.1 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 56 | 16m | 162 km | 157.0 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 55 | 1h 53m | 1,304 km | 1,237.4 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 54 | 13m | - | - |
| 30 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CJT570 | CJT | Winnipeg James Armstrong Richardson International Airport (CYWG) | Montréal (Mirabel) Airport (CYMX) | 2026-04-17 06:37 UTC | 2026-04-17 08:47 UTC | 2h 10m |
| HSOMR1 | HSO | Emden Airport (EDWE) | Norderney Airport (EDWY) | 2026-04-17 08:25 UTC | 2026-04-17 08:46 UTC | 21m |
| AIQ182 | AIQ | Don Mueang International Airport (VTBD) | Langtang Airport (VNLT) | 2026-04-17 05:15 UTC | 2026-04-17 08:41 UTC | 3h 26m |
| RSD932 | RSD | Sheremetyevo International Airport (UUEE) | Sheremetyevo International Airport (UUEE) | 2026-04-17 07:47 UTC | 2026-04-17 08:27 UTC | 40m |
| EW585SL |  | Borovaya Airfield (UMMB) | Borovaya Airfield (UMMB) | 2026-04-17 08:19 UTC | 2026-04-17 08:25 UTC | 6m |
| SFJ27 | SFJ | Tokyo International Airport (RJTT) | Kansai International Airport (RJBB) | 2026-04-17 07:41 UTC | 2026-04-17 08:23 UTC | 41m |
| PHSVD | PHS | Eelde Airport (EHGG) | Eelde Airport (EHGG) | 2026-04-17 07:48 UTC | 2026-04-17 08:21 UTC | 33m |
| FJO71P | FJO | Linate Airport (LIML) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-17 06:17 UTC | 2026-04-17 08:20 UTC | 2h 2m |
| ITY720 | ITY | Leonardo Da Vinci (Fiumicino) International Airport (LIRF) | Eleftherios Venizelos International Airport (LGAV) | 2026-04-17 06:33 UTC | 2026-04-17 08:15 UTC | 1h 42m |
| ESPKY | ESP | Tallinn Airport (EETN) | Johvi Airfield (EEJI) | 2026-04-17 07:41 UTC | 2026-04-17 08:13 UTC | 31m |
| DFC3TB | DFC | Frankfurt am Main International Airport (EDDF) | Glasgow International Airport (EGPF) | 2026-04-17 06:24 UTC | 2026-04-17 08:10 UTC | 1h 45m |
| AFL1044 | AFL | Sheremetyevo International Airport (UUEE) | Pushkin Airport (ULLP) | 2026-04-16 06:46 UTC | 2026-04-17 08:08 UTC | 25h 22m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-04-17 07:54 UTC | 2026-04-17 08:07 UTC | 13m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-04-17 08:00 UTC | 2026-04-17 08:07 UTC | 7m |
| IGO105E | IndiGo | Bengaluru International Airport (VOBL) | Burhar Airport (VA1O) | 2026-04-17 06:19 UTC | 2026-04-17 08:07 UTC | 1h 47m |
| AXB6614 | AXB | Chaudhary Charan Singh International Airport (VILK) | Dubai International Airport (OMDB) | 2026-04-17 03:43 UTC | 2026-04-17 08:06 UTC | 4h 23m |
| IGO936J | IndiGo | Coimbatore International Airport (VOCB) | Burhar Airport (VA1O) | 2026-04-17 02:37 UTC | 2026-04-17 08:03 UTC | 5h 26m |
| AIC217 | Air India | Indira Gandhi International Airport (VIDP) | Langtang Airport (VNLT) | 2026-04-17 06:54 UTC | 2026-04-17 08:02 UTC | 1h 8m |
| AWA415 | AWA | VGZR (VGZR) | Lengpui Airport (VELP) | 2026-04-17 07:34 UTC | 2026-04-17 07:59 UTC | 24m |
| SWR1FP | Swiss International | Zurich Airport (LSZH) | Stuttgart Airport (EDDS) | 2026-04-17 07:33 UTC | 2026-04-17 07:58 UTC | 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
