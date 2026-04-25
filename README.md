# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_17:29:36_UTC-green)

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

**Latest saved flight:** 2026-04-25 17:29:36 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-25 17:29:36 UTC

- **53,832** saved flights
- **21,368** unique routes
- **123** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **53,832** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **645,458.1 tonnes** estimated CO2 emissions
- **37,417,859 km** total distance flown
- **837 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2271 |
| 2 | SkyWest Airlines | 2016 |
| 3 | IndiGo | 1225 |
| 4 | EJA | 954 |
| 5 | American Airlines | 860 |
| 6 | Southwest Airlines | 760 |
| 7 | ENY | 677 |
| 8 | Lufthansa | 636 |
| 9 | Vueling | 545 |
| 10 | AXM | 522 |
| 11 | LATAM Airlines | 520 |
| 12 | All Nippon Airways | 478 |
| 13 | AZU | 456 |
| 14 | WIF | 448 |
| 15 | Delta Air Lines | 444 |
| 16 | QLK | 416 |
| 17 | Swiss International | 416 |
| 18 | LXJ | 393 |
| 19 | AEE | 361 |
| 20 | Alaska Airlines | 354 |
| 21 | easyJet | 344 |
| 22 | EJU | 342 |
| 23 | VIV | 342 |
| 24 | Japan Airlines | 313 |
| 25 | Air France | 312 |
| 26 | AXB | 285 |
| 27 | Cathay Pacific | 285 |
| 28 | AIQ | 277 |
| 29 | GLO | 274 |
| 30 | JetBlue | 274 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 42792 |
| 2 | 🇪🇸 ES | 3913 |
| 3 | 🇮🇳 IN | 3855 |
| 4 | 🇦🇺 AU | 3622 |
| 5 | 🇧🇷 BR | 3125 |
| 6 | 🇮🇹 IT | 2911 |
| 7 | 🇯🇵 JP | 2889 |
| 8 | 🇩🇪 DE | 2886 |
| 9 | 🇨🇦 CA | 2668 |
| 10 | 🇨🇴 CO | 2457 |
| 11 | 🇬🇧 GB | 2258 |
| 12 | 🇫🇷 FR | 2108 |
| 13 | 🇲🇽 MX | 1667 |
| 14 | 🇬🇷 GR | 1616 |
| 15 | 🇨🇭 CH | 1529 |
| 16 | 🇳🇴 NO | 1453 |
| 17 | 🇲🇾 MY | 1269 |
| 18 | 🇿🇦 ZA | 1117 |
| 19 | 🇳🇿 NZ | 1017 |
| 20 | 🇹🇭 TH | 975 |
| 21 | 🇹🇷 TR | 970 |
| 22 | 🇵🇭 PH | 918 |
| 23 | 🇰🇷 KR | 873 |
| 24 | 🇵🇱 PL | 866 |
| 25 | 🇬🇹 GT | 824 |
| 26 | 🇲🇦 MA | 674 |
| 27 | 🇲🇪 ME | 578 |
| 28 | 🇳🇱 NL | 548 |
| 29 | 🇲🇴 MO | 531 |
| 30 | 🇧🇸 BS | 469 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1224 |
| 2 | Tokyo International Airport |  | JP | 980 |
| 3 | Denver International Airport |  | US | 884 |
| 4 | El Dorado International Airport |  | CO | 833 |
| 5 | Indira Gandhi International Airport |  | IN | 819 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 798 |
| 7 | Guaymaral Airport |  | CO | 738 |
| 8 | Harry Reid International Airport |  | US | 690 |
| 9 | Zurich Airport |  | CH | 640 |
| 10 | Frankfurt am Main International Airport |  | DE | 620 |
| 11 | La Aurora Airport |  | GT | 617 |
| 12 | Macau International Airport |  | MO | 531 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 528 |
| 14 | Chicago O'Hare International Airport |  | US | 526 |
| 15 | Hartsfield/Jackson Atlanta International Airport |  | US | 508 |
| 16 | Kuala Lumpur International Airport |  | MY | 505 |
| 17 | Madrid Barajas International Airport |  | ES | 500 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 471 |
| 19 | Bengaluru International Airport |  | IN | 459 |
| 20 | Malpensa International Airport |  | IT | 456 |
| 21 | Congonhas Airport |  | BR | 451 |
| 22 | Charlotte/Douglas International Airport |  | US | 438 |
| 23 | Tenerife Norte Airport |  | ES | 430 |
| 24 | Ninoy Aquino International Airport |  | PH | 424 |
| 25 | Charles de Gaulle International Airport |  | FR | 409 |
| 26 | Salt Lake City International Airport |  | US | 403 |
| 27 | Atizapan De Zaragoza Airport |  | MX | 400 |
| 28 | Capua Airport |  | IT | 393 |
| 29 | Daniel K Inouye International Airport |  | US | 389 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 385 |
| 31 | Vitoria/Foronda Airport |  | ES | 370 |
| 32 | Barcelona International Airport |  | ES | 366 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 358 |
| 34 | Reno/Tahoe International Airport |  | US | 358 |
| 35 | John Paul II International Airport Kraków-Balice Airport |  | PL | 357 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 357 |
| 37 | O. R. Tambo International Airport |  | ZA | 351 |
| 38 | Don Mueang International Airport |  | TH | 332 |
| 39 | Calgary International Airport |  | CA | 320 |
| 40 | Viracopos International Airport |  | BR | 317 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 299 | 27m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 246 | 1h 7m | 706 km | 2,995.1 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 200 | 14m | 114 km | 392.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 175 | 24m | 225 km | 678.9 t |
| 5 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 164 | 21m | 244 km | 690.6 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 156 | 28m | 304 km | 817.8 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 153 | 1h 27m | 910 km | 2,400.9 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 139 | 19m | 165 km | 395.4 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 133 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 130 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 125 | 26m | 275 km | 592.3 t |
| 12 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 107 | 44m | 452 km | 833.9 t |
| 13 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 104 | 54m | 546 km | 979.2 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 98 | 1h 11m | 770 km | 1,301.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 98 | 20m | 99 km | 167.9 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 92 | 31m | 369 km | 585.6 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 89 | 27m | 215 km | 329.6 t |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 89 | 20m | 250 km | 384.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 84 | 20m | 147 km | 212.6 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 84 | 52m | 556 km | 805.2 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 82 | 27m | 152 km | 214.3 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 77 | 1h 1m | 695 km | 923.0 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 76 | 1h 41m | 1,156 km | 1,516.2 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 75 | 13m | 99 km | 128.6 t |
| 25 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 72 | 23m | 55 km | 68.4 t |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 71 | 58m | 493 km | 604.0 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 71 | 13m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 70 | 1h 19m | 961 km | 1,160.3 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 70 | 1h 53m | 1,304 km | 1,574.8 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 69 | 12m | 15 km | 18.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N506DS |  | Sacramento Mather Airport (KMHR) | Byron Airport (KC83) | 2026-04-25 16:48 UTC | 2026-04-25 17:29 UTC | 40m |
| SWA2057 | Southwest Airlines | Ontario International Airport (KONT) | San Martin Airport (KE16) | 2026-04-25 16:34 UTC | 2026-04-25 17:29 UTC | 54m |
| CPA048 | Cathay Pacific | VGZR (VGZR) | Macau International Airport (VMMC) | 2026-04-25 12:16 UTC | 2026-04-25 17:27 UTC | 5h 10m |
| ETH3718 | Ethiopian Airlines | Liege Airport (EBLG) | Zhuhai Airport (ZGSD) | 2026-04-25 06:53 UTC | 2026-04-25 17:23 UTC | 10h 30m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-25 17:07 UTC | 2026-04-25 17:22 UTC | 14m |
| VAR485 | VAR | Gene Wash Reservoir Airport (5CL7) | Lake Havasu City Airport (KHII) | 2026-04-25 17:05 UTC | 2026-04-25 17:17 UTC | 11m |
| MFX7484 | MFX | Geneva Cointrin International Airport (LSGG) | Zhuhai Airport (ZGSD) | 2026-04-24 16:41 UTC | 2026-04-25 17:15 UTC | 24h 34m |
| N1189W |  | Camarillo Airport (KCMA) | Santa Maria Pub/Capt G Allan Hancock Field (KSMX) | 2026-04-25 16:33 UTC | 2026-04-25 17:15 UTC | 42m |
| N9017T |  | Minden-Tahoe Airport (KMEV) | Rosaschi Air Park (KN59) | 2026-04-25 17:00 UTC | 2026-04-25 17:14 UTC | 13m |
| JRT50 | JRT | John C Tune Airport (KJWN) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-04-25 16:29 UTC | 2026-04-25 17:10 UTC | 40m |
| N85M |  | Ciampino Airport (LIRA) | Bangor International Airport (KBGR) | 2026-04-25 10:06 UTC | 2026-04-25 17:07 UTC | 7h 1m |
| N75733 |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-04-25 15:56 UTC | 2026-04-25 17:06 UTC | 1h 9m |
| N205BT |  | Redding Regional Airport (KRDD) | Redding Regional Airport (KRDD) | 2026-04-25 16:30 UTC | 2026-04-25 17:04 UTC | 34m |
| N745AK |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-04-25 16:27 UTC | 2026-04-25 17:03 UTC | 36m |
| N707KW |  | Knox County Regional Airport (KRKD) | Matinicus Island Airport (35ME) | 2026-04-25 16:58 UTC | 2026-04-25 17:02 UTC | 4m |
| N100HH |  | Morris Municipal/James R Washburn Field (KC09) | Morris Municipal/James R Washburn Field (KC09) | 2026-04-25 16:58 UTC | 2026-04-25 17:02 UTC | 3m |
| N7261Y |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-04-25 15:51 UTC | 2026-04-25 17:01 UTC | 1h 10m |
| N117JP |  | City Of Colorado Springs Municipal Airport (KCOS) | City Of Las Animas - Bent County Airport (K7V9) | 2026-04-25 16:24 UTC | 2026-04-25 16:59 UTC | 35m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-04-25 16:39 UTC | 2026-04-25 16:54 UTC | 14m |
| FGHKJ | FGH | Chartres Champhol Airport (LFOR) | Etampes Mondesir Airport (LFOX) | 2026-04-25 16:37 UTC | 2026-04-25 16:54 UTC | 16m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
