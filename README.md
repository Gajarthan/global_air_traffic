# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_18:33:04_UTC-green)

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

**Latest saved flight:** 2026-05-01 18:33:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-01 18:33:04 UTC

- **62,829** saved flights
- **24,051** unique routes
- **126** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **62,829** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **766,630.9 tonnes** estimated CO2 emissions
- **44,442,372 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 2637 |
| 2 | SkyWest Airlines | 2326 |
| 3 | IndiGo | 1435 |
| 4 | EJA | 1133 |
| 5 | American Airlines | 977 |
| 6 | Southwest Airlines | 889 |
| 7 | Lufthansa | 810 |
| 8 | ENY | 775 |
| 9 | Vueling | 615 |
| 10 | AXM | 609 |
| 11 | LATAM Airlines | 590 |
| 12 | All Nippon Airways | 551 |
| 13 | WIF | 531 |
| 14 | Delta Air Lines | 519 |
| 15 | AZU | 513 |
| 16 | QLK | 498 |
| 17 | Swiss International | 485 |
| 18 | LXJ | 448 |
| 19 | Alaska Airlines | 430 |
| 20 | AEE | 409 |
| 21 | easyJet | 409 |
| 22 | EJU | 403 |
| 23 | VIV | 394 |
| 24 | Cathay Pacific | 380 |
| 25 | Japan Airlines | 365 |
| 26 | Air France | 364 |
| 27 | AXB | 348 |
| 28 | AIQ | 320 |
| 29 | CXK | 314 |
| 30 | GLO | 308 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 49730 |
| 2 | 🇪🇸 ES | 4544 |
| 3 | 🇮🇳 IN | 4528 |
| 4 | 🇦🇺 AU | 4288 |
| 5 | 🇧🇷 BR | 3564 |
| 6 | 🇩🇪 DE | 3506 |
| 7 | 🇮🇹 IT | 3418 |
| 8 | 🇯🇵 JP | 3409 |
| 9 | 🇨🇦 CA | 3090 |
| 10 | 🇬🇧 GB | 2678 |
| 11 | 🇨🇴 CO | 2641 |
| 12 | 🇫🇷 FR | 2479 |
| 13 | 🇲🇽 MX | 1988 |
| 14 | 🇬🇷 GR | 1868 |
| 15 | 🇨🇭 CH | 1758 |
| 16 | 🇳🇴 NO | 1736 |
| 17 | 🇲🇾 MY | 1490 |
| 18 | 🇿🇦 ZA | 1283 |
| 19 | 🇳🇿 NZ | 1181 |
| 20 | 🇹🇭 TH | 1128 |
| 21 | 🇹🇷 TR | 1109 |
| 22 | 🇵🇭 PH | 1063 |
| 23 | 🇵🇱 PL | 1015 |
| 24 | 🇰🇷 KR | 1008 |
| 25 | 🇬🇹 GT | 980 |
| 26 | 🇲🇦 MA | 770 |
| 27 | 🇲🇴 MO | 704 |
| 28 | 🇲🇪 ME | 682 |
| 29 | 🇳🇱 NL | 659 |
| 30 | 🇮🇩 ID | 532 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1387 |
| 2 | Tokyo International Airport |  | JP | 1152 |
| 3 | Denver International Airport |  | US | 1032 |
| 4 | Indira Gandhi International Airport |  | IN | 952 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 912 |
| 6 | El Dorado International Airport |  | CO | 878 |
| 7 | Guaymaral Airport |  | CO | 836 |
| 8 | Frankfurt am Main International Airport |  | DE | 810 |
| 9 | Harry Reid International Airport |  | US | 799 |
| 10 | Zurich Airport |  | CH | 748 |
| 11 | La Aurora Airport |  | GT | 733 |
| 12 | Macau International Airport |  | MO | 704 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 619 |
| 14 | Chicago O'Hare International Airport |  | US | 593 |
| 15 | Madrid Barajas International Airport |  | ES | 590 |
| 16 | Kuala Lumpur International Airport |  | MY | 590 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 573 |
| 18 | Sydney Kingsford Smith International Airport |  | AU | 558 |
| 19 | Bengaluru International Airport |  | IN | 545 |
| 20 | Malpensa International Airport |  | IT | 541 |
| 21 | Congonhas Airport |  | BR | 515 |
| 22 | Charlotte/Douglas International Airport |  | US | 499 |
| 23 | Salt Lake City International Airport |  | US | 492 |
| 24 | Charles de Gaulle International Airport |  | FR | 488 |
| 25 | Tenerife Norte Airport |  | ES | 486 |
| 26 | Ninoy Aquino International Airport |  | PH | 483 |
| 27 | Capua Airport |  | IT | 468 |
| 28 | Daniel K Inouye International Airport |  | US | 465 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 456 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 452 |
| 31 | Barcelona International Airport |  | ES | 423 |
| 32 | Vitoria/Foronda Airport |  | ES | 419 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 416 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 410 |
| 35 | O. R. Tambo International Airport |  | ZA | 405 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 394 |
| 37 | Amsterdam Airport Schiphol |  | NL | 392 |
| 38 | Reno/Tahoe International Airport |  | US | 390 |
| 39 | Don Mueang International Airport |  | TH | 388 |
| 40 | Calgary International Airport |  | CA | 372 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 344 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 255 | 1h 7m | 706 km | 3,104.6 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 211 | 21m | 244 km | 888.5 t |
| 4 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 195 | 24m | 225 km | 756.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 185 | 1h 27m | 910 km | 2,903.1 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 179 | 28m | 304 km | 938.4 t |
| 8 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 156 | 20m | 165 km | 443.7 t |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 156 | 9m | - | - |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 147 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 141 | 26m | 275 km | 668.1 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 134 | 1h 12m | 770 km | 1,780.1 t |
| 13 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 115 | 44m | 452 km | 896.3 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 113 | 21m | 99 km | 193.6 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 106 | 31m | 369 km | 674.7 t |
| 16 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 104 | 20m | 250 km | 449.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 101 | 27m | 152 km | 264.0 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 100 | 27m | 215 km | 370.4 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 95 | 20m | 147 km | 240.4 t |
| 21 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 89 | 52m | 556 km | 853.1 t |
| 22 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 88 | 1h 42m | 1,156 km | 1,755.6 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 87 | 1h 1m | 695 km | 1,042.9 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 85 | 57m | 493 km | 723.2 t |
| 25 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 84 | 14m | 154 km | 222.6 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 84 | 23m | 55 km | 79.8 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 84 | 1h 53m | 1,304 km | 1,889.8 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 83 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 81 | 1h 43m | 1,423 km | 1,987.9 t |
| 30 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 79 | 12m | 99 km | 135.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N92DV |  | Vance Brand Airport (KLMO) | Vance Brand Airport (KLMO) | 2026-05-01 17:22 UTC | 2026-05-01 18:33 UTC | 1h 10m |
| N890HN |  | Coal Field (64KY) | Louisville Muhammad Ali International Airport (KSDF) | 2026-05-01 18:06 UTC | 2026-05-01 18:28 UTC | 22m |
| N275AA |  | Kissimmee Gateway Airport (KISM) | Lake Wales Municipal Airport (KX07) | 2026-05-01 17:56 UTC | 2026-05-01 18:26 UTC | 29m |
| BOX556 | BOX | Bengaluru International Airport (VOBL) | Zhuhai Airport (ZGSD) | 2026-05-01 13:52 UTC | 2026-05-01 18:26 UTC | 4h 34m |
| N967MS |  | San Gabriel Valley Airport (KEMT) | Hemet-Ryan Airport (KHMT) | 2026-05-01 17:50 UTC | 2026-05-01 18:26 UTC | 35m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-01 18:04 UTC | 2026-05-01 18:24 UTC | 20m |
| N527BF |  | 6FD7 (6FD7) | Tampa International Airport (KTPA) | 2026-05-01 18:03 UTC | 2026-05-01 18:19 UTC | 16m |
| N493LG |  | CO54 (CO54) | Athanasiou Valley Airport (CO07) | 2026-05-01 17:36 UTC | 2026-05-01 18:19 UTC | 42m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-01 18:02 UTC | 2026-05-01 18:15 UTC | 13m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-01 18:02 UTC | 2026-05-01 18:14 UTC | 12m |
| N65956 |  | Majors Airport (KGVT) | Commerce Municipal Airport (K2F7) | 2026-05-01 17:46 UTC | 2026-05-01 18:13 UTC | 26m |
| N57CJ |  | Leesburg International Airport (KLEE) | Orlando Executive Airport (KORL) | 2026-05-01 17:52 UTC | 2026-05-01 18:09 UTC | 17m |
| N921RA |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-01 17:44 UTC | 2026-05-01 18:07 UTC | 23m |
| N314LM |  | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-05-01 17:41 UTC | 2026-05-01 18:05 UTC | 24m |
| EJA779 | EJA | Fort Lauderdale Executive Airport (KFXE) | Orlando Executive Airport (KORL) | 2026-05-01 17:30 UTC | 2026-05-01 18:05 UTC | 34m |
| EAI62N | EAI | Dublin Airport (EIDW) | Newquay Cornwall Airport (EGHQ) | 2026-05-01 17:04 UTC | 2026-05-01 18:04 UTC | 1h 0m |
| CFXGP | CFX | Reading Regional/Carl A Spaatz Field (KRDG) | Lancaster Airport (KLNS) | 2026-05-01 17:45 UTC | 2026-05-01 17:59 UTC | 14m |
| N118UV |  | Provo Municipal Airport (KPVU) | UT99 (UT99) | 2026-05-01 17:41 UTC | 2026-05-01 17:52 UTC | 11m |
| N17TR |  | Henderson Executive Airport (KHND) | Music Mountain Air Ranch Airport (68AZ) | 2026-05-01 17:38 UTC | 2026-05-01 17:52 UTC | 14m |
| LXJ585 | LXJ | Palm Beach International Airport (KPBI) | Laguardia Airport (KLGA) | 2026-05-01 15:33 UTC | 2026-05-01 17:52 UTC | 2h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
