# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_08:41:09_UTC-green)

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

**Latest saved flight:** 2026-05-16 08:41:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 08:41:09 UTC

- **84,350** saved flights
- **30,395** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,350** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,039,344.6 tonnes** estimated CO2 emissions
- **60,251,860 km** total distance flown
- **866 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3605 |
| 2 | SkyWest Airlines | 3127 |
| 3 | IndiGo | 1821 |
| 4 | EJA | 1594 |
| 5 | American Airlines | 1300 |
| 6 | Southwest Airlines | 1238 |
| 7 | Lufthansa | 1071 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 921 |
| 10 | Vueling | 796 |
| 11 | AXM | 764 |
| 12 | LATAM Airlines | 764 |
| 13 | WIF | 727 |
| 14 | AZU | 661 |
| 15 | All Nippon Airways | 657 |
| 16 | Swiss International | 652 |
| 17 | QLK | 620 |
| 18 | LXJ | 619 |
| 19 | Alaska Airlines | 599 |
| 20 | easyJet | 553 |
| 21 | EJU | 537 |
| 22 | AEE | 533 |
| 23 | Cathay Pacific | 529 |
| 24 | VIV | 505 |
| 25 | Air France | 491 |
| 26 | Japan Airlines | 472 |
| 27 | AXB | 448 |
| 28 | CXK | 446 |
| 29 | MXY | 420 |
| 30 | United Airlines | 417 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69185 |
| 2 | 🇪🇸 ES | 5947 |
| 3 | 🇮🇳 IN | 5699 |
| 4 | 🇦🇺 AU | 5408 |
| 5 | 🇩🇪 DE | 4681 |
| 6 | 🇮🇹 IT | 4645 |
| 7 | 🇧🇷 BR | 4643 |
| 8 | 🇯🇵 JP | 4240 |
| 9 | 🇨🇦 CA | 4203 |
| 10 | 🇬🇧 GB | 3585 |
| 11 | 🇫🇷 FR | 3341 |
| 12 | 🇨🇴 CO | 2821 |
| 13 | 🇲🇽 MX | 2566 |
| 14 | 🇬🇷 GR | 2449 |
| 15 | 🇳🇴 NO | 2343 |
| 16 | 🇨🇭 CH | 2223 |
| 17 | 🇲🇾 MY | 1917 |
| 18 | 🇿🇦 ZA | 1580 |
| 19 | 🇹🇷 TR | 1496 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1462 |
| 22 | 🇵🇱 PL | 1398 |
| 23 | 🇵🇭 PH | 1323 |
| 24 | 🇰🇷 KR | 1301 |
| 25 | 🇬🇹 GT | 1272 |
| 26 | 🇲🇦 MA | 978 |
| 27 | 🇲🇴 MO | 972 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 861 |
| 30 | 🇭🇷 HR | 754 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1849 |
| 2 | Denver International Airport |  | US | 1419 |
| 3 | Tokyo International Airport |  | JP | 1419 |
| 4 | Indira Gandhi International Airport |  | IN | 1212 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1185 |
| 6 | Frankfurt am Main International Airport |  | DE | 1084 |
| 7 | Harry Reid International Airport |  | US | 1060 |
| 8 | Zurich Airport |  | CH | 998 |
| 9 | Macau International Airport |  | MO | 972 |
| 10 | La Aurora Airport |  | GT | 965 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 909 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 850 |
| 15 | Chicago O'Hare International Airport |  | US | 816 |
| 16 | Madrid Barajas International Airport |  | ES | 768 |
| 17 | Kuala Lumpur International Airport |  | MY | 761 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 728 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 706 |
| 20 | Salt Lake City International Airport |  | US | 704 |
| 21 | Malpensa International Airport |  | IT | 704 |
| 22 | Bengaluru International Airport |  | IN | 698 |
| 23 | Capua Airport |  | IT | 686 |
| 24 | Charles de Gaulle International Airport |  | FR | 657 |
| 25 | Charlotte/Douglas International Airport |  | US | 656 |
| 26 | Congonhas Airport |  | BR | 656 |
| 27 | Daniel K Inouye International Airport |  | US | 615 |
| 28 | Tenerife Norte Airport |  | ES | 606 |
| 29 | Ninoy Aquino International Airport |  | PH | 605 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 593 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 570 |
| 32 | Barcelona International Airport |  | ES | 563 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 562 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 540 |
| 35 | Vitoria/Foronda Airport |  | ES | 532 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 530 |
| 37 | Don Mueang International Airport |  | TH | 528 |
| 38 | Amsterdam Airport Schiphol |  | NL | 522 |
| 39 | O. R. Tambo International Airport |  | ZA | 497 |
| 40 | Calgary International Airport |  | CA | 494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 312 | 21m | 244 km | 1,313.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 274 | 1h 8m | 706 km | 3,336.0 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 223 | 28m | 304 km | 1,169.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 217 | 14m | 114 km | 425.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 191 | 1h 11m | 770 km | 2,537.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 190 | 19m | 165 km | 540.5 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 176 | 26m | 275 km | 834.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 143 | 20m | 99 km | 244.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 131 | 31m | 369 km | 833.8 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 121 | 14m | 154 km | 320.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-05-16 08:30 UTC | 2026-05-16 08:41 UTC | 11m |
| SHAHD272 | SHA | Amman-Marka International Airport (OJAM) | Amman-Marka International Airport (OJAM) | 2026-05-16 08:16 UTC | 2026-05-16 08:27 UTC | 10m |
| THY70 | Turkish Airlines | Yalova Airport (LTBP) | Macau International Airport (VMMC) | 2026-05-15 22:59 UTC | 2026-05-16 08:13 UTC | 9h 14m |
| FGDTJ | FGD | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-05-16 08:07 UTC | 2026-05-16 08:13 UTC | 6m |
| CLX4755 | CLX | Luxembourg-Findel International Airport (ELLX) | Macau International Airport (VMMC) | 2026-05-15 21:11 UTC | 2026-05-16 08:07 UTC | 10h 55m |
| TMN26 | TMN | Chek Lap Kok International Airport (VHHH) | Sydney Kingsford Smith International Airport (YSSY) | 2026-05-15 23:33 UTC | 2026-05-16 08:03 UTC | 8h 29m |
| DFLOC | DFL | Bomoen Airport (ENBM) | Bomoen Airport (ENBM) | 2026-05-16 07:25 UTC | 2026-05-16 07:58 UTC | 32m |
| AFR38SN | Air France | Charles de Gaulle International Airport (LFPG) | Zurich Airport (LSZH) | 2026-05-16 07:00 UTC | 2026-05-16 07:58 UTC | 57m |
| SWR138 | Swiss International | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-05-15 20:54 UTC | 2026-05-16 07:54 UTC | 11h 0m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-05-16 06:59 UTC | 2026-05-16 07:53 UTC | 53m |
| FGOBR | FGO | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | Orleans-Saint-Denis-de-l'Hotel Airport (LFOZ) | 2026-05-16 07:41 UTC | 2026-05-16 07:51 UTC | 10m |
| IGO2571 | IndiGo | Hindon Airport (VIDX) | VIBN (VIBN) | 2026-05-16 07:00 UTC | 2026-05-16 07:48 UTC | 48m |
| KAL092 | Korean Air | General Edward Lawrence Logan International Airport (KBOS) | Incheon International Airport (RKSI) | 2026-05-15 17:28 UTC | 2026-05-16 07:48 UTC | 14h 19m |
| UAE9386 | Emirates | Liege Airport (EBLG) | Macau International Airport (VMMC) | 2026-05-15 17:17 UTC | 2026-05-16 07:48 UTC | 14h 30m |
| RYR340F | Ryanair | Brussels South Charleroi Airport (EBCI) | Suceava Stefan cel Mare Airport (LRSV) | 2026-05-16 05:46 UTC | 2026-05-16 07:47 UTC | 2h 0m |
| EJU4787 | EJU | Nantes Atlantique Airport (LFRS) | Kenitra Airport (GMMY) | 2026-05-16 05:52 UTC | 2026-05-16 07:46 UTC | 1h 54m |
| SEH2JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Mikonos Airport (LGMK) | 2026-05-16 07:20 UTC | 2026-05-16 07:46 UTC | 25m |
| SWR41D | Swiss International | Frankfurt am Main International Airport (EDDF) | Zurich Airport (LSZH) | 2026-05-16 07:12 UTC | 2026-05-16 07:44 UTC | 32m |
| SHAHD272 | SHA | Amman-Marka International Airport (OJAM) | Queen Alia International Airport (OJAI) | 2026-05-16 06:55 UTC | 2026-05-16 07:44 UTC | 48m |
| RYR74SV | Ryanair | Luqa Airport (LMML) | Livno Brda Bosni Airport (LQLV) | 2026-05-16 06:24 UTC | 2026-05-16 07:42 UTC | 1h 18m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
