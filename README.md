# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_21:30:55_UTC-green)

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

**Latest saved flight:** 2026-05-06 21:30:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-06 21:30:55 UTC

- **71,350** saved flights
- **26,547** unique routes
- **127** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **71,350** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **879,261.8 tonnes** estimated CO2 emissions
- **50,971,700 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3081 |
| 2 | SkyWest Airlines | 2659 |
| 3 | IndiGo | 1621 |
| 4 | EJA | 1309 |
| 5 | American Airlines | 1119 |
| 6 | Southwest Airlines | 1035 |
| 7 | Lufthansa | 922 |
| 8 | ENY | 893 |
| 9 | Vueling | 702 |
| 10 | AXM | 679 |
| 11 | LATAM Airlines | 664 |
| 12 | WIF | 611 |
| 13 | Delta Air Lines | 599 |
| 14 | All Nippon Airways | 591 |
| 15 | AZU | 578 |
| 16 | Swiss International | 551 |
| 17 | QLK | 547 |
| 18 | LXJ | 517 |
| 19 | Alaska Airlines | 500 |
| 20 | easyJet | 476 |
| 21 | AEE | 460 |
| 22 | EJU | 459 |
| 23 | VIV | 445 |
| 24 | Cathay Pacific | 437 |
| 25 | Japan Airlines | 421 |
| 26 | Air France | 418 |
| 27 | AXB | 395 |
| 28 | AIQ | 358 |
| 29 | CXK | 354 |
| 30 | GLO | 344 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 56954 |
| 2 | 🇪🇸 ES | 5201 |
| 3 | 🇮🇳 IN | 5091 |
| 4 | 🇦🇺 AU | 4710 |
| 5 | 🇧🇷 BR | 4008 |
| 6 | 🇩🇪 DE | 3977 |
| 7 | 🇮🇹 IT | 3918 |
| 8 | 🇯🇵 JP | 3779 |
| 9 | 🇨🇦 CA | 3540 |
| 10 | 🇬🇧 GB | 3087 |
| 11 | 🇫🇷 FR | 2814 |
| 12 | 🇨🇴 CO | 2673 |
| 13 | 🇲🇽 MX | 2256 |
| 14 | 🇬🇷 GR | 2126 |
| 15 | 🇳🇴 NO | 1964 |
| 16 | 🇨🇭 CH | 1950 |
| 17 | 🇲🇾 MY | 1694 |
| 18 | 🇿🇦 ZA | 1406 |
| 19 | 🇳🇿 NZ | 1307 |
| 20 | 🇹🇭 TH | 1285 |
| 21 | 🇹🇷 TR | 1283 |
| 22 | 🇵🇱 PL | 1189 |
| 23 | 🇵🇭 PH | 1171 |
| 24 | 🇬🇹 GT | 1135 |
| 25 | 🇰🇷 KR | 1130 |
| 26 | 🇲🇦 MA | 853 |
| 27 | 🇲🇴 MO | 826 |
| 28 | 🇲🇪 ME | 767 |
| 29 | 🇳🇱 NL | 743 |
| 30 | 🇧🇸 BS | 605 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1595 |
| 2 | Tokyo International Airport |  | JP | 1275 |
| 3 | Denver International Airport |  | US | 1190 |
| 4 | Indira Gandhi International Airport |  | IN | 1072 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1040 |
| 6 | Frankfurt am Main International Airport |  | DE | 915 |
| 7 | Harry Reid International Airport |  | US | 891 |
| 8 | El Dorado International Airport |  | CO | 878 |
| 9 | Guaymaral Airport |  | CO | 868 |
| 10 | Zurich Airport |  | CH | 848 |
| 11 | La Aurora Airport |  | GT | 845 |
| 12 | Macau International Airport |  | MO | 826 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 718 |
| 14 | Chicago O'Hare International Airport |  | US | 696 |
| 15 | Kuala Lumpur International Airport |  | MY | 679 |
| 16 | Madrid Barajas International Airport |  | ES | 677 |
| 17 | Hartsfield/Jackson Atlanta International Airport |  | US | 638 |
| 18 | Malpensa International Airport |  | IT | 623 |
| 19 | Bengaluru International Airport |  | IN | 616 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 613 |
| 21 | Salt Lake City International Airport |  | US | 577 |
| 22 | Congonhas Airport |  | BR | 569 |
| 23 | Capua Airport |  | IT | 562 |
| 24 | Charlotte/Douglas International Airport |  | US | 560 |
| 25 | Charles de Gaulle International Airport |  | FR | 558 |
| 26 | Tenerife Norte Airport |  | ES | 545 |
| 27 | Ninoy Aquino International Airport |  | PH | 532 |
| 28 | Daniel K Inouye International Airport |  | US | 524 |
| 29 | Netaji Subhash Chandra Bose International Airport |  | IN | 516 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 501 |
| 31 | Barcelona International Airport |  | ES | 498 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 486 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 480 |
| 34 | Vitoria/Foronda Airport |  | ES | 471 |
| 35 | Don Mueang International Airport |  | TH | 453 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 449 |
| 37 | Amsterdam Airport Schiphol |  | NL | 443 |
| 38 | O. R. Tambo International Airport |  | ZA | 442 |
| 39 | Calgary International Airport |  | CA | 425 |
| 40 | Reno/Tahoe International Airport |  | US | 422 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 360 | 26m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 264 | 1h 7m | 706 km | 3,214.2 t |
| 3 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 249 | 21m | 244 km | 1,048.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 210 | 24m | 225 km | 814.7 t |
| 5 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 200 | 28m | 304 km | 1,048.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 198 | 1h 27m | 910 km | 3,107.1 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 178 | 9m | - | - |
| 9 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 174 | 20m | 165 km | 494.9 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 172 | 31m | - | - |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 160 | 26m | 275 km | 758.2 t |
| 12 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 157 | 1h 12m | 770 km | 2,085.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 133 | 21m | 99 km | 227.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 132 | 44m | 452 km | 1,028.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 118 | 31m | 369 km | 751.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 115 | 27m | 152 km | 300.5 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 110 | 20m | 250 km | 475.1 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 108 | 27m | 215 km | 400.0 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 107 | 20m | 147 km | 270.8 t |
| 20 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 101 | 14m | 154 km | 267.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 99 | 1h 2m | 695 km | 1,186.7 t |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 98 | 1h 41m | 1,156 km | 1,955.1 t |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 97 | 58m | 493 km | 825.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 95 | 1h 43m | 1,423 km | 2,331.4 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 93 | 1h 52m | 1,304 km | 2,092.3 t |
| 27 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 92 | 12m | - | - |
| 28 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 92 | 52m | 556 km | 881.9 t |
| 29 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 90 | 23m | 55 km | 85.5 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 89 | 1h 19m | 961 km | 1,475.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N896CA |  | Bowman Field (KLOU) | Clark Regional Airport (KJVY) | 2026-05-06 20:45 UTC | 2026-05-06 21:30 UTC | 45m |
| N172DR |  | Leesburg Executive Airport (KJYO) | Eastern Wv Regional/Shepherd Field (KMRB) | 2026-05-06 21:12 UTC | 2026-05-06 21:30 UTC | 17m |
| CFR88 | CFR | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-05-06 20:38 UTC | 2026-05-06 21:30 UTC | 52m |
| N8439T |  | Ramona Airport (KRNM) | Riverside Airport (KRAL) | 2026-05-06 20:46 UTC | 2026-05-06 21:29 UTC | 43m |
| RFS715 | RFS | Astoria Regional Airport (KAST) | Newport Municipal Airport (KONP) | 2026-05-06 20:13 UTC | 2026-05-06 21:26 UTC | 1h 13m |
| PAT128 | PAT | Cheyenne Regional/Jerry Olson Field (KCYS) | Cheyenne Regional/Jerry Olson Field (KCYS) | 2026-05-06 20:02 UTC | 2026-05-06 21:21 UTC | 1h 18m |
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Macau International Airport (VMMC) | 2026-05-06 17:06 UTC | 2026-05-06 21:20 UTC | 4h 14m |
| AL4 |  | Sydney Bankstown Airport (YSBK) | Wallacia Airport (YWLX) | 2026-05-06 21:07 UTC | 2026-05-06 21:20 UTC | 13m |
| N105BG |  | Monterey Regional Airport (KMRY) | Truckee-Tahoe Airport (KTRK) | 2026-05-06 20:40 UTC | 2026-05-06 21:19 UTC | 39m |
| TEX01 | TEX | RNZAF Base Ohakea (NZOH) | RNZAF Base Ohakea (NZOH) | 2026-05-06 20:16 UTC | 2026-05-06 21:18 UTC | 1h 2m |
| N621HD |  | Orlando Executive Airport (KORL) | St Pete-Clearwater International Airport (KPIE) | 2026-05-06 20:56 UTC | 2026-05-06 21:18 UTC | 21m |
| CPA640 | Cathay Pacific | Tribhuvan International Airport (VNKT) | Zhuhai Airport (ZGSD) | 2026-05-06 17:46 UTC | 2026-05-06 21:15 UTC | 3h 28m |
| N24EB |  | The Eastern Iowa Airport (KCID) | Iowa City Municipal Airport (KIOW) | 2026-05-06 20:56 UTC | 2026-05-06 21:14 UTC | 17m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-05-06 20:55 UTC | 2026-05-06 21:11 UTC | 15m |
| CAP4211 | CAP | Fort Worth Meacham International Airport (KFTW) | Bridgeport Municipal Airport (KXBP) | 2026-05-06 20:32 UTC | 2026-05-06 21:08 UTC | 36m |
| N11285 |  | 46FD (46FD) | Hutson Airfield (8FL0) | 2026-05-06 19:38 UTC | 2026-05-06 21:07 UTC | 1h 29m |
| ES803 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-05-06 20:45 UTC | 2026-05-06 21:07 UTC | 21m |
| XBNLT | XBN | Licenciado Benito Juarez International Airport (MMMX) | Atizapan De Zaragoza Airport (MMJC) | 2026-05-06 20:45 UTC | 2026-05-06 21:05 UTC | 20m |
| N738KA |  | Savannah/Hilton Head International Airport (KSAV) | Wright Army Air Field (Fort Stewart)/Midcoast Regional Airport (KLHW) | 2026-05-06 20:24 UTC | 2026-05-06 21:04 UTC | 40m |
| AIC314 | Air India | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-06 16:49 UTC | 2026-05-06 21:03 UTC | 4h 13m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
